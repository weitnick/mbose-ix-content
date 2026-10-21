"""Figures for Class X Science, Chapter 8: Heredity.
Run: python x_sci_ch08_heredity.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_sci_ch05_life_processes import ACC, GREEN, GREY, HI, INK, LGREEN, PINK, SHADE, SOFT, TAN, blob, finish, label, save, smooth
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle

YEL = "#F2D14E"
GRN = "#7DB36B"
SKIN = "#F3D2B8"
TALLBG = "#E5F2DD"
SHORTBG = "#F6E7CF"


def txt(ax, x, y, s, size=9, **kw):
    kw.setdefault("ha", "center")
    kw.setdefault("va", "center")
    ax.text(x, y, s, fontsize=size, color=kw.pop("color", INK), **kw)


def arrow(ax, p0, p1, lw=1.1):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="-|>", color=INK, lw=lw, mutation_scale=11))


def beetle(ax, cx, cy, s, body, spots=0, stripe=False):
    for side in (-1, 1):
        for dy in (0.25, 0.0, -0.25):
            ax.plot([cx + side * 0.25 * s, cx + side * 0.55 * s], [cy + dy * s, cy + (dy - 0.1) * s], color=INK, lw=1.0)
    ax.add_patch(Ellipse((cx, cy), 0.6 * s, 0.9 * s, fc=body, ec=INK, lw=1.0, zorder=2))
    ax.add_patch(Circle((cx, cy + 0.55 * s), 0.16 * s, fc=INK, ec=INK, zorder=2))
    ax.plot([cx, cx], [cy - 0.45 * s, cy + 0.4 * s], color=INK, lw=0.7, zorder=3)
    pos = [(-0.13, 0.15), (0.13, -0.1), (-0.12, -0.22), (0.12, 0.2)]
    for dx, dy in pos[:spots]:
        ax.add_patch(Circle((cx + dx * s, cy + dy * s), 0.06 * s, fc=INK, ec="none", zorder=3))
    if stripe:
        ax.plot([cx - 0.27 * s, cx + 0.27 * s], [cy - 0.05 * s, cy - 0.05 * s], color="#F7F1E1", lw=2.2, zorder=3)


# Fig 8.1: creation of diversity over succeeding generations
def fig_diversity():
    fig, ax = plt.subplots(figsize=(6.6, 5.0))
    gens = {0: [(4.0, 5.2, "#C0392B", 0, False)],
            1: [(2.0, 3.0, "#C0392B", 1, False), (6.0, 3.0, "#D35400", 0, False)],
            2: [(1.0, 0.8, "#C0392B", 2, False), (3.0, 0.8, "#A93226", 1, True),
                (5.0, 0.8, "#D35400", 1, False), (7.0, 0.8, "#E67E22", 0, True)]}
    for parent, kids in ((gens[0][0], gens[1]), (gens[1][0], gens[2][:2]), (gens[1][1], gens[2][2:])):
        for k in kids:
            ax.plot([parent[0], k[0]], [parent[1] - 0.65, k[1] + 0.7], color=GREY, lw=1.0, zorder=0)
    for g in gens.values():
        for x, y, c, sp, st in g:
            beetle(ax, x, y, 1.0, c, sp, st)
    for y, t in ((5.2, "parent"), (3.0, "first generation"), (0.8, "second generation")):
        txt(ax, -0.4, y, t, 8.5, ha="right")
    finish(ax, (-2.9, 7.8), (0.0, 6.0))
    save(fig, "sci_ch08_fig01_diversity.png")


def ear(ax, ox, free):
    head = smooth([(ox, 2.8), (ox + 0.05, 1.6), (ox, 0.4), (ox - 0.15, -0.6), (ox - 0.5, -1.3)], closed=False)
    ax.plot(head[:, 0], head[:, 1], color=INK, lw=1.4)
    if free:
        pts = [(ox, 2.0), (ox + 0.55, 2.45), (ox + 1.1, 2.2), (ox + 1.25, 1.4), (ox + 1.05, 0.7), (ox + 0.85, 0.25),
               (ox + 0.85, -0.2), (ox + 0.6, -0.5), (ox + 0.3, -0.42), (ox + 0.2, -0.1), (ox + 0.02, 0.2)]
    else:
        pts = [(ox, 2.0), (ox + 0.55, 2.45), (ox + 1.1, 2.2), (ox + 1.25, 1.4), (ox + 1.05, 0.7), (ox + 0.8, 0.25),
               (ox + 0.5, -0.05), (ox + 0.2, -0.25), (ox - 0.06, -0.38), (ox - 0.02, 0.2)]
    blob(ax, pts, SKIN, lw=1.2, z=2)
    inner = smooth([(ox + 0.4, 1.95), (ox + 0.85, 1.85), (ox + 0.9, 1.2), (ox + 0.6, 0.6)], closed=False)
    ax.plot(inner[:, 0], inner[:, 1], color="#B9876A", lw=1.2, zorder=3)
    ax.add_patch(Ellipse((ox + 0.4, 1.0), 0.22, 0.32, fc="#B9876A", ec="none", zorder=3))


# Fig 8.2: free and attached earlobes
def fig_earlobes():
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    ear(ax, 0.0, True)
    ear(ax, 3.6, False)
    label(ax, (0.6, -0.4), "earlobe hangs free", (1.6, -1.0))
    label(ax, (3.85, -0.2), "earlobe joined to\nthe side of the head", (5.2, -0.9))
    txt(ax, 0.6, 3.15, "(a) Free earlobe", 9.5, fontweight="bold")
    txt(ax, 4.2, 3.15, "(b) Attached earlobe", 9.5, fontweight="bold")
    finish(ax, (-0.9, 7.2), (-1.5, 3.5))
    save(fig, "sci_ch08_fig02_earlobes.png")


def plant(ax, x, y, tall, s=1.0):
    h = (2.0 if tall else 0.9) * s
    ax.plot([x, x], [y, y + h], color="#3E7B4F", lw=2.0, zorder=2)
    n = 4 if tall else 2
    for i in range(n):
        yy = y + h * (i + 0.6) / (n + 0.4)
        side = 1 if i % 2 == 0 else -1
        ax.add_patch(Ellipse((x + side * 0.22 * s, yy), 0.4 * s, 0.17 * s, angle=side * 25, fc=GRN, ec=INK, lw=0.6, zorder=3))
    ax.add_patch(Circle((x, y + h + 0.05 * s), 0.1 * s, fc="#B58AD1", ec=INK, lw=0.6, zorder=3))


def gamete(ax, x, y, s, fc="#FFF4D6"):
    ax.add_patch(Circle((x, y), 0.28, fc=fc, ec=INK, lw=0.9))
    txt(ax, x, y, s, 9.5, fontweight="bold")


# Fig 8.3: inheritance of tallness over two generations (monohybrid cross)
def fig_monohybrid():
    fig, ax = plt.subplots(figsize=(6.8, 7.4))
    txt(ax, 0.0, 11.6, "Parents", 9.5, fontweight="bold", ha="left")
    plant(ax, 2.5, 9.6, True)
    plant(ax, 6.5, 9.6, False)
    txt(ax, 4.5, 10.3, "×", 16)
    txt(ax, 2.5, 9.25, "tall (TT)", 9)
    txt(ax, 6.5, 9.25, "short (tt)", 9)
    txt(ax, 0.0, 8.4, "Germ-cells", 9.5, fontweight="bold", ha="left")
    gamete(ax, 2.5, 8.4, "T")
    gamete(ax, 6.5, 8.4, "t")
    arrow(ax, (2.8, 8.2), (4.2, 7.3))
    arrow(ax, (6.2, 8.2), (4.8, 7.3))
    txt(ax, 0.0, 6.4, "F1", 9.5, fontweight="bold", ha="left")
    plant(ax, 4.5, 5.6, True)
    txt(ax, 4.5, 5.25, "all tall (Tt)", 9)
    txt(ax, 7.6, 6.4, "self-pollination\nof F1 plants", 8.5, color=ACC)
    arrow(ax, (4.5, 5.0), (4.5, 4.45))
    txt(ax, 0.0, 2.4, "F2", 9.5, fontweight="bold", ha="left")
    x0, y0, c = 2.9, 0.3, 1.6
    for i, gt in enumerate(("T", "t")):
        gamete(ax, x0 + c * (i + 0.5), y0 + 2 * c + 0.4, gt)
        gamete(ax, x0 - 0.4, y0 + c * (1.5 - i), gt)
    cells = [["TT", "Tt"], ["Tt", "tt"]]
    for r in range(2):
        for k in range(2):
            g = cells[r][k]
            tall = "T" in g
            xx, yy = x0 + c * k, y0 + c * (1 - r)
            ax.add_patch(Rectangle((xx, yy), c, c, fc=TALLBG if tall else SHORTBG, ec=INK, lw=1.0))
            plant(ax, xx + 0.45, yy + 0.2, tall, 0.55)
            txt(ax, xx + 1.1, yy + 0.8, g, 10, fontweight="bold")
    txt(ax, x0 + 4.6, y0 + 2.1, "3 tall : 1 short\n(TT, Tt, Tt : tt)", 9, ha="left")
    txt(ax, x0 + 4.6, y0 + 1.0, "genotypes\n1 TT : 2 Tt : 1 tt", 9, ha="left", color=ACC)
    finish(ax, (-0.2, 9.8), (0.1, 12.0))
    save(fig, "sci_ch08_fig03_monohybrid.png")


def seed(ax, x, y, r, round_, yellow):
    t = np.linspace(0, 2 * np.pi, 120)
    rr = r * (1 if round_ else 1 + 0.12 * np.sin(9 * t))
    ax.add_patch(Polygon(np.c_[x + rr * np.cos(t), y + rr * np.sin(t)], fc=YEL if yellow else GRN, ec=INK, lw=0.8, zorder=3))


# Fig 8.4: independent inheritance of seed shape and seed colour (dihybrid cross)
def fig_dihybrid():
    fig, ax = plt.subplots(figsize=(7.6, 8.0))
    seed(ax, 2.0, 12.85, 0.35, True, False)
    seed(ax, 6.0, 12.85, 0.35, False, True)
    txt(ax, 4.0, 12.6, "×", 16)
    txt(ax, 2.0, 11.95, "round, green\nRR yy", 9)
    txt(ax, 6.0, 11.95, "wrinkled, yellow\nrr YY", 9)
    txt(ax, -1.0, 12.6, "Parents", 9.5, fontweight="bold", ha="left")
    for x, g in ((2.0, "Ry"), (6.0, "rY")):
        ax.add_patch(Circle((x, 10.9), 0.32, fc="#FFF4D6", ec=INK, lw=0.9))
        txt(ax, x, 10.9, g, 9, fontweight="bold")
    txt(ax, -1.0, 10.9, "Germ-cells", 9.5, fontweight="bold", ha="left")
    arrow(ax, (2.3, 10.65), (3.6, 9.95))
    arrow(ax, (5.7, 10.65), (4.4, 9.95))
    seed(ax, 4.0, 9.5, 0.35, True, True)
    txt(ax, 4.0, 8.85, "F1: all round, yellow (Rr Yy)", 9)
    txt(ax, -1.0, 9.5, "F1", 9.5, fontweight="bold", ha="left")
    txt(ax, 7.6, 9.5, "F1 × F1\n(self-pollination)", 8.5, color=ACC)
    g = ["RY", "Ry", "rY", "ry"]
    x0, y0, c = 1.4, 0.2, 1.55
    txt(ax, -1.0, 7.6, "F2", 9.5, fontweight="bold", ha="left")
    for i, gg in enumerate(g):
        txt(ax, x0 + c * (i + 0.5), y0 + 4 * c + 0.3, gg, 9, fontweight="bold", color=ACC)
        txt(ax, x0 - 0.35, y0 + c * (3.5 - i), gg, 9, fontweight="bold", color=ACC)
    for r in range(4):
        for k in range(4):
            a, b = g[r], g[k]
            geno = "".join(sorted(a[0] + b[0])) + "".join(sorted(a[1] + b[1]))
            rnd = "R" in geno
            yel = "Y" in geno
            xx, yy = x0 + c * k, y0 + c * (3 - r)
            ax.add_patch(Rectangle((xx, yy), c, c, fc="white", ec=INK, lw=0.9))
            seed(ax, xx + c / 2, yy + c * 0.6, 0.3, rnd, yel)
            txt(ax, xx + c / 2, yy + 0.25, geno, 8)
    tx = x0 + 4 * c + 0.4
    rows = [(True, True, "round, yellow", "315", "9"), (True, False, "round, green", "108", "3"),
            (False, True, "wrinkled, yellow", "101", "3"), (False, False, "wrinkled, green", "32", "1")]
    txt(ax, tx + 1.9, y0 + 5.6, "Mendel's F2 count", 9, fontweight="bold")
    for i, (rn, ye, name, n, ratio) in enumerate(rows):
        yy = y0 + 4.7 - i * 0.85
        seed(ax, tx + 0.2, yy, 0.22, rn, ye)
        txt(ax, tx + 0.55, yy, f"{name}: {n}", 8.5, ha="left")
        txt(ax, tx + 3.9, yy, ratio, 9, fontweight="bold")
    txt(ax, tx + 1.6, y0 + 1.05, "556 seeds\nratio 9 : 3 : 3 : 1", 9)
    finish(ax, (-1.2, 12.6), (0.0, 13.4))
    save(fig, "sci_ch08_fig04_dihybrid.png")


def chromo(ax, x, y, s, fc):
    ax.add_patch(Circle((x, y), 0.3, fc=fc, ec=INK, lw=0.9))
    txt(ax, x, y, s, 9.5, fontweight="bold")


# Fig 8.5: sex determination in human beings
def fig_sex():
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    XC, YC = "#F6C9D0", "#B9D3EE"
    ax.add_patch(FancyBboxPatch((0.6, 7.3), 2.6, 1.1, boxstyle="round,pad=0.05", fc=SOFT, ec=INK, lw=1.0))
    txt(ax, 1.9, 8.1, "father", 9, fontweight="bold")
    chromo(ax, 1.55, 7.65, "X", XC)
    chromo(ax, 2.25, 7.65, "Y", YC)
    ax.add_patch(FancyBboxPatch((5.0, 7.3), 2.6, 1.1, boxstyle="round,pad=0.05", fc=SOFT, ec=INK, lw=1.0))
    txt(ax, 6.3, 8.1, "mother", 9, fontweight="bold")
    chromo(ax, 5.95, 7.65, "X", XC)
    chromo(ax, 6.65, 7.65, "X", XC)
    txt(ax, 4.1, 7.85, "×", 16)
    txt(ax, 1.9, 6.85, "sperms", 8.5, color=ACC)
    txt(ax, 6.3, 6.85, "eggs", 8.5, color=ACC)
    x0, y0, c = 2.6, 1.0, 1.9
    for i, (s, fc) in enumerate((("X", XC), ("Y", YC))):
        chromo(ax, x0 - 0.5, y0 + c * (1.5 - i), s, fc)
    for i in range(2):
        chromo(ax, x0 + c * (i + 0.5), y0 + 2 * c + 0.5, "X", XC)
    txt(ax, x0 - 1.4, y0 + c, "from the\nfather", 8.5, color=ACC)
    txt(ax, x0 + c, y0 + 2 * c + 1.05, "from the mother", 8.5, color=ACC)
    for r, (s, fc, kid, bg) in enumerate((("X", XC, "girl", "#FBE3E7"), ("Y", YC, "boy", "#E2EDF8"))):
        for k in range(2):
            xx, yy = x0 + c * k, y0 + c * (1 - r)
            ax.add_patch(Rectangle((xx, yy), c, c, fc=bg, ec=INK, lw=1.0))
            chromo(ax, xx + 0.65, yy + 1.15, "X", XC)
            chromo(ax, xx + 1.25, yy + 1.15, s, fc)
            txt(ax, xx + c / 2, yy + 0.45, f"{'XX' if s == 'X' else 'XY'}: {kid}", 9)
    txt(ax, x0 + c, 0.45, "half the children are girls (XX) and half are boys (XY)", 8.5)
    finish(ax, (0.0, 8.0), (0.1, 8.7))
    save(fig, "sci_ch08_fig05_sex_determination.png")


if __name__ == "__main__":
    fig_diversity()
    fig_earlobes()
    fig_monohybrid()
    fig_dihybrid()
    fig_sex()
