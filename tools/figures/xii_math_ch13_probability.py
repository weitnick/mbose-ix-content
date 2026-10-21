"""Figures for Class XII Mathematics Chapter 13, Probability.
Run: python xii_math_ch13_probability.py
"""
from xii_math_common import *
from matplotlib.patches import Circle, Rectangle


def fig01_conditional():
    """Venn picture of P(E|F) = P(E ∩ F) / P(F): F becomes the new sample space."""
    fig, a = canvas(6.4, 3.6, (0, 10), (0, 5.6))
    a.add_patch(Rectangle((0.3, 0.3), 9.4, 4.9, fill=False, ec=GREY, lw=1.2))
    a.text(0.5, 4.75, "S", fontsize=11, color=GREY)
    a.add_patch(Circle((3.8, 2.7), 1.8, fc=SOFT, ec=INK, lw=1.4))
    a.add_patch(Circle((6.0, 2.7), 1.8, fc=BLUE, ec=BLUE, lw=1.6, alpha=0.28))
    a.text(2.6, 2.6, "E", fontsize=13, color=INK)
    a.text(7.1, 2.6, "F", fontsize=13, color=BLUE)
    a.text(4.9, 2.6, "E ∩ F", fontsize=10, ha="center", color=INK)
    a.text(5.0, 0.55, "Given F has occurred, only F remains possible:  P(E|F) = P(E ∩ F) / P(F)", fontsize=9,
           ha="center", color=INK)
    save(fig, "math_ch13_fig01_conditional.png")


def fig02_bayes_tree():
    """Tree diagram for the bolt factory (HSSLC 2021 OC Q28; NCERT Example 19)."""
    fig, a = canvas(7.2, 4.4, (0, 12), (0, 7.2))
    root = (0.8, 3.6)
    machines = [("A", 0.25, 0.05, 6.0), ("B", 0.35, 0.04, 3.6), ("C", 0.40, 0.02, 1.2)]
    a.plot(*root, "o", color=INK, ms=5)
    for name, pm, pd, y in machines:
        m = (4.6, y)
        a.plot([root[0], m[0]], [root[1], m[1]], color=INK, lw=1.2)
        a.text((root[0] + m[0]) / 2 - 0.2, (root[1] + m[1]) / 2 + 0.18, f"{pm:.2f}", fontsize=9, color=BLUE)
        a.text(m[0] + 0.15, m[1] + 0.15, name, fontsize=11, weight="bold")
        for lab, p, dy, col in (("defective", pd, 0.55, RED), ("good", 1 - pd, -0.55, GREY)):
            e = (8.4, y + dy)
            a.plot([m[0], e[0]], [m[1], e[1]], color=col, lw=1.1)
            a.text((m[0] + e[0]) / 2, (m[1] + e[1]) / 2 + (0.12 if dy > 0 else -0.38), f"{p:.2f}", fontsize=8.5,
                   color=col, ha="center")
            a.text(e[0] + 0.12, e[1] - 0.12, lab, fontsize=8.5, color=col)
            if lab == "defective":
                a.text(10.2, e[1] - 0.12, f"{pm:.2f} × {pd:.2f} = {pm * pd:.4f}", fontsize=8.5, color=INK)
    a.text(6.0, 7.0, "P(defective) = 0.0125 + 0.0140 + 0.0080 = 0.0345", fontsize=9.5, ha="center", color=INK)
    a.text(6.0, 0.15, "P(C | defective) = 0.0080 / 0.0345 = 16/69", fontsize=9.5, ha="center", color=RED)
    save(fig, "math_ch13_fig02_bayes_tree.png")


if __name__ == "__main__":
    fig01_conditional()
    fig02_bayes_tree()
