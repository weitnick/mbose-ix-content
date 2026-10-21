"""Figures for Class XII Physics Chapter 12, Atoms.
Run: python xii_phy_ch12_atoms.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Rectangle, Wedge

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Physics", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, POS, NEG, ACC, GREY, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#E9F0F7"
GREEN = "#2E7D32"
PURPLE = "#6A1B9A"
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


def line(ax, pts, color=INK, lw=1.3, ls="-"):
    xs, ys = zip(*[tuple(p) for p in pts])
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_capstyle="round")


# ---- Fig 12.1: the Geiger-Marsden experiment ----------------------------------------------------
def fig_geiger():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    blank(ax, (-4.4, 4.0), (-2.6, 2.6))
    ax.add_patch(Rectangle((-4.2, -0.9), 1.4, 1.8, fc="#9AA5B1", ec=INK))
    ax.add_patch(Rectangle((-3.7, -0.15), 0.9, 0.3, fc="white", ec="none"))
    ax.plot([-3.7], [0], "o", color=POS, ms=6)
    ax.text(-3.5, -1.25, "radioactive source\nin a lead block", fontsize=8.5, ha="center")
    for x in (-2.3, -1.9):
        ax.add_patch(Rectangle((x, 0.12), 0.15, 0.9, color="#9AA5B1"))
        ax.add_patch(Rectangle((x, -1.02), 0.15, 0.9, color="#9AA5B1"))
    ax.text(-2.05, 1.25, "collimating\nslits", fontsize=8.5, ha="center")
    arrow(ax, (-2.8, 0), (-0.12, 0), POS, lw=2, ms=11)
    ax.text(-1.5, 0.25, "α-particle beam", fontsize=8.5, color=POS)
    ax.add_patch(Rectangle((-0.06, -1.1), 0.12, 2.2, color=ACC))
    ax.text(0.0, -1.45, "thin gold foil", fontsize=8.5, ha="center", color=ACC)
    # detector circle and the rotatable screen
    ax.add_patch(Circle((0, 0), 2.4, fill=False, ec=GREY, lw=0.9, ls="--"))
    th = np.radians(40)
    D = (2.4 * np.cos(th), 2.4 * np.sin(th))
    arrow(ax, (0.06, 0.04), (D[0] * 0.92, D[1] * 0.92), POS, lw=1.4, ms=10)
    arrow(ax, (0.06, 0), (2.25, 0), POS, lw=1.0, ms=9)
    arrow(ax, (0.05, -0.05), (-1.6, -1.75), POS, lw=1.0, ms=9)
    ax.add_patch(Rectangle((D[0] - 0.05, D[1] - 0.4), 0.18, 0.8, angle=np.degrees(th), color=GREEN))
    line(ax, [(D[0] + 0.15, D[1] + 0.12), (D[0] + 0.85, D[1] + 0.7)], INK, lw=4)
    ax.text(D[0] + 0.35, D[1] - 0.6, "ZnS screen and\nmicroscope", fontsize=8.5, color=GREEN)
    ax.add_patch(Arc((0, 0), 1.4, 1.4, theta1=0, theta2=40, color=INK, lw=1))
    ax.text(0.75, 0.25, "θ", fontsize=10)
    ax.text(-2.9, -2.35, "a few α-particles bounce back", fontsize=8.5, color=POS)
    ax.text(1.0, -0.35, "most pass straight through", fontsize=8.5, color=POS)
    fig.tight_layout()
    save(fig, "phy_ch12_fig01_geiger.png")


# ---- Fig 12.2: number scattered against angle; trajectories -----------------------------------
def fig_scattering():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.8), gridspec_kw={"width_ratios": [1, 1.25]})
    ax = axes[0]
    th = np.linspace(5, 175, 200)
    n = 1.0 / np.sin(np.radians(th) / 2) ** 4
    ax.semilogy(th, n / n.max() * 1e7, color=POS, lw=2)
    pts = np.array([10, 20, 30, 45, 60, 90, 120, 150])
    vals = 1.0 / np.sin(np.radians(pts) / 2) ** 4 / n.max() * 1e7
    ax.semilogy(pts, vals * np.array([1.1, 0.9, 1.05, 0.95, 1.1, 0.9, 1.05, 1.0]), "o", color=INK, ms=4)
    ax.set_xlabel("scattering angle θ (degrees)", fontsize=9)
    ax.set_ylabel("number of α-particles scattered", fontsize=9)
    ax.set_xticks([0, 30, 60, 90, 120, 150, 180])
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("(a) Very few are scattered\nthrough large angles", fontsize=10)
    ax = axes[1]
    blank(ax, (-4.2, 3.0), (-0.6, 2.9))
    ax.add_patch(Circle((0, 0), 0.12, color=POS))
    ax.text(0.05, -0.4, "nucleus (+Ze)", fontsize=8.5, ha="center", color=POS)
    k = 0.6
    for b, col in ((0.0, NEG), (0.2, GREEN), (0.5, ACC), (1.0, PURPLE), (1.9, GREY)):
        # integrate the repulsive Coulomb motion (force k r/|r|^3, unit mass and speed)
        p = np.array([-4.0, b + 1e-4])
        v = np.array([1.0, 0.0])
        pts = [p.copy()]
        dt = 0.004
        for _ in range(6000):
            r = np.hypot(*p)
            a = k * p / r ** 3
            v = v + a * dt
            p = p + v * dt
            pts.append(p.copy())
            if p[0] > 3.0 or p[0] < -4.1 or p[1] > 2.85:
                break
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], color=col, lw=1.4)
        arrow(ax, tuple(pts[len(pts) // 6]), tuple(pts[len(pts) // 6 + 15]), col, lw=0.01, ms=9)
    line(ax, [(-4.0, 1.0), (0, 1.0)], GREY, lw=0.6, ls=":")
    line(ax, [(-4.0, 0.0), (0.3, 0.0)], GREY, lw=0.6, ls=":")
    ax.annotate("", (-3.6, 1.0), (-3.6, 0.0), arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
    ax.text(-3.5, 0.45, "b", fontsize=10, color=GREY)
    ax.text(-4.1, 2.45, "small b: large deflection;\nb = 0: bounces straight back", fontsize=8.5, color=INK)
    ax.set_title("(b) Trajectories for different impact parameters b", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch12_fig02_scattering.png")


# ---- Fig 12.3: an accelerated electron spirals in -----------------------------------------------
def fig_spiral():
    fig, ax = plt.subplots(figsize=(3.4, 3.4))
    blank(ax, (-1.6, 1.6), (-1.6, 1.6))
    t = np.linspace(0, 8 * np.pi, 800)
    r = 1.4 * np.exp(-t / 9.0)
    ax.plot(r * np.cos(t), r * np.sin(t), color=NEG, lw=1.4)
    ax.add_patch(Circle((0, 0), 0.08, color=POS))
    ax.plot([1.4], [0], "o", color=NEG, ms=6)
    for k in range(3):
        a = 0.5 + k * 0.6
        arrow(ax, (1.45 * np.cos(a), 1.45 * np.sin(a)), (1.7 * np.cos(a), 1.7 * np.sin(a)), ACC, lw=1, ms=8)
    ax.text(0, -1.55, "radiating electron loses energy", fontsize=8, ha="center")
    fig.tight_layout()
    save(fig, "phy_ch12_fig04_spiral.png")


# ---- Fig 12.4: energy levels and spectral series ------------------------------------------------
def fig_levels():
    fig, ax = plt.subplots(figsize=(8.6, 5.6))
    ax.set_xlim(0, 10.5)
    ax.set_ylim(-4.2, 0.45)
    ax.axis("off")
    E = {n: -13.6 / n ** 2 for n in range(1, 7)}
    Y = {n: -np.sqrt(-e) for n, e in E.items()}  # compressed scale so the upper levels stay readable
    for n, e in E.items():
        line(ax, [(1.2, Y[n]), (9.6, Y[n])], INK, lw=1.4)
        ax.text(1.1, Y[n], f"n = {n}", fontsize=8.5, ha="right", va="center")
        ax.text(9.7, Y[n], f"{e:.2f} eV", fontsize=8, va="center")
    line(ax, [(1.2, 0), (9.6, 0)], GREY, lw=1.2, ls="--")
    ax.text(1.1, 0, "n = ∞", fontsize=8.5, ha="right", va="center")
    ax.text(9.7, 0, "0 eV", fontsize=8, va="center")
    series = [("Lyman\n(ultraviolet)", 1, 1.6, POS), ("Balmer\n(visible)", 2, 3.4, GREEN), ("Paschen\n(infrared)", 3, 5.2, NEG),
              ("Brackett\n(infrared)", 4, 6.9, ACC), ("Pfund\n(infrared)", 5, 8.4, PURPLE)]
    for name, nf, x0, col in series:
        for k, ni in enumerate(range(nf + 1, 7)):
            x = x0 + 0.22 * k
            arrow(ax, (x, Y[ni]), (x, Y[nf]), col, lw=1.2, ms=8)
        ax.text(x0 + 0.3, Y[nf] - 0.08, name, fontsize=8, ha="center", va="top", color=col)
    ax.text(5.3, 0.3, "Energy levels of the hydrogen atom, $E_n = -13.6/n^2$ eV (spacing not to scale)", fontsize=10, ha="center", fontweight="bold")
    ax.text(4.6, -3.4, "ground state (n = 1): −13.6 eV; ionisation energy 13.6 eV", fontsize=8.5, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch12_fig05_levels.png")


# ---- Fig 12.5: de Broglie standing wave on an orbit --------------------------------------------
def fig_standing():
    fig, ax = plt.subplots(figsize=(3.8, 3.8))
    blank(ax, (-1.7, 1.7), (-1.7, 1.7))
    t = np.linspace(0, 2 * np.pi, 600)
    ax.plot(np.cos(t), np.sin(t), color=GREY, lw=0.9, ls="--")
    r = 1 + 0.18 * np.sin(4 * t)
    ax.plot(r * np.cos(t), r * np.sin(t), color=NEG, lw=1.8)
    ax.add_patch(Circle((0, 0), 0.07, color=POS))
    ax.text(0, -1.6, "2πr = nλ (here n = 4)", fontsize=9, ha="center")
    fig.tight_layout()
    save(fig, "phy_ch12_fig06_standing.png")


# ---- Fig 12.6: emission lines of hydrogen (Balmer series) ---------------------------------------
def fig_lines():
    fig, ax = plt.subplots(figsize=(8.0, 1.8))
    ax.set_xlim(380, 680)
    ax.set_ylim(0, 1)
    ax.set_facecolor("#111111")
    lines = [(656.3, "#FF2A2A", "Hα 656 nm"), (486.1, "#3FD0FF", "Hβ 486 nm"), (434.0, "#5B5BFF", "Hγ 434 nm"), (410.2, "#8A2BE2", "Hδ 410 nm")]
    for k, (lam, col, lab) in enumerate(lines):
        ax.axvline(lam, color=col, lw=3)
        ax.text(lam, 1.05 + 0.3 * (k == 3), lab, fontsize=8, ha="center", va="bottom", color=INK, transform=ax.get_xaxis_transform())
    for lam in (397.0, 388.9, 383.5):
        ax.axvline(lam, color="#7A3BB0", lw=1.2, alpha=0.8)
    ax.set_yticks([])
    ax.set_xlabel("wavelength (nm)", fontsize=9)
    fig.tight_layout()
    save(fig, "phy_ch12_fig03_lines.png")


if __name__ == "__main__":
    fig_geiger()
    fig_scattering()
    fig_spiral()
    fig_levels()
    fig_standing()
    fig_lines()
