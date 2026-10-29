"""Remove the "Beyond the text (... not needed for exam answers)" block from a chapter file.

Usage: python drop_beyond.py <chapter.md> [more.md ...]

The block is a "### N.M Beyond the text ..." subsection of section 5. It runs until the next "###"/"##" heading or
"---" rule. Later subsections of the same section are renumbered (5.4 -> 5.3) so the numbering stays continuous.
Safe to run twice: a file without the block is left alone.
"""
import re
import sys
from pathlib import Path

HEAD = re.compile(r"^### (\d+)\.(\d+) Beyond the text\b.*$", re.M)


def drop(text: str) -> tuple[str, bool]:
    m = HEAD.search(text)
    if not m:
        return text, False
    sec, sub = int(m.group(1)), int(m.group(2))
    end = re.compile(r"^(###? |---\s*$)", re.M).search(text, m.end())
    stop = end.start() if end else len(text)
    text = text[: m.start()] + text[stop:]

    # Renumber the later subsections of the same section.
    def renum(mm: re.Match) -> str:
        n = int(mm.group(2))
        return f"### {sec}.{n - 1}{mm.group(3)}" if n > sub else mm.group(0)

    sec_end = re.compile(r"^## ", re.M).search(text, m.start())
    tail_end = sec_end.start() if sec_end else len(text)
    body = re.sub(rf"^### ({sec})\.(\d+)(.*)$", renum, text[m.start():tail_end], flags=re.M)
    return text[: m.start()] + body + text[tail_end:], True


for arg in sys.argv[1:]:
    p = Path(arg)
    raw = p.read_bytes().decode("utf-8")
    new, changed = drop(raw)
    if changed:
        p.write_bytes(new.encode("utf-8"))
    print(("removed " if changed else "no block ") + p.name)
