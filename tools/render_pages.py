"""Render chosen pages of a PDF to PNG for a visual check.

Usage: python render_pages.py <file.pdf> <out_dir> <page> [<page> ...]   (pages are 1-based)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "pylib"))
import pypdfium2 as pdfium

pdf, out_dir, pages = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3:]]
os.makedirs(out_dir, exist_ok=True)
doc = pdfium.PdfDocument(pdf)
stem = os.path.splitext(os.path.basename(pdf))[0][:4]
for n in pages:
    path = os.path.join(out_dir, f"{stem}_p{n:02d}.png")
    doc[n - 1].render(scale=1.1).to_pil().save(path)
    print(path)
