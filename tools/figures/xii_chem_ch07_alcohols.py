"""Figures for Class XII Chemistry Chapter 7, Alcohols, Phenols and Ethers.
Run: python xii_chem_ch07_alcohols.py
"""
from xii_chem_common import *


def fig01_phenoxide():
    fig, ax = canvas(11.0, 3.2, (0, 22), (0, 6.4))
    xs = [2.0, 6.6, 11.2, 15.8]
    # ring double-bond patterns (edges 0..5 from top vertex anticlockwise) and charge position
    specs = [(None, "O⁻", 1, None), ([1, 3], "O", 2, 5), ([1, 4], "O", 2, 3), ([2, 4], "O", 2, 1)]
    for i, (x, (dbl, lab, bond, neg)) in enumerate(zip(xs, specs)):
        pts = ring(ax, x, 2.4, 1.0, aromatic=False, kekule=(dbl is None), doubles=dbl)
        top = pts[0]
        draw(ax, {"r": (top[0], top[1], ""), "O": (top[0], top[1] + 1.25, lab)}, [("r", "O", bond)], fs=12)
        if neg is not None:
            px, py = pts[neg]
            dx, dy = px - x, py - 2.4
            ax.text(px + dx * 0.35, py + dy * 0.35, "−", fontsize=15, color=RED, ha="center", va="center")
        if i < 3:
            ax.text(x + 2.3, 2.4, "↔", fontsize=16, ha="center", va="center")
    ax.text(19.6, 2.6, "Negative charge spread\nover O and the ortho\nand para carbons:\nphenoxide is stabilised,\nso phenol is acidic", fontsize=8.5,
            va="center")
    ax.set_title("Resonance in the phenoxide ion", fontsize=11)
    save(fig, "chem_ch07_fig01_phenoxide.png")


def fig02_dehydration():
    fig, ax = canvas(11.0, 3.6, (0, 22), (0, 7.2))
    rows = [
        (6.0, "Step 1 (protonation):", "CH₃–CH₂–OH + H⁺  ⇌  CH₃–CH₂–O⁺H₂"),
        (4.2, "Step 2 (slow):", "CH₃–CH₂–O⁺H₂  ⇌  CH₃–C⁺H₂ + H₂O       (carbocation)"),
        (2.4, "Step 3 (loss of H⁺):", "H–CH₂–C⁺H₂  ⇌  CH₂=CH₂ + H⁺"),
    ]
    for y, a, b in rows:
        ax.text(0.4, y, a, fontsize=10, weight="bold", va="center")
        ax.text(6.4, y, b, fontsize=11, va="center")
    ax.text(11.0, 0.7, "Conc. H₂SO₄ at 443 K; the acid used in step 1 is regenerated in step 3 (catalyst). At 413 K, ethoxyethane forms instead.",
            ha="center", fontsize=8.5, color=GREY)
    ax.set_title("Mechanism of acid-catalysed dehydration of ethanol to ethene", fontsize=11)
    save(fig, "chem_ch07_fig02_dehydration.png")


def fig03_nitrophenols():
    fig, ax = canvas(10.0, 3.6, (0, 20), (0, 7.2))
    # ortho: intramolecular H bond
    pts = ring(ax, 4.0, 3.0, 1.1)
    p0, p5 = pts[0], pts[5]
    atoms = {"r0": (p0[0], p0[1], ""), "O": (p0[0], p0[1] + 1.2, "O"), "H": (p0[0] + 1.0, p0[1] + 1.6, "H"),
             "r5": (p5[0], p5[1], ""), "N": (p5[0] + 1.1, p5[1] + 0.3, "N⁺"), "O1": (p5[0] + 2.1, p5[1] - 0.3, "O⁻"),
             "O2": (p5[0] + 1.6, p5[1] + 1.3, "O")}
    draw(ax, atoms, [("r0", "O", 1), ("O", "H", 1), ("r5", "N", 1), ("N", "O1", 1), ("N", "O2", 2), ("H", "O2", "dot")])
    ax.text(4.0, 0.6, "o-nitrophenol: intramolecular H-bond\n(no association; steam volatile)", ha="center", fontsize=8.5)
    # para: intermolecular
    for k, (cx, cy) in enumerate([(12.3, 2.4), (17.3, 4.4)]):
        pts = ring(ax, cx, cy, 0.9)
        top, bot = pts[0], pts[3]
        draw(ax, {"t": (top[0], top[1], ""), "O": (top[0], top[1] + 0.9, "OH"), "b": (bot[0], bot[1], ""),
                  "N": (bot[0], bot[1] - 0.9, "NO₂")}, [("t", "O", 1), ("b", "N", 1)], fs=9)
    ax.plot([12.9, 16.6], [4.3, 2.75], color=BLUE, ls=":", lw=1.6)
    ax.text(14.7, 3.9, "H-bond", fontsize=8, color=BLUE, rotation=-22)
    ax.text(14.9, 6.6, "p-nitrophenol: intermolecular\nH-bonds (associated; not volatile)", ha="center", fontsize=8.5)
    ax.set_title("Hydrogen bonding in nitrophenols", fontsize=11)
    save(fig, "chem_ch07_fig03_nitrophenols.png")


if __name__ == "__main__":
    fig01_phenoxide()
    fig02_dehydration()
    fig03_nitrophenols()
