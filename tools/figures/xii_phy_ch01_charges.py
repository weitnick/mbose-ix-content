"""Figures for Class XII Physics Chapter 1, Electric Charges and Fields.
Run: python xii_phy_ch01_charges.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Physics", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, POS, NEG, ACC, GREY, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#E9F0F7"
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


# ---- Fig 1.1: Coulomb force between two charges ----------------------------------------------
def fig_coulomb():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 2.2))
    for ax, (q1, q2), title in zip(axes, [(1, 1), (1, -1)], ["(a) Like charges repel", "(b) Unlike charges attract"]):
        blank(ax, (-0.4, 4.4), (-0.7, 0.8))
        charge(ax, (1, 0), q1)
        charge(ax, (3, 0), q2)
        ax.annotate("", (1, -0.45), (3, -0.45), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
        ax.text(2, -0.62, "r", ha="center", color=INK, style="italic")
        if q1 * q2 > 0:
            arrow(ax, (0.8, 0), (0.0, 0), POS)
            arrow(ax, (3.2, 0), (4.0, 0), POS)
            ax.text(0.2, 0.22, r"$\vec F_{12}$", ha="center")
            ax.text(3.8, 0.22, r"$\vec F_{21}$", ha="center")
        else:
            arrow(ax, (1.2, 0), (1.9, 0), NEG)
            arrow(ax, (2.8, 0), (2.1, 0), NEG)
            ax.text(1.6, 0.25, r"$\vec F_{12}$", ha="center")
            ax.text(2.4, 0.25, r"$\vec F_{21}$", ha="center")
        ax.text(1, 0.32, r"$q_1$", ha="center")
        ax.text(3, 0.32, r"$q_2$", ha="center")
        ax.set_title(title, color=INK)
    save(fig, "phy_ch01_fig01_coulomb.png")


# ---- Fig 1.2: field lines ----------------------------------------------------------------------
def field(charges, X, Y):
    Ex, Ey = np.zeros_like(X), np.zeros_like(Y)
    for (x0, y0, q) in charges:
        dx, dy = X - x0, Y - y0
        r3 = (dx ** 2 + dy ** 2) ** 1.5 + 1e-9
        Ex += q * dx / r3
        Ey += q * dy / r3
    return Ex, Ey


def fig_field_lines():
    fig, axes = plt.subplots(1, 4, figsize=(11, 3.2))
    cases = [([(0, 0, 1)], "(a) Positive charge"), ([(0, 0, -1)], "(b) Negative charge"),
             ([(-0.8, 0, 1), (0.8, 0, -1)], "(c) Dipole (+q, −q)"), ([(-0.8, 0, 1), (0.8, 0, 1)], "(d) Two equal +q")]
    x = np.linspace(-2.2, 2.2, 300)
    X, Y = np.meshgrid(x, x)
    for ax, (chs, title) in zip(axes, cases):
        Ex, Ey = field(chs, X, Y)
        seeds = []
        for (x0, y0, q) in chs:
            if q > 0 or len(chs) == 1:
                for a in np.linspace(0, 2 * np.pi, 16, endpoint=False):
                    seeds.append((x0 + 0.2 * np.cos(a), y0 + 0.2 * np.sin(a)))
        ax.streamplot(X, Y, Ex, Ey, start_points=np.array(seeds), color=GREY, linewidth=1.0, arrowsize=1.0,
                      density=3, broken_streamlines=False)
        for (x0, y0, q) in chs:
            charge(ax, (x0, y0), q, r=0.17)
        blank(ax, (-2.2, 2.2), (-2.2, 2.2))
        ax.set_title(title, color=INK, fontsize=10)
    save(fig, "phy_ch01_fig02_field_lines.png")


# ---- Fig 1.3: dipole field on the axis and on the equator --------------------------------------
def fig_dipole_points():
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.4))
    ax = axes[0]
    blank(ax, (-1.6, 5.2), (-1.0, 1.1))
    charge(ax, (-1, 0), -1)
    charge(ax, (1, 0), 1)
    ax.plot([-1.4, 5.0], [0, 0], color=GREY, lw=0.8, ls="--")
    ax.plot(4.2, 0, "o", color=INK, ms=4)
    ax.text(4.2, 0.18, "P", ha="center")
    ax.text(0, -0.25, "O", ha="center", color=INK)
    ax.annotate("", (0, -0.55), (4.2, -0.55), arrowprops=dict(arrowstyle="<->", color=GREY))
    ax.text(2.1, -0.75, "r", ha="center", style="italic")
    ax.annotate("", (-1, 0.4), (1, 0.4), arrowprops=dict(arrowstyle="<->", color=GREY))
    ax.text(0, 0.52, "2a", ha="center")
    arrow(ax, (4.2, 0), (5.0, 0), POS)
    ax.text(4.75, 0.18, r"$\vec E_{+q}$", ha="center", fontsize=9)
    arrow(ax, (4.2, 0.0), (3.75, 0.0), NEG, lw=1.3)
    ax.text(3.7, 0.18, r"$\vec E_{-q}$", ha="center", fontsize=9)
    arrow(ax, (-0.6, -0.35), (0.6, -0.35), ACC, lw=1.4)
    ax.text(0.75, -0.4, r"$\vec p$", color=ACC)
    ax.set_title("(a) Point P on the axis", color=INK)
    ax = axes[1]
    blank(ax, (-2.2, 2.2), (-0.8, 3.6))
    charge(ax, (-1, 0), -1)
    charge(ax, (1, 0), 1)
    P = (0, 2.4)
    ax.plot([0, 0], [0, 2.4], color=GREY, lw=0.8, ls="--")
    ax.plot([-1, 0], [0, 2.4], color=GREY, lw=0.8)
    ax.plot([1, 0], [0, 2.4], color=GREY, lw=0.8)
    ax.plot(*P, "o", color=INK, ms=4)
    ax.text(0.12, 2.5, "P", ha="left")
    u_plus = np.array(P) - np.array((1, 0))
    u_plus = u_plus / np.linalg.norm(u_plus)
    u_minus = np.array((-1, 0)) - np.array(P)
    u_minus = u_minus / np.linalg.norm(u_minus)
    arrow(ax, P, tuple(np.array(P) + 0.9 * u_plus), POS)
    arrow(ax, P, tuple(np.array(P) + 0.9 * u_minus), NEG)
    arrow(ax, P, (P[0] - 0.75, P[1]), INK, lw=2)
    ax.text(-1.35, 2.15, r"$\vec E$", fontsize=10, ha="center")
    ax.text(-1.5, 1.85, r"(opposite to $\vec p$)", fontsize=8, ha="center")
    ax.text(-0.1, 3.35, r"$\vec E_{+q}$", fontsize=9, ha="right")
    ax.text(-0.55, 1.55, r"$\vec E_{-q}$", fontsize=9, ha="right")
    ax.text(0.12, 1.1, "r", style="italic")
    ax.annotate("", (-1, -0.45), (1, -0.45), arrowprops=dict(arrowstyle="<->", color=GREY))
    ax.text(0, -0.7, "2a", ha="center")
    ax.set_title("(b) Point P on the equatorial line", color=INK)
    save(fig, "phy_ch01_fig03_dipole_points.png")


# ---- Fig 1.4: dipole in a uniform field --------------------------------------------------------
def fig_dipole_torque():
    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    blank(ax, (-2.6, 2.6), (-1.5, 1.6))
    for y in np.linspace(-1.3, 1.3, 6):
        arrow(ax, (-2.5, y), (2.5, y), "#C9D3DE", lw=1.0, ms=9)
    ax.text(2.45, 1.45, r"$\vec E$", color=GREY)
    th = np.radians(35)
    a = 1.1
    pp = (a * np.cos(th), a * np.sin(th))
    pm = (-a * np.cos(th), -a * np.sin(th))
    ax.plot([pm[0], pp[0]], [pm[1], pp[1]], color=INK, lw=1.4)
    charge(ax, pp, 1)
    charge(ax, pm, -1)
    arrow(ax, pp, (pp[0] + 0.9, pp[1]), POS, lw=2)
    arrow(ax, pm, (pm[0] - 0.9, pm[1]), NEG, lw=2)
    ax.text(pp[0] + 0.95, pp[1] + 0.1, r"$q\vec E$", color=POS)
    ax.text(pm[0] - 1.25, pm[1] + 0.1, r"$-q\vec E$", color=NEG)
    ax.plot([0, 1.4], [0, 0], color=GREY, lw=0.8, ls="--")
    from matplotlib.patches import Arc
    ax.add_patch(Arc((0, 0), 1.0, 1.0, theta1=0, theta2=35, color=ACC))
    ax.text(0.58, 0.14, r"$\theta$", color=ACC)
    ax.plot([pp[0], pp[0]], [0, pp[1]], color=GREY, lw=0.8, ls=":")
    ax.text(pp[0] + 0.05, 0.25, r"$2a\sin\theta$" if False else "", fontsize=8)
    ax.set_title("Dipole in a uniform field: a couple acts", color=INK, fontsize=10)
    save(fig, "phy_ch01_fig04_dipole_torque.png")


# ---- Fig 1.5: Gaussian surfaces ----------------------------------------------------------------
def fig_gauss():
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.6))
    # (a) line charge and cylinder
    ax = axes[0]
    blank(ax, (-2, 2), (-2.2, 2.2))
    ax.plot([0, 0], [-2.1, 2.1], color=POS, lw=3)
    for y in np.linspace(-1.9, 1.9, 9):
        ax.text(-0.18, y, "+", color=POS, fontsize=8, ha="center", va="center")
    ax.add_patch(Ellipse((0, 1.2), 2.4, 0.5, fill=False, color=NEG, lw=1.3))
    ax.add_patch(Ellipse((0, -1.2), 2.4, 0.5, fill=False, color=NEG, lw=1.3, ls="--"))
    ax.plot([-1.2, -1.2], [-1.2, 1.2], color=NEG, lw=1.3)
    ax.plot([1.2, 1.2], [-1.2, 1.2], color=NEG, lw=1.3)
    for y in (-0.6, 0, 0.6):
        arrow(ax, (1.2, y), (1.85, y), ACC, lw=1.4, ms=9)
        arrow(ax, (-1.2, y), (-1.85, y), ACC, lw=1.4, ms=9)
    ax.annotate("", (0, -0.2), (1.2, -0.2), arrowprops=dict(arrowstyle="<->", color=GREY))
    ax.text(0.6, -0.42, "r", ha="center", style="italic")
    ax.text(1.32, 0.95, "l", style="italic")
    ax.set_title("(a) Line charge: cylinder", color=INK, fontsize=10)
    # (b) plane sheet and pill-box
    ax = axes[1]
    blank(ax, (-2, 2), (-2.2, 2.2))
    ax.add_patch(Rectangle((-0.08, -2.0), 0.16, 4.0, color="#F3D6D2"))
    for y in np.linspace(-1.8, 1.8, 10):
        ax.text(0, y, "+", color=POS, fontsize=8, ha="center", va="center")
    ax.add_patch(Rectangle((-1.2, -0.6), 2.4, 1.2, fill=False, color=NEG, lw=1.3))
    ax.add_patch(Ellipse((1.2, 0), 0.3, 1.2, fill=False, color=NEG, lw=1.3))
    ax.add_patch(Ellipse((-1.2, 0), 0.3, 1.2, fill=False, color=NEG, lw=1.3, ls="--"))
    arrow(ax, (1.2, 0), (1.95, 0), ACC, lw=1.6)
    arrow(ax, (-1.2, 0), (-1.95, 0), ACC, lw=1.6)
    ax.text(1.55, 0.18, r"$\vec E$", color=ACC)
    ax.text(-1.75, 0.18, r"$\vec E$", color=ACC)
    ax.text(1.25, -0.95, "area A", fontsize=8, color=NEG)
    ax.set_title("(b) Plane sheet: pill-box", color=INK, fontsize=10)
    # (c) spherical shell
    ax = axes[2]
    blank(ax, (-2.2, 2.2), (-2.2, 2.2))
    ax.add_patch(Circle((0, 0), 1.2, fill=False, color=POS, lw=3))
    for a in np.linspace(0, 2 * np.pi, 14, endpoint=False):
        ax.text(1.38 * np.cos(a), 1.38 * np.sin(a), "+", color=POS, fontsize=8, ha="center", va="center")
    ax.add_patch(Circle((0, 0), 1.85, fill=False, color=NEG, lw=1.3, ls="--"))
    ax.add_patch(Circle((0, 0), 0.6, fill=False, color=NEG, lw=1.3, ls="--"))
    ax.text(0, -2.15, "r > R:  E = q/(4πε₀r²)", fontsize=8, color=INK, ha="center")
    ax.text(0, 0, "r < R\nE = 0", fontsize=8, color=INK, ha="center", va="center")
    ax.text(-0.95, 0.25, "R", fontsize=9)
    ax.set_title("(c) Spherical shell", color=INK, fontsize=10)
    save(fig, "phy_ch01_fig05_gauss_surfaces.png")


# ---- Fig 1.6: E versus r for a charged spherical shell ------------------------------------------
def fig_shell_graph():
    fig, ax = plt.subplots(figsize=(4.8, 3.0))
    R = 1.0
    r_out = np.linspace(R, 4, 200)
    ax.plot([0, R], [0, 0], color=POS, lw=2.2)
    ax.plot(r_out, 1 / r_out ** 2, color=POS, lw=2.2)
    ax.plot([R, R], [0, 1], color=GREY, lw=0.8, ls=":")
    ax.set_xlabel("distance from centre, r")
    ax.set_ylabel("E")
    ax.set_xticks([R])
    ax.set_xticklabels(["R"])
    ax.set_yticks([])
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(2.2, 0.35, r"$E\propto\frac{1}{r^2}$", fontsize=11)
    ax.text(0.2, 0.06, "E = 0 inside", fontsize=8)
    ax.set_title("Field of a charged spherical shell", color=INK, fontsize=10)
    save(fig, "phy_ch01_fig06_shell_graph.png")


# ---- Fig 1.7: flux through an area --------------------------------------------------------------
def fig_flux():
    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    blank(ax, (-2.4, 2.6), (-1.6, 1.8))
    for y in np.linspace(-1.3, 1.5, 7):
        arrow(ax, (-2.3, y), (2.5, y), "#C9D3DE", lw=1.0, ms=9)
    ax.text(2.25, 1.62, r"$\vec E$", color=GREY)
    th = np.radians(35)
    d = np.array([np.sin(th), np.cos(th)])
    ax.plot([-1.0 * d[0], 1.0 * d[0]], [-1.0 * d[1], 1.0 * d[1]], color=NEG, lw=4)
    n = np.array([np.cos(th), -np.sin(th)])
    arrow(ax, (0, 0), tuple(1.2 * n), ACC, lw=2)
    ax.text(1.25 * n[0] + 0.05, 1.25 * n[1] - 0.05, r"$\hat n$", color=ACC)
    ax.plot([0, 1.3], [0, 0], color=GREY, lw=0.8, ls="--")
    from matplotlib.patches import Arc
    ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=-35, theta2=0, color=ACC))
    ax.text(0.68, -0.28, r"$\theta$", color=ACC)
    ax.text(-0.95, 0.95, r"area $\Delta S$", color=NEG, fontsize=9)
    ax.set_title(r"Flux $\Delta\phi = E\,\Delta S\cos\theta$", color=INK, fontsize=10)
    save(fig, "phy_ch01_fig07_flux.png")


# ---- Fig 1.8: tracks of three charged particles (Exercise 1.13) --------------------------------
def fig_tracks():
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    blank(ax, (-0.3, 5.3), (-1.4, 1.5))
    ax.add_patch(Rectangle((0, 1.1), 5, 0.12, color=POS))
    ax.add_patch(Rectangle((0, -1.1), 5, 0.12, color=NEG))
    for x in np.linspace(0.3, 4.7, 9):
        ax.text(x, 1.32, "+", color=POS, ha="center", fontsize=9)
        ax.text(x, -1.28, "−", color=NEG, ha="center", fontsize=10)
    x = np.linspace(0, 4.6, 100)
    for lab, c in {"1": 0.040, "2": 0.022, "3": -0.048}.items():
        ax.plot(x, c * x ** 2, color=INK, lw=1.4)
        ax.text(4.68, c * 4.6 ** 2, lab, fontsize=9, va="center")
    ax.set_title("Exercise 1.13: tracks in a uniform field", color=INK, fontsize=10)
    save(fig, "phy_ch01_fig08_tracks.png")


fig_coulomb()
fig_field_lines()
fig_dipole_points()
fig_dipole_torque()
fig_gauss()
fig_shell_graph()
fig_flux()
fig_tracks()
