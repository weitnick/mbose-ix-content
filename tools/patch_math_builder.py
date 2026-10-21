"""One-off patch: add maths ($...$), figures and multi-line answer boxes to build_review_docx.js."""
p = "build_review_docx.js"
s = open(p, encoding="utf-8").read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b)


rep('''const fs = require("fs");
const MarkdownIt = require("markdown-it");''', '''const fs = require("fs");
const path = require("path");
const MarkdownIt = require("markdown-it");
const { convert: latexToMath, latexToPlain } = require("./math_docx");''')

rep('PageNumber, TabStopType, TableLayoutType, Bookmark, InternalHyperlink,\n} = require("docx");',
    'PageNumber, TabStopType, TableLayoutType, Bookmark, InternalHyperlink, Math: OMath, ImageRun,\n} = require("docx");')

rep('''const md = new MarkdownIt("commonmark", { breaks: true, html: false }).enable("table");
''', r'''const md = new MarkdownIt("commonmark", { breaks: true, html: false }).enable("table");

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
''')

rep('''    else if (t.type === "text" || t.type === "code_inline") {
      if (t.content) lines[lines.length - 1].push({ text: t.content, bold, italics });
    }''', '''    else if (t.type === "text" || t.type === "code_inline") {
      if (t.content) lines[lines.length - 1].push({ text: t.content, bold, italics });
    } else if (t.type === "math_inline") {
      lines[lines.length - 1].push({ text: latexToPlain(t.content), math: t.content, display: t.meta.display, bold, italics });
    } else if (t.type === "image") {
      lines[lines.length - 1].push({ text: t.content || "", image: t.attrGet("src") });
    }''')

rep('''function runs(segs, opts = {}) {
  return segs.map((s) => new TextRun({
    text: s.text, bold: s.bold || opts.bold, italics: s.italics, font: opts.font || FONT,
    size: opts.size, color: opts.color,
  }));
}''', '''function runs(segs, opts = {}) {
  return segs.map((s) => (s.math ? new OMath({ children: latexToMath(s.math) }) : new TextRun({
    text: s.text, bold: s.bold || opts.bold, italics: s.italics, font: opts.font || FONT,
    size: opts.size, color: opts.color,
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
}''')

rep('''function styledLine(segs, ctx) {
  const first = segs[0] || { text: "" };
  const label = first.bold ? first.text.trim() : "";
  const size = ctx.size;

  if (/^(Answer:|Model answer:)$/.test(label)) {''', '''const BOX = {
  answer: { shading: { type: ShadingType.CLEAR, fill: C.ansBg, color: "auto" },
    border: { left: { style: BorderStyle.SINGLE, size: 18, color: C.ans, space: 6 } }, indent: { left: 120, right: 60 } },
  explanation: { shading: { type: ShadingType.CLEAR, fill: C.expBg, color: "auto" },
    border: { left: { style: BorderStyle.SINGLE, size: 18, color: C.expRule, space: 6 } }, indent: { left: 120, right: 60 } },
};
const ANSWER_LABEL = /^(Answer:|Model answer:|Solution:)$/;

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

  if (ANSWER_LABEL.test(label)) {''')

rep('''      indent: { left: 120, right: 60 }, spacing: { before: 40, after: 40, line: 264 }, keepLines: true,
    });
  }
  if (label === "Explanation:") {''', '''      indent: { left: 120, right: 60 }, spacing: { before: 40, after: ctx.lastInBox === false ? 20 : 40, line: 264 }, keepLines: true,
      keepNext: ctx.lastInBox === false,
    });
  }
  if (label === "Explanation:") {''')

rep('''          const isAnswerLabel = (l) => l && l[0] && l[0].bold && /^(Answer:|Model answer:|Explanation:)$/.test(l[0].text.trim());''',
    '''          const isAnswerLabel = (l) => l && l[0] && l[0].bold && /^(Answer:|Model answer:|Solution:|Explanation:)$/.test(l[0].text.trim());''')

rep('''            || (nt.type === "paragraph_open" && /^\\*\\*(Answer|Model answer):\\*\\*/.test(tokens[k + 1]?.content || "")));
          lines.forEach((segs, li) => out.push(styledLine(segs, {
            para: {}, attachNext: li < lines.length - 1 ? isAnswerLabel(lines[li + 1]) : nextBlockAttached,
          })));''', '''            || (nt.type === "paragraph_open" && /^\\*\\*(Answer|Model answer|Solution):\\*\\*/.test(tokens[k + 1]?.content || "")));
          // Lines that follow an Answer/Solution/Explanation label in the same paragraph stay inside its box.
          let box = null;
          lines.forEach((segs, li) => {
            const lab = segs[0] && segs[0].bold ? segs[0].text.trim() : "";
            if (ANSWER_LABEL.test(lab)) box = "answer";
            else if (lab === "Explanation:") box = "explanation";
            else if (li === 0) box = null;
            const inBox = box && li > 0 && !ANSWER_LABEL.test(lab) && lab !== "Explanation:";
            const lastInBox = li === lines.length - 1 || isAnswerLabel(lines[li + 1]);
            const made = styledLine(segs, {
              para: {}, attachNext: li < lines.length - 1 ? isAnswerLabel(lines[li + 1]) : nextBlockAttached,
              box: inBox ? box : null, lastInBox: box ? lastInBox : undefined,
            });
            out.push(...(Array.isArray(made) ? made : [made]));
          });''')

# Other callers of styledLine must accept an array (figure) result too.
rep('''              out.push(styledLine(segs, { para: { indent: { left: 720 } } }));''',
    '''              out.push(...[styledLine(segs, { para: { indent: { left: 720 } } })].flat());''')

open(p, "w", encoding="utf-8").write(s)
print("patched")
