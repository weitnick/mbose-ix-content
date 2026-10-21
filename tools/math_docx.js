// Convert a small subset of LaTeX (what school maths content needs) into docx Math components,
// so equations written as $...$ in the Markdown become real Word equations.
//
// Supported: \frac \dfrac \tfrac, \sqrt[n]{}, ^ and _ (with or without braces), \overline \bar,
// \overleftrightarrow \overrightarrow (line / ray over letters), \left( \right) and friends,
// \text{} \mathrm{}, \mathbb{R}, Greek letters and the common relation/operator symbols.
const {
  XmlComponent, XmlAttributeComponent, MathRun, MathFraction, MathRadical, MathSuperScript,
  MathSubScript, MathSubSuperScript, MathRoundBrackets, MathSquareBrackets, MathCurlyBrackets, createMathBase,
} = require("docx");

const SYMBOLS = {
  // Physics (Class XII): integrals, sums, partial derivatives, field symbols
  int: "∫", oint: "∮", iint: "∬", sum: "∑", prod: "∏", partial: "∂", nabla: "∇", hbar: "ℏ",
  odot: "⊙", otimes: "⊗", oplus: "⊕", AA: "Å", ll: "≪", gg: "≫", langle: "⟨", rangle: "⟩",
  times: "×", div: "÷", pm: "±", mp: "∓", cdot: "·", ast: "∗", star: "⋆",
  neq: "≠", ne: "≠", le: "≤", leq: "≤", ge: "≥", geq: "≥", approx: "≈", equiv: "≡", sim: "∼", simeq: "≃", cong: "≅",
  lt: "<", gt: ">", infty: "∞", propto: "∝",
  pi: "π", theta: "θ", alpha: "α", beta: "β", gamma: "γ", delta: "δ", Delta: "Δ", lambda: "λ", mu: "μ",
  sigma: "σ", Sigma: "Σ", phi: "φ", omega: "ω", Omega: "Ω", epsilon: "ε", rho: "ρ", tau: "τ",
  eta: "η", nu: "ν", kappa: "κ", chi: "χ", psi: "ψ", Psi: "Ψ", xi: "ξ", zeta: "ζ", Phi: "Φ", Gamma: "Γ",
  Lambda: "Λ", Theta: "Θ", varepsilon: "ε", vartheta: "ϑ", varphi: "φ",
  angle: "∠", triangle: "△", square: "□", blacksquare: "■", circ: "°", degree: "°", parallel: "∥", perp: "⊥", nparallel: "∦",
  in: "∈", notin: "∉", subset: "⊂", subseteq: "⊆", supset: "⊃", cup: "∪", cap: "∩", emptyset: "∅", varnothing: "∅",
  nleq: "≰", ngeq: "≱", nsubset: "⊄", nsubseteq: "⊈", ni: "∋",
  uparrow: "↑", downarrow: "↓", rightleftharpoons: "⇌",
  Rightarrow: "⇒", Leftarrow: "⇐", Leftrightarrow: "⇔", leftrightarrow: "↔", longrightarrow: "⟶", rightarrow: "→", leftarrow: "←", to: "→", implies: "⇒", iff: "⇔",
  therefore: "∴", because: "∵", ldots: "…", cdots: "⋯", dots: "…", vdots: "⋮",
  mid: "∣", vert: "|", lvert: "|", rvert: "|", Vert: "‖", colon: ":", prime: "′",
  forall: "∀", exists: "∃", neg: "¬", checkmark: "✓", ell: "ℓ",
  "%": "%", "{": "{", "}": "}", "#": "#", "&": "&", "_": "_", "$": "$",
  ",": " ", ";": " ", ":": " ", "!": "", " ": " ", quad: " ", qquad: "  ",
};
const BLACKBOARD = { R: "ℝ", Q: "ℚ", Z: "ℤ", N: "ℕ", W: "𝕎", C: "ℂ", I: "𝕀" };

// ---- Custom OMML elements that the docx package does not provide --------------------------
class ValAttr extends XmlAttributeComponent {
  constructor(val) { super({ val }); this.xmlKeys = { val: "m:val" }; }
}
class ValElement extends XmlComponent {
  constructor(name, val) { super(name); this.root.push(new ValAttr(val)); }
}
class Wrapper extends XmlComponent {
  constructor(name, children) { super(name); for (const c of children) this.root.push(c); }
}
// Overline: <m:bar><m:barPr><m:pos m:val="top"/></m:barPr><m:e>…</m:e></m:bar>
const MathBar = (children) => new Wrapper("m:bar", [new Wrapper("m:barPr", [new ValElement("m:pos", "top")]), createMathBase({ children })]);
// Accent above (arrow for lines and rays): <m:acc><m:accPr><m:chr m:val="…"/></m:accPr><m:e>…</m:e></m:acc>
const MathAccent = (chr, children) => new Wrapper("m:acc", [new Wrapper("m:accPr", [new ValElement("m:chr", chr)]), createMathBase({ children })]);
// Stretchy delimiters with chosen characters (determinant bars): <m:d><m:dPr><m:begChr/><m:endChr/></m:dPr><m:e>…</m:e></m:d>
const MathDelim = (beg, end, children) => new Wrapper("m:d", [
  new Wrapper("m:dPr", [new ValElement("m:begChr", beg), new ValElement("m:endChr", end)]),
  createMathBase({ children }),
]);
// Normal-text run (<m:rPr><m:nor/></m:rPr>): Word does not treat it as an operator, so the "+" after a
// gas/precipitate arrow (H2↑ + …) stays a binary plus.
class NormalTextRun extends XmlComponent {
  constructor(text) {
    super("m:r");
    this.root.push(new Wrapper("m:rPr", [new XmlComponent("m:nor")]));
    const t = new XmlComponent("m:t");
    t.root.push(text);
    this.root.push(t);
  }
}
// Arrow with a condition written above it (\xrightarrow{heat}): the arrow is a group character below the text.
// <m:groupChr><m:groupChrPr><m:chr m:val="→"/><m:pos m:val="bot"/><m:vertJc m:val="bot"/></m:groupChrPr><m:e>…</m:e></m:groupChr>
const MathArrowOver = (children) => new Wrapper("m:groupChr", [
  new Wrapper("m:groupChrPr", [new ValElement("m:chr", "→"), new ValElement("m:pos", "bot"), new ValElement("m:vertJc", "bot")]),
  createMathBase({ children: children.length ? children : [new MathRun(" ")] }),
]);
// Prescripts, for nuclide symbols such as ^{14}_{7}\text{N}: <m:sPre><m:sub>…</m:sub><m:sup>…</m:sup><m:e>…</m:e></m:sPre>
// (built here because the docx package writes the base before the scripts, against the schema order).
const MathPreScript = (sub, sup, base) => new Wrapper("m:sPre", [
  new Wrapper("m:sub", sub && sub.length ? sub : [new MathRun(" ")]),
  new Wrapper("m:sup", sup && sup.length ? sup : [new MathRun(" ")]),
  createMathBase({ children: base }),
]);
// A ^ or _ right after one of these (or at the very start) has no base of its own: it is a prescript
// on the atom that follows.
const PRE_AFTER_CHR = new Set(["+", "-", "=", ",", "(", "[", "<", ">"]);
const PRE_AFTER_CMD = new Set(["rightarrow", "to", "longrightarrow", "leftarrow", "rightleftharpoons", "xrightarrow", "quad", "qquad", ",", ";", " "]);
// Upright (non-italic) text run: <m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>…</m:t></m:r>
class UprightRun extends XmlComponent {
  constructor(text) {
    super("m:r");
    this.root.push(new Wrapper("m:rPr", [new ValElement("m:sty", "p")]));
    const t = new XmlComponent("m:t");
    t.root.push(text);
    this.root.push(t);
  }
}

// ---- Tokeniser ------------------------------------------------------------------------------
function tokenize(src) {
  const toks = [];
  for (let i = 0; i < src.length;) {
    const ch = src[i];
    if (ch === "\\") {
      const m = /^\\([A-Za-z]+|.)/.exec(src.slice(i));
      i += m[0].length;
      if (/^(text|mathrm|textrm|operatorname)$/.test(m[1]) && src[i] === "{") {
        // Keep the words (and their spaces) of \text{...} exactly as written.
        let depth = 0, j = i;
        for (; j < src.length; j++) {
          if (src[j] === "{") depth++;
          else if (src[j] === "}" && --depth === 0) break;
        }
        toks.push({ t: "text", v: src.slice(i + 1, j) });
        i = j + 1;
      } else {
        toks.push({ t: "cmd", v: m[1] });
      }
    } else if (/\s/.test(ch)) {
      i++;
    } else if (/[0-9]/.test(ch)) {
      const m = /^[0-9]+(?:\.[0-9]*)?/.exec(src.slice(i)); // keep "0." together before a recurring bar
      toks.push({ t: "num", v: m[0] });
      i += m[0].length;
    } else {
      toks.push({ t: "chr", v: ch });
      i++;
    }
  }
  return toks;
}

// ---- Parser ---------------------------------------------------------------------------------
// Trig and log function names are followed by a thin space before their argument ("sin A", "sin² θ", "cos 30°",
// "log x"), but not before a bracket ("sin(A + B)").
const FUNC_SPACE = /\\(cosec|csc|sin|cos|tan|cot|sec|log|ln)(?![A-Za-z])((?:\^(?:\{[^{}]*\}|[0-9A-Za-z]))?)\s*(?=[A-Za-z0-9\\])(?!\\[,;!]|\\left|\\right)/g;

// A comma followed by a space in the source keeps a thin space after it, so "(0, 0)" and "Z = 0, 120, 110"
// do not run together into "0,120,110" (which reads like one number). \text{...} groups are left alone.
const COMMA_SPACE = /(\\(?:text|mathrm|textrm|operatorname)\{[^{}]*\})|,(?=\s)/g;

function convert(src) {
  const toks = tokenize(src.replace(COMMA_SPACE, (m, t) => t || ",\\,").replace(FUNC_SPACE, "\\$1$2\\,"));
  let p = 0;
  const peek = () => toks[p];

  // Read a raw brace group as text (for \text{...}); the tokeniser dropped spaces, so re-read from the source.
  function rawGroupText() {
    // Rebuild from tokens until the matching brace.
    let depth = 0, s = "";
    if (peek() && peek().t === "chr" && peek().v === "{") { p++; depth = 1; } else return "";
    while (p < toks.length) {
      const k = toks[p++];
      if (k.t === "chr" && k.v === "{") depth++;
      if (k.t === "chr" && k.v === "}") { depth--; if (!depth) break; }
      s += k.t === "cmd" ? (SYMBOLS[k.v] ?? k.v) : k.v;
    }
    return s;
  }

  function parseGroupOrAtom() {
    const k = peek();
    if (!k) return [];
    if (k.t === "chr" && k.v === "{") {
      p++;
      const out = parseSeq("}");
      p++; // closing brace
      return out;
    }
    return parseAtom();
  }

  function parseOptional() {
    // [n] after \sqrt
    if (peek() && peek().t === "chr" && peek().v === "[") {
      p++;
      const out = parseSeq("]");
      p++;
      return out;
    }
    return null;
  }

  function parseAtom() {
    const k = toks[p++];
    if (k.t === "num") return [new MathRun(k.v)];
    if (k.t === "text") return [new UprightRun(k.v)];
    if (k.t === "chr") {
      const map = { "-": "−", "*": "∗", "'": "′" };
      return [new MathRun(map[k.v] || k.v)];
    }
    // commands
    switch (k.v) {
      case "frac": case "dfrac": case "tfrac": {
        const num = parseGroupOrAtom();
        const den = parseGroupOrAtom();
        return [new MathFraction({ numerator: num, denominator: den })];
      }
      case "sqrt": {
        const deg = parseOptional();
        const body = parseGroupOrAtom();
        return [new MathRadical(deg ? { children: body, degree: deg } : { children: body })];
      }
      case "overline": case "bar": return [MathBar(parseGroupOrAtom())];
      case "overleftrightarrow": return [MathAccent("⃡", parseGroupOrAtom())];
      case "overrightarrow": case "vec": return [MathAccent("⃗", parseGroupOrAtom())];
      case "hat": case "widehat": return [MathAccent("̂", parseGroupOrAtom())];
      case "dot": return [MathAccent("̇", parseGroupOrAtom())];
      case "tilde": return [MathAccent("̃", parseGroupOrAtom())];
      case "xrightarrow": return [MathArrowOver(parseGroupOrAtom())];
      case "uparrow": case "downarrow": return [new NormalTextRun(SYMBOLS[k.v])];
      case "text": case "mathrm": case "textrm": case "operatorname": return [new UprightRun(rawGroupText())];
      case "mathbb": {
        const s = rawGroupText();
        return [new UprightRun([...s].map((c) => BLACKBOARD[c] || c).join(""))];
      }
      case "left": {
        const open = toks[p++];
        const inner = parseSeq("\\right");
        p++; // \right
        const close = toks[p++];
        const o = open.t === "cmd" ? open.v : open.v;
        if (o === "(") return [new MathRoundBrackets({ children: inner })];
        if (o === "[") return [new MathSquareBrackets({ children: inner })];
        if (o === "{") return [new MathCurlyBrackets({ children: inner })];
        const sym = (x) => (x.t === "cmd" ? SYMBOLS[x.v] ?? x.v : x.v === "." ? "" : x.v);
        // Other delimiters (| ‖ ⟨ and the empty "." of \left. … \right|) stretch with their contents too.
        return [MathDelim(sym(open), sym(close), inner.length ? inner : [new MathRun(" ")])];
      }
      case "right": return []; // handled by \left
      case "begin": {
        // \begin{bmatrix} a & b \\ c & d \end{bmatrix}  ->  <m:m><m:mr><m:e>a</m:e>…</m:mr>…</m:m> in brackets
        const env = rawGroupText();
        const rows = [];
        let row = [];
        while (p < toks.length) {
          row.push(parseSeq("cell"));
          const sep = toks[p];
          if (!sep) break;
          p++;
          if (sep.t === "chr" && sep.v === "&") continue;
          rows.push(row);
          row = [];
          if (sep.t === "cmd" && sep.v === "end") { rawGroupText(); break; }
        }
        const filled = rows.filter((r) => !(r.length === 1 && r[0].length === 0));
        const grid = new Wrapper("m:m", filled.map((r) => new Wrapper("m:mr",
          r.map((c) => createMathBase({ children: c.length ? c : [new MathRun(" ")] })))));
        if (env === "bmatrix") return [new MathSquareBrackets({ children: [grid] })];
        if (env === "pmatrix") return [new MathRoundBrackets({ children: [grid] })];
        if (env === "vmatrix") return [MathDelim("|", "|", [grid])];
        return [grid];
      }
      case "sin": case "cos": case "tan": case "cot": case "sec": case "log": case "ln": case "exp":
      case "sinh": case "cosh": case "max": case "min": case "lim": case "det": return [new UprightRun(k.v)];
      case "csc": case "cosec": return [new UprightRun("cosec")];
      default:
        if (k.v in SYMBOLS) return SYMBOLS[k.v] === "" ? [] : [new MathRun(SYMBOLS[k.v])];
        return [new MathRun(k.v)];
    }
  }

  function parseSeq(stop) {
    const out = [];
    let prev = null; // the token that began the previous atom (null at the start of the sequence)
    const atEnd = () => {
      const n = peek();
      return !n || (n.t === "chr" && (n.v === "}" || n.v === "]" || n.v === "^" || n.v === "_")) || (n.t === "cmd" && n.v === "right");
    };
    while (p < toks.length) {
      const k = peek();
      if (stop === "}" && k.t === "chr" && k.v === "}") break;
      if (stop === "]" && k.t === "chr" && k.v === "]") break;
      if (stop === "\\right" && k.t === "cmd" && k.v === "right") break;
      if (stop === "cell" && ((k.t === "chr" && k.v === "&") || (k.t === "cmd" && (k.v === "\\" || k.v === "end")))) break;
      if (k.t === "chr" && (k.v === "^" || k.v === "_")) {
        const pre = prev === null || (prev.t === "chr" && PRE_AFTER_CHR.has(prev.v)) || (prev.t === "cmd" && PRE_AFTER_CMD.has(prev.v));
        p++;
        const first = k.v;
        const script1 = parseGroupOrAtom();
        let sup = null, sub = null;
        if (first === "^") sup = script1; else sub = script1;
        const n = peek();
        if (n && n.t === "chr" && (n.v === "^" || n.v === "_") && n.v !== first) {
          p++;
          const s2 = parseGroupOrAtom();
          if (n.v === "^") sup = s2; else sub = s2;
        }
        if (pre && !atEnd()) {
          out.push(MathPreScript(sub, sup, parseAtom()));
          prev = { t: "pre" };
          continue;
        }
        prev = { t: "script" };
        const base = out.length ? [out.pop()] : [new MathRun("")];
        if (sup && sub) out.push(new MathSubSuperScript({ children: base, superScript: sup, subScript: sub }));
        else if (sup) out.push(new MathSuperScript({ children: base, superScript: sup }));
        else out.push(new MathSubScript({ children: base, subScript: sub }));
        continue;
      }
      prev = k;
      out.push(...parseAtom());
    }
    return out;
  }

  return parseSeq(null);
}

// Rough plain-text rendering, used for measuring table columns and for checks.
function latexToPlain(src) {
  return src
    .replace(/\\begin\{[a-z]*\}/g, "[").replace(/\\end\{[a-z]*\}/g, "]").replace(/\\\\/g, "; ").replace(/&/g, " ")
    .replace(/\\(?:d|t)?frac\{([^{}]*)\}\{([^{}]*)\}/g, "$1/$2")
    .replace(/\\sqrt\[([^\]]*)\]\{([^{}]*)\}/g, "$1√$2")
    .replace(/\\sqrt\{([^{}]*)\}/g, "√$1")
    .replace(/\\mathbb\{(.)\}/g, (m, c) => BLACKBOARD[c] || c)
    .replace(/\\xrightarrow\{(?:\\text\{)?([^{}]*)\}?\}/g, "→($1)")
    .replace(/\\(?:text|mathrm|overline|bar|overleftrightarrow|overrightarrow)\{([^{}]*)\}/g, "$1")
    .replace(/\\(?:vec|hat|widehat|dot|tilde)\{([^{}]*)\}/g, " $1 ")
    .replace(/\\([A-Za-z]+)/g, (m, c) => SYMBOLS[c] ?? (/^(sin|cos|tan|cot|sec|log|ln|exp|sinh|cosh|max|min|lim)$/.test(c) ? c + " " : ""))
    .replace(/[{}]/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

module.exports = { convert, latexToPlain };
