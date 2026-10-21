"""Figures for Class XII Mathematics Chapter 6, Application of Derivatives.
Run: python xii_math_ch06_derivatives.py
"""
from xii_math_common import *
from matplotlib.patches import Circle


def fig01_increasing_decreasing():
    fig, a = plt.subplots(figsize=(7.2, 4.4))
    axes(a, (-4.5, 5.5), (-100, 80), ticks=True)
    x = np.linspace(-4.2, 5.2, 400)
    y = 2 * x**3 - 3 * x**2 - 36 * x + 7
    a.plot(x, y, color=BLUE, lw=2.2)
    a.plot([-2], [51], "o", color=BLUE, ms=6)
    a.plot([3], [-74], "o", color=BLUE, ms=6)
    a.text(-1.8, 58, "local max (−2, 51)", fontsize=9, color=INK)
    a.text(3.2, -86, "local min (3, −74)", fontsize=9, color=INK)
    for xv in (-2, 3):
        a.axvline(xv, color=GREY, lw=0.7, ls=":")
    a.text(-4.3, 70, "increasing", fontsize=9, color=GREY)
    a.text(0.9, 25, "decreasing", fontsize=9, color=GREY)
    a.text(4.0, 10, "increasing", fontsize=9, color=GREY)
    a.set_title("f(x) = 2x³ − 3x² − 36x + 7:  f′(x) = 6(x + 2)(x − 3)", fontsize=10, pad=10)
    fig.tight_layout()
    save(fig, "math_ch06_fig01_increasing_decreasing.png")


def fig02_solids_in_sphere():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.4))
    R = 1.0
    # (a) cone in a sphere: apex at top (0, R), base at y = R - h, h = 4R/3
    a = axs[0]
    a.set_aspect("equal"); a.axis("off")
    a.add_patch(Circle((0, 0), R, fill=False, ec=GREY, lw=1.6))
    h = 4 * R / 3
    yb = R - h
    r = np.sqrt(R**2 - yb**2)
    a.plot([0, -r, r, 0], [R, yb, yb, R], color=BLUE, lw=2.0)
    a.plot([0, 0], [R, yb], color=INK, lw=0.9, ls="--")
    a.plot([0, r], [0, yb], color=INK, lw=0.9)
    a.plot([0], [0], "o", color=INK, ms=3)
    a.text(0.05, 0.05, "O", fontsize=9)
    a.text(0.5, -0.1, "R", fontsize=10, color=INK)
    a.text(-0.32, 0.25, "h", fontsize=10, color=INK)
    a.text(0.2, yb - 0.13, "r", fontsize=10, color=INK)
    a.set_xlim(-1.25, 1.25); a.set_ylim(-1.25, 1.25)
    a.set_title("(a) Cone in a sphere: h = 4R/3, V = (8/27)·sphere", fontsize=10)
    # (b) cylinder in a sphere: height H, radius r, r² = R² − H²/4, H = 2R/√3
    b = axs[1]
    b.set_aspect("equal"); b.axis("off")
    b.add_patch(Circle((0, 0), R, fill=False, ec=GREY, lw=1.6))
    H = 2 * R / np.sqrt(3)
    rc = np.sqrt(R**2 - H**2 / 4)
    b.plot([-rc, rc, rc, -rc, -rc], [-H / 2, -H / 2, H / 2, H / 2, -H / 2], color=BLUE, lw=2.0)
    b.plot([0, rc], [0, H / 2], color=INK, lw=0.9)
    b.plot([0, 0], [0, H / 2], color=INK, lw=0.9, ls="--")
    b.plot([0], [0], "o", color=INK, ms=3)
    b.text(0.05, -0.12, "O", fontsize=9)
    b.text(0.42, 0.18, "R", fontsize=10, color=INK)
    b.text(-0.22, 0.25, "H/2", fontsize=10, color=INK)
    b.text(0.3, H / 2 + 0.05, "r", fontsize=10, color=INK)
    b.set_xlim(-1.25, 1.25); b.set_ylim(-1.25, 1.25)
    b.set_title("(b) Cylinder in a sphere: H = 2R/√3", fontsize=10)
    fig.tight_layout()
    save(fig, "math_ch06_fig02_solids_in_sphere.png")


if __name__ == "__main__":
    fig01_increasing_decreasing()
    fig02_solids_in_sphere()
