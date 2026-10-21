"""Figures for Class XII Mathematics Chapter 1, Relations and Functions.
Run: python xii_math_ch01_relations.py
"""
from xii_math_common import *


def mapping(ax, x0, title, left, right, pairs, note):
    """Arrow diagram: left set elements -> right set elements."""
    ax.add_patch(Ellipse((x0, 3.0), 1.6, 4.0, fill=False, ec=BLUE, lw=1.4))
    ax.add_patch(Ellipse((x0 + 2.8, 3.0), 1.6, 4.0, fill=False, ec=GREEN, lw=1.4))
    ly = np.linspace(4.3, 1.7, len(left))
    ry = np.linspace(4.3, 1.7, len(right))
    for y, s in zip(ly, left):
        ax.text(x0, y, s, ha="center", va="center", fontsize=10)
    for y, s in zip(ry, right):
        ax.text(x0 + 2.8, y, s, ha="center", va="center", fontsize=10)
    for i, j in pairs:
        arrow(ax, (x0 + 0.25, ly[i]), (x0 + 2.55, ry[j]), color=RED, lw=1.1, ms=9)
    ax.text(x0 + 1.4, 5.6, title, ha="center", fontsize=9.5, weight="bold")
    ax.text(x0 + 1.4, 0.45, note, ha="center", fontsize=8.2, color=GREY)


def fig01_types():
    fig, ax = canvas(12.0, 3.4, (0, 24), (0, 6.4))
    mapping(ax, 1.0, "One-one, not onto", ["1", "2", "3"], ["a", "b", "c", "d"], [(0, 0), (1, 1), (2, 2)],
            "d has no pre-image")
    mapping(ax, 7.0, "Onto, not one-one", ["1", "2", "3", "4"], ["a", "b", "c"], [(0, 0), (1, 0), (2, 1), (3, 2)],
            "1 and 2 share image a")
    mapping(ax, 13.0, "One-one and onto (bijective)", ["1", "2", "3"], ["a", "b", "c"], [(0, 1), (1, 2), (2, 0)],
            "each image has exactly one pre-image")
    mapping(ax, 19.0, "Neither", ["1", "2", "3"], ["a", "b", "c"], [(0, 0), (1, 0), (2, 1)], "c has no pre-image; 1, 2 share a")
    ax.set_title("Types of functions shown by arrow diagrams", fontsize=11)
    save(fig, "math_ch01_fig01_function_types.png")


def fig02_graphs():
    fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.2))
    x = np.linspace(-2.2, 2.2, 400)
    data = [(x ** 3, "f(x) = x³: one-one and onto", "every horizontal line cuts once"),
            (x ** 2, "f(x) = x²: neither (on R → R)", "y = 1 cuts twice; y = −1 never"),
            (np.abs(x), "f(x) = |x|: neither (on R → R)", "negative values are never taken")]
    for a, (y, t, n) in zip(axs, data):
        axes(a, (-2.4, 2.4), (-3.2, 4.0), ticks=False)
        a.plot(x, y, color=BLUE, lw=2, clip_on=True)
        a.axhline(1, color=RED, lw=1, ls="--")
        a.set_title(t, fontsize=9.5, pad=14)
        a.text(0.5, -0.08, n, ha="center", va="top", fontsize=8, color=GREY, transform=a.transAxes)
    fig.suptitle("Horizontal-line test for one-one functions", fontsize=11, weight="bold")
    fig.tight_layout()
    save(fig, "math_ch01_fig02_horizontal_line.png")


if __name__ == "__main__":
    fig01_types()
    fig02_graphs()
