"""Figures for Class IX Mathematics, Chapter 5: Introduction to Euclid's Geometry."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Polygon

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "CLASS IX Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def dot(ax, x, y, name, dx=0, dy=0.18, color=INK):
    ax.plot([x], [y], "o", color=color, ms=4)
    ax.text(x + dx, y + dy, name, ha="center", fontsize=10, weight="bold", color=color)


def fig_lines_through_points():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.4))
    for k in range(7):
        t = math.pi * k / 7
        a1.plot([-1.2 * math.cos(t), 1.2 * math.cos(t)], [-1.2 * math.sin(t), 1.2 * math.sin(t)], color=ACC, lw=1)
    dot(a1, 0, 0, "P", dy=0.15)
    a1.set_title("Through one point: infinitely many lines", fontsize=8.5, color="#5D6B7A")
    a2.annotate("", xy=(1.4, 0.7), xytext=(-1.4, -0.7), arrowprops=dict(arrowstyle="<|-|>", color=ACC, lw=1.2))
    dot(a2, -0.6, -0.3, "P", dy=0.15); dot(a2, 0.6, 0.3, "Q", dy=0.15)
    a2.set_title("Through two points: exactly one line", fontsize=8.5, color="#5D6B7A")
    for a in (a1, a2):
        a.set_xlim(-1.5, 1.5); a.set_ylim(-1.3, 1.3); a.set_aspect("equal"); a.axis("off")
    save(fig, "ch05_fig01_lines_through_points.png")


def fig_segment_produced():
    fig, ax = plt.subplots(figsize=(5.6, 0.9))
    ax.plot([-2.6, -1], [0, 0], color=HI, lw=1.2, ls="--")
    ax.plot([1, 2.6], [0, 0], color=HI, lw=1.2, ls="--")
    ax.annotate("", xy=(2.9, 0), xytext=(2.5, 0), arrowprops=dict(arrowstyle="-|>", color=HI))
    ax.annotate("", xy=(-2.9, 0), xytext=(-2.5, 0), arrowprops=dict(arrowstyle="-|>", color=HI))
    ax.plot([-1, 1], [0, 0], color=ACC, lw=2.2)
    dot(ax, -1, 0, "A", dy=0.12); dot(ax, 1, 0, "B", dy=0.12)
    ax.text(0, -0.28, "terminated line (line segment) AB", ha="center", fontsize=8, color=ACC)
    ax.text(2.0, -0.28, "produced", ha="center", fontsize=8, color=HI)
    ax.set_xlim(-3.1, 3.1); ax.set_ylim(-0.45, 0.4); ax.axis("off")
    save(fig, "ch05_fig02_segment_produced.png")


def fig_fifth_postulate():
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    # AB and CD come closer together towards the left, so they meet on the left of the transversal PQ,
    # which is the side where the interior angles 1 and 2 add up to less than 180 degrees.
    ax.plot([-2.8, 2.6], [0.55, 1.4], color=ACC, lw=1.4)
    ax.plot([-2.8, 2.6], [-0.55, -1.3], color=ACC, lw=1.4)
    ax.plot([-4.3, -2.8], [0.31, 0.55], color=ACC, lw=1, ls=":")
    ax.plot([-4.3, -2.8], [-0.34, -0.55], color=ACC, lw=1, ls=":")
    ax.text(-3.05, 0.68, "A", weight="bold"); ax.text(2.7, 1.4, "B", weight="bold")
    ax.text(-3.05, -0.85, "C", weight="bold"); ax.text(2.7, -1.4, "D", weight="bold")
    ax.plot([0.4, -0.2], [1.8, -1.8], color=HI, lw=1.4)
    ax.text(0.45, 1.85, "P", weight="bold", color=HI); ax.text(-0.35, -2.0, "Q", weight="bold", color=HI)
    ax.text(-0.35, 0.62, "1", fontsize=10, color=INK); ax.text(-0.5, -0.72, "2", fontsize=10, color=INK)
    ax.text(-3.6, -1.35, "the lines meet\non this side", fontsize=8, color="#5D6B7A", ha="center")
    ax.annotate("", xy=(-4.1, -0.1), xytext=(-3.6, -1.0), arrowprops=dict(arrowstyle="->", color="#5D6B7A", lw=0.8))
    ax.text(1.0, -1.95, r"$\angle 1 + \angle 2 < 180^\circ$", fontsize=10, color=INK)
    ax.set_xlim(-4.6, 3.0); ax.set_ylim(-2.2, 2.1); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch05_fig03_fifth_postulate.png")


def fig_equilateral():
    fig, ax = plt.subplots(figsize=(4.4, 3.4))
    A, B = (0, 0), (2, 0)
    C = (1, math.sqrt(3))
    for centre in (A, B):
        ax.add_patch(Circle(centre, 2, fill=False, ec=ACC, lw=0.9, ls="--"))
    ax.add_patch(Polygon([A, B, C], closed=True, fill=True, fc=SOFT, ec=HI, lw=1.6))
    dot(ax, *A, "A", dx=-0.15, dy=-0.3); dot(ax, *B, "B", dx=0.15, dy=-0.3); dot(ax, *C, "C", dy=0.15)
    ax.set_xlim(-2.2, 4.2); ax.set_ylim(-2.2, 2.3); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch05_fig04_equilateral_construction.png")


def fig_four_points():
    fig, ax = plt.subplots(figsize=(5.4, 1.1))
    xs = {"A": 0, "B": 1.4, "C": 3.0, "D": 4.4}
    ax.plot([-0.3, 4.7], [0, 0], color=INK, lw=1)
    for n, x in xs.items():
        dot(ax, x, 0, n, dy=0.12)
    ax.annotate("", xy=(3.0, -0.25), xytext=(0, -0.25), arrowprops=dict(arrowstyle="<->", color=ACC))
    ax.text(1.5, -0.45, "AC", ha="center", fontsize=8.5, color=ACC)
    ax.annotate("", xy=(4.4, -0.62), xytext=(1.4, -0.62), arrowprops=dict(arrowstyle="<->", color=HI))
    ax.text(2.9, -0.85, "BD", ha="center", fontsize=8.5, color=HI)
    ax.set_xlim(-0.5, 4.9); ax.set_ylim(-1.0, 0.4); ax.axis("off")
    save(fig, "ch05_fig05_four_points.png")


def fig_midpoint():
    fig, ax = plt.subplots(figsize=(4.8, 0.9))
    ax.plot([0, 4], [0, 0], color=ACC, lw=1.8)
    dot(ax, 0, 0, "A", dy=0.12); dot(ax, 2, 0, "C", dy=0.12, color=HI); dot(ax, 4, 0, "B", dy=0.12)
    for x in (1, 3):
        ax.plot([x - 0.05, x + 0.05], [-0.08, 0.08], color=HI, lw=1.2)
    ax.text(1, -0.3, "AC", ha="center", fontsize=8.5); ax.text(3, -0.3, "BC", ha="center", fontsize=8.5)
    ax.set_xlim(-0.3, 4.3); ax.set_ylim(-0.45, 0.35); ax.axis("off")
    save(fig, "ch05_fig06_midpoint.png")


def fig_dimensions():
    fig, axs = plt.subplots(1, 4, figsize=(6.4, 1.8))
    ax = axs[0]
    ax.add_patch(Polygon([(0, 0), (1, 0), (1, 1), (0, 1)], fc=SOFT, ec=ACC))
    ax.add_patch(Polygon([(0, 1), (0.4, 1.35), (1.4, 1.35), (1, 1)], fc="#D6E3F1", ec=ACC))
    ax.add_patch(Polygon([(1, 0), (1.4, 0.35), (1.4, 1.35), (1, 1)], fc="#C7D9EC", ec=ACC))
    ax.set_title("Solid: 3 dimensions", fontsize=8)
    axs[1].add_patch(Polygon([(0, 0.2), (1.2, 0.2), (1.2, 1.1), (0, 1.1)], fc=SOFT, ec=ACC))
    axs[1].set_title("Surface: 2", fontsize=8)
    axs[2].plot([0, 1.3], [0.6, 0.6], color=ACC, lw=2)
    axs[2].set_title("Line: 1", fontsize=8)
    axs[3].plot([0.65], [0.6], "o", color=ACC, ms=6)
    axs[3].set_title("Point: 0", fontsize=8)
    for a in axs:
        a.set_xlim(-0.2, 1.6); a.set_ylim(-0.1, 1.5); a.set_aspect("equal"); a.axis("off")
    save(fig, "ch05_fig07_dimensions.png")


if __name__ == "__main__":
    fig_lines_through_points(); fig_segment_produced(); fig_fifth_postulate(); fig_equilateral()
    fig_four_points(); fig_midpoint(); fig_dimensions()
