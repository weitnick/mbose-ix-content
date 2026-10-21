"""Figures for Class XII Biology Chapter 4, Principles of Inheritance and Variation.
Run: python xii_bio_ch04_inheritance.py
"""
from xii_bio_common import *


def fig01_dihybrid():
    """F2 Punnett square of RrYy x RrYy (round yellow x round yellow)."""
    gam = ["RY", "Ry", "rY", "ry"]
    colours = {"round yellow": "#F7E3A1", "round green": "#CFE8C8", "wrinkled yellow": "#F3C7A8",
               "wrinkled green": "#B9D3E8"}
    fig, a = canvas(7.4, 6.4, (-1.6, 9.4), (-1.6, 9.0))
    for i, g in enumerate(gam):
        a.text(1 + 2 * i, 8.5, g, ha="center", fontsize=10, weight="bold", color=BLUE)
        a.text(-0.7, 7 - 2 * i, g, ha="center", va="center", fontsize=10, weight="bold", color=RED)
    for r, gr in enumerate(gam):
        for c, gc in enumerate(gam):
            R = "R" in gr or "R" in gc
            Y = "Y" in gr or "Y" in gc
            ph = ("round" if R else "wrinkled") + " " + ("yellow" if Y else "green")
            geno = "".join(sorted(gr[0] + gc[0])) + "".join(sorted(gr[1] + gc[1]))
            a.add_patch(Rectangle((2 * c, 6 - 2 * r), 2, 2, fc=colours[ph], ec=INK, lw=1))
            a.text(2 * c + 1, 7.25 - 2 * r, geno, ha="center", va="center", fontsize=10)
            a.text(2 * c + 1, 6.6 - 2 * r, ph.replace(" ", "\n"), ha="center", va="center", fontsize=7)
    a.text(4, 9.0 - 0.05, "male gametes", ha="center", fontsize=8.5, color=BLUE)
    a.text(-1.45, 4, "female gametes", rotation=90, ha="center", va="center", fontsize=8.5, color=RED)
    a.text(4, -0.6, "F2 ratio: 9 round yellow : 3 round green : 3 wrinkled yellow : 1 wrinkled green", ha="center",
           fontsize=9)
    a.text(4, -1.25, "R = round, r = wrinkled; Y = yellow, y = green", ha="center", fontsize=8.5, color=GREY)
    save(fig, "bio_ch04_fig01_dihybrid_square.png")


def fig02_sex_determination():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    for ax in (a, b):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis("off")
    # humans
    box(a, (0.4, 6.4), 3.6, 1.0, "mother 44 + XX", fc=PALE_RED, ec=RED)
    box(a, (6.0, 6.4), 3.6, 1.0, "father 44 + XY", fc=PALE_BLUE, ec=BLUE)
    box(a, (0.9, 4.0), 2.6, 0.9, "ova: 22 + X", fc=PALE_RED, ec=RED, fs=8.5)
    box(a, (5.0, 4.0), 2.2, 0.9, "22 + X", fc=PALE_BLUE, ec=BLUE, fs=8.5)
    box(a, (7.5, 4.0), 2.2, 0.9, "22 + Y", fc=PALE_BLUE, ec=BLUE, fs=8.5)
    arrow(a, (2.2, 6.4), (2.2, 4.9))
    arrow(a, (7.8, 6.4), (6.1, 4.9))
    arrow(a, (7.8, 6.4), (8.6, 4.9))
    box(a, (0.9, 1.2), 3.6, 1.1, "44 + XX\ndaughter (50%)", fc=PALE_RED, ec=RED, fs=8.5)
    box(a, (5.4, 1.2), 3.6, 1.1, "44 + XY\nson (50%)", fc=PALE_BLUE, ec=BLUE, fs=8.5)
    arrow(a, (2.2, 4.0), (2.7, 2.3))
    arrow(a, (6.1, 4.0), (3.4, 2.3))
    arrow(a, (2.4, 4.0), (6.6, 2.3))
    arrow(a, (8.6, 4.0), (7.6, 2.3))
    a.set_title("(a) Humans: the sperm decides the sex", fontsize=10)
    # honey bee
    box(b, (0.4, 6.4), 3.8, 1.0, "queen (2n = 32)", fc=PALE_RED, ec=RED)
    box(b, (5.8, 6.4), 3.8, 1.0, "drone (n = 16)", fc=PALE_BLUE, ec=BLUE)
    box(b, (0.6, 4.0), 3.4, 0.9, "eggs (n = 16)\nby meiosis", fc=PALE_RED, ec=RED, fs=8)
    box(b, (6.0, 4.0), 3.4, 0.9, "sperms (n = 16)\nby mitosis", fc=PALE_BLUE, ec=BLUE, fs=8)
    arrow(b, (2.3, 6.4), (2.3, 4.9))
    arrow(b, (7.7, 6.4), (7.7, 4.9))
    box(b, (0.3, 1.1), 4.3, 1.3, "unfertilised egg\n→ drone (male, n = 16)\nparthenogenesis", fc=PALE_BLUE, ec=BLUE, fs=8)
    box(b, (5.4, 1.1), 4.3, 1.3, "fertilised egg (2n = 32)\n→ queen or worker\n(female)", fc=PALE_RED, ec=RED, fs=8)
    arrow(b, (2.0, 4.0), (2.0, 2.4))
    arrow(b, (2.8, 4.0), (6.6, 2.4))
    arrow(b, (7.7, 4.0), (7.7, 2.4))
    b.set_title("(b) Honey bee: haplodiploid system", fontsize=10)
    fig.tight_layout()
    save(fig, "bio_ch04_fig02_sex_determination.png")


def fig03_pedigree():
    fig, a = canvas(9.0, 4.6, (0, 18), (0, 9.2))
    # symbol key
    key = [("male", "sq", "white"), ("female", "ci", "white"), ("affected", "sq", INK), ("carrier (recessive)", "half", None)]
    for i, (name, kind, fc) in enumerate(key):
        x, y = 0.8, 8.2 - i * 1.3
        if kind == "sq":
            a.add_patch(Rectangle((x - 0.35, y - 0.35), 0.7, 0.7, fc=fc, ec=INK, lw=1.2))
        elif kind == "ci":
            a.add_patch(Circle((x, y), 0.37, fc=fc, ec=INK, lw=1.2))
        else:
            a.add_patch(Circle((x, y), 0.37, fc="white", ec=INK, lw=1.2))
            a.add_patch(Wedge((x, y), 0.37, 90, 270, fc=INK, ec=INK))
        a.text(x + 0.7, y, name, va="center", fontsize=8.5)
    a.plot([0.4, 1.2], [2.8, 2.8], color=INK, lw=1.2)
    a.text(1.4, 2.8, "mating", va="center", fontsize=8.5)
    a.plot([0.4, 1.2], [2.0, 2.0], color=INK, lw=1.2)
    a.plot([0.4, 1.2], [1.85, 1.85], color=INK, lw=1.2)
    a.text(1.4, 1.95, "consanguineous mating", va="center", fontsize=8.5)

    def sq(x, y, fc="white"):
        a.add_patch(Rectangle((x - 0.4, y - 0.4), 0.8, 0.8, fc=fc, ec=INK, lw=1.2))

    def ci(x, y, fc="white", half=False):
        a.add_patch(Circle((x, y), 0.42, fc=fc, ec=INK, lw=1.2))
        if half:
            a.add_patch(Wedge((x, y), 0.42, 90, 270, fc=INK, ec=INK))

    # autosomal recessive example: two carriers have an affected child
    a.text(12.0, 8.7, "Autosomal recessive trait (e.g. sickle-cell anaemia)", ha="center", fontsize=9, weight="bold")
    ci(9.5, 7.0, half=True)
    sq(14.5, 7.0)
    a.add_patch(Wedge((14.5, 7.0), 0.0, 0, 1))
    a.add_patch(Rectangle((14.1, 6.6), 0.4, 0.8, fc=INK, ec=INK))
    a.plot([9.92, 14.1], [7.0, 7.0], color=INK, lw=1.2)
    a.plot([12.0, 12.0], [7.0, 5.6], color=INK, lw=1.2)
    a.plot([8.5, 15.5], [5.6, 5.6], color=INK, lw=1.2)
    xs = [8.5, 10.8, 13.2, 15.5]
    kinds = [("sq", INK, False), ("ci", "white", True), ("sq", "white", False), ("ci", "white", True)]
    for x, (k, fc, half) in zip(xs, kinds):
        a.plot([x, x], [5.6, 4.9], color=INK, lw=1.2)
        if k == "sq":
            sq(x, 4.5, fc)
        else:
            ci(x, 4.5, fc, half)
    a.text(9.5, 7.75, "Aa (carrier)", ha="center", fontsize=8)
    a.text(14.5, 7.75, "Aa (carrier)", ha="center", fontsize=8)
    for x, g in zip(xs, ["aa (affected)", "Aa", "AA", "Aa"]):
        a.text(x, 3.7, g, ha="center", fontsize=8)
    a.text(12.0, 2.4, "Unaffected (carrier) parents with an affected child → the trait is recessive.\n"
                      "An autosomal trait appears equally often in sons and daughters.", ha="center", fontsize=8.5,
           color=GREY)
    save(fig, "bio_ch04_fig03_pedigree.png")


if __name__ == "__main__":
    fig01_dihybrid()
    fig02_sex_determination()
    fig03_pedigree()
