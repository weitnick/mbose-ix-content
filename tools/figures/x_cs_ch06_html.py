"""Figures for Class X Computer Science, Ch06: HTML Structure, Text and Lists."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import INK, FILLS, plt, save, table_fig  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

MONO = "DejaVu Sans Mono"


def _frame(ax, x, y, w, h, fc, label, size=9.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08", fc=fc, ec=INK, lw=1.0))
    ax.text(x + 0.12, y + h - 0.12, label, ha="left", va="top", fontsize=size, family=MONO, fontweight="bold", color=INK)


def fig_structure():
    fig, ax = plt.subplots(figsize=(10.5, 4.6))
    # left: the nested structure of the document
    _frame(ax, 0.0, 0.0, 5.0, 4.4, "white", "<HTML>  …  </HTML>")
    _frame(ax, 0.3, 2.75, 4.4, 1.15, FILLS[1], "<HEAD>  …  </HEAD>")
    ax.add_patch(Rectangle((0.6, 2.9), 3.8, 0.45, fc="white", ec=INK, lw=0.8))
    ax.text(2.5, 3.125, "<TITLE> My first page </TITLE>", ha="center", va="center", fontsize=8.6, family=MONO)
    _frame(ax, 0.3, 0.25, 4.4, 2.3, FILLS[2], "<BODY>  …  </BODY>")
    items = ["<H1> heading </H1>", "<P> paragraph </P>", "<UL>, <OL> lists", "pictures, links, tables"]
    for i, t in enumerate(items):
        ax.add_patch(Rectangle((0.6, 1.62 - i * 0.42), 3.8, 0.34, fc="white", ec=INK, lw=0.7))
        ax.text(2.5, 1.79 - i * 0.42, t, ha="center", va="center", fontsize=8.4, family=MONO)
    # right: the browser window
    bx, by, bw, bh = 6.2, 0.4, 4.2, 3.6
    ax.add_patch(Rectangle((bx, by), bw, bh, fc="white", ec=INK, lw=1.2))
    ax.add_patch(Rectangle((bx, by + bh - 0.45), bw, 0.45, fc=FILLS[0], ec=INK, lw=1.2))
    ax.text(bx + 0.15, by + bh - 0.225, "My first page", ha="left", va="center", fontsize=9.5, fontweight="bold")
    ax.text(bx + 0.25, by + bh - 0.85, "heading", ha="left", va="center", fontsize=15, fontweight="bold")
    ax.text(bx + 0.25, by + bh - 1.35, "paragraph text …", ha="left", va="center", fontsize=9.5)
    ax.text(bx + 0.25, by + bh - 1.8, "•  list item", ha="left", va="center", fontsize=9.5)
    ax.text(bx + 0.25, by + bh - 2.2, "•  list item", ha="left", va="center", fontsize=9.5)
    ax.text(bx + bw / 2, by - 0.25, "what the browser shows", ha="center", va="top", fontsize=9, style="italic")
    ax.annotate("", xy=(bx - 0.05, by + bh - 0.22), xytext=(4.75, 3.125),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1, connectionstyle="arc3,rad=-0.15"))
    ax.text(5.55, 3.95, "title bar", ha="center", va="bottom", fontsize=8.5, style="italic")
    ax.annotate("", xy=(bx - 0.05, by + 1.6), xytext=(4.75, 1.4),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1))
    ax.text(5.5, 1.15, "window", ha="center", va="top", fontsize=8.5, style="italic")
    ax.set_xlim(-0.1, 10.6)
    ax.set_ylim(-0.6, 4.6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("The structure of an HTML document", fontsize=11, fontweight="bold", color=INK)
    save(fig, "cs_ch06_fig01_structure.png")


def fig_formatting():
    rows = [
        ("<B>Bold</B>", dict(s="Bold", fontweight="bold")),
        ("<I>Italic</I>", dict(s="Italic", style="italic")),
        ("<U>Underline</U>", dict(s="Underline", line="under")),
        ("<S>Strike</S>  or  <STRIKE>", dict(s="Strike", line="through")),
        ("x<SUP>2</SUP>", dict(s=r"x$^{2}$")),
        ("H<SUB>2</SUB>O", dict(s=r"H$_{2}$O")),
        ("<BIG>Big</BIG>  <SMALL>small</SMALL>", dict(s="Big", size=15, extra=("small", 8.5))),
        ("<TT>Typewriter</TT>", dict(s="Typewriter", family=MONO)),
        ('<FONT SIZE="5" COLOR="red">Red</FONT>', dict(s="Red", size=16, color="#C0392B")),
    ]
    n = len(rows)
    fig, ax = plt.subplots(figsize=(9.6, 0.52 * n + 0.9))
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.2, n + 0.9)
    ax.axis("off")
    ax.add_patch(Rectangle((0, n), 10, 0.6, fc=FILLS[0], ec=INK, lw=0.8))
    ax.text(0.15, n + 0.3, "HTML code", ha="left", va="center", fontsize=10, fontweight="bold")
    ax.text(6.65, n + 0.3, "What the browser shows", ha="left", va="center", fontsize=10, fontweight="bold")
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    for i, (code, spec) in enumerate(rows):
        y = n - i - 0.5
        ax.add_patch(Rectangle((0, y - 0.5), 10, 1.0, fc="white" if i % 2 else "#F6F8FB", ec="#B8C2CC", lw=0.5))
        ax.text(0.15, y, code, ha="left", va="center", fontsize=9.3, family=MONO, color=INK)
        kw = dict(fontsize=spec.get("size", 12), color=spec.get("color", INK))
        for k in ("fontweight", "style", "family"):
            if k in spec:
                kw[k] = spec[k]
        t = ax.text(6.65, y, spec["s"], ha="left", va="center", **kw)
        if "line" in spec or "extra" in spec:
            bb = t.get_window_extent(renderer=rend).transformed(ax.transData.inverted())
            if spec.get("line") == "under":
                ax.plot([bb.x0, bb.x1], [bb.y0 + 0.02, bb.y0 + 0.02], color=INK, lw=1.0)
            elif spec.get("line") == "through":
                mid = (bb.y0 + bb.y1) / 2
                ax.plot([bb.x0, bb.x1], [mid, mid], color=INK, lw=1.0)
            if "extra" in spec:
                ax.text(bb.x1 + 0.25, y, spec["extra"][0], ha="left", va="center", fontsize=spec["extra"][1], color=INK)
    ax.plot([6.5, 6.5], [-0.0, n + 0.6], color="#B8C2CC", lw=0.6)
    ax.set_title("Text-formatting tags and their output", fontsize=11, fontweight="bold", color=INK)
    save(fig, "cs_ch06_fig02_formatting.png")


def fig_lists():
    table_fig(["List", "Code", "The browser shows"],
              [["Unordered (default)", '<UL TYPE="DISC">', "●  Apple    ●  Mango"],
               ["Unordered", '<UL TYPE="CIRCLE">', "○  Apple    ○  Mango"],
               ["Unordered", '<UL TYPE="SQUARE">', "■  Apple    ■  Mango"],
               ["Ordered (default)", '<OL TYPE="1">', "1.  2.  3."],
               ["Ordered", '<OL TYPE="A">', "A.  B.  C."],
               ["Ordered", '<OL TYPE="a">', "a.  b.  c."],
               ["Ordered", '<OL TYPE="I">', "I.  II.  III."],
               ["Ordered", '<OL TYPE="i">', "i.  ii.  iii."],
               ["Ordered, start at 3", '<OL START="3">', "3.  4.  5."],
               ["Definition", "<DL> <DT> <DD>", "term, then its definition indented"]],
              "cs_ch06_fig03_lists.png", col_w=[3.0, 3.6, 4.6], title="Types of lists and the TYPE and START attributes",
              size=9.0)


if __name__ == "__main__":
    fig_structure()
    fig_formatting()
    fig_lists()
