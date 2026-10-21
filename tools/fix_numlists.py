"""Inside $...$ maths, put a thin space after a comma that separates two numbers,
so Word does not read "-30, -15, 0" as one grouped number."""
import re
import sys
from pathlib import Path

p = Path(sys.argv[1])
s = p.read_text(encoding="utf8")
count = 0


def fix(m):
    global count
    body = m.group(1)
    new, n = re.subn(r"(?<=[0-9]),\s*(?=-?[0-9])", r",\\, ", body)
    count += n
    return "$" + new + "$"


s = re.sub(r"(?<!\$)\$([^$\n]+)\$(?!\$)", fix, s)
p.write_text(s, encoding="utf8")
print("thin spaces added:", count)
