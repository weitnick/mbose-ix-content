# MBOSE Class IX content — cloud run

You are writing study content for **MBOSE (Meghalaya Board of School Education) Class IX**, 2026 syllabus, for the
Core9X platform. English and Mathematics are already done (outside this repo). This repo covers the rest:

1. **Science** — 12 chapters (do first)
2. **Social Science** — 12 examined chapters
3. **Health and Physical Education** — only after 1 and 2 are complete
4. **Computer Science** — last

Work straight through without stopping to ask. When a decision is open, take the sensible default, write it under
**Decisions** in `PLAN.md`, and carry on. The user reviews everything afterwards.

**After every finished chapter: commit and push** (the `.md`, the `.docx`, its figures, and the updated `PLAN.md`).
The run may be stopped at any time when the credit runs out, so nothing should sit uncommitted.

## Repository layout

```
<Subject>/NCERT Content/       source books (read only)
<Subject>/Generated Content/   your output: ChNN - <Title> - Content.md + .docx, figures/<prefix>_chNN_figMM_*.png
reference/syllabus/            MBOSE syllabus compilation + the two revised notifications (SS 28 Aug 2026, HPE 24 Aug 2026)
reference/sample-papers/       MBOSE SSLC (Class X) sample papers: the board's question style and pattern
reference/templates/           finished chapters from Class X (and IX Maths) — copy their structure exactly
tools/                         finalize, rebalance, docx builder, figure helpers
PLAN.md                        chapter list, progress checklist, decisions
```

The templates' figure images are not included; only their file names and Markdown references matter.

## Setup (once per container)

```bash
cd tools && npm ci && cd ..
pip install -r tools/requirements.txt
```

The Python scripts add `tools/pylib` to `sys.path`; that folder holds Windows builds and is deliberately absent here.
Ignore it — the pip packages are used instead. `tools/word_check.ps1` is Windows-only: do not run it; the user runs
the Word check locally after pulling.

## Sources

- **Science:** NCERT *Science* Class IX, the rationalised book, **Reprint 2025-26**, `Science/NCERT Content/iesc101–112.pdf`
  (+ `iesc1an.pdf` answers, `iesc1ps.pdf` prelims). This is the book MBOSE prescribes ("Science Class 9, NCERT
  Meghalaya Edition"). NCERT has since replaced it with a new book called *Exploration* — **do not use Exploration.**
- **Social Science:** MBOSE prescribes Goyal *Core Social Science – IX*, which is **not available**. Follow the revised
  DERT syllabus (`reference/syllabus/Revised Syllabus social science 1 - IX.pdf`, Class IX part) and the matching
  chapters of the rationalised NCERT IX books in `Social Science/NCERT Content/`:
  `iess1xx` *Contemporary India – I* (Geography), `iess2xx` *Economics*, `iess3xx` *India and the Contemporary World – I*
  (History), `iess4xx` *Democratic Politics – I*. Say so in each file's *Textbook source* row, as the Class X template does.
- **HPE:** Frank Brothers *Health – A Textbook for Secondary School, Class IX* — **not available**. Follow the revised HPE
  syllabus (`reference/syllabus/Health Education VI to X syllabus.pdf`, Class IX part, effective 2026).
- **Computer Science:** *Click Start 9 – Computer Science for Schools* (Cambridge University Press) — **not available** and
  no syllabus file is on hand. First look for an official MBOSE/DERT Class IX Computer Science syllabus on mbose.in or
  megeducation.gov.in; if there is none, plan the chapters from the book's published contents and from what Class X CS
  assumes students already know (see the Class X CS template). Record the source of the chapter plan in `PLAN.md`.
- Extract NCERT text once per chapter into `<Subject>/NCERT Content/txt/<code>.txt` (pypdf) and commit it, so a later
  container does not have to extract again.

Where `PLAN.md` and the official syllabus disagree, **the syllabus wins**; fix `PLAN.md` and note it under Decisions.

## File format — copy the templates

Every chapter is one Markdown file with the **same structure as the templates in `reference/templates/`**. The Core9X
importer and `tools/build_review_docx.js` parse it, so keep headings, table fields and numbering exactly as there.

- Title line `# <Title>`, then the metadata table with these rows in this order: Board, Class (**IX**), Subject, Chapter,
  Title, Textbook source, Exam weightage, Syllabus scope. Keep rows short — Exam weightage becomes the .docx subtitle.
  - Subject values: `Science`, `Social Science`, `Health and Physical Education`, `Computer Science`.
  - Chapter value: Science uses the plain number (`1`). Social Science uses `History · Chapter 1` style with the
    **book's** chapter number from the syllabus (not the file number). HPE uses `Unit I · Chapter 1`. CS uses
    `<Unit> · Chapter 1`.
- Then the `> **Note on the text:**` block (and `> **Syllabus note:**` where parts are cut or internal-only).
- Then the 17 sections, `## N. Name`, in this order: 1 Complete Lesson, 2 Learning Objectives, 3 Detailed Section
  Explanations, 4 Vocabulary, 5 Important Facts, 6 Person Profiles, 7 Key Ideas / Real-Life Connections,
  8 Exam-Oriented Questions, 9 MCQs with Explanations, 10 Short-Answer Questions, 11 Long-Answer Questions,
  12 Competency / Application, 13 Assertion–Reason, 14 Case-Based Questions, 15 Revision Notes, 16 Chapter Test,
  17 Complete Answer Key. Use the exact heading wording of the matching subject template.
- **Section 8** opens with the "How this chapter is examined (MBOSE pattern)" box. 8.1 solves **every** in-text and
  end-of-chapter textbook question (quote each question so it can be matched to the book). There are **no MBOSE
  Class IX board papers**, so instead of the Class X past-paper subsection write **8.2 High-probability exam questions**
  in the board's style (as `IX Mathematics Ch01` does), solved.
- Marks come from `###` group headings in sections 10 and 11 (e.g. `### Short answers (2 marks each)`); the importer
  reads them, so always include them.
- MCQs: exactly four options (a)–(d); `**Answer:** (x) …` and `**Explanation:** …` lines as in the templates. Use real
  distractors; "All/None of the above" only where it is genuinely right or tempting. Spread the keys evenly — run
  `python tools/rebalance_mcq.py <md>` between two `python tools/finalize_chapter.py <md>` passes. finalize numbers the
  `**Q#.**` placeholders, rebuilds the section 17 key and checks the MCQs; it does not catch a wrong key, so check keys
  yourself. Every explanation must have real text.
- Case-based questions: four cases, each a fresh passage with four 1-mark items (i)–(iv), one built on a table or data.
- Write everything in your own words. **Never copy textbook passages**; retell them. Quote textbook *questions* only
  (8.1). Use Meghalaya settings where they fit naturally (Shillong, Tura, Jowai, Wangala, Nongkrem).

### Per-subject numbers

| | MCQs | Short answers | Long answers | Chapter test (40 marks) |
|---|---|---|---|---|
| Science | 60–80 | 2 and 3 marks | `### Long answers (4 marks each)` | A 10×1; B any 5 of 7 ×2; C any 4 of 6 ×3; D any 2 of 3 ×4 |
| Social Science | 52+ (write ~55) | `### Short answers (2 marks each)` | `### Long answers (5 marks each)` | History/Geography: A 10×1, B 5 of 7 ×2, C 2 of 3 ×5, D 1 case ×4, E map 6 of 8 ×1. Civics/Economics: A 12×1, B 5 of 7 ×2, C 2 of 3 ×5, D 2 cases ×4. A chapter with no map work uses 16 MCQs instead of E. |
| HPE | 52–58 | 2 and 3 marks | 5 marks | A 10×1; B 3 of 4 ×2; C 3 of 4 ×3; D 3 of 4 ×5 |
| Computer Science | 52–55 | 2 and 3 marks | 5 marks | as HPE |

**Exam patterns** (MBOSE Class IX has one final exam, 80 external + 20 internal; no IX paper exists, so the "How this
chapter is examined" box uses the SSLC pattern of the same subject from `reference/sample-papers/`, and says so):
- Science: A 30 MCQ ×1; B any 10 of 14 ×2 (≤30 words); C any 6 of 9 ×3 (≤50 words); D any 3 of 5 ×4 (≤70 words, mostly
  labelled diagrams). Chapter marks are in the syllabus (see `PLAN.md`); put them in *Exam weightage*.
- Social Science: A 30 MCQ ×1; B any 9 of 12 ×2 (30 words); C 4 either/or ×5 (80 words); D 2 either/or case-based ×4
  (Civics, Economics); E map work, any 4 of 7 ×1 (History, Geography). If the revised syllabus gives a Class IX
  design or blueprint, use that instead and record it.
- HPE and CS: A 30 ×1; B 6 of 9 ×2; C 6 of 9 ×3; D 4 of 7 ×5 — unless the HPE syllabus sets a different IX design.

## Figures

Draw every figure with matplotlib (no copying textbook images). One script per chapter in `tools/figures/`, named
`ix_sci_chNN_<slug>.py`, `ix_ss_chNN_<slug>.py`, `ix_hpe_chNN_<slug>.py`, `ix_cs_chNN_<slug>.py`. Reuse the Class X
helpers: `x_sci_ch05_life_processes.py` (`smooth`, `blob`, `tube_path`, `label`, `finish`, `save`), `x_sci_ch09_light.py`,
`x_sci_ch11_electricity.py` (circuits), `x_ss_common.py` (`timeline`, `tree`, `flow`, `box`, `arrow`, `table_fig`),
`x_hpe_common.py`, `x_cs_common.py`. Import numpy after `x_ss_common`. Those helpers set a module-level `OUT` that
points at the Class X folders on the user's PC (`../../Class X Content/...`); in every IX script reassign it right after
the import (e.g. `import x_ss_common as c; c.OUT = <repo>/Social Science/Generated Content/figures`), since `save()`
reads `OUT` when it is called. Output to
`<Subject>/Generated Content/figures/<sci|ss|hpe|cs>_chNN_figMM_<slug>.png` and reference them from the Markdown with
a relative path, as the templates do. Social Science map work is a table (no outline-map figure).

## Build and check each chapter

```bash
python tools/finalize_chapter.py "<md>"          # numbers questions, rebuilds the key, checks MCQs
python tools/rebalance_mcq.py "<md>"             # evens out the answer letters
python tools/finalize_chapter.py "<md>"
python tools/latex_check.py "<md>"               # maths delimiters
PYTHONIOENCODING=utf-8 python tools/chem_balance_check.py "<md>"   # Science chemistry chapters
node tools/build_review_docx.js "<md>" "<same name>.docx" "<today, e.g. 22 Oct 2026>"
```

Fix anything they report before committing. Then tick the chapter in `PLAN.md`, commit and push.

## Gotchas (learned on Class X)

- A dollar sign is the maths delimiter; never write one in prose or code. Write money as "Rs" or "₹".
- Chemistry: plain Unicode formulas (H₂SO₄, SO₄²⁻, ↓ ↑); `$\xrightarrow{\text{heat}}$` only for arrows with
  conditions. Put Ω outside maths. `\oplus` is unsupported — write ⊕ as text.
- HTML or angle-bracket tags in Markdown must be in backticks or a code fence, or they disappear.
- finalize's duplicate-option check is case-insensitive ("small z" / "capital Z", not "z" / "Z"); its duplicate-stem
  check ignores symbols, so add words to tell such stems apart.
- Write backslashes in generated text carefully: a shell heredoc piped into Python can turn `\b`, `\f`, `\n` into
  control characters and the .docx will not open. Before building, check the file for `[\x00-\x08\x0b\x0c\x0e-\x1f]`.
- Social Science chapters with no NCERT source (Meghalaya's resistance, Major Relief Features of the Earth) are written
  from reliable general sources: add a `> **Check note:**` saying the Goyal book was not available and the facts should
  be checked against it, and list any fact you are unsure of under Decisions in `PLAN.md`.
- Keep the token cost down: read each NCERT chapter's text once, write the chapter in a few large edits, and use grep
  rather than re-reading whole chapter files to check them.
