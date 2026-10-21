"""Figures for Class X Science, Chapter 4: Carbon and its Compounds.
Run: python x_sci_ch04_carbon.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Science", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, SHADE = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#BFD3E6"
WATER, FLAME = "#D6E9F8", "#F4A300"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def finish(ax, xl, yl):
    ax.set_xlim(*xl)
    ax.set_ylim(*yl)
    ax.set_aspect("equal")
    ax.axis("off")


def label(ax, xy, text, xytext, ha="left", size=9):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=size, color=INK, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8), annotation_clip=False)


# ---- structural formulas ---------------------------------------------------------------
def mol(ax, atoms, bonds, dx=0.0, dy=0.0, size=11, gap=0.2):
    """atoms: list of (x, y, symbol); bonds: list of (i, j, order)."""
    pts = [(x + dx, y + dy, s) for x, y, s in atoms]
    for i, j, order in bonds:
        x1, y1, s1 = pts[i]
        x2, y2, s2 = pts[j]
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        g1 = gap * (1.0 if s1 else 0.0) + (0.1 if len(s1) > 1 else 0.0)
        g2 = gap * (1.0 if s2 else 0.0) + (0.1 if len(s2) > 1 else 0.0)
        ax_, ay_ = x1 + ux * g1, y1 + uy * g1
        bx_, by_ = x2 - ux * g2, y2 - uy * g2
        offs = {1: [0.0], 2: [-0.055, 0.055], 3: [-0.08, 0.0, 0.08]}[order]
        for o in offs:
            ax.plot([ax_ - uy * o, bx_ - uy * o], [ay_ + ux * o, by_ + ux * o], color=INK, lw=1.1, solid_capstyle="round")
    for x, y, s in pts:
        if s:
            col = INK if s in ("C", "H") else ACC
            ax.text(x, y, s, ha="center", va="center", fontsize=size, color=col, fontweight="bold" if s != "H" else "normal")


def chain(n, skeleton=False):
    """A straight alkane chain C_nH_(2n+2), returned as (atoms, bonds)."""
    atoms, bonds = [], []
    for k in range(n):
        atoms.append((k, 0, "C"))
        if k:
            bonds.append((k - 1, k, 1))
    if skeleton:
        return atoms, bonds
    for k in range(n):
        for dyy in (1, -1):
            atoms.append((k, dyy * 0.8, "H"))
            bonds.append((k, len(atoms) - 1, 1))
    atoms.append((-0.8, 0, "H"))
    bonds.append((0, len(atoms) - 1, 1))
    atoms.append((n - 1 + 0.8, 0, "H"))
    bonds.append((n - 1, len(atoms) - 1, 1))
    return atoms, bonds


# ---- electron-dot helpers ---------------------------------------------------------------
def emark(ax, x, y, m):
    if m == ".":
        ax.text(x, y, "•", ha="center", va="center", fontsize=10, color=HI)
    else:
        ax.text(x, y, "×", ha="center", va="center", fontsize=9, color=ACC)


def lone(ax, x, y, ang, marks, r=0.36, s=0.08):
    a = math.radians(ang)
    cx, cy = x + r * math.cos(a), y + r * math.sin(a)
    px, py = -math.sin(a), math.cos(a)
    for k, m in enumerate(marks):
        o = (k - (len(marks) - 1) / 2) * 2 * s
        emark(ax, cx + px * o, cy + py * o, m)


def shared(ax, p1, p2, pairs):
    """pairs: list of two-character strings, e.g. ['.x'] for one shared pair."""
    mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    L = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
    ux, uy = (p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L
    px, py = -uy, ux
    n = len(pairs)
    for k, pr in enumerate(pairs):
        o = (k - (n - 1) / 2) * 0.17
        for j, m in enumerate(pr):
            a = (j - 0.5) * 0.15
            emark(ax, mx + ux * a + px * o, my + uy * a + py * o, m)


def sym(ax, x, y, s, size=13):
    ax.text(x, y, s, ha="center", va="center", fontsize=size, color=INK, fontweight="bold")


# Fig 4.1: electron-dot structures of H2, O2, N2 and CH4
def fig_dot_simple():
    fig, axs = plt.subplots(1, 4, figsize=(9.0, 2.6))
    # H2
    ax = axs[0]
    sym(ax, 0, 0, "H"); sym(ax, 1.0, 0, "H")
    shared(ax, (0, 0), (1.0, 0), [".x"])
    ax.text(0.5, -0.9, "H₂: H–H (single bond)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-0.6, 1.6), (-1.2, 1.0))
    # O2
    ax = axs[1]
    sym(ax, 0, 0, "O"); sym(ax, 1.2, 0, "O")
    shared(ax, (0, 0), (1.2, 0), [".x", ".x"])
    lone(ax, 0, 0, 135, ".."); lone(ax, 0, 0, 225, "..")
    lone(ax, 1.2, 0, 45, "xx"); lone(ax, 1.2, 0, -45, "xx")
    ax.text(0.6, -0.9, "O₂: O=O (double bond)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-0.7, 1.9), (-1.2, 1.0))
    # N2
    ax = axs[2]
    sym(ax, 0, 0, "N"); sym(ax, 1.2, 0, "N")
    shared(ax, (0, 0), (1.2, 0), [".x", ".x", ".x"])
    lone(ax, 0, 0, 180, ".."); lone(ax, 1.2, 0, 0, "xx")
    ax.text(0.6, -0.9, "N₂: N≡N (triple bond)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-0.7, 1.9), (-1.2, 1.0))
    # CH4
    ax = axs[3]
    sym(ax, 0, 0, "C")
    for hx, hy in ((0, 1.0), (1.0, 0), (0, -1.0), (-1.0, 0)):
        sym(ax, hx, hy, "H", 12)
        shared(ax, (0, 0), (hx, hy), [".x"])
    ax.text(0, -1.55, "CH₄ (methane)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-1.4, 1.4), (-1.8, 1.3))
    fig.text(0.5, 0.97, "• and × show the valence electrons of the two atoms; each shared pair is one covalent bond",
             ha="center", fontsize=8.5, color=GREY)
    save(fig, "sci_ch04_fig01_dot_simple.png")


# Fig 4.2: electron-dot structures of CO2 and ethane
def fig_dot_co2_ethane():
    fig, axs = plt.subplots(1, 2, figsize=(7.6, 2.8))
    ax = axs[0]
    sym(ax, 0, 0, "O"); sym(ax, 1.2, 0, "C"); sym(ax, 2.4, 0, "O")
    shared(ax, (0, 0), (1.2, 0), ["x.", "x."])
    shared(ax, (1.2, 0), (2.4, 0), [".x", ".x"])
    lone(ax, 0, 0, 135, "xx"); lone(ax, 0, 0, 225, "xx")
    lone(ax, 2.4, 0, 45, "xx"); lone(ax, 2.4, 0, -45, "xx")
    ax.text(1.2, -1.0, "CO₂: O=C=O\n(• carbon, × oxygen)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-0.8, 3.2), (-1.5, 1.0))
    ax = axs[1]
    sym(ax, 0, 0, "C"); sym(ax, 1.3, 0, "C")
    shared(ax, (0, 0), (1.3, 0), [".."])
    for cx, hs in ((0, ((0, 1.0), (-1.0, 0), (0, -1.0))), (1.3, ((1.3, 1.0), (2.3, 0), (1.3, -1.0)))):
        for hx, hy in hs:
            sym(ax, hx, hy, "H", 12)
            shared(ax, (cx, 0), (hx, hy), [".x"])
    ax.text(0.65, -1.55, "C₂H₆ (ethane): 7 covalent bonds\n(• carbon, × hydrogen)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-1.4, 2.7), (-2.0, 1.3))
    save(fig, "sci_ch04_fig02_dot_co2_ethane.png")


# Fig 4.3: structures of the first four alkanes
def fig_alkanes():
    fig, axs = plt.subplots(2, 2, figsize=(7.4, 4.4))
    names = ["methane, CH₄", "ethane, C₂H₆", "propane, C₃H₈", "butane, C₄H₁₀"]
    for k, ax in enumerate(axs.flat):
        n = k + 1
        atoms, bonds = chain(n)
        mol(ax, atoms, bonds)
        ax.text((n - 1) / 2, -1.45, names[k], ha="center", fontsize=9, color=INK)
        finish(ax, (-1.2, 4.0), (-1.8, 1.2))
    save(fig, "sci_ch04_fig03_alkanes.png")


# Fig 4.4: structural isomers of butane and the carbon skeletons of pentane's isomers
def fig_isomers():
    fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.2), gridspec_kw={"width_ratios": [1.2, 1]})
    ax = axs[0]
    atoms, bonds = chain(4)
    mol(ax, atoms, bonds, dx=0.0, dy=1.4, size=10)
    ax.text(1.5, 0.15, "n-butane (straight chain)", ha="center", fontsize=8.5, color=INK)
    # isobutane
    iso = [(0, 0, "C"), (1, 0, "C"), (2, 0, "C"), (1, 1.2, "C"),
           (-0.8, 0, "H"), (0, 0.8, "H"), (0, -0.8, "H"), (2.8, 0, "H"), (2, 0.8, "H"), (2, -0.8, "H"),
           (1, -0.8, "H"), (1, 2.0, "H"), (0.3, 1.5, "H"), (1.7, 1.5, "H")]
    ib = [(0, 1, 1), (1, 2, 1), (1, 3, 1), (0, 4, 1), (0, 5, 1), (0, 6, 1), (2, 7, 1), (2, 8, 1), (2, 9, 1),
          (1, 10, 1), (3, 11, 1), (3, 12, 1), (3, 13, 1)]
    mol(ax, iso, ib, dx=4.8, dy=0.9, size=10)
    ax.text(5.8, -0.3, "isobutane (branched)", ha="center", fontsize=8.5, color=INK)
    ax.text(3.2, 3.3, "Both are C₄H₁₀ — structural isomers", ha="center", fontsize=9, color=HI)
    finish(ax, (-1.0, 7.8), (-0.6, 3.6))
    ax = axs[1]
    sk1 = [(k, 0, "C") for k in range(5)]
    mol(ax, sk1, [(k, k + 1, 1) for k in range(4)], dy=2.4, size=10)
    sk2 = [(0, 0, "C"), (1, 0, "C"), (2, 0, "C"), (3, 0, "C"), (1, 0.8, "C")]
    mol(ax, sk2, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (1, 4, 1)], dy=1.0, size=10)
    sk3 = [(0, 0, "C"), (1, 0, "C"), (2, 0, "C"), (1, 0.8, "C"), (1, -0.8, "C")]
    mol(ax, sk3, [(0, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1)], dx=4.2, dy=1.0, size=10)
    ax.text(2.6, 3.3, "Pentane, C₅H₁₂: three isomers\n(carbon skeletons)", ha="center", fontsize=9, color=HI)
    ax.text(4.4, 2.4, "(1) straight chain", ha="left", va="center", fontsize=8, color=INK)
    ax.text(1.5, -0.3, "(2) one branch", ha="center", fontsize=8, color=INK)
    ax.text(5.2, -0.3, "(3) two branches", ha="center", fontsize=8, color=INK)
    finish(ax, (-0.6, 6.6), (-0.6, 3.8))
    save(fig, "sci_ch04_fig04_isomers.png")


def ring(n, r, start=90):
    return [(r * math.cos(math.radians(start + 360 * k / n)), r * math.sin(math.radians(start + 360 * k / n))) for k in range(n)]


# Fig 4.5: ethene, ethyne, cyclohexane and benzene
def fig_unsaturated_rings():
    fig, axs = plt.subplots(1, 4, figsize=(9.6, 3.0))
    ax = axs[0]
    at = [(0, 0, "C"), (1.1, 0, "C"), (-0.6, 0.7, "H"), (-0.6, -0.7, "H"), (1.7, 0.7, "H"), (1.7, -0.7, "H")]
    mol(ax, at, [(0, 1, 2), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1)])
    ax.text(0.55, -1.4, "ethene, C₂H₄\n(double bond)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-1.1, 2.2), (-1.9, 1.2))
    ax = axs[1]
    at = [(-0.9, 0, "H"), (0, 0, "C"), (1.1, 0, "C"), (2.0, 0, "H")]
    mol(ax, at, [(0, 1, 1), (1, 2, 3), (2, 3, 1)])
    ax.text(0.55, -1.4, "ethyne, C₂H₂\n(triple bond)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-1.3, 2.4), (-1.9, 1.2))
    ax = axs[2]
    pts = ring(6, 1.0)
    at = [(x, y, "C") for x, y in pts]
    bd = [(k, (k + 1) % 6, 1) for k in range(6)]
    for k, (x, y) in enumerate(pts):
        ang = math.atan2(y, x)
        for da in (-0.4, 0.4):
            at.append((x + 0.75 * math.cos(ang + da), y + 0.75 * math.sin(ang + da), "H"))
            bd.append((k, len(at) - 1, 1))
    mol(ax, at, bd, size=9)
    ax.text(0, -2.45, "cyclohexane, C₆H₁₂\n(saturated ring)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-1.9, 1.9), (-3.0, 1.9))
    ax = axs[3]
    pts = ring(6, 1.0)
    at = [(x, y, "C") for x, y in pts]
    bd = [(k, (k + 1) % 6, 2 if k % 2 == 0 else 1) for k in range(6)]
    for k, (x, y) in enumerate(pts):
        ang = math.atan2(y, x)
        at.append((x + 0.75 * math.cos(ang), y + 0.75 * math.sin(ang), "H"))
        bd.append((k, len(at) - 1, 1))
    mol(ax, at, bd, size=9)
    ax.text(0, -2.45, "benzene, C₆H₆\n(unsaturated ring)", ha="center", fontsize=8.5, color=INK)
    finish(ax, (-1.9, 1.9), (-3.0, 1.9))
    save(fig, "sci_ch04_fig05_unsaturated_rings.png")


# Fig 4.6: compounds with functional groups
def fig_functional():
    fig, axs = plt.subplots(2, 3, figsize=(10.0, 5.0))

    def hs(atoms, bonds, idx, dirs):
        for dxx, dyy in dirs:
            x, y, _ = atoms[idx]
            atoms.append((x + dxx, y + dyy, "H"))
            bonds.append((idx, len(atoms) - 1, 1))

    # ethanol
    a = [(0, 0, "C"), (1, 0, "C"), (2, 0, "O"), (2.8, 0, "H")]
    b = [(0, 1, 1), (1, 2, 1), (2, 3, 1)]
    hs(a, b, 0, [(-0.8, 0), (0, 0.8), (0, -0.8)])
    hs(a, b, 1, [(0, 0.8), (0, -0.8)])
    mol(axs[0, 0], a, b)
    axs[0, 0].text(1.0, -1.5, "ethanol, C₂H₅OH (alcohol, –OH)", ha="center", fontsize=8.5)
    # ethanoic acid
    a = [(0, 0, "C"), (1, 0, "C"), (1, 0.85, "O"), (2, 0, "O"), (2.8, 0, "H")]
    b = [(0, 1, 1), (1, 2, 2), (1, 3, 1), (3, 4, 1)]
    hs(a, b, 0, [(-0.8, 0), (0, 0.8), (0, -0.8)])
    mol(axs[0, 1], a, b)
    axs[0, 1].text(1.0, -1.5, "ethanoic acid, CH₃COOH (–COOH)", ha="center", fontsize=8.5)
    # propanone
    a = [(0, 0, "C"), (1, 0, "C"), (2, 0, "C"), (1, 0.85, "O")]
    b = [(0, 1, 1), (1, 2, 1), (1, 3, 2)]
    hs(a, b, 0, [(-0.8, 0), (0, 0.8), (0, -0.8)])
    hs(a, b, 2, [(0.8, 0), (0, 0.8), (0, -0.8)])
    mol(axs[0, 2], a, b)
    axs[0, 2].text(1.0, -1.5, "propanone, CH₃COCH₃ (ketone)", ha="center", fontsize=8.5)
    # butanone
    a = [(0, 0, "C"), (1, 0, "C"), (2, 0, "C"), (3, 0, "C"), (1, 0.85, "O")]
    b = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (1, 4, 2)]
    hs(a, b, 0, [(-0.8, 0), (0, 0.8), (0, -0.8)])
    hs(a, b, 2, [(0, 0.8), (0, -0.8)])
    hs(a, b, 3, [(0.8, 0), (0, 0.8), (0, -0.8)])
    mol(axs[1, 0], a, b)
    axs[1, 0].text(1.5, -1.5, "butanone, CH₃COCH₂CH₃ (ketone)", ha="center", fontsize=8.5)
    # hexanal
    a = [(k, 0, "C") for k in range(6)] + [(5.7, 0.7, "O"), (5.7, -0.7, "H")]
    b = [(k, k + 1, 1) for k in range(5)] + [(5, 6, 2), (5, 7, 1)]
    hs(a, b, 0, [(-0.8, 0), (0, 0.8), (0, -0.8)])
    for k in range(1, 5):
        hs(a, b, k, [(0, 0.8), (0, -0.8)])
    mol(axs[1, 1], a, b, size=9)
    axs[1, 1].text(2.6, -1.5, "hexanal, CH₃(CH₂)₄CHO (aldehyde)", ha="center", fontsize=8.5)
    # bromopentane
    a = [(k, 0, "C") for k in range(5)] + [(5.0, 0, "Br")]
    b = [(k, k + 1, 1) for k in range(5)]
    hs(a, b, 0, [(-0.8, 0), (0, 0.8), (0, -0.8)])
    for k in range(1, 5):
        hs(a, b, k, [(0, 0.8), (0, -0.8)])
    mol(axs[1, 2], a, b, size=9)
    axs[1, 2].text(2.4, -1.5, "1-bromopentane, C₅H₁₁Br", ha="center", fontsize=8.5)
    for ax in axs.flat:
        finish(ax, (-1.2, 6.4), (-1.9, 1.4))
    save(fig, "sci_ch04_fig06_functional.png")


# Fig 4.7: formation of an ester (Activity 4.8)
def fig_ester():
    fig, ax = plt.subplots(figsize=(5.4, 4.0))
    # beaker (water bath)
    ax.add_patch(Polygon([[0.0, 2.6], [0.2, 0.4], [2.6, 0.4], [2.8, 2.6]], closed=True, fc="none", ec=INK, lw=1.4))
    ax.add_patch(Polygon([[0.07, 1.9], [0.2, 0.42], [2.6, 0.42], [2.73, 1.9]], closed=True, fc=WATER, ec="none", zorder=0))
    # test tube
    r = 0.25
    ax.plot([1.15, 1.15], [3.4, 0.9], color=INK, lw=1.3)
    ax.plot([1.65, 1.65], [3.4, 0.9], color=INK, lw=1.3)
    t = np.linspace(np.pi, 2 * np.pi, 30)
    ax.plot(1.4 + r * np.cos(t), 0.9 + r * np.sin(t), color=INK, lw=1.3)
    ax.add_patch(Rectangle((1.16, 0.9), 0.48, 0.8, fc="#F3E0B5", ec="none"))
    ax.add_patch(Polygon(np.c_[1.4 + r * np.cos(t), 0.9 + r * np.sin(t)], closed=True, fc="#F3E0B5", ec="none"))
    # tripod, wire gauze, burner
    ax.plot([-0.2, 3.0], [0.4, 0.4], color=GREY, lw=2.5)
    ax.plot([0.1, -0.1], [0.4, -0.8], color=GREY, lw=2)
    ax.plot([2.7, 2.9], [0.4, -0.8], color=GREY, lw=2)
    ax.add_patch(Rectangle((1.2, -0.75), 0.4, 0.6, fc=SHADE, ec=INK, lw=1.0))
    ax.add_patch(Rectangle((0.95, -0.9), 0.9, 0.15, fc=SHADE, ec=INK, lw=1.0))
    ax.add_patch(Polygon([[1.28, -0.15], [1.4, 0.3], [1.52, -0.15]], closed=True, fc=FLAME, ec="#C46A00", lw=0.6))
    label(ax, (1.4, 1.3), "ethanol + ethanoic acid\n+ a few drops of\nconcentrated H₂SO₄", (3.3, 1.6))
    label(ax, (2.5, 1.0), "water bath (beaker\nof water)", (3.3, 0.4))
    label(ax, (2.2, 0.4), "wire gauze on tripod", (3.3, -0.4))
    label(ax, (1.65, -0.5), "burner", (3.3, -1.0))
    label(ax, (1.15, 3.2), "test tube", (-1.2, 3.2))
    finish(ax, (-1.4, 6.0), (-1.2, 3.6))
    save(fig, "sci_ch04_fig07_ester.png")


# Fig 4.8: soap micelle around oily dirt, and a soap molecule
def fig_micelle():
    fig, axs = plt.subplots(1, 2, figsize=(8.0, 3.6), gridspec_kw={"width_ratios": [1, 1.2]})
    ax = axs[0]
    ax.plot([0, 2.4], [0, 0], color=INK, lw=2.0)
    for k in range(9):
        ax.plot([0.15 + 0.25 * k, 0.15 + 0.25 * k + 0.12], [0, 0.12 * ((-1) ** k)], color=INK, lw=0)
    xs = np.linspace(0, 2.4, 13)
    ax.plot(xs, 0.12 * np.array([(-1) ** k for k in range(13)]), color=INK, lw=1.6)
    ax.add_patch(Circle((2.7, 0), 0.25, fc=HI, ec=INK, lw=1.0))
    ax.text(2.7, 0, "−", ha="center", va="center", fontsize=12, color="white", fontweight="bold")
    ax.text(1.2, -0.55, "hydrocarbon tail\n(hydrophobic: dissolves in oil)", ha="center", va="top", fontsize=8.5, color=INK)
    ax.text(2.8, 0.55, "ionic head (–COO⁻ Na⁺)\nhydrophilic: dissolves in water", ha="center", va="bottom", fontsize=8.5, color=INK)
    finish(ax, (-0.4, 4.0), (-1.4, 1.4))
    ax = axs[1]
    ax.add_patch(Circle((0, 0), 2.6, fc=WATER, ec="none"))
    ax.add_patch(Circle((0, 0), 0.9, fc="#E7C982", ec="#B7791F", lw=1.0))
    ax.text(0, 0, "oily\ndirt", ha="center", va="center", fontsize=9, color=INK)
    for k in range(14):
        a = 2 * math.pi * k / 14
        x1, y1 = 0.55 * math.cos(a), 0.55 * math.sin(a)
        x2, y2 = 1.75 * math.cos(a), 1.75 * math.sin(a)
        ax.plot([x1, x2], [y1, y2], color=INK, lw=1.2)
        ax.add_patch(Circle((1.95 * math.cos(a), 1.95 * math.sin(a)), 0.18, fc=HI, ec=INK, lw=0.8))
    ax.text(0, -2.95, "micelle: tails point into the oil,\nionic heads face the water", ha="center", va="top", fontsize=8.5, color=INK)
    ax.text(2.0, 2.3, "water", fontsize=9, color=ACC)
    finish(ax, (-2.9, 3.0), (-3.8, 2.8))
    save(fig, "sci_ch04_fig08_micelle.png")


if __name__ == "__main__":
    fig_dot_simple()
    fig_dot_co2_ethane()
    fig_alkanes()
    fig_isomers()
    fig_unsaturated_rings()
    fig_functional()
    fig_ester()
    fig_micelle()
