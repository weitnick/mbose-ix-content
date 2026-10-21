"""Figures for Class XII Biology Chapter 1, Sexual Reproduction in Flowering Plants.
Run: python xii_bio_ch01_flowering.py
"""
from xii_bio_common import *


def fig01_anther_pollen():
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.2))
    for ax in (a, b):
        ax.set_aspect("equal")
        ax.axis("off")
    # (a) T.S. of a microsporangium: four wall layers round the sporogenous tissue
    a.set_xlim(-3.4, 3.4)
    a.set_ylim(-2.9, 2.9)
    layers = [(2.2, "#F3E6CF", "epidermis"), (1.95, "#E8D4B0", "endothecium"), (1.7, "#F5EBDD", "middle layers"),
              (1.35, PALE_AMBER, "tapetum")]
    for r, c, _ in layers:
        a.add_patch(Circle((0, 0), r, fc=c, ec=INK, lw=0.9))
    a.add_patch(Circle((0, 0), 1.05, fc="white", ec=INK, lw=0.9))
    rng = np.random.default_rng(3)
    for _ in range(26):
        rr, t = 0.85 * np.sqrt(rng.random()), 2 * np.pi * rng.random()
        a.add_patch(Circle((rr * np.cos(t), rr * np.sin(t)), 0.11, fc=PALE_GREEN, ec=GREEN, lw=0.6))
    label(a, (1.5, 1.5), (2.4, 2.5), "epidermis")
    label(a, (1.86, 0.5), (2.6, 1.2), "endothecium")
    label(a, (1.55, -0.5), (2.6, -0.6), "middle layers")
    label(a, (1.2, -0.6), (2.4, -1.6), "tapetum (nourishes\npollen)")
    label(a, (-0.4, -0.3), (-2.4, -2.2), "sporogenous tissue\n(pollen mother cells)")
    a.set_title("(a) T.S. of a microsporangium", fontsize=10)
    # (b) a pollen grain with its two cells
    b.set_xlim(-3.4, 3.4)
    b.set_ylim(-2.9, 2.9)
    b.add_patch(Circle((0, 0), 2.0, fc=PALE_AMBER, ec=AMBER, lw=2.6))
    b.add_patch(Circle((0, 0), 1.78, fc="white", ec=AMBER, lw=0.9))
    b.add_patch(Rectangle((1.8, -0.22), 0.35, 0.44, fc="white", ec="white"))
    b.add_patch(Circle((0.25, 0.2), 0.42, fc=PALE_BLUE, ec=BLUE, lw=1))
    b.add_patch(Ellipse((-0.75, -0.55), 0.95, 0.55, angle=20, fc=PALE_GREEN, ec=GREEN, lw=1))
    b.add_patch(Circle((-0.75, -0.55), 0.13, fc=GREEN, ec=GREEN))
    label(b, (-1.2, 1.55), (-2.5, 2.5), "exine (sporopollenin)")
    label(b, (-1.62, 0.5), (-2.7, 1.2), "intine")
    label(b, (2.0, 0.0), (2.5, 1.0), "germ pore")
    label(b, (0.25, 0.2), (2.4, -1.4), "vegetative cell nucleus")
    label(b, (-0.8, -0.6), (-2.5, -2.2), "generative cell")
    b.set_title("(b) Mature pollen grain (2-celled stage)", fontsize=10)
    fig.tight_layout()
    save(fig, "bio_ch01_fig01_anther_pollen.png")


def fig02_ovule():
    fig, a = canvas(6.4, 5.4, (-4, 4.6), (-3.4, 3.8))
    a.add_patch(Ellipse((0.3, 0.6), 4.6, 5.6, fc="#F3E6CF", ec=INK, lw=1.2))          # outer integument
    a.add_patch(Ellipse((0.3, 0.6), 3.9, 4.9, fc="#E8D4B0", ec=INK, lw=1.0))          # inner integument
    a.add_patch(Ellipse((0.3, 0.6), 3.2, 4.2, fc=PALE_GREEN, ec=GREEN, lw=1.0))       # nucellus
    a.add_patch(Ellipse((0.3, 0.5), 1.3, 2.4, fc="white", ec=INK, lw=1.0))            # embryo sac
    a.add_patch(Rectangle((-0.25, -2.4), 1.1, 0.75, fc="white", ec="white"))          # micropyle gap
    a.plot([-0.2, -0.2], [-2.35, -1.55], color=INK, lw=0.8)
    a.plot([0.8, 0.8], [-2.35, -1.55], color=INK, lw=0.8)
    a.add_patch(Polygon([(-1.55, -1.75), (-1.05, -2.15), (-2.6, -3.35), (-3.1, -2.95)], closed=True,
                        fc="#F3E6CF", ec=INK, lw=1))                                   # funicle (beside micropyle)
    for (x, y) in ((0.05, -0.35), (0.55, -0.35), (0.3, -0.55)):
        a.add_patch(Circle((x, y), 0.13, fc=PALE_BLUE, ec=BLUE, lw=0.8))
    for (x, y) in ((0.1, 1.35), (0.5, 1.35), (0.3, 1.55)):
        a.add_patch(Circle((x, y), 0.12, fc=PALE_AMBER, ec=AMBER, lw=0.8))
    a.add_patch(Circle((0.18, 0.55), 0.1, fc=GREY, ec=INK, lw=0.6))
    a.add_patch(Circle((0.42, 0.55), 0.1, fc=GREY, ec=INK, lw=0.6))
    label(a, (-2.4, -2.9), (-3.7, -2.0), "funicle")
    label(a, (-1.3, -1.95), (-3.7, -1.3), "hilum")
    label(a, (0.3, 3.2), (1.6, 3.6), "chalaza")
    label(a, (2.4, 1.2), (3.2, 2.2), "outer integument")
    label(a, (2.15, 0.2), (3.2, 0.9), "inner integument")
    label(a, (1.75, -0.6), (3.2, -0.4), "nucellus")
    label(a, (0.9, 0.9), (3.2, -1.4), "embryo sac")
    label(a, (0.3, -2.2), (2.2, -2.9), "micropyle")
    label(a, (0.3, 1.45), (-3.0, 0.9), "antipodals")
    label(a, (0.3, 0.55), (-3.0, 0.1), "polar nuclei")
    label(a, (0.05, -0.4), (-3.0, -0.6), "egg apparatus")
    a.set_title("L.S. of an anatropous ovule (schematic)", fontsize=10)
    save(fig, "bio_ch01_fig02_ovule.png")


def fig03_embryo_sac():
    fig, a = canvas(6.4, 4.8, (-4.2, 4.6), (-3.1, 2.6))
    a.add_patch(Ellipse((0, 0), 6.4, 3.4, fc="white", ec=INK, lw=1.4))
    # micropylar end (left): egg apparatus
    a.add_patch(Ellipse((-2.3, 0.55), 1.2, 0.7, fc=PALE_BLUE, ec=BLUE))
    a.add_patch(Ellipse((-2.3, -0.55), 1.2, 0.7, fc=PALE_BLUE, ec=BLUE))
    a.add_patch(Ellipse((-1.55, 0.0), 1.0, 0.95, fc="#D5E6D6", ec=GREEN, lw=1.2))
    for (x, y) in ((-2.25, 0.55), (-2.25, -0.55)):
        a.add_patch(Circle((x, y), 0.12, fc=BLUE, ec=BLUE))
    a.add_patch(Circle((-1.55, 0), 0.15, fc=GREEN, ec=GREEN))
    for y in (0.62, -0.62):
        a.plot([-3.1, -2.8], [y * 0.5, y * 0.8], color=BLUE, lw=2)
    # central cell with two polar nuclei
    a.add_patch(Circle((0.25, 0.15), 0.17, fc=AMBER, ec=AMBER))
    a.add_patch(Circle((0.6, -0.1), 0.17, fc=AMBER, ec=AMBER))
    # chalazal end (right): three antipodals
    for (x, y) in ((2.35, 0.6), (2.35, -0.6), (2.75, 0.0)):
        a.add_patch(Circle((x, y), 0.42, fc="#F1E3F4", ec="#7B3F8C"))
        a.add_patch(Circle((x, y), 0.1, fc="#7B3F8C", ec="#7B3F8C"))
    label(a, (-3.05, 0.4), (-4.0, 1.9), "filiform apparatus")
    label(a, (-2.3, 0.75), (-2.6, 2.3), "synergids (2)")
    label(a, (-1.5, -0.3), (-0.6, -2.1), "egg cell")
    label(a, (0.4, 0.05), (0.6, 2.3), "central cell with\n2 polar nuclei")
    label(a, (2.6, 0.8), (3.2, 2.1), "antipodals (3)")
    a.text(-4.1, -1.0, "micropylar end", fontsize=8.5, color=GREY)
    a.text(3.0, -1.6, "chalazal end", fontsize=8.5, color=GREY)
    a.text(0.2, -2.9, "7 cells, 8 nuclei: 3 (egg apparatus) + 1 central cell (2 nuclei) + 3 antipodals", fontsize=8.5,
           ha="center")
    save(fig, "bio_ch01_fig03_embryo_sac.png")


def fig04_double_fertilisation():
    fig, a = canvas(7.4, 3.6, (0, 12), (0, 5.6))
    box(a, (0.2, 3.6), 2.6, 1.0, "pollen tube\n(2 male gametes, n)", fc=PALE_AMBER, ec=AMBER)
    box(a, (4.2, 4.2), 2.2, 0.9, "egg (n)", fc=PALE_BLUE, ec=BLUE)
    box(a, (4.2, 1.0), 2.2, 1.2, "2 polar nuclei\n(n + n)", fc=PALE_AMBER, ec=AMBER)
    box(a, (8.4, 4.2), 3.3, 0.9, "zygote (2n) → embryo", fc="#D5E6D6", ec=GREEN, bold=True)
    box(a, (8.4, 1.1), 3.3, 1.0, "PEN (3n) → endosperm", fc="#F6E1DE", ec=RED, bold=True)
    arrow(a, (2.8, 4.3), (4.2, 4.65))
    arrow(a, (2.8, 3.8), (4.2, 1.7))
    a.text(2.6, 5.15, "male gamete 1", fontsize=8.5, color=INK)
    a.text(3.6, 2.7, "male gamete 2", fontsize=8.5, color=INK)
    arrow(a, (6.4, 4.65), (8.4, 4.65), text="syngamy", dy=0.1)
    arrow(a, (6.4, 1.6), (8.4, 1.6), text="triple fusion", dy=0.1)
    a.text(6.0, 0.25, "Two fusions in one embryo sac = double fertilisation (unique to flowering plants)",
           ha="center", fontsize=9, color=INK)
    save(fig, "bio_ch01_fig04_double_fertilisation.png")


if __name__ == "__main__":
    fig01_anther_pollen()
    fig02_ovule()
    fig03_embryo_sac()
    fig04_double_fertilisation()
