"""Finalize a chapter content Markdown file in place.

- Numbers the questions in sections 9 (MCQs), 10 (short answers) and 11 (long answers) in order.
- Writes the question range into each sub-heading of section 9, e.g. "### Part I (Q1–Q58)".
- Rebuilds the MCQ quick key (### 17.1) from the answers under each question.
- Checks every MCQ: four options (a)–(d), "All of the above" / "None of the above" only ever as (d),
  no two identical options, and an answer whose text matches the chosen option.
  Flags repeated question stems.

Usage: python finalize_chapter.py <chapter.md>
"""
import math
import re
import sys
from collections import Counter
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
problems = []


def split_sections(s):
    parts = re.split(r"(?m)^(?=## \d+\. )", s)
    return parts[0], {int(re.match(r"## (\d+)\.", p).group(1)): p for p in parts[1:]}


head, secs = split_sections(text)


def renumber(sec):
    n = 0
    def repl(m):
        nonlocal n
        n += 1
        return f"**Q{n}.**"
    return re.sub(r"(?m)^\*\*Q(?:\d+|#)\.\*\*", repl, sec), n


# ---- Section 9: MCQs ---------------------------------------------------------------------
mcq, n_mcq = renumber(secs[9])
# Sub-heading ranges
lines, out, pending = mcq.split("\n"), [], None
first_q = {}
current = None
for i, line in enumerate(lines):
    if line.startswith("### "):
        current = i
    m = re.match(r"^\*\*Q(\d+)\.\*\*", line)
    if m and current is not None:
        first_q.setdefault(current, [int(m.group(1)), int(m.group(1))])
        first_q[current][1] = int(m.group(1))
for i, (a, b) in first_q.items():
    base = re.sub(r"\s*\(Q\d+[–-]Q\d+\)\s*$", "", lines[i])
    lines[i] = f"{base} (Q{a}–Q{b})"
mcq = "\n".join(lines)

answers = []
blocks = re.split(r"(?m)^(?=\*\*Q\d+\.\*\*)", mcq)[1:]
stems = Counter()
for b in blocks:
    qn = int(re.match(r"\*\*Q(\d+)\.\*\*", b).group(1))
    stem = re.match(r"\*\*Q\d+\.\*\*\s*(.*)", b).group(1).strip()
    stems[re.sub(r"[^a-z0-9 ]", "", stem.lower())] += 1
    opts = dict(re.findall(r"(?m)^- \(([a-z])\) (.+)$", b))
    if sorted(opts) != list("abcd"):
        problems.append(f"MCQ Q{qn}: options found {sorted(opts)}")
    for k, v in opts.items():
        if v.strip() in ("All of the above", "None of the above") and k != "d":
            problems.append(f"MCQ Q{qn}: '{v.strip()}' should be option (d)")
    # genotype options (TT / Tt / tt, Rr yy) differ only in case, so compare those case-sensitively
    def is_geno(tok):
        return tok.isalpha() and len(tok) % 2 == 0 and all(tok[i].lower() == tok[i + 1].lower() for i in range(0, len(tok), 2))
    keys = [v.strip() if any(is_geno(t) for t in v.split()) else v.strip().lower() for v in opts.values()]
    if len(set(keys)) != len(opts):
        problems.append(f"MCQ Q{qn}: two options are the same")
    am = re.search(r"(?m)^\*\*Answer:\*\* \(([a-d])\)\s*(.*)$", b)
    if not am:
        problems.append(f"MCQ Q{qn}: no answer line")
        continue
    letter, atext = am.group(1), am.group(2).strip()
    answers.append(letter)
    norm = lambda x: re.sub(r"[\s.*_]+$", "", x.strip().lower())
    if letter in opts and norm(atext) != norm(opts[letter]):
        problems.append(f"MCQ Q{qn}: answer text '{atext}' != option ({letter}) '{opts[letter]}'")
    if not re.search(r"(?m)^\*\*Explanation:\*\*", b):
        problems.append(f"MCQ Q{qn}: no explanation")
for s, c in stems.items():
    if c > 1:
        problems.append(f"Repeated MCQ stem x{c}: {s[:70]}")
secs[9] = mcq

# ---- Sections 10 and 11 --------------------------------------------------------------------
secs[10], n_short = renumber(secs[10])
n_long = 0
if 11 in secs:
    secs[11], n_long = renumber(secs[11])
for n in (10, 11):
    if n not in secs:
        continue
    st = Counter(re.sub(r"[^a-z0-9 ]", "", m.lower()) for m in re.findall(r"(?m)^\*\*Q\d+\.\*\*\s*(.+)$", secs[n]))
    for s, c in st.items():
        if c > 1:
            problems.append(f"Repeated question in section {n} x{c}: {s[:70]}")

# ---- 17.1 MCQ quick key ------------------------------------------------------------------
cols = 5
rows = math.ceil(len(answers) / cols)
table = ["| " + " | ".join(["Q | Ans"] * cols) + " |", "|" + "---|---|" * cols]
for r in range(rows):
    cells = []
    for c in range(cols):
        q = c * rows + r
        cells.append(f"{q + 1} | {answers[q]}" if q < len(answers) else " | ")
    table.append("| " + " | ".join(cells) + " |")
key = "\n".join(table)
secs[17] = re.sub(r"(?s)(### 17\.1[^\n]*\n\n).*?(\n### 17\.2)", lambda m: m.group(1) + key + "\n" + m.group(2), secs[17])
secs[17] = re.sub(r"### 17\.1[^\n]*", "### 17.1 MCQ quick key (Section 9)", secs[17])

path.write_text(head + "".join(secs[k] for k in sorted(secs)), encoding="utf-8")

dist = Counter(answers)
print(f"{path.name}: {n_mcq} MCQs, {n_short} short answers, {n_long} long answers")
print("MCQ answers: " + ", ".join(f"({k}) {dist.get(k, 0)}" for k in "abcd"))
aon = [b for b in blocks if re.search(r"(?m)^- \(d\) (All|None) of the above$", b)]
aon_right = [b for b in aon if re.search(r"(?m)^\*\*Answer:\*\* \(d\) (All|None) of the above", b)]
print(f"'All/None of the above' offered in {len(aon)} MCQs; correct in {len(aon_right)}")
if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print("  - " + p)
else:
    print("All checks passed.")
