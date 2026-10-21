"""Move "> $$...$$" display maths out of blockquotes (the Word builder only renders $$ on its own line),
and report any Unicode minus sign left inside $...$ maths.
Usage: python fix_display.py <chapter.md>
"""
import re
import sys
from pathlib import Path

p = Path(sys.argv[1])
lines = p.read_text(encoding="utf8").split("\n")
out = []
moved = 0
i = 0
while i < len(lines):
    ln = lines[i]
    if ln.startswith("> $$"):
        if out and out[-1] != "":
            out.append("")
        out.append(ln[2:])
        out.append("")
        moved += 1
        if i + 1 < len(lines) and lines[i + 1].strip() == ">":
            i += 1
        i += 1
        continue
    out.append(ln)
    i += 1
s = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
p.write_text(s, encoding="utf8")
bad = [m.group(0) for m in re.finditer(r"\$[^$\n]*\$", s) if "−" in m.group(0)]
print("display lines moved:", moved)
print("unicode minus inside maths:", bad if bad else "none")
