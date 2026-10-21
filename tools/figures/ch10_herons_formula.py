"""Figures for Class IX Mathematics, Chapter 10: Heron's Formula (2026 rationalised book)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "CLASS IX Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, MUTED, GREEN = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#5D6B7A", "#DCEFD8"
plt.rcParams.update({"font.size": 9, "mathtext.fontset": "cm"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def tri_from_sides(a, b, c):
    """Triangle with BC = a on the x-axis, CA = b, AB = c. Returns A, B, C."""
    B, C = (0.0, 0.0), (a, 0.0)
    x = (a * a + c * c - b * b) / (2 * a)
    y = math.sqrt(max(c * c - x * x, 0))
    return (x, y), B, C


def lab(ax, p, t, dx=0.0, dy=0.0, color=INK, fs=9, bold=True):
    ax.text(p[0] + dx, p[1] + dy, t, ha="center", va="center", fontsize=fs, weight="bold" if bold else "normal", color=color)


def side_label(ax, p, q, t, off=0.12, color=INK, fs=8.5, centre=None):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    L = math.hypot(q[0] - p[0], q[1] - p[1])
    nx, ny = -(q[1] - p[1]) / L, (q[0] - p[0]) / L
    if centre is not None and (mx + nx - centre[0]) ** 2 + (my + ny - centre[1]) ** 2 < (mx - nx - centre[0]) ** 2 + (my - ny - centre[1]) ** 2:
        nx, ny = -nx, -ny
    ax.text(mx + nx * off, my + ny * off, t, ha="center", va="center", fontsize=fs, color=color)


def right(ax, v, d1, d2, s):
    u = (v[0] + d1[0] * s, v[1] + d1[1] * s); w = (v[0] + d2[0] * s, v[1] + d2[1] * s)
    c = (u[0] + w[0] - v[0], u[1] + w[1] - v[1])
    ax.plot([u[0], c[0], w[0]], [u[1], c[1], w[1]], color=HI, lw=1)


def finish(ax, title=None, pad=0.3):
    ax.set_aspect("equal"); ax.axis("off")
    ax.autoscale_view()
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    ax.set_xlim(x0 - pad, x1 + pad); ax.set_ylim(y0 - pad, y1 + pad)
    if title:
        ax.set_title(title, fontsize=8.5, color=MUTED)


def draw_tri(ax, a, b, c, scale, names=("A", "B", "C"), labels=None, fill=SOFT):
    A, B, C = tri_from_sides(a * scale, b * scale, c * scale)
    ax.add_patch(Polygon([A, B, C], closed=True, fc=fill, ec=ACC, lw=1.4))
    g = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
    for p, t in zip((A, B, C), names):
        dx, dy = p[0] - g[0], p[1] - g[1]; L = math.hypot(dx, dy)
        lab(ax, (p[0] + 0.16 * dx / L, p[1] + 0.16 * dy / L), t)
    if labels:
        side_label(ax, B, C, labels[0], centre=g); side_label(ax, C, A, labels[1], centre=g); side_label(ax, A, B, labels[2], centre=g)
    return A, B, C


def fig_half_base_height():
    fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.2))
    ax = axs[0]
    A, B, C = (0, 1.2), (0, 0), (1.6, 0)
    ax.add_patch(Polygon([A, B, C], closed=True, fc=SOFT, ec=ACC, lw=1.4)); right(ax, B, (1, 0), (0, 1), 0.12)
    lab(ax, A, "A", dy=0.14); lab(ax, B, "B", dx=-0.12, dy=-0.1); lab(ax, C, "C", dx=0.12, dy=-0.1)
    side_label(ax, B, C, "base 16 cm", off=0.15, centre=(0.5, 0.4)); side_label(ax, B, A, "height\n12 cm", off=0.32, centre=(0.5, 0.4))
    finish(ax, "Right triangle: $\\frac{1}{2} \\times 16 \\times 12 = 96$ cm²")
    ax = axs[1]
    s = 1.8; A, B, C = (s / 2, s * math.sqrt(3) / 2), (0, 0), (s, 0); D = (s / 2, 0)
    ax.add_patch(Polygon([A, B, C], closed=True, fc=SOFT, ec=ACC, lw=1.4))
    ax.plot([A[0], D[0]], [A[1], D[1]], color=HI, lw=1.2, ls="--"); right(ax, D, (1, 0), (0, 1), 0.1)
    lab(ax, A, "A", dy=0.14); lab(ax, B, "B", dx=-0.12, dy=-0.1); lab(ax, C, "C", dx=0.12, dy=-0.1); lab(ax, D, "D", dy=-0.14)
    side_label(ax, A, B, "10", off=0.12, centre=(s / 2, 0.5)); side_label(ax, A, C, "10", off=0.12, centre=(s / 2, 0.5)); side_label(ax, B, D, "5", off=-0.12)
    finish(ax, "Equilateral: height $5\\sqrt{3}$ cm")
    ax = axs[2]
    A, B, C = (0.8, 0.6), (0, 0), (1.6, 0); D = (0.8, 0)
    ax.add_patch(Polygon([A, B, C], closed=True, fc=SOFT, ec=ACC, lw=1.4))
    ax.plot([A[0], D[0]], [A[1], D[1]], color=HI, lw=1.2, ls="--"); right(ax, D, (1, 0), (0, 1), 0.08)
    lab(ax, A, "A", dy=0.14); lab(ax, B, "B", dx=-0.12, dy=-0.1); lab(ax, C, "C", dx=0.12, dy=-0.1); lab(ax, D, "D", dy=-0.13)
    side_label(ax, A, B, "5", off=0.12, centre=(0.8, 0.2)); side_label(ax, A, C, "5", off=0.12, centre=(0.8, 0.2)); side_label(ax, B, D, "4", off=-0.12); side_label(ax, D, C, "4", off=-0.12)
    finish(ax, "Isosceles: height 3 cm")
    save(fig, "ch10_fig01_half_base_height.png")


def fig_heron_general():
    fig, axs = plt.subplots(1, 2, figsize=(5.6, 2.2))
    ax = axs[0]
    draw_tri(ax, 3.0, 2.2, 1.8, 0.7, labels=("$a$", "$b$", "$c$"))
    finish(ax, "$s = \\frac{a + b + c}{2}$")
    ax = axs[1]
    draw_tri(ax, 32, 24, 40, 0.06, labels=("32 m", "24 m", "40 m"), fill=GREEN)
    finish(ax, "Triangular park: area 384 m²")
    save(fig, "ch10_fig02_herons_formula.png")


def fig_examples():
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.4))
    ax = axs[0]
    draw_tri(ax, 13, 11, 8, 0.12, labels=("13 cm", "11 cm", "8 cm"))
    finish(ax, "Example 1: perimeter 32 cm")
    ax = axs[1]
    A, B, C = draw_tri(ax, 120, 80, 50, 0.02, labels=("120 m", "80 m", "50 m"), fill=GREEN)
    gx = B[0] + 0.3; ax.plot([gx, gx + 3 * 0.02 * 3], [0, 0], color="white", lw=3.5)
    ax.text(gx + 0.1, -0.3, "gate", fontsize=7, color=HI, ha="center")
    finish(ax, "Example 2: Dhania's park")
    ax = axs[2]
    draw_tri(ax, 140, 100, 60, 0.012, labels=("140 m", "100 m", "60 m"), fill=GREEN)
    finish(ax, "Example 3: sides 3 : 5 : 7")
    save(fig, "ch10_fig03_examples.png")


def fig_exercise():
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.4))
    ax = axs[0]
    s = 1.6; A, B, C = (s / 2, s * math.sqrt(3) / 2), (0, 0), (s, 0)
    ax.add_patch(Polygon([A, B, C], closed=True, fc="#FBE3E0", ec="#9B2C2C", lw=2.2))
    ax.text(s / 2, 0.42, "SCHOOL\nAHEAD", ha="center", va="center", fontsize=7.5, weight="bold", color=INK)
    side_label(ax, B, C, "$a$", off=-0.14)
    finish(ax, "Q1: equilateral sign board")
    ax = axs[1]
    draw_tri(ax, 122, 22, 120, 0.018, names=("", "", ""), labels=("122 m", "22 m", "120 m"), fill="#FFF3D6")
    finish(ax, "Q2: flyover wall")
    ax = axs[2]
    draw_tri(ax, 15, 11, 6, 0.14, names=("", "", ""), labels=("15 m", "11 m", "6 m"), fill="#E3F1DF")
    finish(ax, "Q3: slide wall")
    save(fig, "ch10_fig04_exercise_10_1.png")


if __name__ == "__main__":
    fig_half_base_height(); fig_heron_general(); fig_examples(); fig_exercise()
