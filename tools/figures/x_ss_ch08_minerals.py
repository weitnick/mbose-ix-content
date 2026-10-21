"""Figures for Class X Social Science, Ch08 (Geography 5): Minerals and Energy Resources."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import ACC, FILLS, GREY, INK, save, tree
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def fig_classification():
    tree("Classification of minerals",
         ["Metallic: ferrous", "Metallic: non-ferrous", "Metallic: precious", "Non-metallic", "Energy minerals"],
         "ss_ch08_fig01_classification.png",
         grand={0: ["Iron ore", "Manganese", "Nickel", "Cobalt"],
                1: ["Copper", "Lead", "Tin", "Bauxite"],
                2: ["Gold", "Silver", "Platinum"],
                3: ["Mica", "Salt, potash", "Sulphur", "Limestone", "Granite, marble"],
                4: ["Coal", "Petroleum", "Natural gas"]},
         width=10.5, child_w=1.95, size=8.0)


def fig_occurrence():
    fig, axs = plt.subplots(1, 4, figsize=(10.5, 2.9))
    # (a) veins and lodes in igneous/metamorphic rock
    ax = axs[0]
    ax.add_patch(Polygon([(0, 0), (4, 0), (4, 3), (0, 3)], closed=True, fc="#D7CFC4", ec=INK, lw=0.7))
    ax.plot([0.6, 1.4, 1.9, 2.6, 3.4], [0.2, 1.0, 1.4, 2.2, 2.9], color="#B7791F", lw=1.6)
    ax.plot([1.6, 2.0, 2.4], [0.1, 0.8, 1.2], color="#B7791F", lw=1.0)
    ax.add_patch(Polygon([(2.6, 0.3), (3.5, 0.6), (3.6, 1.2), (2.9, 1.1)], closed=True, fc="#B7791F", ec=INK, lw=0.6))
    ax.text(0.9, 2.2, "vein", fontsize=8)
    ax.text(3.1, 1.45, "lode", fontsize=8, ha="center")
    ax.set_title("(a) Veins and lodes in\nigneous and metamorphic rocks", fontsize=8.6, color=ACC, fontweight="bold")
    # (b) beds in sedimentary rock
    ax = axs[1]
    cols = ["#E9DDB5", "#3B3B3B", "#E2C9A0", "#CFC2A8", "#3B3B3B", "#E9DDB5"]
    for i, c in enumerate(cols):
        ax.add_patch(Polygon([(0, i * 0.5), (4, i * 0.5), (4, i * 0.5 + 0.5), (0, i * 0.5 + 0.5)], closed=True,
                             fc=c, ec=INK, lw=0.5))
    ax.text(4.1, 0.75, "coal seam", fontsize=7.8, va="center")
    ax.text(4.1, 2.25, "coal seam", fontsize=7.8, va="center")
    ax.set_title("(b) Beds and layers in\nsedimentary rocks", fontsize=8.6, color=ACC, fontweight="bold")
    # (c) residual mass after weathering (bauxite)
    ax = axs[2]
    ax.add_patch(Polygon([(0, 0), (4, 0), (4, 1.6), (0, 1.6)], closed=True, fc="#D7CFC4", ec=INK, lw=0.7))
    ax.add_patch(Polygon([(0, 1.6), (4, 1.6), (4, 2.5), (3, 2.7), (1.5, 2.6), (0, 2.45)], closed=True, fc="#C98B5A",
                         ec=INK, lw=0.7))
    ax.text(2, 2.05, "weathered residue\n(bauxite)", ha="center", va="center", fontsize=7.8)
    ax.text(2, 0.8, "parent rock", ha="center", va="center", fontsize=7.8)
    for x in (0.8, 2.0, 3.2):
        ax.annotate("", xy=(x, 0.15), xytext=(x, 1.3), arrowprops=dict(arrowstyle="-|>", color="#1F78B4", lw=0.8))
    ax.text(2, -0.35, "soluble parts washed away", ha="center", fontsize=7.6, color="#1F78B4")
    ax.set_title("(c) Residue from\ndecomposed surface rocks", fontsize=8.6, color=ACC, fontweight="bold")
    # (d) placer deposits in river sands
    ax = axs[3]
    ax.add_patch(Polygon([(0, 3), (1.3, 1.0), (2.7, 1.0), (4, 3), (4, 0), (0, 0)], closed=True, fc="#D7CFC4", ec=INK,
                         lw=0.7))
    ax.add_patch(Polygon([(1.3, 1.0), (2.7, 1.0), (2.4, 1.35), (1.6, 1.35)], closed=True, fc="#7EC8E3", ec="none"))
    for x, y in [(1.5, 1.08), (1.9, 1.05), (2.3, 1.1), (1.75, 1.15), (2.15, 1.18)]:
        ax.plot([x], [y], "o", ms=3, color="#D4A017", mec=INK, mew=0.3)
    ax.text(2, 0.5, "gold, tin, platinum\nin river sands", ha="center", fontsize=7.8)
    ax.set_title("(d) Placer deposits in\nriver valleys", fontsize=8.6, color=ACC, fontweight="bold")
    for a in axs:
        a.set_xlim(-0.2, 5.0 if a is axs[1] else 4.2)
        a.set_ylim(-0.6, 3.1)
        a.set_aspect("equal")
        a.axis("off")
    fig.suptitle("How minerals occur (a fifth mode: dissolved in ocean water — salt, magnesium, bromine)",
                 fontsize=9.6, fontweight="bold", y=1.04)
    fig.tight_layout()
    save(fig, "ss_ch08_fig02_occurrence.png")


def fig_energy():
    tree("Sources of energy",
         ["Conventional", "Non-conventional"],
         "ss_ch08_fig03_energy.png",
         grand={0: ["Firewood, cattle dung cake", "Coal", "Petroleum", "Natural gas",
                    "Electricity: hydel and thermal"],
                1: ["Nuclear (atomic)", "Solar", "Wind", "Biogas", "Tidal", "Geothermal"]},
         width=8.0, child_w=3.0, size=8.4)


def fig_oil_trap():
    fig, ax = plt.subplots(figsize=(7.5, 3.2))
    import numpy as np
    x = np.linspace(0, 10, 300)

    def layer(base):
        return base + 1.6 * np.exp(-((x - 5) ** 2) / 6.0)

    bands = [(0.0, "#BFB6A8", ""), (0.6, "#E9D9A6", ""), (1.2, "#8C8C8C", "non-porous rock"),
             (1.8, "#E9D9A6", "porous rock (sandstone, limestone)"), (2.4, "#8C8C8C", "non-porous rock")]
    for i, (b, c, lab) in enumerate(bands):
        lo = layer(b)
        hi = layer(b + 0.6)
        ax.fill_between(x, lo, hi, color=c, ec=INK, lw=0.4)
        if lab:
            ax.text(0.2, b + 0.3, lab, fontsize=7.8, va="center")
    lo, hi = layer(1.8), layer(2.4)
    owc, goc = 3.05, 3.72
    ax.fill_between(x, np.maximum(lo, owc), np.minimum(hi, goc), where=hi > owc, color="#3B2F2F", alpha=0.88)
    ax.fill_between(x, np.maximum(lo, goc), hi, where=hi > goc, color="#9AD0EC", alpha=0.95)
    ax.text(8.6, 2.45, "water", fontsize=7.8, color="#1F78B4", ha="center")
    ax.text(5, 3.42, "oil", color="white", ha="center", fontsize=8.5, fontweight="bold")
    ax.text(5, 3.8, "gas", color=INK, ha="center", va="center", fontsize=7.5, fontweight="bold")
    ax.annotate("crest of the upfold\n(anticline)", xy=(5, 4.62), xytext=(7.9, 5.0), fontsize=8,
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=0.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.4)
    ax.axis("off")
    ax.set_title("Occurrence of petroleum in an anticline", fontsize=10, fontweight="bold", color=ACC)
    save(fig, "ss_ch08_fig04_oil_trap.png")


if __name__ == "__main__":
    fig_classification()
    fig_occurrence()
    fig_energy()
    fig_oil_trap()
