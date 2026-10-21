"""Figures for Class IX Mathematics, Chapter 3: Coordinate Geometry."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "CLASS IX Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GRID = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#D9E1EA"
plt.rcParams.update({"font.size": 9, "mathtext.fontset": "cm"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def axes(ax, n=7, labels=True, names=True):
    for k in range(-n, n + 1):
        ax.plot([k, k], [-n, n], color=GRID, lw=0.5, zorder=0)
        ax.plot([-n, n], [k, k], color=GRID, lw=0.5, zorder=0)
    ax.annotate("", xy=(n + 0.6, 0), xytext=(-n - 0.6, 0), arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1))
    ax.annotate("", xy=(0, n + 0.6), xytext=(0, -n - 0.6), arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1))
    if labels:
        for k in range(-n, n + 1):
            if k:
                ax.text(k, -0.45, str(k), ha="center", va="center", fontsize=6.5, color="#5D6B7A")
                ax.text(-0.3, k, str(k), ha="right", va="center", fontsize=6.5, color="#5D6B7A")
    if names:
        ax.text(n + 0.8, 0.3, "X", fontsize=9, weight="bold"); ax.text(-n - 1.1, 0.3, "X′", fontsize=9, weight="bold")
        ax.text(0.3, n + 0.7, "Y", fontsize=9, weight="bold"); ax.text(0.3, -n - 1.0, "Y′", fontsize=9, weight="bold")
        ax.text(-0.45, -0.5, "O", fontsize=9, weight="bold")
    ax.set_xlim(-n - 1.3, n + 1.3); ax.set_ylim(-n - 1.3, n + 1.3); ax.set_aspect("equal"); ax.axis("off")


def point(ax, x, y, name, dx=0.25, dy=0.3, color=ACC):
    ax.plot([x], [y], "o", color=color, ms=4, zorder=5)
    ax.text(x + dx, y + dy, name, fontsize=9, color=color, weight="bold", zorder=6)


def fig_street_plan():
    fig, ax = plt.subplots(figsize=(4.4, 4.4))
    for k in range(1, 6):
        ax.plot([k, k], [0.4, 5.6], color=ACC, lw=1.4)
        ax.plot([0.4, 5.6], [k, k], color=HI, lw=1.4)
        ax.text(k, 0.1, str(k), ha="center", fontsize=9, color=ACC)
        ax.text(0.15, k, str(k), va="center", ha="right", fontsize=9, color=HI)
    for (x, y, lab) in [(4, 3, "(4, 3)"), (3, 4, "(3, 4)")]:
        ax.plot([x], [y], "o", color=INK, ms=6, zorder=5)
        ax.text(x + 0.12, y + 0.15, lab, fontsize=9, weight="bold")
    ax.text(3, -0.45, "Streets running North–South (numbered West to East)", ha="center", fontsize=8, color=ACC)
    ax.text(-0.7, 3, "Streets running East–West", rotation=90, va="center", fontsize=8, color=HI)
    ax.text(5.9, 5.9, "N ↑", fontsize=9)
    ax.set_xlim(-1, 6.2); ax.set_ylim(-0.8, 6.2); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch03_fig01_street_plan.png")


def fig_quadrants():
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    axes(ax, n=5, labels=False)
    for (x, y, q, s, c) in [(2.6, 2.6, "Quadrant I", "(+, +)", SOFT), (-2.6, 2.6, "Quadrant II", "(−, +)", "#FDF7EA"),
                            (-2.6, -2.6, "Quadrant III", "(−, −)", SOFT), (2.6, -2.6, "Quadrant IV", "(+, −)", "#FDF7EA")]:
        ax.add_patch(Rectangle((x - 1.9, y - 1.2), 3.8, 2.4, fc=c, ec="none", zorder=1))
        ax.text(x, y + 0.35, q, ha="center", fontsize=10, weight="bold", color=ACC, zorder=2)
        ax.text(x, y - 0.45, s, ha="center", fontsize=11, color=INK, zorder=2)
    ax.text(4.2, -0.6, "x-axis", fontsize=8, color=INK); ax.text(0.25, 4.6, "y-axis", fontsize=8, color=INK)
    save(fig, "ch03_fig02_quadrants.png")


def fig_p_q():
    fig, ax = plt.subplots(figsize=(5.0, 4.2))
    axes(ax, n=7)
    for (x, y, n, m1, m2) in [(4, 3, "P(4, 3)", "M", "N"), (-6, -2, "Q(−6, −2)", "R", "S")]:
        ax.plot([x, x], [0, y], ls="--", color=HI, lw=1)
        ax.plot([0, x], [y, y], ls="--", color=HI, lw=1)
        point(ax, x, y, n, dx=0.2 if x > 0 else -2.6, dy=0.3 if y > 0 else -0.8)
        ax.text(x + 0.15, -0.9 if y > 0 else 0.25, m1, fontsize=9, color=HI, weight="bold")
        ax.text(0.2 if x > 0 else 0.2, y + 0.2, m2, fontsize=9, color=HI, weight="bold")
    save(fig, "ch03_fig03_points_P_Q.png")


def fig_example1():
    fig, ax = plt.subplots(figsize=(4.8, 4.8))
    axes(ax, n=6)
    for (x, y, n) in [(4, 3, "B"), (-3, 4, "M"), (-5, -4, "L"), (3, -4, "S")]:
        ax.plot([x, x], [0, y], ls=":", color=HI, lw=0.9); ax.plot([0, x], [y, y], ls=":", color=HI, lw=0.9)
        point(ax, x, y, n)
    save(fig, "ch03_fig04_example_points.png")


def fig_axes_points():
    fig, ax = plt.subplots(figsize=(4.8, 4.8))
    axes(ax, n=6)
    for (x, y, n, dx, dy) in [(4, 0, "A", 0.1, 0.3), (0, 3, "B", 0.25, 0.1), (-5, 0, "C", -0.2, 0.35), (0, -4, "D", 0.25, 0.0), (2 / 3, 0, "E", 0.05, 0.35)]:
        point(ax, x, y, n, dx=dx, dy=dy)
    save(fig, "ch03_fig05_points_on_axes.png")


def fig_exercise_32():
    fig, ax = plt.subplots(figsize=(5.2, 5.2))
    axes(ax, n=7)
    for (x, y, n) in [(-5, 2, "B"), (5, -5, "C"), (6, 5, "D"), (-3, -5, "E"), (2, -4, "G"), (-6, -3, "H"), (0, 5, "L"), (-3, 0, "M")]:
        point(ax, x, y, n, dx=0.25, dy=0.25 if y >= 0 else -0.8)
    save(fig, "ch03_fig06_exercise_3_2.png")


def fig_seating():
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    for c in range(1, 7):
        for r in range(1, 5):
            fc = "#FDF7EA" if (c, r) == (5, 3) else ("#E3ECF6" if (c, r) == (4, 1) else SOFT)
            ax.add_patch(Rectangle((c - 0.45, r - 0.4), 0.9, 0.8, fc=fc, ec=ACC, lw=0.8))
    ax.text(5, 3, "You\n(5, 3)", ha="center", va="center", fontsize=7.5, weight="bold")
    ax.text(4, 1, "Sonia\n(4, 1)", ha="center", va="center", fontsize=7.5)
    for c in range(1, 7):
        ax.text(c, 0.3, str(c), ha="center", fontsize=8, color=ACC)
    for r in range(1, 5):
        ax.text(0.3, r, str(r), va="center", ha="center", fontsize=8, color=HI)
    ax.text(3.5, -0.2, "Column", ha="center", fontsize=8, color=ACC); ax.text(-0.25, 2.5, "Row", rotation=90, va="center", fontsize=8, color=HI)
    ax.set_xlim(-0.5, 6.6); ax.set_ylim(-0.5, 4.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch03_fig07_seating_plan.png")


if __name__ == "__main__":
    fig_street_plan(); fig_quadrants(); fig_p_q(); fig_example1(); fig_axes_points(); fig_exercise_32(); fig_seating()
