"""Figures for Class XII Mathematics Chapter 10, Vector Algebra.
Run: python xii_math_ch10_vectors.py
"""
from xii_math_common import *


def _arrow(a, p, q, color, label=None, off=(0, 0), lw=2.0):
    a.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=14))
    if label:
        a.text((p[0] + q[0]) / 2 + off[0], (p[1] + q[1]) / 2 + off[1], label, fontsize=11, color=color,
               ha="center", va="center", style="italic")


def fig01_laws_and_products():
    fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.8))
    for a in axs:
        a.set_aspect("equal"); a.axis("off")
    # (a) triangle law
    a = axs[0]
    A, B, C = (0, 0), (3, 0.6), (4.2, 2.6)
    _arrow(a, A, B, BLUE, "a", (0.0, -0.35))
    _arrow(a, B, C, BLUE, "b", (0.4, -0.1))
    _arrow(a, A, C, INK, "a + b", (-0.55, 0.35))
    for P, n, d in ((A, "A", (-0.25, -0.15)), (B, "B", (0.15, -0.25)), (C, "C", (0.15, 0.1))):
        a.text(P[0] + d[0], P[1] + d[1], n, fontsize=10)
    a.set_xlim(-0.6, 4.8); a.set_ylim(-0.8, 3.2)
    a.set_title("(a) Triangle law: AB + BC = AC", fontsize=10)
    # (b) parallelogram and area |a × b|
    b = axs[1]
    O, P, Q, R = (0, 0), (3.2, 0), (4.2, 1.8), (1.0, 1.8)
    b.fill([O[0], P[0], Q[0], R[0]], [O[1], P[1], Q[1], R[1]], color=BLUE, alpha=0.18)
    _arrow(b, O, P, BLUE, "a", (0, -0.3))
    _arrow(b, O, R, BLUE, "b", (-0.35, 0.05))
    b.plot([P[0], Q[0], R[0]], [P[1], Q[1], R[1]], color=GREY, lw=1.0, ls="--")
    b.plot([1.0, 1.0], [0, 1.8], color=GREY, lw=0.8, ls=":")
    b.text(1.12, 0.75, "|b| sin θ", fontsize=9, color=GREY)
    b.text(0.45, 0.18, "θ", fontsize=10)
    b.text(2.1, 1.0, "area = |a × b|", fontsize=9.5, color=INK)
    b.set_xlim(-0.6, 4.8); b.set_ylim(-0.8, 2.4)
    b.set_title("(b) Parallelogram: area = |a||b| sin θ", fontsize=10)
    # (c) projection of a on b
    c = axs[2]
    O = (0, 0); A2 = (2.4, 2.0); Bd = (4.4, 0.0)
    _arrow(c, O, Bd, BLUE, "b", (1.6, 0.25))
    _arrow(c, O, A2, INK, "a", (-0.3, 0.25))
    c.plot([A2[0], A2[0]], [A2[1], 0], color=GREY, lw=0.8, ls=":")
    c.plot([0, A2[0]], [-0.25, -0.25], color=GREY, lw=1.0)
    c.text(A2[0] / 2, -0.55, "projection = a · b / |b|", fontsize=9, ha="center", color=GREY)
    c.text(0.55, 0.18, "θ", fontsize=10)
    c.set_xlim(-0.6, 4.8); c.set_ylim(-0.9, 2.6)
    c.set_title("(c) Projection of a on b", fontsize=10)
    fig.tight_layout()
    save(fig, "math_ch10_fig01_laws_products.png")


if __name__ == "__main__":
    fig01_laws_and_products()
