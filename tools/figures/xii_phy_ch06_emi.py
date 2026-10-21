"""Figures for Class XII Physics Chapter 6, Electromagnetic Induction.
Run: python xii_phy_ch06_emi.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle

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


def magnet(ax, x0, y0, L=1.6, w=0.45, left="S", right="N"):
    colL = NEG if left == "S" else POS
    colR = POS if right == "N" else NEG
    ax.add_patch(Rectangle((x0, y0 - w / 2), L / 2, w, color=colL, zorder=4))
    ax.add_patch(Rectangle((x0 + L / 2, y0 - w / 2), L / 2, w, color=colR, zorder=4))
    ax.text(x0 + L / 4, y0, left, color="white", ha="center", va="center", fontweight="bold", zorder=5)
    ax.text(x0 + 3 * L / 4, y0, right, color="white", ha="center", va="center", fontweight="bold", zorder=5)


def coil(ax, x0, y0, n=7, dx=0.16, h=1.0, w=0.32, color=INK):
    for i in range(n):
        ax.add_patch(Ellipse((x0 + i * dx, y0), w, h, fill=False, color=color, lw=1.2))
    return x0, x0 + (n - 1) * dx


def galv(ax, c, r=0.24):
    ax.add_patch(Circle(c, r, fill=False, color=INK, lw=1.4, zorder=4))
    ax.text(*c, "G", ha="center", va="center", fontsize=9, fontweight="bold", zorder=5)


def cross(ax, xy, k=0.06, color=GREY):
    wire(ax, [(xy[0] - k, xy[1] - k), (xy[0] + k, xy[1] + k)], color=color, lw=1)
    wire(ax, [(xy[0] - k, xy[1] + k), (xy[0] + k, xy[1] - k)], color=color, lw=1)


def dotsym(ax, xy, r=0.05, color=GREY):
    ax.add_patch(Circle(xy, r, color=color))


# ---- Fig 6.1: Faraday's experiments ------------------------------------------------------------
def fig_faraday():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.4))
    ax = axes[0]
    blank(ax, (-0.6, 5.4), (-1.6, 1.4))
    a, b = coil(ax, 0.3, 0)
    wire(ax, [(a, -0.5), (a, -1.2), (b + 0.0, -1.2), (b, -0.5)])
    galv(ax, ((a + b) / 2, -1.2))
    magnet(ax, 2.6, 0, left="N", right="S")
    arrow(ax, (3.6, 0.55), (2.8, 0.55), GREEN, lw=1.8)
    ax.text(3.2, 0.75, "moving in", fontsize=9, color=GREEN, ha="center")
    ax.text(2.6, -1.0, "deflection only while\nthe magnet moves;\nreverses on pulling out", fontsize=8.5, color=GREY)
    ax.set_title("(a) A magnet moved towards a coil", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.6, 5.4), (-1.6, 1.4))
    a, b = coil(ax, 0.3, 0)
    wire(ax, [(a, -0.5), (a, -1.2), (b, -1.2), (b, -0.5)])
    galv(ax, ((a + b) / 2, -1.2))
    c, d = coil(ax, 2.8, 0, color=NEG)
    wire(ax, [(c, -0.5), (c, -1.2), (c + 0.35, -1.2)])
    ax.plot([c + 0.35, c + 0.35], [-1.38, -1.02], color=INK, lw=1.6)
    ax.plot([c + 0.45, c + 0.45], [-1.3, -1.1], color=INK, lw=3)
    wire(ax, [(c + 0.45, -1.2), (c + 0.6, -1.2)])
    wire(ax, [(c + 0.6, -1.2), (c + 0.8, -1.05)], lw=1.6)
    ax.text(c + 0.72, -0.9, "K", fontsize=9)
    wire(ax, [(c + 0.85, -1.2), (d, -1.2), (d, -0.5)])
    ax.text(3.3, 0.75, r"$C_2$ (with battery)", fontsize=9, color=NEG, ha="center")
    ax.text(0.8, 0.75, r"$C_1$", fontsize=9, ha="center")
    ax.text(2.5, -1.55, "a momentary deflection only when K is pressed or released", fontsize=8.5, color=GREY, ha="center")
    ax.set_title("(b) Two fixed coils and a key", fontsize=10)
    save(fig, "phy_ch06_fig01_faraday.png")


# ---- Fig 6.2: magnetic flux ---------------------------------------------------------------------
def fig_flux():
    fig, ax = plt.subplots(figsize=(5.6, 3.2))
    blank(ax, (-1.8, 3.4), (-1.4, 1.7))
    ax.add_patch(Polygon([(-0.6, -0.9), (0.3, -0.5), (0.3, 1.2), (-0.6, 0.8)], color=SOFT, ec=NEG, lw=1.4))
    ax.text(-0.15, -1.15, "area A", ha="center", fontsize=9)
    c = np.array([-0.15, 0.15])
    n = np.array([1.0, -0.42])
    n = n / np.hypot(*n)
    arrow(ax, c, c + 1.4 * n, GREEN, lw=2)
    ax.text(*(c + 1.5 * n + (0.05, -0.15)), r"$\vec A$ (normal)", color=GREEN, fontsize=10)
    for y in (-0.9, -0.3, 0.3, 0.9, 1.4):
        arrow(ax, (-1.7, y), (3.2, y), ACC, lw=1, ms=9)
    ax.text(3.25, 1.4, r"$\vec B$", color=ACC, fontsize=11, va="center")
    ax.add_patch(Arc(c, 1.2, 1.2, theta1=np.degrees(np.arctan2(n[1], n[0])), theta2=0, color=INK))
    ax.text(0.65, -0.05, "θ", fontsize=11)
    ax.text(0.8, 1.2, r"$\Phi_B = \vec B\cdot\vec A = BA\cos\theta$", fontsize=11, bbox=dict(fc="white", ec="none", alpha=0.9))
    save(fig, "phy_ch06_fig02_flux.png")


# ---- Fig 6.3: Lenz's law ----------------------------------------------------------------------
def fig_lenz():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.4))
    for k, ax in enumerate(axes):
        blank(ax, (-1.4, 4.4), (-1.6, 1.6))
        ax.add_patch(Ellipse((0, 0), 0.6, 2.0, fill=False, color=INK, lw=2))
        towards = k == 0
        magnet(ax, 1.4, 0, left="N", right="S")
        if towards:
            arrow(ax, (3.4, 0.55), (2.4, 0.55), GREEN, lw=1.8)
            ax.text(2.9, 0.78, "N pole approaching", fontsize=9, color=GREEN, ha="center")
            ax.text(0.45, 1.25, "N", fontsize=12, color=POS, fontweight="bold")
            arrow(ax, (-0.32, 0.4), (-0.25, 0.7), POS, lw=1.6)
            ax.text(-1.35, 1.1, "anticlockwise\n(seen from the magnet)", fontsize=8, color=POS)
            ax.text(1.8, -1.2, "repulsion: work must be done\nto push the magnet in", fontsize=8.5, color=GREY)
            ax.set_title("(a) Flux increasing: the coil's face becomes N", fontsize=10)
        else:
            arrow(ax, (2.4, 0.55), (3.4, 0.55), GREEN, lw=1.8)
            ax.text(2.9, 0.78, "N pole receding", fontsize=9, color=GREEN, ha="center")
            ax.text(0.45, 1.25, "S", fontsize=12, color=NEG, fontweight="bold")
            arrow(ax, (-0.25, 0.7), (-0.32, 0.4), POS, lw=1.6)
            ax.text(-1.35, 1.1, "clockwise\n(seen from the magnet)", fontsize=8, color=POS)
            ax.text(1.8, -1.2, "attraction: work must be done\nto pull the magnet away", fontsize=8.5, color=GREY)
            ax.set_title("(b) Flux decreasing: the coil's face becomes S", fontsize=10)
    save(fig, "phy_ch06_fig03_lenz.png")


# ---- Fig 6.4: motional emf --------------------------------------------------------------------
def fig_motional():
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    blank(ax, (-0.8, 5.4), (-1.0, 2.6))
    ax.add_patch(Rectangle((-0.6, -0.6), 5.8, 2.9, color=SOFT, ec="none", zorder=0))
    for x in np.arange(-0.4, 5.2, 0.45):
        for y in np.arange(-0.4, 2.2, 0.45):
            cross(ax, (x, y))
    ax.text(-0.55, 2.4, r"$\vec B$ into the page", fontsize=9, color=GREY, ha="left")
    P, Q, R, S = (1.0, 1.8), (1.0, 0.0), (4.6, 0.0), (4.6, 1.8)
    wire(ax, [(0.2, 1.8), S, R, (0.2, 0.0)], lw=2)
    wire(ax, [P, Q], color=POS, lw=4)
    for p, l, dx, dy in ((P, "P", -0.2, 0.2), (Q, "Q", -0.2, -0.25), (R, "R", 0.2, -0.25), (S, "S", 0.2, 0.2)):
        ax.text(p[0] + dx, p[1] + dy, l, fontsize=10, style="italic")
    arrow(ax, (1.0, 0.9), (0.2, 0.9), GREEN, lw=2)
    ax.text(0.55, 1.1, "v", color=GREEN, fontsize=11, style="italic", ha="center")
    ax.annotate("", (1.0, -0.45), (4.6, -0.45), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
    ax.text(2.8, -0.72, "x", fontsize=10, style="italic", ha="center")
    ax.annotate("", (4.95, 0.0), (4.95, 1.8), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
    ax.text(5.1, 0.9, "l", fontsize=10, style="italic")
    arrow(ax, (2.8, 0.0), (3.2, 0.0), POS, lw=1.6)
    arrow(ax, (4.6, 0.7), (4.6, 1.1), POS, lw=1.6)
    arrow(ax, (3.2, 1.8), (2.8, 1.8), POS, lw=1.6)
    arrow(ax, (1.0, 1.1), (1.0, 0.7), POS, lw=1.6)
    ax.text(2.8, 0.9, "I", color=POS, fontsize=12, style="italic", ha="center")
    ax.text(2.8, 2.15, r"$\Phi_B = Blx,\ \ \varepsilon = Bl\,\dfrac{dx}{dt} = Blv$", fontsize=11, ha="center", bbox=dict(fc="white", ec="none", alpha=0.9))
    save(fig, "phy_ch06_fig04_motional.png")


# ---- Fig 6.5: a rotating rod ------------------------------------------------------------------
def fig_rotating():
    fig, ax = plt.subplots(figsize=(4.6, 3.8))
    blank(ax, (-1.8, 1.8), (-1.7, 1.9))
    for x in np.arange(-1.5, 1.6, 0.4):
        for y in np.arange(-1.5, 1.6, 0.4):
            if x * x + y * y < 2.4:
                dotsym(ax, (x, y), r=0.035)
    ax.add_patch(Circle((0, 0), 1.4, fill=False, color=INK, lw=2.2))
    th = np.radians(35)
    wire(ax, [(0, 0), (1.4 * np.cos(th), 1.4 * np.sin(th))], color=POS, lw=4)
    ax.plot([0], [0], "o", color=INK, ms=6)
    ax.text(-0.25, -0.2, "O", fontsize=10, style="italic")
    ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=35, theta2=95, color=GREEN, lw=1.6))
    arrow(ax, (0.6 * np.cos(np.radians(90)), 0.6 * np.sin(np.radians(90))), (0.6 * np.cos(np.radians(98)), 0.6 * np.sin(np.radians(98))), GREEN, lw=1.6)
    ax.text(0.15, 0.75, "ω", color=GREEN, fontsize=12)
    ax.text(0.85, 0.35, "R", fontsize=10, style="italic")
    ax.text(0, -1.65, r"$\varepsilon = \frac{1}{2}B\omega R^2$  ($\vec B$ out of the page)", fontsize=10.5, ha="center")
    save(fig, "phy_ch06_fig05_rotating.png")


# ---- Fig 6.6: mutual inductance of coaxial solenoids ------------------------------------------
def fig_mutual():
    fig, ax = plt.subplots(figsize=(6.6, 2.8))
    blank(ax, (-0.6, 6.4), (-1.3, 1.4))
    for i in range(22):
        x = 0.3 + i * 0.25
        ax.add_patch(Ellipse((x, 0), 0.22, 2.0, fill=False, color=NEG, lw=1.0))
    for i in range(14):
        x = 1.2 + i * 0.25
        ax.add_patch(Ellipse((x, 0), 0.14, 0.9, fill=False, color=POS, lw=1.2))
    ax.text(5.9, 1.15, r"$S_2$: $n_2$ turns per m (outer)", fontsize=9, color=NEG, ha="right")
    ax.text(3.0, 0.6, r"$S_1$: $n_1$ turns per m, radius $r_1$", fontsize=9, color=POS, ha="center", bbox=dict(fc="white", ec="none", alpha=0.85))
    ax.annotate("", (0.3, -1.15), (5.55, -1.15), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
    ax.text(2.9, -1.35, "length l (both)", fontsize=9, color=GREY, ha="center", va="top")
    ax.text(3.0, -0.55, r"$M = \mu_0 n_1 n_2 \pi r_1^2 l$", fontsize=11, ha="center", bbox=dict(fc="white", ec="none", alpha=0.9))
    save(fig, "phy_ch06_fig06_mutual.png")


# ---- Fig 6.7: the ac generator ----------------------------------------------------------------
def fig_generator():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.6), gridspec_kw={"width_ratios": [1, 1.2]})
    ax = axes[0]
    blank(ax, (-2.6, 2.8), (-2.2, 1.9))
    ax.add_patch(Rectangle((-2.4, -0.7), 0.8, 1.6, color=POS))
    ax.text(-2.0, 0.1, "N", color="white", fontsize=13, fontweight="bold", ha="center", va="center")
    ax.add_patch(Rectangle((1.6, -0.7), 0.8, 1.6, color=NEG))
    ax.text(2.0, 0.1, "S", color="white", fontsize=13, fontweight="bold", ha="center", va="center")
    for y in (-0.4, 0.1, 0.6):
        arrow(ax, (-1.55, y), (1.55, y), ACC, lw=1, ms=8)
    ax.add_patch(Polygon([(-0.6, -0.5), (0.5, -0.2), (0.5, 0.9), (-0.6, 0.6)], fill=False, ec=INK, lw=2.2))
    wire(ax, [(0, -0.35), (0, -1.15)], lw=2)
    ax.add_patch(Ellipse((0, -1.2), 0.5, 0.16, fill=False, ec=INK, lw=1.6))
    ax.add_patch(Ellipse((0, -1.45), 0.5, 0.16, fill=False, ec=INK, lw=1.6))
    ax.text(0.35, -1.38, "slip rings", fontsize=8.5)
    ax.add_patch(Rectangle((-0.42, -1.27), 0.12, 0.14, color=GREY))
    ax.add_patch(Rectangle((-0.42, -1.52), 0.12, 0.14, color=GREY))
    ax.text(-1.4, -1.3, "brushes", fontsize=8.5)
    wire(ax, [(-0.42, -1.2), (-1.0, -1.2), (-1.0, -1.95), (-0.5, -1.95)])
    wire(ax, [(-0.42, -1.45), (-0.75, -1.45), (-0.75, -1.7)])
    ax.add_patch(Circle((-0.25, -1.95), 0.18, fill=False, ec=INK, lw=1.3))
    ax.text(-0.25, -1.95, "L", fontsize=8, ha="center", va="center")
    wire(ax, [(-0.07, -1.95), (0.3, -1.95)])
    ax.text(0.35, -2.0, "load", fontsize=8.5)
    ax.annotate("", (0.75, 1.25), (-0.75, 1.25), arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.6, connectionstyle="arc3,rad=-0.3"))
    ax.text(0, 1.6, "armature turned at ω", fontsize=9, color=GREEN, ha="center")
    ax.set_title("(a) A simple ac generator", fontsize=10)
    ax = axes[1]
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot(t, np.sin(t), color=NEG, lw=2)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
    ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels([r"$-\varepsilon_0$", "0", r"$\varepsilon_0$"])
    ax.set_xlabel("ωt (angle between B and the area vector)", fontsize=9)
    ax.set_ylabel("emf", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.15, -0.35, "plane ⊥ B:\nflux largest,\nemf zero", fontsize=8)
    ax.text(np.pi / 2 - 0.4, 1.08, "plane ∥ B: emf largest", fontsize=8)
    ax.set_title(r"(b) $\varepsilon = NBA\omega\sin\omega t = \varepsilon_0\sin\omega t$", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch06_fig07_generator.png")


if __name__ == "__main__":
    fig_faraday()
    fig_flux()
    fig_lenz()
    fig_motional()
    fig_rotating()
    fig_mutual()
    fig_generator()
