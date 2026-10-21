"""Figures for Class XII Physics Chapter 13, Nuclei.
Run: python xii_phy_ch13_nuclei.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Physics", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, POS, NEG, ACC, GREY, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#E9F0F7"
GREEN = "#2E7D32"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def arrow(ax, p0, p1, color=INK, lw=1.6, ms=12, style="-|>"):
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle=style, mutation_scale=ms, color=color, lw=lw, shrinkA=0, shrinkB=0))


def semf(A):
    """Semi-empirical binding energy per nucleon (MeV), Z near stability."""
    A = np.asarray(A, float)
    Z = A / (1.98 + 0.0155 * A ** (2.0 / 3.0))
    B = 15.75 * A - 17.8 * A ** (2 / 3) - 0.711 * Z * (Z - 1) / A ** (1 / 3) - 23.7 * (A - 2 * Z) ** 2 / A
    return B / A


# ---- Fig 13.1: binding energy per nucleon -----------------------------------------------------
def fig_be_curve():
    fig, ax = plt.subplots(figsize=(8.2, 4.4))
    A = np.linspace(12, 240, 300)
    ax.plot(A, semf(A), color=POS, lw=2)
    light = [(2, 1.11, "²H"), (3, 2.83, "³He"), (4, 7.07, "⁴He"), (6, 5.33, "⁶Li"), (7, 5.61, "⁷Li"), (9, 6.46, "⁹Be"), (12, 7.68, "¹²C"), (16, 7.98, "¹⁶O")]
    xs = [p[0] for p in light]
    ys = [p[1] for p in light]
    ax.plot(xs + [20, 30], ys + [8.03, 8.4], color=POS, lw=1.2, ls="--")
    for a, b, lab in light + [(56, 8.79, "⁵⁶Fe"), (100, 8.6, "¹⁰⁰Mo"), (238, 7.57, "²³⁸U")]:
        ax.plot([a], [b], "o", color=NEG, ms=4)
        if lab in ("³He", "⁶Li", "⁷Li", "⁹Be", "¹²C"):
            continue
        ax.text(a + 3, b - 0.1, lab, fontsize=8.5, color=NEG, va="center")
    ax.annotate("maximum ≈ 8.75 MeV near A = 56", (56, 8.79), (75, 9.6), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=GREY))
    ax.annotate("", (50, 4.0), (15, 4.0), arrowprops=dict(arrowstyle="->", color=GREEN, lw=2))
    ax.text(17, 3.5, "fusion releases energy", fontsize=8.5, color=GREEN)
    ax.annotate("", (150, 5.5), (230, 5.5), arrowprops=dict(arrowstyle="->", color=ACC, lw=2))
    ax.text(160, 5.0, "fission releases energy", fontsize=8.5, color=ACC)
    ax.text(70, 7.3, "nearly constant (about 8 MeV) for 30 < A < 170", fontsize=8.5, color=GREY)
    ax.set_xlim(0, 250)
    ax.set_ylim(0, 10)
    ax.set_xlabel("mass number A", fontsize=9)
    ax.set_ylabel("binding energy per nucleon (MeV)", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "phy_ch13_fig01_be_curve.png")


# ---- Fig 13.2: potential energy of two nucleons -----------------------------------------------
def fig_potential():
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    r = np.linspace(0.45, 3.5, 300)
    r0 = 0.8
    U = 100 * ((r0 / r) ** 8 - 2 * (r0 / r) ** 4) * np.exp(-(r - r0) / 1.6) * 0.9
    ax.plot(r, U, color=NEG, lw=2)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.axvline(r0, color=GREY, lw=0.8, ls=":")
    ax.set_ylim(-110, 150)
    ax.set_xlim(0, 3.6)
    ax.text(r0 + 0.05, 110, "$r_0$ ≈ 0.8 fm", fontsize=9)
    ax.text(0.15, 60, "repulsive", fontsize=9, color=POS)
    ax.text(1.4, -60, "attractive", fontsize=9, color=GREEN)
    ax.text(2.4, 15, "negligible beyond\na few fm", fontsize=8.5, color=GREY)
    ax.set_xlabel("separation r (fm)", fontsize=9)
    ax.set_ylabel("potential energy (MeV)", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "phy_ch13_fig02_potential.png")


# ---- Fig 13.3: a fission chain reaction --------------------------------------------------------
def fig_chain():
    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-3.4, 3.3)
    ax.set_aspect("equal")
    ax.axis("off")

    def nucleus(x, y, r=0.38, col="#C9D6E3", lab="²³⁵U"):
        ax.add_patch(Circle((x, y), r, fc=col, ec=NEG, lw=1.2))
        ax.text(x, y, lab, fontsize=7.5, ha="center", va="center")

    def neutron(x0, y0, x1, y1):
        arrow(ax, (x0, y0), (x1, y1), INK, lw=1.0, ms=8)
        ax.plot([x0], [y0], "o", color=INK, ms=3)

    neutron(-0.3, 0, 0.55, 0)
    nucleus(1.0, 0)
    gen1 = [(3.4, 2.1), (3.4, 0), (3.4, -2.1)]
    for (x, y) in gen1:
        neutron(1.4, 0, x - 0.45, y)
        nucleus(x, y)
    ax.add_patch(Circle((2.0, 0.75), 0.25, fc="#F3D9D5", ec=POS))
    ax.add_patch(Circle((2.0, -0.75), 0.22, fc="#F3D9D5", ec=POS))
    ax.text(2.0, 1.15, "fragment", fontsize=7, ha="center", color=POS)
    for (x, y) in gen1:
        for dy in (0.62, 0, -0.62):
            tx, ty = x + 2.6, y + dy
            neutron(x + 0.4, y, tx - 0.4, ty)
            nucleus(tx, ty, r=0.27)
    ax.text(1.0, -1.0, "1 neutron", fontsize=8.5, ha="center")
    ax.text(3.4, -2.75, "3 neutrons", fontsize=8.5, ha="center")
    ax.text(6.0, -3.3, "9 neutrons", fontsize=8.5, ha="center")
    ax.text(8.4, 0.0, "… and so on:\nthe number of\nfissions multiplies", fontsize=9, va="center")
    fig.tight_layout()
    save(fig, "phy_ch13_fig03_chain.png")


if __name__ == "__main__":
    fig_be_curve()
    fig_potential()
    fig_chain()
