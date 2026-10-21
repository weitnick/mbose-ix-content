"""Figures for Class XII Chemistry Chapter 8, Aldehydes, Ketones and Carboxylic Acids.
Run: python xii_chem_ch08_carbonyl.py
"""
from xii_chem_common import *


def fig01_carbonyl():
    fig, ax = canvas(10.0, 3.4, (0, 20), (0, 6.8))
    # planar carbonyl group
    c, o = (3.2, 3.2), (5.6, 3.2)
    atoms = {"C": (c[0], c[1], "C"), "O": (o[0], o[1], "O"), "R": (1.9, 5.0, "R"), "R2": (1.9, 1.4, "R′ / H")}
    draw(ax, atoms, [("C", "O", 2), ("C", "R", 1), ("C", "R2", 1)], fs=12)
    ax.text(c[0] + 0.1, c[1] + 0.75, "δ+", color=RED, fontsize=11, ha="center")
    ax.text(o[0] + 0.1, o[1] + 0.75, "δ−", color=BLUE, fontsize=11, ha="center")
    ax.text(3.9, 4.25, "120°", fontsize=8.5, color=GREY)
    ax.text(3.6, 0.3, "sp² carbon; the three σ bonds lie in one plane\n(trigonal planar), π bond above and below", ha="center",
            fontsize=8.5)
    # resonance
    x0 = 11.0
    draw(ax, {"C": (x0, 3.2, "C"), "O": (x0 + 2.2, 3.2, "O")}, [("C", "O", 2)], fs=12)
    ax.text(x0 + 3.5, 3.2, "↔", fontsize=18, ha="center", va="center")
    draw(ax, {"C": (x0 + 4.8, 3.2, "C⁺"), "O": (x0 + 7.0, 3.2, "O⁻")}, [("C", "O", 1)], fs=12)
    ax.text(x0 + 3.5, 1.4, "Polarity: O is more electronegative, so the carbonyl\ncarbon is electrophilic (attacked by nucleophiles)\n"
            "and the oxygen is nucleophilic (attacked by H⁺)", ha="center", fontsize=8.5)
    ax.set_title("The carbonyl group: planar and polar", fontsize=11)
    save(fig, "chem_ch08_fig01_carbonyl.png")


def fig02_nucleophilic_addition():
    fig, ax = canvas(11.0, 3.4, (0, 22), (0, 6.8))
    # step 1: planar carbonyl + Nu-
    draw(ax, {"C": (3.0, 3.4, "C"), "O": (5.0, 3.4, "O"), "a": (1.8, 4.9, "R"), "b": (1.8, 1.9, "R′")},
         [("C", "O", 2), ("C", "a", 1), ("C", "b", 1)], fs=12)
    ax.text(3.0, 6.0, "Nu⁻", color=RED, fontsize=12, ha="center")
    arrow(ax, (3.0, 5.6), (3.0, 3.95), color=RED)
    ax.text(3.2, 0.5, "planar (sp²)", ha="center", fontsize=8.5, color=GREY)
    arrow(ax, (6.1, 3.4), (8.6, 3.4), text="slow")
    # tetrahedral intermediate
    draw(ax, {"C": (11.0, 3.4, "C"), "O": (13.0, 3.4, "O⁻"), "a": (9.8, 4.9, "R"), "b": (9.8, 1.9, "R′"),
              "N": (11.0, 5.3, "Nu")}, [("C", "O", 1), ("C", "a", 1), ("C", "b", "wedge"), ("C", "N", 1)], fs=12)
    ax.text(11.2, 0.5, "tetrahedral alkoxide\nintermediate (sp³)", ha="center", fontsize=8.5, color=GREY)
    arrow(ax, (14.1, 3.4), (16.6, 3.4), text="H⁺, fast")
    draw(ax, {"C": (19.0, 3.4, "C"), "O": (21.0, 3.4, "OH"), "a": (17.8, 4.9, "R"), "b": (17.8, 1.9, "R′"),
              "N": (19.0, 5.3, "Nu")}, [("C", "O", 1), ("C", "a", 1), ("C", "b", "wedge"), ("C", "N", 1)], fs=12)
    ax.text(19.2, 0.5, "addition product", ha="center", fontsize=8.5, color=GREY)
    ax.set_title("Mechanism of nucleophilic addition to the carbonyl group", fontsize=11)
    save(fig, "chem_ch08_fig02_nucleophilic_addition.png")


def fig03_carboxylate():
    fig, ax = canvas(10.0, 3.2, (0, 20), (0, 6.4))
    for x, (b1, b2, l1, l2) in zip([3.0, 10.0], [(2, 1, "O", "O⁻"), (1, 2, "O⁻", "O")]):
        draw(ax, {"C": (x, 3.0, "C"), "R": (x - 2.0, 3.0, "R"), "O1": (x + 1.3, 4.6, l1), "O2": (x + 1.3, 1.4, l2)},
             [("C", "R", 1), ("C", "O1", b1), ("C", "O2", b2)], fs=12)
    ax.text(7.0, 3.0, "↔", fontsize=18, ha="center", va="center")
    ax.text(16.0, 3.1, "Two equivalent structures:\nthe charge is shared equally\nby two electronegative O atoms,\n"
            "so RCOO⁻ is more stable than\nphenoxide (charge partly on\nless electronegative C atoms)", ha="center",
            va="center", fontsize=8.5)
    ax.set_title("Resonance in the carboxylate ion", fontsize=11)
    save(fig, "chem_ch08_fig03_carboxylate.png")


if __name__ == "__main__":
    fig01_carbonyl()
    fig02_nucleophilic_addition()
    fig03_carboxylate()
