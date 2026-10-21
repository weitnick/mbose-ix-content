"""Figures for Class X Mathematics, Chapter 3: Pair of Linear Equations in Two Variables.
Run: python x_ch03_linear_equations.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, ACC2 = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#2E7D5B"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})
M = "−"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def grid(ax, xr, yr, step=1, labels=True):
    """Squared graph paper with labelled axes through the origin."""
    for v in np.arange(np.ceil(xr[0]), xr[1] + 1e-9, step):
        ax.axvline(v, color="#DCE3EA", lw=0.5, zorder=0)
    for v in np.arange(np.ceil(yr[0]), yr[1] + 1e-9, step):
        ax.axhline(v, color="#DCE3EA", lw=0.5, zorder=0)
    ax.axhline(0, color=INK, lw=0.9, zorder=1)
    ax.axvline(0, color=INK, lw=0.9, zorder=1)
    ax.set_xlim(*xr); ax.set_ylim(*yr)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_aspect("equal")
    if labels:
        for t in range(int(np.ceil(xr[0])), int(np.floor(xr[1])) + 1):
            if t:
                ax.text(t, -0.3, str(t).replace("-", M), ha="center", va="top", fontsize=7, color=INK)
        for t in range(int(np.ceil(yr[0])), int(np.floor(yr[1])) + 1):
            if t and not (t == -1 and xr[0] > -1.5):
                ax.text(-0.25, t, str(t).replace("-", M), ha="right", va="center", fontsize=7, color=INK)
        ax.text(-0.25, -0.3, "O", ha="right", va="top", fontsize=7, color=INK)
    ax.text(xr[1], 0.15, "X", fontsize=9, color=INK, ha="right", va="bottom")
    ax.text(0.15, yr[1], "Y", fontsize=9, color=INK, va="top")


def line(ax, a, b, c, xr, color, label, pos):
    """Draw a x + b y = c."""
    if b == 0:
        ax.axvline(c / a, color=color, lw=1.6)
    else:
        xs = np.linspace(*xr, 2)
        ax.plot(xs, (c - a * xs) / b, color=color, lw=1.6)
    ax.text(*pos, label, color=color, fontsize=10)


def dot(ax, x, y, text, off=(6, 6), color=HI):
    ax.plot([x], [y], "o", ms=5, color=color, zorder=5)
    ax.annotate(text.replace("-", M), (x, y), textcoords="offset points", xytext=off, fontsize=8.5, color=color)


# Fig 3.1: Example 1, x + 3y = 6 and 2x - 3y = 12 meet at (6, 0)
def fig_example1():
    fig, ax = plt.subplots(figsize=(5.4, 4.0))
    xr, yr = (-2, 8), (-5, 4)
    grid(ax, xr, yr)
    line(ax, 1, 3, 6, xr, ACC, "$x + 3y = 6$", (1.0, 2.5))
    line(ax, 2, -3, 12, xr, ACC2, "$2x - 3y = 12$", (3.6, -4.6))
    dot(ax, 0, 2, "A(0, 2)", (6, 4), ACC)
    dot(ax, 0, -4, "P(0, -4)", (6, -10), ACC2)
    dot(ax, 3, -2, "Q(3, -2)", (6, -10), ACC2)
    dot(ax, 6, 0, "B(6, 0)", (4, 6))
    save(fig, "ch03_fig01_example1.png")


# Fig 3.2: Champa's pants and skirts, y = 2x - 2 and y = 4x - 4 meet at (1, 0)
def fig_champa():
    fig, ax = plt.subplots(figsize=(4.4, 4.0))
    xr, yr = (-2, 4), (-5, 5)
    grid(ax, xr, yr)
    line(ax, -2, 1, -2, xr, ACC, "$y = 2x - 2$", (2.3, 1.2))
    line(ax, -4, 1, -4, (-0.2, 2.2), ACC2, "$y = 4x - 4$", (2.45, -1.3))
    dot(ax, 1, 0, "(1, 0)", (-40, 6))
    save(fig, "ch03_fig02_champa.png")


# Fig 3.3: the three possible cases
def fig_cases():
    fig, axs = plt.subplots(1, 3, figsize=(7.4, 2.8))
    xr, yr = (-1, 5), (-1, 5)
    titles = ["Intersecting:\nunique solution", "Coincident:\ninfinitely many solutions", "Parallel:\nno solution"]
    for ax, t in zip(axs, titles):
        grid(ax, xr, yr, labels=False)
        ax.set_title(t, fontsize=9, color=INK)
    line(axs[0], 1, -2, 0, xr, ACC, "", (0, 0))
    line(axs[0], 3, 4, 20, (1.0, 5), ACC2, "", (0, 0))
    dot(axs[0], 4, 2, "(4, 2)", (4, 6))
    line(axs[1], 2, 3, 9, xr, ACC, "", (0, 0))
    xs = np.linspace(*xr, 2)
    axs[1].plot(xs, (9 - 2 * xs) / 3, color=ACC2, lw=1.6, ls=(0, (4, 3)))
    line(axs[2], 1, 2, 4, xr, ACC, "", (0, 0))
    line(axs[2], 2, 4, 12, xr, ACC2, "", (0, 0))
    axs[0].text(2.0, 4.3, "$x - 2y = 0$\n$3x + 4y = 20$", fontsize=8, color=INK)
    axs[1].text(1.6, 4.0, "$2x + 3y = 9$\n$4x + 6y = 18$", fontsize=8, color=INK)
    axs[2].text(1.4, 4.0, "$x + 2y = 4$\n$2x + 4y = 12$", fontsize=8, color=INK)
    fig.subplots_adjust(wspace=0.15)
    save(fig, "ch03_fig03_three_cases.png")


# Fig 3.4: Exercise 3.1 Q1 (i) x + y = 10, y - x = 4 ; (ii) 5x + 7y = 50, 7x + 5y = 46
def fig_ex31_q1():
    fig, axs = plt.subplots(1, 2, figsize=(7.4, 3.8))
    xr, yr = (-1, 11), (-1, 11)
    grid(axs[0], xr, yr)
    line(axs[0], 1, 1, 10, xr, ACC, "$x + y = 10$", (6.2, 4.6))
    line(axs[0], -1, 1, 4, (-1, 6.8), ACC2, "$y - x = 4$", (4.6, 9.4))
    dot(axs[0], 3, 7, "(3, 7)", (6, 2))
    axs[0].set_title("(i) boys $x$, girls $y$", fontsize=9)
    grid(axs[1], xr, yr)
    line(axs[1], 5, 7, 50, xr, ACC, "$5x + 7y = 50$", (6.0, 3.5))
    line(axs[1], 7, 5, 46, (-1, 7.5), ACC2, "$7x + 5y = 46$", (0.2, 10.0))
    dot(axs[1], 3, 5, "(3, 5)", (6, 2))
    axs[1].set_title("(ii) pencil ₹$x$, pen ₹$y$", fontsize=9)
    save(fig, "ch03_fig04_ex31_q1.png")


# Fig 3.5: Exercise 3.1 Q4 (iii) 2x + y = 6, 4x - 2y = 4 meet at (2, 2)
def fig_ex31_q4():
    fig, ax = plt.subplots(figsize=(4.2, 4.0))
    xr, yr = (-1, 5), (-3, 7)
    grid(ax, xr, yr)
    line(ax, 2, 1, 6, (-0.5, 4.5), ACC, "$2x + y = 6$", (2.9, 0.9))
    line(ax, 4, -2, 4, (-0.5, 4.2), ACC2, "$4x - 2y = 4$", (2.8, 5.6))
    dot(ax, 2, 2, "(2, 2)", (-40, 4))
    save(fig, "ch03_fig05_ex31_q4iii.png")


# Fig 3.6: Exercise 3.1 Q7, triangle with vertices (-1, 0), (4, 0), (2, 3)
def fig_ex31_q7():
    fig, ax = plt.subplots(figsize=(5.0, 3.6))
    xr, yr = (-3, 6), (-1, 6)
    grid(ax, xr, yr)
    ax.add_patch(Polygon([(-1, 0), (4, 0), (2, 3)], closed=True, fc="#F6E7C8", ec="none", zorder=1))
    line(ax, 1, -1, -1, (-2.5, 5), ACC, "$x - y + 1 = 0$", (2.6, 5.2))
    line(ax, 3, 2, 12, (1.0, 5.5), ACC2, "$3x + 2y - 12 = 0$", (3.1, 2.2))
    dot(ax, -1, 0, "(-1, 0)", (-30, 6))
    dot(ax, 4, 0, "(4, 0)", (4, 6))
    dot(ax, 2, 3, "(2, 3)", (-38, 4))
    save(fig, "ch03_fig06_ex31_q7.png")


if __name__ == "__main__":
    fig_example1()
    fig_champa()
    fig_cases()
    fig_ex31_q1()
    fig_ex31_q4()
    fig_ex31_q7()
