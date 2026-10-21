"""Figures for Class X Computer Science, Ch12: Java Programming."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import INK, FILLS, plt, save, tree, table_fig  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle  # noqa: E402

NOTE = "#7A2E1B"


def fig_types():
    tree("Data types in Java", ["Primitive (8 built-in types)", "Non-primitive (reference types)"],
         "cs_ch12_fig01_types.png",
         grand={0: ["whole numbers: byte, short, int, long", "decimals: float, double", "character: char",
                    "true / false: boolean"],
                1: ["classes and objects", "arrays", "String", "interfaces"]},
         width=9.5, child_w=4.0, size=9.0,
         title="Primitive types hold values; reference types hold a reference or null")


def fig_sizes():
    table_fig(["Type", "Size", "Range or values", "Example"],
              [["byte", "1 byte", "-128 to 127", "byte b = 100;"],
               ["short", "2 bytes", "-32,768 to 32,767", "short s = 2000;"],
               ["int", "4 bytes", "about -2.1 billion to 2.1 billion", "int marks = 85;"],
               ["long", "8 bytes", "very large whole numbers", "long pop = 3700000L;"],
               ["float", "4 bytes", "decimals, about 7 digits", "float rate = 7.5f;"],
               ["double", "8 bytes", "decimals, about 15 digits", "double pi = 3.14159;"],
               ["char", "2 bytes", "0 to 65,535 (Unicode characters)", "char g = 'A';"],
               ["boolean", "1 bit", "true or false", "boolean pass = true;"]],
              "cs_ch12_fig02_sizes.png", col_w=[1.8, 1.6, 5.0, 4.0], title="The eight primitive data types of Java",
              size=9.0)


def _proc(ax, x, y, text, w=2.2, h=0.5, fc=FILLS[0]):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc=fc, ec=INK, lw=1.1))
    ax.text(x, y, text, ha="center", va="center", fontsize=8.8)


def _dec(ax, x, y, text, w=2.0, h=0.8):
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)], closed=True,
                         fc=FILLS[1], ec=INK, lw=1.1))
    ax.text(x, y, text, ha="center", va="center", fontsize=8.6)


def _arr(ax, p0, p1, label=None, lpos=None):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0))
    if label:
        ax.text(lpos[0], lpos[1], label, fontsize=8.4, color=NOTE, fontweight="bold", ha="center", va="center")


def fig_constructs():
    fig, ax = plt.subplots(figsize=(11, 4.4))
    # sequence
    x = 1.6
    for i, t in enumerate(["statement 1", "statement 2", "statement 3"]):
        _proc(ax, x, 3.4 - i * 1.0, t)
        if i:
            _arr(ax, (x, 3.4 - (i - 1) * 1.0 - 0.25), (x, 3.4 - i * 1.0 + 0.25))
    ax.text(x, 4.25, "1. Sequence", ha="center", fontsize=10.5, fontweight="bold")
    # selection
    x = 5.4
    _dec(ax, x, 3.3, "condition?")
    _proc(ax, x - 1.3, 1.9, "do this", w=1.6)
    _proc(ax, x + 1.3, 1.9, "do that", w=1.6)
    ax.plot([x - 1.0, x - 1.3], [3.3, 3.3], color=INK, lw=1.0)
    _arr(ax, (x - 1.3, 3.3), (x - 1.3, 2.15), "true", (x - 1.62, 2.75))
    ax.plot([x + 1.0, x + 1.3], [3.3, 3.3], color=INK, lw=1.0)
    _arr(ax, (x + 1.3, 3.3), (x + 1.3, 2.15), "false", (x + 1.68, 2.75))
    ax.text(x, 4.25, "2. Selection (if, switch)", ha="center", fontsize=10.5, fontweight="bold")
    # repetition
    x = 9.3
    _dec(ax, x, 3.3, "condition?")
    _proc(ax, x, 1.9, "repeat body", w=1.8)
    _arr(ax, (x, 2.9), (x, 2.15), "true", (x + 0.35, 2.55))
    ax.plot([x - 0.9, x - 1.35, x - 1.35], [1.9, 1.9, 3.3], color=INK, lw=1.0)
    _arr(ax, (x - 1.35, 3.3), (x - 1.0, 3.3))
    ax.plot([x + 1.0, x + 1.35, x + 1.35], [3.3, 3.3, 1.2], color=INK, lw=1.0)
    _arr(ax, (x + 1.35, 1.2), (x + 0.6, 1.2), "false", (x + 1.65, 2.3))
    ax.text(x + 0.1, 1.2, "exit", ha="right", va="center", fontsize=8.8, style="italic")
    ax.text(x, 4.25, "3. Repetition (for, while, do-while)", ha="center", fontsize=10.5, fontweight="bold")
    ax.set_xlim(0.2, 11.0)
    ax.set_ylim(0.8, 4.6)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "cs_ch12_fig03_constructs.png")


def fig_trace():
    table_fig(["i", "t (start of pass)", "sum += t", "printed", "t += 3", "i++"],
              [["1", "1", "1", "Term=1", "4", "2"],
               ["2", "4", "5", "Term=4", "7", "3"],
               ["3", "7", "12", "Term=7", "10", "4"],
               ["4", "10", "22", "Term=10", "13", "5 (loop ends)"],
               ["after the loop", "", "", "Sum of series=22", "", ""]],
              "cs_ch12_fig04_trace.png", col_w=[2.2, 2.4, 1.8, 3.0, 1.4, 2.2],
              title="Dry run of the 2024 series program (while i <= 4)", size=9.0)


if __name__ == "__main__":
    fig_types()
    fig_sizes()
    fig_constructs()
    fig_trace()
