"""Figures for Class X Mathematics, Chapter 2: Polynomials.
Run: python x_ch02_polynomials.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def axes(ax, xr, yr, ticks=True, labels=True):
    ax.axhline(0, color=INK, lw=0.9)
    ax.axvline(0, color=INK, lw=0.9)
    ax.set_xlim(*xr); ax.set_ylim(*yr)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    if ticks:
        span = yr[1] - yr[0]
        for t in range(int(np.ceil(xr[0])), int(np.floor(xr[1])) + 1):
            if t == 0:
                continue
            ax.plot([t, t], [-0.012 * span, 0.012 * span], color=INK, lw=0.8)
            ax.text(t, -0.05 * span, str(t).replace("-", "−"), ha="center", va="top", fontsize=8, color=INK)
    ax.grid(False)
    if labels:
        ax.text(xr[1], 0, " X", va="center", fontsize=9, color=INK)
        ax.text(0, yr[1], "Y", ha="center", va="bottom", fontsize=9, color=INK)


def mark_zeros(ax, xs):
    for x in xs:
        ax.plot([x], [0], "o", ms=5, color=HI, zorder=5)


# Fig 2.1: the line y = 2x + 3
def fig_linear():
    fig, ax = plt.subplots(figsize=(4.2, 3.6))
    x = np.linspace(-3.2, 2.6, 50)
    axes(ax, (-3.6, 3), (-4, 8.5))
    ax.plot(x, 2 * x + 3, color=ACC, lw=1.8)
    for px, py in [(-2, -1), (2, 7)]:
        ax.plot(px, py, "o", ms=4, color=ACC)
        ax.annotate(f"({px}, {py})".replace("-", "2212"), (px, py), textcoords="offset points", xytext=(6, -10), fontsize=9)
    mark_zeros(ax, [-1.5])
    ax.annotate(r"$\left(-\frac{3}{2}, 0\right)$", (-1.5, 0), textcoords="offset points", xytext=(-48, 10), fontsize=10, color=HI)
    ax.text(1.1, 3.6, "$y = 2x + 3$", color=ACC, fontsize=11)
    save(fig, "ch02_fig01_linear_graph.png")


# Fig 2.2: the parabola y = x^2 - 3x - 4
def fig_parabola():
    fig, ax = plt.subplots(figsize=(4.6, 4.0))
    x = np.linspace(-2.4, 5.4, 200)
    axes(ax, (-3, 6), (-7.5, 8.5))
    ax.plot(x, x ** 2 - 3 * x - 4, color=ACC, lw=1.8)
    pts = [(-2, 6), (-1, 0), (0, -4), (1, -6), (2, -6), (3, -4), (4, 0), (5, 6)]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], "o", ms=3.5, color=ACC)
    mark_zeros(ax, [-1, 4])
    ax.annotate("(−1, 0)", (-1, 0), textcoords="offset points", xytext=(-40, 6), fontsize=9, color=HI)
    ax.annotate("(4, 0)", (4, 0), textcoords="offset points", xytext=(6, 6), fontsize=9, color=HI)
    ax.text(2.4, 6.6, "$y = x^2 - 3x - 4$", color=ACC, fontsize=11)
    save(fig, "ch02_fig02_parabola.png")


# Fig 2.3 to 2.5: the three cases for a quadratic (a > 0 above, a < 0 below)
def fig_three_cases():
    fig, axs = plt.subplots(2, 3, figsize=(7.2, 4.4))
    x = np.linspace(-2.6, 2.6, 200)
    rows = [(1, "a > 0"), (-1, "a < 0")]
    titles = ["Two distinct zeroes", "One zero (two equal zeroes)", "No zero"]
    shifts = [-1.6, 0.0, 1.2]
    for r, (sgn, lab) in enumerate(rows):
        for c, k in enumerate(shifts):
            ax = axs[r][c]
            axes(ax, (-3, 3), (-3, 4) if sgn > 0 else (-4, 3), ticks=False)
            y = sgn * (x ** 2 + k)
            ax.plot(x, y, color=ACC, lw=1.6)
            if k < 0:
                mark_zeros(ax, [-np.sqrt(-k), np.sqrt(-k)])
                ax.text(-np.sqrt(-k) - 0.2, 0.35 * sgn, "A", fontsize=9, ha="right", color=HI)
                ax.text(np.sqrt(-k) + 0.2, 0.35 * sgn, "A′", fontsize=9, color=HI)
            elif k == 0:
                mark_zeros(ax, [0])
                ax.text(0.25, 0.35 * sgn, "A", fontsize=9, color=HI)
            if r == 0:
                ax.set_title(titles[c], fontsize=9, color=INK, pad=14)
            if c == 0:
                ax.text(-3.3, 0.5, lab, fontsize=9, color=ACC, ha="right")
    fig.subplots_adjust(wspace=0.25, hspace=0.25)
    save(fig, "ch02_fig03_quadratic_cases.png")


# Fig 2.6 to 2.8: cubic graphs
def fig_cubics():
    fig, axs = plt.subplots(1, 3, figsize=(7.4, 3.0))
    x = np.linspace(-2.5, 2.5, 300)
    data = [(x ** 3 - 4 * x, "$y = x^3 - 4x$", [-2, 0, 2], (-6.5, 6.5)),
            (x ** 3, "$y = x^3$", [0], (-6.5, 6.5)),
            (x ** 3 - x ** 2, "$y = x^3 - x^2$", [0, 1], (-6.5, 6.5))]
    for ax, (y, t, z, yr) in zip(axs, data):
        axes(ax, (-3, 3), yr)
        ax.plot(x, y, color=ACC, lw=1.6)
        mark_zeros(ax, z)
        ax.set_title(t, fontsize=10.5, color=ACC, pad=14)
    save(fig, "ch02_fig04_cubic_graphs.png")


def sketch_grid(name, curves, labels):
    fig, axs = plt.subplots(2, 3, figsize=(7.4, 4.6))
    for ax, (fn, xr, yr), lab in zip(axs.flat, curves, labels):
        x = np.linspace(xr[0] + 0.25, xr[1] - 0.25, 400)
        axes(ax, xr, yr, ticks=False)
        y = fn(x)
        y = np.where((y > yr[1] * 1.05) | (y < yr[0] * 1.05), np.nan, y)
        ax.plot(x, y, color=ACC, lw=1.6)
        ax.set_xlabel(lab, fontsize=10, color=INK, labelpad=4)
    fig.subplots_adjust(wspace=0.2, hspace=0.3)
    save(fig, name)


# Fig 2.9: Example 1 (zeroes 1, 2, 3, 1, 1, 4)
def fig_example1():
    curves = [
        (lambda x: 0.9 * x + 0.6, (-3, 3), (-3, 3)),
        (lambda x: 0.8 * x ** 2 - 1.6, (-3, 3), (-3, 4)),
        (lambda x: 0.35 * (x ** 3 - 4 * x), (-3, 3), (-3, 3)),
        (lambda x: 0.4 * (x - 0.6) ** 3 + 0.2 * x, (-3, 3), (-3, 3)),
        (lambda x: 0.35 * x ** 3 + 0.4 * x + 0.8, (-3, 3), (-3, 3)),
        (lambda x: 0.12 * (x ** 2 - 1) * (x ** 2 - 5), (-3, 3), (-2.5, 3)),
    ]
    sketch_grid("ch02_fig05_example1_graphs.png", curves, ["(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)"])


# Fig 2.10: Exercise 2.1 Q1 (zeroes 0, 1, 3, 2, 4, 3)
def fig_exercise21():
    curves = [
        (lambda x: 1.0 + 0.0 * x, (-3, 3), (-2, 3)),
        (lambda x: -0.9 * x + 0.5, (-3, 3), (-3, 3)),
        (lambda x: -0.35 * (x ** 3 - 4 * x), (-3, 3), (-3, 3)),
        (lambda x: -0.6 * x ** 2 + 1.8, (-3, 3), (-3, 3)),
        (lambda x: 0.12 * (x ** 2 - 1) * (x ** 2 - 5), (-3, 3), (-2.5, 3)),
        (lambda x: 0.3 * (x + 2) * (x - 0.3) * (x - 2), (-3, 3), (-3, 3)),
    ]
    sketch_grid("ch02_fig06_exercise_2_1.png", curves, ["(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)"])


if __name__ == "__main__":
    fig_linear()
    fig_parabola()
    fig_three_cases()
    fig_cubics()
    fig_example1()
    fig_exercise21()
