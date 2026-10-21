"""Figures for Class XII Chemistry Chapter 10, Biomolecules.
Run: python xii_chem_ch10_biomolecules.py
"""
from xii_chem_common import *


def fig01_glucose():
    fig, ax = canvas(10.0, 4.4, (0, 20), (0, 8.8))
    # Fischer projection of D-glucose
    x = 3.0
    rows = [("CHO", None, None), ("C", "H", "OH"), ("C", "HO", "H"), ("C", "H", "OH"), ("C", "H", "OH"), ("CH₂OH", None, None)]
    ys = [7.6, 6.4, 5.2, 4.0, 2.8, 1.6]
    for i, ((c, l, r), y) in enumerate(zip(rows, ys)):
        ax.text(x, y, c, ha="center", va="center", fontsize=11, bbox=dict(fc="white", ec="none", pad=0.3))
        if l:
            ax.plot([x - 1.2, x - 0.3], [y, y], color=INK, lw=1.4)
            ax.plot([x + 0.3, x + 1.2], [y, y], color=INK, lw=1.4)
            ax.text(x - 1.6, y, l, ha="center", va="center", fontsize=10)
            ax.text(x + 1.7, y, r, ha="center", va="center", fontsize=10)
        if i < 5:
            ax.plot([x, x], [y - 0.35, ys[i + 1] + 0.35], color=INK, lw=1.4)
    ax.text(x, 0.5, "D-glucose (open chain)", ha="center", fontsize=9)
    ax.text(x + 2.6, 2.8, "← C-5 OH on right: D", fontsize=8, color=BLUE, va="center")
    # Haworth projection of alpha-D-glucopyranose
    x0, y0 = 11.5, 4.8
    P = {"C5": (x0, y0 + 0.8), "O": (x0 + 1.8, y0 + 0.8), "C1": (x0 + 3.1, y0 - 0.1), "C2": (x0 + 2.1, y0 - 1.0),
         "C3": (x0 - 0.5, y0 - 1.0), "C4": (x0 - 1.5, y0 - 0.1)}
    order = ["C5", "O", "C1", "C2", "C3", "C4", "C5"]
    for a, b in zip(order, order[1:]):
        lw = 3.2 if (a, b) in [("C1", "C2"), ("C2", "C3"), ("C3", "C4")] else 1.5
        ax.plot([P[a][0], P[b][0]], [P[a][1], P[b][1]], color=INK, lw=lw, solid_capstyle="round")
    ax.text(P["O"][0], P["O"][1] + 0.05, "O", ha="center", va="center", fontsize=11, color=RED,
            bbox=dict(fc="white", ec="none", pad=0.2))
    # simplified Haworth: only OH, CH2OH and the anomeric H are shown
    subs = [("C1", "up", "H", INK), ("C1", "dn", "OH", RED), ("C2", "dn", "OH", INK), ("C3", "up", "OH", INK),
            ("C4", "dn", "OH", INK), ("C5", "up", "CH₂OH", INK)]
    for k, d, lab, col in subs:
        cx, cy = P[k]
        sgn = 1 if d == "up" else -1
        ax.plot([cx, cx], [cy, cy + sgn * 0.9], color=INK, lw=1.2)
        ax.text(cx, cy + sgn * 1.2, lab, ha="center", va="center", fontsize=9.5, color=col)
    for k, lab in [("C1", "1"), ("C2", "2"), ("C3", "3"), ("C4", "4"), ("C5", "5")]:
        cx, cy = P[k]
        ax.text(cx + 0.25, cy - 0.35, lab, fontsize=7, color=GREY)
    ax.text(x0 + 1.0, 0.5, "α-D-glucopyranose: OH on C-1 down (β: up)\nC-1 is the anomeric carbon", ha="center", fontsize=9)
    ax.set_title("Glucose: open-chain (Fischer) and cyclic (Haworth) structures", fontsize=11)
    save(fig, "chem_ch10_fig01_glucose.png")


def fig02_peptide():
    fig, ax = canvas(10.5, 2.6, (0, 21), (0, 5.2))
    ax.text(0.3, 3.4, "H₂N–CH₂–COOH  +  H₂N–CH(CH₃)–COOH", fontsize=11, va="center")
    ax.text(1.6, 2.5, "glycine", fontsize=8.5, color=GREY)
    ax.text(6.6, 2.5, "alanine", fontsize=8.5, color=GREY)
    arrow(ax, (11.2, 3.4), (12.8, 3.4), above="−H₂O")
    ax.text(13.1, 3.4, "H₂N–CH₂–", fontsize=11, va="center")
    ax.text(15.45, 3.4, "CO–NH", fontsize=11, va="center", color=RED,
            bbox=dict(fc=SOFT, ec=RED, boxstyle="round,pad=0.25"))
    ax.text(17.35, 3.4, "–CH(CH₃)–COOH", fontsize=11, va="center")
    ax.text(16.1, 1.9, "peptide linkage (amide bond)", fontsize=8.5, color=RED, ha="center")
    ax.text(16.1, 0.9, "glycylalanine (Gly-Ala), a dipeptide", fontsize=9, ha="center")
    ax.set_title("Formation of a peptide bond", fontsize=11)
    save(fig, "chem_ch10_fig02_peptide.png")


def fig03_dna_pairs():
    fig, ax = canvas(9.0, 4.0, (0, 18), (0, 8.0))
    xl, xr = 3.0, 11.0
    for xx in (xl, xr):
        ax.plot([xx, xx], [0.8, 7.2], color=BLUE, lw=4, solid_capstyle="round")
    ax.text(xl, 7.6, "5′", ha="center", fontsize=9)
    ax.text(xl, 0.35, "3′", ha="center", fontsize=9)
    ax.text(xr, 7.6, "3′", ha="center", fontsize=9)
    ax.text(xr, 0.35, "5′", ha="center", fontsize=9)
    pairs = [("A", "T", 2), ("G", "C", 3), ("T", "A", 2), ("C", "G", 3), ("A", "T", 2)]
    for i, (l, r, n) in enumerate(pairs):
        y = 6.4 - i * 1.25
        ax.plot([xl, 5.6], [y, y], color=INK, lw=1.4)
        ax.plot([8.4, xr], [y, y], color=INK, lw=1.4)
        ax.text(6.0, y, l, ha="center", va="center", fontsize=11, weight="bold",
                bbox=dict(fc="#FDF2E0", ec=AMBER, boxstyle="round,pad=0.2"))
        ax.text(8.0, y, r, ha="center", va="center", fontsize=11, weight="bold",
                bbox=dict(fc="#E8F3E8", ec=GREEN, boxstyle="round,pad=0.2"))
        for k in range(n):
            yy = y + (k - (n - 1) / 2) * 0.16
            ax.plot([6.35, 7.65], [yy, yy], color=RED, lw=1.0, ls=(0, (1.5, 1.5)))
    ax.text(14.6, 4.0, "Sugar–phosphate backbones\nrun in opposite directions.\n\nA pairs with T (2 H-bonds)\n"
            "G pairs with C (3 H-bonds)\n\nSo the two strands are\ncomplementary, not identical.", ha="center", va="center",
            fontsize=8.8)
    ax.set_title("Complementary base pairing in DNA", fontsize=11)
    save(fig, "chem_ch10_fig03_dna_pairs.png")


if __name__ == "__main__":
    fig01_glucose()
    fig02_peptide()
    fig03_dna_pairs()
