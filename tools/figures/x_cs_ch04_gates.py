"""Figures for Class X Computer Science, Ch04: Logic Gates (drawn gate symbols and a combined truth table)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import INK, FILLS, plt, save, table_fig  # noqa: E402
from matplotlib.patches import Circle, PathPatch  # noqa: E402
from matplotlib.path import Path  # noqa: E402

LW = 1.6


def _bubble(ax, x, y):
    ax.add_patch(Circle((x + 0.07, y), 0.07, fill=True, facecolor="white", edgecolor=INK, lw=LW, zorder=3))
    return x + 0.14


def _and_body(ax, x, y, fill):
    verts = [(x, y + 0.5), (x + 0.5, y + 0.5), (x + 1.0, y + 0.5), (x + 1.0, y), (x + 1.0, y - 0.5), (x + 0.5, y - 0.5),
             (x, y - 0.5), (x, y + 0.5)]
    codes = [Path.MOVETO, Path.LINETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=fill, edgecolor=INK, lw=LW, zorder=2))
    return x + 1.0, x  # tip x, input x


def _or_body(ax, x, y, fill, xor=False):
    verts = [(x, y + 0.5), (x + 0.55, y + 0.5), (x + 1.05, y), (x + 0.55, y - 0.5), (x, y - 0.5), (x + 0.28, y), (x, y + 0.5)]
    codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=fill, edgecolor=INK, lw=LW, zorder=2))
    if xor:
        ex = x - 0.14
        verts2 = [(ex, y + 0.5), (ex + 0.28, y), (ex, y - 0.5)]
        ax.add_patch(PathPatch(Path(verts2, [Path.MOVETO, Path.CURVE3, Path.CURVE3]), fill=False, edgecolor=INK, lw=LW, zorder=2))
    return x + 1.05, x + 0.2


def gate(ax, kind, x, y, title, expr, fill):
    if kind == "NOT":
        verts = [(x, y + 0.42), (x + 0.85, y), (x, y - 0.42), (x, y + 0.42)]
        ax.add_patch(PathPatch(Path(verts, [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]),
                               facecolor=fill, edgecolor=INK, lw=LW, zorder=2))
        tip = _bubble(ax, x + 0.85, y)
        ax.plot([x - 0.5, x], [y, y], color=INK, lw=LW)
        ax.text(x - 0.58, y, "A", ha="right", va="center", fontsize=11, fontweight="bold")
    else:
        if kind in ("AND", "NAND"):
            tip, inx = _and_body(ax, x, y, fill)
        else:
            tip, inx = _or_body(ax, x, y, fill, xor=kind in ("XOR", "XNOR"))
        if kind in ("NAND", "NOR", "XNOR"):
            tip = _bubble(ax, tip, y)
        for dy, lab in ((0.25, "A"), (-0.25, "B")):
            start = x - 0.6
            end = inx if kind in ("AND", "NAND") else x + 0.12
            if kind in ("XOR", "XNOR"):
                end = x - 0.06
            ax.plot([start, end], [y + dy, y + dy], color=INK, lw=LW, zorder=1)
            ax.text(start - 0.08, y + dy, lab, ha="right", va="center", fontsize=11, fontweight="bold")
    ax.plot([tip, tip + 0.5], [y, y], color=INK, lw=LW)
    ax.text(tip + 0.58, y, "Y", ha="left", va="center", fontsize=11, fontweight="bold")
    ax.text(x + 0.45, y + 0.8, title, ha="center", va="bottom", fontsize=11, fontweight="bold", color=INK)
    ax.text(x + 0.45, y - 0.8, expr, ha="center", va="top", fontsize=11, color=INK)


def fig_primary():
    fig, ax = plt.subplots(figsize=(10, 2.8))
    gate(ax, "AND", 0.8, 0, "AND gate", "Y = A · B", FILLS[1])
    gate(ax, "OR", 4.4, 0, "OR gate", "Y = A + B", FILLS[2])
    gate(ax, "NOT", 8.0, 0, "NOT gate", "Y = A′  (A bar)", FILLS[3])
    ax.set_xlim(-0.2, 10.2)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "cs_ch04_fig01_primary.png")


def fig_secondary():
    fig, ax = plt.subplots(figsize=(13, 2.8))
    gate(ax, "NAND", 0.8, 0, "NAND gate", "Y = (A · B)′", FILLS[0])
    gate(ax, "NOR", 4.3, 0, "NOR gate", "Y = (A + B)′", FILLS[4])
    gate(ax, "XOR", 7.8, 0, "EXOR (XOR) gate", "Y = A ⊕ B", FILLS[5])
    gate(ax, "XNOR", 11.3, 0, "EXNOR (XNOR) gate", "Y = (A ⊕ B)′", FILLS[6])
    ax.set_xlim(-0.2, 13.6)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "cs_ch04_fig02_secondary.png")


def fig_table():
    rows = []
    for a in (0, 1):
        for b in (0, 1):
            rows.append([str(a), str(b), str(a & b), str(a | b), str(1 - (a & b)), str(1 - (a | b)), str(a ^ b), str(1 - (a ^ b))])
    table_fig(["A", "B", "AND", "OR", "NAND", "NOR", "EXOR", "EXNOR"], rows, "cs_ch04_fig03_truth.png",
              col_w=[1.0, 1.0, 1.3, 1.3, 1.4, 1.3, 1.4, 1.5], title="Truth table of the two-input gates", size=9.5)


if __name__ == "__main__":
    fig_primary()
    fig_secondary()
    fig_table()
