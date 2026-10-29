"""Parse chapters with the Core9X importer (vendored copy of api/app/importer/chapter_md.py) and compare with originals/.

Usage (from icse-x/):  python tools/check_parse.py chapters/<Subject> [more folders or files]

Prints lessons/questions/warnings per file and flags any change in the question count or any warning.
A change in lesson count is reported (allowed only when a non-exam ### part was deleted or a syllabus topic added).
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from app.importer.chapter_md import parse_chapter  # noqa: E402

ORIG = HERE.parent / "originals"
bad = 0
for arg in sys.argv[1:]:
    q = Path(arg)
    for f in sorted(q.glob("*.md")) if q.is_dir() else [q]:
        ch = parse_chapter(f)
        msg = f"{f.name[:48]:48} lessons {len(ch.lessons):3}  questions {len(ch.questions):4}  warnings {len(ch.warnings)}"
        o = ORIG / f.parent.name / f.name
        if o.exists():
            oc = parse_chapter(o)
            if len(oc.questions) != len(ch.questions):
                msg += f"  QUESTIONS CHANGED (was {len(oc.questions)})"
                bad += 1
            if len(oc.lessons) != len(ch.lessons):
                msg += f"  lessons was {len(oc.lessons)}"
        if ch.warnings:
            bad += 1
            msg += "  " + "; ".join(ch.warnings[:3])
        print(msg)
sys.exit(1 if bad else 0)
