"""Figures for Class X Science, Chapter 10: The Human Eye and the Colourful World.
Run: python x_sci_ch10_eye.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
Prism, dispersion and raindrop paths are traced with Snell's law.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_sci_ch05_life_processes import ACC, GREY, HI, INK, SOFT, blob, finish, label, save, smooth, tube_path
from x_sci_ch09_light import GLASS, R1C, R2C, draw_lens, extend, seg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle, Wedge

SPECTRUM = [("red", "#D62728", 1.47), ("orange", "#FF7F0E", 1.49), ("yellow", "#E6C700", 1.51), ("green", "#2CA02C", 1.53),
            ("blue", "#1F77B4", 1.555), ("indigo", "#3F3FA0", 1.575), ("violet", "#8E44AD", 1.60)]


def unit(v):
    n = math.hypot(*v)
    return (v[0] / n, v[1] / n)


def refract(d, nrm, n1, n2):
    """d: unit direction; nrm: unit normal pointing against d (towards the incoming side)."""
    cosi = -(d[0] * nrm[0] + d[1] * nrm[1])
    eta = n1 / n2
    k = 1 - eta * eta * (1 - cosi * cosi)
    if k < 0:
        return None
    t = eta * cosi - math.sqrt(k)
    return unit((eta * d[0] + t * nrm[0], eta * d[1] + t * nrm[1]))


def hit_segment(p, d, a, b):
    """Intersection of the ray p + t d with segment ab; returns (point, t) or None."""
    ex, ey = b[0] - a[0], b[1] - a[1]
    den = d[0] * ey - d[1] * ex
    if abs(den) < 1e-12:
        return None
    t = ((a[0] - p[0]) * ey - (a[1] - p[1]) * ex) / den
    s = ((a[0] - p[0]) * d[1] - (a[1] - p[1]) * d[0]) / den
    if t > 1e-9 and -1e-9 <= s <= 1 + 1e-9:
        return (p[0] + t * d[0], p[1] + t * d[1]), t
    return None


def outward_normal(a, b, inside):
    nx, ny = unit((b[1] - a[1], -(b[0] - a[0])))
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    if (inside[0] - mx) * nx + (inside[1] - my) * ny > 0:
        nx, ny = -nx, -ny
    return (nx, ny)


def through_prism(p, d, tri, n):
    """Trace a ray through a triangular prism; returns [entry, exit] points and the exit direction."""
    cen = (sum(v[0] for v in tri) / 3, sum(v[1] for v in tri) / 3)
    faces = [(tri[i], tri[(i + 1) % 3]) for i in range(3)]
    best = min((h for h in (hit_segment(p, d, a, b) + (a, b) if hit_segment(p, d, a, b) else None for a, b in faces) if h),
               key=lambda h: h[1])
    e, _, a, b = best
    nrm = outward_normal(a, b, cen)
    d2 = refract(d, nrm, 1.0, n)
    hits = [hit_segment(e, d2, a2, b2) + (a2, b2) for a2, b2 in faces if (a2, b2) != (a, b) and hit_segment(e, d2, a2, b2)]
    f, _, a2, b2 = min(hits, key=lambda h: h[1])
    nrm2 = outward_normal(a2, b2, cen)
    d3 = refract(d2, (-nrm2[0], -nrm2[1]), n, 1.0)
    return e, f, d2, d3, nrm, nrm2


def angle_arc(ax, c, a0, a1, rad, text, off=0.16, size=9):
    while a1 - a0 > 180:
        a1 -= 360
    while a0 - a1 > 180:
        a1 += 360
    t = np.radians(np.linspace(a0, a1, 24))
    ax.plot(c[0] + rad * np.cos(t), c[1] + rad * np.sin(t), color=INK, lw=0.8, zorder=6)
    am = math.radians((a0 + a1) / 2)
    ax.text(c[0] + (rad + off) * math.cos(am), c[1] + (rad + off) * math.sin(am), text, fontsize=size, ha="center", va="center", zorder=7)


def deg(v):
    return math.degrees(math.atan2(v[1], v[0]))


# Fig 10.1: the human eye
def fig_eye():
    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    ax.add_patch(Circle((0, 0), 1.25, fc="#FBFBF7", ec=INK, lw=1.6, zorder=1))
    t = np.radians(np.linspace(-62, 62, 60))
    ax.plot(1.18 * np.cos(t), 1.18 * np.sin(t), color="#C0392B", lw=3.0, zorder=2)
    tc = np.radians(np.linspace(128, 232, 40))
    ax.add_patch(Polygon(np.c_[-0.62 + 0.78 * np.cos(tc), 0.78 * np.sin(tc)], closed=False, fc="#E3F0FA", ec=INK, lw=1.3, zorder=3))
    ax.add_patch(Ellipse((-0.72, 0), 0.32, 0.88, fc="#CFE6F5", ec=INK, lw=1.1, zorder=4))
    for s in (1, -1):
        ax.plot([-0.95, -0.95], [s * 0.3, s * 0.8], color="#6B4226", lw=4, zorder=5, solid_capstyle="butt")
        blob(ax, [(-0.78, s * 0.47), (-0.62, s * 0.52), (-0.55, s * 0.72), (-0.72, s * 0.95), (-0.85, s * 0.8)], "#E8A0A0", z=4)
        ax.plot([-0.72, -0.62], [s * 0.44, s * 0.55], color=GREY, lw=0.6, zorder=5)
    tube_path(ax, [(1.1, -0.38), (1.6, -0.45), (2.2, -0.5)], 0.32, "#F3D58A", z=0)
    ax.add_patch(Circle((1.16, -0.38), 0.07, fc=INK, ec=INK, zorder=6))
    labs = [((-1.38, 0.35), "cornea", (-2.3, 1.15)), ((-0.95, 0.6), "iris", (-2.3, 0.75)), ((-1.0, 0.0), "pupil", (-2.3, 0.0)),
            ((-1.2, -0.25), "aqueous humour", (-2.3, -0.6)), ((-0.72, -0.3), "eye lens", (-2.3, -1.15)),
            ((-0.62, 0.72), "ciliary muscles", (-0.2, 1.65)), ((0.3, 0.3), "vitreous humour", (1.6, 1.55)),
            ((1.0, 0.65), "retina", (1.7, 1.0)), ((1.85, -0.48), "optic nerve", (2.3, -0.95)), ((1.16, -0.38), "blind spot", (1.7, 0.3))]
    for xy, t_, xt in labs:
        label(ax, xy, t_, xt, ha="left" if xt[0] > 0 else "right", size=8.5)
    finish(ax, (-3.6, 3.4), (-1.6, 1.85))
    save(fig, "sci_ch10_fig01_eye.png")


def eye_outline(ax, cx=0.0):
    ax.add_patch(Circle((cx, 0), 1.0, fc="#FBFBF7", ec=INK, lw=1.3, zorder=1))
    t = np.radians(np.linspace(-55, 55, 40))
    ax.plot(cx + 0.96 * np.cos(t), 0.96 * np.sin(t), color="#C0392B", lw=2.4, zorder=2)
    ax.add_patch(Ellipse((cx - 0.62, 0), 0.24, 0.8, fc="#CFE6F5", ec=INK, lw=1.0, zorder=3))
    return (cx + 0.96, 0)


def converge(ax, src, lens_x, ys, target, color=R1C, past=None):
    for y in ys:
        p = (lens_x, y)
        seg(ax, src(y), p, color)
        end = target if past is None else extend(p, target, past)
        seg(ax, p, end, color, arrow=False)


def eye_panel_title(ax, x, y, text):
    ax.text(x, y, text, fontsize=8.5, ha="left", va="center", color=INK)


# Fig 10.2: myopia and its correction
def fig_myopia():
    fig, axs = plt.subplots(3, 1, figsize=(6.4, 6.2))
    ret = 0.96
    # (a) far point of a myopic eye: rays from the far point O focus on the retina
    ax = axs[0]
    eye_outline(ax)
    O = (-3.2, 0)
    for y in (0.3, -0.3):
        seg(ax, O, (-0.62, y), R1C)
        seg(ax, (-0.62, y), (ret, 0), R1C, arrow=False)
    ax.plot(*O, marker="o", ms=4, color=INK)
    ax.text(O[0], -0.2, "O (far point of\nthe myopic eye)", fontsize=8, ha="center", va="top")
    eye_panel_title(ax, -5.4, 1.15, "(a) far point of a myopic eye")
    finish(ax, (-5.5, 2.6), (-1.15, 1.3))
    # (b) parallel rays from a distant object focus in front of the retina
    ax = axs[1]
    eye_outline(ax)
    I = (0.45, 0)
    for y in (0.3, -0.3):
        seg(ax, (-5.2, y), (-0.62, y), R1C)
        seg(ax, (-0.62, y), I, R1C, arrow=False)
        seg(ax, I, extend((-0.62, y), I, ret), R1C, arrow=False)
    ax.plot(*I, marker="o", ms=3.5, color=INK, zorder=8)
    label(ax, I, "image forms in front of the retina", (1.4, -0.95))
    ax.text(-5.2, 0.45, "rays from a distant object", fontsize=8, color=R1C)
    eye_panel_title(ax, -5.4, 1.15, "(b) myopic eye")
    finish(ax, (-5.5, 2.6), (-1.15, 1.3))
    # (c) correction with a concave lens: parallel rays diverge as if from O
    ax = axs[2]
    eye_outline(ax)
    Lx = -2.0
    t = np.linspace(-0.6, 0.6, 40)
    xr = 0.05 + 0.16 * (t / 0.6) ** 2
    ax.add_patch(Polygon(np.r_[np.c_[Lx + xr, t], np.c_[Lx - xr[::-1], t[::-1]]], closed=True, fc=GLASS, ec=INK, lw=1.0, zorder=3))
    for y in (0.2, -0.2):
        seg(ax, (-5.2, y), (Lx, y), R1C)
        d = unit((Lx - O[0], y))
        yk = y + d[1] / d[0] * (-0.62 - Lx)
        seg(ax, (Lx, y), (-0.62, yk), R1C)
        seg(ax, (-0.62, yk), (ret, 0), R1C, arrow=False)
        seg(ax, O, (Lx, y), R1C, dashed=True)
    ax.plot(*O, marker="o", ms=4, color=INK)
    ax.text(O[0], -0.2, "O", fontsize=8, ha="center", va="top")
    label(ax, (Lx, -0.6), "concave lens", (-2.6, -1.0), ha="right")
    eye_panel_title(ax, -5.4, 1.15, "(c) correction with a concave lens")
    finish(ax, (-5.5, 2.6), (-1.15, 1.3))
    fig.subplots_adjust(hspace=0.05)
    save(fig, "sci_ch10_fig02_myopia.png")


# Fig 10.3: hypermetropia and its correction
def fig_hypermetropia():
    fig, axs = plt.subplots(3, 1, figsize=(6.4, 6.2))
    ret = 0.96
    N, N2 = (-5.0, 0), (-2.9, 0)
    ax = axs[0]
    eye_outline(ax)
    for y in (0.3, -0.3):
        seg(ax, N, (-0.62, y), R1C)
        seg(ax, (-0.62, y), (ret, 0), R1C, arrow=False)
    ax.plot(*N, marker="o", ms=4, color=INK)
    ax.text(N[0], -0.2, "N (near point of the\nhypermetropic eye)", fontsize=8, ha="center", va="top")
    eye_panel_title(ax, -5.4, 1.15, "(a) near point of a hypermetropic eye")
    finish(ax, (-5.6, 2.6), (-1.15, 1.3))
    ax = axs[1]
    eye_outline(ax)
    I = (1.55, 0)
    for y in (0.3, -0.3):
        seg(ax, N2, (-0.62, y), R1C)
        q = extend((-0.62, y), I, ret)
        seg(ax, (-0.62, y), q, R1C, arrow=False)
        seg(ax, q, I, R1C, dashed=True)
    ax.plot(*N2, marker="o", ms=4, color=INK)
    ax.text(N2[0], -0.2, "N' (normal\nnear point)", fontsize=8, ha="center", va="top")
    label(ax, I, "image would form\nbehind the retina", (1.9, 0.75))
    eye_panel_title(ax, -5.4, 1.15, "(b) hypermetropic eye")
    finish(ax, (-5.6, 2.6), (-1.15, 1.3))
    ax = axs[2]
    eye_outline(ax)
    Lx = -1.9
    t = np.linspace(-0.6, 0.6, 40)
    xr = 0.17 * np.sqrt(1 - (t / 0.6) ** 2)
    ax.add_patch(Polygon(np.r_[np.c_[Lx + xr, t], np.c_[Lx - xr[::-1], t[::-1]]], closed=True, fc=GLASS, ec=INK, lw=1.0, zorder=3))
    for y in (0.27, -0.27):
        seg(ax, N2, (Lx, y), R1C)
        d = unit((Lx - N[0], y))
        yk = y + d[1] / d[0] * (-0.62 - Lx)
        seg(ax, (Lx, y), (-0.62, yk), R1C)
        seg(ax, (-0.62, yk), (ret, 0), R1C, arrow=False)
        seg(ax, N, (Lx, y), R1C, dashed=True)
    for p, t_ in ((N, "N"), (N2, "N'")):
        ax.plot(*p, marker="o", ms=4, color=INK)
        ax.text(p[0], -0.2, t_, fontsize=8, ha="center", va="top")
    label(ax, (Lx, -0.6), "convex lens", (-2.6, -1.0), ha="right")
    eye_panel_title(ax, -5.4, 1.15, "(c) correction with a convex lens")
    finish(ax, (-5.6, 2.6), (-1.15, 1.3))
    fig.subplots_adjust(hspace=0.05)
    save(fig, "sci_ch10_fig03_hypermetropia.png")


TRI = [(0.0, 2.6), (-1.5, 0.0), (1.5, 0.0)]   # A (apex), B, C


def draw_prism(ax, tri=TRI, labels=True):
    ax.add_patch(Polygon(tri, closed=True, fc=GLASS, ec=INK, lw=1.3, zorder=1))
    if labels:
        for (x, y), t in zip(tri, "ABC"):
            ax.text(x + (0 if t == "A" else (-0.12 if x < 0 else 0.12)), y + (0.12 if t == "A" else -0.08), t, fontsize=9,
                    ha="center" if t == "A" else ("right" if x < 0 else "left"), va="bottom" if t == "A" else "top")


# Fig 10.4: refraction of light through a triangular glass prism
def fig_prism():
    fig, ax = plt.subplots(figsize=(6.6, 4.6))
    draw_prism(ax)
    E0 = (-0.75, 1.3)
    d = unit((math.cos(math.radians(15)), math.sin(math.radians(15))))
    P = (E0[0] - 2.6 * d[0], E0[1] - 2.6 * d[1])
    e, f, d2, d3, n1, n2 = through_prism(P, d, TRI, 1.5)
    S = (f[0] + 2.4 * d3[0], f[1] + 2.4 * d3[1])
    seg(ax, P, e, R1C)
    seg(ax, e, f, R1C)
    seg(ax, f, S, R1C)
    for p, t in ((P, "P"), ((P[0] + 0.45 * (e[0] - P[0]), P[1] + 0.45 * (e[1] - P[1])), "Q"),
                 ((f[0] + 0.55 * (S[0] - f[0]), f[1] + 0.55 * (S[1] - f[1])), "R"), (S, "S")):
        ax.plot(*p, marker="o", ms=3.5, color=INK, zorder=6)
        ax.text(p[0], p[1] - 0.14, t, fontsize=8.5, ha="center", va="top")
    for c, nv, name in ((e, n1, "N"), (f, n2, "M")):
        a, b = (c[0] + 0.9 * nv[0], c[1] + 0.9 * nv[1]), (c[0] - 0.7 * nv[0], c[1] - 0.7 * nv[1])
        ax.plot([a[0], b[0]], [a[1], b[1]], color=INK, lw=0.8, ls=(0, (4, 3)), zorder=2)
    ax.text(e[0] - 0.06, e[1] + 0.06, "E", fontsize=8.5, ha="right", va="bottom")
    ax.text(f[0] + 0.06, f[1] + 0.06, "F", fontsize=8.5, ha="left", va="bottom")
    angle_arc(ax, e, deg((-d[0], -d[1])), deg(n1), 0.42, "i")
    angle_arc(ax, e, deg(d2), deg((-n1[0], -n1[1])), 0.5, "r")
    angle_arc(ax, f, deg(d3), deg(n2), 0.42, "e")
    # deviation: extend the incident ray forward and the emergent ray backward
    G = (e[0] + 2.6 * d[0], e[1] + 2.6 * d[1])
    ax.plot([e[0], G[0]], [e[1], G[1]], color=GREY, lw=0.9, ls=(0, (2, 2)))
    # intersection of incident line and emergent line
    den = d[0] * d3[1] - d[1] * d3[0]
    tt = ((f[0] - e[0]) * d3[1] - (f[1] - e[1]) * d3[0]) / den
    X = (e[0] + tt * d[0], e[1] + tt * d[1])
    ax.plot([X[0], f[0]], [X[1], f[1]], color=GREY, lw=0.9, ls=(0, (2, 2)))
    angle_arc(ax, X, deg(d3), deg(d), 0.85, "D", off=0.2)
    ax.text(3.2, 2.2, "PE: incident ray\nEF: refracted ray\nFS: emergent ray\ni: angle of incidence\nr: angle of refraction\n"
            "e: angle of emergence\nA: angle of the prism\nD: angle of deviation", fontsize=7.8, va="top", color=INK)
    finish(ax, (-3.6, 5.6), (-1.4, 3.0))
    save(fig, "sci_ch10_fig04_prism.png")


def spectrum_rays(ax, tri, P, d, screen_x=None, length=3.2, draw_inside=True):
    outs = []
    for name, col, n in SPECTRUM:
        e, f, d2, d3, _, _ = through_prism(P, d, tri, n)
        if draw_inside:
            ax.plot([e[0], f[0]], [e[1], f[1]], color=col, lw=1.0, zorder=3)
        if screen_x is not None:
            t = (screen_x - f[0]) / d3[0]
            end = (screen_x, f[1] + t * d3[1])
        else:
            end = (f[0] + length * d3[0], f[1] + length * d3[1])
        ax.plot([f[0], end[0]], [f[1], end[1]], color=col, lw=1.4, zorder=3)
        outs.append((name, col, n, f, d3, end))
    return outs


# Fig 10.5: dispersion of white light by a glass prism
def fig_dispersion():
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    draw_prism(ax, labels=False)
    d = unit((math.cos(math.radians(15)), math.sin(math.radians(15))))
    P = (-0.75 - 3.0 * d[0], 1.3 - 3.0 * d[1])
    e, *_ = through_prism(P, d, TRI, 1.5)
    ax.plot([P[0], e[0]], [P[1], e[1]], color=INK, lw=2.2, zorder=3)
    ax.text(P[0], P[1] + 0.15, "white light", fontsize=8.5, rotation=15, va="bottom")
    ax.add_patch(Rectangle((P[0] - 0.25, P[1] - 0.55), 0.12, 1.1, fc=GREY, ec=INK, lw=0.6))
    ax.text(P[0] - 0.19, P[1] - 0.68, "slit", fontsize=7.5, ha="center", va="top")
    sx = 4.2
    outs = spectrum_rays(ax, TRI, P, d, screen_x=sx)
    ylo, yhi = outs[-1][5][1], outs[0][5][1]
    ax.plot([sx, sx], [ylo - 0.4, yhi + 0.4], color=INK, lw=3)
    ax.text(sx, yhi + 0.5, "screen", fontsize=8, ha="center")
    for name, col, n, f, d3, end in outs:
        ax.text(sx + 0.15, end[1], name, fontsize=8, color=col, va="center")
    ax.text(0, -0.3, "glass prism", fontsize=8.5, ha="center", va="top")
    finish(ax, (-4.4, 5.6), (min(-0.8, ylo - 0.6), 3.0))
    save(fig, "sci_ch10_fig05_dispersion.png")


# Fig 10.6: recombination of the spectrum by an inverted prism
def fig_recombination():
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    draw_prism(ax, labels=False)
    d = unit((math.cos(math.radians(15)), math.sin(math.radians(15))))
    P = (-0.75 - 2.6 * d[0], 1.3 - 2.6 * d[1])
    e, *_ = through_prism(P, d, TRI, 1.5)
    ax.plot([P[0], e[0]], [P[1], e[1]], color=INK, lw=2.2, zorder=3)
    ax.text(P[0], P[1] + 0.15, "white light", fontsize=8.5, rotation=15, va="bottom")
    # second, inverted prism placed where the spectrum is spread
    mid = through_prism(P, d, TRI, 1.53)
    f, d3 = mid[1], mid[3]
    cx, cy = f[0] + 1.9 * d3[0] + 1.1, f[1] + 1.9 * d3[1] - 0.2
    TRI2 = [(cx + 0.0, cy - 1.3), (cx - 1.5, cy + 1.3), (cx + 1.5, cy + 1.3)]
    ax.add_patch(Polygon(TRI2, closed=True, fc=GLASS, ec=INK, lw=1.3, zorder=1))
    exits = []
    for name, col, n in SPECTRUM:
        e1, f1, d2, d3, _, _ = through_prism(P, d, TRI, n)
        ax.plot([e1[0], f1[0]], [e1[1], f1[1]], color=col, lw=1.0, zorder=3)
        e2, f2, dd2, dd3, _, _ = through_prism(f1, d3, TRI2, n)
        ax.plot([f1[0], e2[0]], [f1[1], e2[1]], color=col, lw=1.3, zorder=3)
        ax.plot([e2[0], f2[0]], [e2[1], f2[1]], color=col, lw=1.0, zorder=3)
        exits.append((f2, dd3))
    fx = sum(p[0] for p, _ in exits) / 7
    fy = sum(p[1] for p, _ in exits) / 7
    dx = sum(q[0] for _, q in exits) / 7
    dy = sum(q[1] for _, q in exits) / 7
    ax.plot([fx, fx + 2.2 * dx], [fy, fy + 2.2 * dy], color=INK, lw=2.2, zorder=3)
    ax.text(fx + 2.3 * dx, fy + 2.3 * dy, "white light", fontsize=8.5, va="center")
    ax.text(0, -0.3, "prism", fontsize=8.5, ha="center", va="top")
    ax.text(cx, cy - 1.45, "inverted prism", fontsize=8.5, ha="center", va="top")
    finish(ax, (-3.8, cx + 4.2), (-1.0, 3.0))
    save(fig, "sci_ch10_fig06_recombination.png")


def drop_trace(b, n):
    p = (-math.sqrt(1 - b * b), b)
    d = (1.0, 0.0)
    nrm = unit(p)
    d1 = refract(d, nrm, 1.0, n)
    t = -2 * (p[0] * d1[0] + p[1] * d1[1])
    q = (p[0] + t * d1[0], p[1] + t * d1[1])
    nq = unit(q)
    dot = d1[0] * nq[0] + d1[1] * nq[1]
    d2 = (d1[0] - 2 * dot * nq[0], d1[1] - 2 * dot * nq[1])
    t2 = -2 * (q[0] * d2[0] + q[1] * d2[1])
    r = (q[0] + t2 * d2[0], q[1] + t2 * d2[1])
    nr = unit(r)
    d3 = refract(d2, (-nr[0], -nr[1]), n, 1.0)
    return p, q, r, d3


# Fig 10.7: formation of a rainbow in a raindrop
def fig_rainbow():
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    ax.add_patch(Circle((0, 0), 1.0, fc="#E6F2FB", ec=INK, lw=1.3))
    b = 0.86
    p0, *_ = drop_trace(b, 1.33)
    ax.plot([-3.2, p0[0]], [b, b], color=INK, lw=2.0)
    ax.text(-3.2, b + 0.1, "sunlight (white)", fontsize=8.5, va="bottom")
    for name, col, n in (SPECTRUM[0], SPECTRUM[-1]):
        nn = 1.331 + (n - 1.47) * 0.35
        p, q, r, d3 = drop_trace(b, nn)
        ax.plot([p[0], q[0], r[0]], [p[1], q[1], r[1]], color=col, lw=1.3)
        ax.plot([r[0], r[0] + 2.4 * d3[0]], [r[1], r[1] + 2.4 * d3[1]], color=col, lw=1.6)
        ax.text(r[0] + 2.5 * d3[0], r[1] + 2.5 * d3[1], name, color=col, fontsize=8.5, ha="right", va="center")
    p, q, r, _ = drop_trace(b, 1.335)
    label(ax, p, "refraction and\ndispersion", (-2.4, 1.6), ha="right")
    label(ax, q, "internal reflection", (1.4, 0.9))
    label(ax, r, "refraction", (0.9, -1.4))
    ax.text(0.1, 0.0, "raindrop", fontsize=8.5, ha="center", color=ACC)
    finish(ax, (-3.8, 2.6), (-2.2, 1.9))
    save(fig, "sci_ch10_fig07_rainbow.png")


# Fig 10.8: apparent position of a star due to atmospheric refraction
def fig_star():
    fig, ax = plt.subplots(figsize=(5.8, 4.6))
    for i, y in enumerate(np.linspace(0.0, 3.0, 7)):
        ax.add_patch(Rectangle((-3.0, y), 6.0, 0.5, fc=(0.86 - 0.05 * (6 - i), 0.92 - 0.03 * (6 - i), 0.99), ec="none", zorder=0))
    ax.add_patch(Rectangle((-3.0, -0.4), 6.0, 0.4, fc="#9CC48A", ec="none"))
    ax.text(-2.9, 3.2, "rarer air (higher up)", fontsize=8, color=ACC)
    ax.text(-2.9, 0.15, "denser air (near the ground)", fontsize=8, color=ACC)
    obs = (1.8, 0.0)
    pts = [obs]
    ang = math.radians(25)   # angle of the ray with the vertical near the ground
    y = 0.0
    x = obs[0]
    for k in range(7):
        a = ang + math.radians(3 * k)
        x -= 0.5 * math.tan(a)
        y += 0.5
        pts.append((x, y))
    star_actual = (pts[-1][0] - 0.9 * math.tan(ang + math.radians(23)), 4.4)
    pts.append(star_actual)
    pts = pts[::-1]
    for a, b in zip(pts[:-1], pts[1:]):
        seg(ax, a, b, R1C, arrow=a == pts[2])
    dist = math.hypot(star_actual[0] - obs[0], star_actual[1] - obs[1])
    dv = unit((pts[-2][0] - obs[0], pts[-2][1] - obs[1]))
    app = (obs[0] + dist * dv[0], obs[1] + dist * dv[1])
    ax.plot([obs[0], app[0]], [obs[1], app[1]], color=GREY, lw=1.0, ls=(0, (4, 3)))
    ax.plot(*star_actual, marker="*", ms=14, color="#E6C700", mec=INK, mew=0.6)
    ax.plot(*app, marker="*", ms=14, color="#FFF3B0", mec=GREY, mew=0.6)
    ax.text(star_actual[0] - 0.25, star_actual[1], "actual position\nof the star", fontsize=8, va="center", ha="right")
    ax.text(app[0] + 0.25, app[1], "apparent position\n(appears higher)", fontsize=8, va="center")
    ax.plot(*obs, marker="o", ms=6, color=INK)
    ax.text(obs[0] + 0.1, obs[1] - 0.1, "observer", fontsize=8, va="top")
    finish(ax, (-3.6, 3.2), (-0.5, 5.3))
    save(fig, "sci_ch10_fig08_star.png")


# Fig 10.9: advance sunrise and delayed sunset
def fig_sunrise():
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.add_patch(Circle((0, -3.0), 3.0, fc="#9CC48A", ec=INK, lw=1.0, zorder=2))
    ax.add_patch(Circle((0, -3.0), 3.7, fc="#DCEBF8", ec="none", zorder=1))
    obs = (0.0, 0.0)
    ax.plot([-5.5, 3.0], [0, 0], color=GREY, lw=0.9, ls=(0, (5, 3)))
    ax.text(2.9, 0.08, "horizon", fontsize=8, ha="right", va="bottom", color=GREY)
    sun_actual = (-4.6, -0.6)
    entry = (-2.25, -0.03)
    ax.plot([sun_actual[0], entry[0]], [sun_actual[1], entry[1]], color=R1C, lw=1.3, zorder=3)
    path = smooth([entry, (-1.3, 0.13), (-0.6, 0.08), obs], closed=False)
    ax.plot(path[:, 0], path[:, 1], color=R1C, lw=1.3, zorder=3)
    ax.annotate("", xy=obs, xytext=tuple(path[-4]), arrowprops=dict(arrowstyle="-|>", color=R1C, lw=1.2))
    d = unit((obs[0] - path[-3][0], obs[1] - path[-3][1]))
    app = (obs[0] - 4.8 * d[0], obs[1] - 4.8 * d[1])
    ax.plot([obs[0], app[0]], [obs[1], app[1]], color=GREY, lw=1.0, ls=(0, (4, 3)))
    ax.add_patch(Circle(sun_actual, 0.35, fc="#F5B041", ec=INK, lw=0.8, zorder=4))
    ax.add_patch(Circle(app, 0.35, fc="#FDEBD0", ec=GREY, lw=0.8, ls="--", zorder=4))
    ax.text(sun_actual[0], sun_actual[1] - 0.45, "actual Sun\n(below the horizon)", fontsize=8, ha="center", va="top")
    ax.text(app[0], app[1] + 0.45, "apparent Sun", fontsize=8, ha="center", va="bottom")
    ax.plot(*obs, marker="o", ms=5, color=INK, zorder=5)
    ax.text(0.1, -0.1, "observer", fontsize=8, va="top")
    ax.text(1.6, -1.6, "Earth", fontsize=9, ha="center")
    ax.text(2.6, 0.55, "atmosphere", fontsize=8, color=ACC)
    finish(ax, (-6.0, 3.6), (-2.2, 1.6))
    save(fig, "sci_ch10_fig09_sunrise.png")


if __name__ == "__main__":
    fig_eye()
    fig_myopia()
    fig_hypermetropia()
    fig_prism()
    fig_dispersion()
    fig_recombination()
    fig_rainbow()
    fig_star()
    fig_sunrise()
