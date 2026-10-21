"""Figures for Class XII Physics Chapter 4, Moving Charges and Magnetism.
Run: python xii_phy_ch04_magnetism.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle, Wedge

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


def dot(ax, xy, r=0.16, color=INK, out=True):
    """Current or field out of the page (dot) or into it (cross)."""
    ax.add_patch(Circle(xy, r, fill=False, color=color, lw=1.4, zorder=4))
    if out:
        ax.add_patch(Circle(xy, r * 0.28, color=color, zorder=5))
    else:
        k = r * 0.62
        wire(ax, [(xy[0] - k, xy[1] - k), (xy[0] + k, xy[1] + k)], color=color, lw=1.3)
        wire(ax, [(xy[0] - k, xy[1] + k), (xy[0] + k, xy[1] - k)], color=color, lw=1.3)


def cross(ax, xy, k=0.07, color=GREY, lw=1.0):
    wire(ax, [(xy[0] - k, xy[1] - k), (xy[0] + k, xy[1] + k)], color=color, lw=lw)
    wire(ax, [(xy[0] - k, xy[1] + k), (xy[0] + k, xy[1] - k)], color=color, lw=lw)


def needle(ax, c, u, L=0.5, w=0.09):
    c, u = np.array(c, float), np.array(u, float) / np.hypot(*u)
    n = np.array([-u[1], u[0]])
    ax.add_patch(Polygon([c + u * L / 2, c + n * w, c - n * w], color=POS, zorder=5))
    ax.add_patch(Polygon([c - u * L / 2, c + n * w, c - n * w], color=NEG, zorder=5))


def _frame(p0, p1):
    p0, p1 = np.array(p0, float), np.array(p1, float)
    d = p1 - p0
    length = float(np.hypot(*d))
    u = d / length
    return p0, p1, length, u, np.array([-u[1], u[0]])


def res(ax, p0, p1, label=None, side=1, L=0.8, amp=0.12, n=6, fs=9):
    p0, p1, length, u, nrm = _frame(p0, p1)
    L = min(L, 0.8 * length)
    a = p0 + u * (length - L) / 2
    b = a + u * L
    wire(ax, [p0, a])
    wire(ax, [b, p1])
    pts = [a + u * L * t + nrm * amp * (0 if i in (0, 2 * n) else (1 if i % 2 else -1)) for i, t in enumerate(np.linspace(0, 1, 2 * n + 1))]
    wire(ax, pts)
    if label:
        ax.text(*((a + b) / 2 + nrm * side * (amp + 0.22)), label, ha="center", va="center", fontsize=fs)


def galv(ax, p0, p1, r=0.25, label="G"):
    p0, p1, length, u, nrm = _frame(p0, p1)
    m = (p0 + p1) / 2
    wire(ax, [p0, m - u * r])
    wire(ax, [m + u * r, p1])
    ax.add_patch(Circle(m, r, fill=False, color=INK, lw=1.4))
    ax.text(*m, label, ha="center", va="center", fontsize=10, fontweight="bold")


def carrow(ax, xy, direction, label=None, color=POS, off=(0, 0.22), fs=9):
    u = np.array(direction, float)
    u = u / np.hypot(*u)
    xy = np.array(xy, float)
    arrow(ax, xy - u * 0.13, xy + u * 0.13, color, lw=1.4, ms=11)
    if label:
        ax.text(xy[0] + off[0], xy[1] + off[1], label, ha="center", va="center", fontsize=fs, color=color)


def wires_field(X, Y, wires):
    """2D field of long straight wires (x0, y0, I) with I > 0 out of the page."""
    Bx, By = np.zeros_like(X), np.zeros_like(Y)
    for x0, y0, I in wires:
        dx, dy = X - x0, Y - y0
        r2 = dx**2 + dy**2 + 1e-3
        Bx += -I * dy / r2
        By += I * dx / r2
    return Bx, By


# ---- Fig 4.1: Oersted's observation -------------------------------------------------------------
def fig_oersted():
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.6))
    for k, ax in enumerate(axes[:2]):
        blank(ax, (-1.9, 1.9), (-1.9, 1.9))
        out = k == 0
        dot(ax, (0, 0), r=0.2, color=POS, out=out)
        for ang in np.arange(0, 360, 45):
            t = np.radians(ang)
            c = 1.25 * np.array([np.cos(t), np.sin(t)])
            u = np.array([-np.sin(t), np.cos(t)]) * (1 if out else -1)
            needle(ax, c, u)
        ax.set_title("(a) Current out of the page" if out else "(b) Current into the page", fontsize=10)
        ax.text(0, -1.8, "needles point anticlockwise" if out else "needles point clockwise", ha="center", fontsize=8.5, color=GREY)
    ax = axes[2]
    blank(ax, (-1.9, 1.9), (-1.9, 1.9))
    dot(ax, (0, 0), r=0.2, color=POS, out=True)
    for r in (0.55, 0.95, 1.4):
        ax.add_patch(Circle((0, 0), r, fill=False, color=NEG, lw=1.1))
        arrow(ax, (r, -0.05), (r, 0.08), NEG, lw=1.2, ms=10)
    ax.set_title("(c) Field lines: concentric circles", fontsize=10)
    ax.text(0, -1.8, "right-hand rule: thumb along I, fingers curl along B", ha="center", fontsize=8.5, color=GREY)
    save(fig, "phy_ch04_fig01_oersted.png")


# ---- Fig 4.2: the magnetic force on a moving charge --------------------------------------------
def fig_lorentz():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.4))
    ax = axes[0]
    blank(ax, (-0.6, 3.4), (-0.6, 2.4))
    o = np.array([0.2, 0.2])
    arrow(ax, o, o + (2.6, 0), NEG, lw=2)
    ax.text(2.95, 0.2, r"$\vec v$", color=NEG, fontsize=12, va="center")
    t = np.radians(40)
    arrow(ax, o, o + 2.2 * np.array([np.cos(t), np.sin(t)]), ACC, lw=2)
    ax.text(*(o + 2.4 * np.array([np.cos(t), np.sin(t)])), r"$\vec B$", color=ACC, fontsize=12)
    ax.add_patch(Arc(o, 1.2, 1.2, theta1=0, theta2=40, color=INK))
    ax.text(0.95, 0.42, "θ", fontsize=11)
    dot(ax, o, r=0.18, color=POS, out=True)
    ax.text(0.2, -0.35, r"$\vec F = q\,\vec v\times\vec B$ (out of page for $q>0$)", fontsize=9.5, color=POS)
    ax.text(0.2, 1.95, r"$F = qvB\sin\theta$", fontsize=11)
    ax.set_title("(a) Direction of the magnetic force", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.4, 4.4), (-2.0, 1.6))
    ax.add_patch(Rectangle((1.6, -1.5), 2.7, 3.0, color=SOFT, ec=GREY, lw=0.8))
    for x in np.arange(1.85, 4.3, 0.45):
        for y in np.arange(-1.3, 1.4, 0.45):
            cross(ax, (x, y))
    ax.text(2.95, -1.62, r"$\vec B$ into the page", ha="center", fontsize=9, color=GREY, va="top")
    for sgn, col, lab in ((1, POS, "+q"), (-1, NEG, "−q")):
        th = np.linspace(-np.pi / 2, 0, 40)
        R = 1.15
        xs = 1.6 + R * np.cos(th)
        ys = sgn * (R + R * np.sin(th)) * 1.0
        wire(ax, [(0.0, 0.0), (1.6, 0.0)], color=col, lw=1.6)
        wire(ax, list(zip(xs, ys)), color=col, lw=1.6)
        arrow(ax, (xs[-2], ys[-2]), (xs[-1], ys[-1] + sgn * 0.01), col, lw=1.6)
        ax.text(2.95, sgn * 1.25, lab, color=col, fontsize=10, ha="center")
    ax.plot([0], [0], "o", color=INK, ms=4)
    ax.text(0.0, 0.25, "same v", fontsize=8.5)
    ax.set_title("(b) Opposite charges bend opposite ways", fontsize=10)
    save(fig, "phy_ch04_fig02_lorentz.png")


# ---- Fig 4.3: circular and helical motion ------------------------------------------------------
def fig_motion():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.6), gridspec_kw={"width_ratios": [1, 1.4]})
    ax = axes[0]
    blank(ax, (-2.0, 2.0), (-2.0, 2.0))
    for x in np.arange(-1.8, 1.9, 0.45):
        for y in np.arange(-1.8, 1.9, 0.45):
            cross(ax, (x, y), k=0.05)
    ax.add_patch(Circle((0, 0), 1.25, fill=False, color=POS, lw=1.8))
    p = np.array([0, -1.25])
    ax.plot(*p, "o", color=POS, ms=8, zorder=6)
    arrow(ax, p, p + (0.9, 0), NEG, lw=1.8)
    ax.text(1.0, -1.5, r"$\vec v$", color=NEG, fontsize=11)
    arrow(ax, p, p + (0, 0.75), ACC, lw=1.8)
    ax.text(0.12, -0.75, r"$\vec F$", color=ACC, fontsize=11)
    wire(ax, [(0, 0), (0.88, 0.88)], color=GREY, lw=1)
    ax.text(0.35, 0.6, "r", fontsize=11, style="italic")
    ax.set_title(r"(a) $\vec v \perp \vec B$: a circle, $r = mv/qB$", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.5, 6.6), (-1.6, 1.8))
    t = np.linspace(0, 6.3 * np.pi, 900)
    x = 0.3 + 0.2 * t + 0.5 * np.sin(t)
    y = 0.85 * np.cos(t)
    ax.plot(x, y, color=POS, lw=1.7)
    arrow(ax, (x[-3], y[-3]), (x[-1], y[-1]), POS, lw=1.7)
    arrow(ax, (0, -1.35), (6.3, -1.35), ACC, lw=1.6)
    ax.text(6.35, -1.35, r"$\vec B$", color=ACC, fontsize=11, va="center")
    x0, x1 = 0.3, 0.3 + 0.2 * 2 * np.pi
    ax.annotate("", (x0, 1.25), (x1, 1.25), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
    ax.text((x0 + x1) / 2, 1.45, r"pitch $p = v_\parallel T = \dfrac{2\pi m v_\parallel}{qB}$", ha="center", fontsize=9.5)
    ax.set_title(r"(b) $\vec v$ at an angle to $\vec B$: a helix", fontsize=10, pad=14)
    save(fig, "phy_ch04_fig03_motion.png")


# ---- Fig 4.4: Biot-Savart law -------------------------------------------------------------------
def fig_biot():
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    blank(ax, (-0.5, 5.2), (-1.3, 2.6))
    wire(ax, [(0, -1.0), (0, 2.4)], color=INK, lw=2)
    ax.text(-0.3, -1.0, "X", fontsize=10)
    ax.text(-0.3, 2.35, "Y", fontsize=10)
    arrow(ax, (0, 0.4), (0, 1.0), POS, lw=2.4)
    ax.text(-0.45, 0.7, r"$I\,d\vec l$", color=POS, fontsize=11)
    P = np.array([3.6, 1.6])
    wire(ax, [(0, 0.7), P], color=NEG, lw=1.3)
    arrow(ax, (2.6, 0.7 + (P[1] - 0.7) * 2.6 / 3.6), (2.75, 0.7 + (P[1] - 0.7) * 2.75 / 3.6), NEG, lw=1.3)
    ax.text(1.9, 1.35, r"$\vec r$", color=NEG, fontsize=11)
    ax.add_patch(Arc((0, 0.7), 0.9, 0.9, theta1=np.degrees(np.arctan2(P[1] - 0.7, P[0])), theta2=90, color=INK))
    ax.text(0.28, 1.25, "θ", fontsize=11)
    dot(ax, P, r=0.17, color=ACC, out=False)
    ax.text(P[0] + 0.25, P[1] + 0.05, r"P: $d\vec B$ into the page", fontsize=9, color=ACC, va="center")
    wire(ax, [(0, 2.4), (0, 2.6)], color=GREY, lw=1, ls="--")
    ax.text(0.15, 2.45, "dB = 0 along the line of dl", fontsize=8, color=GREY)
    ax.text(2.4, -0.9, r"$d\vec B=\dfrac{\mu_0}{4\pi}\dfrac{I\,d\vec l\times\vec r}{r^3}$", fontsize=12, ha="center")
    save(fig, "phy_ch04_fig04_biot.png")


# ---- Fig 4.5: field on the axis of a circular loop ---------------------------------------------
def fig_loop_axis():
    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    blank(ax, (-1.4, 6.4), (-2.2, 2.4))
    ax.add_patch(Ellipse((0, 0), 0.9, 3.2, fill=False, color=INK, lw=1.8))
    wire(ax, [(-1.2, 0), (6.2, 0)], color=GREY, lw=1, ls="--")
    ax.text(6.2, -0.25, "x (axis)", fontsize=9, color=GREY, ha="right")
    O, P, top, bot = np.array([0, 0]), np.array([3.6, 0]), np.array([0, 1.6]), np.array([0, -1.6])
    node = lambda p, l, dx, dy: (ax.plot(*p, "o", color=INK, ms=4), ax.text(p[0] + dx, p[1] + dy, l, fontsize=10, style="italic"))
    node(O, "O", -0.3, -0.3)
    node(P, "P", 0.05, -0.32)
    ax.annotate("", (0.05, -0.55), (3.6, -0.55), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
    ax.text(1.8, -0.8, "x", fontsize=10, style="italic", ha="center")
    wire(ax, [O, top], color=GREY, lw=1)
    ax.text(-0.35, 0.8, "R", fontsize=10, style="italic")
    arrow(ax, top + (0.1, -0.02), top + (-0.25, 0.03), POS, lw=2.2)
    ax.text(-0.75, 1.75, r"$d\vec l$", color=POS, fontsize=11)
    wire(ax, [top, P], color=NEG, lw=1.2)
    ax.text(0.9, 1.45, r"$r=\sqrt{x^2+R^2}$", color=NEG, fontsize=9.5)
    u = (P - top) / np.hypot(*(P - top))
    n = np.array([u[1], -u[0]])
    n = -n if n[1] < 0 else n
    dB = 1.4 * np.array([n[0], n[1]])
    if dB[0] < 0:
        dB = -dB
    arrow(ax, P, P + dB, ACC, lw=2)
    ax.text(*(P + dB + (0.1, 0.05)), r"$d\vec B$", color=ACC, fontsize=11)
    arrow(ax, P, P + (dB[0], 0), ACC, lw=1.4)
    ax.text(P[0] + dB[0] + 0.05, -0.28, r"$dB_x$", color=ACC, fontsize=10)
    arrow(ax, P, P + (0, dB[1]), ACC, lw=1.4)
    ax.text(P[0] - 0.62, dB[1] * 0.55, r"$dB_\perp$", color=ACC, fontsize=10)
    wire(ax, [P, P + (dB[0], -dB[1])], color=ACC, lw=1, ls="--")
    ax.text(P[0] + 0.2, -dB[1] - 0.15, r"$dB_\perp$ of the opposite element cancels", fontsize=8.5, color=GREY)
    ax.text(2.8, 2.15, r"$B=\dfrac{\mu_0 I R^2}{2(x^2+R^2)^{3/2}}$", fontsize=12, ha="center")
    save(fig, "phy_ch04_fig05_loop_axis.png")


# ---- Fig 4.6: field lines of a current loop ----------------------------------------------------
def fig_loop_lines():
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    x = np.linspace(-3, 3, 300)
    y = np.linspace(-2.4, 2.4, 240)
    X, Y = np.meshgrid(x, y)
    Bx, By = wires_field(X, Y, [(0, 1.0, 1), (0, -1.0, -1)])
    ax.streamplot(X, Y, Bx, By, color=NEG, density=1.1, linewidth=0.9, arrowsize=0.9)
    dot(ax, (0, 1.0), r=0.17, color=POS, out=True)
    dot(ax, (0, -1.0), r=0.17, color=POS, out=False)
    ax.add_patch(Ellipse((0, 0), 0.5, 2.0, fill=False, color=POS, lw=1.2, ls="--"))
    ax.text(1.0, 1.95, "N face", fontsize=10, color=POS, fontweight="bold", bbox=dict(fc="white", ec="none", alpha=0.85))
    ax.text(-1.95, 1.95, "S face", fontsize=10, color=NEG, fontweight="bold", bbox=dict(fc="white", ec="none", alpha=0.85))
    ax.set_title("A current loop seen edge-on: the axial field runs from the S face to the N face", fontsize=9)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2.4, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "phy_ch04_fig06_loop_lines.png")


# ---- Fig 4.7: Ampere's law for a long wire -----------------------------------------------------
def fig_ampere():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.4))
    ax = axes[0]
    blank(ax, (-2.0, 2.0), (-1.9, 1.9))
    dot(ax, (0, 0), r=0.2, color=POS, out=True)
    ax.add_patch(Circle((0, 0), 1.3, fill=False, color=GREEN, lw=1.6, ls="--"))
    for ang in (30, 150, 270):
        t = np.radians(ang)
        p = 1.3 * np.array([np.cos(t), np.sin(t)])
        u = np.array([-np.sin(t), np.cos(t)])
        arrow(ax, p, p + 0.55 * u, ACC, lw=1.8)
    ax.text(1.05, 1.15, r"$\vec B$", color=ACC, fontsize=11)
    wire(ax, [(0, 0), (1.3 * np.cos(np.radians(-30)), 1.3 * np.sin(np.radians(-30)))], color=GREY, lw=1)
    ax.text(0.55, -0.55, "r", fontsize=11, style="italic")
    ax.text(0, -1.85, r"$B\cdot 2\pi r=\mu_0 I \Rightarrow B=\dfrac{\mu_0 I}{2\pi r}$", ha="center", fontsize=10.5)
    ax.set_title("(a) A circular Amperian loop", fontsize=10)
    ax = axes[1]
    a = 1.0
    r = np.linspace(0, 4, 300)
    B = np.where(r < a, r / a, a / np.maximum(r, 1e-9))
    ax.plot(r, B, color=NEG, lw=2)
    ax.axvline(a, color=GREY, ls=":", lw=1)
    ax.set_xticks([0, a])
    ax.set_xticklabels(["0", "a"])
    ax.set_yticks([1])
    ax.set_yticklabels([r"$\dfrac{\mu_0 I}{2\pi a}$"])
    ax.set_xlabel("distance r from the axis", fontsize=9)
    ax.set_ylabel("B", fontsize=9, rotation=0, labelpad=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.15, 0.6, r"inside: $B\propto r$", fontsize=9)
    ax.text(2.0, 0.6, r"outside: $B\propto 1/r$", fontsize=9)
    ax.set_title("(b) A thick wire of radius a (NCERT Ex. 4.7)", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch04_fig07_ampere.png")


# ---- Fig 4.8: the solenoid ---------------------------------------------------------------------
def fig_solenoid():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.6))
    ax = axes[0]
    blank(ax, (-0.4, 6.4), (-1.6, 1.8))
    xs = np.arange(0.3, 6.0, 0.4)
    for x in xs:
        dot(ax, (x, 0.9), r=0.13, color=POS, out=True)
        dot(ax, (x, -0.9), r=0.13, color=POS, out=False)
    for y in (-0.45, 0, 0.45):
        arrow(ax, (0.3, y), (5.9, y), NEG, lw=1.1, ms=9)
    ax.add_patch(Rectangle((1.8, -0.25), 2.2, 1.65, fill=False, ec=GREEN, lw=1.6, ls="--"))
    for (x, y, l) in ((1.6, -0.35, "a"), (4.15, -0.35, "b"), (4.15, 1.5, "c"), (1.6, 1.5, "d")):
        ax.text(x, y, l, fontsize=10, color=GREEN, style="italic")
    ax.annotate("", (1.8, -0.5), (4.0, -0.5), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
    ax.text(2.9, -0.75, "h", fontsize=10, style="italic", ha="center")
    ax.text(3.1, -1.45, r"$Bh=\mu_0 (nh) I \Rightarrow B=\mu_0 n I$", ha="center", fontsize=10.5)
    ax.text(6.2, 1.35, "B ≈ 0\noutside", fontsize=8.5, color=GREY, ha="right")
    ax.set_title("(a) A long solenoid and the loop abcd", fontsize=10)
    ax = axes[1]
    x = np.linspace(-4, 4, 360)
    y = np.linspace(-2.5, 2.5, 240)
    X, Y = np.meshgrid(x, y)
    w = [(xx, 0.7, 1) for xx in np.linspace(-1.8, 1.8, 13)] + [(xx, -0.7, -1) for xx in np.linspace(-1.8, 1.8, 13)]
    Bx, By = wires_field(X, Y, w)
    ax.streamplot(X, Y, Bx, By, color=NEG, density=1.2, linewidth=0.8, arrowsize=0.8)
    for xx, yy, I in w:
        ax.add_patch(Circle((xx, yy), 0.09, color=POS, zorder=5))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(b) Finite solenoid: uniform, strong field inside", fontsize=10)
    save(fig, "phy_ch04_fig08_solenoid.png")


# ---- Fig 4.9: force between parallel currents --------------------------------------------------
def fig_parallel():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.6))
    for k, ax in enumerate(axes):
        blank(ax, (-1.2, 3.4), (-1.6, 1.9))
        same = k == 0
        wire(ax, [(0, -1.4), (0, 1.5)], color=INK, lw=2.2)
        wire(ax, [(2.2, -1.4), (2.2, 1.5)], color=INK, lw=2.2)
        arrow(ax, (0, 0.6), (0, 1.2), POS, lw=2.2)
        if same:
            arrow(ax, (2.2, 0.6), (2.2, 1.2), POS, lw=2.2)
        else:
            arrow(ax, (2.2, 1.2), (2.2, 0.6), POS, lw=2.2)
        ax.text(-0.35, 1.0, r"$I_a$", color=POS, fontsize=11)
        ax.text(2.4, 1.0, r"$I_b$", color=POS, fontsize=11)
        dot(ax, (2.2, -0.35), r=0.15, color=ACC, out=False)
        ax.text(2.45, -0.35, r"$B_a$", color=ACC, fontsize=10, va="center")
        if same:
            arrow(ax, (2.2, -0.9), (1.4, -0.9), GREEN, lw=2)
            arrow(ax, (0, -0.9), (0.8, -0.9), GREEN, lw=2)
            ax.set_title("(a) Same direction: attract", fontsize=10)
        else:
            arrow(ax, (2.2, -0.9), (3.0, -0.9), GREEN, lw=2)
            arrow(ax, (0, -0.9), (-0.8, -0.9), GREEN, lw=2)
            ax.set_title("(b) Opposite directions: repel", fontsize=10)
        ax.annotate("", (0, 1.7), (2.2, 1.7), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
        ax.text(1.1, 1.82, "d", fontsize=10, style="italic", ha="center")
        ax.text(1.1, -1.55, r"$\dfrac{F}{L}=\dfrac{\mu_0 I_a I_b}{2\pi d}$", ha="center", fontsize=10.5)
    save(fig, "phy_ch04_fig09_parallel.png")


# ---- Fig 4.10: torque on a rectangular loop ----------------------------------------------------
def fig_torque():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.8), gridspec_kw={"width_ratios": [1.1, 1]})
    ax = axes[0]
    blank(ax, (-1.0, 5.1), (-1.4, 2.7))
    A, B, C, D = (0.5, 2.0), (3.5, 2.0), (3.5, 0.0), (0.5, 0.0)
    A, B, C, D = (0.5, 0.0), (0.5, 2.0), (3.5, 2.0), (3.5, 0.0)
    wire(ax, [A, B, C, D, A], color=INK, lw=2)
    for p, l, dx, dy in ((A, "A", -0.3, -0.2), (B, "B", -0.3, 0.15), (C, "C", 0.15, 0.15), (D, "D", 0.15, -0.2)):
        ax.text(p[0] + dx, p[1] + dy, l, fontsize=10, style="italic")
    carrow(ax, (0.5, 1.0), (0, 1), None)
    carrow(ax, (2.0, 2.0), (1, 0), None)
    carrow(ax, (3.5, 1.0), (0, -1), None)
    carrow(ax, (2.0, 0.0), (-1, 0), None)
    ax.text(2.0, 1.0, "I", color=POS, fontsize=12, ha="center", style="italic")
    for y in (-0.9, 2.5):
        arrow(ax, (-0.8, y), (4.6, y), ACC, lw=1.2, ms=10)
    ax.text(4.7, 2.5, r"$\vec B$", color=ACC, fontsize=11, ha="left", va="center")
    dot(ax, (0.0, 1.0), r=0.17, color=GREEN, out=False)
    ax.text(-0.75, 1.0, r"$F_1$", color=GREEN, fontsize=10, va="center")
    dot(ax, (4.0, 1.0), r=0.17, color=GREEN, out=True)
    ax.text(4.25, 1.0, r"$F_2$", color=GREEN, fontsize=10, va="center")
    ax.text(2.0, -0.5, "a", fontsize=10, style="italic", ha="center")
    ax.text(0.2, 1.4, "b", fontsize=10, style="italic")
    ax.text(2.0, -1.3, "no force on BC and DA (parallel to B)", fontsize=8.5, color=GREY, ha="center")
    ax.set_title(r"(a) $\vec B$ in the plane of the loop: $\tau = IAB$", fontsize=10)
    ax = axes[1]
    blank(ax, (-2.4, 2.6), (-2.0, 2.2))
    th = np.radians(55)
    u = np.array([np.cos(np.pi / 2 - th), np.sin(np.pi / 2 - th)])
    u = np.array([np.sin(th), np.cos(th)])
    half = 1.2
    p1, p2 = -half * u, half * u
    wire(ax, [p1, p2], color=INK, lw=3)
    dot(ax, p2, r=0.16, color=POS, out=True)
    dot(ax, p1, r=0.16, color=POS, out=False)
    nrm = np.array([u[1], -u[0]])
    arrow(ax, (0, 0), 1.4 * nrm, NEG, lw=2)
    ax.text(*(1.5 * nrm + (0.05, -0.15)), r"$\vec m$", color=NEG, fontsize=11)
    arrow(ax, (-2.2, -1.75), (2.4, -1.75), ACC, lw=1.4)
    ax.text(2.4, -1.55, r"$\vec B$", color=ACC, fontsize=11, ha="right")
    wire(ax, [(0, 0), (1.8, 0)], color=GREY, lw=1, ls="--")
    ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=np.degrees(np.arctan2(nrm[1], nrm[0])), theta2=0, color=INK))
    ax.text(0.7, -0.38, "θ", fontsize=11)
    arrow(ax, p2, p2 + (0, 0.8), GREEN, lw=2)
    ax.text(p2[0] + 0.12, p2[1] + 0.7, r"$F_2$", color=GREEN, fontsize=10)
    arrow(ax, p1, p1 + (0, -0.8), GREEN, lw=2)
    ax.text(p1[0] - 0.45, p1[1] - 0.7, r"$F_1$", color=GREEN, fontsize=10)
    ax.text(-2.3, 1.9, r"$\tau = IAB\sin\theta,\ \ \vec\tau=\vec m\times\vec B$", fontsize=10.5)
    ax.set_title("(b) Top view: plane of the loop at an angle", fontsize=10)
    save(fig, "phy_ch04_fig10_torque.png")


# ---- Fig 4.11: the moving coil galvanometer ----------------------------------------------------
def fig_mcg():
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    blank(ax, (-3.6, 3.6), (-3.1, 3.0))
    ax.add_patch(Wedge((0, 0), 2.4, 115, 245, width=1.0, color="#C9D3DD", ec=INK, lw=1.2))
    ax.add_patch(Wedge((0, 0), 2.4, -65, 65, width=1.0, color="#C9D3DD", ec=INK, lw=1.2))
    ax.text(-1.9, 0, "N", fontsize=14, fontweight="bold", color=POS, ha="center", va="center")
    ax.text(1.9, 0, "S", fontsize=14, fontweight="bold", color=NEG, ha="center", va="center")
    ax.add_patch(Circle((0, 0), 0.75, color="#9AA7B4", ec=INK, lw=1.2))
    ax.text(0, 0, "soft\niron\ncore", fontsize=7.5, ha="center", va="center")
    for ang in list(range(120, 245, 20)) + list(range(-60, 65, 20)):
        t = np.radians(ang)
        d = np.array([np.cos(t), np.sin(t)])
        if np.cos(t) < 0:
            arrow(ax, 1.38 * d, 0.8 * d, ACC, lw=1, ms=8)
        else:
            arrow(ax, 0.8 * d, 1.38 * d, ACC, lw=1, ms=8)
    for t, out in ((np.radians(150), True), (np.radians(-30), False)):
        p = 1.05 * np.array([np.cos(t), np.sin(t)])
        dot(ax, p, r=0.14, color=POS, out=out)
    wire(ax, [1.05 * np.array([np.cos(np.radians(150)), np.sin(np.radians(150))]), 1.05 * np.array([np.cos(np.radians(-30)), np.sin(np.radians(-30))])], color=POS, lw=1, ls=":")
    ax.text(0, 2.75, "concave pole pieces + soft iron core give a radial field", fontsize=9, ha="center", va="top")
    ax.text(0, -2.35, r"$NIAB = k\phi \Rightarrow \phi = \left(\dfrac{NAB}{k}\right)I$", fontsize=11, ha="center", va="top")
    save(fig, "phy_ch04_fig11_mcg.png")


# ---- Fig 4.12: ammeter and voltmeter -----------------------------------------------------------
def fig_convert():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 2.8))
    ax = axes[0]
    blank(ax, (-0.5, 4.5), (-1.3, 1.6))
    wire(ax, [(-0.3, 0.3), (0.8, 0.3)])
    wire(ax, [(0.8, 1.0), (0.8, -0.4)])
    galv(ax, (0.8, 1.0), (3.2, 1.0), label="G")
    res(ax, (0.8, -0.4), (3.2, -0.4), r"shunt $S$ (small)", side=-1, L=0.8)
    wire(ax, [(3.2, 1.0), (3.2, -0.4)])
    wire(ax, [(3.2, 0.3), (4.3, 0.3)])
    carrow(ax, (0.2, 0.3), (1, 0), "I", off=(0, 0.25))
    carrow(ax, (1.5, 1.0), (1, 0), r"$I_g$", off=(0, 0.28))
    carrow(ax, (1.3, -0.4), (1, 0), r"$I-I_g$", off=(0, 0.3))
    ax.text(2.0, 1.5, r"$I_gG=(I-I_g)S \Rightarrow S=\dfrac{I_gG}{I-I_g}$", ha="center", fontsize=10)
    ax.set_title("(a) Ammeter: small shunt in parallel", fontsize=10, pad=18)
    ax = axes[1]
    blank(ax, (-0.5, 4.5), (-1.3, 1.6))
    wire(ax, [(-0.3, 0.3), (0.4, 0.3)])
    galv(ax, (0.4, 0.3), (1.8, 0.3), label="G")
    res(ax, (1.8, 0.3), (4.0, 0.3), r"$R$ (large)", side=-1, L=1.0)
    wire(ax, [(4.0, 0.3), (4.3, 0.3)])
    ax.annotate("", (-0.3, -0.6), (4.3, -0.6), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
    ax.text(2.0, -0.85, "V across the voltmeter", fontsize=9, ha="center", color=GREY)
    ax.text(2.0, 1.25, r"$V=I_g(G+R) \Rightarrow R=\dfrac{V}{I_g}-G$", ha="center", fontsize=10)
    ax.set_title("(b) Voltmeter: large resistance in series", fontsize=10, pad=18)
    save(fig, "phy_ch04_fig12_convert.png")


# ---- Fig 4.13: board figures ------------------------------------------------------------------
def fig_board():
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.6))
    ax = axes[0]
    blank(ax, (-2.0, 1.9), (-2.3, 1.9))
    ax.add_patch(Circle((0, 0), 1.3, fill=False, color=NEG, lw=1.6, ls="--"))
    ax.add_patch(Circle((0, 0), 0.12, color=POS))
    ax.text(0.18, -0.25, "+e", fontsize=9, color=POS)
    p = np.array([0, 1.3])
    ax.add_patch(Circle(p, 0.14, color=NEG, zorder=5))
    ax.text(0, 1.55, "−e", fontsize=9, color=NEG, ha="center")
    arrow(ax, p + (0.15, 0), p + (0.8, 0), NEG, lw=1.6)
    ax.text(0.9, 1.4, "v", fontsize=10, color=NEG, style="italic")
    wire(ax, [(0, 0), (1.3 * np.cos(np.radians(-40)), 1.3 * np.sin(np.radians(-40)))], color=GREY, lw=1)
    ax.text(0.55, -0.62, "r", fontsize=10, style="italic")
    ax.annotate("", (-1.15, -0.6), (-0.6, -1.15), arrowprops=dict(arrowstyle="->", color=POS, lw=1.4, connectionstyle="arc3,rad=-0.3"))
    ax.text(-1.9, -1.55, "current I\n(opposite to e⁻)", fontsize=8, color=POS)
    ax.text(0.3, -2.05, r"$\mu = IA = \dfrac{e v}{2\pi r}\pi r^2 = \dfrac{evr}{2}$", ha="center", fontsize=10)
    ax.set_title("(a) A revolving electron", fontsize=10)
    ax = axes[1]
    blank(ax, (-2.2, 2.2), (-0.7, 2.4))
    R1, R2 = 1.0, 1.7
    th = np.linspace(0, np.pi, 100)
    wire(ax, list(zip(R2 * np.cos(th), R2 * np.sin(th))), color=INK, lw=1.8)
    wire(ax, list(zip(R1 * np.cos(th), R1 * np.sin(th))), color=INK, lw=1.8)
    wire(ax, [(R1, 0), (R2, 0)], color=INK, lw=1.8)
    wire(ax, [(-R1, 0), (-R2, 0)], color=INK, lw=1.8)
    carrow(ax, (0, R2), (1, 0), None)
    carrow(ax, (0, R1), (-1, 0), None)
    carrow(ax, (1.35, 0), (-1, 0), None)
    carrow(ax, (-1.35, 0), (-1, 0), None)
    for x, l in ((R2, "P"), (R1, "Q"), (-R1, "R"), (-R2, "S")):
        ax.text(x, -0.3, l, ha="center", fontsize=10, style="italic")
    ax.plot([0], [0], "o", color=INK, ms=4)
    ax.text(0, -0.3, "O", ha="center", fontsize=10, style="italic")
    wire(ax, [(0, 0), (R1 * np.cos(np.radians(60)), R1 * np.sin(np.radians(60)))], color=GREY, lw=1)
    wire(ax, [(0, 0), (R2 * np.cos(np.radians(115)), R2 * np.sin(np.radians(115)))], color=GREY, lw=1)
    ax.text(0.35, 0.35, r"$R_1$", fontsize=9)
    ax.text(-0.75, 0.85, r"$R_2$", fontsize=9)
    ax.set_title("(b) HSSLC 2019, Q21: loop PQRSP", fontsize=10)
    ax = axes[2]
    blank(ax, (-2.0, 2.0), (-1.9, 2.1))
    wire(ax, [(0, -1.6), (0, 1.6)], color=INK, lw=3)
    arrow(ax, (0, 0.6), (0, 1.3), POS, lw=2.2)
    ax.text(0.15, 1.1, "I", color=POS, fontsize=11, style="italic")
    ax.text(0, 1.85, "N", ha="center", fontsize=11, fontweight="bold")
    ax.text(0, -1.85, "S", ha="center", fontsize=11, fontweight="bold")
    ax.text(-1.9, 0, "W", ha="center", fontsize=10, color=GREY)
    ax.text(1.9, 0, "E", ha="center", fontsize=10, color=GREY)
    needle(ax, (0, -0.2), (-np.sin(np.radians(55)), np.cos(np.radians(55))), L=1.3, w=0.12)
    wire(ax, [(0.25, -0.85), (0.25, 0.45)], color=GREY, lw=1, ls="--")
    ax.text(0.32, 0.5, "before", fontsize=7.5, color=GREY)
    arrow(ax, (-0.25, 0.45), (-0.8, 0.25), GREEN, lw=1.4)
    ax.text(-1.0, 0.65, "N end turns\nwest (left)", fontsize=8.5, color=GREEN, ha="center")
    ax.text(0.95, -1.2, "needle below\nthe wire", fontsize=8.5, color=GREY, ha="center")
    ax.set_title("(c) HSSLC 2026, Q9: compass under a wire", fontsize=10)
    save(fig, "phy_ch04_fig13_board.png")


if __name__ == "__main__":
    fig_oersted()
    fig_lorentz()
    fig_motion()
    fig_biot()
    fig_loop_axis()
    fig_loop_lines()
    fig_ampere()
    fig_solenoid()
    fig_parallel()
    fig_torque()
    fig_mcg()
    fig_convert()
    fig_board()
