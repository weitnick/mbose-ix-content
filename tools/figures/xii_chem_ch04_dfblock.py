"""Figures for Class XII Chemistry Chapter 4, The d- and f-Block Elements.
Run: python xii_chem_ch04_dfblock.py
"""
from xii_chem_common import *


def fig01_radii():
    s3 = ["Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
    r3 = [164, 147, 135, 129, 137, 126, 125, 125, 128, 137]
    r4 = [180, 160, 147, 140, 135, 134, 134, 137, 144, 154]
    r5 = [187, 159, 147, 141, 137, 135, 136, 139, 144, 157]
    x = np.arange(10)
    fig, ax = plt.subplots(figsize=(6.4, 3.9))
    ax.plot(x, r3, "o-", color=BLUE, label="3d series (Sc–Zn)")
    ax.plot(x, r4, "s-", color=RED, label="4d series (Y–Cd)")
    ax.plot(x, r5, "^-", color=GREEN, label="5d series (La, Hf–Hg)")
    ax.set_xticks(x)
    ax.set_xticklabels(["3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
    ax.set_xlabel("Group")
    ax.set_ylabel("Metallic radius / pm")
    ax.set_title("Atomic radii of the transition metals")
    ax.text(3.3, 168, "4d and 5d radii almost equal\n(lanthanoid contraction)", fontsize=8.5)
    ax.legend(frameon=False, fontsize=8.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "chem_ch04_fig01_radii.png")


def fig02_lanthanoid():
    el = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
    r = [103, 102, 99, 98.3, 97, 95.8, 94.7, 93.8, 92.3, 91.2, 90.1, 89, 88, 86.8, 86.1]
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(range(15), r, "o-", color=RED)
    ax.set_xticks(range(15))
    ax.set_xticklabels(el, fontsize=8.5)
    ax.set_ylabel("Ln³⁺ ionic radius / pm")
    ax.set_title("Lanthanoid contraction: steady decrease in Ln³⁺ radius")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "chem_ch04_fig02_lanthanoid.png")


def fig03_oxoanions():
    fig, ax = canvas(10.4, 5.4, (0, 21), (0, 10.5))
    # chromate
    tetra(ax, 2.6, 7.6, "Cr", ["O", "O⁻", "O⁻", "O"], r=1.25, bonds=[2, 1, 1, 2])
    ax.text(2.6, 5.4, "chromate, CrO₄²⁻\n(tetrahedral, yellow)", ha="center", fontsize=9)
    # dichromate
    atoms = {"Cr1": (8.0, 7.6, "Cr"), "Cr2": (11.6, 7.6, "Cr"), "Ob": (9.8, 6.8, "O"),
             "a1": (8.0, 9.2, "O"), "a2": (6.5, 7.6, "O⁻"), "a3": (8.0, 6.0, "O"),
             "b1": (11.6, 9.2, "O"), "b2": (13.1, 7.6, "O⁻"), "b3": (11.6, 6.0, "O")}
    draw(ax, atoms, [("Cr1", "Ob", 1), ("Ob", "Cr2", 1), ("Cr1", "a1", 2), ("Cr1", "a2", 1), ("Cr1", "a3", 2),
                     ("Cr2", "b1", 2), ("Cr2", "b2", 1), ("Cr2", "b3", 2)])
    ax.text(9.8, 4.3, "dichromate, Cr₂O₇²⁻ (orange)\ntwo tetrahedra sharing one O;\nCr–O–Cr angle 126°", ha="center", fontsize=9)
    # manganate
    tetra(ax, 17.0, 7.6, "Mn", ["O", "O⁻", "O⁻", "O"], r=1.25, bonds=[2, 1, 1, 2])
    ax.text(17.0, 5.4, "manganate, MnO₄²⁻\n(tetrahedral, green, paramagnetic)", ha="center", fontsize=9)
    # permanganate
    tetra(ax, 6.0, 2.4, "Mn", ["O", "O", "O⁻", "O"], r=1.25, bonds=[2, 2, 1, 2])
    ax.text(6.0, 0.25, "permanganate, MnO₄⁻\n(tetrahedral, purple, diamagnetic)", ha="center", fontsize=9)
    ax.text(14.5, 2.6, "In each ion the metal is surrounded\ntetrahedrally by four O atoms;\nthe charge is spread over the\nterminal O atoms (resonance).", ha="center", fontsize=9, color=GREY)
    save(fig, "chem_ch04_fig03_oxoanions.png")


if __name__ == "__main__":
    fig01_radii()
    fig02_lanthanoid()
    fig03_oxoanions()
