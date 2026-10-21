"""Figures for Class XII Biology Chapter 5, Molecular Basis of Inheritance.
Run: python xii_bio_ch05_molecular.py
"""
from xii_bio_common import *

PURPLE = "#7B3F8C"


def fig01_double_helix():
    fig, a = plt.subplots(figsize=(4.6, 6.6))
    a.set_xlim(-3.4, 3.6)
    a.set_ylim(-0.8, 10.6)
    a.axis("off")
    y = np.linspace(0, 10, 400)
    x1 = 1.0 * np.sin(2 * np.pi * y / 3.4)
    x2 = 1.0 * np.sin(2 * np.pi * y / 3.4 + np.pi)
    pairs = ["A–T", "G≡C", "T–A", "C≡G", "A–T", "G≡C", "C≡G", "T–A", "A–T", "G≡C", "T–A", "C≡G", "G≡C",
             "A–T", "T–A", "C≡G", "A–T", "G≡C", "T–A", "C≡G", "A–T", "G≡C", "C≡G", "T–A", "A–T", "G≡C",
             "T–A", "C≡G", "A–T"]
    for k, yy in enumerate(np.arange(0.17, 9.9, 0.34)):
        xa = np.sin(2 * np.pi * yy / 3.4)
        col = BLUE if "A" in pairs[k % len(pairs)] else RED
        a.plot([xa, -xa], [yy, yy], color=col, lw=1.4, alpha=0.8)
    a.plot(x1, y, color=INK, lw=3)
    a.plot(x2, y, color=GREY, lw=3)
    a.annotate("", xy=(2.3, 6.8), xytext=(2.3, 3.4), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
    a.text(2.45, 5.1, "one turn\n= 3.4 nm\n= 10 bp", fontsize=8.5, va="center")
    a.annotate("", xy=(-1.0, -0.45), xytext=(1.0, -0.45), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
    a.text(0, -0.75, "diameter 2 nm", ha="center", fontsize=8.5)
    a.text(-1.9, 10.2, "5′", fontsize=10, color=INK)
    a.text(1.2, 10.2, "3′", fontsize=10, color=GREY)
    a.text(-1.9, 0.1, "3′", fontsize=10, color=INK)
    a.text(1.2, 0.1, "5′", fontsize=10, color=GREY)
    label(a, (0.95, 8.0), (2.3, 9.3), "sugar–phosphate\nbackbone")
    label(a, (0.0, 7.65), (-2.0, 8.6), "base pairs")
    a.text(-3.3, 2.2, "A–T: 2 H-bonds\nG≡C: 3 H-bonds\nstrands antiparallel\n0.34 nm between\nbase pairs", fontsize=8,
           va="center", color=INK)
    a.set_title("DNA double helix (Watson and Crick)", fontsize=10)
    save(fig, "bio_ch05_fig01_double_helix.png")


def fig02_nucleosome():
    fig, a = canvas(7.0, 3.6, (0, 14), (0, 7.2))
    for cx in (3.0, 9.0):
        a.add_patch(Circle((cx, 3.6), 1.4, fc=PALE_AMBER, ec=AMBER, lw=1.4))
        t = np.linspace(-0.3, 2 * np.pi * 1.65, 300)
        a.plot(cx + 1.6 * np.cos(t), 3.6 + 1.6 * np.sin(t) * 0.55 + 0.15 * t - 0.6, color=BLUE, lw=2.4)
        a.add_patch(Rectangle((cx + 1.45, 2.3), 0.35, 2.6, fc="#DDD5E8", ec=PURPLE, lw=1))
    a.plot([4.6, 7.4], [4.0, 3.2], color=BLUE, lw=2.4)
    a.plot([0.2, 1.4], [3.0, 2.8], color=BLUE, lw=2.4)
    a.plot([10.6, 13.6], [4.2, 4.6], color=BLUE, lw=2.4)
    label(a, (3.0, 3.6), (1.0, 6.6), "histone octamer\n(positively charged)")
    label(a, (4.4, 4.4), (5.6, 6.6), "DNA (negatively charged)\nwrapped round it")
    label(a, (10.6, 3.0), (11.6, 1.2), "H1 histone")
    label(a, (6.0, 3.6), (6.0, 1.0), "linker DNA")
    a.text(7.0, 0.25, "One nucleosome ≈ 200 bp of DNA; nucleosomes look like 'beads on a string' (chromatin)",
           ha="center", fontsize=8.5, color=GREY)
    save(fig, "bio_ch05_fig02_nucleosome.png")


def fig03_replication_fork():
    fig, a = canvas(8.6, 4.4, (0, 17), (0, 8.6))
    a.plot([0.5, 7.0], [4.6, 4.6], color=INK, lw=2.4)
    a.plot([0.5, 7.0], [4.0, 4.0], color=GREY, lw=2.4)
    a.add_patch(Circle((7.2, 4.3), 0.5, fc=PALE_AMBER, ec=AMBER, lw=1.2))
    a.text(5.2, 5.3, "helicase (fork moves ←)", fontsize=8.5, color=AMBER)
    a.plot([7.4, 16.5], [4.6, 7.2], color=INK, lw=2.4)
    a.plot([7.4, 16.5], [4.0, 1.4], color=GREY, lw=2.4)
    a.add_patch(FancyArrowPatch((16.2, 6.55), (8.0, 4.15 + 0.6), arrowstyle="-|>", mutation_scale=12, color=BLUE,
                                lw=2.2))
    a.text(9.6, 4.55, "leading strand (continuous, 5′ → 3′)", fontsize=8.5, color=BLUE, rotation=12)
    for x0 in (8.4, 11.2, 14.0):
        y0 = 4.0 - (x0 - 7.4) * (2.6 / 9.1) - 0.55
        x1 = x0 + 2.3
        y1 = 4.0 - (x1 - 7.4) * (2.6 / 9.1) - 0.55
        a.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=10, color=RED, lw=2.0))
    a.text(7.6, 0.3, "lagging strand: Okazaki fragments (5′ → 3′), joined by DNA ligase", fontsize=8.5, color=RED)
    a.text(0.5, 5.0, "parent DNA", fontsize=8.5)
    a.text(16.6, 7.4, "3′", fontsize=9)
    a.text(16.6, 1.0, "5′", fontsize=9)
    a.text(0.2, 4.55, "5′", fontsize=9)
    a.text(0.2, 3.85, "3′", fontsize=9)
    a.text(8.5, 8.1, "Replication fork: DNA polymerase adds nucleotides only in the 5′ → 3′ direction", ha="center",
           fontsize=9, weight="bold")
    save(fig, "bio_ch05_fig03_replication_fork.png")


def fig04_transcription_unit():
    fig, a = canvas(8.6, 3.2, (0, 17), (0, 6.2))
    for y, (l, r), name in ((4.0, ("3′", "5′"), "template strand (3′ → 5′)"), (2.6, ("5′", "3′"), "coding strand (5′ → 3′)")):
        a.plot([1.2, 16.0], [y, y], color=INK, lw=2)
        a.text(0.7, y, l, va="center", fontsize=9)
        a.text(16.2, y, r, va="center", fontsize=9)
        a.text(16.8, y, "", fontsize=8)
    a.text(8.7, 3.65, "template strand (3′ → 5′)", ha="center", fontsize=8.5, color=BLUE)
    a.text(8.7, 2.15, "coding strand (5′ → 3′)", ha="center", fontsize=8.5, color=GREY)
    a.add_patch(FancyBboxPatch((2.8, 2.3), 2.4, 2.0, boxstyle="round,pad=0.05,rounding_size=0.25", fc="none",
                               ec=GREEN, lw=1.6))
    a.add_patch(FancyBboxPatch((12.2, 2.3), 2.4, 2.0, boxstyle="round,pad=0.05,rounding_size=0.25", fc="none",
                               ec=RED, lw=1.6))
    a.text(4.0, 4.75, "promoter", ha="center", fontsize=9, color=GREEN)
    a.text(13.4, 4.75, "terminator", ha="center", fontsize=9, color=RED)
    a.text(8.7, 4.75, "structural gene", ha="center", fontsize=9)
    a.annotate("", xy=(7.2, 5.6), xytext=(5.3, 5.6), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2))
    a.plot([5.3, 5.3], [4.3, 5.6], color=INK, lw=1.2)
    a.text(5.4, 5.8, "transcription start site", fontsize=8.5)
    a.text(8.5, 0.6, "Promoter lies towards the 5′ end (upstream) of the structural gene, with reference to the coding "
                     "strand; the terminator at the 3′ end (downstream).", ha="center", fontsize=8, color=GREY)
    save(fig, "bio_ch05_fig04_transcription_unit.png")


def fig05_lac_operon():
    fig, (a, b) = plt.subplots(2, 1, figsize=(9.0, 5.2))
    for ax in (a, b):
        ax.set_xlim(0, 18)
        ax.set_ylim(0, 5)
        ax.axis("off")
    genes = [("i", 0.4, 1.6, "#DDD5E8", PURPLE), ("p", 2.6, 1.2, PALE_GREEN, GREEN), ("o", 3.8, 1.2, PALE_AMBER, AMBER),
             ("z", 5.0, 3.4, PALE_BLUE, BLUE), ("y", 8.4, 3.0, PALE_BLUE, BLUE), ("a", 11.4, 3.0, PALE_BLUE, BLUE)]
    for ax in (a, b):
        ax.plot([0.2, 14.8], [2.0, 2.0], color=INK, lw=1.4)
        for g, x, w, fc, ec in genes:
            ax.add_patch(Rectangle((x, 1.6), w, 0.8, fc=fc, ec=ec, lw=1.2))
            ax.text(x + w / 2, 2.0, g, ha="center", va="center", fontsize=10, weight="bold")
    # (a) no inducer
    a.add_patch(Ellipse((4.4, 2.75), 1.6, 1.0, fc="#DDD5E8", ec=PURPLE, lw=1.2))
    a.text(4.4, 2.75, "repressor", ha="center", va="center", fontsize=7.5)
    arrow(a, (1.2, 2.4), (3.6, 2.9), color=PURPLE, lw=1.0, ms=8)
    a.text(1.0, 3.5, "i gene makes the repressor", fontsize=7.5, color=PURPLE)
    a.text(15.3, 2.6, "repressor binds the operator:\nRNA polymerase is blocked\n→ no transcription (OFF)",
           fontsize=8.5, color=RED)
    a.set_title("(a) No inducer (no lactose)", fontsize=10, loc="left")
    # (b) inducer present
    b.add_patch(Ellipse((4.0, 3.9), 1.6, 1.0, fc="#DDD5E8", ec=PURPLE, lw=1.2))
    b.text(4.0, 3.9, "repressor", ha="center", va="center", fontsize=7.5)
    b.add_patch(Circle((4.95, 4.25), 0.3, fc=AMBER, ec=AMBER))
    b.text(5.4, 4.25, "inducer (allolactose)\ninactivates repressor", fontsize=7.5, va="center")
    b.add_patch(FancyBboxPatch((2.4, 0.4), 1.2, 0.7, boxstyle="round,pad=0.03", fc=PALE_GREEN, ec=GREEN))
    b.text(3.0, 0.75, "RNA pol", ha="center", va="center", fontsize=7.5)
    arrow(b, (5.0, 1.1), (14.4, 1.1), color=GREEN, lw=1.4)
    b.text(9.0, 0.5, "polycistronic mRNA → β-galactosidase (z), permease (y), transacetylase (a)", fontsize=7.5,
           ha="center", color=GREEN)
    b.text(15.3, 2.6, "operator free:\ntranscription of z, y, a\n(ON)", fontsize=8.5, color=GREEN)
    b.set_title("(b) Inducer (lactose) present", fontsize=10, loc="left")
    fig.tight_layout()
    save(fig, "bio_ch05_fig05_lac_operon.png")


def fig06_translation():
    fig, a = canvas(8.6, 4.2, (0, 17), (0, 8.4))
    a.plot([0.5, 16.5], [2.0, 2.0], color=INK, lw=2)
    codons = ["AUG", "UUC", "GGA", "AAA", "UGG", "UAA"]
    for i, c in enumerate(codons):
        a.text(2.5 + i * 2.3, 1.45, c, ha="center", fontsize=9, family="monospace")
    a.text(0.4, 1.45, "5′", fontsize=9)
    a.text(16.3, 1.45, "3′", fontsize=9)
    a.add_patch(Ellipse((6.0, 2.8), 7.0, 2.4, fc=PALE_BLUE, ec=BLUE, lw=1.4, alpha=0.7))     # small subunit
    a.add_patch(Ellipse((6.0, 5.0), 7.6, 3.6, fc="#E7EEF7", ec=BLUE, lw=1.4, alpha=0.7))     # large subunit
    for x, aa, ac, lab in ((4.8, "Met–Phe", "AAG", "P site"), (7.1, "Gly", "CCU", "A site")):
        a.add_patch(Rectangle((x - 0.5, 2.25), 1.0, 2.4, fc="#FCEBD9", ec=AMBER, lw=1.2))
        a.text(x, 2.5, ac, ha="center", fontsize=7.5, family="monospace")
        a.text(x, 4.95, aa, ha="center", fontsize=8, color=RED, weight="bold")
        a.text(x, 6.3, lab, ha="center", fontsize=8, color=BLUE)
    a.text(10.2, 4.6, "peptide bond formed by\nrRNA (ribozyme) in the\nlarge subunit", fontsize=8.5)
    a.text(1.0, 7.6, "Ribosome moves along mRNA codon by codon; tRNAs bring amino acids; a stop codon (UAA) ends it",
           fontsize=8.5, weight="bold")
    label(a, (2.5, 2.0), (1.0, 0.5), "start codon AUG (Met)")
    label(a, (14.0, 2.0), (12.0, 0.5), "stop codon")
    save(fig, "bio_ch05_fig06_translation.png")


if __name__ == "__main__":
    fig01_double_helix()
    fig02_nucleosome()
    fig03_replication_fork()
    fig04_transcription_unit()
    fig05_lac_operon()
    fig06_translation()
