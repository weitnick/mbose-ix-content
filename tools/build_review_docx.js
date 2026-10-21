// Turn a chapter content Markdown file into a formatted Word document for review.
// Usage: node build_review_docx.js <chapter.md> <out.docx> ["<review date>"]
const fs = require("fs");
const path = require("path");
const MarkdownIt = require("markdown-it");
const { convert: latexToMath, latexToPlain } = require("./math_docx");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, LevelFormat, Header, Footer,
  PageNumber, TabStopType, TableLayoutType, Bookmark, InternalHyperlink, Math: OMath, ImageRun,
} = require("docx");

const [, , srcPath, outPath, reviewDate = ""] = process.argv;
if (!srcPath || !outPath) {
  console.error("Usage: node build_review_docx.js <chapter.md> <out.docx> [\"<review date>\"]");
  process.exit(1);
}

// ---- Page geometry and palette -------------------------------------------------------------
const PAGE_W = 11906; // A4 width in DXA
const MARGIN_X = 1077; // ~1.9 cm
const CONTENT_W = PAGE_W - 2 * MARGIN_X;
const C = {
  ink: "1D2733", muted: "5D6B7A", accent: "1F4E79", accentSoft: "E9F0F7", rule: "CFD8E3",
  ans: "2E7D32", ansBg: "EEF7EF", expBg: "F4F6F8", expRule: "9AA7B4", expInk: "334155",
  quote: "B7791F", quoteBg: "FDF7EA", tagA: "1F4E79", tagR: "7C3AED", header: "7A8594",
  statusBg: "FFF3D6", statusInk: "8A5A00", zebra: "FAFBFC",
};
const FONT = "Calibri";
const HEAD_FONT = "Georgia";
const CODE_FONT = "Consolas";

// ---- Split the cover block from the numbered sections ------------------------------------
const text = fs.readFileSync(srcPath, "utf8").replace(/\r\n/g, "\n");
const firstH2 = text.indexOf("\n## ");
let coverMd = text.slice(0, firstH2);
const bodyMd = text.slice(firstH2);
const title = (coverMd.match(/^# (.+)$/m) || [, "Chapter"])[1].trim();
coverMd = coverMd.replace(/^# .+\n/m, "").trim().replace(/\n---\s*$/, "");

const meta = {};
for (const m of coverMd.matchAll(/^\|(.+)\|\s*$/gm)) {
  const cells = m[1].split("|").map((s) => s.trim());
  if (cells.length === 2 && !/^[-: ]+$/.test(cells[0])) meta[cells[0]] = cells[1].replace(/[*_]/g, "");
}
const chapter = meta["Chapter"] || "";
const unitLabel = /^\d+$/.test(chapter) ? `Chapter ${chapter}` : chapter; // e.g. "Poem 1"
const band = [(meta["Board"] || "MBOSE").split(" ")[0], `Class ${meta["Class"] || ""}`, meta["Subject"] || "", unitLabel].join("  ·  ");
const subtitle = meta["Part I"]
  ? `Prose · Part I: ${meta["Part I"].split(" (by")[0]} · Part II: ${meta["Part II"] || ""}`
  : [meta["Genre"], meta["Author"] && !/^Not named/.test(meta["Author"]) ? `by ${meta["Author"]}` : "",
    meta["Exam weightage"] ? `Exam weightage: ${meta["Exam weightage"]}` : ""].filter(Boolean).join(" · ");

const md = new MarkdownIt("commonmark", { breaks: true, html: false }).enable("table");

// $...$ (inline) and $$...$$ (display) maths, written in LaTeX. Parsed before escapes and emphasis,
// so underscores and asterisks inside an equation are left alone.
md.inline.ruler.before("escape", "math_inline", (state, silent) => {
  const src = state.src, start = state.pos;
  if (src[start] !== "$") return false;
  const display = src[start + 1] === "$";
  const open = display ? 2 : 1;
  let end = start + open;
  while (end < state.posMax) {
    if (src[end] === "\\") { end += 2; continue; }
    if (src[end] === "$" && (!display || src[end + 1] === "$")) break;
    end++;
  }
  if (end >= state.posMax) return false;
  const content = src.slice(start + open, end);
  if (!content.trim()) return false;
  if (!silent) {
    const tok = state.push("math_inline", "math", 0);
    tok.content = content;
    tok.meta = { display };
  }
  state.pos = end + open;
  return true;
});

// ---- Inline handling ----------------------------------------------------------------------
// Returns an array of lines; each line is an array of {text, bold, italics}.
function inlineLines(inlineToken) {
  const lines = [[]];
  let bold = false, italics = false;
  for (const t of inlineToken.children || []) {
    if (t.type === "strong_open") bold = true;
    else if (t.type === "strong_close") bold = false;
    else if (t.type === "em_open") italics = true;
    else if (t.type === "em_close") italics = false;
    else if (t.type === "softbreak" || t.type === "hardbreak") lines.push([]);
    else if (t.type === "text" || t.type === "code_inline") {
      if (t.content) lines[lines.length - 1].push({ text: t.content, bold, italics, code: t.type === "code_inline" });
    } else if (t.type === "math_inline") {
      lines[lines.length - 1].push({ text: latexToPlain(t.content), math: t.content, display: t.meta.display, bold, italics });
    } else if (t.type === "image") {
      lines[lines.length - 1].push({ text: t.content || "", image: t.attrGet("src") });
    }
  }
  return lines.filter((l) => l.length);
}
const plain = (segs) => segs.map((s) => s.text).join("");

function runs(segs, opts = {}) {
  return segs.map((s) => (s.math ? new OMath({ children: latexToMath(s.math) }) : new TextRun({
    text: s.text, bold: s.bold || opts.bold, italics: s.italics, font: s.code ? CODE_FONT : opts.font || FONT,
    size: s.code && opts.size ? opts.size - 1 : opts.size, color: opts.color,
  })));
}

// Figures: ![caption](figures/name.png). PNGs are drawn at FIG_DPI, so their printed size follows the pixels.
const FIG_DPI = 200;
const MAX_FIG_PX = Math.floor((CONTENT_W / 1440) * 96);
function imageParagraphs(seg) {
  const file = path.resolve(path.dirname(srcPath), seg.image);
  const data = fs.readFileSync(file);
  const w = data.readUInt32BE(16), h = data.readUInt32BE(20);
  let dw = Math.round((w * 96) / FIG_DPI), dh = Math.round((h * 96) / FIG_DPI);
  if (dw > MAX_FIG_PX) { dh = Math.round((dh * MAX_FIG_PX) / dw); dw = MAX_FIG_PX; }
  const out = [P({ alignment: AlignmentType.CENTER, keepNext: !!seg.text, spacing: { before: 120, after: 40 },
    children: [new ImageRun({ type: "png", data, transformation: { width: dw, height: dh } })] })];
  if (seg.text) out.push(P({ alignment: AlignmentType.CENTER, spacing: { after: 160 },
    children: [new TextRun({ text: seg.text, italics: true, size: 18, color: C.muted, font: FONT })] }));
  return out;
}

// ---- Paragraph builders -------------------------------------------------------------------
const P = (o) => new Paragraph({ spacing: { after: 100, line: 276 }, ...o });

const BOX = {
  answer: { shading: { type: ShadingType.CLEAR, fill: C.ansBg, color: "auto" },
    border: { left: { style: BorderStyle.SINGLE, size: 18, color: C.ans, space: 6 } }, indent: { left: 120, right: 60 } },
  explanation: { shading: { type: ShadingType.CLEAR, fill: C.expBg, color: "auto" },
    border: { left: { style: BorderStyle.SINGLE, size: 18, color: C.expRule, space: 6 } }, indent: { left: 120, right: 60 } },
};
const ANSWER_LABEL = /^(Answer:|Model answer:|Solution:)$/;

// An answer box that holds a display equation is drawn as a one-cell table: Word ignores paragraph
// borders and indents for a line that holds only an equation, but a table cell keeps it inside the box.
function boxTable(kind, boxLines) {
  const ans = kind === "answer";
  const width = CONTENT_W - 180;
  const paras = boxLines.map((segs, idx) => {
    const displayOnly = segs.length === 1 && segs[0].math && segs[0].display;
    const children = idx === 0
      ? [new TextRun({ text: segs[0].text, bold: true, color: ans ? C.ans : C.expInk, font: FONT, size: ans ? undefined : 19 }),
        ...runs(segs.slice(1), { size: ans ? undefined : 19, color: ans ? undefined : C.expInk })]
      : runs(segs, { size: ans ? undefined : 19, color: ans ? undefined : C.expInk });
    return new Paragraph({ children, alignment: displayOnly ? AlignmentType.CENTER : undefined,
      spacing: { before: displayOnly ? 40 : 0, after: displayOnly ? 60 : 30, line: 264 } });
  });
  return [new Table({
    width: { size: width, type: WidthType.DXA }, columnWidths: [width], layout: TableLayoutType.FIXED,
    indent: { size: 120, type: WidthType.DXA }, borders: noBordersTable,
    rows: [new TableRow({ cantSplit: boxLines.length <= 12, children: [new TableCell({
      width: { size: width, type: WidthType.DXA }, children: paras,
      shading: { type: ShadingType.CLEAR, fill: ans ? C.ansBg : C.expBg, color: "auto" },
      borders: { top: nb, bottom: nb, right: nb, left: { style: BorderStyle.SINGLE, size: 18, color: ans ? C.ans : C.expRule } },
      margins: { top: 60, bottom: 60, left: 140, right: 100 },
    })] })],
  }), new Paragraph({ spacing: { after: ans ? 60 : 120 }, children: [] })];
}

function styledLine(segs, ctx) {
  const first = segs[0] || { text: "" };
  const label = first.bold ? first.text.trim() : "";
  const size = ctx.size;

  if (segs.length === 1 && first.image) return imageParagraphs(first);
  const displayOnly = segs.length === 1 && first.math && first.display;
  if (ctx.box && !ANSWER_LABEL.test(label) && label !== "Explanation:") {
    // A further line of working inside an answer or explanation box.
    const exp = ctx.box === "explanation";
    return P({ children: runs(segs, { size: exp ? 19 : size, color: exp ? C.expInk : undefined }),
      ...BOX[ctx.box], alignment: displayOnly ? AlignmentType.CENTER : undefined,
      spacing: { before: 0, after: ctx.lastInBox ? 140 : 20, line: 264 }, keepNext: !ctx.lastInBox, keepLines: true });
  }
  if (displayOnly) return P({ alignment: AlignmentType.CENTER, children: runs(segs), spacing: { before: 60, after: 120 } });

  if (ANSWER_LABEL.test(label)) {
    return P({
      children: [new TextRun({ text: first.text, bold: true, color: C.ans, font: FONT, size }), ...runs(segs.slice(1), { size })],
      shading: { type: ShadingType.CLEAR, fill: C.ansBg, color: "auto" },
      border: { left: { style: BorderStyle.SINGLE, size: 18, color: C.ans, space: 6 } },
      indent: { left: 120, right: 60 }, spacing: { before: 40, after: ctx.lastInBox === false ? 20 : 40, line: 264 }, keepLines: true,
      keepNext: ctx.lastInBox === false,
    });
  }
  if (label === "Explanation:") {
    return P({
      children: [new TextRun({ text: first.text, bold: true, color: C.expInk, font: FONT, size: 19 }), ...runs(segs.slice(1), { size: 19, color: C.expInk })],
      shading: { type: ShadingType.CLEAR, fill: C.expBg, color: "auto" },
      border: { left: { style: BorderStyle.SINGLE, size: 18, color: C.expRule, space: 6 } },
      indent: { left: 120, right: 60 }, spacing: { before: 0, after: 140, line: 264 }, keepLines: true,
    });
  }
  if (label === "A:" || label === "R:") {
    const fill = label === "A:" ? C.tagA : C.tagR;
    return P({
      children: [
        new TextRun({ text: ` ${label[0]} `, bold: true, color: "FFFFFF", font: FONT, size: 17, shading: { type: ShadingType.CLEAR, fill, color: "auto" } }),
        new TextRun({ text: " ", font: FONT }),
        ...runs(segs.slice(1).map((s, i) => (i === 0 ? { ...s, text: s.text.replace(/^\s+/, "") } : s)), { size }),
      ],
      spacing: { after: 40, line: 264 }, keepNext: true,
    });
  }
  if (/^(Q\d+\.|\d+\.|\([ivx]+\)|Example \d+\.)$/.test(label)) {
    return P({
      children: [new TextRun({ text: first.text, bold: true, color: C.accent, font: FONT, size }), ...runs(segs.slice(1), { size })],
      spacing: { before: 200, after: 60, line: 264 }, keepNext: ctx.attachNext !== false, keepLines: true,
    });
  }
  return P({ children: runs(segs, { size }), ...ctx.para });
}

// ---- Tables -------------------------------------------------------------------------------
const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: C.rule };
function buildTable(rows, opts = {}) {
  // rows: [{header: bool, cells: [segs lines]}]
  const nCols = Math.max(...rows.map((r) => r.cells.length));
  const weight = Array(nCols).fill(6);
  for (const r of rows) r.cells.forEach((lines, i) => {
    const len = Math.max(...lines.map((l) => plain(l).length), 1);
    // Header text is bold and needs cell padding, so give it a little extra room ("Marks" broke as "Mar ks").
    weight[i] = Math.max(weight[i], Math.min(r.header ? len + 3 : len, r.header ? 18 : 70));
  });
  // Amount columns (ledgers, balance sheets) hold short figures beside long particulars; give them room for the
  // longest figure in bold, or Word wraps "2,16,000" as "2,16, 000" (Accountancy, 17 Oct 2026).
  const AMOUNT = /^[(\-−]?\s*₹?\s*\d[\d,]*(\.\d+)?\)?(\s*(Dr|Cr)\.?)?$/;
  for (let i = 0; i < nCols; i++) {
    const body = rows.filter((r) => !r.header).map((r) => (r.cells[i] || []).map((l) => plain(l)).join(" ").trim())
      .filter((t) => t && t !== "—" && t !== "–");
    const nums = body.filter((t) => AMOUNT.test(t.replace(/\*/g, "")));
    if (body.length && nums.length / body.length >= 0.6) {
      const longest = Math.max(...nums.map((t) => t.replace(/\*/g, "").length));
      weight[i] = Math.max(weight[i], longest + 5);
    }
  }
  const total = weight.reduce((a, b) => a + b, 0);
  const width = opts.width || CONTENT_W;
  const widths = weight.map((w) => Math.floor((w / total) * width));
  widths[widths.length - 1] += width - widths.reduce((a, b) => a + b, 0);

  const trows = rows.map((r, ri) => new TableRow({
    tableHeader: r.header, cantSplit: true,
    children: Array.from({ length: nCols }, (_, ci) => {
      const lines = r.cells[ci] || [[{ text: "" }]];
      return new TableCell({
        width: { size: widths[ci], type: WidthType.DXA },
        shading: r.header ? { type: ShadingType.CLEAR, fill: C.accentSoft, color: "auto" }
          : (ri % 2 === 0 && !opts.plain ? { type: ShadingType.CLEAR, fill: C.zebra, color: "auto" } : undefined),
        margins: { top: 50, bottom: 50, left: 100, right: 100 },
        borders: opts.plain ? noBorders : undefined,
        children: (lines.length ? lines : [[{ text: "" }]]).map((segs) => new Paragraph({
          spacing: { after: 0, line: 252 },
          children: r.header ? runs(segs, { bold: true, color: C.accent, size: 18 }) : runs(segs, { size: 18 }),
        })),
      });
    }),
  }));
  return new Table({
    width: { size: width, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED, rows: trows,
    borders: opts.plain ? noBordersTable : {
      top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder,
      insideHorizontal: cellBorder, insideVertical: cellBorder,
    },
  });
}
const nb = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: nb, bottom: nb, left: nb, right: nb };
const noBordersTable = { top: nb, bottom: nb, left: nb, right: nb, insideHorizontal: nb, insideVertical: nb };

// ---- Token walker -------------------------------------------------------------------------
let listInstance = 0;
const toc = [];

function render(tokens) {
  const out = [];
  const listStack = []; // {type: 'bullet'|'ordered'|'options', instance}
  let quote = 0;

  for (let i = 0; i < tokens.length; i++) {
    const t = tokens[i];
    switch (t.type) {
      case "heading_open": {
        const inline = tokens[i + 1];
        const segs = inlineLines(inline).flat();
        const textStr = plain(segs);
        const level = Number(t.tag.slice(1));
        if (level === 2) {
          const id = `sec${toc.length + 1}`;
          toc.push({ id, text: textStr });
          out.push(new Paragraph({
            heading: HeadingLevel.HEADING_1, pageBreakBefore: true,
            shading: { type: ShadingType.CLEAR, fill: C.accent, color: "auto" },
            spacing: { before: 0, after: 240 }, indent: { left: 0 },
            children: [new Bookmark({ id, children: [new TextRun({ text: ` ${textStr}`, font: HEAD_FONT, size: 36, bold: true, color: "FFFFFF" })] })],
          }));
        } else if (level === 3) {
          out.push(new Paragraph({
            heading: HeadingLevel.HEADING_2, keepNext: true,
            spacing: { before: 280, after: 120 },
            border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: C.rule, space: 2 } },
            children: runs(segs, { bold: true, color: C.accent, size: 26 }),
          }));
        } else {
          out.push(new Paragraph({
            heading: HeadingLevel.HEADING_3, keepNext: true, spacing: { before: 200, after: 80 },
            children: runs(segs, { bold: true, color: C.ink, size: 23 }),
          }));
        }
        i += 2;
        break;
      }
      case "bullet_list_open":
      case "ordered_list_open": {
        // MCQ option lists (first item starts with "(a)") are shown without bullets.
        let k = i + 1;
        while (k < tokens.length && tokens[k].type !== "inline") k++;
        const isOptions = t.type === "bullet_list_open" && /^\(a\)/.test(tokens[k]?.content || "");
        listStack.push({ type: isOptions ? "options" : t.type === "ordered_list_open" ? "ordered" : "bullet", instance: ++listInstance });
        break;
      }
      case "bullet_list_close":
      case "ordered_list_close":
        listStack.pop();
        break;
      case "blockquote_open": quote++; break;
      case "blockquote_close": quote--; break;
      case "fence":
      case "code_block": {
        // Program listings: monospace, shaded, kept on one page when short; leading spaces are kept.
        const codeLines = t.content.replace(/\t/g, "    ").replace(/\n$/, "").split("\n");
        const keep = codeLines.length <= 40;
        codeLines.forEach((ln, li) => {
          const last = li === codeLines.length - 1;
          out.push(new Paragraph({
            children: [new TextRun({ text: ln.length ? ln : " ", font: CODE_FONT, size: 18, color: C.ink })],
            shading: { type: ShadingType.CLEAR, fill: "F3F5F8", color: "auto" },
            border: { left: { style: BorderStyle.SINGLE, size: 18, color: C.rule, space: 6 } },
            indent: { left: 200, right: 60 },
            spacing: { before: li === 0 ? 60 : 0, after: last ? 140 : 0, line: 240 },
            keepNext: keep && !last, keepLines: true,
          }));
        });
        break;
      }
      case "table_open": {
        const rows = [];
        let row = null, header = false;
        for (i = i + 1; tokens[i].type !== "table_close"; i++) {
          const u = tokens[i];
          if (u.type === "thead_open") header = true;
          else if (u.type === "thead_close") header = false;
          else if (u.type === "tr_open") row = { header, cells: [] };
          else if (u.type === "tr_close") rows.push(row);
          else if (u.type === "inline") row.cells.push(inlineLines(u));
        }
        out.push(buildTable(rows));
        out.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
        break;
      }
      case "inline": {
        const lines = inlineLines(t);
        const list = listStack[listStack.length - 1];
        if (list) {
          const depth = listStack.filter((l) => l.type !== "options").length - 1;
          lines.forEach((segs, li) => {
            if (list.type === "options") {
              // Keep the options with their question, but let the last option end the chain so a run of
              // test questions without answer boxes can still break across pages.
              let k = i + 1;
              while (k < tokens.length && !["list_item_open", "bullet_list_close"].includes(tokens[k].type)) k++;
              const lastOption = tokens[k]?.type === "bullet_list_close";
              out.push(P({ children: runs(segs, { size: 21 }), indent: { left: 420 }, spacing: { after: 30, line: 264 }, keepNext: !lastOption || !!tokens[k + 1] && /Answer/.test(tokens[k + 2]?.content || "") }));
            } else if (li === 0) {
              out.push(P({
                children: runs(segs), spacing: { after: 60, line: 264 },
                numbering: { reference: list.type === "ordered" ? "numbers" : "bullets", level: Math.max(depth, 0), instance: list.instance },
              }));
            } else {
              out.push(...[styledLine(segs, { para: { indent: { left: 720 } } })].flat());
            }
          });
        } else if (quote) {
          // Each paragraph inside a quote (e.g. a stanza) gets space after its last line.
          lines.forEach((segs, li) => out.push(P({
            children: runs(segs), shading: { type: ShadingType.CLEAR, fill: C.quoteBg, color: "auto" },
            border: { left: { style: BorderStyle.SINGLE, size: 24, color: C.quote, space: 8 } },
            indent: { left: 160, right: 80 },
            spacing: { after: li === lines.length - 1 ? 180 : 20, line: 276 },
          })));
        } else {
          // A question keeps with what belongs to it (its answer, options, extract or table), not with the
          // next question, so a run of unanswered test questions can flow across pages.
          const isAnswerLabel = (l) => l && l[0] && l[0].bold && /^(Answer:|Model answer:|Solution:|Explanation:)$/.test(l[0].text.trim());
          let k = i + 1;
          while (k < tokens.length && tokens[k].type === "paragraph_close") k++;
          const nt = tokens[k];
          const nextBlockAttached = !!nt && (["bullet_list_open", "ordered_list_open", "blockquote_open", "table_open", "fence", "code_block"].includes(nt.type)
            || (nt.type === "paragraph_open" && /^\*\*(Answer|Model answer|Solution):\*\*/.test(tokens[k + 1]?.content || "")));
          // Lines that follow an Answer/Solution/Explanation label in the same paragraph stay inside its box.
          // Split the paragraph's lines into chunks, one per label (lines before the first label are plain).
          const chunks = [];
          lines.forEach((segs) => {
            const lab = segs[0] && segs[0].bold ? segs[0].text.trim() : "";
            const kind = ANSWER_LABEL.test(lab) ? "answer" : lab === "Explanation:" ? "explanation" : null;
            if (kind || !chunks.length) chunks.push({ box: kind, lines: [] });
            chunks[chunks.length - 1].lines.push(segs);
          });
          chunks.forEach((ch, ci) => {
            const hasDisplay = ch.lines.some((l) => l.length === 1 && l[0].math && l[0].display);
            if (ch.box && hasDisplay) { out.push(...boxTable(ch.box, ch.lines)); return; }
            ch.lines.forEach((segs, li) => {
              const lastLine = li === ch.lines.length - 1;
              // A question or example written over several lines stays on the page with its answer box.
              const keepWithBox = !ch.box && ci < chunks.length - 1;
              const made = styledLine(segs, {
                para: keepWithBox ? { keepNext: true, keepLines: true } : {},
                attachNext: !lastLine ? !!ch.box || keepWithBox : ci < chunks.length - 1 ? true : nextBlockAttached,
                box: ch.box && li > 0 ? ch.box : null, lastInBox: ch.box ? lastLine : undefined,
              });
              out.push(...(Array.isArray(made) ? made : [made]));
            });
          });
        }
        break;
      }
      default:
        break;
    }
  }
  return out;
}

const bodyChildren = render(md.parse(bodyMd, {}));
const coverTokens = md.parse(coverMd, {});

// ---- Cover page ---------------------------------------------------------------------------
const cover = [
  new Paragraph({
    spacing: { after: 600 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: C.accent, space: 4 } },
    children: [new TextRun({ text: band.toUpperCase(), bold: true, color: C.accent, size: 18, font: FONT, characterSpacing: 40 })],
  }),
  new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: title, font: HEAD_FONT, bold: true, size: 64, color: C.accent })] }),
  new Paragraph({ spacing: { after: 280 }, children: [new TextRun({ text: subtitle, size: 25, color: C.muted, font: FONT })] }),
  new Paragraph({
    spacing: { after: 320 },
    children: [new TextRun({
      text: ` CONTENT REVIEW DRAFT${reviewDate ? " · " + reviewDate.toUpperCase() : ""} `, bold: true, size: 17, color: C.statusInk, font: FONT,
      shading: { type: ShadingType.CLEAR, fill: C.statusBg, color: "auto" },
    })],
  }),
  ...render(coverTokens),
  new Paragraph({
    spacing: { before: 280, after: 100 },
    children: [new TextRun({ text: "CONTENTS", bold: true, color: C.accent, size: 20, font: FONT, characterSpacing: 30 })],
  }),
];
// Two-column contents list with links to each section.
const half = Math.ceil(toc.length / 2);
const tocCell = (entry) => {
  if (!entry) return [new Paragraph({ children: [] })];
  const [num, ...rest] = entry.text.split(". ");
  return [new Paragraph({
    spacing: { after: 40 },
    border: { bottom: { style: BorderStyle.DOTTED, size: 4, color: C.rule, space: 2 } },
    children: [new InternalHyperlink({
      anchor: entry.id,
      children: [
        new TextRun({ text: `${num}   `, bold: true, color: C.accent, size: 19, font: FONT }),
        new TextRun({ text: rest.join(". "), color: C.ink, size: 19, font: FONT }),
      ],
    })],
  })];
};
const colW = Math.floor(CONTENT_W / 2);
cover.push(new Table({
  width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [colW, CONTENT_W - colW], layout: TableLayoutType.FIXED,
  borders: noBordersTable,
  rows: Array.from({ length: half }, (_, r) => new TableRow({
    children: [toc[r], toc[r + half]].map((e, ci) => new TableCell({
      width: { size: ci ? CONTENT_W - colW : colW, type: WidthType.DXA }, borders: noBorders,
      margins: { top: 20, bottom: 20, left: ci ? 240 : 0, right: ci ? 0 : 240 }, children: tocCell(e),
    })),
  })),
}));

// ---- Document -----------------------------------------------------------------------------
const headerLeft = `${title} — ${unitLabel}`;
const headerRight = `${(meta["Board"] || "MBOSE").split(" ")[0]} · Class ${meta["Class"] || ""} · ${meta["Subject"] || ""}`;
const small = { size: 16, color: C.header, font: FONT };

const doc = new Document({
  creator: "Core9X content",
  title: `${title} — Content Review`,
  styles: {
    default: { document: { run: { font: FONT, size: 21, color: C.ink } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: HEAD_FONT, size: 36, bold: true, color: "FFFFFF" }, paragraph: { outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: FONT, size: 26, bold: true, color: C.accent }, paragraph: { outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: FONT, size: 23, bold: true, color: C.ink }, paragraph: { outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets", levels: [0, 1, 2].map((l) => ({
        level: l, format: LevelFormat.BULLET, text: ["•", "◦", "▪"][l], alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 400 + 360 * l, hanging: 260 } } },
      })) },
      { reference: "numbers", levels: [0, 1, 2].map((l) => ({
        level: l, format: LevelFormat.DECIMAL, text: `%${l + 1}.`, alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 440 + 360 * l, hanging: 320 } } },
      })) },
    ],
  },
  sections: [{
    properties: {
      titlePage: true,
      page: { margin: { top: 1134, bottom: 1134, left: MARGIN_X, right: MARGIN_X, header: 567, footer: 567 } },
    },
    headers: {
      first: new Header({ children: [new Paragraph({ children: [] })] }),
      default: new Header({ children: [new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C.rule, space: 4 } },
        children: [new TextRun({ text: headerLeft, ...small }), new TextRun({ text: `\t${headerRight}`, ...small })],
      })] }),
    },
    footers: {
      first: new Footer({ children: [new Paragraph({ children: [] })] }),
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: ["Page ", PageNumber.CURRENT, " of ", PageNumber.TOTAL_PAGES], ...small })],
      })] }),
    },
    children: [...cover, ...bodyChildren],
  }],
});

// Word lays out an equation that sits alone on its line ("display" maths) using the document's
// equation margins rather than the paragraph indent, so set those margins to match the answer boxes.
const MATH_PR = '<m:mathPr><m:mathFont m:val="Cambria Math"/><m:brkBin m:val="before"/><m:brkBinSub m:val="--"/>'
  + '<m:smallFrac m:val="0"/><m:dispDef/><m:lMargin m:val="120"/><m:rMargin m:val="60"/><m:defJc m:val="centerGroup"/>'
  + '<m:wrapIndent m:val="1440"/><m:intLim m:val="subSup"/><m:naryLim m:val="undOvr"/></m:mathPr>';
async function withMathSettings(buf) {
  const JSZip = require("jszip");
  const zip = await JSZip.loadAsync(buf);
  const settings = await zip.file("word/settings.xml").async("string");
  if (!settings.includes("<m:mathPr>")) zip.file("word/settings.xml", settings.replace("</w:compat>", "</w:compat>" + MATH_PR));
  return zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" });
}

Packer.toBuffer(doc).then(withMathSettings).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log(`wrote ${outPath} (${(buf.length / 1024).toFixed(0)} KB, ${toc.length} sections)`);
});
