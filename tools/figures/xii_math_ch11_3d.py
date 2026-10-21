"""Figures for Class XII Mathematics Chapter 11, Three Dimensional Geometry.
Run: python xii_math_ch11_3d.py
"""
from xii_math_common import *


def fig01_line_and_skew():
    fig = plt.figure(figsize=(10.0, 4.4))
    # (a) direction angles of a line
    a = fig.add_subplot(1, 2, 1, projection="3d")
    for v, lab in (((3, 0, 0), "x"), ((0, 3, 0), "y"), ((0, 0, 3), "z")):
        a.plot([0, v[0]], [0, v[1]], [0, v[2]], color=GREY, lw=1.2)
        a.text(v[0] * 1.05, v[1] * 1.05, v[2] * 1.05, lab, fontsize=10)
    P = np.array([2.4, 2.2, 1.8])
    a.plot([0, P[0]], [0, P[1]], [0, P[2]], color=BLUE, lw=2.2)
    a.text(P[0], P[1], P[2] + 0.15, "P(x, y, z)", fontsize=9)
    a.text(0.9, 0.25, 0.1, "α", fontsize=11, color=INK)
    a.text(0.3, 0.9, 0.1, "β", fontsize=11, color=INK)
    a.text(0.25, 0.25, 0.9, "γ", fontsize=11, color=INK)
    a.set_title("(a) l = cos α, m = cos β, n = cos γ", fontsize=10)
    a.set_axis_off()
    a.view_init(elev=22, azim=-60)
    # (b) skew lines and their common perpendicular
    b = fig.add_subplot(1, 2, 2, projection="3d")
    t = np.linspace(-1.5, 1.5, 2)
    L1 = np.array([[0, 0, 0] + s * np.array([1, 0, 0]) for s in t])
    L2 = np.array([[0, 0, 2] + s * np.array([0, 1, 0]) for s in t])
    b.plot(L1[:, 0], L1[:, 1], L1[:, 2], color=BLUE, lw=2.2)
    b.plot(L2[:, 0], L2[:, 1], L2[:, 2], color=INK, lw=2.2)
    b.plot([0, 0], [0, 0], [0, 2], color=GREY, lw=1.4, ls="--")
    b.text(1.5, 0, -0.3, "l₁: r = a₁ + λb₁", fontsize=9, color=BLUE)
    b.text(0, 1.5, 2.2, "l₂: r = a₂ + μb₂", fontsize=9, color=INK)
    b.text(0.1, 0.1, 1.0, "shortest distance d", fontsize=9, color=GREY)
    b.set_title("(b) Skew lines: d = |(b₁ × b₂)·(a₂ − a₁)| / |b₁ × b₂|", fontsize=10)
    b.set_axis_off()
    b.view_init(elev=18, azim=40)
    fig.tight_layout()
    save(fig, "math_ch11_fig01_lines.png")


if __name__ == "__main__":
    fig01_line_and_skew()
