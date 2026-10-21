"""Figures for Class XII Physics Chapter 8, Electromagnetic Waves.
Run: python xii_phy_ch08_emwaves.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyArrowPatch, Rectangle

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
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle=style, mutation_scale=ms, color=color, lw=lw, shrinkA=0, shrinkB=0))


def blank(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")


def wire(ax, pts, color=INK, lw=1.4, ls="-"):
    xs, ys = zip(*[tuple(p) for p in pts])
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_capstyle="round")


def plates(ax, xl, xr, h, signs=True):
    """Two capacitor plates seen edge-on, at x = xl (+) and x = xr (-), height 2h."""
    for x, col in ((xl, POS), (xr, NEG)):
        ax.add_patch(Rectangle((x - 0.06, -h), 0.12, 2 * h, color=col, zorder=3))
    if signs:
        for y in np.linspace(-0.8 * h, 0.8 * h, 4):
            ax.text(xl - 0.22, y, "+", color=POS, fontsize=9, ha="center", va="center")
            ax.text(xr + 0.22, y, "−", color=NEG, fontsize=10, ha="center", va="center")


# ---- Fig 8.1: Ampere's law and two surfaces with the same rim -----------------------------------
def fig_surfaces():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.3))
    for k, ax in enumerate(axes):
        blank(ax, (-3.3, 3.0), (-1.6, 1.7))
        wire(ax, [(-3.2, 0), (0.94, 0)])
        wire(ax, [(1.66, 0), (2.9, 0)])
        plates(ax, 1.0, 1.6, 1.0, signs=False)
        arrow(ax, (-3.0, 0), (-2.5, 0), POS, lw=1.8)
        ax.text(-2.75, 0.16, "i(t)", color=POS, fontsize=10, ha="center")
        # the circular loop around the wire, seen at a slant
        ax.add_patch(Ellipse((-1.0, 0), 0.5, 2.2, fill=False, ec=ACC, lw=2.2, zorder=4))
        ax.plot([-1.0], [1.1], "o", color=INK, ms=4, zorder=5)
        ax.text(-1.0, 1.28, "P", fontsize=10, ha="center", fontweight="bold")
        ax.text(-1.55, -1.35, "loop of radius r", color=ACC, fontsize=8.5, ha="center")
    ax = axes[0]
    ax.add_patch(Ellipse((-1.0, 0), 0.5, 2.2, fc=SOFT, ec="none", zorder=1))
    ax.text(-0.3, -1.35, "flat surface S₁:\nthe current i passes through it", fontsize=8.5, ha="left", color=NEG)
    ax.set_title("(a) Flat surface: B(2πr) = μ₀ i", fontsize=10)
    ax = axes[1]
    xs = np.linspace(-1.0, 1.3, 60)
    top = 1.1 - 0.4 * ((xs + 1.0) / 2.3) ** 1.5
    ax.fill_between(xs, -top, top, color=SOFT, zorder=1)
    ax.plot(xs, top, color=NEG, lw=1.2)
    ax.plot(xs, -top, color=NEG, lw=1.2)
    ax.plot([1.3, 1.3], [-0.7, 0.7], color=NEG, lw=1.2)
    for y in (-0.45, 0, 0.45):
        arrow(ax, (1.06, y), (1.54, y), GREEN, lw=1.2, ms=8)
    ax.text(1.3, 1.25, "E between\nthe plates", color=GREEN, fontsize=8.5, ha="center")
    ax.text(-0.3, -1.35, "pot-shaped surface S₂: its bottom lies\nbetween the plates; no current passes through it", fontsize=8.5, ha="left", color=NEG)
    ax.set_title("(b) Same rim, pot-shaped surface: B(2πr) = 0 ?", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch08_fig01_surfaces.png")


# ---- Fig 8.2: conduction and displacement current ----------------------------------------------
def fig_displacement():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.4), gridspec_kw={"width_ratios": [1.5, 1]})
    ax = axes[0]
    blank(ax, (-3.2, 3.2), (-1.6, 1.7))
    wire(ax, [(-3.1, 0), (-0.36, 0)])
    wire(ax, [(0.36, 0), (3.1, 0)])
    plates(ax, -0.3, 0.3, 1.1)
    for y in np.linspace(-0.85, 0.85, 5):
        arrow(ax, (-0.22, y), (0.22, y), GREEN, lw=1.1, ms=7)
    arrow(ax, (-2.8, 0), (-2.0, 0), POS, lw=1.8)
    arrow(ax, (2.0, 0), (2.8, 0), POS, lw=1.8)
    ax.text(-2.4, 0.18, "$i_c$", color=POS, fontsize=11, ha="center")
    ax.text(2.4, 0.18, "$i_c$", color=POS, fontsize=11, ha="center")
    ax.text(0, 1.35, r"$i_d = \varepsilon_0\,d\Phi_E/dt$", color=GREEN, fontsize=10, ha="center")
    ax.text(-2.45, -0.75, "conduction\ncurrent in\nthe wires", color=POS, fontsize=8.5, ha="center")
    ax.text(1.85, -0.75, "same value as the\ndisplacement current\nbetween the plates", color=GREEN, fontsize=8.5, ha="center")
    # magnetic field circles around the gap and around the wire
    for xc in (0.0, -1.2):
        ax.add_patch(Ellipse((xc, 0), 0.32, 2.7 if xc == 0 else 1.5, fill=False, ec=NEG, lw=1.4, ls="--"))
    ax.text(0.27, -1.45, "B", color=NEG, fontsize=10, fontweight="bold")
    ax.text(-0.95, -0.9, "B", color=NEG, fontsize=10, fontweight="bold")
    ax.set_title("(a) Charging capacitor: B exists between the plates too", fontsize=10)
    ax = axes[1]
    blank(ax, (-1.6, 1.6), (-1.6, 1.6))
    ax.add_patch(plt.Circle((0, 0), 1.25, fc=SOFT, ec=GREY, lw=1))
    for x in np.linspace(-0.8, 0.8, 4):
        for y in np.linspace(-0.8, 0.8, 4):
            if x * x + y * y < 1.1:
                ax.plot([x], [y], "o", color=GREEN, ms=4)
    for r in (0.55, 1.0):
        ax.add_patch(plt.Circle((0, 0), r, fill=False, ec=NEG, lw=1.3, ls="--"))
    arrow(ax, (0.02, 1.0), (-0.02, 1.0), NEG, lw=1.3, ms=11)
    arrow(ax, (-0.02, -0.55), (0.02, -0.55), NEG, lw=1.3, ms=11)
    ax.text(0, -1.5, "E out of the page (dots), increasing;\nB in circles around it", fontsize=8.5, ha="center")
    ax.set_title("(b) Cross-section between the plates", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch08_fig02_displacement.png")


# ---- Fig 8.3: a plane electromagnetic wave -----------------------------------------------------
# Oblique 2D projection: z to the right, x up, y out of the page (drawn down-left).
YX, YY = -0.35, -0.45


def proj(z, x, y):
    return z + YX * y, x + YY * y


def fig_wave():
    fig, ax = plt.subplots(figsize=(9.6, 4.0))
    blank(ax, (-1.6, 15.6), (-2.7, 2.1))
    z = np.linspace(0, 4 * np.pi, 400)
    s_ = np.sin(z)
    for zz in np.linspace(0, 4 * np.pi, 33):
        v = np.sin(zz)
        ax.plot(*zip(proj(zz, 0, 0), proj(zz, 1.4 * v, 0)), color=POS, lw=0.8, alpha=0.6)
        ax.plot(*zip(proj(zz, 0, 0), proj(zz, 0, 1.7 * v)), color=NEG, lw=0.8, alpha=0.6)
    ax.plot(*proj(z, 1.4 * s_, 0 * z), color=POS, lw=2.2)
    ax.plot(*proj(z, 0 * z, 1.7 * s_), color=NEG, lw=2.2)
    arrow(ax, proj(0, 0, 0), proj(14.6, 0, 0), INK, lw=1.4)
    ax.text(14.7, 0.15, "z: direction of\ntravel, speed c", fontsize=9, va="bottom")
    arrow(ax, proj(0, 0, 0), proj(0, 1.9, 0), GREY, lw=1, ms=9)
    ax.text(*proj(0, 2.0, 0), "x", fontsize=10, ha="center", va="bottom")
    arrow(ax, proj(0, 0, 0), proj(0, 0, 2.6), GREY, lw=1, ms=9)
    ax.text(*proj(-0.25, 0, 2.75), "y", fontsize=10, ha="center", va="top")
    ax.text(*proj(np.pi / 2 + 0.3, 1.45, 0), r"$E_x$", color=POS, fontsize=13, va="bottom")
    ax.text(*proj(np.pi / 2 + 0.3, 0, 1.85), r"$B_y$", color=NEG, fontsize=13, va="top")
    # wavelength marker between two crests of E
    for zz in (1.5 * np.pi, 3.5 * np.pi):
        ax.plot([zz, zz], [-1.6, -1.9], color=GREY, lw=1)
    ax.annotate("", (3.5 * np.pi, -1.75), (1.5 * np.pi, -1.75), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
    ax.text(2.5 * np.pi, -1.85, "wavelength λ", color=GREY, fontsize=9, ha="center", va="top")
    ax.text(7.5, -2.6, "E (red) oscillates along x, B (blue) along y; both are in phase and perpendicular to z.",
            fontsize=9, ha="center")
    fig.tight_layout()
    save(fig, "phy_ch08_fig03_wave.png")


# ---- Fig 8.5: the electromagnetic spectrum ----------------------------------------------------
BANDS = [
    ("γ-rays", 1e-15, 1e-12, "#6A1B9A"),
    ("X-rays", 1e-12, 1e-9, "#3949AB"),
    ("Ultraviolet", 1e-9, 4e-7, "#7E57C2"),
    ("", 4e-7, 7e-7, None),
    ("Infrared", 7e-7, 1e-3, "#C62828"),
    ("Microwaves", 1e-3, 1e-1, "#EF6C00"),
    ("Radio waves", 1e-1, 1e4, "#8D6E63"),
]


def fig_spectrum():
    fig, ax = plt.subplots(figsize=(10.0, 3.6))
    lo, hi = -15, 4
    ax.set_xlim(lo, hi)
    ax.set_ylim(-2.2, 2.3)
    ax.axis("off")
    for name, a, b, col in BANDS:
        la, lb = np.log10(a), np.log10(b)
        if col is None:
            for i, x in enumerate(np.linspace(la, lb, 12)):
                c = plt.cm.rainbow(1 - i / 11)
                ax.add_patch(Rectangle((x, 0), (lb - la) / 12, 1.0, color=c, lw=0))
            continue
        ax.add_patch(Rectangle((la, 0), lb - la, 1.0, color=col, alpha=0.85, lw=0))
        ax.text((la + lb) / 2, 0.5, name, color="white", fontsize=9.5, ha="center", va="center", fontweight="bold")
    # wavelength scale below
    for p in range(lo, hi + 1):
        ax.plot([p, p], [0, -0.12], color=INK, lw=0.8)
        if p % 2 == 1 or p == hi:
            ax.text(p, -0.35, f"10$^{{{p}}}$", fontsize=8, ha="center", va="top")
    ax.text(-1.0, -0.85, "wavelength λ (m)  →  increasing", fontsize=9, ha="center")
    # frequency scale above: f = c / λ
    for p in range(lo, hi + 1):
        f = 8.477 - p  # log10(3e8) = 8.477
        ax.plot([p, p], [1.0, 1.12], color=INK, lw=0.8)
        if p % 2 == 1:
            ax.text(p, 1.32, f"3×10$^{{{int(round(f - 0.477))}}}$", fontsize=7.5, ha="center", va="bottom")
    ax.text((lo + hi) / 2, 1.8, "frequency ν (Hz)  ←  increasing", fontsize=9, ha="center")
    # call-out for visible light
    vx = (np.log10(4e-7) + np.log10(7e-7)) / 2
    arrow(ax, (vx, -1.1), (vx, -0.05), INK, lw=1, ms=9)
    ax.text(vx, -1.35, "visible light, 400–700 nm\n(violet → red)", fontsize=8.5, ha="center", va="top")
    ax.text(-14.9, -1.6, "Short λ, high ν, high photon energy", fontsize=8.5, color=GREY, va="top")
    ax.text(3.9, -1.6, "Long λ, low ν, low photon energy", fontsize=8.5, color=GREY, va="top", ha="right")
    fig.tight_layout()
    save(fig, "phy_ch08_fig05_spectrum.png")


# ---- Fig 8.4: E, B and the direction of travel -------------------------------------------------
def triad(ax, labels, title):
    blank(ax, (-1.6, 1.9), (-1.35, 1.5))
    (le, lb, lc) = labels
    arrow(ax, (0, 0), (0, 1.15), POS, lw=2.2)
    ax.text(0.08, 1.2, le, color=POS, fontsize=11, va="bottom")
    arrow(ax, (0, 0), (-0.85, -0.65), NEG, lw=2.2)
    ax.text(-0.9, -0.78, lb, color=NEG, fontsize=11, ha="center", va="top")
    arrow(ax, (0, 0), (1.3, 0), INK, lw=2.2)
    ax.text(1.36, 0, lc, color=INK, fontsize=11, va="center")
    ax.plot([0], [0], "o", color=INK, ms=3)
    ax.set_title(title, fontsize=10)


def fig_triad():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.4))
    triad(axes[0], (r"$\vec{E}$ (along x)", r"$\vec{B}$ (along y)", "travel\n(along z)"),
          "(a) E, B and the direction of travel")
    triad(axes[1], (r"$\vec{E}$ = 6.3 ĵ V/m", r"$\vec{B}$ along k̂", "travel\nalong î"),
          "(b) Example 8.1: ĵ × k̂ = î")
    fig.text(0.5, 0.01, "The wave travels along E × B: turn E towards B, and a right-handed screw advances along the direction of travel.",
             fontsize=9, ha="center")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    save(fig, "phy_ch08_fig04_triad.png")


# ---- Fig 8.6: Exercise 8.1 capacitor -----------------------------------------------------------
def fig_ex81():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    blank(ax, (-3.2, 3.2), (-1.7, 1.7))
    wire(ax, [(-3.0, 0), (-0.56, 0)])
    wire(ax, [(0.56, 0), (3.0, 0)])
    plates(ax, -0.5, 0.5, 1.2, signs=False)
    arrow(ax, (-2.6, 0), (-1.6, 0), POS, lw=1.8)
    arrow(ax, (1.6, 0), (2.6, 0), POS, lw=1.8)
    ax.text(-2.1, 0.2, "0.15 A", color=POS, fontsize=10, ha="center")
    ax.text(2.1, 0.2, "0.15 A", color=POS, fontsize=10, ha="center")
    wire(ax, [(-0.5, -1.45), (0.5, -1.45)], color=GREY, lw=1)
    for x in (-0.5, 0.5):
        wire(ax, [(x, -1.35), (x, -1.55)], color=GREY, lw=1)
    ax.text(0, -1.68, "5.0 cm", fontsize=9, ha="center", va="top", color=GREY)
    wire(ax, [(-0.95, 0), (-0.95, 1.2)], color=GREY, lw=1)
    ax.text(-1.05, 0.6, "R = 12 cm", fontsize=9, ha="right", va="center", color=GREY)
    ax.text(0, 1.45, "circular plates", fontsize=9, ha="center")
    fig.tight_layout()
    save(fig, "phy_ch08_fig06_ex81.png")


if __name__ == "__main__":
    fig_surfaces()
    fig_displacement()
    fig_wave()
    fig_spectrum()
    fig_triad()
    fig_ex81()
