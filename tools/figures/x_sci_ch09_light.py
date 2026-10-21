"""Figures for Class X Science, Chapter 9: Light - Reflection and Refraction.
Run: python x_sci_ch09_light.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
Ray diagrams are computed from the mirror and lens formulas, so every image is where the formula puts it.
The optics helpers (mirror_case, lens_case, ...) are reused by the Chapter 10 figures.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_sci_ch05_life_processes import ACC, GREY, HI, INK, SOFT, finish, save
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle

R1C = "#C0392B"   # first ray
R2C = "#2E6DB4"   # second ray
OBJ = "#1F7A3A"   # object arrow
IMG = "#8E44AD"   # image arrow
GLASS = "#D6EAF5"
plt.rcParams.update({"font.size": 8.5})


# ---------- drawing primitives ----------
def seg(ax, p0, p1, color, dashed=False, arrow=True, lw=1.15):
    ls = (0, (4, 3)) if dashed else "-"
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=color, lw=lw, ls=ls, zorder=4)
    if arrow and not dashed:
        m = (0.55 * p0[0] + 0.45 * p1[0], 0.55 * p0[1] + 0.45 * p1[1])
        d = (p1[0] - p0[0], p1[1] - p0[1])
        n = math.hypot(*d) or 1
        ax.annotate("", xy=(m[0] + 0.01 * d[0] / n, m[1] + 0.01 * d[1] / n), xytext=m,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=9), zorder=5)


def extend(p0, p1, x_to):
    """Point on the line p0-p1 at x = x_to."""
    if abs(p1[0] - p0[0]) < 1e-9:
        return p1
    t = (x_to - p0[0]) / (p1[0] - p0[0])
    return (x_to, p0[1] + t * (p1[1] - p0[1]))


def axis_line(ax, x0, x1):
    ax.plot([x0, x1], [0, 0], color=GREY, lw=0.8, zorder=1)


def tick(ax, x, text, below=True):
    ax.plot([x, x], [-0.06, 0.06], color=INK, lw=0.8, zorder=2)
    ax.text(x + 0.1, -0.1 if below else 0.1, text, ha="left", va="top" if below else "bottom", fontsize=8, color=INK, zorder=7)


def obj_arrow(ax, x, h, color=OBJ, dashed=False, name=None):
    ls = (0, (3, 2)) if dashed else "-"
    ax.annotate("", xy=(x, h), xytext=(x, 0), arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6, ls=ls, mutation_scale=10), zorder=6)
    if name:
        left = color == OBJ
        ax.text(x - 0.12 if left else x + 0.12, h, name, fontsize=8, color=color, ha="right" if left else "left",
                va="center", zorder=7)


# ---------- spherical mirrors ----------
def sag(kind, R, y):
    """x-position of the mirror surface at height y (pole at the origin, light from the left)."""
    s = R - math.sqrt(R * R - y * y)
    return -s if kind == "concave" else s


def draw_mirror(ax, kind, R, ap):
    ys = np.linspace(-ap, ap, 80)
    xs = np.array([sag(kind, R, y) for y in ys])
    ax.plot(xs, ys, color=INK, lw=1.8, zorder=3)
    for y in np.linspace(-ap + 0.1, ap - 0.1, 12):
        x = sag(kind, R, y)
        ax.plot([x + 0.02, x + 0.22], [y, y + 0.14], color=GREY, lw=0.7, zorder=2)


def mirror_case(ax, kind, u, h, f=2.0, ap=1.8, xlim=(-8.2, 4.4), names=("A", "B", "A'", "B'")):
    """u: object distance (negative) or None for an object at infinity. f: magnitude of focal length."""
    fs = -f if kind == "concave" else f       # signed focal length
    R = 2 * f
    axis_line(ax, xlim[0], xlim[1])
    draw_mirror(ax, kind, R, ap)
    tick(ax, 0, "P")
    tick(ax, fs, "F")
    tick(ax, 2 * fs, "C")
    if u is None:
        for y in (0.45, 0.95, -0.7):
            hit = (sag(kind, R, y), y)
            seg(ax, (xlim[0] + 0.3, y), hit, R1C)
            if kind == "concave":
                seg(ax, hit, extend(hit, (fs, 0), fs - 1.1), R1C)
            else:
                d = (hit[0] - fs, hit[1])
                seg(ax, hit, (hit[0] + 2.6 * d[0] / abs(d[0]), hit[1] + 2.6 * d[1] / abs(d[0])), R1C)
                seg(ax, hit, (fs, 0), R1C, dashed=True)
        return
    obj_arrow(ax, u, h, name=names[0])
    A = (u, h)
    left = xlim[0] + 0.2
    if abs(u - fs) < 1e-9:      # object at F: reflected rays parallel, image at infinity
        hit = (sag(kind, R, h), h)
        seg(ax, A, hit, R1C)
        seg(ax, hit, extend(hit, (fs, 0), left), R1C)
        seg(ax, A, (0, 0), R2C)
        seg(ax, (0, 0), extend((0, 0), (u, -h), left), R2C)
        return
    v = 1 / (1 / fs - 1 / u)
    hi = -v * h / u
    I = (v, hi)
    hit = (sag(kind, R, h), h)
    seg(ax, A, hit, R1C)
    seg(ax, A, (0, 0), R2C)
    if v < 0:   # real image in front of the mirror
        far = min(v, u) - 0.8
        seg(ax, hit, extend(hit, I, max(far, left)), R1C)
        seg(ax, (0, 0), extend((0, 0), I, max(far, left)), R2C)
        obj_arrow(ax, v, hi, IMG, name=names[2])
    else:       # virtual image behind the mirror
        d1 = (hit[0] - v, hit[1] - hi)
        k1 = (left + 2.5 - hit[0]) / d1[0]
        seg(ax, hit, (hit[0] + k1 * d1[0], hit[1] + k1 * d1[1]), R1C)
        seg(ax, hit, I, R1C, dashed=True)
        p2 = extend((0, 0), (u, -h), left + 2.5)
        seg(ax, (0, 0), p2, R2C)
        seg(ax, (0, 0), I, R2C, dashed=True)
        obj_arrow(ax, v, hi, IMG, dashed=True, name=names[2])


# ---------- thin lenses ----------
def draw_lens(ax, kind, ap):
    t = np.linspace(-ap, ap, 60)
    if kind == "convex":
        w = 0.28
        xr = w * np.sqrt(1 - (t / ap) ** 2)
        poly = np.r_[np.c_[xr, t], np.c_[-xr[::-1], t[::-1]]]
    else:
        w0, w1 = 0.07, 0.3
        xr = w0 + (w1 - w0) * (t / ap) ** 2
        poly = np.r_[np.c_[xr, t], np.c_[-xr[::-1], t[::-1]]]
    ax.add_patch(Polygon(poly, closed=True, fc=GLASS, ec=INK, lw=1.1, zorder=3))


def lens_case(ax, kind, u, h, f=2.0, ap=1.8, xlim=(-7.4, 7.4), names=("A", "B", "A'", "B'"), two_f=True):
    fs = f if kind == "convex" else -f
    axis_line(ax, xlim[0], xlim[1])
    draw_lens(ax, kind, ap)
    tick(ax, 0, "O")
    tick(ax, -f, "F₁")
    tick(ax, f, "F₂")
    if two_f:
        tick(ax, -2 * f, "2F₁")
        tick(ax, 2 * f, "2F₂")
    left, right = xlim[0] + 0.2, xlim[1] - 0.2
    if u is None:
        for y in (0.5, 1.0, -0.75):
            seg(ax, (left, y), (0, y), R1C)
            if kind == "convex":
                seg(ax, (0, y), extend((0, y), (f, 0), f + 1.6), R1C)
            else:
                seg(ax, (0, y), extend((-f, 0), (0, y), right - 2.5), R1C)
                seg(ax, (-f, 0), (0, y), R1C, dashed=True)
        return
    obj_arrow(ax, u, h, name=names[0])
    A = (u, h)
    if kind == "convex" and abs(u + f) < 1e-9:   # object at F1
        seg(ax, A, (0, h), R1C)
        seg(ax, (0, h), extend((0, h), (f, 0), right), R1C)
        seg(ax, A, (0, 0), R2C)
        seg(ax, (0, 0), extend(A, (0, 0), right), R2C)
        return
    v = 1 / (1 / fs + 1 / u)
    hi = v * h / u
    I = (v, hi)
    seg(ax, A, (0, h), R1C)
    seg(ax, A, (0, 0), R2C)
    if kind == "convex":
        if v > 0:
            far = min(v + 1.0, right)
            seg(ax, (0, h), extend((0, h), (f, 0), far), R1C)
            seg(ax, (0, 0), extend(A, (0, 0), far), R2C)
            obj_arrow(ax, v, hi, IMG, name=names[2])
        else:
            seg(ax, (0, h), extend((0, h), (f, 0), right - 1.0), R1C)
            seg(ax, (0, 0), extend(A, (0, 0), right - 1.0), R2C)
            seg(ax, (0, h), I, R1C, dashed=True)
            seg(ax, A, I, R2C, dashed=True)
            obj_arrow(ax, v, hi, IMG, dashed=True, name=names[2])
    else:
        seg(ax, (0, h), extend((-f, 0), (0, h), right - 1.5), R1C)
        seg(ax, (-f, 0), (0, h), R1C, dashed=True)
        seg(ax, (0, 0), extend(A, (0, 0), right - 1.5), R2C)
        obj_arrow(ax, v, hi, IMG, dashed=True, name=names[2])


def panel_title(ax, text, xlim, y):
    ax.text(xlim[0], y, text, fontsize=8.5, color=INK, ha="left", va="center")


def grid_fig(cases, draw, xlim, ylim, ncols, w=3.9, hgt=2.3, name=None):
    nrows = math.ceil(len(cases) / ncols)
    hgt = w * (ylim[1] - ylim[0]) / (xlim[1] - xlim[0]) + 0.15
    fig, axs = plt.subplots(nrows, ncols, figsize=(w * ncols, hgt * nrows))
    axs = np.atleast_1d(axs).ravel()
    for ax, (title, args) in zip(axs, cases):
        draw(ax, *args)
        panel_title(ax, title, xlim, ylim[1] - 0.15)
        finish(ax, xlim, ylim)
    for ax in axs[len(cases):]:
        ax.axis("off")
    fig.subplots_adjust(wspace=0.08, hspace=0.12)
    save(fig, name)


# Fig 9.1: concave and convex mirrors - pole, centre of curvature, focus, aperture
def fig_mirrors():
    fig, axs = plt.subplots(1, 2, figsize=(8.2, 3.3))
    for ax, kind in zip(axs, ("concave", "convex")):
        xl = (-5.0, 3.4) if kind == "concave" else (-4.8, 4.8)
        mirror_case(ax, kind, None, 1.0, f=2.0, ap=1.9, xlim=xl)
        R = 4.0
        top, bot = (sag(kind, R, 1.9), 1.9), (sag(kind, R, -1.9), -1.9)
        ax.text(top[0] + 0.25, top[1] + 0.05, "M", fontsize=8.5)
        ax.text(bot[0] + 0.25, bot[1] - 0.05, "N", fontsize=8.5, va="top")
        ax.text(xl[0] + 0.2, 0.12, "principal axis", fontsize=7.5, color=GREY)
        ax.text(xl[0], 2.25, f"({'a' if kind == 'concave' else 'b'}) {kind.capitalize()} mirror", fontsize=9, fontweight="bold")
        finish(ax, xl, (-2.2, 2.45))
    save(fig, "sci_ch09_fig01_mirrors.png")


def rule_mirror(ax, kind, rule):
    f, R, ap = 2.0, 4.0, 1.7
    fs = -f if kind == "concave" else f
    xl = (-5.2, 3.0) if kind == "concave" else (-4.8, 4.8)
    axis_line(ax, *xl)
    draw_mirror(ax, kind, R, ap)
    tick(ax, 0, "P")
    tick(ax, fs, "F")
    tick(ax, 2 * fs, "C")
    if rule == 1:      # parallel to the axis -> through F (or appears to come from F)
        y = 1.1
        hit = (sag(kind, R, y), y)
        seg(ax, (xl[0] + 0.3, y), hit, R1C)
        if kind == "concave":
            seg(ax, hit, extend(hit, (fs, 0), fs - 1.4), R1C)
        else:
            seg(ax, hit, extend((fs, 0), hit, -2.6), R1C)
            seg(ax, hit, (fs, 0), R1C, dashed=True)
    elif rule == 2:    # through F (or towards F) -> parallel to the axis
        y = 1.0 if kind == "concave" else 0.55
        hit = (sag(kind, R, y), y)
        seg(ax, extend((fs, 0), hit, -4.4), hit, R1C)
        if kind == "convex":
            seg(ax, hit, (fs, 0), R1C, dashed=True)
        seg(ax, hit, (xl[0] + 0.3, y), R1C)
    elif rule == 3:    # through C (or towards C) -> back along the same path
        y = 1.1 if kind == "concave" else 0.8
        hit = (sag(kind, R, y), y)
        p0 = extend((2 * fs, 0), hit, -4.6)
        seg(ax, p0, hit, R1C)
        d = (hit[0] - p0[0], hit[1] - p0[1])
        n = math.hypot(*d)
        off = (-0.09 * d[1] / n, 0.09 * d[0] / n)
        back = (p0[0] + 0.35 * d[0], p0[1] + 0.35 * d[1])
        seg(ax, (hit[0] + off[0], hit[1] + off[1]), (back[0] + off[0], back[1] + off[1]), R2C)
        if kind == "convex":
            seg(ax, hit, (2 * fs, 0), R1C, dashed=True)
    else:              # to the pole -> reflected at an equal angle
        seg(ax, (-4.4, 1.3), (0, 0), R1C)
        seg(ax, (0, 0), (-4.4, -1.3), R1C)
        ax.text(-1.15, 0.12, "i", fontsize=8, color=INK)
        ax.text(-1.15, -0.12, "r", fontsize=8, color=INK, va="top")
    return xl


# Fig 9.2: the four rays used in ray diagrams for spherical mirrors
def fig_mirror_rules():
    fig, axs = plt.subplots(2, 4, figsize=(11.0, 4.6))
    titles = ["(i) parallel to the axis", "(ii) through / towards F", "(iii) through / towards C", "(iv) to the pole P"]
    for r, kind in enumerate(("concave", "convex")):
        for c in range(4):
            ax = axs[r, c]
            xl = rule_mirror(ax, kind, c + 1)
            if r == 0:
                ax.text(xl[0], 2.05, titles[c], fontsize=8.5, fontweight="bold")
            if c == 0:
                ax.text(xl[0] - 0.2, 0, kind, rotation=90, fontsize=9, ha="right", va="center", fontweight="bold")
            finish(ax, xl, (-1.9, 2.3))
    fig.subplots_adjust(wspace=0.05, hspace=0.1)
    save(fig, "sci_ch09_fig02_mirror_rays.png")


# Fig 9.3: image formation by a concave mirror
def fig_concave_images():
    xl, yl = (-8.4, 4.4), (-2.3, 2.6)
    cases = [("(a) object at infinity: image at F", ("concave", None, 1.0)),
             ("(b) object beyond C: image between F and C", ("concave", -6.0, 1.0)),
             ("(c) object at C: image at C", ("concave", -4.0, 1.0)),
             ("(d) object between C and F: image beyond C", ("concave", -3.0, 0.8)),
             ("(e) object at F: image at infinity", ("concave", -2.0, 0.9)),
             ("(f) object between P and F: image behind mirror", ("concave", -1.2, 0.6))]
    grid_fig(cases, lambda ax, k, u, h: mirror_case(ax, k, u, h, xlim=xl), xl, yl, 2, w=4.1, hgt=2.35,
             name="sci_ch09_fig03_concave_images.png")


# Fig 9.4: image formation by a convex mirror
def fig_convex_images():
    xl, yl = (-6.4, 4.4), (-2.1, 2.4)
    cases = [("(a) object at infinity", ("convex", None, 1.0)), ("(b) object at a finite distance", ("convex", -4.0, 1.2))]
    grid_fig(cases, lambda ax, k, u, h: mirror_case(ax, k, u, h, xlim=xl), xl, yl, 2, w=4.1, hgt=2.6,
             name="sci_ch09_fig04_convex_images.png")


# Fig 9.5: New Cartesian sign convention
def fig_sign_convention():
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    draw_mirror(ax, "concave", 6.0, 2.2)
    ax.annotate("", xy=(4.2, 0), xytext=(-5.6, 0), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0))
    ax.annotate("", xy=(0, 2.7), xytext=(0, -2.7), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0))
    ax.text(4.3, 0, "X", va="center", fontsize=9)
    ax.text(-5.9, 0, "X'", va="center", fontsize=9)
    ax.text(0.1, 2.75, "Y", fontsize=9)
    ax.text(0.1, -2.95, "Y'", fontsize=9)
    ax.text(0.12, -0.3, "P (origin)", fontsize=8)
    obj_arrow(ax, -3.6, 1.0)
    ax.text(-3.6, 1.25, "object", ha="center", fontsize=8, color=OBJ)
    ax.annotate("", xy=(-1.0, 1.8), xytext=(-3.4, 1.8), arrowprops=dict(arrowstyle="-|>", color=HI, lw=1.4))
    ax.text(-2.2, 2.0, "direction of incident light", ha="center", fontsize=8, color=HI)
    ax.annotate("", xy=(-4.5, -0.55), xytext=(-0.2, -0.55), arrowprops=dict(arrowstyle="-|>", color=R1C, lw=1.0))
    ax.text(-2.35, -0.85, "distance to the left: negative (−)", ha="center", fontsize=8, color=R1C)
    ax.annotate("", xy=(3.6, -0.55), xytext=(0.6, -0.55), arrowprops=dict(arrowstyle="-|>", color=R2C, lw=1.0))
    ax.text(2.1, -0.85, "to the right: positive (+)", ha="center", fontsize=8, color=R2C)
    ax.annotate("", xy=(1.0, 2.2), xytext=(1.0, 0.25), arrowprops=dict(arrowstyle="-|>", color=R2C, lw=1.0))
    ax.text(1.15, 1.25, "height upwards:\npositive (+)", fontsize=8, color=R2C, va="center")
    ax.annotate("", xy=(1.0, -2.2), xytext=(1.0, -1.15), arrowprops=dict(arrowstyle="-|>", color=R1C, lw=1.0))
    ax.text(1.15, -1.75, "height downwards:\nnegative (−)", fontsize=8, color=R1C, va="center")
    finish(ax, (-6.2, 4.8), (-3.2, 3.0))
    save(fig, "sci_ch09_fig05_sign_convention.png")


# Fig 9.6: refraction of light through a rectangular glass slab
def fig_glass_slab():
    fig, ax = plt.subplots(figsize=(6.2, 5.6))
    n = 1.5
    i = math.radians(45)
    r = math.asin(math.sin(i) / n)
    top, bot = 1.5, -1.5
    ax.add_patch(Rectangle((-3.0, bot), 6.0, top - bot, fc=GLASS, ec=INK, lw=1.2, zorder=1))
    for (x, y), t in (((-3.0, top), "A"), ((3.0, top), "B"), ((3.0, bot), "C"), ((-3.0, bot), "D")):
        ax.text(x + (-0.2 if x < 0 else 0.1), y + (0.12 if y > 0 else -0.12), t, fontsize=9, va="bottom" if y > 0 else "top")
    O = (-1.2, top)
    O2 = (O[0] + (top - bot) * math.tan(r), bot)
    L = 2.4
    E = (O[0] - L * math.sin(i), O[1] + L * math.cos(i))
    H = (O2[0] + L * math.sin(i), O2[1] - L * math.cos(i))
    seg(ax, E, O, R1C)
    seg(ax, O, O2, R1C)
    seg(ax, O2, H, R1C)
    P = (O[0] + 2.4 * math.sin(i) * 1.6, O[1] - 2.4 * math.cos(i) * 1.6)
    ax.plot([O[0], P[0]], [O[1], P[1]], color=GREY, lw=0.9, ls=(0, (2, 2)), zorder=2)
    for p, t in ((O, "N"), (O2, "M")):
        ax.plot([p[0], p[0]], [p[1] - 1.3, p[1] + 1.3], color=INK, lw=0.8, ls=(0, (4, 3)), zorder=2)
        ax.text(p[0] - 0.1, p[1] + 1.35, t, fontsize=8.5, ha="right")
        ax.text(p[0] - 0.1, p[1] - 1.35, t + "'", fontsize=8.5, ha="right", va="top")
    for p, t in ((E, "E"), ((0.55 * E[0] + 0.45 * O[0], 0.55 * E[1] + 0.45 * O[1]), "F"),
                 ((0.55 * O2[0] + 0.45 * H[0], 0.55 * O2[1] + 0.45 * H[1]), "G"), (H, "H")):
        ax.plot(*p, marker="o", ms=3.5, color=INK, zorder=6)
        ax.text(p[0] - 0.15, p[1], t, fontsize=8.5, ha="right", va="center")
    ax.text(O[0] + 0.05, O[1] + 0.05, "O", fontsize=8.5, ha="left", va="bottom")
    ax.text(O2[0] - 0.1, O2[1] - 0.05, "O'", fontsize=8.5, ha="right", va="top")
    def arc(c, a0, a1, rad, lab, off):
        t = np.radians(np.linspace(a0, a1, 20))
        ax.plot(c[0] + rad * np.cos(t), c[1] + rad * np.sin(t), color=INK, lw=0.8)
        am = math.radians((a0 + a1) / 2)
        ax.text(c[0] + (rad + off) * math.cos(am), c[1] + (rad + off) * math.sin(am), lab, fontsize=9, ha="center", va="center")
    arc(O, 90, 90 + 45, 0.55, "i", 0.18)
    arc(O, 270, 270 + math.degrees(r), 0.75, "r", 0.18)
    arc(O2, 270, 270 + 45, 0.55, "e", 0.18)
    # lateral displacement
    t = ((O2[0] - O[0]) * math.cos(i) + (O2[1] - O[1]) * math.sin(i))
    foot = (O[0] + 0, O[1])
    d = (math.sin(i), -math.cos(i))
    proj = ((O2[0] - O[0]) * d[0] + (O2[1] - O[1]) * d[1])
    Q = (O[0] + proj * d[0], O[1] + proj * d[1])
    ax.annotate("", xy=O2, xytext=Q, arrowprops=dict(arrowstyle="<->", color=HI, lw=1.0))
    ax.text((Q[0] + O2[0]) / 2 + 0.75, (Q[1] + O2[1]) / 2 - 0.15, "lateral\ndisplacement", fontsize=7.5, color=HI, ha="left")
    ax.text(-2.85, top - 0.25, "glass", fontsize=8.5, color=ACC, va="top")
    ax.text(2.0, top + 0.45, "air", fontsize=8.5, color=ACC)
    ax.text(2.0, bot - 0.6, "air", fontsize=8.5, color=ACC)
    ax.text(E[0] + 0.3, E[1] + 0.05, "incident ray", fontsize=8, color=R1C)
    ax.text(H[0] + 0.15, H[1], "emergent ray", fontsize=8, color=R1C, va="center")
    ax.text(-0.55, -0.35, "refracted\nray", fontsize=8, color=R1C, ha="right", va="center")
    finish(ax, (-4.2, 4.4), (-3.6, 3.6))
    save(fig, "sci_ch09_fig06_glass_slab.png")


# Fig 9.7: converging action of a convex lens and diverging action of a concave lens
def fig_lens_action():
    xl, yl = (-5.4, 5.4), (-2.0, 2.4)
    cases = [("(a) convex lens: converging", ("convex", None, 1.0)), ("(b) concave lens: diverging", ("concave", None, 1.0))]
    grid_fig(cases, lambda ax, k, u, h: lens_case(ax, k, u, h, xlim=xl), xl, yl, 2, w=4.0, hgt=2.4,
             name="sci_ch09_fig07_lens_action.png")


# Fig 9.8: image formation by a convex lens
def fig_convex_lens_images():
    xl, yl = (-7.6, 7.6), (-2.6, 2.7)
    cases = [("(a) object at infinity: image at F₂", ("convex", None, 1.0)),
             ("(b) beyond 2F₁: image between F₂ and 2F₂", ("convex", -6.0, 1.0)),
             ("(c) at 2F₁: image at 2F₂", ("convex", -4.0, 1.0)),
             ("(d) between F₁ and 2F₁: image beyond 2F₂", ("convex", -3.0, 0.8)),
             ("(e) at F₁: image at infinity", ("convex", -2.0, 0.9)),
             ("(f) between F₁ and O: virtual image", ("convex", -1.2, 0.6))]
    grid_fig(cases, lambda ax, k, u, h: lens_case(ax, k, u, h, xlim=xl), xl, yl, 2, w=4.1, hgt=2.15,
             name="sci_ch09_fig08_convex_lens_images.png")


# Fig 9.9: image formation by a concave lens
def fig_concave_lens_images():
    xl, yl = (-6.0, 5.0), (-2.0, 2.4)
    cases = [("(a) object at infinity", ("concave", None, 1.0)), ("(b) object at a finite distance", ("concave", -3.0, 1.5))]
    grid_fig(cases, lambda ax, k, u, h: lens_case(ax, k, u, h, f=3.0, xlim=xl, two_f=False), xl, yl, 2, w=4.0, hgt=2.5,
             name="sci_ch09_fig09_concave_lens_images.png")


if __name__ == "__main__":
    fig_mirrors()
    fig_mirror_rules()
    fig_concave_images()
    fig_convex_images()
    fig_sign_convention()
    fig_glass_slab()
    fig_lens_action()
    fig_convex_lens_images()
    fig_concave_lens_images()
