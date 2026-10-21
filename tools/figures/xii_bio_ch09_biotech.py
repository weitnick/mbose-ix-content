"""Figures for Class XII Biology Chapter 9, Biotechnology: Principles and Processes.
Run: python xii_bio_ch09_biotech.py
"""
from xii_bio_common import *

MONO = dict(family="DejaVu Sans Mono")


def fig01_ecori():
    fig, a = canvas(9.4, 4.8, (0, 19), (0, 9.6))
    a.text(9.5, 9.1, "EcoRI cuts the palindrome GAATTC between G and A on both strands, leaving sticky ends",
           ha="center", fontsize=9, weight="bold")
    a.text(1.0, 7.6, "5′ – C T G A A T T C G A – 3′", fontsize=11, **MONO)
    a.text(1.0, 6.8, "3′ – G A C T T A A G C T – 5′", fontsize=11, **MONO)
    a.plot([3.56, 3.56], [7.45, 8.2], color=RED, lw=2)
    a.plot([5.56, 5.56], [6.55, 7.25], color=RED, lw=2)
    a.text(3.56, 8.35, "cut", color=RED, fontsize=8, ha="center")
    a.text(5.56, 6.25, "cut", color=RED, fontsize=8, ha="center")
    arrow(a, (9.8, 7.2), (11.4, 7.2), text="EcoRI", fs=8)
    a.text(11.7, 7.6, "5′ – C T G", fontsize=11, **MONO)
    a.text(11.7, 6.8, "3′ – G A C T T A A", fontsize=11, **MONO)
    a.text(15.4, 7.6, "A A T T C G A – 3′", fontsize=11, **MONO)
    a.text(15.4, 6.8, "      G C T – 5′", fontsize=11, **MONO)
    a.text(14.2, 5.9, "sticky ends (single-stranded overhangs AATT)", ha="center", fontsize=8.5, color=BLUE)
    box(a, (0.6, 1.0), 5.2, 2.6, "vector DNA cut\nwith EcoRI", fc=PALE_BLUE, ec=BLUE, fs=9)
    box(a, (6.9, 1.0), 5.2, 2.6, "foreign DNA (gene of\ninterest) cut with EcoRI", fc=PALE_AMBER, ec=AMBER, fs=9)
    box(a, (13.2, 1.0), 5.4, 2.6, "sticky ends pair;\nDNA ligase joins them\n→ recombinant DNA", fc=PALE_GREEN, ec=GREEN,
        fs=9, bold=True)
    arrow(a, (5.8, 2.3), (6.9, 2.3), text="+", fs=10, dy=0.1)
    arrow(a, (12.1, 2.3), (13.2, 2.3))
    save(fig, "bio_ch09_fig01_ecori_sticky_ends.png")


def fig02_pbr322():
    fig, a = canvas(6.4, 6.0, (-5.2, 5.2), (-4.8, 4.8))
    a.add_patch(Circle((0, 0), 2.6, fc="none", ec=INK, lw=2.4))
    a.add_patch(Wedge((0, 0), 2.85, 200, 290, width=0.5, fc=PALE_RED, ec=RED))         # ampR
    a.add_patch(Wedge((0, 0), 2.85, 30, 120, width=0.5, fc=PALE_BLUE, ec=BLUE))         # tetR
    a.add_patch(Wedge((0, 0), 2.85, 300, 330, width=0.5, fc=PALE_GREEN, ec=GREEN))      # ori
    a.add_patch(Wedge((0, 0), 2.85, 335, 355, width=0.5, fc=PALE_AMBER, ec=AMBER))      # rop
    a.text(-1.55, -1.0, "ampᴿ", fontsize=11, color=RED, ha="center")
    a.text(0.6, 1.5, "tetᴿ", fontsize=11, color=BLUE, ha="center")
    a.text(1.65, -0.9, "ori", fontsize=10, color=GREEN, ha="center")
    a.text(1.9, -0.25, "rop", fontsize=9, color=AMBER, ha="center")
    a.text(0, 0, "pBR322\n(4361 bp)", ha="center", va="center", fontsize=10, weight="bold")
    sites = [("EcoRI", 140), ("ClaI", 128), ("HindIII", 118), ("BamHI", 80), ("SalI", 55), ("PvuII", 340),
             ("PstI", 250), ("PvuI", 232)]
    for name, ang in sites:
        t = np.radians(ang)
        a.plot([2.6 * np.cos(t), 3.2 * np.cos(t)], [2.6 * np.sin(t), 3.2 * np.sin(t)], color=INK, lw=1)
        a.text(3.6 * np.cos(t), 3.6 * np.sin(t), name, ha="center", va="center", fontsize=8)
    a.text(0, -4.5, "ampᴿ, tetᴿ: antibiotic-resistance genes (selectable markers); ori: origin of replication;\n"
                    "rop: codes proteins for plasmid replication; BamHI and SalI lie in tetᴿ, PstI and PvuI in ampᴿ",
           ha="center", fontsize=7.5, color=GREY)
    save(fig, "bio_ch09_fig02_pbr322.png")


def fig03_pcr():
    fig, a = canvas(9.4, 4.4, (0, 19), (0, 8.8))
    steps = [("1. Denaturation\n(about 94 °C)", "double-stranded DNA\nseparates into\nsingle strands"),
             ("2. Annealing\n(about 50–60 °C)", "two primers bind to\ncomplementary ends\nof the target region"),
             ("3. Extension\n(about 72 °C)", "Taq DNA polymerase\n(Thermus aquaticus)\nextends the primers")]
    for i, (t, d) in enumerate(steps):
        x = 0.5 + i * 6.3
        box(a, (x, 5.4), 5.4, 1.6, t, fc=SOFT, ec=BLUE, fs=9, bold=True)
        a.text(x + 2.7, 4.2, d, ha="center", va="center", fontsize=8.5)
        if i < 2:
            arrow(a, (x + 5.4, 6.2), (x + 6.3, 6.2))
    a.annotate("", xy=(1.5, 7.1), xytext=(17.3, 7.1),
               arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.4, connectionstyle="arc3,rad=0.25"))
    a.text(9.5, 8.45, "repeat the cycle (about 30 times)", ha="center", fontsize=8.5, color=GREEN)
    a.text(9.5, 1.8, "Each cycle doubles the DNA: after n cycles, about 2ⁿ copies — about 1 billion copies in 30 cycles",
           ha="center", fontsize=8.5, weight="bold")
    a.text(9.5, 0.9, "Ingredients: template DNA, two primers, dNTPs, thermostable DNA polymerase, buffer", ha="center",
           fontsize=8, color=GREY)
    save(fig, "bio_ch09_fig03_pcr.png")


def fig04_gel():
    fig, a = canvas(5.6, 4.6, (0, 11), (0, 9))
    a.add_patch(Rectangle((1.0, 1.0), 8.0, 6.6, fc="#F1EFE6", ec=INK, lw=1.2))
    a.text(5.0, 8.2, "cathode (–): wells (samples loaded)", ha="center", fontsize=8.5)
    a.text(5.0, 0.4, "anode (+): DNA (negative) moves this way", ha="center", fontsize=8.5)
    lanes = [[1.2], [2.0, 3.6, 5.2], [1.6, 4.1], [2.8, 4.6, 6.0]]
    for i, bands in enumerate(lanes):
        x = 2.0 + i * 1.9
        a.add_patch(Rectangle((x - 0.5, 7.1), 1.0, 0.3, fc="white", ec=INK, lw=0.8))
        for b in bands:
            a.add_patch(Rectangle((x - 0.5, 7.0 - b), 1.0, 0.25, fc="#E6893A", ec="none"))
        a.text(x, 7.75, str(i + 1), ha="center", fontsize=8)
    a.annotate("", xy=(9.6, 1.6), xytext=(9.6, 6.6), arrowprops=dict(arrowstyle="-|>", color=INK))
    a.text(10.0, 4.1, "smaller\nfragments\nmove\nfarther", fontsize=7.5, va="center")
    save(fig, "bio_ch09_fig04_gel.png")


def fig05_rdna_steps():
    fig, a = canvas(10.0, 3.6, (0, 20), (0, 7.2))
    steps = ["isolate DNA\n(lysozyme,\ncellulase,\nchitinase;\nRNase, protease;\nchilled ethanol)",
             "cut DNA and\nvector with the\nsame restriction\nenzyme",
             "amplify gene\nof interest\nby PCR", "ligate gene\ninto vector\n(DNA ligase) →\nrecombinant DNA",
             "insert into a\ncompetent host\n(transformation)", "select\nrecombinants;\nexpress gene\n(bioreactor)",
             "downstream\nprocessing:\nseparate, purify,\nformulate, test"]
    for i, t in enumerate(steps):
        x = 0.2 + i * 2.85
        box(a, (x, 1.6), 2.5, 4.2, t, fc=SOFT if i % 2 == 0 else PALE_GREEN, ec=BLUE if i % 2 == 0 else GREEN, fs=7.2)
        if i < 6:
            arrow(a, (x + 2.5, 3.7), (x + 2.85, 3.7), ms=8)
    a.text(10.0, 6.6, "Processes of recombinant DNA technology", ha="center", fontsize=9.5, weight="bold")
    save(fig, "bio_ch09_fig05_rdna_steps.png")


if __name__ == "__main__":
    fig01_ecori()
    fig02_pbr322()
    fig03_pcr()
    fig04_gel()
    fig05_rdna_steps()
