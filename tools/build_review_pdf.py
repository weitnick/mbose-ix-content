"""Render a chapter content Markdown file to print-ready HTML (then printed to PDF by Edge)."""
import html
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt

src = Path(sys.argv[1])
out = Path(sys.argv[2])
review_date = sys.argv[3] if len(sys.argv) > 3 else ""

text = src.read_text(encoding="utf-8")

# Split the cover block (H1 + metadata table + note) from the numbered sections.
first_h2 = text.index("\n## ")
cover_md, body_md = text[:first_h2], text[first_h2:]
title = re.search(r"^# (.+)$", cover_md, re.M).group(1).strip()
cover_md = re.sub(r"^# .+\n", "", cover_md, count=1, flags=re.M).strip()
cover_md = re.sub(r"\n---\s*$", "", cover_md)

# Chapter details for the cover band, subtitle and running headers come from the metadata table.
meta = {}
for row in re.findall(r"^\|(.+)\|\s*$", cover_md, re.M):
    cells = [c.strip() for c in row.split("|")]
    if len(cells) == 2 and not set(cells[0]) <= set("-: "):
        meta[cells[0]] = re.sub(r"[*_]", "", cells[1])
chapter = meta.get("Chapter", "")
band = " &middot; ".join(html.escape(x) for x in (
    meta.get("Board", "MBOSE").split(" ")[0], "Class " + meta.get("Class", ""),
    meta.get("Subject", ""), "Chapter " + chapter))
if "Part I" in meta:
    subtitle = (f"Prose &middot; Part I: {html.escape(meta['Part I'].split(' (by')[0])}"
                f" &middot; Part II: {html.escape(meta.get('Part II', ''))}")
else:
    subtitle = f"{html.escape(meta.get('Genre', ''))} &middot; by {html.escape(meta.get('Author', ''))}"
header_left = f"{title} \\2014  Chapter {chapter}".replace('"', "'")
header_right = f"MBOSE \\00B7  Class {meta.get('Class', '')} \\00B7  {meta.get('Subject', '')}"

md = MarkdownIt("commonmark", {"breaks": True, "html": False}).enable("table")

def slug(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def polish(h):
    br = r"<br\s*/?>\n"
    # Answer / explanation / model-answer blocks become their own styled paragraphs.
    for label, cls in (("Answer:", "answer"), ("Model answer:", "answer"), ("Explanation:", "explain")):
        h = re.sub(br + rf"<strong>{label}</strong>", f'</p>\n<p class="{cls}"><strong>{label}</strong>', h)
        h = h.replace(f"<p><strong>{label}</strong>", f'<p class="{cls}"><strong>{label}</strong>')
    # Question paragraphs and MCQ option lists.
    h = re.sub(r"<p><strong>(Q\d+\.|\d+\.)</strong>", r'<p class="q"><strong>\1</strong>', h)
    h = re.sub(r"<ul>\n<li>\(a\)", '<ul class="options">\n<li>(a)', h)
    # Assertion / Reason lines.
    h = h.replace("<strong>A:</strong>", '<span class="tag tag-a">A</span>')
    h = h.replace("<strong>R:</strong>", '<span class="tag tag-r">R</span>')
    # Horizontal rules between sections are replaced by page breaks.
    h = h.replace("<hr />\n", "")
    # Wrap wide tables so they never overflow.
    h = h.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    return h

body_html = polish(md.render(body_md))

toc = []
def add_id(m):
    level, inner = m.group(1), m.group(2)
    anchor = slug(inner)
    if level == "2":
        toc.append((anchor, re.sub(r"<[^>]+>", "", inner)))
    return f'<h{level} id="{anchor}">{inner}</h{level}>'
body_html = re.sub(r"<h([23])>(.*?)</h\1>", add_id, body_html)

cover_html = polish(md.render(cover_md))
toc_html = "\n".join(
    f'<li><a href="#{a}"><span class="toc-num">{t.split(".", 1)[0]}</span>'
    f'<span class="toc-name">{html.escape(t.split(".", 1)[1].strip())}</span></a></li>'
    for a, t in toc
)

css = r"""
@page {
  size: A4;
  margin: 20mm 17mm 20mm 17mm;
  @top-left { content: "__HEADER_LEFT__"; font: 8pt "Segoe UI", sans-serif; color: #7a8594; }
  @top-right { content: "__HEADER_RIGHT__"; font: 8pt "Segoe UI", sans-serif; color: #7a8594; }
  @bottom-center { content: "Page " counter(page) " of " counter(pages); font: 8pt "Segoe UI", sans-serif; color: #7a8594; }
}
@page :first {
  @top-left { content: none; } @top-right { content: none; } @bottom-center { content: none; }
}
:root {
  --ink: #1d2733; --muted: #5d6b7a; --accent: #1f4e79; --accent-soft: #e9f0f7;
  --rule: #cfd8e3; --ans: #2e7d32; --ans-bg: #eef7ef; --exp-bg: #f4f6f8;
  --quote: #b7791f; --quote-bg: #fdf7ea;
}
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif; font-size: 10.3pt; line-height: 1.5; color: var(--ink); background: #fff; margin: 0; }

/* Cover */
.cover { height: 257mm; display: flex; flex-direction: column; break-after: page; }
.cover .band { font-size: 9pt; letter-spacing: .18em; text-transform: uppercase; color: var(--accent); font-weight: 600; border-bottom: 2px solid var(--accent); padding-bottom: 6px; }
.cover h1 { font-family: Georgia, "Times New Roman", serif; font-size: 34pt; line-height: 1.1; margin: 16mm 0 3mm; color: var(--accent); font-weight: 700; }
.cover .sub { font-size: 12.5pt; color: var(--muted); margin: 0 0 8mm; }
.cover .status { display: inline-block; font-size: 8.5pt; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: #8a5a00; background: #fff3d6; border: 1px solid #f0d58c; border-radius: 3px; padding: 3px 8px; margin-bottom: 7mm; align-self: flex-start; }
.cover .meta table { font-size: 9.4pt; }
.cover blockquote { margin-top: 5mm; }
.cover .toc-title { font-size: 10pt; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: .1em; margin: 7mm 0 2mm; }
.toc { list-style: none; padding: 0; margin: 0; columns: 2; column-gap: 10mm; font-size: 9.6pt; }
.toc li { break-inside: avoid; border-bottom: 1px dotted var(--rule); padding: 2.2px 0; }
.toc a { color: var(--ink); text-decoration: none; display: flex; gap: 6px; }
.toc-num { color: var(--accent); font-weight: 700; min-width: 1.6em; }

/* Headings */
h2 { break-before: page; font-family: Georgia, "Times New Roman", serif; font-size: 20pt; color: #fff; background: var(--accent); margin: 0 0 5mm; padding: 9px 14px; border-radius: 3px; font-weight: 700; }
h3 { font-size: 13pt; color: var(--accent); border-bottom: 1.5px solid var(--rule); padding-bottom: 3px; margin: 7mm 0 3mm; break-after: avoid; }
h4 { font-size: 11pt; color: var(--ink); margin: 5mm 0 2mm; break-after: avoid; }
h2 + h3 { margin-top: 2mm; }
p { margin: 0 0 2.4mm; }
ul, ol { margin: 0 0 3mm; padding-left: 6mm; }
li { margin: 0 0 1mm; }
a { color: var(--accent); }
em { color: #334155; }

/* Tables */
.tbl { margin: 2mm 0 4mm; }
table { width: 100%; border-collapse: collapse; font-size: 9.2pt; line-height: 1.38; }
th { background: var(--accent-soft); color: var(--accent); text-align: left; font-weight: 700; }
th, td { border: 1px solid var(--rule); padding: 4px 7px; vertical-align: top; }
tr { break-inside: avoid; }
thead { display: table-header-group; }
tbody tr:nth-child(even) td { background: #fafbfc; }

/* Passages and notes */
blockquote { margin: 3mm 0 4mm; padding: 3mm 4.5mm; background: var(--quote-bg); border-left: 3.5px solid var(--quote); border-radius: 0 3px 3px 0; break-inside: avoid; }
blockquote p:last-child { margin-bottom: 0; }

/* Questions */
p.q { margin: 4.2mm 0 1.4mm; break-after: avoid; }
p.q strong:first-child { color: var(--accent); }
ul.options { list-style: none; padding-left: 5mm; margin: 0 0 1.8mm; break-before: avoid; break-inside: avoid; }
ul.options li { margin: 0 0 .6mm; break-inside: avoid; }
p.answer { background: var(--ans-bg); border-left: 3px solid var(--ans); padding: 1.6mm 3mm; margin: 0 0 1mm; break-inside: avoid; break-before: avoid; }
p.answer strong:first-child { color: var(--ans); }
p.explain { background: var(--exp-bg); border-left: 3px solid #9aa7b4; padding: 1.6mm 3mm; margin: 0 0 2mm; font-size: 9.7pt; color: #334155; break-inside: avoid; break-before: avoid; }
p.explain strong:first-child { color: #475569; }
.tag { display: inline-block; font-weight: 700; font-size: 8.5pt; color: #fff; border-radius: 2px; padding: 0 5px; margin-right: 4px; }
.tag-a { background: #1f4e79; } .tag-r { background: #7c3aed; }
"""

css = css.replace("__HEADER_LEFT__", header_left).replace("__HEADER_RIGHT__", header_right)

doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)} — Content Review</title>
<style>{css}</style></head>
<body>
<section class="cover">
  <div class="band">{band}</div>
  <h1>{html.escape(title)}</h1>
  <p class="sub">{subtitle}</p>
  <span class="status">Content review draft{(' &middot; ' + html.escape(review_date)) if review_date else ''}</span>
  <div class="meta">{cover_html}</div>
  <div class="toc-title">Contents</div>
  <ol class="toc">{toc_html}</ol>
</section>
{body_html}
</body></html>"""

out.write_text(doc, encoding="utf-8")
print(f"wrote {out} ({len(doc):,} chars, {len(toc)} sections)")
