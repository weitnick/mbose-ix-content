"""Figures for Class XII Physics Chapter 9, Ray Optics and Optical Instruments.
Run: python xii_phy_ch09_rayoptics.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, FancyArrowPatch, Polygon, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Physics", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, POS, NEG, ACC, GREY, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#E9F0F7"
GREEN = "#2E7D32"
GLASS = "#DCEAF5"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def arrow(ax, p0, p1, color=INK, lw=1.6, ms=12, style="-|>"):
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle=style, mutation_scale=ms, color=color, lw=lw, shrinkA=0, shrinkB=0))


def blank(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")


def line(ax, pts, color=INK, lw=1.3, ls="-", z=2):
    xs, ys = zip(*[tuple(p) for p in pts])
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_capstyle="round", zorder=z)


def ray(ax, pts, color=POS, lw=1.5, ls="-", marks=True):
    """A polyline ray with a small arrowhead in the middle of each segment."""
    line(ax, pts, color, lw, ls, z=3)
    if not marks:
        return
    for p, q in zip(pts[:-1], pts[1:]):
        p, q = np.array(p, float), np.array(q, float)
        m = (p + q) / 2
        d = (q - p) / (np.hypot(*(q - p)) + 1e-9)
        arrow(ax, m - 0.08 * d, m + 0.08 * d, color, lw=0.01, ms=11)


def obj(ax, x, h, color=INK, label=None, dy=0.12, ls="-"):
    arrow(ax, (x, 0), (x, h), color, lw=2.0, ms=11)
    if ls != "-":
        line(ax, [(x, 0), (x, h)], "white", lw=2.6, z=4)
        line(ax, [(x, 0), (x, h)], color, lw=1.6, ls=ls, z=5)
    if label:
        ax.text(x, h + (dy if h > 0 else -dy), label, ha="center", va="bottom" if h > 0 else "top", fontsize=9.5, color=color)


def axis_line(ax, x0, x1):
    line(ax, [(x0, 0), (x1, 0)], GREY, lw=0.9)


def dot(ax, x, y, label, dx=0, dy=-0.18, color=INK, va="top"):
    ax.plot([x], [y], "o", color=color, ms=3.5, zorder=6)
    ax.text(x + dx, y + dy, label, ha="center", va=va, fontsize=9.5, color=color)


def convex_lens(ax, x, h, bulge=0.18, color=NEG):
    t = np.linspace(-h, h, 60)
    xr = x + bulge * (1 - (t / h) ** 2)
    xl = x - bulge * (1 - (t / h) ** 2)
    ax.fill_betweenx(t, xl, xr, color=GLASS, zorder=1)
    ax.plot(xr, t, color=color, lw=1.4, zorder=2)
    ax.plot(xl, t, color=color, lw=1.4, zorder=2)


def concave_lens(ax, x, h, w=0.16, dip=0.12, color=NEG):
    t = np.linspace(-h, h, 60)
    xr = x + w - dip * (1 - (t / h) ** 2)
    xl = x - w + dip * (1 - (t / h) ** 2)
    ax.fill_betweenx(t, xl, xr, color=GLASS, zorder=1)
    ax.plot(xr, t, color=color, lw=1.4, zorder=2)
    ax.plot(xl, t, color=color, lw=1.4, zorder=2)
    line(ax, [(xl[0], -h), (xr[0], -h)], color, lw=1.4)
    line(ax, [(xl[-1], h), (xr[-1], h)], color, lw=1.4)


def thin_image(f, u):
    """Thin lens: 1/v - 1/u = 1/f (Cartesian)."""
    return 1.0 / (1.0 / f + 1.0 / u)


# ---- Fig 9.1: focal length of a concave mirror ---------------------------------------------------
def fig_focus():
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    R = 6.0
    blank(ax, (-7.0, 1.0), (-2.2, 2.6))
    th = np.linspace(-0.42, 0.42, 80)
    ax.plot(-R + R * np.cos(th), R * np.sin(th), color=NEG, lw=2.2)
    for t in np.linspace(-0.4, 0.4, 14):
        x, y = -R + R * np.cos(t), R * np.sin(t)
        line(ax, [(x, y), (x + 0.18, y + 0.1)], NEG, lw=0.8)
    axis_line(ax, -6.9, 0.6)
    th0 = 0.33
    M = (-R + R * np.cos(th0), R * np.sin(th0))
    ray(ax, [(-6.6, M[1]), M], POS)
    F = (-R / 2 - 0.08, 0)
    ray(ax, [M, (-5.0, M[1] - (M[1] / (M[0] - F[0])) * (M[0] + 5.0))], POS)
    line(ax, [(-R, 0), M], GREY, lw=1, ls="--")
    line(ax, [M, (M[0], 0)], GREY, lw=1, ls=":")
    dot(ax, -R, 0, "C")
    dot(ax, F[0], 0, "F")
    dot(ax, 0, 0, "P", dx=0.2)
    dot(ax, M[0], 0, "D", dx=0.12)
    ax.text(M[0] + 0.12, M[1] + 0.12, "M", fontsize=10)
    ax.add_patch(Arc((-R, 0), 1.6, 1.6, theta1=0, theta2=np.degrees(th0), color=INK, lw=1))
    ax.text(-R + 0.9, 0.17, "θ", fontsize=10)
    ax.add_patch(Arc(F, 1.2, 1.2, theta1=0, theta2=np.degrees(np.arctan2(M[1], M[0] - F[0])), color=INK, lw=1))
    ax.text(F[0] + 0.66, 0.2, "2θ", fontsize=10)
    ax.text(-2.9, -1.6, "R = CP,  f = FP = R/2", fontsize=9.5, color=GREY)
    ax.text(-6.6, M[1] + 0.15, "ray parallel to the axis", fontsize=8.5, color=POS)
    fig.tight_layout()
    save(fig, "phy_ch09_fig01_focus.png")


# ---- Fig 9.2: image by a concave mirror ----------------------------------------------------------
def fig_mirror_image():
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    R, f = 6.0, -3.0
    blank(ax, (-9.6, 1.0), (-2.6, 2.4))
    th = np.linspace(-0.4, 0.4, 80)
    ax.plot(-R + R * np.cos(th) + 0.0, R * np.sin(th), color=NEG, lw=2.2)
    axis_line(ax, -9.5, 0.6)
    u, h = -8.4, 1.4
    v = 1.0 / (1.0 / f - 1.0 / u)  # mirror: 1/v + 1/u = 1/f
    hi = -v / u * h
    obj(ax, u, h, INK, "A")
    ax.text(u, -0.2, "B", ha="center", va="top", fontsize=9.5)
    obj(ax, v, hi, POS, None)
    ax.text(v, hi - 0.12, "A′", ha="center", va="top", fontsize=9.5, color=POS)
    ax.text(v + 0.2, 0.12, "B′", ha="center", va="bottom", fontsize=9.5, color=POS)
    ray(ax, [(u, h), (-0.17, h), (v, hi)], POS)  # parallel -> through F
    # ray through F: from A through F to the mirror, then back parallel to the axis
    yM = h * (0 - f) / (u - f)
    ray(ax, [(u, h), (-0.04, yM), (v - 0.1, yM)], NEG)
    line(ax, [(u, h), (v, hi)], GREY, lw=0.9, ls=":")
    dot(ax, -R, 0, "C")
    dot(ax, f, 0, "F")
    dot(ax, 0, 0, "P", dx=0.25)
    ax.text(0.05, h + 0.12, "M", fontsize=9.5)
    ax.text(-9.4, -2.3, "Real, inverted image A′B′ between C and F for an object beyond C", fontsize=9, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch09_fig02_mirror_image.png")


# ---- Fig 9.3: lateral shift and apparent depth ---------------------------------------------------
def fig_slab_depth():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6))
    ax = axes[0]
    blank(ax, (-2.4, 2.6), (-2.0, 2.0))
    ax.add_patch(Rectangle((-1.4, -0.8), 2.8, 1.6, color=GLASS, ec=NEG, lw=1.2))
    n = 1.5
    i = np.radians(50)
    r = np.arcsin(np.sin(i) / n)
    P1 = (-0.8, 0.8)
    P0 = (P1[0] - 1.1 * np.tan(i), P1[1] + 1.1)
    P2 = (P1[0] + 1.6 * np.tan(r), -0.8)
    P3 = (P2[0] + 1.1 * np.tan(i), -1.9)
    ray(ax, [P0, P1, P2, P3], POS)
    line(ax, [P1, (P1[0] + 2.7 * np.tan(i), P1[1] - 2.7)], GREY, lw=0.9, ls="--")
    for p in (P1, P2):
        line(ax, [(p[0], p[1] + 0.6), (p[0], p[1] - 0.6)], GREY, lw=0.8, ls=":")
    ax.text(P1[0] - 0.36, 1.15, "i", fontsize=10)
    ax.text(P1[0] + 0.08, 0.3, "r", fontsize=10)
    ax.text(P2[0] + 0.1, -1.3, "i", fontsize=10)
    ax.text(1.5, -1.7, "lateral\nshift", fontsize=8.5, color=GREY)
    ax.text(-1.3, -0.6, "glass slab", fontsize=8.5, color=NEG)
    ax.set_title("(a) Emergent ray parallel to the incident ray", fontsize=10)
    ax = axes[1]
    blank(ax, (-2.4, 2.4), (-2.3, 1.9))
    ax.add_patch(Rectangle((-2.2, -2.0), 4.4, 2.0, color=GLASS, lw=0))
    line(ax, [(-2.2, 0), (2.2, 0)], NEG, lw=1.4)
    O = (0, -1.8)
    I = (0, -1.8 / 1.33)
    for x in (0.35, -0.35):
        Pt = (x * 0.55, 0)
        # refracted ray leaves away from normal; its backward extension passes through I
        d = np.array(Pt) - np.array(I)
        ray(ax, [O, Pt, tuple(np.array(Pt) + 1.6 * d / np.hypot(*d))], POS)
        line(ax, [Pt, I], GREY, lw=0.9, ls="--")
    dot(ax, *O, "O (object)", dy=-0.08)
    dot(ax, *I, "I (image)", dx=0.62, dy=0.12, va="bottom", color=POS)
    ax.text(-2.1, -0.35, "water", fontsize=8.5, color=NEG)
    ax.text(-2.1, 0.2, "air", fontsize=8.5, color=GREY)
    ax.annotate("", (1.6, -1.8), (1.6, 0), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text(1.7, -0.95, "real\ndepth", fontsize=8.5, color=GREY)
    ax.annotate("", (-0.9, I[1]), (-0.9, 0), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text(-2.25, I[1] / 2, "apparent\ndepth", fontsize=8.5, color=GREY, va="center")
    ax.set_title("(b) Apparent depth = real depth / n", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch09_fig03_slab_depth.png")


# ---- Fig 9.4: total internal reflection -----------------------------------------------------------
def fig_tir():
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    blank(ax, (-3.6, 4.4), (-2.2, 1.9))
    ax.add_patch(Rectangle((-3.6, -2.2), 8.0, 2.2, color=GLASS, lw=0))
    line(ax, [(-3.6, 0), (4.4, 0)], NEG, lw=1.5)
    A = (-2.6, -1.9)
    n = 1.33
    ic = np.arcsin(1 / n)
    cols = [GREEN, ACC, POS, NEG]
    angles = [np.radians(20), np.radians(36), ic, np.radians(62)]
    names = ["O₁", "O₂", "O₃", "O₄"]
    for ang, col, nm in zip(angles, cols, names):
        x = A[0] + 1.9 * np.tan(ang)
        O = (x, 0)
        if ang < ic - 1e-6:
            r = np.arcsin(n * np.sin(ang))
            ray(ax, [A, O, (x + 1.5 * np.sin(r), 1.5 * np.cos(r))], col)
            ray(ax, [O, (x + 0.6 * np.tan(ang), -0.6)], col, lw=0.8, marks=False)
        elif abs(ang - ic) < 1e-6:
            ray(ax, [A, O, (x + 1.7, 0.02)], col)
        else:
            ray(ax, [A, O, (x + 1.9 * np.tan(ang), -1.9)], col)
        ax.text(x, 0.08 if ang <= ic else -0.12, nm, fontsize=9, ha="center", va="bottom" if ang <= ic else "top", color=col)
    xc = A[0] + 1.9 * np.tan(ic)
    line(ax, [(xc, 0.9), (xc, -1.2)], GREY, lw=0.8, ls=":")
    ax.text(xc - 0.55, -0.55, "$i_c$", fontsize=10, color=POS)
    dot(ax, *A, "A", dy=-0.05)
    ax.text(-3.5, 1.5, "air (rarer)", fontsize=9, color=GREY)
    ax.text(-3.5, -0.4, "water (denser)", fontsize=9, color=NEG)
    ax.text(1.4, 0.65, "refracted rays bend away from the normal", fontsize=8.5, color=INK)
    ax.text(2.0, -1.6, "i > $i_c$: totally reflected", fontsize=8.5, color=NEG)
    ax.text(1.9, 0.12, "grazing (r = 90°)", fontsize=8.5, color=POS)
    fig.tight_layout()
    save(fig, "phy_ch09_fig04_tir.png")


# ---- Fig 9.5: totally reflecting prisms and an optical fibre ---------------------------------------
def prism45(ax, pts):
    ax.add_patch(Polygon(pts, closed=True, fc=GLASS, ec=NEG, lw=1.4))


def fig_tir_prisms():
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.3), gridspec_kw={"width_ratios": [1, 1, 1.4]})
    ax = axes[0]
    blank(ax, (-1.6, 1.8), (-1.6, 1.7))
    prism45(ax, [(-1, -1), (1, -1), (-1, 1)])
    ray(ax, [(-1.5, 0.3), (-0.3, 0.3), (-0.3, -1.5)], POS)
    ax.text(-0.25, 0.42, "45°", fontsize=8.5)
    ax.set_title("(a) Turned through 90°", fontsize=10)
    ax = axes[1]
    blank(ax, (-1.7, 1.7), (-1.5, 1.8))
    prism45(ax, [(-1.2, 0), (1.2, 0), (0, 1.2)])
    ray(ax, [(-0.55, -1.2), (-0.55, 0.65), (0.55, 0.65), (0.55, -1.2)], POS)
    ax.text(0, 1.35, "90°", fontsize=8.5, ha="center")
    ax.set_title("(b) Turned through 180°", fontsize=10)
    ax = axes[2]
    blank(ax, (-2.9, 2.9), (-1.2, 1.7))
    prism45(ax, [(-2.0, 0.0), (2.0, 0.0), (0.9, 1.1), (-0.9, 1.1)])
    n = 1.5
    tilt = np.radians(-45) + np.arcsin(np.sin(np.radians(45)) / n)  # direction inside, below horizontal
    for y0, col, lab in ((0.32, POS, "2"), (0.72, NEG, "1")):
        xin = -2.0 + y0
        xb = xin + y0 / np.tan(-tilt)
        # up again at the same angle until the right face x + y = 2
        t = (2.0 - xb) / (np.cos(tilt) + np.sin(-tilt))
        xo, yo = xb + t * np.cos(tilt), t * np.sin(-tilt)
        ray(ax, [(-2.8, y0), (xin, y0), (xb, 0.0), (xo, yo), (2.8, yo)], col, lw=1.3, marks=False)
        ax.text(-2.85, y0 + 0.05, lab, color=col, fontsize=9, va="bottom")
        ax.text(2.75, yo + 0.05, lab, color=col, fontsize=9, va="bottom")
    ax.text(0.0, -0.25, "refracted at the sloping faces, totally reflected at the base:\nrays 1 and 2 change places, so the image is inverted",
            fontsize=8.5, ha="center", va="top")
    ax.set_title("(c) Inverting an image", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch09_fig05_tir_prisms.png")


# ---- Fig 9.6: an optical fibre --------------------------------------------------------------------
def fig_fibre():
    fig, ax = plt.subplots(figsize=(8.6, 2.6))
    blank(ax, (-0.6, 10.4), (-1.3, 1.4))
    ax.add_patch(Rectangle((0, -0.75), 10, 1.5, color="#F3E9D2", lw=0))
    ax.add_patch(Rectangle((0, -0.5), 10, 1.0, color=GLASS, lw=0))
    for y in (-0.75, -0.5, 0.5, 0.75):
        line(ax, [(0, y), (10, y)], NEG if abs(y) == 0.5 else ACC, lw=1.1)
    pts = [(-0.5, -0.3), (0.0, -0.1)]
    x, y, s = 0.0, -0.1, 1
    while x < 9.3:
        ny = 0.5 * s
        x = x + abs(ny - y) / 0.55
        if x > 10:
            break
        pts.append((x, ny))
        y, s = ny, -s
    pts.append((10.4, y + 0.3 * (1 if s > 0 else -1)))
    ray(ax, pts, POS, lw=1.3)
    ax.text(5, -1.05, "cladding (lower refractive index)", fontsize=8.5, ha="center", color=ACC)
    ax.text(5, 1.0, "core (higher refractive index)", fontsize=8.5, ha="center", color=NEG)
    ax.text(-0.5, 0.15, "light in", fontsize=8.5, color=POS)
    fig.tight_layout()
    save(fig, "phy_ch09_fig06_fibre.png")


# ---- Fig 9.7: refraction at a convex spherical surface -------------------------------------------
def fig_spherical():
    fig, ax = plt.subplots(figsize=(8.2, 3.4))
    blank(ax, (-5.2, 6.2), (-1.4, 2.2))
    R = 1.5
    t = np.linspace(-1.0, 1.0, 80)
    xs, ys = R - R * np.cos(t), R * np.sin(t)
    ax.fill_betweenx(ys, xs, 6.0, color=GLASS, zorder=0)
    ax.plot(xs, ys, color=NEG, lw=1.8)
    axis_line(ax, -5.1, 6.0)
    O, C = (-4.0, 0.0), (R, 0.0)
    th = 0.55
    N = (R - R * np.cos(th), R * np.sin(th))
    n1, n2 = 1.0, 2.0
    u = O[0]
    v = 1.0 / ((n2 - n1) / R + n1 / u) * n2
    I = (v, 0.0)
    ray(ax, [O, N, I], POS)
    ray(ax, [O, (0, 0), I], POS, lw=1.0, marks=False)
    d = np.array(N) - np.array(C)
    d = d / np.hypot(*d)
    line(ax, [tuple(np.array(N) + 1.0 * d), C], GREY, lw=0.9, ls="--")
    line(ax, [N, (N[0], 0)], GREY, lw=0.8, ls=":")
    dot(ax, *O, "O")
    dot(ax, *C, "C")
    dot(ax, *I, "I", color=POS)
    dot(ax, 0, 0, "M", dx=-0.2)
    ax.text(N[0] - 0.05, N[1] + 0.12, "N", fontsize=10)
    ax.text(N[0] - 0.55, N[1] + 0.25, "i", fontsize=10, color=INK)
    ax.text(N[0] + 0.35, N[1] - 0.05, "r", fontsize=10, color=INK)
    ax.text(-5.0, 1.8, "medium 1 (n₁, rarer)", fontsize=9, color=GREY)
    ax.text(2.6, 1.8, "medium 2 (n₂, denser)", fontsize=9, color=NEG)
    ax.text(-4.9, -1.05, "u = −OM,  v = +MI,  R = +MC", fontsize=9, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch09_fig07_spherical.png")


# ---- Fig 9.8: refraction by a lens (two surfaces) ------------------------------------------------
def fig_lensmaker():
    fig, ax = plt.subplots(figsize=(8.4, 3.2))
    blank(ax, (-5.6, 8.2), (-1.6, 2.0))
    convex_lens(ax, 0, 1.5, bulge=0.32)
    axis_line(ax, -5.5, 8.0)
    O, I1, I = (-4.5, 0), (7.6, 0), (3.2, 0)
    N1, N2 = (-0.2, 0.9), (0.2, 0.9)
    ray(ax, [O, N1], POS)
    line(ax, [N1, I1], GREY, lw=1, ls="--")
    ray(ax, [N1, N2, I], POS)
    dot(ax, *O, "O")
    dot(ax, *I, "I", color=POS)
    dot(ax, *I1, "I₁", color=GREY)
    ax.text(-0.75, -1.4, "surface 1\n(R₁)", fontsize=8.5, ha="center", color=NEG)
    ax.text(0.85, -1.4, "surface 2\n(R₂)", fontsize=8.5, ha="center", color=NEG)
    ax.text(3.8, 1.25, "surface 1 alone would form I₁;\nI₁ is the (virtual) object for surface 2", fontsize=8.5, color=GREY)
    ax.text(-5.4, 1.6, "n₁ outside", fontsize=8.5, color=GREY)
    ax.text(-0.35, 1.65, "n₂", fontsize=9, color=NEG)
    fig.tight_layout()
    save(fig, "phy_ch09_fig08_lensmaker.png")


# ---- Fig 9.9: ray tracing through lenses ---------------------------------------------------------
def fig_lens_rays():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.4))
    ax = axes[0]
    f = 2.0
    blank(ax, (-6.6, 6.8), (-2.2, 1.9))
    convex_lens(ax, 0, 1.7, bulge=0.2)
    axis_line(ax, -6.5, 6.7)
    u, h = -5.0, 1.1
    v = thin_image(f, u)
    hi = v / u * h
    obj(ax, u, h, INK, "object")
    obj(ax, v, hi, POS, "real image")
    ray(ax, [(u, h), (0, h), (v, hi)], POS)
    ray(ax, [(u, h), (v, hi)], NEG)
    yl = h * (0 + f) / (u + f)
    ray(ax, [(u, h), (0, yl), (v, yl)], GREEN)
    for x, lab in ((-f, "F"), (f, "F′"), (-2 * f, "2F"), (2 * f, "2F′")):
        dot(ax, x, 0, lab)
    ax.set_title("(a) Convex lens: object beyond 2F", fontsize=10)
    ax = axes[1]
    f = -2.5
    blank(ax, (-6.2, 3.8), (-1.8, 2.1))
    concave_lens(ax, 0, 1.7)
    axis_line(ax, -6.1, 3.7)
    u, h = -4.5, 1.2
    v = thin_image(f, u)
    hi = v / u * h
    obj(ax, u, h, INK, "object")
    obj(ax, v, hi, POS, None, ls="--")
    ax.text(v - 0.1, hi + 0.12, "virtual\nimage", fontsize=8.5, color=POS, ha="right")
    # parallel ray diverges as if from F (on the object side)
    slope = (h - 0) / (0 - f)
    ray(ax, [(u, h), (0, h), (3.2, h + slope * 3.2)], POS)
    line(ax, [(f, 0), (0, h)], GREY, lw=0.9, ls="--")
    ray(ax, [(u, h), (3.2, h * 3.2 / u)], NEG)
    dot(ax, f, 0, "F")
    dot(ax, -f, 0, "F′")
    ax.set_title("(b) Concave lens: virtual, erect, diminished image", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch09_fig09_lens_rays.png")


# ---- Fig 9.10: two thin lenses in contact --------------------------------------------------------
def fig_contact():
    fig, ax = plt.subplots(figsize=(7.6, 2.9))
    blank(ax, (-5.2, 7.2), (-1.4, 1.8))
    convex_lens(ax, -0.2, 1.4, bulge=0.16)
    convex_lens(ax, 0.2, 1.4, bulge=0.16)
    axis_line(ax, -5.1, 7.1)
    O, I, I1 = (-4.4, 0), (2.6, 0), (6.6, 0)
    ray(ax, [O, (-0.2, 0.75)], POS)
    line(ax, [(-0.2, 0.75), I1], GREY, lw=1, ls="--")
    ray(ax, [(-0.2, 0.75), (0.2, 0.73), I], POS)
    dot(ax, *O, "O")
    dot(ax, *I, "I", color=POS)
    dot(ax, *I1, "I₁", color=GREY)
    ax.text(-0.75, 1.5, "A", fontsize=10, color=NEG)
    ax.text(0.45, 1.5, "B", fontsize=10, color=NEG)
    ax.text(2.9, 0.95, "lens A alone would form I₁,\nwhich is the object for lens B", fontsize=8.5, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch09_fig10_contact.png")


# ---- Fig 9.11: refraction through a prism and the deviation curve --------------------------------
def fig_prism():
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 3.9), gridspec_kw={"width_ratios": [1.2, 1]})
    ax = axes[0]
    blank(ax, (-3.2, 3.4), (-1.6, 2.5))
    A = np.radians(60)
    apex = (0, 2.0)
    bl = (-3.3 * np.tan(A / 2), -1.3)
    br = (3.3 * np.tan(A / 2), -1.3)
    ax.add_patch(Polygon([apex, bl, br], closed=True, fc=GLASS, ec=NEG, lw=1.4))
    n = 1.5
    # point Q on the left face
    s = 0.45
    Q = (apex[0] + s * (bl[0] - apex[0]), apex[1] + s * (bl[1] - apex[1]))
    nl = np.array([-np.cos(A / 2), np.sin(A / 2)])  # outward normal, left face
    i = np.radians(48)
    # incident direction: rotate inward normal (-nl) by +i (coming from lower left)
    inward = -nl
    rot = lambda v, a: np.array([v[0] * np.cos(a) - v[1] * np.sin(a), v[0] * np.sin(a) + v[1] * np.cos(a)])
    din = rot(inward, i)
    P = np.array(Q) - 1.6 * din
    r1 = np.arcsin(np.sin(i) / n)
    dg = rot(inward, r1)
    # intersect with right face
    nr = np.array([np.cos(A / 2), np.sin(A / 2)])
    # right face: points X with (X - apex) . nr = 0
    tt = -np.dot(np.array(Q) - np.array(apex), nr) / np.dot(dg, nr)
    Rr = np.array(Q) + tt * dg
    r2 = np.radians(60) - r1
    e = np.arcsin(n * np.sin(r2))
    dout = rot(nr, -e)
    S = Rr + 1.7 * dout
    ray(ax, [tuple(P), Q, tuple(Rr), tuple(S)], POS)
    line(ax, [Q, tuple(np.array(Q) + 3.2 * din)], GREY, lw=0.9, ls="--")
    for X, nn in ((Q, nl), (tuple(Rr), nr)):
        line(ax, [tuple(np.array(X) + 0.8 * nn), tuple(np.array(X) - 1.0 * nn)], GREY, lw=0.8, ls=":")
    ax.text(Q[0] - 0.55, Q[1] - 0.45, "i", fontsize=10)
    ax.text(Q[0] + 0.32, Q[1] - 0.22, "r₁", fontsize=10)
    ax.text(Rr[0] - 0.55, Rr[1] - 0.22, "r₂", fontsize=10)
    ax.text(Rr[0] + 0.45, Rr[1] - 0.5, "e", fontsize=10)
    ax.text(2.35, -0.05, "δ", fontsize=12, color=ACC)
    ax.text(-0.12, 1.45, "A", fontsize=10)
    ax.text(Q[0] - 0.25, Q[1] + 0.05, "Q", fontsize=9)
    ax.text(Rr[0] + 0.08, Rr[1] + 0.08, "R", fontsize=9)
    ax.set_title("(a) A ray through a prism", fontsize=10)
    ax = axes[1]
    ii = np.radians(np.linspace(30, 88, 200))
    r1 = np.arcsin(np.sin(ii) / n)
    r2 = A - r1
    ok = n * np.sin(r2) <= 1
    ee = np.arcsin(np.clip(n * np.sin(r2), -1, 1))
    dd = np.degrees(ii + ee - A)
    ax.plot(np.degrees(ii[ok]), dd[ok], color=POS, lw=2)
    k = np.argmin(dd[ok])
    imin, dmin = np.degrees(ii[ok][k]), dd[ok][k]
    ax.axhline(dmin, color=GREY, lw=0.8, ls=":")
    ax.axvline(imin, color=GREY, lw=0.8, ls=":")
    ax.text(imin + 1, dmin - 2.2, "$D_m$ at i = e", fontsize=9, color=INK)
    ax.set_xlabel("angle of incidence i (degrees)", fontsize=9)
    ax.set_ylabel("angle of deviation δ (degrees)", fontsize=9)
    ax.set_ylim(dmin - 6, dmin + 22)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("(b) δ against i: one minimum, $D_m$", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch09_fig11_prism.png")


# ---- Fig 9.12: simple microscope ---------------------------------------------------------------
def fig_simple_microscope():
    fig, ax = plt.subplots(figsize=(7.8, 3.4))
    f = 2.0
    blank(ax, (-9.0, 2.6), (-1.4, 3.6))
    convex_lens(ax, 0, 1.6, bulge=0.16)
    axis_line(ax, -8.9, 1.9)
    D = 7.5
    v = -D
    u = 1.0 / (1.0 / v - 1.0 / f)
    h = 0.55
    hi = v / u * h
    obj(ax, u, h, INK, "object")
    obj(ax, v, hi, POS, None, ls="--")
    ax.text(v, hi + 0.1, "virtual, erect,\nmagnified image", fontsize=8.5, ha="center", va="bottom", color=POS)
    ray(ax, [(u, h), (0, h), (1.8, h - h / f * 1.8)], POS)
    line(ax, [(0, h), (v, hi)], GREY, lw=0.9, ls="--")
    ray(ax, [(u, h), (1.8, h * 1.8 / u)], NEG)
    line(ax, [(u, h), (v, hi)], GREY, lw=0.9, ls="--")
    dot(ax, -f, 0, "F")
    dot(ax, f, 0, "F′")
    ax.text(1.0, -0.6, "eye", fontsize=9)
    ax.annotate("", (v, -0.75), (0, -0.75), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text(v / 2, -1.0, "D ≈ 25 cm (near point)", fontsize=8.5, ha="center", va="top", color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch09_fig12_simple_microscope.png")


# ---- Fig 9.13: compound microscope ------------------------------------------------------------
def fig_compound():
    fig, ax = plt.subplots(figsize=(10.0, 5.4))
    fo, fe = 1.0, 2.5
    xo, xe = 0.0, 7.0
    blank(ax, (-7.4, 11.2), (-6.8, 2.6))
    convex_lens(ax, xo, 0.8, bulge=0.1)
    convex_lens(ax, xe, 1.8, bulge=0.2)
    axis_line(ax, -4.3, 11.0)
    u_o, h = -1.25, 0.3
    v_o = thin_image(fo, u_o)
    h1 = v_o / u_o * h
    x1 = xo + v_o
    obj(ax, xo + u_o, h, INK, None)
    ax.text(xo + u_o - 0.1, h + 0.05, "AB", fontsize=9, ha="right", va="bottom")
    obj(ax, x1, h1, ACC, None)
    ax.text(x1 - 0.12, h1 - 0.08, "A′B′", fontsize=9, ha="right", va="top", color=ACC)
    ray(ax, [(xo + u_o, h), (xo, h), (x1, h1)], POS)
    ray(ax, [(xo + u_o, h), (x1, h1)], NEG)
    u_e = x1 - xe
    v_e = thin_image(fe, u_e)
    x2 = xe + v_e
    h2 = v_e / u_e * h1
    obj(ax, x2, h2, POS, None, ls="--")
    ax.text(x2 - 0.25, h2 + 0.3, "A″B″: final image\n(virtual, inverted,\nat the near point)", fontsize=8.5, ha="right", va="bottom", color=POS)
    end = 10.6
    ray(ax, [(x1, h1), (xe, h1), (end, h1 + (0 - h1) / fe * (end - xe))], POS)
    line(ax, [(xe, h1), (x2, h2)], GREY, lw=0.9, ls="--")
    ray(ax, [(x1, h1), (end, h1 + (0 - h1) / (xe - x1) * (end - x1))], NEG)
    line(ax, [(x1, h1), (x2, h2)], GREY, lw=0.9, ls="--")
    dot(ax, xo + fo, 0, "$F_o$", dy=0.12, va="bottom")
    dot(ax, xe - fe, 0, "$F_e$", dy=0.12, va="bottom")
    ax.text(xo, 1.05, "objective", fontsize=9, ha="center", color=NEG)
    ax.text(xe, 2.05, "eyepiece", fontsize=9, ha="center", color=NEG)
    ax.annotate("", (xe - fe, 0.55), (xo + fo, 0.55), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text((xo + fo + xe - fe) / 2, 0.62, "tube length L", fontsize=8.5, ha="center", va="bottom", color=GREY)
    ax.text(10.2, -0.45, "eye", fontsize=9)
    ax.annotate("", (x2, -6.55), (xe, -6.55), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text((x2 + xe) / 2, -6.62, "D = 25 cm from the eyepiece", fontsize=8.5, ha="center", va="top", color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch09_fig13_compound.png")


# ---- Fig 9.14: astronomical telescope in normal adjustment --------------------------------------
def fig_telescope():
    fig, ax = plt.subplots(figsize=(10.0, 3.6))
    fo, fe = 7.0, 2.0
    blank(ax, (-2.6, 12.8), (-2.2, 2.4))
    convex_lens(ax, 0, 1.8, bulge=0.2)
    convex_lens(ax, fo + fe, 1.5, bulge=0.18)
    axis_line(ax, -2.5, 11.7)
    a = np.radians(6)
    hI = -fo * np.tan(a)
    for y0, col in ((0.9, POS), (0.0, NEG), (-0.9, GREEN)):
        start = (-2.4, y0 + 2.4 * np.tan(a))
        P = (0, y0)
        ray(ax, [start, P, (fo, hI)], col, lw=1.3)
        # continue to the eyepiece; the emergent rays are parallel to the line from the
        # image point through the eyepiece centre (slope -hI/fe)
        slope = (hI - y0) / fo
        yE = hI + slope * fe
        if abs(yE) < 1.5:
            ray(ax, [(fo, hI), (fo + fe, yE), (fo + fe + 2.3, yE - hI / fe * 2.3)], col, lw=1.3)
    obj(ax, fo, hI, ACC, None)
    ax.text(fo, 0.15, "image at $F_o$ = $F_e$", fontsize=8.5, color=ACC, va="bottom", ha="center")
    ax.text(0, 2.0, "objective ($f_o$, large aperture)", fontsize=9, ha="center", color=NEG)
    ax.text(fo + fe, 1.7, "eyepiece ($f_e$)", fontsize=9, ha="center", color=NEG)
    ax.text(-2.4, -1.4, "parallel rays from a\ndistant object, at angle α", fontsize=8.5, color=GREY)
    ax.annotate("", (fo + fe, -1.65), (0, -1.65), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text((fo + fe) / 2, -1.72, "$f_o + f_e$", fontsize=9, ha="center", va="top", color=GREY)
    ax.text(fo + fe + 0.5, 0.75, "rays emerge parallel at β:\nfinal image at infinity", fontsize=8.5, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch09_fig14_telescope.png")


# ---- Fig 9.15: Cassegrain reflecting telescope ---------------------------------------------------
def fig_cassegrain():
    fig, ax = plt.subplots(figsize=(8.4, 3.4))
    blank(ax, (-1.0, 9.6), (-2.0, 2.0))
    R1 = 14.0
    t = np.linspace(0.04, 0.115, 40)
    for sgn in (1, -1):
        ax.plot(8.0 - R1 * (1 - np.cos(t)) * 1.0 + 0 * t, sgn * R1 * np.sin(t), color=NEG, lw=2.4)
    axis_line(ax, -0.8, 9.4)
    # secondary convex mirror
    t2 = np.linspace(-0.25, 0.25, 30)
    ax.plot(3.2 + 1.2 * (1 - np.cos(t2)), 1.2 * np.sin(t2) * 1.0, color=NEG, lw=2.4)
    for y in (1.2, -1.2):
        P = (8.0 - R1 * (1 - np.cos(y / R1)), y)
        ray(ax, [(0.0, y), P], POS, lw=1.2)
        S = (3.2 + 1.2 * (1 - np.cos(y * 0.25 / 1.2 / 1.2 * 1.0)), y * 0.25)
        ray(ax, [P, S], POS, lw=1.2)
        ray(ax, [S, (9.2, 0.0)], POS, lw=1.2)
    ax.text(7.9, 1.75, "primary concave mirror\n(with a central hole)", fontsize=8.5, ha="right", color=NEG)
    ax.text(3.3, 0.45, "secondary\nconvex mirror", fontsize=8.5, ha="center", color=NEG)
    ax.text(9.25, 0.12, "eyepiece /\ncamera", fontsize=8.5)
    ax.text(0.0, 1.35, "light from a distant star", fontsize=8.5, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch09_fig15_cassegrain.png")


# ---- Fig 9.16: board diagram, HSSLC 2026 Q5 ----------------------------------------------------
def fig_board_meniscus():
    fig, ax = plt.subplots(figsize=(2.2, 2.6))
    blank(ax, (-1.0, 1.0), (-1.3, 1.3))
    t = np.linspace(-1.1, 1.1, 80)
    xl = -0.35 + 0.5 * (t / 1.1) ** 2
    xr = xl + 0.28
    ax.fill_betweenx(t, xl, xr, color=GLASS)
    ax.plot(xl, t, color=INK, lw=1.4)
    ax.plot(xr, t, color=INK, lw=1.4)
    line(ax, [(xl[0], t[0]), (xr[0], t[0])], INK, lw=1.4)
    line(ax, [(xl[-1], t[-1]), (xr[-1], t[-1])], INK, lw=1.4)
    fig.tight_layout()
    save(fig, "phy_ch09_fig16_board.png")


if __name__ == "__main__":
    fig_focus()
    fig_mirror_image()
    fig_slab_depth()
    fig_tir()
    fig_tir_prisms()
    fig_fibre()
    fig_spherical()
    fig_lensmaker()
    fig_lens_rays()
    fig_contact()
    fig_prism()
    fig_simple_microscope()
    fig_compound()
    fig_telescope()
    fig_cassegrain()
    fig_board_meniscus()
