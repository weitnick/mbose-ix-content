"""Figures for Class X Social Science, Ch09 (Geography 6): Agriculture."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import ACC, FILLS, GREY, INK, box, save, tree
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def fig_seasons():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    fig, ax = plt.subplots(figsize=(9.5, 3.0))
    rows = [("Rabi", FILLS[0], [(9, 3, "sown Oct–Dec"), (0, 6, "grows; harvested Apr–Jun")],
             "wheat, barley, peas, gram, mustard"),
            ("Zaid", FILLS[1], [(2, 4, "short summer season")], "watermelon, muskmelon, cucumber, vegetables, fodder"),
            ("Kharif", FILLS[2], [(5, 5, "monsoon sowing;\nharvest Sep–Oct")],
             "paddy, maize, jowar, bajra, tur, moong, urad, cotton, jute, groundnut, soyabean")]
    for r, (name, col, spans, crops) in enumerate(rows):
        y = 2 - r
        for start, length, lab in spans:
            ax.add_patch(FancyBboxPatch((start + 0.05, y - 0.32), length - 0.1, 0.64, boxstyle="round,pad=0.02",
                                        fc=col, ec=INK, lw=0.7))
            ax.text(start + length / 2, y, lab, ha="center", va="center", fontsize=7.8)
        ax.text(-0.25, y, name, ha="right", va="center", fontsize=9.5, fontweight="bold", color=ACC)
        ax.text(12.15, y, crops, ha="left", va="center", fontsize=7.8, color=INK, wrap=True)
    for i, m in enumerate(months):
        ax.text(i + 0.5, 2.62, m, ha="center", fontsize=8.2, color=GREY)
        ax.plot([i, i], [-0.45, 2.45], color="#E3E7EC", lw=0.6, zorder=0)
    ax.plot([12, 12], [-0.45, 2.45], color="#E3E7EC", lw=0.6, zorder=0)
    ax.set_xlim(-1.4, 19.5)
    ax.set_ylim(-0.55, 2.95)
    ax.axis("off")
    ax.set_title("India's three cropping seasons", fontsize=10.5, fontweight="bold", color=ACC)
    save(fig, "ss_ch09_fig01_seasons.png")


def fig_farming():
    tree("Types of farming in India",
         ["Primitive\nsubsistence", "Intensive\nsubsistence", "Commercial", "Plantation"],
         "ss_ch09_fig02_farming.png",
         grand={0: ["slash and burn (jhum)", "small patches", "hoe, dao, digging stick",
                    "family labour"],
                1: ["high population", "small holdings", "heavy inputs", "much labour"],
                2: ["HYV seeds, fertilisers", "insecticides", "crops for sale", "Punjab, Haryana"],
                3: ["one crop, large area", "capital and labour", "tea, coffee, rubber", "linked to industry"]},
         width=10.0, child_w=2.3, size=8.2)


def fig_jhum():
    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    steps = ["1. A patch of forest\nis cleared", "2. The cut vegetation\nis burnt", "3. Ash enriches the soil;\ncrops are sown",
             "4. After a few years\nfertility falls", "5. Farmers shift to a\nnew patch", "6. The old patch rests;\nforest regrows"]
    n = len(steps)
    R = 2.45
    pts = []
    for i, s in enumerate(steps):
        a = math.pi / 2 - i * 2 * math.pi / n
        c = (R * 1.5 * math.cos(a), R * math.sin(a))
        pts.append(c)
        box(ax, c, s, FILLS[i % len(FILLS)], w=2.6, h=0.8, size=8.2)
    for i in range(n):
        p0, p1 = pts[i], pts[(i + 1) % n]
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        d = math.hypot(dx, dy)
        sx, sy = p0[0] + dx * 0.36, p0[1] + dy * 0.36
        ex, ey = p0[0] + dx * 0.64, p0[1] + dy * 0.64
        ax.add_patch(FancyArrowPatch((sx, sy), (ex, ey), arrowstyle="-|>", mutation_scale=12, color=INK, lw=1.1))
    ax.text(0, 0.15, "Jhum cycle", ha="center", va="center", fontsize=11, fontweight="bold", color=ACC)
    ax.text(0, -0.3, "(slash and burn)", ha="center", va="center", fontsize=8.5, color=GREY)
    ax.set_xlim(-5.0, 5.0)
    ax.set_ylim(-3.0, 3.0)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "ss_ch09_fig03_jhum.png")


if __name__ == "__main__":
    fig_seasons()
    fig_farming()
    fig_jhum()
