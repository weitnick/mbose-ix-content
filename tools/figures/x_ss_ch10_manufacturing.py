"""Figures for Class X Social Science, Ch10 (Geography 7): Manufacturing Industries."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import ACC, FILLS, GREY, INK, arrow, box, flow, save, tree
import matplotlib.pyplot as plt


def fig_classification():
    tree("Classification of industries",
         ["Source of\nraw material", "Main role", "Capital\ninvestment", "Ownership", "Bulk and weight"],
         "ss_ch10_fig01_classification.png",
         grand={0: ["Agro (cotton, sugar)", "Mineral (steel, cement)"],
                1: ["Basic (iron, steel)", "Consumer (sugar, fans)"],
                2: ["Small-scale", "Large-scale"],
                3: ["Public (SAIL)", "Private (TISCO)", "Joint (Oil India)", "Co-operative (sugar)"],
                4: ["Heavy (iron, steel)", "Light (electrical)"]},
         width=11.0, child_w=2.1, size=8.0)


def fig_location():
    fig, ax = plt.subplots(figsize=(9.5, 3.8))
    factors = ["Raw material", "Labour", "Capital", "Power", "Market"]
    for i, f in enumerate(factors):
        y = 3.2 - i * 0.8
        box(ax, (0.9, y), f, FILLS[i % len(FILLS)], w=1.7, h=0.55, size=8.6)
        arrow(ax, (1.78, y), (3.22, 1.6), color=GREY, lw=0.9)
    box(ax, (4.3, 1.6), "Industry is located\nwhere costs\nare lowest", FILLS[0], w=2.1, h=1.05, size=8.4, bold=True)
    arrow(ax, (5.38, 1.6), (6.05, 1.6))
    box(ax, (7.0, 1.6), "Urbanisation\nfollows", FILLS[2], w=1.8, h=0.8, size=8.6)
    arrow(ax, (7.92, 1.6), (8.8, 1.6))
    box(ax, (9.95, 1.6), "Agglomeration\neconomies:\nindustries cluster\nin cities", FILLS[1], w=2.2, h=1.25, size=8.4)
    ax.text(7.0, 0.55, "cities give markets, banking, insurance,\ntransport, labour and advice", ha="center", fontsize=8,
            color=GREY)
    ax.set_xlim(-0.1, 11.2)
    ax.set_ylim(-0.45, 3.75)
    ax.axis("off")
    ax.set_title("What decides where an industry is located", fontsize=10.5, fontweight="bold", color=ACC)
    save(fig, "ss_ch10_fig02_location.png")


def fig_steel():
    flow(["Iron ore, coking\ncoal, limestone\n(4 : 2 : 1)",
          "Blast furnace:\nsmelting",
          "Pig iron",
          "Steel making:\nremove impurities;\nadd manganese,\nnickel, chromium",
          "Rolling, pressing,\ncasting, forging",
          "Steel"],
         "ss_ch10_fig03_steel.png", width=10.5, w=1.72, h=1.25, size=7.6,
         title="Making iron and steel: the process")


if __name__ == "__main__":
    fig_classification()
    fig_location()
    fig_steel()
