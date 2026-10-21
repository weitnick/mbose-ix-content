"""Figures for Class XII Physics Chapter 2, Electrostatic Potential and Capacitance.
Run: python xii_phy_ch02_potential.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle, Polygon

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Physics", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, POS, NEG, ACC, GREY, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#E9F0F7"
GREEN = "#2E7D32"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def arrow(ax, p0, p1, color=INK, lw=1.6, ms=12, style="-|>"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, color=color, lw=lw, shrinkA=0, shrinkB=0))


def charge(ax, xy, q, r=0.16, fs=12):
    col = POS if q > 0 else NEG
    ax.add_patch(Circle(xy, r, color=col, zorder=5))
    ax.text(*xy, "+" if q > 0 else "−", color="white", ha="center", va="center", fontsize=fs, fontweight="bold", zorder=6)


def blank(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")


def cap(ax, x, y, label, vertical=True, gap=0.12, h=0.5, lw=2.4):
    """Draw a capacitor symbol centred at (x, y); vertical plates by default (current flows left-right)."""
    if vertical:
        ax.plot([x - gap / 2, x - gap / 2], [y - h / 2, y + h / 2], color=INK, lw=lw)
        ax.plot([x + gap / 2, x + gap / 2], [y - h / 2, y + h / 2], color=INK, lw=lw)
        ax.text(x, y + h / 2 + 0.12, label, ha="center", va="bottom", fontsize=9)
    else:
        ax.plot([x - h / 2, x + h / 2], [y + gap / 2, y + gap / 2], color=INK, lw=lw)
        ax.plot([x - h / 2, x + h / 2], [y - gap / 2, y - gap / 2], color=INK, lw=lw)
        ax.text(x + h / 2 + 0.1, y, label, ha="left", va="center", fontsize=9)


def wire(ax, pts, color=INK, lw=1.4):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="round")


# ---- Fig 2.1: potential of a point charge -----------------------------------------------------
def fig_point():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.2), gridspec_kw={"width_ratios": [1.15, 1]})
    ax = axes[0]
    blank(ax, (-0.6, 6.2), (-1.5, 0.9))
    charge(ax, (0, 0), 1)
    ax.text(0, -0.42, "Q", ha="center", style="italic")
    ax.plot([0, 6.0], [0, 0], color=GREY, lw=0.8, ls="--")
    for x, lab in ((2.0, "P"), (3.6, "R")):
        ax.plot([x], [0], "o", color=INK, ms=5)
        ax.text(x, -0.35, lab, ha="center")
    ax.text(2.0, 0.55, "r", ha="center", style="italic")
    ax.annotate("", (0.2, 0.35), (2.0, 0.35), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
    charge(ax, (5.3, 0), 1, r=0.11, fs=9)
    ax.text(5.3, -0.35, "q (from ∞)", ha="center", fontsize=9)
    arrow(ax, (5.05, 0.0), (4.0, 0.0), ACC, lw=1.8)
    ax.text(4.55, 0.25, r"$\vec F_{ext}$", ha="center", color=ACC)
    ax.text(2.9, -0.95, r"$V(P)=\dfrac{W_{\infty\to P}}{q}=\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r}$", ha="center", fontsize=11)
    ax.set_title("(a) Bringing a test charge from infinity", fontsize=10)
    ax = axes[1]
    r = np.linspace(0.35, 4, 300)
    ax.plot(r, 1 / r, color=NEG, lw=2, label=r"$V \propto 1/r$")
    ax.plot(r, 1 / r ** 2, color=POS, lw=2, ls="--", label=r"$E \propto 1/r^2$")
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 3)
    ax.set_xlabel("distance r from Q")
    ax.set_yticks([])
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("(b) V and E fall with distance", fontsize=10)
    save(fig, "phy_ch02_fig01_point_potential.png")


# ---- Fig 2.2: dipole geometry for the potential -----------------------------------------------
def fig_dipole():
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    blank(ax, (-2.6, 4.2), (-1.2, 3.0))
    A, B, P = (-1.0, 0.0), (1.0, 0.0), (3.0, 2.4)
    charge(ax, A, -1)
    charge(ax, B, 1)
    ax.text(A[0], -0.45, "A (−q)", ha="center")
    ax.text(B[0], -0.45, "B (+q)", ha="center")
    ax.plot([0], [0], "o", color=INK, ms=4)
    ax.text(0, -0.38, "O", ha="center")
    ax.plot([-2.4, 3.9], [0, 0], color=GREY, lw=0.8, ls="--")
    arrow(ax, (-0.55, 0.32), (0.55, 0.32), GREEN, lw=1.8)
    ax.text(0, 0.52, r"$\vec p$", ha="center", color=GREEN, fontsize=12)
    ax.plot([0, P[0]], [0, P[1]], color=INK, lw=1.4)
    ax.plot([A[0], P[0]], [A[1], P[1]], color=GREY, lw=1, ls=":")
    ax.plot([B[0], P[0]], [B[1], P[1]], color=GREY, lw=1, ls=":")
    ax.plot([P[0]], [P[1]], "o", color=INK, ms=5)
    ax.text(P[0] + 0.12, P[1] + 0.1, "P", fontsize=11)
    ax.text(1.35, 1.35, "r", style="italic", fontsize=11)
    ax.text(0.7, 1.55, r"$r_1$", color=GREY)
    ax.text(2.2, 1.0, r"$r_2$", color=GREY)
    th = np.linspace(0, np.arctan2(P[1], P[0]), 30)
    ax.plot(0.55 * np.cos(th), 0.55 * np.sin(th), color=ACC, lw=1.2)
    ax.text(0.7, 0.22, r"$\theta$", color=ACC)
    ax.text(-2.4, 2.6, r"$r_1^2 \approx r^2(1+\frac{2a}{r}\cos\theta)$, $r_2^2 \approx r^2(1-\frac{2a}{r}\cos\theta)$ for $r \gg a$",
            fontsize=8.6, color=INK)
    ax.set_title("Potential at P due to a dipole (AB = 2a)", fontsize=10)
    save(fig, "phy_ch02_fig02_dipole.png")


def potential_grid(charges, x, y):
    X, Y = np.meshgrid(x, y)
    V = np.zeros_like(X)
    for (cx, cy, q) in charges:
        V += q / np.sqrt((X - cx) ** 2 + (Y - cy) ** 2 + 1e-6)
    return X, Y, V


# ---- Fig 2.3: equipotential surfaces ---------------------------------------------------------
def fig_equipotentials():
    fig, axes = plt.subplots(1, 4, figsize=(12.0, 3.3))
    # (a) point charge
    ax = axes[0]
    blank(ax, (-2.2, 2.2), (-2.2, 2.2))
    for rr in (0.6, 1.1, 1.6, 2.05):
        ax.add_patch(Circle((0, 0), rr, fill=False, color=NEG, lw=1.2))
    for ang in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        arrow(ax, (0.25 * np.cos(ang), 0.25 * np.sin(ang)), (2.1 * np.cos(ang), 2.1 * np.sin(ang)), POS, lw=1, ms=8)
    charge(ax, (0, 0), 1, r=0.18)
    ax.set_title("(a) Point charge", fontsize=10)
    # (b) uniform field
    ax = axes[1]
    blank(ax, (-2.2, 2.2), (-2.2, 2.2))
    for yy in np.linspace(-1.6, 1.6, 5):
        arrow(ax, (-2.0, yy), (2.0, yy), POS, lw=1, ms=8)
    for xx in np.linspace(-1.5, 1.5, 4):
        ax.plot([xx, xx], [-2.0, 2.0], color=NEG, lw=1.4)
    ax.text(0, -2.15, "planes perpendicular to E", ha="center", fontsize=8.5, color=NEG)
    ax.set_title("(b) Uniform field", fontsize=10)
    # (c) dipole and (d) two equal positive charges
    x = np.linspace(-2.2, 2.2, 400)
    for ax, chs, title in ((axes[2], [(-0.7, 0, -1), (0.7, 0, 1)], "(c) Dipole"),
                           (axes[3], [(-0.7, 0, 1), (0.7, 0, 1)], "(d) Two equal + charges")):
        X, Y, V = potential_grid(chs, x, x)
        if chs[0][2] < 0:
            levels = [-3, -1.6, -0.9, -0.45, -0.15, 0.15, 0.45, 0.9, 1.6, 3]
        else:
            levels = [1.6, 2.0, 2.5, 2.86, 3.3, 4.2, 6]
        ax.contour(X, Y, V, levels=levels, colors=NEG, linewidths=1.0)
        if chs[0][2] < 0:
            ax.plot([0, 0], [-2.2, 2.2], color=NEG, lw=1.0, ls="--")
        Ey, Ex = np.gradient(-V, x, x)
        ax.streamplot(X, Y, Ex, Ey, color=POS, density=0.55, linewidth=0.7, arrowsize=0.7)
        for cx, cy, q in chs:
            charge(ax, (cx, cy), q, r=0.15, fs=10)
        blank(ax, (-2.2, 2.2), (-2.2, 2.2))
        ax.set_title(title, fontsize=10)
    fig.text(0.5, 0.0, "Blue: equipotential surfaces (in section).  Red: field lines — always perpendicular to the equipotentials.",
             ha="center", fontsize=9, color=GREY)
    save(fig, "phy_ch02_fig03_equipotentials.png")


# ---- Fig 2.4: conductor in a field; shielding --------------------------------------------------
def fig_conductor():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.4))
    ax = axes[0]
    blank(ax, (-3, 3), (-2, 2))
    th = np.linspace(0, 2 * np.pi, 200)
    ax.fill(1.2 * np.cos(th), 1.2 * np.sin(th), color=SOFT, ec=INK, lw=1.4)
    for yy in (-1.5, -0.75, 0, 0.75, 1.5):
        if abs(yy) < 1.2:
            xin = np.sqrt(1.2 ** 2 - yy ** 2)
            arrow(ax, (-2.9, yy), (-xin - 0.02, yy), POS, lw=1, ms=8)
            arrow(ax, (xin + 0.02, yy), (2.9, yy), POS, lw=1, ms=8)
        else:
            arrow(ax, (-2.9, yy), (2.9, yy), POS, lw=1, ms=8)
    for ang in np.linspace(0.6, 2 * np.pi - 0.6, 6):
        pass
    for ang, sgn in ((np.pi, -1), (2.6, -1), (3.7, -1), (0, 1), (0.55, 1), (-0.55, 1)):
        ax.text(1.32 * np.cos(ang), 1.32 * np.sin(ang), "+" if sgn > 0 else "−", ha="center", va="center",
                color=POS if sgn > 0 else NEG, fontsize=12, fontweight="bold")
    ax.text(0, 0, r"$\vec E = 0$" "\ninside", ha="center", va="center", fontsize=10)
    ax.set_title("(a) Conductor in an external field", fontsize=10)
    ax = axes[1]
    blank(ax, (-3, 3), (-2, 2))
    ax.add_patch(Rectangle((-2.0, -1.4), 4.0, 2.8, fc=SOFT, ec=INK, lw=1.4))
    ax.add_patch(Rectangle((-1.1, -0.7), 2.2, 1.4, fc="white", ec=INK, lw=1.2))
    ax.text(0, 0, "cavity:\nE = 0", ha="center", va="center", fontsize=10)
    for yy in (-1.0, 1.0):
        pass
    arrow(ax, (-2.9, 1.7), (2.9, 1.7), POS, lw=1, ms=8)
    arrow(ax, (-2.9, -1.7), (2.9, -1.7), POS, lw=1, ms=8)
    ax.text(0, -1.95, "outside fields do not enter the cavity — electrostatic shielding", ha="center", fontsize=8.5, color=GREY)
    ax.set_title("(b) Cavity inside a conductor", fontsize=10)
    save(fig, "phy_ch02_fig04_conductor.png")


# ---- Fig 2.5: polarisation of a dielectric -----------------------------------------------------
def fig_dielectric():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.2))
    ax = axes[0]
    blank(ax, (-3, 3), (-1.8, 1.8))
    ax.add_patch(Rectangle((-1.4, -1.3), 2.8, 2.6, fc=SOFT, ec=INK, lw=1.2))
    rng = np.random.default_rng(3)
    for i in range(12):
        x0, y0 = rng.uniform(-1.1, 1.1), rng.uniform(-1.0, 1.0)
        a = rng.uniform(0, 2 * np.pi)
        arrow(ax, (x0, y0), (x0 + 0.35 * np.cos(a), y0 + 0.35 * np.sin(a)), GREEN, lw=1.2, ms=8)
    ax.text(0, -1.6, "polar molecules, random: no field", ha="center", fontsize=8.5, color=GREY)
    ax.set_title("(a) No external field", fontsize=10)
    ax = axes[1]
    blank(ax, (-3, 3), (-1.8, 1.8))
    ax.add_patch(Rectangle((-1.4, -1.3), 2.8, 2.6, fc=SOFT, ec=INK, lw=1.2))
    for x0 in (-0.9, -0.15, 0.6):
        for y0 in (-0.8, 0, 0.8):
            arrow(ax, (x0, y0), (x0 + 0.45, y0), GREEN, lw=1.3, ms=8)
    for y0 in np.linspace(-1.1, 1.1, 6):
        ax.text(-1.55, y0, "−", color=NEG, ha="center", va="center", fontsize=12, fontweight="bold")
        ax.text(1.55, y0, "+", color=POS, ha="center", va="center", fontsize=12, fontweight="bold")
    arrow(ax, (-2.95, 1.55), (-1.9, 1.55), POS, lw=1.6)
    ax.text(-2.45, 1.2, r"$\vec E_0$", color=POS, ha="center")
    arrow(ax, (1.1, -1.55), (-1.1, -1.55), NEG, lw=1.4)
    ax.text(0, -1.78, r"field of the surface charges opposes $E_0$", ha="center", fontsize=8.5, color=NEG)
    ax.text(2.4, 0.4, r"$-\sigma_p$ … $+\sigma_p$", ha="center", fontsize=8.5)
    ax.set_title("(b) In a field: dipoles align, surfaces charge", fontsize=10)
    save(fig, "phy_ch02_fig05_dielectric.png")


# ---- Fig 2.6: parallel plate capacitor -------------------------------------------------------
def fig_parallel():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    blank(ax, (-3.2, 3.2), (-2.2, 1.9))
    ax.add_patch(Rectangle((-0.9, -1.5), 0.12, 3.0, color=POS))
    ax.add_patch(Rectangle((0.78, -1.5), 0.12, 3.0, color=NEG))
    for y0 in np.linspace(-1.0, 1.0, 6):
        arrow(ax, (-0.72, y0), (0.72, y0), INK, lw=1.0, ms=8)
    ax.text(-0.84, 1.68, "+Q (σ)", ha="center", color=POS)
    ax.text(0.84, 1.68, "−Q (−σ)", ha="center", color=NEG)
    ax.text(0, -2.0, r"between the plates: $E = \sigma/\varepsilon_0$", ha="center")
    ax.text(-2.2, 0, "region I\nE = 0", ha="center", va="center", fontsize=9, color=GREY)
    ax.text(2.2, 0, "region III\nE = 0", ha="center", va="center", fontsize=9, color=GREY)
    ax.annotate("", (-0.78, -1.3), (0.78, -1.3), arrowprops=dict(arrowstyle="<->", color=ACC))
    ax.text(0, -1.42, "d", color=ACC, ha="center", va="top", style="italic")
    ax.text(0, 1.28, "area A", ha="center", fontsize=9, color=GREY)
    ax.set_title(r"Parallel plate capacitor: $V = Ed = \dfrac{Qd}{\varepsilon_0 A}$, $C = \dfrac{\varepsilon_0 A}{d}$", fontsize=10)
    save(fig, "phy_ch02_fig06_parallel_plate.png")


# ---- Fig 2.7: partial dielectric slab -------------------------------------------------------
def fig_slab():
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    blank(ax, (-3.0, 3.0), (-1.9, 1.9))
    ax.add_patch(Rectangle((-1.6, -1.5), 0.12, 3.0, color=POS))
    ax.add_patch(Rectangle((1.48, -1.5), 0.12, 3.0, color=NEG))
    ax.add_patch(Rectangle((-0.3, -1.5), 1.2, 3.0, fc="#FCE7B2", ec=ACC, lw=1.2))
    for y0 in np.linspace(-1.2, 1.2, 5):
        arrow(ax, (-1.45, y0), (-0.35, y0), INK, lw=1.2, ms=8)
        arrow(ax, (-0.25, y0), (0.85, y0), INK, lw=0.6, ms=6)
        arrow(ax, (0.95, y0), (1.45, y0), INK, lw=1.2, ms=8)
    ax.text(0.3, 0, "K", ha="center", va="center", fontsize=14, color=ACC, fontweight="bold")
    ax.annotate("", (-0.3, -1.68), (0.9, -1.68), arrowprops=dict(arrowstyle="<->", color=ACC))
    ax.text(0.3, -1.88, "t", ha="center", color=ACC, style="italic")
    ax.annotate("", (-1.48, 1.68), (1.48, 1.68), arrowprops=dict(arrowstyle="<->", color=GREY))
    ax.text(0, 1.78, "d", ha="center", color=GREY, style="italic")
    ax.text(-2.4, 0.5, r"in air: $E_0=\dfrac{\sigma}{\varepsilon_0}$", ha="center", fontsize=9)
    ax.text(2.45, 0.5, r"in slab: $\dfrac{E_0}{K}$", ha="center", fontsize=9)
    ax.set_title(r"Slab of thickness $t$: $V = E_0(d-t) + \dfrac{E_0}{K}t$,  $C = \dfrac{\varepsilon_0 A}{d - t + t/K}$", fontsize=10)
    save(fig, "phy_ch02_fig07_slab.png")


# ---- Fig 2.8: series and parallel -----------------------------------------------------------
def fig_combinations():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.0))
    ax = axes[0]
    blank(ax, (-0.3, 6.3), (-1.2, 1.3))
    wire(ax, [(0, 0), (0.85, 0)])
    for i, (x, lab) in enumerate(((1.0, "C₁"), (2.5, "C₂"), (4.0, "C₃"))):
        cap(ax, x, 0, lab)
        if i < 2:
            wire(ax, [(x + 0.06, 0), (x + 1.44, 0)])
    wire(ax, [(4.06, 0), (6.0, 0)])
    for x, lab in ((1.0, "+Q −Q"), (2.5, "+Q −Q"), (4.0, "+Q −Q")):
        ax.text(x, -0.45, lab, ha="center", fontsize=8, color=GREY)
    ax.text(3.0, -0.95, r"same Q; $V = V_1+V_2+V_3$;  $\dfrac{1}{C} = \dfrac{1}{C_1}+\dfrac{1}{C_2}+\dfrac{1}{C_3}$", ha="center", fontsize=9.5)
    ax.text(0, 0.12, "A", fontsize=9); ax.text(5.95, 0.12, "B", fontsize=9)
    ax.set_title("(a) Series", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.3, 6.3), (-1.6, 1.4))
    wire(ax, [(0, 0), (1.5, 0)])
    wire(ax, [(1.5, -0.9), (1.5, 0.9)])
    wire(ax, [(4.5, -0.9), (4.5, 0.9)])
    wire(ax, [(4.5, 0), (6.0, 0)])
    for y, lab in ((0.9, "C₁"), (0, "C₂"), (-0.9, "C₃")):
        wire(ax, [(1.5, y), (2.94, y)])
        cap(ax, 3.0, y, lab, h=0.38)
        wire(ax, [(3.06, y), (4.5, y)])
    ax.text(3.0, -1.5, r"same V; $Q = Q_1+Q_2+Q_3$;  $C = C_1+C_2+C_3$", ha="center", fontsize=9.5)
    ax.set_title("(b) Parallel", fontsize=10)
    save(fig, "phy_ch02_fig08_combinations.png")


# ---- Fig 2.9: HSSLC 2021 (Old Course) Q19 network ---------------------------------------------
def fig_network():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 2.6), gridspec_kw={"width_ratios": [1.15, 1]})
    ax = axes[0]
    blank(ax, (-0.4, 7.6), (-1.0, 1.1))
    xs = [1.0, 2.6, 4.2, 5.8]
    labs = ["C₁ 2 μF", "C₂ 3 μF", "C₃ 5 μF", "C₄ 10 μF"]
    wire(ax, [(0, 0), (0.94, 0)])
    for i, (x, lab) in enumerate(zip(xs, labs)):
        cap(ax, x, 0, lab, h=0.42)
        nxt = xs[i + 1] - 0.06 if i < 3 else 7.0
        wire(ax, [(x + 0.06, 0), (nxt, 0)])
    wire(ax, [(0.5, 0), (0.5, 0.75), (3.4, 0.75), (3.4, 0)])        # top wire: X to node between C2 and C3
    wire(ax, [(1.8, 0), (1.8, -0.75), (5.0, -0.75), (5.0, 0)])      # bottom wire: node between C1, C2 to node after C3
    ax.plot([0, 7.0], [0, 0], "o", color=INK, ms=4)
    ax.text(-0.2, 0, "X", va="center", ha="right")
    ax.text(7.15, 0, "Y", va="center")
    ax.set_title("(a) The network (HSSLC 2021, Old Course, Q19)", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.3, 6.6), (-1.35, 1.2))
    wire(ax, [(0, 0), (1.0, 0)])
    wire(ax, [(1.0, -0.8), (1.0, 0.8)])
    wire(ax, [(3.0, -0.8), (3.0, 0.8)])
    for y, lab in ((0.8, "2 μF"), (0, "3 μF"), (-0.8, "5 μF")):
        wire(ax, [(1.0, y), (1.94, y)])
        cap(ax, 2.0, y, "", h=0.3)
        ax.text(2.2, y + 0.17, lab, fontsize=9)
        wire(ax, [(2.06, y), (3.0, y)])
    wire(ax, [(3.0, 0), (4.44, 0)])
    cap(ax, 4.5, 0, "10 μF", h=0.42)
    wire(ax, [(4.56, 0), (6.2, 0)])
    ax.text(3.1, -1.3, r"$2+3+5 = 10$ μF in series with 10 μF: $C = 5$ μF", ha="center", fontsize=9.5)
    ax.set_title("(b) Redrawn", fontsize=10)
    save(fig, "phy_ch02_fig09_network.png")


# ---- Fig 2.10: V–Q graphs ---------------------------------------------------------------------
def fig_vq():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.2))
    ax = axes[0]
    q = np.linspace(0, 1, 50)
    ax.plot(q, q, color=NEG, lw=2)
    ax.fill_between(q, 0, q, color=SOFT)
    ax.text(0.62, 0.25, r"area $=\dfrac{1}{2}QV = U$", ha="center")
    ax.set_xlabel("charge Q")
    ax.set_ylabel("potential difference V")
    ax.set_xticks([]); ax.set_yticks([])
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("(a) Energy = area under the V–Q line", fontsize=10)
    ax = axes[1]
    ax.plot(q, 1.4 * q, color=POS, lw=2)
    ax.plot(q, 0.7 * q, color=NEG, lw=2)
    ax.text(0.95, 1.38, "B", color=POS, fontsize=11)
    ax.text(0.95, 0.72, "A", color=NEG, fontsize=11)
    ax.plot([0.6, 0.6], [0, 0.84], color=GREY, ls="--", lw=1)
    ax.plot([0, 0.6], [0.84, 0.84], color=GREY, ls="--", lw=1)
    ax.plot([0, 0.6], [0.42, 0.42], color=GREY, ls="--", lw=1)
    ax.text(-0.04, 0.84, r"$V_B$", ha="right", va="center")
    ax.text(-0.04, 0.42, r"$V_A$", ha="right", va="center")
    ax.text(0.6, -0.1, "Q", ha="center")
    ax.set_xlim(0, 1.05); ax.set_ylim(0, 1.5)
    ax.set_xticks([]); ax.set_yticks([])
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("(b) Same Q: smaller V means larger C (A)", fontsize=10)
    save(fig, "phy_ch02_fig10_vq.png")


fig_point(); fig_dipole(); fig_equipotentials(); fig_conductor(); fig_dielectric(); fig_parallel(); fig_slab()
fig_combinations(); fig_network(); fig_vq()
