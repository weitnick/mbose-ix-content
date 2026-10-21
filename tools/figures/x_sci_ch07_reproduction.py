"""Figures for Class X Science, Chapter 7: How do Organisms Reproduce?
Run: python x_sci_ch07_reproduction.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_sci_ch05_life_processes import (ACC, GREEN, GREY, HI, INK, LGREEN, PINK, SHADE, SOFT, TAN, blob, finish, label, save,
                                       smooth, tube_path)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle

CYTO = "#E3EEF8"
NUC = "#8FAACB"
POLLEN = "#F2C14E"
FLESH = "#F2C2B0"


def arrow(ax, p0, p1, color=INK, lw=1.2):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=12))


def caption(ax, x, y, text, size=8.5):
    ax.text(x, y, text, ha="center", va="top", fontsize=size, color=INK)


def title(ax, x, y, text):
    ax.text(x, y, text, ha="left", va="center", fontsize=10, fontweight="bold", color=INK)


def amoeba_pts(cx, cy, r, seed, lobes=6):
    rng = np.random.default_rng(seed)
    pts = []
    n = lobes * 2
    for i in range(n):
        a = 2 * math.pi * i / n
        rr = r * (1.25 if i % 2 == 0 else 0.85) * rng.uniform(0.9, 1.1)
        pts.append((cx + rr * math.cos(a), cy + 0.8 * rr * math.sin(a)))
    return pts


# Fig 7.1: binary fission in Amoeba and multiple fission in Plasmodium
def fig_fission():
    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    title(ax, 0.0, 8.6, "(a) Binary fission in Amoeba")
    y = 6.4
    blob(ax, amoeba_pts(1.6, y, 0.95, 1), CYTO)
    ax.add_patch(Circle((1.6, y), 0.28, fc=NUC, ec=INK, lw=0.8, zorder=3))
    caption(ax, 1.6, y - 1.35, "parent Amoeba")
    ax.add_patch(Ellipse((5.5, y), 2.5, 1.5, fc=CYTO, ec=INK, lw=1.1))
    for dx in (-0.38, 0.38):
        ax.add_patch(Circle((5.5 + dx, y), 0.24, fc=NUC, ec=INK, lw=0.8, zorder=3))
    caption(ax, 5.5, y - 1.35, "nucleus divides")
    blob(ax, [(8.3, y), (8.6, y + 0.7), (9.3, y + 0.75), (9.8, y + 0.25), (10.3, y + 0.75), (11.0, y + 0.7), (11.3, y),
              (11.0, y - 0.7), (10.3, y - 0.75), (9.8, y - 0.25), (9.3, y - 0.75), (8.6, y - 0.7)], CYTO)
    for dx in (-0.7, 0.7):
        ax.add_patch(Circle((9.8 + dx, y), 0.24, fc=NUC, ec=INK, lw=0.8, zorder=3))
    caption(ax, 9.8, y - 1.35, "cytoplasm divides")
    for (cx, cy), s in (((13.3, y + 0.45), 2), ((14.9, y - 0.35), 3)):
        blob(ax, amoeba_pts(cx, cy, 0.6, s), CYTO)
        ax.add_patch(Circle((cx, cy), 0.2, fc=NUC, ec=INK, lw=0.8, zorder=3))
    caption(ax, 14.1, y - 1.35, "two daughter cells")
    for x0, x1 in ((2.9, 4.0), (7.0, 8.1), (11.5, 12.5)):
        arrow(ax, (x0, y), (x1, y))
    label(ax, (1.95, 6.95), "pseudopodia", (3.0, 8.0))
    label(ax, (1.6, y + 0.1), "nucleus", (0.2, 7.95), ha="right")

    title(ax, 0.0, 3.6, "(b) Multiple fission in Plasmodium")
    y = 1.7
    ax.add_patch(Circle((1.8, y), 0.85, fc=CYTO, ec=INK, lw=1.1))
    ax.add_patch(Circle((1.8, y), 0.28, fc=NUC, ec=INK, lw=0.8))
    caption(ax, 1.8, y - 1.2, "single cell")
    ax.add_patch(Circle((7.0, y), 1.05, fc=CYTO, ec=INK, lw=2.4))
    for i in range(8):
        a = 2 * math.pi * i / 8
        ax.add_patch(Circle((7.0 + 0.6 * math.cos(a), y + 0.6 * math.sin(a)), 0.15, fc=NUC, ec=INK, lw=0.6))
    ax.add_patch(Circle((7.0, y), 0.15, fc=NUC, ec=INK, lw=0.6))
    caption(ax, 7.0, y - 1.35, "nucleus divides many times\n(inside a protective wall)")
    for a0, a1 in ((20, 95), (130, 210), (250, 330)):
        t = np.radians(np.linspace(a0, a1, 20))
        ax.plot(12.4 + 1.05 * np.cos(t), y + 1.05 * np.sin(t), color=INK, lw=2.4)
    rng = np.random.default_rng(5)
    for i in range(9):
        a = 2 * math.pi * i / 9 + 0.3
        rr = 0.55 if i % 2 else 1.4
        cx, cy = 12.4 + rr * math.cos(a), y + rr * 0.9 * math.sin(a)
        ax.add_patch(Circle((cx, cy), 0.24, fc=CYTO, ec=INK, lw=0.8))
        ax.add_patch(Circle((cx, cy), 0.09, fc=NUC, ec=INK, lw=0.5))
    caption(ax, 12.4, y - 1.6, "many daughter cells released")
    arrow(ax, (3.0, y), (5.6, y))
    arrow(ax, (8.4, y), (10.6, y))
    label(ax, (7.0 + 1.05 * math.cos(math.radians(60)), y + 1.05 * math.sin(math.radians(60))), "cyst wall", (8.6, 3.3))
    finish(ax, (-0.2, 16.0), (-0.3, 9.0))
    save(fig, "sci_ch07_fig01_fission.png")


def planaria(ax, cx, cy, s, fc="#D8B48A"):
    pts = [(0, 1.6), (0.22, 1.42), (0.42, 1.38), (0.3, 1.15), (0.3, 0.4), (0.28, -0.7), (0.15, -1.35), (0, -1.5)]
    full = pts + [(-x, y) for x, y in reversed(pts[1:-1])]
    blob(ax, [(cx + s * x, cy + s * y) for x, y in full], fc)
    for dx in (-0.1, 0.1):
        ax.add_patch(Circle((cx + s * dx, cy + s * 1.2), 0.05 * s, fc=INK, ec=INK, zorder=3))


# Fig 7.2: fragmentation in Spirogyra and regeneration in Planaria
def fig_fragment_regen():
    fig, axs = plt.subplots(1, 2, figsize=(8.0, 4.4), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axs[0]
    title(ax, 0.0, 5.6, "(a) Fragmentation in Spirogyra")
    w, h = 0.62, 0.42

    def filament(x0, y0, n):
        for i in range(n):
            x = x0 + i * w
            ax.add_patch(Rectangle((x, y0 - h / 2), w, h, fc="#E8F3E2", ec=INK, lw=0.9))
            t = np.linspace(0, 1, 40)
            ax.plot(x + t * w, y0 + 0.13 * np.sin(2 * math.pi * 2 * t), color=GREEN, lw=1.3)
            ax.add_patch(Circle((x + w / 2, y0), 0.045, fc=INK, ec=INK))

    filament(0.2, 4.4, 10)
    caption(ax, 3.3, 3.95, "a mature filament")
    arrow(ax, (3.3, 3.45), (3.3, 2.75))
    for x0, n in ((0.0, 3), (2.25, 3), (4.5, 3)):
        filament(x0, 2.3, n)
    caption(ax, 3.3, 1.85, "it breaks into fragments; each grows\ninto a new filament")
    label(ax, (0.2 + 2.5 * w, 4.4 + 0.12), "spiral chloroplast", (2.4, 5.1))
    label(ax, (0.2 + 7.6 * w, 4.4 + 0.21), "one cell", (5.2, 5.1))
    finish(ax, (-0.2, 6.8), (0.9, 5.9))

    ax = axs[1]
    title(ax, 0.0, 5.6, "(b) Regeneration in Planaria")
    planaria(ax, 1.0, 2.8, 1.3)
    for yc in (3.45, 2.15):
        ax.plot([0.35, 1.65], [yc, yc], color=HI, lw=1.4, ls=(0, (4, 2)))
    label(ax, (1.55, 3.45), "cut", (2.3, 4.6))
    arrow(ax, (2.0, 2.8), (2.9, 2.8))
    for i, yc in enumerate((4.3, 2.8, 1.3)):
        planaria(ax, 3.9 + 0.95 * i, 2.8, 0.75)
    caption(ax, 4.85, 1.25, "each piece grows into a\ncomplete Planaria")
    label(ax, (1.0, 2.8 + 1.3 * 1.2), "eye spots", (0.0, 5.0), ha="left")
    finish(ax, (-0.2, 6.2), (0.3, 5.9))
    save(fig, "sci_ch07_fig02_fragment_regen.png")


def hydra(ax, cx, base, s, bud=None):
    """bud: None, or 0..1 stage of bud growth."""
    top = base + 2.6 * s
    tube_path(ax, [(cx, base), (cx + 0.05 * s, base + 1.3 * s), (cx, top)], 0.55 * s, "#BFE0C8", z=2)
    ax.add_patch(Ellipse((cx, base), 0.75 * s, 0.22 * s, fc="#9CC9A8", ec=INK, lw=0.9, zorder=3))
    ax.add_patch(Polygon([(cx - 0.18 * s, top - 0.02), (cx, top + 0.25 * s), (cx + 0.18 * s, top - 0.02)], fc="#BFE0C8", ec=INK, lw=0.9, zorder=3))
    for a in (-60, -25, 25, 60):
        r = math.radians(a)
        pts = [(cx, top + 0.15 * s), (cx + math.sin(r) * 0.6 * s, top + 0.5 * s + math.cos(r) * 0.2 * s),
               (cx + math.sin(r) * 1.1 * s, top + 0.75 * s)]
        ax.plot(*smooth(pts, closed=False).T, color="#3E7B4F", lw=1.6, zorder=1)
    if bud:
        y0 = base + 1.1 * s
        L = 0.9 * s * bud
        tube_path(ax, [(cx + 0.2 * s, y0), (cx + 0.2 * s + 0.6 * L, y0 + 0.3 * L), (cx + 0.2 * s + L, y0 + 0.7 * L)], 0.3 * s * max(bud, 0.5), "#BFE0C8", z=4)
        if bud > 0.7:
            tx, ty = cx + 0.2 * s + L, y0 + 0.7 * L
            for a in (-30, 20, 60):
                r = math.radians(a)
                ax.plot([tx, tx + 0.35 * s * math.cos(r)], [ty, ty + 0.35 * s * math.sin(r) + 0.15 * s], color="#3E7B4F", lw=1.2, zorder=5)
    return top


# Fig 7.3: budding in Hydra and in yeast
def fig_budding():
    fig, axs = plt.subplots(1, 2, figsize=(8.2, 4.2), gridspec_kw={"width_ratios": [2.1, 1]})
    ax = axs[0]
    title(ax, -0.4, 4.6, "(a) Budding in Hydra")
    hydra(ax, 0.6, 0.6, 1.0)
    hydra(ax, 3.0, 0.6, 1.0, bud=0.45)
    hydra(ax, 5.5, 0.6, 1.0, bud=1.0)
    hydra(ax, 8.0, 0.6, 1.0)
    hydra(ax, 9.6, 0.6, 0.55)
    for x0 in (1.4, 3.9, 6.6):
        arrow(ax, (x0, 1.8), (x0 + 0.7, 1.8))
    label(ax, (3.3, 1.9), "bud", (3.7, 0.25))
    label(ax, (0.6 - 0.75, 3.6), "tentacles", (-0.4, 4.1), ha="right")
    label(ax, (0.6, 0.55), "base", (-0.3, 0.05), ha="right")
    caption(ax, 8.8, 0.3, "new Hydra separates")
    finish(ax, (-1.0, 10.5), (0.0, 4.9))

    ax = axs[1]
    title(ax, 0.0, 4.6, "(b) Budding in yeast")
    cells = [((1.5, 2.0), 0.75), ((2.45, 2.7), 0.42), ((2.95, 3.25), 0.22), ((0.95, 2.95), 0.3)]
    for (x, y), r in cells:
        ax.add_patch(Ellipse((x, y), 2 * r, 1.8 * r, fc="#F3E3B5", ec=INK, lw=1.0))
        ax.add_patch(Circle((x, y), 0.25 * r, fc=NUC, ec=INK, lw=0.6))
    label(ax, (1.5, 1.4), "parent yeast cell", (2.6, 0.8))
    label(ax, (2.95, 3.4), "bud", (3.4, 4.0))
    finish(ax, (0.0, 4.6), (0.4, 4.9))
    save(fig, "sci_ch07_fig03_budding.png")


# Fig 7.4: leaf of Bryophyllum with buds
def fig_bryophyllum():
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    t = np.linspace(0, 2 * np.pi, 400)
    a, b = 3.0, 1.4
    x, y = a * np.cos(t), b * np.sin(t)
    notch = 1 - 0.05 * (np.abs(np.sin(9 * t)) ** 0.4 < 0.35)
    ax.add_patch(Polygon(np.c_[x * notch, y * notch], fc="#9CCB8A", ec=INK, lw=1.1))
    ax.plot([-3.0, 3.0], [0, 0], color="#4E7F3E", lw=1.3)
    ax.plot([-4.3, -3.0], [-0.1, 0], color="#4E7F3E", lw=2.5)
    for k in range(9):
        tt = (k + 0.5) * np.pi / 9
        for sgn in (1, -1):
            px, py = a * np.cos(tt) * 0.95, sgn * b * np.sin(tt) * 0.95
            if abs(px) > 2.6 or (k % 2 == 1):
                continue
            if sgn == 1:
                ax.plot([px, px], [py, py + 0.35], color="#3E7B4F", lw=1.2)
                for s in (-1, 1):
                    ax.add_patch(Ellipse((px + s * 0.14, py + 0.42), 0.26, 0.14, angle=s * 30, fc="#5FA352", ec=INK, lw=0.6))
            else:
                for s in (-1, 1):
                    ax.add_patch(Ellipse((px + s * 0.15, py - 0.08), 0.26, 0.14, angle=-s * 25, fc="#5FA352", ec=INK, lw=0.6, zorder=3))
                for dx in (-0.12, 0.0, 0.12):
                    ax.plot([px, px + dx], [py - 0.1, py - 0.5], color="#8A6A3B", lw=0.8)
    label(ax, (1.95, -1.4), "new plantlet growing\nfrom a bud in a notch", (2.3, -2.2))
    label(ax, (-0.6, 0.5), "leaf", (-2.0, 2.4), ha="right")
    label(ax, (-0.95, 1.25), "notch on the leaf margin", (-0.4, 2.3))
    finish(ax, (-4.5, 4.5), (-2.6, 2.6))
    save(fig, "sci_ch07_fig04_bryophyllum.png")


# Fig 7.5: spore formation in Rhizopus
def fig_rhizopus():
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.add_patch(Rectangle((-0.2, -0.6), 7.4, 0.6, fc=TAN, ec=INK, lw=0.8))
    ax.text(6.9, -0.3, "bread", ha="right", va="center", fontsize=8.5, color=INK)
    t = np.linspace(0, 7, 200)
    ax.plot(t, 0.15 + 0.08 * np.sin(3 * t), color=GREY, lw=1.3)
    ax.plot(t, 0.3 + 0.08 * np.sin(2.4 * t + 1), color=GREY, lw=1.3)
    for x, hgt, burst in ((1.0, 2.4, False), (2.6, 3.0, False), (4.3, 2.6, True), (5.8, 2.2, False)):
        ax.plot(*smooth([(x, 0.25), (x + 0.08, hgt / 2), (x, hgt)], closed=False).T, color=GREY, lw=1.3)
        if burst:
            for a0, a1 in ((200, 340),):
                tt = np.radians(np.linspace(a0, a1, 20))
                ax.plot(x + 0.4 * np.cos(tt), hgt + 0.25 + 0.4 * np.sin(tt), color=INK, lw=1.0)
            rng = np.random.default_rng(3)
            for i in range(14):
                ang = rng.uniform(20, 160)
                rr = rng.uniform(0.5, 1.2)
                ax.add_patch(Circle((x + rr * math.cos(math.radians(ang)), hgt + 0.3 + rr * math.sin(math.radians(ang))), 0.05, fc="#4A4A4A", ec="none"))
        else:
            ax.add_patch(Circle((x, hgt + 0.25), 0.4, fc="#5A5A5A", ec=INK, lw=0.9))
            rng = np.random.default_rng(int(x * 10))
            for i in range(10):
                rr, ang = rng.uniform(0, 0.3), rng.uniform(0, 2 * np.pi)
                ax.add_patch(Circle((x + rr * math.cos(ang), hgt + 0.25 + rr * math.sin(ang)), 0.04, fc="#BDBDBD", ec="none"))
    label(ax, (0.7, 2.9), "sporangium\n(contains spores)", (0.2, 3.9), ha="right")
    label(ax, (4.6, 3.9), "spores released", (5.3, 4.6))
    label(ax, (5.85, 1.2), "stalk (sporangiophore)", (6.4, 1.3))
    label(ax, (0.5, 0.3), "hyphae (thread-like)", (0.2, 1.3), ha="right")
    finish(ax, (-2.6, 8.4), (-0.8, 4.9))
    save(fig, "sci_ch07_fig05_rhizopus.png")


# Fig 7.6: longitudinal section of a flower
def fig_flower():
    fig, ax = plt.subplots(figsize=(6.8, 5.8))
    tube_path(ax, [(0, -2.0), (0, -0.9), (0, -0.1)], 0.38, "#7DB36B")
    blob(ax, [(-0.9, -0.1), (0, -0.35), (0.9, -0.1), (0.75, 0.35), (0, 0.45), (-0.75, 0.35)], "#A9D18E", z=2)
    for s in (-1, 1):
        sep = [(0.7, 0.05), (1.5, 0.15), (2.1, 0.75), (1.55, 0.75), (0.95, 0.45)]
        blob(ax, [(s * x, y) for x, y in sep], "#7DB36B", z=2)
        pet = [(0.6, 0.3), (1.5, 0.9), (2.4, 2.4), (2.75, 3.6), (2.1, 3.3), (1.3, 2.2), (0.75, 0.9)]
        blob(ax, [(s * x, y) for x, y in pet], "#F2B8C6", z=1)
        fil = smooth([(s * 0.5, 0.4), (s * 0.85, 1.4), (s * 1.1, 2.6)], closed=False)
        ax.plot(fil[:, 0], fil[:, 1], color="#C9A227", lw=1.8, zorder=4)
        ax.add_patch(Ellipse((s * 1.13, 2.92), 0.32, 0.62, fc=POLLEN, ec=INK, lw=0.9, zorder=5))
        for dx, dy in ((0.25, 3.3), (0.35, 3.05), (0.15, 3.45)):
            ax.add_patch(Circle((s * (1.13 + dx), dy), 0.04, fc="#D49A1F", ec="none", zorder=5))
    ax.add_patch(Ellipse((0, 0.95), 1.1, 1.35, fc=LGREEN, ec=INK, lw=1.1, zorder=5))
    for dx, dy in ((-0.2, 0.7), (0.2, 0.7), (-0.2, 1.15), (0.2, 1.15)):
        ax.add_patch(Ellipse((dx, dy), 0.22, 0.32, fc="#F7E7A1", ec=INK, lw=0.7, zorder=6))
    tube_path(ax, [(0, 1.55), (0, 2.3), (0, 3.0)], 0.2, LGREEN, z=5)
    blob(ax, [(-0.35, 3.05), (0, 2.95), (0.35, 3.05), (0.3, 3.3), (0, 3.38), (-0.3, 3.3)], "#E7B85A", z=6)
    L = -3.4
    for xy, t, yt in (((-0.25, 3.2), "stigma", 3.6), ((-0.08, 2.3), "style", 2.5), ((-0.5, 0.95), "ovary", 1.25),
                      ((-0.2, 0.7), "ovule", 0.5), ((-0.7, 0.05), "receptacle", -0.45)):
        label(ax, xy, t, (L, yt), ha="right")
    ax.plot([L - 1.15, L - 1.3, L - 1.3, L - 1.15], [3.6, 3.6, 1.25, 1.25], color=ACC, lw=1.0)
    ax.text(L - 1.4, 2.42, "pistil\n(female)", fontsize=8.5, color=ACC, va="center", ha="right")
    R = 3.5
    for xy, t, yt in (((2.4, 3.3), "petal", 3.9), ((1.25, 2.95), "anther", 2.95), ((0.9, 1.6), "filament", 1.75),
                      ((1.7, 0.55), "sepal", 0.5)):
        label(ax, xy, t, (R, yt))
    ax.plot([R + 1.3, R + 1.45, R + 1.45, R + 1.3], [2.95, 2.95, 1.75, 1.75], color=ACC, lw=1.0)
    ax.text(R + 1.55, 2.35, "stamen\n(male)", fontsize=8.5, color=ACC, va="center")
    finish(ax, (-6.0, 5.8), (-2.1, 4.1))
    save(fig, "sci_ch07_fig06_flower.png")


# Fig 7.7: germination of pollen on the stigma
def fig_pollen_tube():
    fig, ax = plt.subplots(figsize=(5.6, 5.8))
    ax.add_patch(Ellipse((0, 1.3), 2.8, 2.5, fc=LGREEN, ec=INK, lw=1.1))
    tube_path(ax, [(0, 2.45), (0, 3.6), (0, 4.75)], 0.55, LGREEN, z=2)
    blob(ax, [(-0.85, 4.75), (0, 4.6), (0.85, 4.75), (0.75, 5.15), (0, 5.25), (-0.75, 5.15)], "#E7B85A", z=3)
    ax.add_patch(Ellipse((0.35, 1.1), 0.95, 1.4, fc="#F7E7A1", ec=INK, lw=1.0, zorder=3))
    ax.add_patch(Circle((0.35, 0.68), 0.13, fc="#C98FB0", ec=INK, lw=0.7, zorder=4))
    path = smooth([(-0.35, 5.25), (-0.12, 4.6), (0.0, 3.6), (-0.05, 2.4), (-0.75, 1.3), (-0.45, 0.42), (0.3, 0.42)], closed=False)
    ax.plot(path[:, 0], path[:, 1], color=HI, lw=1.8, zorder=5)
    for k in (-14, -8):
        ax.add_patch(Circle(tuple(path[k]), 0.06, fc="#7B4F9E", ec="none", zorder=6))
    for x, y in ((-0.35, 5.38), (0.3, 5.4), (0.62, 5.3)):
        ax.add_patch(Circle((x, y), 0.14, fc=POLLEN, ec=INK, lw=0.8, zorder=6))
    labs = [((0.3, 5.5), "pollen grains", (1.5, 5.9)), ((0.7, 4.95), "stigma", (1.6, 5.0)),
            ((0.27, 3.6), "style", (1.6, 3.7)), ((-0.04, 3.2), "pollen tube", (-1.6, 3.6)),
            ((1.2, 1.7), "ovary", (1.9, 2.4)), ((0.75, 1.35), "ovule", (2.0, 1.6)),
            ((0.45, 0.62), "female germ-cell (egg)", (1.3, -0.2)), (tuple(path[-14]), "male germ-cells", (-1.9, 1.9))]
    for xy, t, xt in labs:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "right")
    finish(ax, (-3.6, 4.0), (-0.4, 6.1))
    save(fig, "sci_ch07_fig07_pollen_tube.png")


# Fig 7.8: parts of a germinating seed
def fig_germination():
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    ax.add_patch(Ellipse((0, 1.6), 3.0, 2.0, fc="none", ec="#8A6A3B", lw=1.6, ls=(0, (5, 2))))
    blob(ax, [(-1.3, 1.6), (-1.0, 2.35), (-0.2, 2.45), (-0.05, 1.6), (-0.2, 0.75), (-1.0, 0.85)], "#F1D9A0", z=2)
    blob(ax, [(1.3, 1.6), (1.0, 2.35), (0.2, 2.45), (0.05, 1.6), (0.2, 0.75), (1.0, 0.85)], "#F1D9A0", z=2)
    tube_path(ax, [(0, 1.6), (0.02, 2.4), (0.05, 3.2), (0.0, 3.6)], 0.14, "#9CCB8A", z=3)
    for s in (-1, 1):
        ax.add_patch(Ellipse((s * 0.22, 3.72), 0.38, 0.18, angle=s * 30, fc="#7DB36B", ec=INK, lw=0.7, zorder=4))
    tube_path(ax, [(0, 1.6), (0.05, 0.8), (0.0, -0.2), (0.1, -1.0)], 0.18, "#F3E8D2", z=3)
    for y in (-0.2, -0.6):
        for s in (-1, 1):
            ax.plot([0.03, s * 0.35], [y, y - 0.25], color="#8A6A3B", lw=0.8)
    labs = [((0.2, 3.72), "plumule (future shoot)", (1.3, 3.9)), ((-0.9, 1.9), "cotyledon (stores food)", (-1.9, 3.1)),
            ((0.08, -0.4), "radicle (future root)", (1.0, -0.7)), ((1.4, 1.1), "seed coat", (2.2, 0.8))]
    for xy, t, xt in labs:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "right")
    finish(ax, (-4.2, 4.4), (-1.2, 4.2))
    save(fig, "sci_ch07_fig08_germination.png")


# Fig 7.9: human male reproductive system (schematic, front view)
def fig_male():
    fig, ax = plt.subplots(figsize=(6.6, 5.8))
    for s in (-1, 1):
        ax.plot([s * 0.45, s * 1.3], [3.55, 4.8], color="#E8C35A", lw=3, zorder=1)
    blob(ax, [(-0.8, 3.0), (-0.5, 3.65), (0.5, 3.65), (0.8, 3.0), (0.5, 2.4), (-0.5, 2.4)], "#F3D58A", z=2)
    for s in (-1, 1):
        blob(ax, [(s * 0.55, 2.55), (s * 0.95, 2.95), (s * 1.15, 2.75), (s * 0.85, 2.25), (s * 0.4, 2.1)], "#C9B6E4", z=3)
    ax.add_patch(Ellipse((0, 1.95), 0.95, 0.55, fc="#D99A8A", ec=INK, lw=1.0, zorder=4))
    blob(ax, [(-1.35, 0.1), (-0.9, 0.55), (0.9, 0.55), (1.35, 0.1), (1.2, -0.9), (0.6, -1.25), (-0.6, -1.25), (-1.2, -0.9)], "#F6E3D6", z=1)
    for s in (-1, 1):
        ax.add_patch(Ellipse((s * 0.75, -0.35), 0.6, 0.85, fc="#9FB8D9", ec=INK, lw=1.0, zorder=2))
        vd = smooth([(s * 0.85, 0.05), (s * 1.4, 1.0), (s * 1.75, 2.6), (s * 1.5, 3.85), (s * 1.0, 3.8), (s * 0.95, 3.1),
                     (s * 0.5, 2.25), (s * 0.12, 1.95)], closed=False)
        ax.plot(vd[:, 0], vd[:, 1], color="#7B4F9E", lw=2.0, zorder=5)
    tube_path(ax, [(0, 1.65), (0, 0.2), (0, -1.6)], 0.5, FLESH, z=3)
    ax.plot([0, 0], [2.35, -1.6], color="#C9A227", lw=2.2, zorder=6)
    labs = [((1.2, 4.65), "ureter", (2.3, 4.9)), ((0.5, 3.25), "urinary bladder", (2.3, 4.2)),
            ((1.72, 2.6), "vas deferens (sperm duct)", (2.3, 3.4)), ((1.0, 2.6), "seminal vesicle", (2.3, 2.65)),
            ((0.45, 1.95), "prostate gland", (2.3, 1.95)), ((0.0, 0.6), "urethra", (2.3, 1.1)),
            ((0.2, -1.2), "penis", (2.3, -1.4)), ((-0.9, -0.4), "testis", (-2.2, 0.1)), ((-1.2, -0.95), "scrotum", (-2.2, -1.1))]
    for xy, t, xt in labs:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "right")
    finish(ax, (-3.6, 5.6), (-1.8, 5.2))
    save(fig, "sci_ch07_fig09_male.png")


# Fig 7.10: human female reproductive system (schematic, front view)
def fig_female():
    fig, ax = plt.subplots(figsize=(6.8, 5.0))
    for s in (-1, 1):
        tube_path(ax, [(s * 0.85, 2.9), (s * 1.6, 3.35), (s * 2.4, 3.35), (s * 2.9, 2.85)], 0.17, "#E9A1A6", z=2)
        fan = [(s * 2.85, 2.95), (s * 3.25, 2.75), (s * 3.2, 2.35), (s * 2.95, 2.45), (s * 2.75, 2.7)]
        blob(ax, fan, "#E9A1A6", z=3)
        ax.add_patch(Ellipse((s * 2.3, 2.2), 0.8, 0.5, fc="#F3D58A", ec=INK, lw=1.0, zorder=3))
        for dx in (-0.15, 0.12):
            ax.add_patch(Circle((s * (2.3 + dx), 2.22), 0.07, fc="#FFF4D6", ec=INK, lw=0.5, zorder=4))
    blob(ax, [(-1.0, 3.0), (0, 3.2), (1.0, 3.0), (0.85, 2.0), (0.45, 1.1), (0.22, 0.8), (-0.22, 0.8), (-0.45, 1.1), (-0.85, 2.0)], "#E9A1A6", z=4)
    blob(ax, [(-0.55, 2.8), (0.55, 2.8), (0.12, 1.2), (-0.12, 1.2)], "#F6D3D6", z=5)
    tube_path(ax, [(0, 0.85), (0, 0.0), (0, -0.9)], 0.5, FLESH, z=3)
    labs = [((1.6, 3.42), "oviduct (fallopian tube)", (2.0, 4.1)), ((3.2, 2.5), "funnel of the oviduct", (3.6, 3.1)),
            ((2.6, 2.1), "ovary", (3.6, 1.7)), ((-0.3, 2.3), "uterus", (-2.4, 1.3)), ((0.0, 0.85), "cervix", (-2.4, 0.6)),
            ((0.0, -0.4), "vagina", (-2.4, -0.4))]
    for xy, t, xt in labs:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "right")
    finish(ax, (-4.0, 6.0), (-1.1, 4.4))
    save(fig, "sci_ch07_fig10_female.png")


if __name__ == "__main__":
    fig_fission()
    fig_fragment_regen()
    fig_budding()
    fig_bryophyllum()
    fig_rhizopus()
    fig_flower()
    fig_pollen_tube()
    fig_germination()
    fig_male()
    fig_female()
