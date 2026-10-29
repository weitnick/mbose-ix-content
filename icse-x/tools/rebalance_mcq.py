"""Even out which letter (a)–(d) holds the correct MCQ answer in section 9, in place.

Swaps the correct option with another option in the same question. Leaves a question alone if it
offers "All of the above" / "None of the above", or if its explanation mentions an option letter.
Run finalize_chapter.py afterwards to rebuild the answer key.
Usage: python rebalance_mcq.py <chapter.md>
"""
import random
import re
import sys
from collections import Counter
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
parts = re.split(r"(?m)^(?=## \d+\. )", text)
head, secs = parts[0], {int(re.match(r"## (\d+)\.", p).group(1)): p for p in parts[1:]}
L = "abcd"

pieces = re.split(r"(?m)^(?=\*\*Q(?:\d+|#)\.\*\*)", secs[9])
lead, blocks = pieces[0], pieces[1:]
items = []
for b in blocks:
    opts = dict(re.findall(r"(?m)^- \(([a-d])\) (.+)$", b))
    ans = re.search(r"(?m)^\*\*Answer:\*\* \(([a-d])\)", b).group(1)
    expl = (re.search(r"(?m)^\*\*Explanation:\*\*(.*)$", b) or [None, ""])[1]
    # Also keep options that have a natural order (quadrant I, II, III, IV) where they are.
    natural = sum(bool(re.match(r"^(quadrant [IV]+|on an axis|on the [xy]-axis)$", o.strip())) for o in opts.values()) >= 3
    # Fixed-order option sets: statement pairs and assertion–reason keys keep the board's standard order.
    fixed = any(o.strip().startswith(("Both the statements", "Statement 1 is", "A is true", "A is false", "Both A and R"))
                for o in opts.values())
    # An option that refers to other options by letter ("both (a) and (b)") must not move.
    refers = any(re.search(r"\(\s*[a-d]\s*\)\s*(and|or)\s*\(\s*[a-d]\s*\)", o) for o in opts.values())
    locked = (opts.get("d", "") in ("All of the above", "None of the above")
              or re.search(r"\([a-d]\)", expl) is not None or natural or fixed or refers)
    items.append({"b": b, "opts": [opts[k] for k in L], "ans": ans, "locked": locked, "moved": False})

count = Counter(i["ans"] for i in items)
target = len(items) / 4
# Visit the questions in a fixed shuffled order, so the moved answers are spread through the whole
# bank instead of bunching at the start (which left long runs of one letter near the end).
order = list(range(len(items)))
random.Random(len(items)).shuffle(order)
for it in (items[k] for k in order):
    if it["locked"] or count[it["ans"]] <= target + 0.5:
        continue
    under = min(L, key=lambda k: count[k])
    if count[under] >= target - 0.5:
        continue
    i, j = L.index(it["ans"]), L.index(under)
    it["opts"][i], it["opts"][j] = it["opts"][j], it["opts"][i]
    count[it["ans"]] -= 1
    count[under] += 1
    it["ans"], it["moved"] = under, True

out = []
for it in items:
    b = it["b"]
    if it["moved"]:
        b = re.sub(r"(?m)^- \([a-d]\) .+\n?", "", b)
        opt_block = "".join(f"- ({L[k]}) {o}\n" for k, o in enumerate(it["opts"]))
        b = re.sub(r"(?m)^(\*\*Q(?:\d+|#)\.\*\*.*\n)", lambda m: m.group(1) + opt_block, b, count=1)
        new_answer = f"**Answer:** ({it['ans']}) {it['opts'][L.index(it['ans'])]}"
        # A function replacement, so backslashes in LaTeX answers are copied literally.
        b = re.sub(r"(?m)^\*\*Answer:\*\* \([a-d]\).*$", lambda m: new_answer, b)
    out.append(b)
secs[9] = lead + "".join(out)
path.write_text(head + "".join(secs[k] for k in sorted(secs)), encoding="utf-8")
print(path.name, "answer spread now:", dict(sorted(count.items())), "| moved", sum(i["moved"] for i in items))
