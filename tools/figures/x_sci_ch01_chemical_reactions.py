"""Figures for Class X Science, Chapter 1: Chemical Reactions and Equations.
Run: python x_sci_ch01_chemical_reactions.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Science", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, SHADE = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#BFD3E6"
WATER, BLUE, RUST, FLAME = "#D6E9F8", "#5B9BD5", "#A0522D", "#F4A300"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def label(ax, xy, text, xytext, ha="left"):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=9, color=INK, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8), annotation_clip=False)


def test_tube(ax, x, y_top, y_bot, w, fill_to=None, fill=WATER, inverted=False, ec=INK):
    """A test tube with a round end. Upright: open at y_top, round end at y_bot. Inverted: the reverse."""
    r = w / 2
    if not inverted:
        ax.plot([x - r, x - r], [y_top, y_bot + r], color=ec, lw=1.3)
        ax.plot([x + r, x + r], [y_top, y_bot + r], color=ec, lw=1.3)
        t = np.linspace(np.pi, 2 * np.pi, 40)
        ax.plot(x + r * np.cos(t), y_bot + r + r * np.sin(t), color=ec, lw=1.3)
        if fill_to is not None:
            t2 = np.linspace(np.pi, 2 * np.pi, 40)
            xs = list(x + r * np.cos(t2)) + [x + r, x - r]
            ys = list(y_bot + r + r * np.sin(t2)) + [fill_to, fill_to]
            ax.add_patch(Polygon(np.c_[xs, ys], closed=True, fc=fill, ec="none", zorder=0))
    else:
        ax.plot([x - r, x - r], [y_bot, y_top - r], color=ec, lw=1.3)
        ax.plot([x + r, x + r], [y_bot, y_top - r], color=ec, lw=1.3)
        t = np.linspace(0, np.pi, 40)
        ax.plot(x + r * np.cos(t), y_top - r + r * np.sin(t), color=ec, lw=1.3)


# Fig 1.1: electrolysis of water
def fig_electrolysis():
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    # mug
    ax.add_patch(Polygon([[0.6, 3.6], [1.0, 0.6], [5.0, 0.6], [5.4, 3.6]], closed=True, fc="none", ec=INK, lw=1.5))
    ax.add_patch(Polygon([[0.65, 3.2], [1.0, 0.62], [5.0, 0.62], [5.35, 3.2]], closed=True, fc=WATER, ec="none", zorder=0))
    # electrodes through the base
    for xe in (2.1, 3.9):
        ax.add_patch(Rectangle((xe - 0.09, 0.2), 0.18, 1.5, fc="#3A3A3A", ec=INK, zorder=3))
    # inverted tubes over the electrodes: hydrogen tube (left) has twice the gas
    tube_top, tube_bot, w = 4.0, 1.2, 0.7
    for xe, gas_to, name in ((2.1, 2.2, "hydrogen"), (3.9, 2.93, "oxygen")):
        ax.add_patch(Rectangle((xe - w / 2, tube_bot), w, gas_to - tube_bot, fc=WATER, ec="none", zorder=1))
        test_tube(ax, xe, tube_top, tube_bot, w, inverted=True)
        ax.add_patch(Rectangle((xe - w / 2 + 0.02, gas_to), w - 0.04, tube_top - 0.35 - gas_to, fc="white", ec="none", zorder=1))
        for k in range(4):
            ax.add_patch(Ellipse((xe + 0.12 * ((-1) ** k), 1.85 + 0.08 * k), 0.08, 0.08, fc="white", ec=ACC, lw=0.6, zorder=4))
    # wires and battery
    ax.plot([2.1, 2.1, 2.6], [0.2, -0.4, -0.4], color=INK, lw=1.2)
    ax.plot([3.9, 3.9, 3.4], [0.2, -0.4, -0.4], color=INK, lw=1.2)
    ax.plot([2.6, 2.6], [-0.15, -0.65], color=INK, lw=2.4)
    ax.plot([2.8, 2.8], [-0.25, -0.55], color=INK, lw=1.2)
    ax.plot([3.2, 3.2], [-0.15, -0.65], color=INK, lw=2.4)
    ax.plot([3.4, 3.4], [-0.25, -0.55], color=INK, lw=1.2)
    ax.plot([2.8, 3.2], [-0.4, -0.4], color=INK, lw=1.0, ls=":")
    ax.text(3.0, -0.95, "6 V battery", ha="center", fontsize=9, color=INK)
    label(ax, (2.1 - 0.35, 3.0), "hydrogen gas\n(twice the volume)", (-0.4, 4.3), ha="left")
    label(ax, (3.9 + 0.35, 3.5), "oxygen gas", (5.7, 4.3), ha="left")
    label(ax, (2.0, 0.35), "carbon electrode\n(cathode, −)", (-0.6, -0.2))
    label(ax, (4.1, 0.9), "carbon electrode\n(anode, +)", (5.7, 0.5))
    label(ax, (5.1, 2.6), "water with a little\ndilute sulphuric acid", (5.7, 2.4))
    label(ax, (0.75, 3.3), "plastic mug", (-0.5, 2.6))
    ax.set_xlim(-0.6, 7.2)
    ax.set_ylim(-1.2, 4.7)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "sci_ch01_fig01_electrolysis.png")


# Fig 1.2: heating ferrous sulphate crystals
def fig_heating_ferrous_sulphate():
    fig, ax = plt.subplots(figsize=(5.2, 3.8))
    # boiling tube held at an angle
    ang = np.radians(35)
    d = np.array([np.cos(ang), np.sin(ang)])
    n = np.array([-np.sin(ang), np.cos(ang)])
    base = np.array([1.6, 1.2])
    L, w = 3.4, 0.5
    p1, p2 = base + n * w / 2, base - n * w / 2
    ax.plot(*zip(p1, p1 + d * L), color=INK, lw=1.4)
    ax.plot(*zip(p2, p2 + d * L), color=INK, lw=1.4)
    t = np.linspace(np.pi / 2, 3 * np.pi / 2, 30)
    arc = np.array([base + (w / 2) * (np.cos(tt) * d + np.sin(tt) * n) for tt in t])
    ax.plot(arc[:, 0], arc[:, 1], color=INK, lw=1.4)
    # crystals at the closed end
    crys = [base + d * s + n * o for s, o in ((0.0, 0.0), (0.18, 0.1), (0.2, -0.12), (0.38, 0.02), (0.05, -0.15))]
    for c in crys:
        ax.add_patch(Polygon([c + [-0.07, -0.05], c + [0.07, -0.05], c + [0.0, 0.08]], closed=True, fc="#7FB77E", ec="#3E7B3D", lw=0.6))
    # tongs/holder
    hold = base + d * 2.6
    ax.plot([hold[0], hold[0] + 1.3], [hold[1], hold[1] - 0.2], color=GREY, lw=3)
    # burner and flame
    ax.add_patch(Rectangle((1.25, -0.8), 0.5, 1.0, fc=SHADE, ec=INK, lw=1.2))
    ax.add_patch(Rectangle((0.95, -1.0), 1.1, 0.2, fc=SHADE, ec=INK, lw=1.2))
    ax.add_patch(Polygon([[1.3, 0.2], [1.5, 1.0], [1.7, 0.2]], closed=True, fc=FLAME, ec="#C46A00", lw=0.8))
    # fumes from the mouth
    mouth = base + d * L
    for k in range(3):
        xs = mouth[0] + 0.15 * k + 0.25 * np.sin(np.linspace(0, 3, 20))
        ys = mouth[1] + 0.2 + np.linspace(0, 0.9, 20) + 0.1 * k
        ax.plot(xs, ys, color=GREY, lw=0.9)
    label(ax, crys[1], "ferrous sulphate crystals\n(green → brown residue)", (-1.2, 2.3))
    label(ax, base + d * 1.5 + n * 0.25, "dry boiling tube", (0.6, 3.6))
    label(ax, (1.5, 0.6), "burner flame", (-1.2, 0.5))
    label(ax, (mouth[0] + 0.3, mouth[1] + 0.8), "SO₂ and SO₃ gases\n(smell of burning sulphur)", (5.2, 3.4))
    label(ax, (hold[0] + 1.0, hold[1] - 0.15), "test-tube holder", (5.0, 2.4))
    ax.set_xlim(-1.3, 6.6)
    ax.set_ylim(-1.1, 4.7)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "sci_ch01_fig02_heating_ferrous_sulphate.png")


# Fig 1.3: iron nails in copper sulphate solution, compared after 20 minutes
def fig_iron_nails():
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    test_tube(ax, 1.2, 3.4, 0.2, 0.9, fill_to=2.4, fill="#4A90D9")
    test_tube(ax, 3.9, 3.4, 0.2, 0.9, fill_to=2.4, fill="#A9C9A4")
    # nails in B, coated brown
    for dx in (-0.12, 0.12):
        ax.plot([3.9 + dx, 3.9 + dx], [0.55, 3.6], color=RUST, lw=3.2, solid_capstyle="butt")
        ax.plot([3.9 + dx - 0.1, 3.9 + dx + 0.1], [3.6, 3.6], color=RUST, lw=3)
    ax.plot([3.75, 4.05], [3.35, 3.35], color=GREY, lw=1.0)
    # nail kept aside
    ax.plot([6.3, 6.3], [0.4, 2.6], color="#6E6E6E", lw=3.2)
    ax.plot([6.2, 6.4], [2.6, 2.6], color="#6E6E6E", lw=3)
    ax.text(1.2, -0.25, "(A) copper sulphate\nsolution only:\nstays blue", ha="center", va="top", fontsize=9, color=INK)
    ax.text(3.9, -0.25, "(B) iron nails dipped\nfor 20 minutes: colour\nfades, nails turn brown", ha="center", va="top", fontsize=9, color=INK)
    ax.text(6.3, -0.25, "nail kept\naside: grey", ha="center", va="top", fontsize=9, color=INK)
    label(ax, (4.02, 3.35), "thread", (4.9, 3.8))
    ax.set_xlim(-0.1, 7.3)
    ax.set_ylim(-1.3, 4.0)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "sci_ch01_fig03_iron_nails.png")


# Fig 1.4: the types of chemical reactions
def fig_types_map():
    fig, ax = plt.subplots(figsize=(7.2, 4.6))

    def box(x, y, w, h, title, body, fc):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.12", fc=fc, ec=ACC, lw=1.1))
        ax.text(x + w / 2, y + h - 0.22, title, ha="center", va="top", fontsize=9.5, color=INK, fontweight="bold")
        ax.text(x + w / 2, y + h - 0.65, body, ha="center", va="top", fontsize=8.2, color=INK, linespacing=1.35)

    ax.add_patch(FancyBboxPatch((2.0, 4.6), 3.8, 0.6, boxstyle="round,pad=0.04,rounding_size=0.12", fc=HI, ec=INK, lw=1.1))
    ax.text(3.9, 4.9, "Types of chemical reactions", ha="center", va="center", fontsize=10.5, color="white", fontweight="bold")
    w = 2.5
    ax.plot([w / 2, 5.3 + w / 2], [4.4, 4.4], color=GREY, lw=0.9)
    ax.plot([3.9, 3.9], [4.4, 4.6], color=GREY, lw=0.9)
    items = [
        (0.0, 2.3, "Combination", "A + B \u2192 AB\nCaO + H\u2082O \u2192 Ca(OH)\u2082", SOFT),
        (2.65, 2.3, "Decomposition", "AB \u2192 A + B\nby heat, light or\nelectricity", SOFT),
        (5.3, 2.3, "Displacement", "A + BC \u2192 AC + B\nFe + CuSO\u2084 \u2192\nFeSO\u2084 + Cu", SOFT),
        (0.0, 0.0, "Double displacement", "AB + CD \u2192 AD + CB\nNa\u2082SO\u2084 + BaCl\u2082 \u2192\nBaSO\u2084\u2193 + 2NaCl", SHADE),
        (2.65, 0.0, "Redox", "oxidation: gain of O\nor loss of H\nreduction: loss of O\nor gain of H", SHADE),
        (5.3, 0.0, "Heat change", "exothermic:\nheat given out\nendothermic:\nenergy absorbed", SHADE),
    ]
    for x, y, t, b, fc in items:
        box(x, y, w, 1.95, t, b, fc)
        if y > 1:
            ax.plot([x + w / 2, x + w / 2], [4.4, 4.3], color=GREY, lw=0.9)
    ax.set_xlim(-0.2, 8.0)
    ax.set_ylim(-0.2, 5.35)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "sci_ch01_fig04_types_map.png")


if __name__ == "__main__":
    fig_electrolysis()
    fig_heating_ferrous_sulphate()
    fig_iron_nails()
    fig_types_map()
