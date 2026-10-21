"""Figures for Class XII Mathematics Chapter 8, Application of Integrals.
Run: python xii_math_ch08_areas.py
"""
from xii_math_common import *


def fig01_ellipse():
    fig, a = plt.subplots(figsize=(6.4, 4.2))
    axes(a, (-5, 5), (-3.8, 3.8), ticks=True)
    t = np.linspace(0, 2 * np.pi, 400)
    a.plot(4 * np.cos(t), 3 * np.sin(t), color=BLUE, lw=2.0)
    x = np.linspace(0, 4, 200)
    a.fill_between(x, 0, 3 * np.sqrt(1 - x**2 / 16), color=BLUE, alpha=0.25)
    a.text(0.9, 0.9, "quarter area\n= 3π", fontsize=9, color=INK)
    a.text(4.1, 0.15, "(4, 0)", fontsize=8.5)
    a.text(0.1, 3.1, "(0, 3)", fontsize=8.5)
    a.set_title("x²/16 + y²/9 = 1: whole area = 4 × 3π = 12π", fontsize=10, pad=10)
    fig.tight_layout()
    save(fig, "math_ch08_fig01_ellipse.png")


def fig02_circle_line():
    fig, a = plt.subplots(figsize=(5.6, 5.0))
    R = np.sqrt(32)
    axes(a, (-0.8, 6.6), (-0.8, 6.6), ticks=True)
    t = np.linspace(0, np.pi / 2, 200)
    a.plot(R * np.cos(t), R * np.sin(t), color=BLUE, lw=2.0)
    a.plot([0, 5.2], [0, 5.2], color=INK, lw=1.4)
    x1 = np.linspace(0, 4, 100)
    a.fill_between(x1, 0, x1, color=BLUE, alpha=0.25)
    x2 = np.linspace(4, R, 100)
    a.fill_between(x2, 0, np.sqrt(np.clip(32 - x2**2, 0, None)), color=BLUE, alpha=0.25)
    a.plot([4, 4], [0, 4], color=GREY, lw=0.8, ls=":")
    a.plot([4], [4], "o", color=INK, ms=4)
    a.text(4.15, 4.15, "(4, 4)", fontsize=9)
    a.text(R + 0.05, 0.15, "(4√2, 0)", fontsize=9)
    a.text(5.25, 4.75, "y = x", fontsize=9)
    a.text(0.4, 5.9, "x² + y² = 32", fontsize=9, color=BLUE)
    a.set_title("Region between the x-axis, y = x and x² + y² = 32", fontsize=10, pad=10)
    fig.tight_layout()
    save(fig, "math_ch08_fig02_circle_line.png")


if __name__ == "__main__":
    fig01_ellipse()
    fig02_circle_line()
