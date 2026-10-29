"""Read a 17-section chapter file (the format used in D:\\MBOSE APP) into lessons and questions.

Sections used:
  1          Complete Lesson          -> one lesson per "###" part
  2–8, 15    notes of various kinds   -> one lesson each
  9          MCQs                     -> mcq, topic from the "###" group heading
  10 / 11    Short / Long answers     -> short (2 marks) / long (5 marks), self-marked; a "###" group
             heading that says "(N marks each)" sets the marks for its questions (Class X has 3-mark short answers)
             A "**Marking:**" list after a model answer ("- Format: … — 2 marks") becomes its marking scheme.
  12         Competency               -> short, self-marked
  13         Assertion–Reason         -> assertion_reason (auto-marked)
  14         Case-based               -> a case parent with its parts (i)–(x), worth the sum of its parts
  16, 17     Chapter test, answer key -> not imported (tests are generated); 17.1 is used to cross-check MCQs
"""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from app.slug import slugify

SECTION_RE = re.compile(r"^## (\d+)\. (.+?)\s*$")
SUB_RE = re.compile(r"^### (.+?)\s*$")
Q_RE = re.compile(r"^\*\*Q(\d+)\.(?:\s*\(([^)]*)\))?\*\*\s*(.*)$")
OPT_RE = re.compile(r"^- \(([a-d])\)\s*(.*)$")
ANS_RE = re.compile(r"^\*\*(?:Answer|Model answer):\*\*\s*(.*)$")
EXPL_RE = re.compile(r"^\*\*Explanation:\*\*\s*(.*)$")
AR_A_RE = re.compile(r"^\*\*A:\*\*\s*(.*)$")
AR_R_RE = re.compile(r"^\*\*R:\*\*\s*(.*)$")
PART_RE = re.compile(r"^\*\*\((i|ii|iii|iv|v|vi|vii|viii|ix|x)\)\*\*\s*(.*)$")
KEY_LETTER_RE = re.compile(r"^\(([a-d])\)\s*(.*)$", re.S)
IMG_RE = re.compile(r"(!\[[^\]]*\]\()(figures/[^)\s]+)(\))")
META_ROW_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$")
QGROUP_SUFFIX_RE = re.compile(r"\s*\(Q\d+\s*[–-]\s*Q?\d+\)\s*$")
GROUP_MARKS_RE = re.compile(r"\((\d+) marks? each\)", re.IGNORECASE)
MARKING_RE = re.compile(r"^\*\*Marking:\*\*\s*$")
MARK_POINT_RE = re.compile(r"^- (.+?)\s+[—–-]\s+(\d+(?:\.\d+)?) marks?\.?\s*$")

NOTE_SECTIONS = {
    2: "objectives", 3: "explanations", 4: "vocabulary", 5: "facts",
    6: "profiles", 7: "themes", 8: "solutions", 15: "revision",
}
# "Skill" files are skills taught across the syllabus rather than a textbook piece: English reading and
# writing, Social Science map work.
FILE_KIND = {"ch": "chapter", "poem": "poem", "sr": "supplementary", "play": "play", "skill": "skills"}
SUBJECT_CODES = {"mathematics": "maths", "maths": "maths", "science": "science", "english": "english", "english i": "english",
                 "social science": "social", "health and physical education": "hpe", "computer science": "computer",
                 # ICSE sets Physics, Chemistry and Biology as separate papers, and History, Civics and Geography
                 # as two (H.C.G. Papers 1 and 2).
                 "physics": "physics", "chemistry": "chemistry", "biology": "biology",
                 "history and civics": "history", "geography": "geography", "computer applications": "computer",
                 # ASSEB HSLC electives (each student takes one; Geography and Computer Science as above).
                 "advanced mathematics": "advmaths", "history": "history",
                 # NBSE HSLC: Social Sciences, and the optional sixth subjects Core9X teaches (one, or none).
                 "social sciences": "social", "environmental education": "environmental", "foundation of it": "fit",
                 "book-keeping and accountancy": "accountancy",
                 # CBSE Class X: the sixth subjects Core9X teaches (two skill subjects and two academic electives).
                 "artificial intelligence": "ai", "information technology": "it",
                 "elements of book keeping and accountancy": "accountancy",
                 # MBSE HSLC: the additional subjects Core9X teaches (one, or none).
                 "introductory information technology": "iit", "civics and economics": "civics",
                 "commercial studies": "commercial", "home science": "homesci",
                 # ASSEB Class XII (HS Final): the Commerce and Arts subjects and the electives Core9X teaches.
                 "accountancy": "accountancy", "business studies": "bst", "economics": "economics",
                 "political science": "polsci", "sociology": "sociology", "psychology": "psychology",
                 "education": "education", "logic and philosophy": "logic",
                 "business mathematics and statistics": "bmst", "computer science and application": "csca",
                 "statistics": "statistics",
                 # NBSE Class XII (HSSLC): the subjects not named above.
                 "entrepreneurship": "entrepreneurship", "fundamentals of business mathematics": "fbm",
                 "informatics practices": "ip", "philosophy": "philosophy",
                 # MBSE XII
                 "business mathematics": "bmath", "public administration": "pubad",
                 # BSEM HSLC: the additional subjects Core9X teaches (one, or none) not named above.
                 "higher mathematics": "hmaths", "commerce": "commerce",
                 # MBOSE XII (HSSLC): English Core is the compulsory English; Elective English and Physical
                 # Education are electives.
                 "english core": "english", "elective english": "eleng", "physical education": "pe",
                 # ISC (CISCE Class XII): the subjects not named above.
                 "accounts": "accountancy", "environmental science": "evs", "biotechnology": "biotech",
                 "applied mathematics": "appmaths",
                 # ICSE Class X: the Group II and III electives not named above.
                 "economic applications": "ecoapps", "commercial applications": "commapps", "cookery": "cookery",
                 "fashion designing": "fashion", "yoga": "yoga", "technical drawing": "techdrawing",
                 "robotics and artificial intelligence": "robotics", "mass media and communication": "massmedia",
                 "hospitality management": "hospitality",
                 # Manipur Class XII (COHSEM's HSE): the subject not named above.
                 "human ecology and family sciences": "homesci"}


# A chapter file's board, where Core9X files it under another board's code.
BOARD_CODES = {"COHSEM": "BSEM"}


class ImportError_(ValueError):
    pass


@dataclass
class ParsedLesson:
    kind: str
    title: str
    body_md: str
    sort: int

    @property
    def slug(self) -> str:
        return slugify(f"{self.kind}-{self.title}")

    @property
    def est_minutes(self) -> int:
        return max(2, round(len(self.body_md.split()) / 150))


def lesson_order(lessons: list) -> list:
    """The learning objectives first, so a student knows what to look for before reading (the files have them as
    section 2, after the lesson), then everything else as the file has it. Renumbers `sort` 1, 2, 3 …; works on
    parsed lessons and on Lesson rows alike."""
    ordered = sorted(lessons, key=lambda l: (l.kind != "objectives", l.sort))
    for i, lesson in enumerate(ordered, 1):
        lesson.sort = i
    return ordered


@dataclass
class ParsedQuestion:
    local_id: str  # e.g. "mcq-017", "case2-iii"
    qtype: str
    stem_md: str
    marks: float
    sort: int
    options: list[dict] | None = None
    answer: dict | None = None
    explanation_md: str | None = None
    solution_md: str | None = None
    topic: str | None = None
    parent_local_id: str | None = None
    part_label: str | None = None
    marking_scheme: list[dict] | None = None


@dataclass
class ParsedChapter:
    meta: dict[str, str]
    kind: str
    number: int
    title: str
    subject_code: str
    grade_code: str
    board_code: str
    lessons: list[ParsedLesson] = field(default_factory=list)
    questions: list[ParsedQuestion] = field(default_factory=list)
    topics: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def uid_prefix(self) -> str:
        kind = {"chapter": "ch", "poem": "poem", "supplementary": "sr", "play": "play", "skills": "skill"}[self.kind]
        return f"{self.board_code}-{self.grade_code}-{self.subject_code}-{kind}{self.number:02d}".lower()


def _clean(lines: list[str]) -> str:
    text = "\n".join(lines).strip()
    text = re.sub(r"\n-{3,}\s*$", "", text).strip()
    return text


def _split_sections(lines: list[str]) -> tuple[list[str], dict[int, tuple[str, list[str]]]]:
    head: list[str] = []
    sections: dict[int, tuple[str, list[str]]] = {}
    current: int | None = None
    for line in lines:
        m = SECTION_RE.match(line)
        if m:
            current = int(m.group(1))
            sections[current] = (m.group(2), [])
        elif current is None:
            head.append(line)
        else:
            sections[current][1].append(line)
    return head, sections


def _split_blocks(lines: list[str]) -> list[tuple[str | None, int, str | None, list[str]]]:
    """Split a question section into (group heading, number, label, block lines)."""
    blocks = []
    group = None
    current = None
    for line in lines:
        sm = SUB_RE.match(line)
        if sm:
            group = QGROUP_SUFFIX_RE.sub("", sm.group(1)).strip()
            current = None
            continue
        qm = Q_RE.match(line)
        if qm:
            current = (group, int(qm.group(1)), qm.group(2), [qm.group(3)] if qm.group(3) else [])
            blocks.append(current)
        elif current is not None:
            current[3].append(line)
    return blocks


def _answer_and_explanation(lines: list[str]) -> tuple[list[str], list[str], list[str]]:
    """Split block lines into (before answer, answer, explanation)."""
    pre, ans, expl = [], [], []
    target = pre
    for line in lines:
        am = ANS_RE.match(line)
        em = EXPL_RE.match(line)
        if am and target is pre:
            target = ans
            if am.group(1):
                ans.append(am.group(1))
        elif em and target is not expl:
            target = expl
            if em.group(1):
                expl.append(em.group(1))
        else:
            target.append(line)
    return pre, ans, expl


def _marking(ans: list[str]) -> tuple[list[str], list[dict] | None]:
    """Take a "**Marking:**" list off the end of a model answer: "- Format: sender, date, subject — 2 marks"."""
    start = next((i for i, line in enumerate(ans) if MARKING_RE.match(line.strip())), None)
    if start is None:
        return ans, None
    scheme = [{"point": m.group(1), "marks": float(m.group(2))}
              for m in (MARK_POINT_RE.match(line.strip()) for line in ans[start + 1:]) if m]
    return ans[:start], scheme or None


def _options(pre: list[str]) -> tuple[list[str], list[dict]]:
    stem, options = [], []
    for line in pre:
        om = OPT_RE.match(line.strip())
        if om:
            options.append({"key": om.group(1), "text": om.group(2).strip()})
        elif options and line.strip() and not line.startswith("- "):
            options[-1]["text"] += " " + line.strip()
        elif not options:
            stem.append(line)
    return stem, options


def _mcq_key(ans_text: str) -> str | None:
    m = KEY_LETTER_RE.match(ans_text.strip())
    return m.group(1) if m else None


def parse_chapter(path: Path) -> ParsedChapter:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    head, sections = _split_sections(lines)

    meta: dict[str, str] = {}
    for line in head:
        m = META_ROW_RE.match(line)
        if m and m.group(1) not in ("Field", "---") and not set(m.group(1)) <= {"-"}:
            meta[m.group(1)] = m.group(2)

    fm = re.match(r"^(Ch|Poem|SR|Play|Skill)(\d+)", path.name, re.I)
    if not fm:
        raise ImportError_(f"{path.name}: file name must start with Ch01 / Poem01 / SR01 / Play01 / Skill01")
    kind = FILE_KIND[fm.group(1).lower()]
    number = int(fm.group(2))

    subject_raw = meta.get("Subject", "").strip().lower()
    subject_code = SUBJECT_CODES.get(subject_raw)
    if not subject_code:
        raise ImportError_(f"{path.name}: unknown subject {meta.get('Subject')!r}")
    grade_code = meta.get("Class", "").strip().upper()
    board_code = "MBOSE" if meta.get("Board", "").upper().startswith("MBOSE") else meta.get("Board", "").split()[0]
    # Manipur's Class XII is examined by COHSEM and its Class X by BSEM; Core9X lists both under one Manipur board.
    board_code = BOARD_CODES.get(board_code, board_code)
    # "The Last Lesson (Prose)" and BSEM's "Sagol Kangjei (Course Book — Prose)" are titled without the book part.
    title = re.sub(r"\s*\((?:Course Book\s*[—–-]\s*)?(Prose|Poem|Poetry|Play|Supplementary)[^)]*\)\s*$", "",
                   meta.get("Title", "").strip()) or \
        (head[0].lstrip("# ").strip() if head else path.stem)

    ch = ParsedChapter(meta=meta, kind=kind, number=number, title=title, subject_code=subject_code,
                       grade_code=grade_code, board_code=board_code)

    # Lessons ---------------------------------------------------------------------------------
    sort = 0
    if 1 in sections:
        parts: list[tuple[str, list[str]]] = []
        for line in sections[1][1]:
            sm = SUB_RE.match(line)
            if sm:
                parts.append((sm.group(1), []))
            elif parts:
                parts[-1][1].append(line)
            elif line.strip():
                parts.append(("Introduction", [line]))
        for ptitle, plines in parts:
            body = _clean(plines)
            if body:
                sort += 1
                ch.lessons.append(ParsedLesson("lesson", ptitle, body, sort))
    for number_, kind_ in NOTE_SECTIONS.items():
        if number_ in sections:
            title_, body_lines = sections[number_]
            body = _clean(body_lines)
            if body:
                sort += 1
                ch.lessons.append(ParsedLesson(kind_, title_, body, sort))
    ch.lessons = lesson_order(ch.lessons)

    # Questions -------------------------------------------------------------------------------
    qsort = 0

    def add(q: ParsedQuestion) -> None:
        nonlocal qsort
        qsort += 1
        q.sort = qsort
        ch.questions.append(q)

    if 9 in sections:
        for group, n, _label, block in _split_blocks(sections[9][1]):
            pre, ans, expl = _answer_and_explanation(block)
            stem, options = _options(pre)
            key = _mcq_key(" ".join(ans))
            if len(options) != 4 or key is None:
                ch.warnings.append(f"MCQ Q{n}: expected 4 options and a lettered answer; skipped")
                continue
            if group and group not in ch.topics:
                ch.topics.append(group)
            add(ParsedQuestion(f"mcq-{n:03d}", "mcq", _clean(stem), 1, 0, options=options, answer={"key": key},
                               explanation_md=_clean(expl) or None, topic=group))

    for sec, qtype, marks, prefix in ((10, "short", 2, "sa"), (11, "long", 5, "la"), (12, "short", 3, "comp")):
        if sec in sections:
            for group, n, label, block in _split_blocks(sections[sec][1]):
                gm = GROUP_MARKS_RE.search(group or "")
                q_marks = int(gm.group(1)) if gm else marks
                pre, ans, expl = _answer_and_explanation(block)
                ans, scheme = _marking(ans)
                stem = _clean(pre)
                if label:
                    stem = f"*{label}.* {stem}"
                solution = _clean(ans)
                if not stem or not solution:
                    ch.warnings.append(f"Section {sec} Q{n}: missing question or answer; skipped")
                    continue
                if scheme and sum(p["marks"] for p in scheme) != q_marks:
                    ch.warnings.append(f"Section {sec} Q{n}: the marking points add up to "
                                       f"{sum(p['marks'] for p in scheme):g}, not {q_marks}")
                add(ParsedQuestion(f"{prefix}-{n:03d}", qtype, stem, q_marks, 0, solution_md=solution,
                                   explanation_md=_clean(expl) or None, marking_scheme=scheme))

    if 13 in sections:
        sec_lines = sections[13][1]
        first_q = next((i for i, l in enumerate(sec_lines) if Q_RE.match(l)), len(sec_lines))
        _stem, ar_options = _options(sec_lines[:first_q])
        if len(ar_options) != 4:
            ch.warnings.append("Assertion–Reason: could not read the four standard options")
        for _group, n, _label, block in _split_blocks(sec_lines):
            pre, ans, expl = _answer_and_explanation(block)
            a = next((AR_A_RE.match(l).group(1) for l in pre if AR_A_RE.match(l)), None)
            r = next((AR_R_RE.match(l).group(1) for l in pre if AR_R_RE.match(l)), None)
            key = _mcq_key(" ".join(ans))
            if not (a and r and key and len(ar_options) == 4):
                ch.warnings.append(f"Assertion–Reason Q{n}: incomplete; skipped")
                continue
            add(ParsedQuestion(f"ar-{n:03d}", "assertion_reason",
                               f"**Assertion (A):** {a}\n\n**Reason (R):** {r}", 1, 0,
                               options=[dict(o) for o in ar_options], answer={"key": key},
                               explanation_md=_clean(expl) or None))

    if 14 in sections:
        cases: list[tuple[str, list[str]]] = []
        for line in sections[14][1]:
            sm = SUB_RE.match(line)
            if sm:
                cases.append((sm.group(1), []))
            elif cases:
                cases[-1][1].append(line)
        for ci, (ctitle, clines) in enumerate(cases, start=1):
            first_part = next((i for i, l in enumerate(clines) if PART_RE.match(l)), None)
            if first_part is None:
                ch.warnings.append(f"Case {ci}: no parts found; skipped")
                continue
            passage = _clean(clines[:first_part])
            parent_id = f"case{ci}"
            title_clean = re.sub(r"^(?:Case|Passage) \d+\s*[—–-]\s*", "", ctitle).strip()
            parent = ParsedQuestion(parent_id, "case", f"**{title_clean}**\n\n{passage}", 4, 0)
            add(parent)
            part_blocks: list[tuple[str, list[str]]] = []
            for line in clines[first_part:]:
                pm = PART_RE.match(line)
                if pm:
                    part_blocks.append((pm.group(1), [pm.group(2)] if pm.group(2) else []))
                elif part_blocks:
                    part_blocks[-1][1].append(line)
            for label, block in part_blocks:
                pre, ans, expl = _answer_and_explanation(block)
                stem, options = _options(pre)
                key = _mcq_key(" ".join(ans)) if options else None
                if options and len(options) == 4 and key:
                    q = ParsedQuestion(f"{parent_id}-{label}", "mcq", _clean(stem), 1, 0, options=options,
                                       answer={"key": key}, explanation_md=_clean(expl) or None)
                else:
                    q = ParsedQuestion(f"{parent_id}-{label}", "short", _clean(pre), 1, 0,
                                       solution_md=_clean(ans), explanation_md=_clean(expl) or None)
                q.parent_local_id = parent_id
                q.part_label = f"({label})"
                add(q)
            # A set is worth its parts: the literature extracts 4 × 1, a reading passage 10 × 1.
            parent.marks = sum(q.marks for q in ch.questions if q.parent_local_id == parent_id) or 4

    # Cross-check MCQ answers with the quick key in 17.1 ---------------------------------------
    if 17 in sections:
        key_table: dict[int, str] = {}
        in_key = False
        for line in sections[17][1]:
            if line.startswith("### 17.1"):
                in_key = True
                continue
            if in_key and line.startswith("### "):
                break
            if in_key and line.startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                for i in range(0, len(cells) - 1, 2):
                    if cells[i].isdigit() and re.fullmatch(r"[a-d]", cells[i + 1]):
                        key_table[int(cells[i])] = cells[i + 1]
        for q in ch.questions:
            if q.qtype == "mcq" and q.local_id.startswith("mcq-"):
                n = int(q.local_id[4:])
                if n in key_table and key_table[n] != q.answer["key"]:
                    ch.warnings.append(f"MCQ Q{n}: answer {q.answer['key']} disagrees with key table {key_table[n]}")

    # Images --------------------------------------------------------------------------------------
    for item in [*ch.lessons, *ch.questions]:
        for field_name in ("body_md", "stem_md", "solution_md", "explanation_md"):
            value = getattr(item, field_name, None)
            if value:
                for m in IMG_RE.finditer(value):
                    if m.group(2) not in ch.images:
                        ch.images.append(m.group(2))
    return ch


def media_prefix(ch: ParsedChapter) -> str:
    return f"/media/{ch.board_code}/{ch.grade_code}/{ch.subject_code}".lower()


def rewrite_images(md: str | None, prefix: str) -> str | None:
    if not md:
        return md
    return IMG_RE.sub(lambda m: f"{m.group(1)}{prefix}/{m.group(2)}{m.group(3)}", md)


def copy_images(ch: ParsedChapter, source_dir: Path, media_dir: Path) -> list[str]:
    missing = []
    target = media_dir / media_prefix(ch).removeprefix("/media/")
    for rel in ch.images:
        src = source_dir / rel
        if not src.exists():
            missing.append(rel)
            continue
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    return missing
