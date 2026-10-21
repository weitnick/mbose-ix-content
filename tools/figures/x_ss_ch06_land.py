"""Figures for Class X Social Science, Ch06 (Geography 2): Land Resources (land use, degradation, soils)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import ACC, FILLS, GREY, INK, save, tree
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon


def fig_relief():
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    vals = [43, 30, 27]
    labels = ["Plains 43%\nagriculture and industry", "Mountains 30%\nperennial rivers, tourism,\necology",
              "Plateaus 27%\nminerals, fossil fuels,\nforests"]
    ax.pie(vals, labels=labels, colors=[FILLS[2], FILLS[0], FILLS[1]], startangle=90, counterclock=False,
           wedgeprops=dict(edgecolor=INK, linewidth=0.8), textprops=dict(fontsize=8.6), labeldistance=1.12)
    ax.set_title("India's land under different relief features", fontsize=10, fontweight="bold", color=ACC)
    ax.set_aspect("equal")
    save(fig, "ss_ch06_fig01_relief.png")


def fig_land_use():
    tree("Land utilisation in India",
         ["Forests", "Land not available\nfor cultivation", "Other uncultivated\nland (excl. fallow)",
          "Fallow lands", "Net sown area"],
         "ss_ch06_fig02_land_use.png",
         grand={1: ["Barren, waste land", "Non-farm uses"],
                2: ["Permanent pastures", "Tree crops, groves", "Culturable waste"],
                3: ["Current (≤ 1 yr)", "Other (1–5 yrs)"],
                4: ["Sown in a year"]},
         width=10.5, child_w=1.95, size=8.0)


def _panel_title(ax, t):
    ax.set_title(t, fontsize=9.2, fontweight="bold", color=ACC, pad=4)


def fig_conservation():
    fig, axs = plt.subplots(1, 4, figsize=(10.5, 3.0))
    # (a) terrace farming: a stepped slope with crops on each step
    ax = axs[0]
    xs, ys = [0], [0]
    for i in range(5):
        xs += [xs[-1] + 0.25, xs[-1] + 1.0]
        ys += [ys[-1] + 0.6, ys[-1] + 0.6]
    poly = list(zip(xs, ys)) + [(xs[-1], 0)]
    ax.add_patch(Polygon(poly, closed=True, fc="#C9A26B", ec=INK, lw=0.8))
    for i in range(5):
        x0 = 0.25 + i * 1.0
        y = 0.6 * (i + 1)
        for k in range(4):
            ax.plot([x0 + 0.12 + k * 0.17] * 2, [y, y + 0.18], color="#2F7D32", lw=1.6)
    ax.set_xlim(-0.2, 5.4)
    ax.set_ylim(-0.2, 3.6)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_title(ax, "(a) Terrace farming")
    # (b) contour ploughing: furrows follow the contours of a hill seen from above
    ax = axs[1]
    t = np.linspace(0, 2 * np.pi, 200)
    for r in np.arange(0.35, 2.2, 0.22):
        ax.plot(r * 1.15 * np.cos(t), r * np.sin(t), color="#8B5A2B", lw=1.0)
    ax.plot([0], [0], "^", ms=7, color=INK)
    ax.text(0, -2.4, "a hill seen from above (▲ = top):\nfurrows follow the contours", ha="center", va="top", fontsize=8)
    ax.set_xlim(-2.8, 3.1)
    ax.set_ylim(-3.5, 2.3)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_title(ax, "(b) Contour ploughing")
    # (c) strip cropping: alternate strips of crop and grass
    ax = axs[2]
    for i in range(6):
        fc = "#E9D58A" if i % 2 == 0 else "#9CCB86"
        ax.add_patch(Polygon([(0, i * 0.6), (4, i * 0.6 + 0.35), (4, i * 0.6 + 0.95), (0, i * 0.6 + 0.6)],
                             closed=True, fc=fc, ec=INK, lw=0.5))
    ax.text(2, -0.45, "crop strips with grass strips\nbetween them", ha="center", fontsize=8, va="top")
    ax.text(4.15, 0.55, "crop", fontsize=7.5, va="center")
    ax.text(4.15, 1.15, "grass", fontsize=7.5, va="center")
    ax.set_xlim(-0.2, 4.9)
    ax.set_ylim(-1.3, 4.0)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_title(ax, "(c) Strip cropping")
    # (d) shelter belt: rows of trees break the wind
    ax = axs[3]
    for row in range(3):
        for k in range(5):
            cx, cy = 2.0 + row * 0.45, 0.4 + k * 0.7
            ax.add_patch(plt.Circle((cx, cy), 0.22, fc="#2F7D32", ec=INK, lw=0.5))
    for y in (0.7, 1.75, 2.8):
        ax.add_patch(FancyArrowPatch((0.0, y), (1.55, y), arrowstyle="-|>", mutation_scale=11, color=ACC, lw=1.3))
    ax.text(0.75, 3.45, "wind", ha="center", fontsize=8, color=ACC)
    ax.add_patch(Polygon([(3.4, 0.1), (4.6, 0.1), (4.6, 3.3), (3.4, 3.3)], closed=True, fc="#F3E3B5", ec="none"))
    ax.text(4.0, 1.7, "protected\nfield", ha="center", va="center", fontsize=7.8)
    ax.text(2.45, -0.45, "rows of trees\n(shelter belt)", ha="center", fontsize=8, va="top")
    ax.set_xlim(-0.1, 4.8)
    ax.set_ylim(-1.3, 3.8)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel_title(ax, "(d) Shelter belts")
    fig.suptitle("Methods of soil conservation", fontsize=10.5, fontweight="bold", color=INK, y=1.02)
    fig.tight_layout()
    save(fig, "ss_ch06_fig03_soil_conservation.png")


if __name__ == "__main__":
    fig_relief()
    fig_land_use()
    fig_conservation()
