# ICSE Class X — deep lessons (cloud run, Oct–Nov 2026)

This folder is a self-contained job. **Ignore the repository-root CLAUDE.md and PLAN.md** (they belong to a different job, MBOSE Class IX). Work only inside `icse-x/`.

## The job

Deepen **Section 1 ("## 1. Complete Lesson")** of all 68 ICSE Class X chapter files in `chapters/`:

| Folder | Files | ICSE paper |
|---|---|---|
| `chapters/English` | 20 | English Language (Paper 1, 80 marks) and Literature in English (Paper 2, 80 marks) |
| `chapters/History and Civics` | 19 | H.C.G. Paper 1 (History & Civics, 80 marks) |
| `chapters/Geography` | 16 | H.C.G. Paper 2 (Geography, 80 marks; includes topographical maps and map of India) |
| `chapters/Computer Applications` | 13 | Computer Applications (Java/BlueJ, 100 marks: 70 theory + 30 internal) |

Core9X (www.core9x.com) is a Class IX–XII study site; ICSE Class X is live with students. The same deep-lesson work is already finished and reviewed for MBOSE, ASSEB and CBSE Class X. **Read `tools/DEPTH_STANDARD.md` first and follow it exactly**, and study one finished example in `examples/` before writing:
- `examples/MBOSE X Science - Ch01 …` — the pilot; the depth, tone and block layout to match;
- `examples/MBOSE X Social Science - Ch05 Resources …` — model answers with "Why this scores" (use for History & Civics, Geography);
- `examples/MBOSE X English - Ch01 A Letter to God …` — literature model answers (use for English);
- `examples/MBOSE X Computer Science - Ch12 Java Programming …` — code examples with output (use for Computer Applications).

### What to add to every `###` part of Section 1
`#### Foundation first` (where the part needs earlier knowledge), the "why", `#### Worked examples` (at least 3, graded basic → board level → twist; model answers with a **"Why this scores"** line for descriptive parts; full programs with output for Java), `#### Doubts cleared`, `#### Mistakes to avoid`, `#### Check yourself` with answers.

### The user's rules
1. **Exam topics only**, judged against the ICSE 2027 syllabus in `sources/syllabus/`. No "beyond the syllabus" / "not examined" material, no next-class ideas. Other sources may be used only to explain a syllabus topic better, in our own words.
2. **Foundation concepts** wherever a topic needs them.
3. **Remove the old "### 5.x Beyond the text" blocks**: `python tools/drop_beyond.py <file>` (the only change allowed outside Section 1).
4. **Never rename or add a `###` heading** — the live site matches lessons by title (students' progress). Delete a part only if the ICSE syllabus does not examine it, and say so in the report.
5. **Marks and answers follow CISCE**: the 2027 specimen papers with marking schemes (`sources/specimen-2027/`) and the 2025 examiner reports (`sources/examiner-reports-2025/`, "Analysis of Pupil Performance" — what examiners reward and where candidates lose marks; use these heavily for "Why this scores" and "Mistakes to avoid").
6. **Citations**: a worked example may name a past/specimen question only if that question is in the SAME file's section 8 (forms used there, e.g. "ICSE 2027 specimen, Q3(i) (4 marks)" or the board-paper labels in 8.2). Never cite anything else.
7. **Accuracy**: verify dates, names, facts (WebSearch where unsure); compile and run every Java program you add (`javac`/`java`, JDK 17+) and state its real output; check every map/grid/scale calculation with a script. For facts that changed after the textbook era, teach the exam answer and add one sentence on the current position.
8. Copyrighted literary texts: paraphrase, or quote only short extracts.
9. Use Sonnet for any helper agents you start.

## Checks per file (all must pass before you commit it)
Run from `icse-x/`:
1. `python tools/drop_beyond.py "<file>"`
2. `python tools/latex_check.py "<file>"` — no UNKNOWN commands
3. `cp "<file>" /tmp/c.md && python tools/finalize_chapter.py /tmp/c.md` — must print "All checks passed" (files without section 9/17: compare with the result on the file in `originals/`)
4. `python tools/depth_audit.py "<file>"` — must print OK (TITLES CHANGED only for an allowed syllabus deletion)
5. `python tools/check_parse.py "<file>"` — 0 warnings, question count unchanged

Do **not** build .docx or PDF files (the overseer rebuilds Word files locally). Do not touch `originals/`, `sources/` or `examples/`.

## Git
Work on a branch named `icse-x-deep`. Commit each subject (or every few chapters) with a clear message, and **push often** so progress is visible even if the run stops. Do not push to `main`.

## Finish
When all 68 files pass, write `icse-x/REPORT.md`: per subject, a table of files with Section 1 words before → after; every syllabus deletion with its evidence; facts a teacher should check; any Java program that could not be run. Commit and push it.
