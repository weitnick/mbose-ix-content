"""Figures for Class X Science, Chapter 3: Metals and Non-metals.
Run: python x_sci_ch03_metals_nonmetals.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Science", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, SHADE = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#BFD3E6"
WATER, FLAME, COPPER, RUST = "#D6E9F8", "#F4A300", "#C8742E", "#A0522D"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def label(ax, xy, text, xytext, ha="left", size=9):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=size, color=INK, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8), annotation_clip=False)


def finish(ax, xl, yl):
    ax.set_xlim(*xl)
    ax.set_ylim(*yl)
    ax.set_aspect("equal")
    ax.axis("off")


def tube(ax, x, y_top, y_bot, w, fill_to=None, fill=WATER):
    r = w / 2
    ax.plot([x - r, x - r], [y_top, y_bot + r], color=INK, lw=1.3)
    ax.plot([x + r, x + r], [y_top, y_bot + r], color=INK, lw=1.3)
    t = np.linspace(np.pi, 2 * np.pi, 40)
    ax.plot(x + r * np.cos(t), y_bot + r + r * np.sin(t), color=INK, lw=1.3)
    if fill_to is not None:
        xs = list(x + r * np.cos(t)) + [x + r, x - r]
        ys = list(y_bot + r + r * np.sin(t)) + [fill_to, fill_to]
        ax.add_patch(Polygon(np.c_[xs, ys], closed=True, fc=fill, ec="none", zorder=0))


def burner(ax, x, y):
    ax.add_patch(Rectangle((x - 0.18, y - 0.7), 0.36, 0.7, fc=SHADE, ec=INK, lw=1.0))
    ax.add_patch(Rectangle((x - 0.4, y - 0.85), 0.8, 0.15, fc=SHADE, ec=INK, lw=1.0))
    ax.add_patch(Polygon([[x - 0.13, y], [x, y + 0.55], [x + 0.13, y]], closed=True, fc=FLAME, ec="#C46A00", lw=0.6))


# Fig 3.1: metals conduct heat (Activity 3.5)
def fig_heat_conduction():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    ax.add_patch(Rectangle((0.0, 0.0), 0.25, 3.2, fc=SHADE, ec=INK, lw=1.0))
    ax.add_patch(Rectangle((-0.4, -0.15), 1.0, 0.15, fc=SHADE, ec=INK, lw=1.0))
    ax.add_patch(Rectangle((0.15, 2.6), 0.5, 0.3, fc="#8E8E8E", ec=INK, lw=0.9))
    ax.plot([0.6, 4.4], [2.75, 2.75], color=COPPER, lw=2.5)
    ax.add_patch(Circle((4.4, 2.75), 0.1, fc="#F3E3B5", ec=INK, lw=0.8))
    ax.plot([4.4, 4.4], [2.65, 2.25], color=GREY, lw=1.0)
    ax.annotate("", xy=(4.4, 1.6), xytext=(4.4, 2.15), arrowprops=dict(arrowstyle="->", color=HI, lw=1.2))
    burner(ax, 1.1, 2.0)
    label(ax, (0.12, 1.2), "stand", (-1.2, 1.2))
    label(ax, (2.5, 2.75), "copper or aluminium wire", (2.0, 3.35))
    label(ax, (4.45, 2.8), "pin fixed with wax", (4.7, 3.2))
    ax.text(4.55, 1.7, "the wax melts and\nthe pin drops", fontsize=8.5, color=HI, va="center")
    label(ax, (1.25, 1.7), "burner (heat near\nthe clamp)", (2.0, 0.9))
    finish(ax, (-1.6, 6.2), (-0.4, 3.6))
    save(fig, "sci_ch03_fig01_heat_conduction.png")


# Fig 3.2: metals conduct electricity (Activity 3.6)
def fig_electric_conduction():
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    ax.plot([0, 0, 1.4], [0, 1.6, 1.6], color=INK, lw=1.2)
    for x0, tall in ((1.4, True), (1.6, False), (1.8, True), (2.0, False)):
        ax.plot([x0, x0], [1.35, 1.85] if tall else [1.45, 1.75], color=INK, lw=2.0 if tall else 1.2)
    ax.plot([2.0, 3.0], [1.6, 1.6], color=INK, lw=1.2)
    ax.add_patch(Circle((3.3, 1.6), 0.3, fc="#FFF3B0", ec=INK, lw=1.2))
    ax.plot([3.15, 3.45], [1.45, 1.75], color=INK, lw=0.9)
    ax.plot([3.15, 3.45], [1.75, 1.45], color=INK, lw=0.9)
    ax.plot([3.6, 4.6, 4.6, 3.4], [1.6, 1.6, 0, 0], color=INK, lw=1.2)
    ax.plot([0, 1.4], [0, 0], color=INK, lw=1.2)
    ax.add_patch(Circle((1.4, 0), 0.06, fc=INK))
    ax.add_patch(Circle((3.4, 0), 0.06, fc=INK))
    ax.add_patch(Rectangle((1.4, -0.08), 2.0, 0.16, fc="#9AA3AD", ec=INK, lw=0.9))
    ax.text(1.4, -0.35, "A", ha="center", fontsize=10, color=INK)
    ax.text(3.4, -0.35, "B", ha="center", fontsize=10, color=INK)
    label(ax, (2.4, 0.05), "metal sample", (2.0, -0.85))
    label(ax, (1.7, 1.85), "battery", (0.6, 2.4))
    label(ax, (3.3, 1.9), "bulb glows", (3.8, 2.4))
    finish(ax, (-0.4, 5.2), (-1.1, 2.7))
    save(fig, "sci_ch03_fig02_electric_conduction.png")


# Fig 3.3: action of steam on a metal
def fig_steam():
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    # boiling tube with water and glass wool, heated
    tube(ax, 0.8, 2.8, 0.6, 0.7, fill_to=1.2)
    burner(ax, 0.8, -0.1)
    ax.add_patch(Rectangle((0.55, 2.8), 0.5, 0.25, fc="#8B5A2B", ec=INK, lw=0.8))
    # horizontal hard glass tube with metal sample
    ax.plot([0.8, 0.8, 1.5], [3.05, 3.3, 3.3], color=INK, lw=1.3)
    ax.add_patch(Rectangle((1.5, 3.05), 2.6, 0.5, fc="none", ec=INK, lw=1.3))
    for k in range(6):
        ax.add_patch(Rectangle((2.3 + 0.12 * k, 3.12), 0.08, 0.12, fc="#7A7A7A", ec="none"))
    burner(ax, 2.6, 2.2)
    # delivery tube to inverted gas jar over water trough
    ax.plot([4.1, 4.6, 4.6, 5.3, 5.3], [3.3, 3.3, 0.5, 0.5, 0.9], color=INK, lw=1.3)
    ax.add_patch(Rectangle((4.4, 0.0), 2.0, 1.2, fc="none", ec=INK, lw=1.2))
    ax.add_patch(Rectangle((4.42, 0.02), 1.96, 0.9, fc=WATER, ec="none", zorder=0))
    ax.add_patch(Rectangle((5.0, 0.6), 0.65, 2.2, fc="white", ec=INK, lw=1.2))
    ax.add_patch(Rectangle((5.02, 0.62), 0.61, 0.6, fc=WATER, ec="none"))
    label(ax, (0.8, 0.95), "water", (-0.8, 1.2))
    label(ax, (2.6, 3.2), "metal sample", (2.6, 4.0))
    label(ax, (5.3, 2.2), "hydrogen gas\ncollected", (5.9, 2.6))
    label(ax, (5.9, 0.5), "water trough", (6.2, -0.3))
    label(ax, (1.5, 3.3), "steam", (0.5, 4.0))
    finish(ax, (-1.0, 7.4), (-1.1, 4.3))
    save(fig, "sci_ch03_fig03_steam.png")


SLOTS = [(-0.13, 1), (1, 0.13), (0.13, -1), (-1, -0.13), (0.13, 1), (1, -0.13), (-0.13, -1), (-1, 0.13)]


def atom(ax, x, y, sym, marks, r=0.55):
    """marks: a string of electron symbols, e.g. "xxxxxxx." for chloride (7 own, 1 gained)."""
    ax.add_patch(Circle((x, y), r, fc="none", ec=GREY, lw=0.8, ls="--"))
    ax.text(x, y, sym, ha="center", va="center", fontsize=12, color=INK, fontweight="bold")
    for i, m in enumerate(marks):
        sx, sy = SLOTS[i]
        px = x + r * (sx if abs(sx) == 1 else sx / 0.55 * 0.25) if abs(sx) == 1 else x + sx * 1.6
        py = y + r * sy if abs(sy) == 1 else y + sy * 1.6
        if abs(sx) == 1:
            px = x + r * sx
        if abs(sy) == 1:
            py = y + r * sy
        sym_m, col = ("\u2022", HI) if m == "." else ("\u00d7", ACC)
        ax.text(px, py, sym_m, ha="center", va="center", fontsize=11 if m == "." else 9, color=col)


# Fig 3.4: formation of NaCl and MgCl2 by transfer of electrons
def fig_ionic_formation():
    fig, ax = plt.subplots(figsize=(7.6, 3.9))
    rows = [(2.6, "Na", ".", "2, 8, 1", "Na\u207a", "2, 8", "", "\u2212", "NaCl", ""),
            (0.4, "Mg", "..", "2, 8, 2", "Mg\u00b2\u207a", "2, 8", "2", "\u2212", "MgCl\u2082", " (\u00d72)")]
    for y, m, me, mconf, cat, cconf, mult, ch, name, note in rows:
        atom(ax, 0.6, y, m, me)
        ax.text(1.35, y, "+", fontsize=14, ha="center", va="center", color=INK)
        atom(ax, 2.1, y, "Cl", "xxxxxxx")
        ax.annotate("", xy=(3.6, y), xytext=(2.9, y), arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
        ax.text(4.3, y, cat, fontsize=13, ha="center", va="center", color=INK, fontweight="bold")
        if mult:
            ax.text(5.15, y, mult, fontsize=14, ha="center", va="center", color=INK)
        ax.text(5.5, y, "[", fontsize=26, ha="center", va="center", color=INK)
        atom(ax, 6.2, y, "Cl", "xxxxxxx.")
        ax.text(6.9, y, "]", fontsize=26, ha="center", va="center", color=INK)
        ax.text(7.1, y + 0.45, ch, fontsize=12, ha="center", va="center", color=INK)
        ax.text(7.5, y, name, fontsize=11, va="center", color=HI, fontweight="bold")
        ax.text(0.6, y - 0.85, mconf, fontsize=8.5, ha="center", color=GREY)
        ax.text(2.1, y - 0.85, "2, 8, 7" + note, fontsize=8.5, ha="center", color=GREY)
        ax.text(4.3, y - 0.85, cconf, fontsize=8.5, ha="center", color=GREY)
        ax.text(6.2, y - 0.85, "2, 8, 8", fontsize=8.5, ha="center", color=GREY)
    ax.text(0.0, 3.6, "\u2022 electron of the metal      \u00d7 electron of chlorine", fontsize=8.5, color=INK)
    finish(ax, (-0.3, 8.7), (-0.75, 3.9))
    save(fig, "sci_ch03_fig04_ionic_formation.png")


# Fig 3.5: formation of Na2O and MgO (electron dot)
def fig_oxides_formation():
    fig, ax = plt.subplots(figsize=(7.6, 3.6))
    y1 = 2.3
    atom(ax, 0.5, y1 + 0.55, "Na", ".", r=0.45)
    atom(ax, 0.5, y1 - 0.55, "Na", ".", r=0.45)
    ax.text(1.25, y1, "+", fontsize=14, ha="center", va="center")
    atom(ax, 2.0, y1, "O", "xxxxxx")
    ax.annotate("", xy=(3.5, y1), xytext=(2.8, y1), arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    ax.text(4.2, y1, "2Na\u207a", fontsize=13, ha="center", va="center", fontweight="bold")
    ax.text(5.0, y1, "[", fontsize=26, ha="center", va="center")
    atom(ax, 5.7, y1, "O", "xxxxxx..")
    ax.text(6.4, y1, "]", fontsize=26, ha="center", va="center")
    ax.text(6.65, y1 + 0.45, "2\u2212", fontsize=11, ha="center", va="center")
    ax.text(7.1, y1, "Na\u2082O", fontsize=11, va="center", color=HI, fontweight="bold")
    y2 = 0.3
    atom(ax, 0.5, y2, "Mg", "..")
    ax.text(1.25, y2, "+", fontsize=14, ha="center", va="center")
    atom(ax, 2.0, y2, "O", "xxxxxx")
    ax.annotate("", xy=(3.5, y2), xytext=(2.8, y2), arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    ax.text(4.2, y2, "Mg\u00b2\u207a", fontsize=13, ha="center", va="center", fontweight="bold")
    ax.text(5.0, y2, "[", fontsize=26, ha="center", va="center")
    atom(ax, 5.7, y2, "O", "xxxxxx..")
    ax.text(6.4, y2, "]", fontsize=26, ha="center", va="center")
    ax.text(6.65, y2 + 0.45, "2\u2212", fontsize=11, ha="center", va="center")
    ax.text(7.1, y2, "MgO", fontsize=11, va="center", color=HI, fontweight="bold")
    ax.text(0.0, 3.55, "\u2022 electron of the metal      \u00d7 electron of oxygen", fontsize=8.5, color=INK)
    finish(ax, (-0.2, 8.0), (-0.4, 3.8))
    save(fig, "sci_ch03_fig05_oxides_formation.png")


# Fig 3.6: activity series and the method of extraction
def fig_series_metallurgy():
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    metals = ["K", "Na", "Ca", "Mg", "Al", "Zn", "Fe", "Pb", "Cu", "Ag", "Au"]
    for i, m in enumerate(metals):
        y = 4.0 - i * 0.36
        ax.add_patch(Rectangle((0.0, y - 0.16), 0.7, 0.32, fc=SOFT, ec=ACC, lw=0.8))
        ax.text(0.35, y, m, ha="center", va="center", fontsize=10, color=INK, fontweight="bold")
    groups = [(0, 4, "high reactivity:\nelectrolysis of molten\nchlorides or oxides", "#F6D7C3"),
              (5, 8, "medium reactivity:\nroasting or calcination,\nthen reduction with carbon", "#FCEBC2"),
              (9, 10, "low reactivity:\nfound free (native state)", "#DDEFD9")]
    for a, b, t, c in groups:
        ytop = 4.0 - a * 0.36 + 0.16
        ybot = 4.0 - b * 0.36 - 0.16
        ax.add_patch(Rectangle((0.9, ybot), 3.6, ytop - ybot, fc=c, ec=GREY, lw=0.8))
        ax.text(2.7, (ytop + ybot) / 2, t, ha="center", va="center", fontsize=8.5, color=INK)
    ax.annotate("", xy=(-0.35, 0.3), xytext=(-0.35, 4.1), arrowprops=dict(arrowstyle="->", color=HI, lw=1.4))
    ax.text(-0.55, 2.2, "reactivity decreases", rotation=90, ha="center", va="center", fontsize=8.5, color=HI)
    finish(ax, (-0.8, 4.7), (0.0, 4.3))
    save(fig, "sci_ch03_fig06_series_metallurgy.png")


# Fig 3.7: steps in the extraction of metals
def fig_extraction_steps():
    fig, ax = plt.subplots(figsize=(8.2, 4.2))

    def b(x, y, w, t, fc=SOFT, h=0.56):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.03,rounding_size=0.1", fc=fc, ec=ACC, lw=1.0))
        ax.text(x, y, t, ha="center", va="center", fontsize=8.4, color=INK)

    def arr(pts):
        xs, ys = zip(*pts)
        ax.plot(xs[:-1] + (xs[-1],), ys, color=GREY, lw=1.0)
        ax.annotate("", xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle="->", color=GREY, lw=1.0))

    L, M, R = 1.3, 4.1, 6.9
    b(M, 3.5, 1.6, "Ore", HI)
    b(M, 2.7, 3.8, "Enrichment (removal of gangue)")
    arr([(M, 3.22), (M, 2.98)])
    b(L, 1.7, 2.4, "High reactivity")
    b(M, 1.7, 2.6, "Medium reactivity")
    b(R, 1.7, 2.4, "Low reactivity")
    arr([(M, 2.42), (L, 1.98)])
    arr([(M, 2.42), (M, 1.98)])
    arr([(M, 2.42), (R, 1.98)])
    b(L, 0.6, 2.4, "Electrolysis of the\nmolten compound", SHADE, 0.7)
    b(M, 0.6, 2.9, "Sulphide ore: roasting\nCarbonate ore: calcination", SHADE, 0.7)
    b(R, 0.6, 2.4, "Sulphide ore heated\nin air gives the metal", SHADE, 0.7)
    for x in (L, M, R):
        arr([(x, 1.42), (x, 0.95)])
    b(M, -0.45, 3.3, "Oxide reduced to metal\n(carbon or a reactive metal)", SHADE, 0.7)
    arr([(M, 0.25), (M, -0.1)])
    b(M, -1.45, 2.8, "Refining (electrolytic)", "#DDEFD9")
    arr([(M, -0.8), (M, -1.17)])
    arr([(L, 0.25), (L, -1.45), (M - 1.4, -1.45)])
    arr([(R, 0.25), (R, -1.45), (M + 1.4, -1.45)])
    finish(ax, (-0.1, 8.3), (-1.9, 3.9))
    save(fig, "sci_ch03_fig07_extraction_steps.png")


# Fig 3.8: electrolytic refining of copper
def fig_refining():
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    ax.add_patch(Rectangle((0.5, 0.0), 3.6, 2.4, fc="none", ec=INK, lw=1.4))
    ax.add_patch(Rectangle((0.52, 0.02), 3.56, 1.9, fc="#9CC3E6", ec="none", zorder=0))
    ax.add_patch(Rectangle((1.1, 0.5), 0.35, 2.4, fc=COPPER, ec=INK, lw=1.0))
    ax.add_patch(Rectangle((3.15, 0.5), 0.15, 2.4, fc="#E08A4B", ec=INK, lw=1.0))
    for k in range(7):
        ax.add_patch(Circle((1.0 + 0.22 * k, 0.12), 0.07, fc="#5E5E5E", ec="none"))
    ax.plot([1.27, 1.27, 2.0], [2.9, 3.4, 3.4], color=INK, lw=1.2)
    ax.plot([3.22, 3.22, 2.6], [2.9, 3.4, 3.4], color=INK, lw=1.2)
    ax.plot([2.0, 2.0], [3.2, 3.6], color=INK, lw=2.0)
    ax.plot([2.15, 2.15], [3.28, 3.52], color=INK, lw=1.2)
    ax.plot([2.45, 2.45], [3.2, 3.6], color=INK, lw=2.0)
    ax.plot([2.6, 2.6], [3.28, 3.52], color=INK, lw=1.2)
    ax.text(1.27, 3.6, "+", ha="center", fontsize=12, color=INK, fontweight="bold")
    ax.text(3.22, 3.6, "−", ha="center", fontsize=12, color=INK, fontweight="bold")
    ax.annotate("", xy=(2.95, 1.3), xytext=(1.6, 1.3), arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
    ax.text(2.28, 1.42, "Cu²⁺", ha="center", fontsize=9, color=INK)
    label(ax, (1.2, 2.2), "anode: impure copper", (-1.8, 2.7))
    label(ax, (3.3, 2.2), "cathode: thin strip\nof pure copper", (4.4, 2.7))
    label(ax, (3.6, 1.0), "electrolyte: acidified\ncopper sulphate solution", (4.4, 1.2))
    label(ax, (1.4, 0.12), "anode mud (insoluble impurities)", (-1.8, -0.5))
    finish(ax, (-2.0, 6.8), (-0.8, 3.9))
    save(fig, "sci_ch03_fig08_refining.png")


# Fig 3.9: conditions for rusting (Activity 3.14)
def fig_rusting():
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    xa, xb, xc = 0.9, 3.3, 5.7
    for x in (xa, xb, xc):
        tube(ax, x, 3.0, 0.2, 0.8)
        ax.add_patch(Rectangle((x - 0.42, 3.0), 0.84, 0.3, fc="#8B5A2B", ec=INK, lw=0.8))
    ax.add_patch(Rectangle((xa - 0.38, 0.6), 0.76, 1.0, fc=WATER, ec="none", zorder=0))
    ax.plot([xa, xa], [0.45, 2.4], color=RUST, lw=3.5)
    for k in range(5):
        ax.add_patch(Circle((xa + 0.06 * ((-1) ** k), 0.7 + 0.3 * k), 0.05, fc="#B5651D", ec="none"))
    ax.add_patch(Rectangle((xb - 0.38, 0.6), 0.76, 1.2, fc=WATER, ec="none", zorder=0))
    ax.add_patch(Rectangle((xb - 0.38, 1.8), 0.76, 0.2, fc="#F2D06B", ec="none", zorder=0))
    ax.plot([xb, xb], [0.45, 2.4], color="#6E6E6E", lw=3.5)
    for k in range(7):
        ax.add_patch(Circle((xc - 0.25 + 0.08 * k, 0.4 + 0.04 * (k % 2)), 0.07, fc="white", ec=GREY, lw=0.6))
    ax.plot([xc, xc], [0.6, 2.4], color="#6E6E6E", lw=3.5)
    ax.text(xa, -0.3, "A: air and water\nnail rusts", ha="center", va="top", fontsize=8.5, color=INK)
    ax.text(xb, -0.3, "B: boiled water + oil\n(no air): no rust", ha="center", va="top", fontsize=8.5, color=INK)
    ax.text(xc, -0.3, "C: dry air (CaCl\u2082)\nno rust", ha="center", va="top", fontsize=8.5, color=INK)
    label(ax, (xb + 0.35, 1.9), "layer of oil", (xb + 0.9, 3.5))
    finish(ax, (-0.3, 7.0), (-1.1, 3.8))
    save(fig, "sci_ch03_fig09_rusting.png")


if __name__ == "__main__":
    fig_heat_conduction()
    fig_electric_conduction()
    fig_steam()
    fig_ionic_formation()
    fig_oxides_formation()
    fig_series_metallurgy()
    fig_extraction_steps()
    fig_refining()
    fig_rusting()
