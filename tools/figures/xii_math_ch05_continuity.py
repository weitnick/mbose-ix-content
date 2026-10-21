"""Figures for Class XII Mathematics Chapter 5, Continuity and Differentiability.
Run: python xii_math_ch05_continuity.py
"""
from xii_math_common import *


def fig01_jump_and_corner():
    fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
    # (a) jump: f(x) = x + 5 (x <= 1), x - 5 (x > 1)
    a = axs[0]
    axes(a, (-3, 4), (-6, 9), ticks=True)
    x1 = np.linspace(-3, 1, 50)
    x2 = np.linspace(1, 4, 50)
    a.plot(x1, x1 + 5, color=BLUE, lw=2.2)
    a.plot(x2, x2 - 5, color=BLUE, lw=2.2)
    a.plot([1], [6], "o", color=BLUE, ms=6)
    a.plot([1], [-4], "o", mfc="white", mec=BLUE, ms=6, mew=1.6)
    a.axvline(1, color=GREY, lw=0.7, ls=":")
    a.text(1.2, 6.3, "f(1) = 6 (LHL = 6)", fontsize=8.5, color=INK)
    a.text(1.2, -4.9, "RHL = −4", fontsize=8.5, color=INK)
    a.set_title("(a) A jump at x = 1: not continuous", fontsize=10, pad=10)
    # (b) corner: f(x) = |x - 5|
    b = axs[1]
    axes(b, (0, 10), (-1, 6), ticks=True)
    x = np.linspace(0, 10, 200)
    b.plot(x, np.abs(x - 5), color=BLUE, lw=2.2)
    b.plot([5], [0], "o", color=BLUE, ms=6)
    b.text(5.3, -0.65, "corner at (5, 0)", fontsize=8.5, color=INK)
    b.text(1.0, 4.6, "slope −1", fontsize=8.5, color=GREY)
    b.text(7.6, 4.6, "slope +1", fontsize=8.5, color=GREY)
    b.set_title("(b) y = |x − 5|: continuous, not differentiable at 5", fontsize=10, pad=10)
    fig.tight_layout()
    save(fig, "math_ch05_fig01_jump_and_corner.png")


if __name__ == "__main__":
    fig01_jump_and_corner()
