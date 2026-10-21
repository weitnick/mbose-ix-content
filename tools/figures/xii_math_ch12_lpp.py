"""Figures for Class XII Mathematics Chapter 12, Linear Programming.
Run: python xii_math_ch12_lpp.py
"""
from xii_math_common import *


def corner(a, p, label, dx=0.15, dy=0.15, fs=8.5):
    a.plot([p[0]], [p[1]], "o", color=INK, ms=4)
    a.text(p[0] + dx, p[1] + dy, label, fontsize=fs)


def fig01_dealer():
    """Fig 12.1: 5x + y <= 100, x + y <= 60, x, y >= 0."""
    fig, a = plt.subplots(figsize=(5.8, 4.8))
    axes(a, (-4, 80), (-6, 110), ticks=True)
    x = np.linspace(0, 70, 200)
    a.plot(x, 100 - 5 * x, color=BLUE, lw=1.6)
    a.plot(x, 60 - x, color=INK, lw=1.6)
    a.add_patch(Polygon([(0, 0), (20, 0), (10, 50), (0, 60)], closed=True, color=BLUE, alpha=0.25))
    corner(a, (0, 0), "O(0, 0)", dx=1, dy=-7)
    corner(a, (20, 0), "A(20, 0)", dx=1, dy=2)
    corner(a, (10, 50), "B(10, 50)", dx=2, dy=1)
    corner(a, (0, 60), "C(0, 60)", dx=2, dy=2)
    a.text(15, 92, "5x + y = 100", fontsize=9, color=BLUE)
    a.text(55, 10, "x + y = 60", fontsize=9, color=INK)
    a.text(4, 22, "feasible\nregion", fontsize=9)
    a.set_ylim(-6, 105)
    a.set_title("Feasible region OABC (bounded)", fontsize=10, pad=10)
    fig.tight_layout()
    save(fig, "math_ch12_fig01_feasible_region.png")


def fig02_bounded():
    """HSSLC 2026 Q33 / Ex 12.1 Q3: max 5x + 3y, 3x + 5y <= 15, 5x + 2y <= 10."""
    fig, a = plt.subplots(figsize=(5.8, 4.8))
    axes(a, (-0.3, 5.6), (-0.4, 5.6), ticks=True)
    x = np.linspace(0, 5.2, 200)
    a.plot(x, (15 - 3 * x) / 5, color=BLUE, lw=1.6)
    xx = np.linspace(0, 2.6, 100)
    a.plot(xx, (10 - 5 * xx) / 2, color=INK, lw=1.6)
    P = (20 / 19, 45 / 19)
    a.add_patch(Polygon([(0, 0), (2, 0), P, (0, 3)], closed=True, color=BLUE, alpha=0.25))
    corner(a, (0, 0), "O(0, 0)", dx=0.08, dy=-0.35)
    corner(a, (2, 0), "A(2, 0)", dx=0.08, dy=0.12)
    corner(a, P, "B(20/19, 45/19)", dx=0.12, dy=0.12)
    corner(a, (0, 3), "C(0, 3)", dx=0.1, dy=0.12)
    a.text(3.3, 1.25, "3x + 5y = 15", fontsize=9, color=BLUE)
    a.text(1.75, 4.2, "5x + 2y = 10", fontsize=9, color=INK)
    a.set_title("Max Z = 5x + 3y: Z(B) = 235/19 is the largest", fontsize=10, pad=10)
    fig.tight_layout()
    save(fig, "math_ch12_fig02_bounded_max.png")


def fig03_unbounded():
    """HSSLC 2020 (NC) Q32 / Ex 12.1 Q4: min 3x + 5y, x + 3y >= 3, x + y >= 2."""
    fig, a = plt.subplots(figsize=(5.8, 4.8))
    axes(a, (-0.3, 4.6), (-0.3, 3.6), ticks=True)
    X, Y = 4.4, 3.4
    a.add_patch(Polygon([(0, 2), (1.5, 0.5), (3, 0), (X, 0), (X, Y), (0, Y)], closed=True, color=BLUE, alpha=0.25))
    x = np.linspace(0, 4.4, 200)
    a.plot(x, (3 - x) / 3, color=BLUE, lw=1.6)
    a.plot(x[x <= 2.2], 2 - x[x <= 2.2], color=INK, lw=1.6)
    xd = np.linspace(0, 7 / 3, 100)
    a.plot(xd, (7 - 3 * xd) / 5, color=RED, lw=1.4, ls="--")
    corner(a, (0, 2), "C(0, 2)", dx=0.1, dy=0.08)
    corner(a, (1.5, 0.5), "B(3/2, 1/2)", dx=0.12, dy=0.1)
    corner(a, (3, 0), "A(3, 0)", dx=0.05, dy=0.12)
    a.text(3.0, 0.42, "x + 3y = 3", fontsize=9, color=BLUE)
    a.text(1.05, 1.15, "x + y = 2", fontsize=9, color=INK)
    a.annotate("3x + 5y = 7", xy=(0.6, 1.04), xytext=(0.12, 0.42), fontsize=9, color=RED,
               arrowprops=dict(arrowstyle="-|>", color=RED, lw=0.9))
    a.text(2.6, 2.3, "unbounded\nfeasible region", fontsize=9)
    a.set_title("Min Z = 3x + 5y: the half-plane 3x + 5y < 7 misses the region", fontsize=10, pad=10)
    fig.tight_layout()
    save(fig, "math_ch12_fig03_unbounded_min.png")


if __name__ == "__main__":
    fig01_dealer()
    fig02_bounded()
    fig03_unbounded()
