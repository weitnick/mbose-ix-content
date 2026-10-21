"""List the LaTeX commands used in a chapter file and flag any that math_docx.js does not know.

Usage: python latex_check.py <chapter.md>
"""
import re
import sys
from collections import Counter
from pathlib import Path

here = Path(__file__).parent
js = (here / "math_docx.js").read_text(encoding="utf-8")
known = set(re.findall(r"\b([A-Za-z]+):\s*\"", js.split("const SYMBOLS")[1].split("};")[0]))
# Structural commands handled by the parser itself.
known |= {"frac", "dfrac", "tfrac", "sqrt", "text", "mathrm", "mathbb", "overline", "overleftrightarrow",
          "left", "right", "big", "Big", "bigl", "bigr", "operatorname", "begin", "end"}
known |= set(re.findall(r'"\\\\?([A-Za-z]+)"', js))
known |= set(re.findall(r'case "([A-Za-z]+)"', js))  # commands handled in the parser's switch (sin, cot, cosec, ...)

md = Path(sys.argv[1]).read_text(encoding="utf-8")
maths = re.findall(r"\$\$(.+?)\$\$|\$(.+?)\$", md, flags=re.S)
used = Counter()
for a, b in maths:
    used.update(re.findall(r"\\([A-Za-z]+)", a or b))
unknown = {k: v for k, v in used.items() if k not in known}
print("commands used:", ", ".join(f"{k}×{v}" for k, v in used.most_common()))
print("UNKNOWN:", unknown or "none")
