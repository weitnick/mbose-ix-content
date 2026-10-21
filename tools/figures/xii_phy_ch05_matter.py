"""Figures for Class XII Physics Chapter 5, Magnetism and Matter.
Run: python xii_phy_ch05_matter.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
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


def sheet_field(X, Y, half_len=1.0, half_w=0.35, n=21):
    """Field of a finite solenoid / bar magnet: two current sheets along x at y = +-half_w."""
    Bx, By = np.zeros_like(X), np.zeros_like(Y)
    for x0 in np.linspace(-half_len, half_len, n):
        for y0, I in ((half_w, 1.0), (-half_w, -1.0)):
            dx, dy = X - x0, Y - y0
            r2 = dx**2 + dy**2 + 2e-3
            Bx += -I * dy / r2
            By += I * dx / r2
    return Bx, By


def magnet(ax, c=(0, 0), L=2.0, w=0.7, fs=11):
    x0, y0 = c[0] - L / 2, c[1] - w / 2
    ax.add_patch(Rectangle((x0, y0), L / 2, w, color=NEG, zorder=4))
    ax.add_patch(Rectangle((c[0], y0), L / 2, w, color=POS, zorder=4))
    ax.text(c[0] - L / 4, c[1], "S", color="white", ha="center", va="center", fontsize=fs, fontweight="bold", zorder=5)
    ax.text(c[0] + L / 4, c[1], "N", color="white", ha="center", va="center", fontsize=fs, fontweight="bold", zorder=5)


# ---- Fig 5.1: field lines of a bar magnet, a solenoid and an electric dipole -------------------
def fig_lines():
    fig, axes = plt.subplots(1, 3, figsize=(12.6, 3.8))
    x = np.linspace(-3, 3, 300)
    y = np.linspace(-2.2, 2.2, 220)
    X, Y = np.meshgrid(x, y)
    Bx, By = sheet_field(X, Y)
    for k, ax in enumerate(axes[:2]):
        ax.streamplot(X, Y, Bx, By, color=NEG, density=1.0, linewidth=0.8, arrowsize=0.8)
        if k == 0:
            magnet(ax)
            ax.add_patch(Ellipse((-1.0, 0), 1.0, 1.4, fill=False, ec=GREEN, lw=1.4, ls="--", zorder=6))
            ax.add_patch(Ellipse((1.0, 0), 1.0, 1.4, fill=False, ec=GREEN, lw=1.4, ls="--", zorder=6))
            ax.text(-1.0, 0.85, "i", color=GREEN, fontsize=11, ha="center", fontweight="bold")
            ax.text(1.0, 0.85, "ii", color=GREEN, fontsize=11, ha="center", fontweight="bold")
            ax.set_title("(a) Bar magnet", fontsize=10)
        else:
            for xx in np.linspace(-1.0, 1.0, 11):
                ax.add_patch(Circle((xx, 0.35), 0.06, color=POS, zorder=5))
                ax.add_patch(Circle((xx, -0.35), 0.06, color=POS, zorder=5))
            ax.set_title("(b) Current-carrying solenoid", fontsize=10)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-2.2, 2.2)
        ax.set_aspect("equal")
        ax.axis("off")
    ax = axes[2]
    Ex, Ey = np.zeros_like(X), np.zeros_like(Y)
    for x0, q in ((1.0, 1), (-1.0, -1)):
        dx, dy = X - x0, Y
        r3 = (dx**2 + dy**2 + 1e-2) ** 1.5
        Ex += q * dx / r3
        Ey += q * dy / r3
    ax.streamplot(X, Y, Ex, Ey, color=ACC, density=1.0, linewidth=0.8, arrowsize=0.8)
    for x0, q in ((1.0, 1), (-1.0, -1)):
        ax.add_patch(Circle((x0, 0), 0.18, color=POS if q > 0 else NEG, zorder=5))
        ax.text(x0, 0, "+" if q > 0 else "−", color="white", ha="center", va="center", fontsize=12, fontweight="bold", zorder=6)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(c) Electric dipole (lines start and end on charges)", fontsize=10)
    save(fig, "phy_ch05_fig01_lines.png")


# ---- Fig 5.2: a magnetic dipole in a uniform field ---------------------------------------------
def fig_dipole_field():
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 3.4), gridspec_kw={"width_ratios": [1, 1.1]})
    ax = axes[0]
    blank(ax, (-2.2, 2.4), (-1.6, 1.8))
    for y in (-1.3, 1.5):
        arrow(ax, (-2.0, y), (2.3, y), ACC, lw=1.2, ms=10)
    ax.text(2.3, 1.62, r"$\vec B$", color=ACC, fontsize=11, ha="right")
    th = np.radians(35)
    u = np.array([np.cos(th), np.sin(th)])
    n = np.array([-u[1], u[0]])
    L, w = 1.6, 0.3
    c = np.array([0, 0.1])
    for s, col, lab in ((1, POS, "N"), (-1, NEG, "S")):
        p0 = c
        p1 = c + s * u * L / 2
        poly = [p0 + n * w / 2, p1 + n * w / 2, p1 - n * w / 2, p0 - n * w / 2]
        ax.add_patch(plt.Polygon(poly, color=col, zorder=4))
        ax.text(*(c + s * u * L / 3), lab, color="white", ha="center", va="center", fontsize=10, fontweight="bold", zorder=5)
    arrow(ax, c, c + 1.3 * u, GREEN, lw=1.8)
    ax.text(*(c + 1.4 * u + (0, 0.05)), r"$\vec m$", color=GREEN, fontsize=11)
    ax.add_patch(matplotlib.patches.Arc(c, 1.0, 1.0, theta1=0, theta2=35, color=INK))
    ax.text(0.6, 0.22, "θ", fontsize=11)
    ax.text(0, -0.95, r"$\vec\tau=\vec m\times\vec B$: turns $\vec m$ towards $\vec B$", ha="center", fontsize=9.5)
    ax.set_title("(a) Torque on a bar magnet; no net force", fontsize=10)
    ax = axes[1]
    t = np.linspace(0, 180, 200)
    ax.plot(t, -np.cos(np.radians(t)), color=NEG, lw=2)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.set_xticks([0, 90, 180])
    ax.set_xticklabels(["0°", "90°", "180°"])
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels(["−mB", "0", "+mB"])
    ax.set_xlabel("angle θ between m and B", fontsize=9)
    ax.set_ylabel("U", fontsize=9, rotation=0, labelpad=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(30, -0.6, "stable\n(minimum U)", fontsize=8.5, color=GREEN)
    ax.text(120, 0.12, "unstable\n(maximum U)", fontsize=8.5, color=POS)
    ax.set_title(r"(b) $U = -\vec m\cdot\vec B = -mB\cos\theta$", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch05_fig02_dipole_field.png")


# ---- Fig 5.3: axial and equatorial fields of a bar magnet -------------------------------------
def fig_axial_equatorial():
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    blank(ax, (-1.6, 6.0), (-0.6, 3.2))
    magnet(ax, (0, 0), L=1.6, w=0.5, fs=10)
    wire = lambda pts, **k: ax.plot(*zip(*pts), **k)
    wire([(0.8, 0), (5.6, 0)], color=GREY, lw=1, ls="--")
    wire([(0, 0.25), (0, 3.0)], color=GREY, lw=1, ls="--")
    ax.plot([4.2], [0], "o", color=INK, ms=5)
    arrow(ax, (4.2, 0), (5.3, 0), ACC, lw=2)
    ax.text(4.75, 0.25, r"$B_A=\dfrac{\mu_0}{4\pi}\dfrac{2m}{r^3}$", fontsize=10, ha="center", va="bottom")
    ax.text(4.2, -0.35, "axial point (along m)", fontsize=8.5, ha="center", color=GREY)
    ax.plot([0], [2.3], "o", color=INK, ms=5)
    arrow(ax, (0, 2.3), (-0.9, 2.3), ACC, lw=2)
    ax.text(0.15, 2.65, r"$B_E=-\dfrac{\mu_0}{4\pi}\dfrac{m}{r^3}$", fontsize=10)
    ax.text(0.15, 1.95, "equatorial point (opposite to m)", fontsize=8.5, color=GREY)
    arrow(ax, (-0.6, -0.45), (0.6, -0.45), GREEN, lw=1.6)
    ax.text(0, -0.6, r"$\vec m$ (S to N)", fontsize=9, color=GREEN, ha="center", va="top")
    ax.text(2.6, 2.75, "for r ≫ size of the magnet", fontsize=8.5, color=GREY)
    save(fig, "phy_ch05_fig03_axial_equatorial.png")


# ---- Fig 5.4: Gauss's law for magnetism -------------------------------------------------------
def fig_gauss():
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    x = np.linspace(-3, 3, 300)
    y = np.linspace(-2.2, 2.2, 220)
    X, Y = np.meshgrid(x, y)
    Bx, By = sheet_field(X, Y)
    ax.streamplot(X, Y, Bx, By, color=NEG, density=1.0, linewidth=0.8, arrowsize=0.8)
    magnet(ax)
    ax.add_patch(Circle((1.0, 0), 0.9, fill=False, ec=GREEN, lw=1.8, ls="--", zorder=6))
    ax.text(1.0, 1.05, "closed surface S", color=GREEN, fontsize=9, ha="center", bbox=dict(fc="white", ec="none", alpha=0.85))
    ax.text(0, -2.1, r"lines in = lines out: $\oint\vec B\cdot d\vec S = 0$ (no monopoles)", ha="center", fontsize=10, bbox=dict(fc="white", ec="none", alpha=0.9))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2.3, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "phy_ch05_fig04_gauss.png")


# ---- Fig 5.5: dia- and paramagnetic bars in a field -------------------------------------------
def fig_dia_para():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.2))
    for k, ax in enumerate(axes):
        blank(ax, (-2.4, 2.4), (-1.5, 1.5))
        dia = k == 0
        ax.add_patch(Rectangle((-0.7, -0.5), 1.4, 1.0, color=SOFT, ec=INK, lw=1.2, zorder=1))
        for y0 in np.linspace(-1.3, 1.3, 9):
            xs = np.linspace(-2.3, 2.3, 200)
            bump = np.exp(-(xs / 0.9) ** 4)
            if dia:
                ys = y0 + np.sign(y0) * 0.35 * bump * np.exp(-abs(y0) / 1.2) if y0 != 0 else y0 + 0 * xs
                ys = np.where(np.abs(y0) < 0.6, y0 + np.sign(y0 if y0 != 0 else 1) * 0.45 * bump * (1 - abs(y0) / 0.9), y0 + np.sign(y0) * 0.12 * bump)
            else:
                ys = y0 - np.sign(y0) * 0.38 * bump * min(1, abs(y0) / 0.9)
            ax.plot(xs, ys, color=NEG, lw=1)
            arrow(ax, (2.0, ys[-25]), (2.25, ys[-5]), NEG, lw=1, ms=8)
        ax.set_title("(a) Diamagnetic: lines pushed out" if dia else "(b) Paramagnetic: lines drawn in", fontsize=10)
        ax.text(0, -1.5, "field inside slightly weaker; repelled" if dia else "field inside slightly stronger; attracted", ha="center", fontsize=8.5, color=GREY)
    save(fig, "phy_ch05_fig05_dia_para.png")


# ---- Fig 5.6: domains and the effect of temperature ------------------------------------------
def fig_domains():
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.4), gridspec_kw={"width_ratios": [1, 1, 1.2]})
    rng = np.random.default_rng(3)
    for k, ax in enumerate(axes[:2]):
        blank(ax, (-0.1, 4.1), (-0.4, 3.1))
        for i in range(4):
            for j in range(3):
                ax.add_patch(Rectangle((i, j), 1, 1, fill=False, ec=GREY, lw=1))
                c = np.array([i + 0.5, j + 0.5])
                ang = rng.uniform(0, 2 * np.pi) if k == 0 else 0.0
                d = 0.35 * np.array([np.cos(ang), np.sin(ang)])
                arrow(ax, c - d, c + d, POS, lw=1.8, ms=10)
        if k == 1:
            arrow(ax, (0.3, -0.25), (3.7, -0.25), ACC, lw=1.4, ms=10)
            ax.text(2.0, -0.38, r"applied $\vec B_0$", color=ACC, fontsize=9, ha="center", va="top")
        ax.set_title("(a) Domains at random: no net M" if k == 0 else "(b) In a field: domains align and grow", fontsize=10)
    ax = axes[2]
    T = np.linspace(0, 1.3, 200)
    M = np.where(T < 1, np.sqrt(np.clip(1 - T**2, 0, None)), 0)
    ax.plot(T, M, color=NEG, lw=2)
    ax.axvline(1.0, color=GREY, ls=":", lw=1)
    ax.set_xticks([0, 1.0])
    ax.set_xticklabels(["0", r"$T_C$"])
    ax.set_yticks([])
    ax.set_xlabel("temperature", fontsize=9)
    ax.set_ylabel("magnetisation", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.05, 0.25, "ferromagnetic", fontsize=9)
    ax.text(1.03, 0.25, "para-\nmagnetic", fontsize=9)
    ax.set_title("(c) Heating destroys the domains", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch05_fig06_domains.png")


# ---- Fig 5.7: the susceptibility scale ---------------------------------------------------------
def fig_chi_scale():
    fig, ax = plt.subplots(figsize=(9.0, 2.4))
    blank(ax, (-0.3, 10.3), (-1.2, 1.6))
    arrow(ax, (0, 0), (10.1, 0), INK, lw=1.4)
    marks = [(0.4, "−1", "superconductor\n(perfect diamagnet)", NEG),
             (3.2, "about −10⁻⁵", "diamagnetic:\nBi, Cu, water", NEG),
             (5.0, "0", "vacuum", GREY),
             (6.8, "about +10⁻⁵", "paramagnetic:\nAl, Na, O₂", GREEN),
             (9.3, "≫ 1 (μr > 1000)", "ferromagnetic:\nFe, Co, Ni", POS)]
    for x, v, lab, col in marks:
        ax.plot([x, x], [-0.12, 0.12], color=col, lw=2)
        ax.text(x, 0.3, v, ha="center", fontsize=9, color=col)
        ax.text(x, -0.35, lab, ha="center", va="top", fontsize=8.5, color=col)
    ax.text(5.0, 1.25, r"magnetic susceptibility $\chi$  (with $\mu_r = 1+\chi$)  — not to scale", ha="center", fontsize=10)
    save(fig, "phy_ch05_fig07_chi_scale.png")


if __name__ == "__main__":
    fig_lines()
    fig_dipole_field()
    fig_axial_equatorial()
    fig_gauss()
    fig_dia_para()
    fig_domains()
    fig_chi_scale()
