"""Figures for Class XII Chemistry Chapter 9, Amines.
Run: python xii_chem_ch09_amines.py
"""
from xii_chem_common import *


def fig01_pyramidal():
    fig, ax = canvas(9.0, 3.4, (0, 18), (0, 6.8))
    n = (4.5, 3.6)
    atoms = {"N": (n[0], n[1], "N"), "a": (2.4, 2.0, "CH₃"), "b": (6.6, 2.0, "CH₃"), "c": (5.2, 1.3, "CH₃")}
    draw(ax, atoms, [("N", "a", 1), ("N", "b", 1), ("N", "c", "wedge")], fs=12)
    # lone pair lobe
    ax.add_patch(Polygon([(4.25, 4.0), (4.75, 4.0), (5.0, 5.4), (4.0, 5.4)], closed=True, fc=SOFT, ec=BLUE, lw=1.2))
    ax.text(4.5, 4.95, "••", ha="center", va="center", fontsize=14, color=BLUE)
    ax.text(4.5, 0.25, "Trimethylamine: N is sp³; three bonds + one lone pair\n→ pyramidal, C–N–C angle 108°",
            ha="center", fontsize=8.5)
    ax.text(12.8, 3.6, "The lone pair on N makes amines\n• bases (accept H⁺)\n• nucleophiles (attack C of RX, RCOCl)\n"
            "The lone pair occupies more space,\nso the angle is less than 109.5°", fontsize=9, va="center")
    ax.set_title("Pyramidal shape of amines", fontsize=11)
    save(fig, "chem_ch09_fig01_pyramidal.png")


def fig02_aniline():
    fig, ax = canvas(11.0, 3.2, (0, 22), (0, 6.4))
    xs = [2.0, 6.6, 11.2, 15.8]
    specs = [(None, "NH₂", 1, None), ([1, 3], "N⁺H₂", 2, 5), ([1, 4], "N⁺H₂", 2, 3), ([2, 4], "N⁺H₂", 2, 1)]
    for i, (x, (dbl, lab, bond, neg)) in enumerate(zip(xs, specs)):
        pts = ring(ax, x, 2.4, 1.0, aromatic=False, kekule=(dbl is None), doubles=dbl)
        top = pts[0]
        draw(ax, {"r": (top[0], top[1], ""), "N": (top[0], top[1] + 1.25, lab)}, [("r", "N", bond)], fs=11)
        if neg is not None:
            px, py = pts[neg]
            dx, dy = px - x, py - 2.4
            ax.text(px + dx * 0.35, py + dy * 0.35, "−", fontsize=15, color=RED, ha="center", va="center")
        if i < 3:
            ax.text(x + 2.3, 2.4, "↔", fontsize=16, ha="center", va="center")
    ax.text(19.6, 2.6, "The N lone pair is\ndelocalised into the ring:\nless available for H⁺,\nso aniline is a weaker\nbase than alkylamines;\n"
            "o and p carbons become\nelectron-rich", fontsize=8.5, va="center")
    ax.set_title("Resonance in aniline", fontsize=11)
    save(fig, "chem_ch09_fig02_aniline.png")


def fig03_coupling():
    fig, ax = canvas(11.0, 3.0, (0, 22), (0, 6.0))
    p1 = ring(ax, 2.2, 3.0, 0.9)
    draw(ax, {"r": (p1[5][0], p1[5][1], ""), "N": (p1[5][0] + 1.4, p1[5][1] - 0.45, "N₂⁺Cl⁻")}, [("r", "N", 1)], fs=10)
    ax.text(5.6, 3.0, "+", fontsize=16, ha="center", va="center")
    p2 = ring(ax, 7.4, 3.0, 0.9)
    draw(ax, {"r": (p2[5][0], p2[5][1], ""), "O": (p2[5][0] + 1.1, p2[5][1] - 0.35, "OH")}, [("r", "O", 1)], fs=10)
    arrow(ax, (10.0, 3.0), (12.6, 3.0), text="OH⁻", above="273–278 K")
    p3 = ring(ax, 14.0, 3.0, 0.9)
    q = p3[5]
    a = {"r": (q[0], q[1], ""), "N1": (q[0] + 1.0, q[1] - 0.35, "N"), "N2": (q[0] + 2.0, q[1] + 0.05, "N")}
    draw(ax, a, [("r", "N1", 1), ("N1", "N2", 2)], fs=11)
    p4 = ring(ax, q[0] + 3.3, 3.2, 0.9, start=150)
    draw(ax, {"N2": (q[0] + 2.0, q[1] + 0.05, "N"), "s": (p4[0][0], p4[0][1], "")}, [("N2", "s", 1)], fs=11)
    far = p4[3]
    draw(ax, {"f": (far[0], far[1], ""), "O": (far[0] + 1.0, far[1] + 0.2, "OH")}, [("f", "O", 1)], fs=10)
    ax.text(17.0, 0.6, "p-hydroxyazobenzene (orange dye)", ha="center", fontsize=8.5, color=AMBER)
    ax.set_title("Coupling of benzenediazonium chloride with phenol", fontsize=11)
    save(fig, "chem_ch09_fig03_coupling.png")


if __name__ == "__main__":
    fig01_pyramidal()
    fig02_aniline()
    fig03_coupling()
