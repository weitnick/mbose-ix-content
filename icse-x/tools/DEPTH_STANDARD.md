# Core9X deep-lesson standard

Started 27 Oct 2026. Every chapter's **Section 1 (Complete Lesson)** is deepened so that a student with a doubt can clear it on Core9X alone, without a guidebook or tutor. Pilot: MBOSE Class X Science Ch01.

## Why

The audit of all 115 MBOSE Class X chapter files (27 Oct 2026) found that the files are long (8,000–21,000 words) but almost all of that is questions. The teaching itself is thin:

- Section 1 (the lesson students read) is 450–5,000 words; Section 3 is a 150-word exam note.
- Worked examples in the lesson: Science 0–4 per chapter (9 of 13 chapters have none), Social Science, HPE and English 0, CS 0–4. Only Maths has a reasonable number (3–16).
- Nothing in the lesson answers the questions students actually ask ("why can't I change the subscript?").

## What to add to every `###` part of Section 1

Each `###` part becomes one lesson page on the site, so every part gets its own blocks. Keep the existing text (it is checked and correct) and add around it:

0. **`#### Foundation first`** — wherever a part depends on something from an earlier class or an earlier chapter (valency and formulas before balancing; fractions and LCM before polynomials; map directions before resources), open the part with a short refresher of exactly that prerequisite: the idea, a quick table or rule, and one small example. Only what this part needs, and only foundation for an exam topic (user, 27 Oct 2026). Skip it when nothing earlier is needed.
1. **Explain the why.** Where the text only states a fact, add one or two sentences of reasoning: why it happens, what causes it, how it links to what the student already knows.
2. **`#### Worked examples`** — graded, each with a full step-by-step solution:
   - *Example 1 (basic)* → *Example 2 (board level)* → *Example 3 (a twist the board likes)*.
   - At least **3 per part** for anything procedural (Maths, numericals, balancing, code, grammar). Maths answers show the board's minimum steps (2 marks: 3 steps; 3 marks: 5; 5 marks: 8).
   - For descriptive subjects (SS, HPE, English literature, theory CS) the worked examples are **model answers**: a 2/3-mark and a long-answer question written the way the examiner marks it, with an **"Why this scores"** line naming the points that earn marks.
   - Use a past board question where one exists, and say so ("SSLC 2024").
3. **`#### Doubts cleared`** — 3–6 real student questions, each `**Q. …?**` followed by a short, plain answer. Pick the doubts teachers hear every year and those behind common wrong MCQ options.
4. **`#### Mistakes to avoid`** — 2–4 bullets: the slips that cost marks.
5. **`#### Check yourself`** — 3 quick questions, then `**Answers:**` with brief working.

Add **"In the exam, write:"** lines where the wording of an answer matters.

## Rules

- **Exam topics only (user, 27 Oct 2026).** Teach only what the board's current syllabus examines — never removed topics, never "beyond the syllabus" or "not examined" boxes, never next-class ideas. Go as deep as needed *on those topics*: other sources (NCERT Exemplar, older NCERT editions, NIOS, the board's guidebook, standard reference books, open resources) may be used to explain a syllabus topic better, but never to add a topic. Rewrite in our own words.
- **Accuracy first.** Check every number with a script (sympy for Maths/Physics; `chem_balance_check.py` for equations). Facts from the NCERT/board book or the official guidebook only.
- **Own words.** Never copy the textbook or a guidebook.
- **Class X reading level.** Short sentences, one idea each. Meghalaya and North-East settings where they fit (Sohra rain, Umiam, Shillong market).
- **Only Section 1 changes.** Do not touch sections 2–17 (questions are numbered and keyed), the header table or the figures. Section 1 should grow to about **2.5–3×** its current length; a lesson page lands at 700–1,800 words.
- Headings: `###` stays the lesson split; new blocks are `####`, or bold labels inside parts that already use `####`.
- **Never rename or add a `###` heading.** The site matches lessons by their title; a renamed part is deleted and re-created, and students lose their "done" ticks on it.

## Porting a deepened lesson to another board (from 28 Oct 2026, ASSEB X first)

Where a board's chapter was adapted from an MBOSE chapter and its `###` titles still match, start from the **final** MBOSE Section 1 in `D:\MBOSE APP\Class X Content\<Subject>\Generated Content\`. It already carries the depth blocks and every accuracy-review fix. Then adapt it:
- **Keep the target file's own `###` titles** exactly as they are. The board is live, and titles carry students' progress.
- **Syllabus:** follow the target board's own 2026-27 syllabus (for ASSEB: `D:\core9X\ASSEB\Class X\Official ASSEB\txt\`). Something MBOSE removed may be examined there, and something MBOSE kept may not be. Never import MBOSE's cut list.
- **Exam pattern:** rewrite every mark value, "In the exam, write" line, step rule and "Why this scores" split for the target board's paper (for ASSEB: HSLC, 90 marks, its own mark tiers).
- **Citations:** a worked example may name a past paper only if that question is in the TARGET file's own section 8 (HSLC for ASSEB). Remove or replace any SSLC or MBOSE citation.
- **Settings:** swap Meghalaya places and festivals for the board's state (Assam: Guwahati, the Brahmaputra, Kaziranga, Majuli, Bihu, Sualkuchi…) where they fit.
- Carry over nothing from MBOSE sections 2–17.
- **Check for MISSING topics, not just extra ones** (lesson from ASSEB, 29 Oct 2026). If the target board's syllabus lists a topic, or its past papers ask it, and the MBOSE lesson dropped it (e.g. complementary angles, constructions, Euclid's lemma in ASSEB), teach it fully. A new `###` part is allowed for such a topic.
- **CBSE X (from 29 Oct 2026):** files are in `D:\core9X\CBSE\Class X\<Subject>\` (no Generated Content folder; Word files are named `<stem> - Content.docx`). Syllabus: `Official CBSE\Curriculum 2026-27\`. Backup: `D:\core9X\CBSE\backups\depth-2026-10-29\<Subject>\`. Past-paper citations use the CBSE form, e.g. "CBSE 2025 (30/1/1), Q22", and must be in the file's own section 8. Check against the marking schemes in `Official CBSE\Marking Schemes\`.

## After editing a chapter

- **Non-exam material already in a file** (a `###` part, solutions or MCQs marked "not for the examination", "optional" or "not from the examination point of view"): remove it, even outside Section 1. A deleted `###` part is the one allowed change to the lesson list. Replace non-exam MCQs with new exam-topic MCQs under the same numbers, so the answer key stays intact. Short "why it works" proofs or derivations of an examined rule stay, labelled "(you will not be asked to prove this)". List every removal in the report. (Overseer ruling, 27 Oct 2026.) This includes MCQs whose explanation says "General knowledge, beyond the textbook": keep one only if the guidebook or a past paper asks or teaches the fact (then give that source in the explanation); otherwise replace it under the same number and letter.

0. `python drop_beyond.py <md>` — removes the old "### 5.x Beyond the text (… not needed for exam answers)" block (user, 27 Oct 2026). It is the only change allowed outside Section 1.
1. `python latex_check.py <md>` (and `chem_balance_check.py` for Science, `PYTHONIOENCODING=utf-8`).
2. `python finalize_chapter.py <md>` must still pass unchanged.
3. Parse with the Core9X importer (no warnings); compare lesson count before/after.
4. `node build_review_docx.js <md> <docx> "<date>"` and check the Word file.
4a. **No PDFs (user, 27 Oct 2026):** "if we dont need pdfs, then lets not waste time on them". The site reads the .md and reviews use the .docx, so don't build PDFs. If one is ever wanted, `docx_to_pdf.py` (Word's own export) is the tool.
5. Production: the user re-imports the chapter with `python -m app.cli import "<md>"` (lessons are matched by title, so students keep their progress).
