"""Figures for Class X Social Science, Ch07 (Geography 3): Water Resources."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import ACC, FILLS, GREY, INK, save, table_fig
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle


def fig_water_on_earth():
    fig, ax = plt.subplots(figsize=(9.0, 2.6))
    # bar 1: all water
    parts = [(96.5, "Oceans 96.5%", FILLS[0]), (2.5, "Fresh water\n2.5%", FILLS[2]), (1.0, "", FILLS[5])]
    x = 0
    for w, t, c in parts:
        ax.add_patch(Rectangle((x, 1.4), w, 0.6, fc=c, ec=INK, lw=0.7))
        if t and w > 10:
            ax.text(x + w / 2, 1.7, t, ha="center", va="center", fontsize=9)
        x += w
    ax.text(97.75, 2.25, "Fresh water 2.5%", ha="center", fontsize=8.5)
    ax.text(-1.5, 1.7, "All water\non Earth", ha="right", va="center", fontsize=9, fontweight="bold")
    # bar 2: the fresh water, enlarged
    parts = [(70, "Ice sheets and glaciers about 70%", "#E8F4FB"), (29, "Groundwater about 30%", FILLS[1]),
             (1, "", FILLS[0])]
    x = 0
    for w, t, c in parts:
        ax.add_patch(Rectangle((x, 0.2), w, 0.6, fc=c, ec=INK, lw=0.7))
        if t:
            ax.text(x + w / 2, 0.5, t, ha="center", va="center", fontsize=9)
        x += w
    ax.text(-1.5, 0.5, "The fresh\nwater only", ha="right", va="center", fontsize=9, fontweight="bold")
    ax.add_patch(FancyArrowPatch((97.2, 1.38), (60, 0.83), arrowstyle="-|>", mutation_scale=10, color=GREY,
                                 connectionstyle="arc3,rad=-0.15"))
    ax.text(100.5, 0.5, "rivers, lakes:\na tiny share", ha="left", va="center", fontsize=8, color=GREY)
    ax.set_xlim(-14, 112)
    ax.set_ylim(0.0, 2.5)
    ax.axis("off")
    ax.set_title("Where the Earth's water is", fontsize=10.5, fontweight="bold", color=ACC)
    save(fig, "ss_ch07_fig01_water_on_earth.png")


def fig_projects():
    rows = [["Irrigation for crops in the dry season", "Poor sediment flow; silt piles up in the reservoir"],
            ["Hydroelectricity for industries and homes", "Rockier stream beds; poorer habitats for aquatic life"],
            ["Water supply for homes and industry", "Fish cannot migrate upstream to spawn"],
            ["Flood control", "Submerged forests and soil decompose"],
            ["Inland navigation and fish breeding", "Large-scale displacement; loss of land and livelihood"],
            ["Recreation and tourism", "Inter-state disputes; salinisation; floods when water is released"]]
    table_fig(["Advantages (uses)", "Disadvantages (problems)"], rows, "ss_ch07_fig02_projects.png",
              col_w=[5.2, 7.0], title="Multipurpose river projects: a comparison", size=8.4)


def fig_bamboo_drip():
    fig, ax = plt.subplots(figsize=(9.0, 3.8))
    # hill slope
    ax.add_patch(Polygon([(0, 0), (0, 3.6), (1.4, 3.6), (9.6, 0.35), (9.6, 0)], closed=True, fc="#D9C7A3",
                         ec=INK, lw=0.8))
    # spring on the hilltop
    ax.add_patch(plt.Circle((0.7, 3.75), 0.22, fc="#7EC8E3", ec=INK, lw=0.7))
    ax.text(0.7, 4.15, "perennial spring\non the hilltop", ha="center", fontsize=8.2)

    def bamboo(p0, p1, lw=5.0):
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="#6B8E23", lw=lw, solid_capstyle="round", zorder=4)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="#C5D86D", lw=lw * 0.35, zorder=5)

    # main channel down the slope, carried on supports
    main = [(0.95, 3.75), (3.2, 3.15), (5.6, 2.3), (6.9, 1.78)]
    for a, b in zip(main, main[1:]):
        bamboo(a, b)
    for x, y in main[1:]:
        ax.plot([x, x], [y, y - 0.55], color="#6B4F2A", lw=1.4, zorder=3)
    # branch pipes to the plants
    def ground(x):
        return 3.6 - (3.25 / 8.2) * (x - 1.4)

    for px in (7.7, 8.4, 9.1):
        g = ground(px)
        bamboo((6.9, 1.78), (px - 0.15, g + 0.45), lw=3.0)
        ax.plot([px - 0.15, px - 0.15], [g + 0.4, g + 0.08], ls=(0, (1, 2)), color="#1F78B4", lw=1.6, zorder=6)
        ax.plot([px, px], [g, g + 0.5], color="#2F7D32", lw=1.8, zorder=6)
        for dy, sx in ((0.22, 1), (0.36, -1), (0.48, 1)):
            ax.plot([px, px + sx * 0.16], [g + dy, g + dy + 0.1], color="#2F7D32", lw=2.2, zorder=6)
    ax.text(2.0, 2.65, "bamboo pipes carry water downhill by gravity", fontsize=8.2, rotation=-14, color=INK)
    ax.text(5.0, 1.15, "channel sections divide\nthe water into branches", fontsize=8.0, ha="center")
    ax.text(8.3, 2.0, "water falls as 20–80 drops\na minute near the roots", fontsize=8.0, ha="center")
    ax.annotate("", xy=(8.3, 1.25), xytext=(8.3, 1.75), arrowprops=dict(arrowstyle="-|>", color=GREY, lw=0.9))
    ax.text(0.3, 0.35, "about 18–20 litres a minute enter at the top", fontsize=8.0, color=ACC)
    ax.set_xlim(-0.1, 9.7)
    ax.set_ylim(-0.05, 4.6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Bamboo drip irrigation in Meghalaya", fontsize=10.5, fontweight="bold", color=ACC)
    save(fig, "ss_ch07_fig03_bamboo_drip.png")


if __name__ == "__main__":
    fig_water_on_earth()
    fig_projects()
    fig_bamboo_drip()
