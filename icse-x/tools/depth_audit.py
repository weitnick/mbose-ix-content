"""Audit ICSE chapters against DEPTH_STANDARD.md (repo-relative version of the overseer's tool).

Usage (from icse-x/):  python tools/depth_audit.py chapters/<Subject>            # a folder
                       python tools/depth_audit.py "chapters/<Subject>/<file>.md" # one file

For each chapter: Section 1 words (original -> now), and for every "###" lesson part whether it has Worked examples,
Doubts cleared, Mistakes to avoid and Check yourself blocks; leftover non-exam blocks; "###" titles changed against
originals/; and original Section 1 lines that went missing (LOST). Prints OK or FIX per file.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
ORIG = ROOT / "originals"
BLOCKS = {"ex": r"worked example", "dbt": r"doubts? cleared", "mis": r"mistakes to avoid", "chk": r"check yourself"}
SKIP_PARTS = re.compile(r"summary|at a glance|recap", re.I)


def section1(text: str) -> str:
    a = re.search(r"^## 1\. ", text, re.M)
    b = re.search(r"^## 2\. ", text, re.M)
    return text[a.start():b.start()] if a and b and b.start() > a.start() else ""


def parts(s1: str) -> list[tuple[str, str]]:
    bits = re.split(r"^### (.+)$", s1, flags=re.M)
    return [(bits[i].strip(), bits[i + 1]) for i in range(1, len(bits) - 1, 2)]


def audit(p: Path) -> None:
    t = p.read_text(encoding="utf-8")
    s1 = section1(t)
    ps = parts(s1)
    bad = [f"{title[:40]} (no {', '.join(k for k, rx in BLOCKS.items() if not re.search(rx, body, re.I))})"
           for title, body in ps
           if not SKIP_PARTS.search(title) and any(not re.search(rx, body, re.I) for rx in BLOCKS.values())]
    leftovers = len(re.findall(r"Beyond the (text|syllabus)|not examined|not needed for (the )?exam", t, re.I))
    found = len(re.findall(r"Foundation first", s1))
    note, grow = "", "(no original) "
    old = ORIG / p.parent.name / p.name
    if old.exists():
        o1 = section1(old.read_text(encoding="utf-8"))
        before = [x for x, _ in parts(o1)]
        now = [x for x, _ in ps]
        if before != now:
            note = f"  TITLES CHANGED: {sorted(set(before) ^ set(now))}"
        squash = lambda x: re.sub(r"\\,|\s", "", x)
        new_sq = squash(s1)
        lost = [ln.strip() for ln in o1.splitlines() if ln.strip() and squash(ln) not in new_sq and not ln.startswith("### ")]
        if lost:
            note += f"  LOST {len(lost)} old line(s), e.g. «{lost[0][:70]}»"
        grow = f"{len(o1.split())}->"
    status = "OK " if not bad and not leftovers and not note else "FIX"
    print(f"{status} {p.name[:50]:50} s1 {grow}{len(s1.split())} words, {len(ps)} parts, foundation {found}"
          + (f", non-exam {leftovers}" if leftovers else "") + note)
    for b in bad:
        print("      missing:", b)


for arg in sys.argv[1:]:
    q = Path(arg)
    for f in sorted(q.glob("*.md")) if q.is_dir() else [q]:
        audit(f)
