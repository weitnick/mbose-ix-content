"""Figures for Class X Social Science, Ch11 (Geography 8): Lifelines of National Economy."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import ACC, FILLS, GREY, HI, INK, flow, save, tree
import matplotlib.pyplot as plt


def fig_means():
    tree("Lifelines of the national economy",
         ["Land transport", "Water transport", "Air transport", "Communication", "Trade and tourism"],
         "ss_ch11_fig01_means.png",
         grand={0: ["Roadways", "Railways", "Pipelines"],
                1: ["Inland waterways", "Sea ports"],
                2: ["Air India", "Pawan Hans"],
                3: ["Post", "Telecom", "Radio, TV, press", "Films"],
                4: ["Exports", "Imports", "Tourism"]},
         width=10.5, child_w=1.95, size=8.0)


def fig_roads():
    flow(["Golden\nQuadrilateral\n(NHAI)",
          "National\nHighways\n(CPWD)",
          "State\nHighways\n(State PWD)",
          "District\nroads\n(Zila Parishad)",
          "Other (rural)\nroads\n(PMGSY)",
          "Border\nroads\n(BRO, 1960)"],
         "ss_ch11_fig02_roads.png", width=10.5, w=1.62, h=1.2, size=7.8,
         title="Six classes of roads in India (and who builds them)")


def fig_gq():
    fig, ax = plt.subplots(figsize=(6.2, 6.6))
    city = {"Delhi": (77.2, 28.6), "Kolkata": (88.4, 22.6), "Chennai": (80.3, 13.1), "Mumbai": (72.9, 19.1),
            "Srinagar": (74.8, 34.1), "Kanyakumari": (77.5, 8.1), "Silchar": (92.8, 24.8), "Porbandar": (69.6, 21.6)}
    gq = ["Delhi", "Kolkata", "Chennai", "Mumbai", "Delhi"]
    xs = [city[c][0] for c in gq]
    ys = [city[c][1] for c in gq]
    ax.plot(xs, ys, color=HI, lw=4.0, solid_capstyle="round", zorder=2, label="Golden Quadrilateral")
    ns = [(74.8, 34.1), (77.2, 28.6), (78.2, 26.2), (79.1, 21.1), (78.5, 17.4), (77.6, 13.0), (77.5, 8.1)]
    ax.plot([p[0] for p in ns], [p[1] for p in ns], color=ACC, lw=2.2, ls="--", zorder=3,
            label="North–South corridor")
    ew = [(69.6, 21.6), (70.8, 22.3), (73.7, 24.6), (75.8, 25.2), (78.6, 25.4), (80.3, 26.4), (83.4, 26.8),
          (85.4, 26.1), (88.4, 26.7), (91.7, 26.1), (92.8, 24.8)]
    ax.plot([p[0] for p in ew], [p[1] for p in ew], color="#2F7D32", lw=2.2, ls="-.", zorder=3,
            label="East–West corridor")
    for name, (x, y) in city.items():
        ax.plot([x], [y], "o", ms=6, color=INK, zorder=4)
        dx, ha = (0.5, "left")
        if name in ("Mumbai", "Porbandar"):
            dx, ha = (-0.5, "right")
        ax.text(x + dx, y + 0.35, name, fontsize=8.6, ha=ha, zorder=5)
    ax.legend(loc="lower right", fontsize=8, frameon=False)
    ax.text(68.0, 9.0, "Schematic only: not to scale;\npositions approximate.", fontsize=7.4, color=GREY, ha="left")
    ax.set_xlim(67.5, 95)
    ax.set_ylim(6.8, 35.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("The Golden Quadrilateral and the two corridors", fontsize=10.5, fontweight="bold", color=ACC)
    save(fig, "ss_ch11_fig03_gq.png")


if __name__ == "__main__":
    fig_means()
    fig_roads()
    fig_gq()
