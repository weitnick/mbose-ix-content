"""Figures for Class XII Chemistry Chapter 6, Haloalkanes and Haloarenes.
Run: python xii_chem_ch06_haloalkanes.py
"""
from xii_chem_common import *


def tet(ax, cx, cy, labels, s=1.0, back="dash", front="wedge", flip=False, fs=11, centre="C"):
    """sp3 carbon: labels = (left, up-right... ) as dict keys 'L','U','D','B'.
    L: in-plane left bond; R: in-plane right bond; W: wedge; H: hash."""
    d = -1 if flip else 1
    pos = {"L": (cx - 1.1 * s * d, cy), "W": (cx + 0.55 * s * d, cy - 0.85 * s), "H": (cx + 0.55 * s * d, cy + 0.85 * s),
           "U": (cx, cy + 1.1 * s)}
    atoms = {"C": (cx, cy, centre)}
    bonds = []
    for k, lab in labels.items():
        atoms[k] = (pos[k][0], pos[k][1], lab)
        kind = {"L": 1, "W": "wedge", "H": "dash", "U": 1}[k]
        bonds.append(("C", k, kind))
    draw(ax, atoms, bonds, fs=fs)


def fig01_sn2():
    fig, ax = canvas(11.0, 3.8, (0, 22), (0, 7.6))
    # reactant: HO- + CH3-Cl ; carbon with H's
    ax.text(0.6, 3.8, "HO⁻", fontsize=12, color=BLUE, va="center")
    arrow(ax, (1.8, 3.8), (3.2, 3.8), color=BLUE, lw=1.2)
    atoms = {"C": (4.6, 3.8, "C"), "X": (6.2, 3.8, "Cl"), "a": (4.1, 5.0, "H"), "b": (3.9, 2.8, "H"), "c": (5.0, 2.6, "H")}
    draw(ax, atoms, [("C", "X", 1), ("C", "a", 1), ("C", "b", "wedge"), ("C", "c", "dash")])
    arrow(ax, (7.2, 3.8), (8.6, 3.8), color=INK, lw=1.4, ms=14)
    # transition state
    ts = {"O": (9.3, 3.8, "HO"), "C": (11.0, 3.8, "C"), "X": (12.7, 3.8, "Cl"), "a": (11.0, 5.2, "H"), "b": (10.5, 2.6, "H"),
          "c": (11.6, 2.6, "H")}
    draw(ax, ts, [("O", "C", "dot"), ("C", "X", "dot"), ("C", "a", 1), ("C", "b", 1), ("C", "c", 1)])
    ax.text(11.0, 6.4, "transition state", ha="center", fontsize=9)
    ax.text(13.6, 5.5, "‡", fontsize=14)
    ax.plot([9.0, 9.0, 13.4, 13.4], [1.9, 6.0, 6.0, 1.9], color=GREY, lw=0.8, ls=":")
    arrow(ax, (14.0, 3.8), (15.4, 3.8), color=INK, lw=1.4, ms=14)
    prod = {"O": (16.6, 3.8, "HO"), "C": (18.2, 3.8, "C"), "a": (18.7, 5.0, "H"), "b": (18.9, 2.8, "H"), "c": (17.8, 2.6, "H")}
    draw(ax, prod, [("O", "C", 1), ("C", "a", 1), ("C", "b", "wedge"), ("C", "c", "dash")])
    ax.text(20.0, 3.8, "+ Cl⁻", fontsize=12, va="center")
    ax.text(11.0, 0.6, "One step: OH⁻ attacks from the side opposite Cl; the C–OH bond forms as C–Cl breaks; configuration is inverted",
            ha="center", fontsize=8.5, color=GREY)
    ax.set_title("SN2 mechanism (rate = k[RX][OH⁻])", fontsize=11)
    save(fig, "chem_ch06_fig01_sn2.png")


def fig02_sn1():
    fig, ax = canvas(11.0, 3.8, (0, 22), (0, 7.6))
    a = {"C": (2.2, 3.8, "C"), "X": (3.9, 3.8, "Br"), "m1": (1.4, 5.0, "CH₃"), "m2": (1.0, 3.0, "CH₃"), "m3": (2.4, 2.4, "CH₃")}
    draw(ax, a, [("C", "X", 1), ("C", "m1", 1), ("C", "m2", 1), ("C", "m3", 1)], fs=10)
    arrow(ax, (5.0, 3.8), (7.2, 3.8), color=INK, lw=1.4, ms=14)
    ax.text(6.1, 4.2, "slow", ha="center", fontsize=9)
    ax.text(6.1, 3.2, "step I", ha="center", fontsize=8.5, color=GREY)
    b = {"C": (9.4, 3.8, "C⁺"), "m1": (9.4, 5.3, "CH₃"), "m2": (8.0, 3.0, "CH₃"), "m3": (10.8, 3.0, "CH₃")}
    draw(ax, b, [("C", "m1", 1), ("C", "m2", 1), ("C", "m3", 1)], fs=10)
    ax.text(9.4, 1.6, "planar 3° carbocation\n+ Br⁻", ha="center", fontsize=8.5)
    arrow(ax, (12.0, 3.8), (14.2, 3.8), color=INK, lw=1.4, ms=14)
    ax.text(13.1, 4.2, "fast, OH⁻", ha="center", fontsize=9)
    ax.text(13.1, 3.2, "step II", ha="center", fontsize=8.5, color=GREY)
    c = {"C": (16.6, 3.8, "C"), "X": (18.3, 3.8, "OH"), "m1": (15.8, 5.0, "CH₃"), "m2": (15.4, 3.0, "CH₃"),
         "m3": (16.8, 2.4, "CH₃")}
    draw(ax, c, [("C", "X", 1), ("C", "m1", 1), ("C", "m2", 1), ("C", "m3", 1)], fs=10)
    ax.text(11.0, 0.5, "Two steps; rate = k[(CH₃)₃CBr]. OH⁻ can attack the flat carbocation from either face: a chiral substrate is racemised",
            ha="center", fontsize=8.5, color=GREY)
    ax.set_title("SN1 mechanism: (CH₃)₃C–Br + OH⁻ → (CH₃)₃C–OH + Br⁻", fontsize=11)
    save(fig, "chem_ch06_fig02_sn1.png")


def fig03_resonance():
    fig, ax = canvas(11.0, 3.0, (0, 22), (0, 6))
    xs = [2.2, 7.0, 11.8, 16.6, 20.6]
    # five canonical structures, simplified: Cl single bond (I), C=Cl+ with negative at o, p, o'
    labels = ["Cl", "Cl⁺", "Cl⁺", "Cl⁺", "Cl"]
    neg = [None, 120, 0, 240, None]
    for i, x in enumerate(xs):
        if i == 4:
            continue
        dbl = [None, [1, 3], [1, 4], [2, 4]][i]
        pts = ring(ax, x, 2.6, 1.0, aromatic=False, kekule=(i == 0), doubles=dbl)
        top = pts[0]
        bond = 1 if i == 0 else 2
        draw(ax, {"r": (top[0], top[1], ""), "X": (top[0], top[1] + 1.2, labels[i])}, [("r", "X", bond)], fs=11)
        if neg[i] is not None:
            ang = np.radians(90 - (60 if neg[i] == 120 else (180 if neg[i] == 0 else 300)))
            px, py = x + 1.35 * np.cos(ang), 2.6 + 1.35 * np.sin(ang)
            ax.text(px, py, "−", fontsize=14, color=RED, ha="center", va="center")
        if i < 3:
            ax.text(x + 2.4, 2.6, "↔", fontsize=16, ha="center", va="center")
    ax.text(19.6, 2.6, "C–Cl has partial\ndouble-bond character:\nshorter (169 pm), stronger,\nhard to break", fontsize=8.5, va="center")
    ax.set_title("Resonance in chlorobenzene (negative charge at ortho and para positions)", fontsize=10)
    save(fig, "chem_ch06_fig03_resonance.png")


def fig04_enantiomers():
    fig, ax = canvas(8.0, 3.6, (0, 16), (0, 7.2))
    tet(ax, 4.0, 3.6, {"U": "Br", "L": "CH₃", "W": "H", "H": "C₂H₅"}, s=1.4)
    tet(ax, 12.0, 3.6, {"U": "Br", "L": "CH₃", "W": "H", "H": "C₂H₅"}, s=1.4, flip=True)
    ax.plot([8, 8], [0.8, 6.6], color=GREY, ls="--")
    ax.text(8, 6.8, "mirror", ha="center", fontsize=8.5, color=GREY)
    ax.text(8, 0.2, "Butan-2-ol and 2-bromobutane have a chiral carbon (four different groups): two enantiomers", ha="center",
            fontsize=8.5, color=GREY)
    ax.set_title("Enantiomers of 2-bromobutane", fontsize=11)
    save(fig, "chem_ch06_fig04_enantiomers.png")


if __name__ == "__main__":
    fig01_sn2()
    fig02_sn1()
    fig03_resonance()
    fig04_enantiomers()
