"""Figures for Class X Science, Chapter 5: Life Processes.
Run: python x_sci_ch05_life_processes.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
Schematic, clearly labelled diagrams in the style students are expected to draw.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Science", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, SHADE = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#BFD3E6"
PINK, RED, BLUE, GREEN, LGREEN, TAN = "#F4C7C3", "#C0392B", "#2E6DB4", "#3E8E41", "#CDE8C5", "#E9D3A8"
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


def label(ax, xy, text, xytext, ha="left", size=8.5):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=size, color=INK, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7), annotation_clip=False)


def smooth(pts, closed=True, n=16):
    """Catmull-Rom spline through the points."""
    P = np.array(pts, dtype=float)
    if closed:
        P = np.vstack([P[-1], P, P[0], P[1]])
    else:
        P = np.vstack([P[0], P, P[-1]])
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for t in np.linspace(0, 1, n, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    if not closed:
        out.append(P[-2])
    return np.array(out)


def blob(ax, pts, fc, ec=INK, lw=1.1, z=1):
    s = smooth(pts)
    ax.add_patch(Polygon(s, closed=True, fc=fc, ec=ec, lw=lw, zorder=z))


def tube_path(ax, pts, width, fc, ec=INK, lw=1.0, z=1):
    """A tube of given width following a smooth path."""
    c = smooth(pts, closed=False)
    d = np.gradient(c, axis=0)
    nrm = np.c_[-d[:, 1], d[:, 0]]
    nrm /= np.linalg.norm(nrm, axis=1)[:, None]
    left, right = c + nrm * width / 2, c - nrm * width / 2
    poly = np.vstack([left, right[::-1]])
    ax.add_patch(Polygon(poly, closed=True, fc=fc, ec=ec, lw=lw, zorder=z))


# Fig 5.1: cross-section of a leaf
def fig_leaf_section():
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    ax.add_patch(Rectangle((0, 3.3), 8, 0.12, fc="#F6F1D5", ec=INK, lw=0.8))
    for k in range(16):
        ax.add_patch(Rectangle((0.02 + k * 0.5, 2.9), 0.46, 0.4, fc="#F6F1D5", ec=INK, lw=0.6))
    for k in range(20):
        x = 0.05 + k * 0.4
        ax.add_patch(FancyBboxPatch((x, 1.75), 0.32, 1.1, boxstyle="round,pad=0.01,rounding_size=0.12", fc=LGREEN, ec=GREEN, lw=0.6))
        for j in range(3):
            ax.add_patch(Circle((x + 0.16, 1.95 + j * 0.35), 0.06, fc=GREEN, ec="none"))
    rng = np.random.default_rng(3)
    for k in range(14):
        x, y = 0.4 + k * 0.55 + rng.uniform(-0.1, 0.1), 1.15 + rng.uniform(-0.25, 0.25)
        if 3.4 < x < 4.6:
            continue
        ax.add_patch(Ellipse((x, y), 0.45, 0.32, angle=rng.uniform(0, 60), fc=LGREEN, ec=GREEN, lw=0.6))
        ax.add_patch(Circle((x, y), 0.05, fc=GREEN, ec="none"))
    ax.add_patch(Ellipse((4.0, 1.25), 1.1, 0.75, fc="#EADFB4", ec=INK, lw=0.8))
    ax.add_patch(Ellipse((4.0, 1.42), 0.7, 0.3, fc="#B9D3EE", ec=INK, lw=0.6))
    ax.add_patch(Ellipse((4.0, 1.08), 0.7, 0.28, fc="#F3C9A3", ec=INK, lw=0.6))
    for k in range(16):
        if k in (5, 6):
            continue
        ax.add_patch(Rectangle((0.02 + k * 0.5, 0.25), 0.46, 0.38, fc="#F6F1D5", ec=INK, lw=0.6))
    ax.add_patch(Ellipse((2.85, 0.44), 0.32, 0.36, fc=LGREEN, ec=GREEN, lw=0.8))
    ax.add_patch(Ellipse((3.35, 0.44), 0.32, 0.36, fc=LGREEN, ec=GREEN, lw=0.8))
    ax.add_patch(Rectangle((0, 0.13), 8, 0.12, fc="#F6F1D5", ec=INK, lw=0.8))
    label(ax, (1.0, 3.36), "cuticle", (8.3, 3.55))
    label(ax, (2.0, 3.1), "upper epidermis", (8.3, 3.1))
    label(ax, (2.2, 2.3), "palisade cells (with chloroplasts)", (8.3, 2.45))
    label(ax, (6.0, 1.2), "spongy cells with air spaces", (8.3, 1.55))
    label(ax, (4.0, 1.45), "xylem", (8.3, 1.1))
    label(ax, (4.2, 1.05), "phloem", (8.3, 0.75))
    label(ax, (5.0, 0.45), "lower epidermis", (8.3, 0.35))
    label(ax, (3.1, 0.3), "stoma with guard cells", (8.3, 0.0))
    finish(ax, (-0.2, 11.6), (-0.2, 3.7))
    save(fig, "sci_ch05_fig01_leaf_section.png")


# Fig 5.2: open and closed stomata
def fig_stomata():
    fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.0))
    for ax, open_ in zip(axs, (True, False)):
        gap = 0.35 if open_ else 0.04
        for side in (-1, 1):
            cx = side * (0.42 + gap / 2)
            ax.add_patch(Ellipse((cx, 0), 0.8, 2.0, fc=LGREEN, ec=GREEN, lw=1.2))
            ax.add_patch(Circle((cx + side * 0.12, 0.1), 0.12, fc="#9ACD8C", ec=GREEN, lw=0.6))
            for k in range(4):
                ax.add_patch(Circle((cx + side * 0.15, -0.55 + k * 0.32), 0.05, fc=GREEN, ec="none"))
        if open_:
            ax.add_patch(Ellipse((0, 0), gap + 0.12, 1.2, fc="white", ec=INK, lw=0.6))
        ax.text(0, -1.45, "(a) open stomatal pore" if open_ else "(b) closed stomatal pore", ha="center", fontsize=9)
        finish(ax, (-1.6, 1.6), (-1.7, 1.3))
    label(axs[0], (-0.55, 0.6), "guard cell", (-1.55, 1.15))
    label(axs[0], (0, 0.4), "stomatal pore", (0.6, 1.15))
    label(axs[0], (0.6, -0.55), "chloroplast", (0.9, -1.0))
    label(axs[0], (-0.45, 0.1), "nucleus", (-1.55, -0.6))
    save(fig, "sci_ch05_fig02_stomata.png")


# Fig 5.3: variegated leaf before and after the starch test
def fig_variegated():
    fig, axs = plt.subplots(1, 2, figsize=(6.2, 3.0))
    outline = [(0, -1.6), (0.9, -0.6), (1.0, 0.5), (0.4, 1.4), (0, 1.7), (-0.4, 1.4), (-1.0, 0.5), (-0.9, -0.6)]
    inner = [(0, -1.0), (0.55, -0.3), (0.55, 0.6), (0.15, 1.1), (-0.15, 1.1), (-0.55, 0.6), (-0.55, -0.3)]
    for ax, (outer_c, inner_c, title) in zip(axs, ((("#F5F1D0"), GREEN, "(a) before: green and white areas"),
                                                 (("#F5F1D0"), "#20304A", "(b) after the iodine test"))):
        blob(ax, outline, outer_c)
        blob(ax, inner, inner_c, ec="none")
        ax.plot([0, 0], [-1.9, 1.5], color=GREY, lw=1.0)
        ax.text(0, -2.3, title, ha="center", fontsize=8.5)
        finish(ax, (-1.6, 1.6), (-2.6, 1.9))
    label(axs[0], (0.3, 0.2), "green area\n(has chlorophyll)", (1.1, 1.3))
    label(axs[0], (0.8, -0.6), "white area", (1.1, -1.4))
    label(axs[1], (0.3, 0.2), "blue-black:\nstarch present", (1.1, 1.3))
    label(axs[1], (0.8, -0.6), "no starch", (1.1, -1.4))
    save(fig, "sci_ch05_fig03_variegated.png")


# Fig 5.4: KOH experiment (Activity 5.2)
def fig_koh():
    fig, axs = plt.subplots(1, 2, figsize=(6.6, 3.4))
    for ax, koh in zip(axs, (True, False)):
        ax.add_patch(Rectangle((-1.6, -0.15), 3.2, 0.15, fc=SOFT, ec=INK, lw=0.9))
        jar = [(-1.3, 0), (-1.3, 2.4), (-1.0, 2.9), (1.0, 2.9), (1.3, 2.4), (1.3, 0)]
        ax.plot(*smooth(jar, closed=False).T, color=ACC, lw=1.4)
        ax.add_patch(Polygon([[-0.45, 0], [-0.35, 0.7], [0.35, 0.7], [0.45, 0]], closed=True, fc="#B5743B", ec=INK, lw=0.9))
        ax.plot([0, 0], [0.7, 1.9], color=GREEN, lw=1.6)
        for side in (-1, 1):
            for hh in (1.1, 1.5, 1.85):
                ax.add_patch(Ellipse((side * 0.25, hh), 0.45, 0.18, angle=side * 25, fc=GREEN, ec="none"))
        if koh:
            ax.add_patch(Ellipse((0.85, 0.08), 0.5, 0.14, fc="white", ec=INK, lw=0.8))
            label(ax, (0.85, 0.12), "watch-glass with\npotassium hydroxide", (0.4, 3.5))
        ax.text(0, -0.6, "(a) with KOH: no CO₂ inside" if koh else "(b) without KOH", ha="center", fontsize=8.5)
        finish(ax, (-1.8, 2.0), (-0.9, 3.9))
    label(axs[1], (1.25, 1.5), "bell-jar", (1.6, 2.6))
    label(axs[1], (-1.3, 0.02), "vaseline seal on\nglass plate", (-1.75, 3.55))
    save(fig, "sci_ch05_fig04_koh.png")


# Fig 5.5: nutrition in Amoeba
def fig_amoeba():
    fig, axs = plt.subplots(1, 4, figsize=(9.0, 2.6))
    stages = [
        [(-1.0, 0), (-0.6, 0.6), (0.2, 0.7), (0.5, 0.2), (0.3, -0.5), (-0.5, -0.6)],
        [(-1.0, 0), (-0.6, 0.6), (0.3, 0.8), (1.0, 0.6), (0.6, 0.1), (1.0, -0.5), (0.3, -0.6), (-0.5, -0.6)],
        [(-1.0, 0), (-0.6, 0.6), (0.3, 0.7), (1.0, 0.5), (1.2, 0.0), (1.0, -0.5), (0.3, -0.6), (-0.5, -0.6)],
        [(-1.0, 0), (-0.6, 0.6), (0.3, 0.6), (0.9, 0.3), (0.9, -0.3), (0.3, -0.6), (-0.5, -0.6)],
    ]
    titles = ["food particle near\nAmoeba", "pseudopodia surround\nthe food", "food vacuole forms", "food digested;\nwaste thrown out"]
    for k, (ax, st, t) in enumerate(zip(axs, stages, titles)):
        blob(ax, st, "#EAF2F8", ec=ACC)
        ax.add_patch(Circle((-0.4, 0.05), 0.15, fc="#C9A9DC", ec=INK, lw=0.6))
        if k == 0:
            ax.add_patch(Circle((1.0, 0.1), 0.12, fc=HI, ec=INK, lw=0.6))
        elif k == 1:
            ax.add_patch(Circle((0.95, 0.1), 0.12, fc=HI, ec=INK, lw=0.6))
        elif k == 2:
            ax.add_patch(Circle((0.75, 0.0), 0.22, fc="white", ec=INK, lw=0.6))
            ax.add_patch(Circle((0.75, 0.0), 0.11, fc=HI, ec="none"))
        else:
            ax.add_patch(Circle((0.3, 0.0), 0.2, fc="white", ec=INK, lw=0.6))
            ax.add_patch(Circle((0.3, 0.0), 0.05, fc=HI, ec="none"))
            ax.annotate("", xy=(1.4, -0.4), xytext=(0.9, -0.3), arrowprops=dict(arrowstyle="->", color=HI, lw=1))
        ax.text(0.1, -1.2, t, ha="center", fontsize=8)
        finish(ax, (-1.3, 1.5), (-1.6, 1.0))
    label(axs[0], (-0.4, 0.05), "nucleus", (-1.2, 0.9))
    label(axs[2], (0.75, 0.0), "food vacuole", (0.5, 0.95))
    save(fig, "sci_ch05_fig05_amoeba.png")


# Fig 5.6: human alimentary canal
def fig_alimentary():
    fig, ax = plt.subplots(figsize=(6.6, 7.4))
    # head outline (mouth region)
    ax.plot(*smooth([(-0.6, 8.6), (-0.2, 9.4), (0.8, 9.6), (1.4, 9.0), (1.3, 8.3), (0.9, 7.9)], closed=False).T, color=GREY, lw=1.0)
    ax.add_patch(Ellipse((1.15, 8.45), 0.45, 0.18, fc="#E58C8A", ec=INK, lw=0.8))
    ax.add_patch(Ellipse((0.55, 8.15), 0.4, 0.22, fc=TAN, ec=INK, lw=0.7))
    # oesophagus
    tube_path(ax, [(0.7, 8.2), (0.5, 7.4), (0.45, 6.4), (0.5, 5.6)], 0.22, PINK)
    # liver
    blob(ax, [(-1.6, 5.4), (-0.4, 5.9), (0.6, 5.5), (0.4, 4.8), (-0.6, 4.6), (-1.5, 4.7)], "#A9583F")
    ax.add_patch(Ellipse((-0.55, 4.6), 0.35, 0.25, fc="#6E9F4F", ec=INK, lw=0.7))
    # stomach
    blob(ax, [(0.45, 5.6), (1.0, 5.75), (1.6, 5.5), (1.8, 4.9), (1.5, 4.3), (0.9, 4.15), (0.5, 4.4), (0.9, 4.7), (1.2, 5.0), (0.8, 5.2)], PINK)
    # pancreas
    blob(ax, [(0.2, 4.08), (0.9, 4.12), (1.6, 4.02), (1.6, 3.86), (0.9, 3.9), (0.2, 3.92)], "#F1C27D", z=5)
    # small intestine: duodenum then coils
    tube_path(ax, [(0.55, 4.3), (0.1, 4.0), (0.0, 3.6), (0.4, 3.4)], 0.2, "#F2B8A2")
    for k in range(4):
        y = 3.25 - k * 0.38
        xs = [(-0.6, y), (0.2, y + 0.05), (1.0, y), (1.2, y - 0.19)] if k % 2 == 0 else [(1.2, y), (0.2, y - 0.05), (-0.6, y), (-0.8, y - 0.19)]
        tube_path(ax, xs, 0.24, "#F2B8A2")
    # large intestine (frame)
    tube_path(ax, [(-0.9, 1.5), (-1.3, 1.5), (-1.4, 2.4), (-1.4, 3.4), (-1.0, 3.7), (0.2, 3.75), (1.5, 3.7), (1.9, 3.4), (1.9, 2.2), (1.7, 1.4), (1.1, 1.0)], 0.38, "#D9A27C")
    # rectum and anus
    tube_path(ax, [(1.1, 1.0), (0.6, 0.85), (0.4, 0.5), (0.4, 0.15)], 0.3, "#D9A27C")
    # appendix
    tube_path(ax, [(-1.35, 1.6), (-1.5, 1.2), (-1.45, 1.0)], 0.1, "#D9A27C")
    labels = [((1.15, 8.45), "mouth (buccal cavity)", (2.6, 9.3)),
              ((0.55, 8.15), "salivary glands", (-2.8, 8.7)),
              ((0.48, 7.0), "oesophagus (food pipe)", (2.6, 7.4)),
              ((-1.0, 5.2), "liver", (-2.8, 6.0)),
              ((-0.55, 4.6), "gall bladder", (-2.8, 4.7)),
              ((1.4, 5.1), "stomach", (2.6, 5.6)),
              ((1.4, 3.88), "pancreas", (2.6, 4.4)),
              ((0.4, 2.5), "small intestine", (2.6, 2.9)),
              ((1.9, 2.4), "large intestine", (2.6, 2.0)),
              ((-1.45, 1.05), "appendix", (-2.8, 1.0)),
              ((0.6, 0.85), "rectum", (2.6, 0.9)),
              ((0.4, 0.15), "anus", (2.6, 0.2))]
    for xy, t, xt in labels:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "right", size=9)
    finish(ax, (-4.4, 5.2), (-0.1, 9.9))
    save(fig, "sci_ch05_fig06_alimentary.png")


# Fig 5.7: break-down of glucose by various pathways
def fig_glucose_pathways():
    fig, ax = plt.subplots(figsize=(7.6, 3.6))

    def b(x, y, w, t, fc=SOFT):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - 0.32), w, 0.64, boxstyle="round,pad=0.03,rounding_size=0.1", fc=fc, ec=ACC, lw=1.0))
        ax.text(x, y, t, ha="center", va="center", fontsize=8.5, color=INK)

    def arr(a, c, t=None, side=0.0):
        ax.annotate("", xy=c, xytext=a, arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
        if t:
            ax.text((a[0] + c[0]) / 2 + side, (a[1] + c[1]) / 2, t, ha="center", va="center", fontsize=7.8, color=HI)

    b(-0.2, 2.0, 2.4, "Glucose (6-carbon)", HI)
    b(3.0, 2.0, 2.2, "Pyruvate (3-carbon)\n+ energy")
    arr((1.0, 2.0), (1.9, 2.0))
    ax.text(1.45, 2.35, "in cytoplasm", ha="center", fontsize=7.8, color=HI)
    b(7.4, 3.4, 3.2, "Ethanol + CO₂ + energy\n(yeast: fermentation)")
    b(7.4, 2.0, 3.2, "CO₂ + H₂O + energy\n(aerobic, in mitochondria)")
    b(7.4, 0.6, 3.2, "Lactic acid + energy\n(muscle cells)")
    arr((4.1, 2.25), (5.8, 3.3))
    arr((4.1, 2.0), (5.8, 2.0))
    arr((4.1, 1.75), (5.8, 0.7))
    ax.text(4.75, 3.05, "absence of oxygen", ha="center", fontsize=7.8, color=HI, rotation=30)
    ax.text(4.95, 2.2, "presence of oxygen", ha="center", fontsize=7.8, color=HI)
    ax.text(4.75, 0.95, "lack of oxygen", ha="center", fontsize=7.8, color=HI, rotation=-32)
    finish(ax, (-1.6, 9.2), (0.0, 4.0))
    save(fig, "sci_ch05_fig07_glucose_pathways.png")


# Fig 5.8: human respiratory system
def fig_respiratory():
    fig, ax = plt.subplots(figsize=(6.8, 6.0))
    # nasal cavity / throat
    ax.plot(*smooth([(-0.5, 7.4), (0.0, 7.9), (0.6, 7.8), (0.8, 7.3)], closed=False).T, color=GREY, lw=1.0)
    ax.add_patch(Ellipse((0.3, 7.45), 0.7, 0.25, fc=PINK, ec=INK, lw=0.7))
    tube_path(ax, [(0.15, 7.3), (0.1, 6.8), (0.0, 6.4)], 0.28, PINK)
    # trachea with cartilage rings
    ax.add_patch(Rectangle((-0.17, 4.4), 0.34, 2.0, fc="#F7E3DE", ec=INK, lw=0.9))
    for k in range(9):
        ax.plot([-0.17, 0.17], [4.55 + k * 0.2, 4.55 + k * 0.2], color=GREY, lw=1.2)
    # bronchi
    tube_path(ax, [(0.0, 4.45), (-0.6, 4.0), (-1.1, 3.6)], 0.22, "#F7E3DE")
    tube_path(ax, [(0.0, 4.45), (0.6, 4.0), (1.1, 3.6)], 0.22, "#F7E3DE")
    # lungs
    blob(ax, [(-0.4, 4.8), (-1.2, 5.1), (-2.2, 4.3), (-2.5, 2.6), (-2.2, 1.5), (-0.6, 1.6), (-0.35, 2.6)], "#F2A7A0", z=0)
    blob(ax, [(0.4, 4.8), (1.2, 5.1), (2.2, 4.3), (2.5, 2.6), (2.2, 1.5), (0.7, 1.6), (0.45, 2.6)], "#F2A7A0", z=0)
    # bronchioles in left lung
    for (x1, y1, x2, y2) in ((-1.1, 3.6, -1.6, 3.0), (-1.1, 3.6, -0.9, 2.6), (-1.6, 3.0, -1.9, 2.4), (-1.6, 3.0, -1.4, 2.2)):
        ax.plot([x1, x2], [y1, y2], color="#B5524A", lw=1.4)
    for x, y in ((-1.9, 2.4), (-1.4, 2.2), (-0.9, 2.6)):
        for dx, dy in ((0, -0.12), (0.1, 0.0), (-0.1, 0.0)):
            ax.add_patch(Circle((x + dx, y + dy), 0.08, fc="#FADBD8", ec="#B5524A", lw=0.6))
    # diaphragm
    ax.plot(*smooth([(-2.6, 1.2), (-1.3, 1.45), (0, 1.0), (1.3, 1.45), (2.6, 1.2)], closed=False).T, color=INK, lw=2.0)
    # ribs
    for k in range(4):
        ax.plot(*smooth([(-2.7, 4.2 - k * 0.8), (-2.85, 3.8 - k * 0.8), (-2.7, 3.4 - k * 0.8)], closed=False).T, color=TAN, lw=2)
        ax.plot(*smooth([(2.7, 4.2 - k * 0.8), (2.85, 3.8 - k * 0.8), (2.7, 3.4 - k * 0.8)], closed=False).T, color=TAN, lw=2)
    labels = [((0.3, 7.45), "nasal passage", (1.5, 7.8)), ((0.05, 6.6), "pharynx and larynx", (1.5, 7.0)),
              ((0.17, 5.4), "trachea (wind pipe)\nwith rings of cartilage", (1.5, 6.1)),
              ((0.6, 4.0), "bronchus", (3.2, 4.8)), ((-1.6, 3.0), "bronchioles", (-3.2, 3.6)),
              ((-1.95, 2.35), "alveolar sacs", (-3.2, 2.2)), ((2.0, 3.0), "lung", (3.2, 3.3)),
              ((2.75, 2.6), "ribs", (3.2, 2.4)), ((1.3, 1.42), "diaphragm", (3.2, 1.4))]
    for xy, t, xt in labels:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "right", size=9)
    finish(ax, (-5.0, 5.4), (0.7, 8.1))
    save(fig, "sci_ch05_fig08_respiratory.png")


# Fig 5.9: sectional view of the human heart
def fig_heart():
    fig, ax = plt.subplots(figsize=(6.8, 5.6))
    # outer wall
    blob(ax, [(-1.6, 2.6), (0.0, 3.0), (1.6, 2.6), (2.0, 1.0), (1.2, -1.2), (0.0, -2.3), (-1.2, -1.2), (-2.0, 1.0)], "#E8A39B", z=0)
    # chambers (viewer's left = right side of the heart)
    blob(ax, [(-1.5, 2.3), (-0.3, 2.4), (-0.25, 1.2), (-1.5, 1.1)], "#9FB8D9", z=1)          # right atrium
    blob(ax, [(0.3, 2.4), (1.5, 2.3), (1.5, 1.1), (0.25, 1.2)], "#E79A93", z=1)              # left atrium
    blob(ax, [(-1.5, 0.85), (-0.25, 0.9), (-0.25, -1.5), (-0.9, -1.0)], "#9FB8D9", z=1)      # right ventricle
    blob(ax, [(0.25, 0.9), (1.6, 0.85), (1.0, -1.0), (0.25, -1.7)], "#E79A93", z=1)          # left ventricle
    # septum
    ax.plot([0, 0], [2.6, -2.0], color=INK, lw=2.4, zorder=2)
    # valves
    for x in (-0.85, 0.85):
        ax.plot([x - 0.35, x], [1.0, 0.75], color=INK, lw=1.4, zorder=3)
        ax.plot([x + 0.35, x], [1.0, 0.75], color=INK, lw=1.4, zorder=3)
    # vessels
    ax.add_patch(Rectangle((-1.45, 2.4), 0.45, 1.4, fc="#9FB8D9", ec=INK, lw=0.9, zorder=0))        # superior vena cava
    ax.add_patch(Rectangle((-1.45, -1.1), 0.4, 0.6, fc="#9FB8D9", ec=INK, lw=0.9, zorder=0))
    ax.plot(*smooth([(0.2, 2.6), (0.4, 3.8), (1.2, 4.1), (1.9, 3.7), (2.0, 3.2)], closed=False).T, color=RED, lw=9, zorder=0, solid_capstyle="round")
    ax.plot(*smooth([(-0.4, 2.6), (-0.6, 3.4), (-1.4, 3.6), (-2.4, 3.5)], closed=False).T, color=BLUE, lw=7, zorder=0, solid_capstyle="round")
    ax.plot([1.5, 2.6], [2.0, 2.3], color=RED, lw=6, zorder=0)
    ax.plot([1.5, 2.6], [1.6, 1.4], color=RED, lw=6, zorder=0)
    labels = [((-1.2, 3.5), "superior vena cava\n(from upper body)", (-3.2, 4.3)),
              ((-1.25, -0.9), "inferior vena cava\n(from lower body)", (-3.2, -1.6)),
              ((-1.8, 3.55), "pulmonary artery\n(to lungs)", (-3.2, 2.9)),
              ((1.2, 4.1), "aorta (to body)", (2.3, 4.6)),
              ((2.3, 2.2), "pulmonary veins\n(from lungs)", (3.0, 2.9)),
              ((-0.9, 1.8), "right atrium", (-3.2, 1.6)),
              ((-0.8, 0.0), "right ventricle", (-3.2, 0.3)),
              ((0.9, 1.8), "left atrium", (3.0, 1.0)),
              ((0.8, -0.2), "left ventricle\n(thickest wall)", (3.0, -0.3)),
              ((0.85, 0.78), "valves", (3.0, 0.35)),
              ((0.0, -1.0), "septum", (1.0, -2.4))]
    for xy, t, xt in labels:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "right", size=8.5)
    ax.text(0, -2.9, "Blue: deoxygenated blood (right side)   Red: oxygenated blood (left side)", ha="center", fontsize=8, color=INK)
    finish(ax, (-5.0, 5.2), (-3.2, 5.0))
    save(fig, "sci_ch05_fig09_heart.png")


# Fig 5.10: double circulation
def fig_double_circulation():
    fig, ax = plt.subplots(figsize=(6.0, 5.2))
    ax.add_patch(FancyBboxPatch((-1.4, 3.8), 2.8, 0.8, boxstyle="round,pad=0.05,rounding_size=0.2", fc="#F2A7A0", ec=INK, lw=1.0))
    ax.text(0, 4.2, "lungs\nblood takes O₂, gives CO₂", ha="center", va="center", fontsize=8)
    ax.add_patch(FancyBboxPatch((-1.4, -1.6), 2.8, 0.8, boxstyle="round,pad=0.05,rounding_size=0.2", fc=TAN, ec=INK, lw=1.0))
    ax.text(0, -1.2, "body organs\nblood gives O₂, takes CO₂", ha="center", va="center", fontsize=8)
    for (x, y, t, c) in ((-0.55, 2.0, "RA", "#9FB8D9"), (0.55, 2.0, "LA", "#E79A93"), (-0.55, 0.9, "RV", "#9FB8D9"), (0.55, 0.9, "LV", "#E79A93")):
        ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1.0, 1.0, fc=c, ec=INK, lw=1.0))
        ax.text(x, y, t, ha="center", va="center", fontsize=10, fontweight="bold")
    ax.text(0, 2.75, "heart", ha="center", fontsize=9)

    def path(pts, col):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=col, lw=2.2)
        ax.annotate("", xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle="->", color=col, lw=2.2))

    path([(-0.55, 0.4), (-0.55, 0.2), (-2.3, 0.2), (-2.3, 4.2), (-1.45, 4.2)], BLUE)
    path([(1.45, 4.2), (2.3, 4.2), (2.3, 2.0), (1.05, 2.0)], RED)
    path([(0.55, 0.4), (0.55, -0.1), (1.0, -0.1), (1.0, -0.75)], RED)
    path([(-1.0, -0.75), (-1.0, -0.2), (-1.6, -0.2), (-1.6, 2.0), (-1.05, 2.0)], BLUE)
    ax.text(-2.45, 2.2, "pulmonary\nartery", ha="right", fontsize=8, color=BLUE)
    ax.text(2.45, 3.1, "pulmonary\nveins", ha="left", fontsize=8, color=RED)
    ax.text(1.1, -0.35, "aorta", ha="left", fontsize=8, color=RED)
    ax.text(-1.7, 1.0, "vena\ncava", ha="right", fontsize=8, color=BLUE)
    ax.text(0, -2.2, "Blood passes through the heart twice in one complete circuit", ha="center", fontsize=8.5, color=HI)
    finish(ax, (-3.6, 3.6), (-2.5, 4.9))
    save(fig, "sci_ch05_fig10_double_circulation.png")


# Fig 5.11: movement of water during transpiration in a tree
def fig_transpiration():
    fig, ax = plt.subplots(figsize=(5.6, 5.4))
    ax.add_patch(Rectangle((-3, -0.2), 6, 0.2, fc="#8B6B45", ec="none"))
    blob(ax, [(-2.2, 3.4), (-1.0, 4.6), (0.6, 4.8), (2.0, 4.0), (2.2, 2.9), (1.0, 2.4), (-1.2, 2.5)], "#7DBF72", ec=GREEN)
    ax.add_patch(Polygon([[-0.25, 0], [-0.18, 2.6], [0.18, 2.6], [0.25, 0]], closed=True, fc="#9B6B3E", ec=INK, lw=0.9))
    for x0 in (-1.2, -0.6, 0.5, 1.1):
        ax.plot(*smooth([(0, 0), (x0 * 0.5, -0.5), (x0, -1.2)], closed=False).T, color="#9B6B3E", lw=1.6)
    for k in range(4):
        ax.annotate("", xy=(0, 0.6 + k * 0.5 + 0.35), xytext=(0, 0.6 + k * 0.5), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.4))
    for x, y in ((-1.4, 4.4), (0.3, 5.0), (1.8, 4.3)):
        ax.annotate("", xy=(x + 0.2, y + 0.6), xytext=(x, y), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2, ls="--"))
    for x0 in (-1.2, 0.5):
        ax.annotate("", xy=(x0 * 0.6, -0.7), xytext=(x0, -1.25), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    label(ax, (0.3, 5.4), "water vapour lost from\nleaves (transpiration pull)", (1.4, 6.0))
    label(ax, (0.05, 1.6), "water moves up\nin xylem", (1.2, 1.6))
    label(ax, (0.9, -1.0), "water and minerals\nabsorbed by roots", (1.4, -1.0))
    finish(ax, (-3.0, 4.4), (-1.6, 6.6))
    save(fig, "sci_ch05_fig11_transpiration.png")


# Fig 5.12: excretory system in human beings
def fig_excretory():
    fig, ax = plt.subplots(figsize=(6.6, 5.4))
    ax.add_patch(Rectangle((-0.22, -0.2), 0.18, 4.6, fc=RED, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((0.04, -0.2), 0.2, 4.6, fc=BLUE, ec=INK, lw=0.8))
    for side, cx in ((-1, -1.3), (1, 1.3)):
        blob(ax, [(cx - 0.45, 3.4), (cx, 3.75), (cx + 0.45, 3.4), (cx + 0.5, 2.6), (cx + 0.4, 1.9), (cx, 1.6),
                  (cx - 0.45, 1.9), (cx - 0.5, 2.6)], "#B5524A", z=2)
        ax.plot([-0.13, cx], [2.85, 2.85], color=RED, lw=3, zorder=1)
        ax.plot([0.14, cx], [2.55, 2.55], color=BLUE, lw=3, zorder=1)
        ax.plot(*smooth([(cx - side * 0.1, 2.0), (cx * 0.8, 1.3), (cx * 0.45, 0.6), (side * 0.25, 0.25)], closed=False).T, color="#E8C35A", lw=2.5, zorder=1)
    blob(ax, [(-0.6, 0.4), (0.0, 0.6), (0.6, 0.4), (0.55, -0.3), (0.0, -0.6), (-0.55, -0.3)], "#F3D58A", z=3)
    ax.plot([0, 0], [-0.6, -1.3], color="#E8C35A", lw=3)
    labels = [((-1.3, 2.7), "kidney", (-3.0, 3.6)), ((-0.13, 3.8), "aorta", (-3.0, 4.3)), ((0.14, 3.8), "vena cava", (2.2, 4.3)),
              ((-0.7, 2.85), "renal artery", (-3.0, 2.85)), ((0.7, 2.55), "renal vein", (2.2, 2.7)),
              ((0.85, 1.2), "ureter", (2.2, 1.5)), ((0.4, 0.0), "urinary bladder", (2.2, 0.2)), ((0.0, -1.1), "urethra", (2.2, -1.0))]
    for xy, t, xt in labels:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "right", size=9)
    finish(ax, (-4.6, 4.6), (-1.6, 4.6))
    save(fig, "sci_ch05_fig12_excretory.png")


# Fig 5.13: structure of a nephron
def fig_nephron():
    fig, ax = plt.subplots(figsize=(6.6, 5.6))
    # Bowman's capsule with glomerulus
    ax.add_patch(Circle((0, 4.0), 0.75, fc="#F7E3DE", ec=INK, lw=1.2))
    ax.add_patch(Circle((0, 4.0), 0.5, fc="white", ec="none"))
    for k in range(10):
        a = 2 * math.pi * k / 10
        ax.add_patch(Circle((0.25 * math.cos(a), 4.0 + 0.25 * math.sin(a)), 0.12, fc="#E06A5F", ec="#8E2B22", lw=0.5))
    ax.plot([-1.2, -0.2], [4.6, 4.15], color=RED, lw=3)
    ax.plot([0.2, 1.1], [4.15, 4.6], color="#9B3B6E", lw=2.5)
    # tubule
    tube_path(ax, [(0.6, 3.55), (1.3, 3.3), (1.0, 2.9), (1.6, 2.6), (1.2, 2.2), (1.4, 1.6), (1.35, 0.2), (1.2, -0.6),
                   (1.6, -0.6), (1.75, 0.2), (1.8, 1.5), (2.2, 2.3), (2.8, 2.6), (2.6, 3.1), (3.2, 3.4), (3.6, 3.4)], 0.22, "#F7E3DE")
    ax.add_patch(Rectangle((3.6, -1.4), 0.4, 5.0, fc="#F3E5B8", ec=INK, lw=1.0))
    # capillary network around tubule
    ax.plot(*smooth([(1.1, 4.6), (2.0, 4.2), (2.4, 3.0), (2.1, 1.8), (2.2, 0.4), (2.0, -0.9), (0.9, -0.9), (0.9, 0.5), (0.7, 2.0), (0.4, 2.9)], closed=False).T,
            color="#9B3B6E", lw=1.0, ls="--")
    labels = [((-0.6, 4.4), "Bowman's capsule", (-3.0, 4.9)), ((0.0, 4.0), "glomerulus\n(cluster of capillaries)", (-3.0, 3.7)),
              ((-0.8, 4.43), "branch of renal artery", (-3.0, 5.6)), ((1.4, 2.4), "tubule (glucose, amino\nacids, salts, water\nreabsorbed here)", (-3.0, 2.0)),
              ((1.5, -0.55), "loop of the tubule", (-3.0, -0.6)), ((2.4, 3.0), "capillary network", (4.4, 4.6)),
              ((3.8, 1.0), "collecting duct\n(urine to ureter)", (4.4, 1.0))]
    for xy, t, xt in labels:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "right", size=9)
    finish(ax, (-6.0, 7.2), (-1.6, 6.0))
    save(fig, "sci_ch05_fig13_nephron.png")


if __name__ == "__main__":
    fig_leaf_section()
    fig_stomata()
    fig_variegated()
    fig_koh()
    fig_amoeba()
    fig_alimentary()
    fig_glucose_pathways()
    fig_respiratory()
    fig_heart()
    fig_double_circulation()
    fig_transpiration()
    fig_excretory()
    fig_nephron()
