"""List every chemical equation (formulas joined by " + " around "→") in a chapter file and check that it balances.
Usage: python chem_balance_check.py <chapter.md>
Prints the equations that do NOT balance (skeletal equations and exercise prompts are expected there).
"""
import re
import sys
from collections import Counter
from pathlib import Path

SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
SUP_CHARGE = re.compile(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]*[⁺⁻]")
ELEM = re.compile(r"([A-Z][a-z]?)(\d*)")
TOKEN = re.compile(r"^\d*(?:[A-Z][a-z]?|[()₀-₉0-9·x])+(?:\((?:s|l|g|aq)\))?[↓↑]?$")
SKIP_WORDS = {"heat", "energy", "light"}


def count(s):
    stack = [Counter()]
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "(":
            stack.append(Counter())
            i += 1
        elif ch == ")":
            if len(stack) < 2:
                return None
            i += 1
            m = re.match(r"\d*", s[i:])
            n = int(m.group(0)) if m.group(0) else 1
            i += len(m.group(0))
            top = stack.pop()
            for k, v in top.items():
                stack[-1][k] += v * n
        else:
            m = ELEM.match(s, i)
            if not m:
                return None
            stack[-1][m.group(1)] += int(m.group(2)) if m.group(2) else 1
            i = m.end()
    return stack[0] if len(stack) == 1 else None


def parse_formula(f):
    f = f.translate(SUB)
    f = SUP_CHARGE.sub("", f)
    f = re.sub(r"\((s|l|g|aq)\)", "", f).replace("↓", "").replace("↑", "")
    m = re.match(r"^(\d*)(.*)$", f)
    coef = int(m.group(1)) if m.group(1) else 1
    total = Counter()
    for part in m.group(2).split("·"):
        pm = re.match(r"^(\d*|x)(.*)$", part)
        if pm.group(1) == "x":
            continue
        pcoef = int(pm.group(1)) if pm.group(1) else 1
        c = count(pm.group(2))
        if c is None:
            return None
        for k, v in c.items():
            total[k] += v * pcoef
    return Counter({k: v * coef for k, v in total.items()})


def grab(tokens):
    """Formula terms joined by '+', read from the start of the token list."""
    terms, expect_term = [], True
    for t in tokens:
        t2 = t.strip(".,;:*")
        if expect_term:
            if t2.lower() in SKIP_WORDS:
                expect_term = False
                continue
            if TOKEN.match(t2) and re.search(r"[A-Z]", t2):
                terms.append(t2)
                expect_term = False
                if t2 != t:
                    break
                continue
            break
        else:
            if t == "+":
                expect_term = True
                continue
            break
    return terms


ARROW_COND = re.compile(r"\$\\xrightarrow\{\\text\{[^}]*\}\}\$")
text = Path(sys.argv[1]).read_text(encoding="utf8")
seen, bad, total_eq = set(), 0, 0
for raw in text.splitlines():
    line = ARROW_COND.sub("→", raw).replace("**", " ")
    parts = line.split("→")
    for i in range(len(parts) - 1):
        left = grab(list(reversed(parts[i].split())))[::-1]
        right = grab(parts[i + 1].split())
        if not left or not right:
            continue
        key = (" + ".join(left), " + ".join(right))
        if key in seen:
            continue
        seen.add(key)
        L = sum((parse_formula(t) or Counter() for t in left), Counter())
        R = sum((parse_formula(t) or Counter() for t in right), Counter())
        if not L or not R:
            continue
        total_eq += 1
        if L != R:
            bad += 1
            print(f"UNBALANCED: {key[0]} → {key[1]}")
print(f"checked {total_eq} equations, {bad} not balanced")
