"""Figures for Class X Mathematics, Chapter 14: Probability.
Run: python x_ch14_probability.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrow, Rectangle, Wedge

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, SHADE = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#BFD3E6"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


# Fig 14.1: the 36 outcomes of throwing two dice, sum 8 highlighted
def fig_two_dice():
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    for i in range(6):
        for j in range(6):
            b, g = i + 1, j + 1
            x, y = 1 + j, 6 - i
            hit = b + g == 8
            ax.add_patch(Rectangle((x, y), 1, 1, fc=HI if hit else SOFT, ec=ACC, lw=0.9))
            ax.text(x + 0.5, y + 0.5, f"({b}, {g})", ha="center", va="center", fontsize=8.5,
                    color="white" if hit else INK, fontweight="bold" if hit else "normal")
    for k in range(6):
        ax.text(0.55, 6.5 - k, str(k + 1), ha="center", va="center", fontsize=10, color=ACC, fontweight="bold")
        ax.text(1.5 + k, 7.35, str(k + 1), ha="center", va="center", fontsize=10, color=ACC, fontweight="bold")
    ax.text(4, 7.85, "grey die", ha="center", va="center", fontsize=9, color=GREY)
    ax.text(-0.05, 4, "blue die", ha="center", va="center", fontsize=9, color=GREY, rotation=90)
    ax.text(4, 0.45, "highlighted: sum of the two numbers = 8  (5 of the 36 outcomes)", ha="center",
            va="center", fontsize=9, color=INK)
    ax.set_xlim(-0.3, 7.1)
    ax.set_ylim(0.1, 8.1)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "ch14_fig01_two_dice.png")


# Fig 14.2: spinner with eight equal sectors (Ex 14.1 Q12)
def fig_spinner():
    fig, ax = plt.subplots(figsize=(3.4, 3.4))
    r = 1.5
    for k in range(8):
        a1 = 90 - 45 * (k + 1)
        ax.add_patch(Wedge((0, 0), r, a1, a1 + 45, fc=SOFT if k % 2 else SHADE, ec=ACC, lw=1.2))
        mid = np.radians(a1 + 22.5)
        ax.text(1.05 * np.cos(mid), 1.05 * np.sin(mid), str(k + 1), ha="center", va="center", fontsize=13,
                color=INK, fontweight="bold")
    ang = np.radians(90 - 45 * 2 - 22.5)
    ax.add_patch(FancyArrow(-0.35 * np.cos(ang), -0.35 * np.sin(ang), 1.05 * np.cos(ang), 1.05 * np.sin(ang),
                            width=0.06, head_width=0.2, head_length=0.22, length_includes_head=True,
                            fc=HI, ec=INK, lw=0.8))
    ax.add_patch(Circle((0, 0), 0.08, fc=INK, ec=INK))
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.7, 1.7)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "ch14_fig02_spinner.png")


# Fig 14.3: a rectangle 3 m by 2 m with a circle of diameter 1 m (Ex 14.1 Q20, not for the examination)
def fig_rect_circle():
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    ax.add_patch(Rectangle((0, 0), 3, 2, fc=SOFT, ec=ACC, lw=1.4))
    ax.add_patch(Circle((1.5, 1.0), 0.5, fc=SHADE, ec=INK, lw=1.3))
    ax.plot([1.0, 2.0], [1.0, 1.0], color=INK, lw=1.0, ls="--")
    ax.text(1.5, 1.1, "1 m", ha="center", va="bottom", fontsize=10, color=INK)
    ax.annotate("", xy=(0, -0.22), xytext=(3, -0.22), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9),
                annotation_clip=False)
    ax.text(1.5, -0.34, "3 m", ha="center", va="top", fontsize=10, color=INK)
    ax.annotate("", xy=(3.22, 0), xytext=(3.22, 2), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9),
                annotation_clip=False)
    ax.text(3.32, 1.0, "2 m", ha="left", va="center", fontsize=10, color=INK)
    ax.set_xlim(-0.2, 3.7)
    ax.set_ylim(-0.6, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "ch14_fig03_rectangle_circle.png")


if __name__ == "__main__":
    fig_two_dice()
    fig_spinner()
    fig_rect_circle()
