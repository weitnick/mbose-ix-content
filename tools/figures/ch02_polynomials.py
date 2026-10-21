"""Figures for Class IX Mathematics, Chapter 2: Polynomials."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "CLASS IX Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, WARM = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#FDF7EA"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def area_diagram(w1, w2, h1, h2, labels, top, left, name, total_label):
    fig, ax = plt.subplots(figsize=(3.8, 3.8))
    cells = [(0, h2, w1, h1, labels[0], SOFT), (w1, h2, w2, h1, labels[1], WARM),
             (0, 0, w1, h2, labels[2], WARM), (w1, 0, w2, h2, labels[3], "#E3ECF6")]
    for x0, y0, w, h, lab, c in cells:
        ax.add_patch(Rectangle((x0, y0), w, h, fc=c, ec=ACC, lw=1.2))
        ax.text(x0 + w / 2, y0 + h / 2, lab, ha="center", va="center", fontsize=13, color=INK)
    W, H = w1 + w2, h1 + h2
    ax.text(w1 / 2, H + 0.12, top[0], ha="center", fontsize=12, color=ACC)
    ax.text(w1 + w2 / 2, H + 0.12, top[1], ha="center", fontsize=12, color=HI)
    ax.text(-0.14, h2 + h1 / 2, left[0], ha="right", va="center", fontsize=12, color=ACC)
    ax.text(-0.14, h2 / 2, left[1], ha="right", va="center", fontsize=12, color=HI)
    ax.text(W / 2, -0.32, total_label, ha="center", fontsize=11, color=INK)
    ax.set_xlim(-0.8, W + 0.2); ax.set_ylim(-0.55, H + 0.45); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)


if __name__ == "__main__":
    area_diagram(2.2, 1.0, 2.2, 1.0, ["$x^2$", "$xy$", "$xy$", "$y^2$"], ["$x$", "$y$"], ["$x$", "$y$"],
                 "ch02_fig01_square_identity.png", "Area $= (x+y)^2 = x^2 + 2xy + y^2$")
    area_diagram(2.2, 0.8, 2.2, 1.2, ["$x^2$", "$ax$", "$bx$", "$ab$"], ["$x$", "$a$"], ["$x$", "$b$"],
                 "ch02_fig02_product_identity.png", "Area $= (x+a)(x+b) = x^2 + (a+b)x + ab$")
