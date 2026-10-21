"""Figures for Class X Social Science, Ch12 (Geography 9): Meghalaya: An Overview."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import ACC, FILLS, GREY, INK, save, tree
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon


def fig_rain():
    fig, ax = plt.subplots(figsize=(9.6, 3.9))
    # relief: Bangladesh plains (left/south) -> steep southern escarpment -> plateau -> gentle slope to Brahmaputra (right/north)
    xs = [0, 3.2, 3.6, 4.4, 5.0, 6.2, 7.4, 8.6, 10.2, 10.2, 0]
    ys = [0.15, 0.2, 0.9, 1.9, 2.15, 2.2, 2.05, 1.4, 0.35, 0, 0]
    ax.add_patch(Polygon(list(zip(xs, ys)), closed=True, fc="#C9D9A8", ec=INK, lw=0.8))
    # moist monsoon winds from the Bay of Bengal rising over the escarpment
    for y0 in (0.55, 0.9):
        ax.add_patch(FancyArrowPatch((0.2, y0), (3.0, y0 + 0.1), arrowstyle="-|>", mutation_scale=12, color=ACC, lw=1.4))
    ax.add_patch(FancyArrowPatch((3.05, 1.1), (4.05, 2.75), arrowstyle="-|>", mutation_scale=12, color=ACC, lw=1.4,
                                 connectionstyle="arc3,rad=-0.2"))
    # clouds and rain over the windward slope
    for cx in (3.7, 4.3, 4.9):
        for dx, dy, r in ((0, 0, 0.32), (0.28, 0.1, 0.26), (-0.26, 0.08, 0.24)):
            ax.add_patch(plt.Circle((cx + dx, 3.1 + dy), r, fc="#B9C4CF", ec="none"))
    for x in np.linspace(3.3, 5.2, 10):
        ax.plot([x, x - 0.08], [2.75, 2.35], color="#1F78B4", lw=1.0)
    # drier lee side
    ax.add_patch(FancyArrowPatch((5.6, 2.95), (8.6, 2.0), arrowstyle="-|>", mutation_scale=12, color="#B7791F", lw=1.3,
                                 connectionstyle="arc3,rad=-0.15"))
    ax.text(1.5, 1.25, "moist south-west monsoon\nwinds from the Bay of Bengal", ha="center", fontsize=8.2, color=ACC)
    ax.text(1.6, 0.28, "Bangladesh plains (south)", ha="center", va="bottom", fontsize=7.8, color=INK)
    ax.text(4.25, 3.65, "air rises, cools and condenses:\nvery heavy rain at Sohra and Mawsynram", ha="center",
            fontsize=8.2, color=INK, fontweight="bold")
    ax.text(2.55, 1.75, "steep southern\nescarpment", ha="center", fontsize=7.8, rotation=0)
    ax.plot([4.55], [2.0], "v", ms=6, color=INK)
    ax.text(4.95, 1.75, "Sohra", ha="left", fontsize=8)
    ax.plot([6.6], [2.15], "s", ms=5, color=INK)
    ax.text(6.6, 2.35, "Shillong", ha="center", fontsize=8)
    ax.text(8.6, 3.15, "descending air: much\nless rain (rain shadow)", ha="center", fontsize=8, color="#7A5A12")
    ax.text(9.0, 0.45, "Brahmaputra\nvalley (north)", ha="center", fontsize=7.8)
    ax.set_xlim(0, 10.2)
    ax.set_ylim(0, 4.1)
    ax.axis("off")
    ax.set_title("Why Sohra and Mawsynram are so wet (south–north section, not to scale)", fontsize=10,
                 fontweight="bold", color=ACC)
    save(fig, "ss_ch12_fig01_rain.png")


def fig_regions():
    tree("The Meghalaya (Shillong) plateau",
         ["Garo Hills (west)", "Khasi Hills (centre)", "Jaintia Hills (east)"],
         "ss_ch12_fig02_regions.png",
         grand={0: ["lower, rolling hills", "Nokrek peak, 1,412 m", "Tura", "cashew, jute, cotton, rubber"],
                1: ["highest part of the plateau", "Shillong Peak, about 1,960 m", "Shillong (capital)",
                    "Sohra, Mawsynram"],
                2: ["limestone and coal", "Lakadong turmeric", "Jowai", "Krem Liat Prah cave"]},
         width=9.6, child_w=2.8, size=8.4)


def fig_crops():
    tree("Where Meghalaya's crops grow",
         ["Garo Hills", "Khasi Hills", "Jaintia Hills", "Ri-Bhoi"],
         "ss_ch12_fig03_crops.png",
         grand={0: ["rice (jhum and wet)", "cashew nut", "jute and mesta", "cotton", "rubber", "areca nut"],
                1: ["potato", "Khasi mandarin (Sohra)", "maize", "strawberry", "broom grass"],
                2: ["turmeric (Lakadong)", "ginger", "areca nut, betel leaf", "black pepper"],
                3: ["pineapple", "ginger", "rice", "eri silk (Umden)"]},
         width=10.0, child_w=2.3, size=8.2)


if __name__ == "__main__":
    fig_rain()
    fig_regions()
    fig_crops()
