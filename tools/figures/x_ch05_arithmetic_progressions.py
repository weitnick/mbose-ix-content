"""Figures for Class X Mathematics, Chapter 5: Arithmetic Progressions.
Run: python x_ch05_arithmetic_progressions.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, WOOD = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#C9A27A"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


# Fig 5.1: ladder whose 8 rungs shrink by 2 cm from 45 cm (bottom) to 31 cm (top)
def fig_ladder():
    fig, ax = plt.subplots(figsize=(3.6, 4.2))
    lengths = [45 - 2 * k for k in range(8)]
    s = 0.1  # drawing units per cm
    for k, L in enumerate(lengths):
        y = 0.9 * k
        half = L * s / 2
        ax.plot([-half, half], [y, y], color=WOOD, lw=4, solid_capstyle="round")
        ax.text(half + 0.35, y, f"{L} cm", va="center", fontsize=8.5, color=INK)
    top, bot = lengths[-1] * s / 2, lengths[0] * s / 2
    for sgn in (-1, 1):
        ax.plot([sgn * (bot + 0.15), sgn * (top + 0.15)], [-0.3, 0.9 * 7 + 0.4], color=INK, lw=1.8)
    ax.text(0, -0.85, "bottom rung", ha="center", fontsize=8.5, color=ACC)
    ax.text(0, 0.9 * 7 + 0.75, "top rung", ha="center", fontsize=8.5, color=ACC)
    ax.set_xlim(-3.0, 3.6); ax.set_ylim(-1.2, 7.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch05_fig01_ladder.png")


# Fig 5.2: squares of side 1, 2, 3 made of unit squares (1, 4, 9 squares)
def fig_squares():
    fig, ax = plt.subplots(figsize=(4.6, 1.9))
    x0 = 0
    for n in (1, 2, 3):
        for i in range(n):
            for j in range(n):
                ax.add_patch(Rectangle((x0 + i, j), 1, 1, fc=SOFT, ec=ACC, lw=1.1))
        ax.text(x0 + n / 2, -0.45, f"side {n}\n{n * n} unit square{'s' if n > 1 else ''}", ha="center", va="top",
                fontsize=9, linespacing=1.3)
        x0 += n + 2.0
    ax.set_xlim(-1.0, x0 - 1.4); ax.set_ylim(-1.6, 3.2); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch05_fig02_unit_squares.png")


# Fig 5.3: spiral of successive semicircles, centres alternately A and B, radii 0.5, 1.0, 1.5, ...
def fig_spiral():
    fig, ax = plt.subplots(figsize=(3.8, 3.2))
    A, B = np.array([0.0, 0.0]), np.array([0.5, 0.0])
    start = np.array([0.5, 0.0])  # the spiral starts at B and the first semicircle (centre A, r = 0.5) goes over the top
    cur = start
    for k in range(1, 8):
        c = A if k % 2 == 1 else B
        r = 0.5 * k
        if k % 2 == 1:   # centre A: upper half, from right to left
            theta1, theta2 = 0, 180
        else:            # centre B: lower half, from left to right
            theta1, theta2 = 180, 360
        ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=theta1, theta2=theta2, color=ACC, lw=1.4))
        if k <= 3:
            ang = np.radians(90 if k % 2 == 1 else 270)
            ax.text(*(c + (r + 0.18) * np.array([np.cos(ang), np.sin(ang)])), f"$l_{k}$", ha="center", va="center",
                    fontsize=13, color=HI)
    for pt, lab, off in [(A, "A", (-4, -12)), (B, "B", (2, 4))]:
        ax.plot(*pt, "o", ms=4, color=INK)
        ax.annotate(lab, pt, textcoords="offset points", xytext=off, fontsize=10, color=INK)
    ax.set_xlim(-4.0, 4.4); ax.set_ylim(-4.0, 4.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch05_fig03_spiral.png")


# Fig 5.4: logs stacked 20, 19, 18, ... (only the first few rows drawn, then a gap)
def fig_logs():
    fig, ax = plt.subplots(figsize=(5.2, 2.6))
    r = 0.5
    rows = [20, 19, 18, 17]
    for k, n in enumerate(rows):
        y = r + k * r * np.sqrt(3)
        x_start = r + k * r
        for i in range(n):
            ax.add_patch(Circle((x_start + 2 * r * i, y), r * 0.96, fc=WOOD, ec="#8A6640", lw=0.8))
        ax.text(x_start + 2 * r * n + 0.3, y, f"{n} logs", va="center", fontsize=9, color=INK)
    ytop = r + 4 * r * np.sqrt(3)
    ax.text(10.5, ytop + 0.2, "⋮  and so on, one fewer log in each row", ha="center", fontsize=9, color=ACC)
    ax.set_xlim(-0.2, 24.5); ax.set_ylim(-0.2, ytop + 0.8); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch05_fig04_logs.png")


# Fig 5.5: potato race - bucket, first potato 5 m away, then potatoes 3 m apart (10 potatoes)
def fig_potato():
    fig, ax = plt.subplots(figsize=(6.4, 1.7))
    xs = [5 + 3 * i for i in range(10)]
    ax.plot([0, xs[-1] + 1], [0, 0], color="#9AA5B1", lw=0.8)
    ax.add_patch(Rectangle((-0.9, -0.1), 1.8, 1.4, fc=SOFT, ec=ACC, lw=1.2))
    ax.text(0, -1.0, "bucket", ha="center", va="top", fontsize=9)
    for i, x in enumerate(xs):
        ax.add_patch(Circle((x, 0.45), 0.55, fc="#D9B38C", ec="#8A6640", lw=0.8))
    ax.annotate("", xy=(0, 1.75), xytext=(5, 1.75), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9))
    ax.text(2.5, 2.05, "5 m", ha="center", fontsize=9)
    for a, b in [(5, 8), (8, 11)]:
        ax.annotate("", xy=(a, 1.75), xytext=(b, 1.75), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9))
        ax.text((a + b) / 2, 2.05, "3 m", ha="center", fontsize=9)
    ax.text(xs[-1], -1.0, "10th potato", ha="center", va="top", fontsize=9)
    ax.set_xlim(-1.5, xs[-1] + 1.5); ax.set_ylim(-2.2, 2.5); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch05_fig05_potato_race.png")


if __name__ == "__main__":
    fig_ladder()
    fig_squares()
    fig_spiral()
    fig_logs()
    fig_potato()
