"""Figures for Class XII Physics Chapter 10, Wave Optics.
Run: python xii_phy_ch10_waveoptics.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon, Rectangle

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


# ---- Fig 10.1: wavefronts and Huygens construction ---------------------------------------------
def fig_wavefronts():
    fig, axes = plt.subplots(1, 3, figsize=(10.6, 3.4))
    ax = axes[0]
    blank(ax, (-2.2, 2.2), (-2.2, 2.2))
    for r in (0.5, 1.0, 1.5, 2.0):
        ax.add_patch(Circle((0, 0), r, fill=False, ec=NEG, lw=1.2))
    for a in np.radians([0, 45, 90, 135, 180, 225, 270, 315]):
        arrow(ax, (0.25 * np.cos(a), 0.25 * np.sin(a)), (2.1 * np.cos(a), 2.1 * np.sin(a)), POS, lw=0.9, ms=8)
    ax.plot([0], [0], "o", color=INK, ms=4)
    ax.set_title("(a) Spherical wavefronts\nfrom a point source", fontsize=10)
    ax = axes[1]
    blank(ax, (-1.6, 2.4), (-2.0, 2.0))
    for x in (-1.0, -0.3, 0.4, 1.1, 1.8):
        line(ax, [(x, -1.7), (x, 1.7)], NEG, lw=1.2)
    for y in (-1.2, 0, 1.2):
        arrow(ax, (-1.4, y), (2.3, y), POS, lw=0.9, ms=8)
    ax.set_title("(b) Plane wavefronts:\nrays are normal to them", fontsize=10)
    ax = axes[2]
    blank(ax, (-0.2, 3.4), (-2.0, 2.0))
    R0, vt = 1.0, 0.8
    th = np.linspace(-0.95, 0.95, 60)
    ax.plot(R0 * np.cos(th), R0 * np.sin(th), color=NEG, lw=2)
    ax.plot((R0 + vt) * np.cos(th), (R0 + vt) * np.sin(th), color=POS, lw=2)
    for t in np.linspace(-0.85, 0.85, 7):
        c = (R0 * np.cos(t), R0 * np.sin(t))
        ax.add_patch(Arc(c, 2 * vt, 2 * vt, theta1=np.degrees(t) - 80, theta2=np.degrees(t) + 80, color=GREY, lw=0.9))
        ax.plot(*c, "o", color=NEG, ms=2.5)
    ax.plot([0], [0], "o", color=INK, ms=4)
    ax.text(0.05, -0.2, "O", fontsize=9)
    ax.text(R0 * np.cos(0.95) - 0.1, R0 * np.sin(0.95) + 0.1, "F₁", fontsize=9, color=NEG)
    ax.text(R0 * np.cos(-0.95) - 0.1, R0 * np.sin(-0.95) - 0.3, "F₂", fontsize=9, color=NEG)
    ax.text((R0 + vt) * np.cos(0.95) + 0.05, (R0 + vt) * np.sin(0.95), "G₁", fontsize=9, color=POS)
    ax.text((R0 + vt) * np.cos(-0.95) + 0.05, (R0 + vt) * np.sin(-0.95) - 0.2, "G₂", fontsize=9, color=POS)
    ax.text(2.0, -0.12, "wavelets\nof radius vτ", fontsize=8.5, color=GREY)
    ax.set_title("(c) Huygens construction: G₁G₂\nis the envelope of the wavelets", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch10_fig01_wavefronts.png")


# ---- Fig 10.2: refraction of a plane wave (Huygens) ------------------------------------------------
def fig_refraction():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    blank(ax, (-3.4, 3.8), (-2.6, 2.4))
    ax.add_patch(Rectangle((-3.4, -2.6), 7.2, 2.6, color=GLASS, lw=0))
    line(ax, [(-3.4, 0), (3.8, 0)], INK, lw=1.4)
    ax.text(-3.3, 0.15, "P", fontsize=10)
    ax.text(3.6, 0.15, "P′", fontsize=10)
    n = 1.5
    i = np.radians(50)
    r = np.arcsin(np.sin(i) / n)
    A = (-1.6, 0.0)
    AC = 3.0
    C = (A[0] + AC, 0.0)
    BC = AC * np.sin(i)
    # B: on the incident wavefront through A, a distance BC (along the ray) before C
    d_in = np.array([np.sin(i), -np.cos(i)])  # direction of the incident rays
    B = np.array(C) - BC * d_in
    line(ax, [A, tuple(B)], NEG, lw=2.2)
    ax.text(B[0] - 0.05, B[1] + 0.12, "B", fontsize=10, color=NEG)
    ax.text(A[0] - 0.25, A[1] + 0.12, "A", fontsize=10, color=NEG)
    for P in (np.array(A), B):
        arrow(ax, tuple(P - 1.0 * d_in), tuple(P), POS, lw=1.0, ms=9)
    arrow(ax, tuple(B), C, POS, lw=1.0, ms=9)
    AE = AC * np.sin(r)
    ax.add_patch(Arc(A, 2 * AE, 2 * AE, theta1=200, theta2=340, color=GREY, lw=1, ls="--"))
    d_out = np.array([np.sin(r), -np.cos(r)])
    E = np.array(A) + AE * d_out
    line(ax, [tuple(E), C], GREEN, lw=2.2)
    arrow(ax, A, tuple(E), POS, lw=1.0, ms=9)
    arrow(ax, C, tuple(np.array(C) + 1.0 * d_out), POS, lw=1.0, ms=9)
    ax.text(C[0] + 0.05, C[1] + 0.12, "C", fontsize=10, color=GREEN)
    ax.text(E[0] - 0.3, E[1] - 0.2, "E", fontsize=10, color=GREEN)
    line(ax, [(A[0], 1.6), (A[0], -2.2)], GREY, lw=0.8, ls=":")
    ax.text(A[0] - 0.55, 0.8, "i", fontsize=11)
    ax.text(A[0] + 0.2, -0.9, "r", fontsize=11)
    ax.text(B[0] + 0.8, B[1] - 0.3, "BC = v₁τ", fontsize=9, color=POS)
    ax.text(A[0] - 1.5, -1.2, "AE = v₂τ", fontsize=9, color=POS)
    ax.text(-3.3, 1.95, "medium 1 (speed v₁)", fontsize=9, color=GREY)
    ax.text(-3.3, -2.45, "medium 2 (speed v₂ < v₁)", fontsize=9, color=NEG)
    ax.text(1.6, 1.6, "AB: incident wavefront", fontsize=8.5, color=NEG)
    ax.text(1.6, -2.0, "CE: refracted wavefront", fontsize=8.5, color=GREEN)
    fig.tight_layout()
    save(fig, "phy_ch10_fig02_refraction.png")


# ---- Fig 10.3: reflection of a plane wave (Huygens) ------------------------------------------------
def fig_reflection():
    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    blank(ax, (-3.4, 3.8), (-0.8, 3.0))
    line(ax, [(-3.3, 0), (3.7, 0)], INK, lw=2.0)
    for x in np.linspace(-3.2, 3.6, 30):
        line(ax, [(x, 0), (x - 0.15, -0.18)], INK, lw=0.7)
    ax.text(-3.3, -0.55, "M", fontsize=10)
    ax.text(3.6, -0.55, "N", fontsize=10)
    i = np.radians(35)
    A, AC = (-1.5, 0.0), 3.0
    C = (A[0] + AC, 0.0)
    d_in = np.array([np.sin(i), -np.cos(i)])
    BC = AC * np.sin(i)
    B = np.array(C) - BC * d_in
    line(ax, [A, tuple(B)], NEG, lw=2.2)
    for P in (np.array(A), B):
        arrow(ax, tuple(P - 1.0 * d_in), tuple(P), POS, lw=1.0, ms=9)
    arrow(ax, tuple(B), C, POS, lw=1.0, ms=9)
    d_out = np.array([np.sin(i), np.cos(i)])
    E = np.array(A) + BC * d_out
    ax.add_patch(Arc(A, 2 * BC, 2 * BC, theta1=30, theta2=85, color=GREY, lw=1, ls="--"))
    line(ax, [tuple(E), C], GREEN, lw=2.2)
    arrow(ax, A, tuple(E), POS, lw=1.0, ms=9)
    arrow(ax, C, tuple(np.array(C) + 1.0 * d_out), POS, lw=1.0, ms=9)
    ax.text(A[0] - 0.25, 0.12, "A", fontsize=10, color=NEG)
    ax.text(B[0] - 0.05, B[1] + 0.12, "B", fontsize=10, color=NEG)
    ax.text(C[0] + 0.05, 0.12, "C", fontsize=10, color=GREEN)
    ax.text(E[0] - 0.25, E[1] + 0.1, "E", fontsize=10, color=GREEN)
    ax.text(B[0] + 0.75, B[1] - 0.6, "BC = vτ", fontsize=9, color=POS)
    ax.text(A[0] + 0.15, 1.15, "AE = vτ", fontsize=9, color=POS)
    ax.text(-3.3, 2.7, "AB: incident wavefront;  CE: reflected wavefront", fontsize=8.5, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch10_fig03_reflection.png")


# ---- Fig 10.4: wavefronts through a prism, a lens and from a mirror ------------------------------
def fig_wavefront_optics():
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.2))
    ax = axes[0]
    blank(ax, (-2.0, 2.6), (-1.6, 1.8))
    ax.add_patch(Polygon([(0, 1.5), (-0.6, -1.3), (0.6, -1.3)], closed=True, fc=GLASS, ec=NEG, lw=1.3))
    for x in (-1.7, -1.2):
        line(ax, [(x, -1.2), (x, 1.2)], POS, lw=1.4)
    for k, x in enumerate((1.2, 1.8)):
        line(ax, [(x + 0.35, 1.2), (x - 0.35, -1.2)], POS, lw=1.4)
    ax.set_title("(a) Thin prism: the part through\nthe thick base is delayed", fontsize=10)
    ax = axes[1]
    blank(ax, (-2.2, 3.0), (-1.6, 1.8))
    t = np.linspace(-1.3, 1.3, 60)
    ax.fill_betweenx(t, -0.25 * (1 - (t / 1.3) ** 2), 0.25 * (1 - (t / 1.3) ** 2), color=GLASS)
    ax.plot(0.25 * (1 - (t / 1.3) ** 2), t, color=NEG, lw=1.3)
    ax.plot(-0.25 * (1 - (t / 1.3) ** 2), t, color=NEG, lw=1.3)
    for x in (-1.8, -1.2):
        line(ax, [(x, -1.2), (x, 1.2)], POS, lw=1.4)
    F = (2.5, 0)
    for rr in (1.3, 1.8):
        th = np.linspace(np.pi - 0.55, np.pi + 0.55, 40)
        ax.plot(F[0] + rr * np.cos(th), rr * np.sin(th), color=POS, lw=1.4)
    ax.plot(*F, "o", color=INK, ms=3.5)
    ax.text(F[0], -0.25, "F", fontsize=9, ha="center")
    ax.set_title("(b) Convex lens: a converging\nspherical wavefront", fontsize=10)
    ax = axes[2]
    blank(ax, (-2.4, 2.2), (-1.6, 1.8))
    th = np.linspace(-0.5, 0.5, 40)
    Rm = 3.0
    ax.plot(1.6 - Rm + Rm * np.cos(th) + 0.0, Rm * np.sin(th), color=NEG, lw=2.2)
    for x in (-2.1, -1.6):
        line(ax, [(x, -1.2), (x, 1.2)], POS, lw=1.4)
    F = (1.6 - Rm / 2, 0)
    for rr in (0.6, 1.0):
        th = np.linspace(-0.6, 0.6, 40)
        ax.plot(F[0] + rr * np.cos(th), rr * np.sin(th), color=GREEN, lw=1.4)
    ax.plot(*F, "o", color=INK, ms=3.5)
    ax.text(F[0] - 0.1, -0.25, "F", fontsize=9, ha="center")
    ax.set_title("(c) Concave mirror: reflected\nwavefront converges to F", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch10_fig04_wavefront_optics.png")


# ---- Fig 10.5: Young's double-slit geometry -----------------------------------------------------
def fig_ydse():
    fig, ax = plt.subplots(figsize=(8.4, 3.8))
    blank(ax, (-1.8, 7.6), (-2.0, 2.4))
    line(ax, [(0, -1.8), (0, -0.62)], INK, lw=3)
    line(ax, [(0, -0.38), (0, 0.38)], INK, lw=3)
    line(ax, [(0, 0.62), (0, 1.8)], INK, lw=3)
    S1, S2 = (0, 0.5), (0, -0.5)
    line(ax, [(-1.5, 0.08), (-1.5, 1.0)], INK, lw=3)
    line(ax, [(-1.5, -0.08), (-1.5, -1.0)], INK, lw=3)
    ax.text(-1.75, 0.1, "S", fontsize=10)
    line(ax, [(6.5, -1.9), (6.5, 2.2)], NEG, lw=2.4)
    P = (6.5, 1.5)
    line(ax, [S1, P], POS, lw=1.3)
    line(ax, [S2, P], POS, lw=1.3)
    line(ax, [(0, 0), (6.5, 0)], GREY, lw=0.8, ls="--")
    ax.plot(*P, "o", color=INK, ms=4)
    ax.text(P[0] + 0.12, P[1], "P", fontsize=10)
    ax.text(6.62, -0.05, "O", fontsize=10)
    ax.text(-0.35, 0.5, "S₁", fontsize=10)
    ax.text(-0.35, -0.6, "S₂", fontsize=10)
    ax.annotate("", (0.35, -0.5), (0.35, 0.5), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text(0.45, -0.1, "d", fontsize=10, color=GREY)
    ax.annotate("", (6.5, -1.6), (0, -1.6), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text(3.25, -1.85, "D (D ≫ d)", fontsize=9, ha="center", color=GREY)
    ax.annotate("", (7.1, 1.5), (7.1, 0), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text(7.2, 0.7, "x", fontsize=10, color=GREY)
    ax.text(1.7, 1.75, "path difference  S₂P − S₁P ≈ xd/D", fontsize=9.5, color=POS)
    ax.text(7.2, -1.5, "screen", fontsize=9, color=NEG)
    fig.tight_layout()
    save(fig, "phy_ch10_fig05_ydse.png")


# ---- Fig 10.6: interference and single-slit diffraction patterns -------------------------------
def fig_patterns():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.0))
    ax = axes[0]
    x = np.linspace(-2.6, 2.6, 800)
    ax.plot(x, np.cos(np.pi * x) ** 2, color=POS, lw=2)
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_xticklabels(["−2β", "−β", "0", "β", "2β"])
    ax.set_yticks([])
    ax.set_ylabel("intensity", fontsize=9)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_ylim(0, 1.15)
    ax.set_title("(i) Double-slit interference: equally spaced,\nequally bright fringes, I = 4I₀cos²(φ/2)", fontsize=10)
    ax = axes[1]
    t = np.linspace(-4.5, 4.5, 1600)
    s = np.sinc(t) ** 2
    ax.plot(t, s, color=NEG, lw=2)
    ax.set_xticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
    ax.set_xticklabels(["−4", "−3", "−2", "−1", "0", "1", "2", "3", "4"])
    ax.set_xlabel("θ in units of λ/a", fontsize=9)
    ax.set_yticks([])
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_ylim(0, 1.15)
    ax.set_title("(ii) Single-slit diffraction: a wide central\nmaximum, much weaker secondary maxima", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch10_fig06_patterns.png")


# ---- Fig 10.7: single-slit geometry ---------------------------------------------------------------
def fig_single_slit():
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    blank(ax, (-2.2, 7.2), (-2.0, 2.2))
    a = 1.6
    line(ax, [(0, a / 2), (0, 2.0)], INK, lw=3)
    line(ax, [(0, -a / 2), (0, -2.0)], INK, lw=3)
    for y in np.linspace(-0.9, 0.9, 4):
        arrow(ax, (-2.0, y * 0.8), (-0.15, y * 0.8), POS, lw=0.9, ms=8)
    th = np.radians(24)
    L, M, N = (0, a / 2), (0, 0), (0, -a / 2)
    for p, col in ((L, NEG), (M, NEG), (N, NEG)):
        line(ax, [p, (p[0] + 6.0 * np.cos(th), p[1] + 6.0 * np.sin(th))], col, lw=1.1)
    line(ax, [M, (6.4, 0)], GREY, lw=0.8, ls="--")
    # perpendicular from L to the ray from N
    foot = (N[0] + a * np.sin(th) * np.cos(th), N[1] + a * np.sin(th) * np.sin(th))
    line(ax, [L, foot], GREEN, lw=1.2, ls="--")
    ax.text(foot[0] + 0.05, foot[1] - 0.35, "path difference\nNQ = a sin θ", fontsize=8.5, color=GREEN)
    ax.text(-0.35, a / 2 + 0.05, "L", fontsize=10)
    ax.text(-0.4, -0.05, "M", fontsize=10)
    ax.text(-0.35, -a / 2 - 0.25, "N", fontsize=10)
    ax.annotate("", (-0.6, -a / 2), (-0.6, a / 2), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text(-0.95, -0.1, "a", fontsize=10, color=GREY)
    ax.add_patch(Arc(M, 2.4, 2.4, theta1=0, theta2=np.degrees(th), color=INK, lw=1))
    ax.text(1.35, 0.18, "θ", fontsize=10)
    ax.text(5.0, 2.0, "to a point P on a distant screen", fontsize=8.5, color=GREY)
    ax.text(5.0, -0.35, "to C (central maximum)", fontsize=8.5, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch10_fig07_single_slit.png")


# ---- Fig 10.8: polaroids and Malus' law -----------------------------------------------------------
def fig_polaroids():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.2), gridspec_kw={"width_ratios": [1.6, 1]})
    ax = axes[0]
    blank(ax, (-0.4, 9.4), (-1.6, 1.8))
    line(ax, [(0, 0), (9.2, 0)], GREY, lw=0.8)
    arrow(ax, (8.6, 0), (9.2, 0), GREY, lw=0.8, ms=8)
    # unpolarised: star of double arrows
    for a in np.radians([0, 45, 90, 135]):
        arrow(ax, (1.0 - 0.45 * np.cos(a) * 0.4, -0.45 * np.sin(a)), (1.0 + 0.45 * np.cos(a) * 0.4, 0.45 * np.sin(a)), POS, lw=1.1, ms=7, style="<|-|>")
    ax.text(1.0, -1.0, "unpolarised\n(intensity I)", fontsize=8.5, ha="center")
    for xp, ang, lab in ((3.0, 90, "P₁"), (6.2, 50, "P₂")):
        ax.add_patch(Rectangle((xp - 0.12, -1.2), 0.24, 2.4, fc=SOFT, ec=NEG, lw=1.2))
        t = np.radians(ang)
        line(ax, [(xp - 0.1 * np.cos(t), -0.9 * np.sin(t)), (xp + 0.1 * np.cos(t), 0.9 * np.sin(t))], NEG, lw=2)
        ax.text(xp, 1.35, lab, fontsize=10, ha="center", color=NEG)
    arrow(ax, (4.6, -0.55), (4.6, 0.55), POS, lw=1.3, ms=8, style="<|-|>")
    ax.text(4.6, -1.0, "polarised,\nI₀ = I/2", fontsize=8.5, ha="center")
    t = np.radians(50)
    arrow(ax, (7.8 - 0.35 * np.cos(t), -0.45), (7.8 + 0.35 * np.cos(t), 0.45), POS, lw=1.3, ms=8, style="<|-|>")
    ax.text(7.8, -1.0, "I = I₀cos²θ", fontsize=8.5, ha="center")
    ax.text(6.4, 0.95, "θ between\npass axes", fontsize=8, color=GREY)
    ax.set_title("(a) Light through two polaroids", fontsize=10)
    ax = axes[1]
    th = np.linspace(0, 360, 400)
    ax.plot(th, np.cos(np.radians(th)) ** 2, color=POS, lw=2)
    ax.set_xticks([0, 90, 180, 270, 360])
    ax.set_xlabel("θ (degrees)", fontsize=9)
    ax.set_ylabel("I / I₀", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("(b) Malus' law: two maxima and\ntwo minima in one turn", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch10_fig08_polaroids.png")


# ---- Fig 10.9: polarisation by reflection (Brewster) --------------------------------------------
def fig_brewster():
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    blank(ax, (-3.2, 3.2), (-2.4, 2.4))
    ax.add_patch(Rectangle((-3.2, -2.4), 6.4, 2.4, color=GLASS, lw=0))
    line(ax, [(-3.2, 0), (3.2, 0)], INK, lw=1.4)
    line(ax, [(0, 2.2), (0, -2.2)], GREY, lw=0.8, ls=":")
    n = 1.5
    ib = np.arctan(n)
    rb = np.pi / 2 - ib
    Pin = (-2.2 * np.sin(ib), 2.2 * np.cos(ib))
    Pref = (2.2 * np.sin(ib), 2.2 * np.cos(ib))
    Pr = (2.2 * np.sin(rb), -2.2 * np.cos(rb))
    for a, b in ((Pin, (0, 0)), ((0, 0), Pref), ((0, 0), Pr)):
        arrow(ax, a, b, POS, lw=1.4, ms=10)
    # marks: dots (perpendicular to the plane) and short double lines (in the plane)
    def marks(p, q, dots, dashes):
        p, q = np.array(p), np.array(q)
        d = (q - p) / np.hypot(*(q - p))
        nrm = np.array([-d[1], d[0]])
        for k, f in enumerate(np.linspace(0.25, 0.75, 4)):
            c = p + f * (q - p)
            if dots and (k % 2 == 0 or not dashes):
                ax.plot(*c, "o", color=NEG, ms=4)
            if dashes and (k % 2 == 1 or not dots):
                line(ax, [tuple(c - 0.14 * nrm), tuple(c + 0.14 * nrm)], NEG, lw=1.6)
    marks(Pin, (0, 0), True, True)
    marks((0, 0), Pref, True, False)
    marks((0, 0), Pr, True, True)
    ax.add_patch(Arc((0, 0), 1.3, 1.3, theta1=90, theta2=90 + np.degrees(ib), color=INK, lw=1))
    ax.text(-0.45, 0.8, "$i_B$", fontsize=10)
    ax.add_patch(Arc((0, 0), 1.0, 1.0, theta1=270, theta2=270 + np.degrees(rb), color=INK, lw=1))
    ax.text(0.2, -0.75, "r", fontsize=10)
    ax.text(1.0, 0.25, "90°", fontsize=9, color=ACC)
    ax.text(-3.1, 2.1, "unpolarised", fontsize=8.5)
    ax.text(1.3, 2.1, "reflected: completely\npolarised (dots only)", fontsize=8.5)
    ax.text(1.0, -2.2, "refracted: partly polarised", fontsize=8.5)
    ax.text(-3.1, -2.2, "tan $i_B$ = n;  $i_B$ + r = 90°", fontsize=9, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch10_fig09_brewster.png")


if __name__ == "__main__":
    fig_wavefronts()
    fig_refraction()
    fig_reflection()
    fig_wavefront_optics()
    fig_ydse()
    fig_patterns()
    fig_single_slit()
    fig_polaroids()
    fig_brewster()
