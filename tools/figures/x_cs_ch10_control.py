"""Figures for Class X Computer Science, Ch10: C++ Control Structures (flowcharts, loop anatomy, trace table)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import INK, FILLS, plt, save, table_fig  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle  # noqa: E402

MONO = "DejaVu Sans Mono"
NOTE = "#7A2E1B"


def _proc(ax, x, y, text, w=2.4, h=0.6, fc=FILLS[0]):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc=fc, ec=INK, lw=1.1))
    ax.text(x, y, text, ha="center", va="center", fontsize=9)


def _term(ax, x, y, text, w=1.6, h=0.5):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.25",
                                fc=FILLS[5], ec=INK, lw=1.1))
    ax.text(x, y, text, ha="center", va="center", fontsize=9, fontweight="bold")


def _dec(ax, x, y, text, w=2.4, h=1.0):
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)], closed=True,
                         fc=FILLS[1], ec=INK, lw=1.1))
    ax.text(x, y, text, ha="center", va="center", fontsize=8.8)


def _arr(ax, p0, p1, label=None, lpos=None):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0))
    if label:
        ax.text(lpos[0], lpos[1], label, fontsize=8.6, color=NOTE, fontweight="bold", ha="center", va="center")


def _line(ax, pts):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=INK, lw=1.0)


def fig_ifelse():
    fig, ax = plt.subplots(figsize=(10.5, 4.6))
    # left: if-else
    x = 3.0
    _term(ax, x, 5.2, "Start")
    _arr(ax, (x, 4.95), (x, 4.45))
    _dec(ax, x, 3.95, "condition\ntrue?")
    _proc(ax, x - 1.9, 2.6, "statements of if", w=2.0)
    _proc(ax, x + 1.9, 2.6, "statements of else", w=2.0)
    _line(ax, [(x - 1.2, 3.95), (x - 1.9, 3.95)])
    _arr(ax, (x - 1.9, 3.95), (x - 1.9, 2.9), "true", (x - 1.55, 3.6))
    _line(ax, [(x + 1.2, 3.95), (x + 1.9, 3.95)])
    _arr(ax, (x + 1.9, 3.95), (x + 1.9, 2.9), "false", (x + 1.55, 3.6))
    _line(ax, [(x - 1.9, 2.3), (x - 1.9, 1.6), (x + 1.9, 1.6), (x + 1.9, 2.3)])
    _arr(ax, (x, 1.6), (x, 1.05))
    _term(ax, x, 0.8, "Stop")
    ax.text(x, 5.85, "if … else", ha="center", fontsize=10.5, fontweight="bold")
    # right: else-if ladder
    x2 = 8.0
    _term(ax, x2, 5.2, "Start")
    _arr(ax, (x2, 4.95), (x2, 4.6))
    _dec(ax, x2, 4.2, "marks >= 75 ?", w=2.4, h=0.8)
    _dec(ax, x2, 3.0, "marks >= 33 ?", w=2.4, h=0.8)
    _arr(ax, (x2, 3.8), (x2, 3.4), "false", (x2 + 0.35, 3.6))
    _proc(ax, x2 + 2.65, 4.2, 'print "Distinction"', w=2.0, h=0.5)
    _proc(ax, x2 + 2.65, 3.0, 'print "Pass"', w=2.0, h=0.5)
    _proc(ax, x2, 1.85, 'print "Fail"', w=1.9, h=0.5)
    _arr(ax, (x2 + 1.2, 4.2), (x2 + 1.65, 4.2), "true", (x2 + 1.42, 4.45))
    _arr(ax, (x2 + 1.2, 3.0), (x2 + 1.65, 3.0), "true", (x2 + 1.42, 3.25))
    _arr(ax, (x2, 2.6), (x2, 2.1), "false", (x2 + 0.35, 2.35))
    _line(ax, [(x2 + 2.65, 3.95), (x2 + 2.65, 3.25)])
    _line(ax, [(x2 + 2.65, 2.75), (x2 + 2.65, 1.3), (x2, 1.3)])
    _line(ax, [(x2, 1.6), (x2, 1.3)])
    _arr(ax, (x2, 1.3), (x2, 1.05))
    _term(ax, x2, 0.8, "Stop")
    ax.text(x2 + 0.6, 5.85, "else-if ladder", ha="center", fontsize=10.5, fontweight="bold")
    ax.set_xlim(0.0, 11.9)
    ax.set_ylim(0.4, 6.1)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "cs_ch10_fig01_ifelse.png")


def fig_loops():
    fig, ax = plt.subplots(figsize=(10.5, 5.0))
    # while
    x = 2.4
    _proc(ax, x, 5.0, "initialise: i = 1", w=2.4, h=0.5, fc=FILLS[2])
    _arr(ax, (x, 4.75), (x, 4.35))
    _dec(ax, x, 3.85, "i <= n ?")
    _proc(ax, x, 2.55, "body of the loop", w=2.4, h=0.5)
    _proc(ax, x, 1.75, "update: i++", w=2.4, h=0.5, fc=FILLS[2])
    _arr(ax, (x, 3.35), (x, 2.8), "true", (x + 0.35, 3.1))
    _arr(ax, (x, 2.3), (x, 2.0))
    _line(ax, [(x - 1.2, 1.75), (x - 1.75, 1.75), (x - 1.75, 4.55)])
    _arr(ax, (x - 1.75, 4.55), (x - 0.03, 4.55))
    _line(ax, [(x + 1.2, 3.85), (x + 1.75, 3.85), (x + 1.75, 1.05)])
    _arr(ax, (x + 1.75, 1.05), (x + 0.82, 1.05), "false", (x + 2.05, 2.5))
    _term(ax, x, 1.05, "exit loop")
    ax.text(x, 5.75, "while loop: entry-controlled", ha="center", fontsize=10.5, fontweight="bold")
    ax.text(x, 0.3, "the condition is tested first;\nthe body may run zero times", ha="center", fontsize=8.6,
            style="italic")
    # do-while
    x2 = 8.0
    _proc(ax, x2, 5.0, "initialise: i = 1", w=2.4, h=0.5, fc=FILLS[2])
    _arr(ax, (x2, 4.75), (x2, 4.35))
    _proc(ax, x2, 4.1, "body of the loop", w=2.4, h=0.5)
    _proc(ax, x2, 3.3, "update: i++", w=2.4, h=0.5, fc=FILLS[2])
    _arr(ax, (x2, 3.85), (x2, 3.55))
    _arr(ax, (x2, 3.05), (x2, 2.65))
    _dec(ax, x2, 2.15, "i <= n ?")
    _line(ax, [(x2 - 1.2, 2.15), (x2 - 1.75, 2.15), (x2 - 1.75, 4.45)])
    _arr(ax, (x2 - 1.75, 4.45), (x2 - 0.2, 4.45), "true", (x2 - 2.05, 3.3))
    _arr(ax, (x2, 1.65), (x2, 1.3), "false", (x2 + 0.4, 1.47))
    _term(ax, x2, 1.05, "exit loop")
    ax.text(x2, 5.75, "do … while loop: exit-controlled", ha="center", fontsize=10.5, fontweight="bold")
    ax.text(x2, 0.3, "the condition is tested last;\nthe body runs at least once", ha="center", fontsize=8.6,
            style="italic")
    ax.set_xlim(-0.2, 10.6)
    ax.set_ylim(-0.4, 6.0)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "cs_ch10_fig02_loops.png")


def fig_for():
    fig, ax = plt.subplots(figsize=(10, 2.4))
    ax.set_xlim(0, 10.5)
    ax.set_ylim(-0.6, 1.5)
    ax.axis("off")
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    inv = ax.transData.inverted()
    segs = [("for ( ", None), ("i = 1", ("initialisation\n(done once)", FILLS[2])), (" ;  ", None),
            ("i <= 10", ("condition\n(tested each time)", FILLS[1])), (" ;  ", None),
            ("i++", ("update\n(after each pass)", FILLS[0])), (" )", None)]
    x = 0.8
    for text, mark in segs:
        t = ax.text(x, 1.0, text, ha="left", va="center", fontsize=17, family=MONO, color=INK, zorder=2)
        bb = t.get_window_extent(renderer=rend).transformed(inv)
        if mark:
            lab, fc = mark
            ax.add_patch(Rectangle((bb.x0 - 0.04, 0.72), bb.x1 - bb.x0 + 0.08, 0.56, fc=fc, ec="none", zorder=0))
            mid = (bb.x0 + bb.x1) / 2
            ax.plot([mid, mid], [0.7, 0.35], color=NOTE, lw=1.0)
            ax.text(mid, 0.2, lab, ha="center", va="top", fontsize=9.5, color=NOTE)
        x = bb.x1
    ax.set_title("The three parts of a for loop", fontsize=11, fontweight="bold", color=INK)
    save(fig, "cs_ch10_fig03_for.png")


def fig_trace():
    table_fig(["Pass", "n (start of pass)", "r = n % 10", "sum = sum + r", "n = n / 10"],
              [["1", "3524", "4", "0 + 4 = 4", "352"],
               ["2", "352", "2", "4 + 2 = 6", "35"],
               ["3", "35", "5", "6 + 5 = 11", "3"],
               ["4", "3", "3", "11 + 3 = 14", "0  (loop stops)"]],
              "cs_ch10_fig04_trace.png", col_w=[1.2, 2.8, 2.2, 3.0, 3.0],
              title="Dry run: sum of the digits of 3524 (while n != 0)", size=9.2)


if __name__ == "__main__":
    fig_ifelse()
    fig_loops()
    fig_for()
    fig_trace()
