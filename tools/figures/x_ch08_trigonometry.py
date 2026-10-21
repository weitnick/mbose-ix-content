"""Figures for Class X Mathematics, Chapter 8: Introduction to Trigonometry.
Run: python x_ch08_trigonometry.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Polygon

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def P(*xy):
    return np.array(xy, dtype=float)


def right(ax, at, p, q, s=0.25):
    u = (p - at) / np.linalg.norm(p - at) * s
    v = (q - at) / np.linalg.norm(q - at) * s
    ax.plot(*zip(at + u, at + u + v, at + v), color=INK, lw=0.9)


def angle(ax, at, p, q, r=0.5, text=None, tr=None, color=HI, size=10):
    a1 = np.degrees(np.arctan2(*(p - at)[::-1]))
    a2 = np.degrees(np.arctan2(*(q - at)[::-1]))
    if (a2 - a1) % 360 > 180:
        a1, a2 = a2, a1
    ax.add_patch(Arc(at, 2 * r, 2 * r, theta1=a1, theta2=a2, color=color, lw=1.1))
    if text:
        mid = np.radians(a1 + ((a2 - a1) % 360) / 2)
        rr = tr or r + 0.3
        ax.text(at[0] + rr * np.cos(mid), at[1] + rr * np.sin(mid), text, ha="center", va="center", fontsize=size, color=color)


def tri(ax, pts, fc=SOFT):
    ax.add_patch(Polygon(np.array(pts), closed=True, fc=fc, ec=INK, lw=1.3))


def lab(ax, p, s, off, size=11):
    ax.annotate(s, p, textcoords="offset points", xytext=off, ha="center", va="center", fontsize=size, color=INK)


def side(ax, a, b, s, off, size=9.5, color=ACC, rot=False):
    m = (a + b) / 2 + np.array(off)
    kw = {}
    if rot:
        d = b - a
        kw["rotation"] = np.degrees(np.arctan2(d[1], d[0]))
        kw["rotation_mode"] = "anchor"
    ax.text(*m, s, ha="center", va="center", fontsize=size, color=color, **kw)


def finish(ax):
    ax.set_aspect("equal")
    ax.axis("off")
    ax.margins(0.12)


# Fig 8.1: the sides of a right triangle named with respect to angle A, and then angle C
def fig_sides():
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 2.8))
    A, B, C = P(0, 0), P(4, 0), P(4, 2.8)
    for ax, ang in zip(axs, "AC"):
        tri(ax, [A, B, C])
        right(ax, B, A, C)
        lab(ax, A, "A", (-9, -6)); lab(ax, B, "B", (8, -7)); lab(ax, C, "C", (8, 6))
        side(ax, A, C, "hypotenuse", (-0.35, 0.45), rot=True)
        if ang == "A":
            angle(ax, A, B, C, 0.6)
            side(ax, A, B, "side adjacent to $\\angle$A", (0, -0.38))
            side(ax, B, C, "side opposite\nto $\\angle$A", (0.95, 0))
        else:
            angle(ax, C, A, B, 0.5)
            side(ax, A, B, "side opposite to $\\angle$C", (0, -0.38))
            side(ax, B, C, "side adjacent\nto $\\angle$C", (0.95, 0))
        finish(ax)
    save(fig, "ch08_fig01_naming_sides.png")


# Fig 8.2: the ratios of angle A do not depend on the size of the triangle
def fig_similar():
    fig, ax = plt.subplots(figsize=(4.8, 2.8))
    A = P(0, 0)
    t = np.radians(32)
    for k, (base, nm, top) in enumerate([(2.2, "M", "P"), (3.6, "B", "C"), (5.0, "N", "Q")]):
        foot_, apex = P(base, 0), P(base, base * np.tan(t))
        ax.plot(*zip(foot_, apex), color=[HI, INK, ACC][k], lw=1.3)
        right(ax, foot_, A, apex, 0.18)
        lab(ax, foot_, nm, (0, -11)); lab(ax, apex, top, (-8, 9))
    ax.plot([0, 5.4], [0, 0], color=INK, lw=1.3)
    end = P(5.4, 5.4 * np.tan(t))
    ax.plot(*zip(A, end), color=INK, lw=1.3)
    angle(ax, A, P(1, 0), end, 0.7, "A", tr=1.05)
    lab(ax, A, "", (0, 0))
    finish(ax)
    save(fig, "ch08_fig02_ratios_same.png")


# Fig 8.3: right isosceles triangle (45 degrees) and half of an equilateral triangle (30 and 60 degrees)
def fig_special():
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 3.2), gridspec_kw={"width_ratios": [1, 1.1]})
    ax = axs[0]
    A, B, C = P(0, 0), P(3, 0), P(3, 3)
    tri(ax, [A, B, C])
    right(ax, B, A, C)
    angle(ax, A, B, C, 0.6, "45°", tr=0.95, size=9)
    angle(ax, C, A, B, 0.5, "45°", tr=0.85, size=9)
    lab(ax, A, "A", (-9, -6)); lab(ax, B, "B", (8, -7)); lab(ax, C, "C", (8, 6))
    side(ax, A, B, "$a$", (0, -0.3)); side(ax, B, C, "$a$", (0.3, 0)); side(ax, A, C, r"$a\sqrt{2}$", (-0.4, 0.35))
    finish(ax)
    ax = axs[1]
    s = 3.4
    B2, C2 = P(0, 0), P(s, 0)
    A2 = P(s / 2, s * np.sqrt(3) / 2)
    D = P(s / 2, 0)
    tri(ax, [A2, B2, C2])
    ax.plot(*zip(A2, D), color=ACC, lw=1.3)
    right(ax, D, A2, C2, 0.2)
    angle(ax, B2, C2, A2, 0.5, "60°", tr=0.85, size=9)
    angle(ax, A2, B2, D, 0.6, "30°", tr=0.95, size=9)
    lab(ax, A2, "A", (0, 9)); lab(ax, B2, "B", (-8, -7)); lab(ax, C2, "C", (8, -7)); lab(ax, D, "D", (0, -11))
    side(ax, B2, A2, "$2a$", (-0.3, 0.12)); side(ax, B2, D, "$a$", (0, -0.3)); side(ax, A2, D, r"$a\sqrt{3}$", (0.32, 0))
    finish(ax)
    save(fig, "ch08_fig03_special_angles.png")


# Fig 8.4: Example 5 - triangle OPQ right-angled at P, OP = 7 cm, OQ - PQ = 1 cm
def fig_example5():
    fig, ax = plt.subplots(figsize=(4.2, 2.0))
    s = 0.16
    Pp, Q, O = P(0, 0), P(24 * s, 0), P(0, 7 * s)
    tri(ax, [O, Pp, Q])
    right(ax, Pp, O, Q, 0.18)
    lab(ax, O, "O", (-7, 6)); lab(ax, Pp, "P", (-7, -7)); lab(ax, Q, "Q", (8, -6))
    side(ax, O, Pp, "7 cm", (-0.38, 0))
    side(ax, Pp, Q, "PQ", (0, -0.2))
    side(ax, O, Q, "OQ = PQ + 1", (0.15, 0.25), rot=True)
    finish(ax)
    save(fig, "ch08_fig04_example5.png")


# Fig 8.5: Ex 8.1 Q2 - triangle PQR right-angled at Q, PQ = 12 cm, PR = 13 cm
def fig_ex81_q2():
    fig, ax = plt.subplots(figsize=(2.8, 3.2))
    s = 0.22
    Q, Pp, R = P(0, 0), P(0, 12 * s), P(5 * s, 0)
    tri(ax, [Pp, Q, R])
    right(ax, Q, Pp, R, 0.18)
    lab(ax, Pp, "P", (-6, 7)); lab(ax, Q, "Q", (-7, -7)); lab(ax, R, "R", (8, -6))
    side(ax, Pp, Q, "12 cm", (-0.4, 0))
    side(ax, Pp, R, "13 cm", (0.4, 0.15))
    finish(ax)
    save(fig, "ch08_fig05_ex81_q2.png")


# Fig 8.6: Example 6 - triangle ABC right-angled at B, AB = 5 cm, angle C = 30 degrees
def fig_example6():
    fig, ax = plt.subplots(figsize=(4.0, 2.4))
    s = 0.42
    B, A, C = P(0, 0), P(0, 5 * s), P(5 * np.sqrt(3) * s, 0)
    tri(ax, [A, B, C])
    right(ax, B, A, C, 0.2)
    angle(ax, C, A, B, 0.7, "30°", tr=1.1, size=9)
    lab(ax, A, "A", (-6, 7)); lab(ax, B, "B", (-7, -7)); lab(ax, C, "C", (8, -6))
    side(ax, A, B, "5 cm", (-0.4, 0))
    finish(ax)
    save(fig, "ch08_fig06_example6.png")


# Fig 8.7: sin A rises from 0 to 1 and cos A falls from 1 to 0 as A goes from 0 to 90 degrees
def fig_graph():
    fig, ax = plt.subplots(figsize=(4.6, 2.6))
    a = np.linspace(0, 90, 200)
    ax.plot(a, np.sin(np.radians(a)), color=ACC, lw=1.8, label="sin A")
    ax.plot(a, np.cos(np.radians(a)), color=HI, lw=1.8, label="cos A")
    for v in (0, 30, 45, 60, 90):
        ax.axvline(v, color="#DDE3EA", lw=0.8, zorder=0)
    ax.set_xticks([0, 30, 45, 60, 90])
    ax.set_xticklabels(["0°", "30°", "45°", "60°", "90°"])
    ax.set_yticks([0, 0.5, 1])
    ax.set_xlim(0, 90); ax.set_ylim(0, 1.08)
    ax.legend(frameon=False, loc="center right")
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
    ax.set_xlabel("angle A")
    save(fig, "ch08_fig07_sin_cos_graph.png")


if __name__ == "__main__":
    fig_sides()
    fig_similar()
    fig_special()
    fig_example5()
    fig_ex81_q2()
    fig_example6()
    fig_graph()
