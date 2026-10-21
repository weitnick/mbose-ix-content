"""Figures for Class XII Biology Chapter 8, Microbes in Human Welfare.
Run: python xii_bio_ch08_microbes.py
"""
from xii_bio_common import *


def fig01_sewage():
    fig, a = canvas(10.0, 4.6, (0, 20), (0, 9.2))
    box(a, (0.2, 6.6), 3.0, 1.4, "sewage\n(municipal\nwaste water)", fc="#EEE7DD", ec=AMBER, fs=8)
    box(a, (4.2, 6.4), 4.2, 1.8, "PRIMARY TREATMENT\n(physical): filtration of\ndebris, sedimentation of grit",
        fc=PALE_AMBER, ec=AMBER, fs=7.8)
    box(a, (4.4, 3.6), 3.8, 1.2, "primary sludge\n(settled solids)", fc="white", ec=GREY, fs=8)
    box(a, (9.4, 6.4), 4.6, 1.8, "SECONDARY TREATMENT\n(biological): aeration tank —\naerobic microbes form flocs;\nBOD falls",
        fc=PALE_GREEN, ec=GREEN, fs=7.8)
    box(a, (15.0, 6.4), 4.7, 1.8, "settling tank: flocs\nsediment as\nACTIVATED SLUDGE", fc=SOFT, ec=BLUE, fs=7.8)
    box(a, (15.0, 1.6), 4.7, 1.8, "anaerobic sludge digester:\nbacteria digest sludge →\nbiogas (CH₄, H₂S, CO₂)", fc=PALE_RED,
        ec=RED, fs=7.8)
    box(a, (9.4, 1.6), 4.6, 1.8, "effluent (low BOD)\nreleased into rivers\nand streams", fc="#E3F1F7", ec=BLUE, fs=7.8)
    arrow(a, (3.2, 7.3), (4.2, 7.3))
    arrow(a, (6.3, 6.4), (6.3, 4.8))
    arrow(a, (8.4, 7.3), (9.4, 7.3), text="primary\neffluent", fs=7, dy=0.15)
    arrow(a, (14.0, 7.3), (15.0, 7.3))
    arrow(a, (17.35, 6.4), (17.35, 3.4), text="major part", fs=7, dy=0)
    arrow(a, (15.0, 6.6), (12.5, 6.4), color=GREEN, lw=1.0, ms=8)
    a.text(13.2, 5.6, "small part returned\nas inoculum", fontsize=7, color=GREEN, ha="center")
    arrow(a, (15.0, 7.0), (13.8, 3.4), color=BLUE, lw=1.0, ms=8)
    a.text(10.0, 8.9, "Sewage treatment plant (STP)", ha="center", fontsize=10, weight="bold")
    save(fig, "bio_ch08_fig01_sewage.png")


def fig02_biogas():
    fig, a = canvas(7.6, 4.6, (0, 15), (0, 9.2))
    a.add_patch(Rectangle((4.0, 1.0), 6.0, 4.2, fc="#EEE7DD", ec=INK, lw=1.4))       # digester pit
    a.add_patch(Rectangle((4.0, 1.0), 6.0, 2.8, fc="#C9B79C", ec="none"))              # slurry
    a.add_patch(Rectangle((4.3, 3.8), 5.4, 2.4, fc="#DCE8F4", ec=BLUE, lw=1.6))       # floating gas holder
    a.text(7.0, 5.0, "floating cover\n(rises as gas collects)", ha="center", fontsize=8)
    a.text(7.0, 2.2, "dung slurry —\nmethanogens\n(Methanobacterium)", ha="center", fontsize=8)
    a.plot([7.0, 7.0, 12.6], [6.2, 7.6, 7.6], color=BLUE, lw=3)
    a.text(12.7, 7.6, "biogas to homes\n(cooking, lighting)", fontsize=8, va="center")
    a.add_patch(Polygon([(0.6, 5.4), (3.0, 5.4), (2.2, 4.4), (1.4, 4.4)], closed=True, fc="#EEE7DD", ec=INK))
    a.plot([1.8, 1.8, 4.2], [4.4, 1.6, 1.6], color=INK, lw=3)
    a.text(1.8, 5.8, "inlet: dung +\nwater slurry", ha="center", fontsize=8)
    a.plot([9.8, 12.0, 12.0], [1.6, 1.6, 3.6], color=INK, lw=3)
    a.add_patch(Polygon([(11.2, 3.6), (13.0, 3.6), (12.6, 4.4), (11.6, 4.4)], closed=True, fc="#C9B79C", ec=INK))
    a.text(12.1, 4.9, "outlet: spent slurry\n(used as manure)", ha="center", fontsize=8)
    a.text(7.0, 0.35, "Concrete tank 10–15 feet deep; technology developed by IARI and KVIC", ha="center", fontsize=8,
           color=GREY)
    save(fig, "bio_ch08_fig02_biogas.png")


if __name__ == "__main__":
    fig01_sewage()
    fig02_biogas()
