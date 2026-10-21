"""Figures for Class X Mathematics, Chapter 9: Some Applications of Trigonometry.
Run: python x_ch09_heights_distances.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Polygon, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, GROUND = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#8C6A43"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})
R3 = np.sqrt(3)


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def P(*xy):
    return np.array(xy, dtype=float)


def new(w=4.6, h=3.0):
    fig, ax = plt.subplots(figsize=(w, h))
    return fig, ax


def ground(ax, x0, x1, y=0.0):
    ax.plot([x0, x1], [y, y], color=GROUND, lw=1.6)
    for x in np.arange(x0, x1, (x1 - x0) / 28):
        ax.plot([x, x - 0.012 * (x1 - x0)], [y, y - 0.02 * (x1 - x0)], color=GROUND, lw=0.6)


def seg(ax, a, b, color=INK, lw=1.4, ls="-"):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls=ls, solid_capstyle="round")


def sight(ax, a, b):
    seg(ax, a, b, HI, 1.1, "--")


def right(ax, at, p, q, s=None):
    s = s or 0.04 * max(ax.get_xlim()[1] - ax.get_xlim()[0], 1)
    u = (p - at) / np.linalg.norm(p - at) * s
    v = (q - at) / np.linalg.norm(q - at) * s
    ax.plot(*zip(at + u, at + u + v, at + v), color=INK, lw=0.8)


def angle(ax, at, p, q, r, text, tr=None, size=9):
    a1 = np.degrees(np.arctan2(*(p - at)[::-1]))
    a2 = np.degrees(np.arctan2(*(q - at)[::-1]))
    if (a2 - a1) % 360 > 180:
        a1, a2 = a2, a1
    ax.add_patch(Arc(at, 2 * r, 2 * r, theta1=a1, theta2=a2, color=HI, lw=1.1))
    mid = np.radians(a1 + ((a2 - a1) % 360) / 2)
    rr = tr or r * 1.55
    ax.text(at[0] + rr * np.cos(mid), at[1] + rr * np.sin(mid), text, ha="center", va="center", fontsize=size, color=HI)


def lab(ax, p, s, off, size=10.5):
    ax.annotate(s, p, textcoords="offset points", xytext=off, ha="center", va="center", fontsize=size, color=INK)


def dim(ax, a, b, s, off=(0, 0), size=9, color=ACC, rot=0):
    m = (np.array(a) + np.array(b)) / 2 + np.array(off)
    ax.text(*m, s, ha="center", va="center", fontsize=size, color=color, rotation=rot)


def person(ax, x, h, color=ACC):
    """A simple standing figure of height h with its eye at (x, h)."""
    seg(ax, P(x, 0), P(x, h * 0.55), color, 1.4)
    seg(ax, P(x, h * 0.55), P(x - h * 0.12, 0), color, 1.2)
    ax.add_patch(plt.Circle((x, h * 0.88), h * 0.1, fc="white", ec=color, lw=1.2))


def tower(ax, x, h, w, fc=SOFT):
    ax.add_patch(Rectangle((x - w / 2, 0), w, h, fc=fc, ec=INK, lw=1.2))


def finish(ax, xl, yl):
    ax.set_xlim(*xl); ax.set_ylim(*yl)
    ax.set_aspect("equal"); ax.axis("off")


# Fig 9.1: line of sight and angle of elevation
def fig_elevation():
    fig, ax = new(4.6, 2.8)
    ground(ax, -0.5, 9)
    tower(ax, 7.5, 5.5, 1.0)
    person(ax, 1, 1.5)
    E, T, H = P(1, 1.5), P(7.5, 5.5), P(7.0, 1.5)
    sight(ax, E, T)
    seg(ax, E, H, GREY, 0.9, ":")
    angle(ax, E, H, T, 1.1, "angle of\nelevation", tr=2.3, size=8)
    dim(ax, E, T, "line of sight", (-0.5, 0.55), rot=np.degrees(np.arctan2(4, 6.5)), color=HI)
    ax.text(4.0, 1.15, "horizontal", fontsize=8, color=GREY, ha="center")
    finish(ax, (-0.6, 9.2), (-0.5, 6.2))
    save(fig, "ch09_fig01_elevation.png")


# Fig 9.2: angle of depression
def fig_depression():
    fig, ax = new(4.6, 2.8)
    ground(ax, -0.5, 9)
    ax.add_patch(Rectangle((0, 0), 1.6, 4.6, fc=SOFT, ec=INK, lw=1.2))
    E, F, H = P(1.3, 4.6), P(7.5, 0.25), P(7.0, 4.6)
    person(ax, 1.3, 0.0001)
    ax.add_patch(plt.Circle((1.3, 4.75), 0.15, fc="white", ec=ACC, lw=1.2))
    ax.add_patch(Rectangle((7.3, 0), 0.5, 0.5, fc="#D9B38C", ec=INK, lw=0.9))
    sight(ax, E, F)
    seg(ax, E, H, GREY, 0.9, ":")
    angle(ax, E, H, F, 1.4, "angle of\ndepression", tr=2.5, size=8)
    ax.text(4.2, 4.8, "horizontal", fontsize=8, color=GREY, ha="center")
    dim(ax, E, F, "line of sight", (1.2, 0.2), rot=-np.degrees(np.arctan2(4.35, 6.2)), color=HI)
    finish(ax, (-0.6, 9.2), (-0.5, 5.6))
    save(fig, "ch09_fig02_depression.png")


def basic(ax, base, h, ang_text, labels=("A", "B", "C"), hlabel=None, blabel=None, xl=None, yl=None, w=0.5):
    """Right triangle: tower AB of height h at x = base, observer C at the origin."""
    A, B, C = P(base, h), P(base, 0), P(0, 0)
    tower(ax, base, h, w)
    sight(ax, C, A)
    right(ax, B, A, C)
    angle(ax, C, B, A, 0.18 * base, ang_text)
    lab(ax, A, labels[0], (8, 6)); lab(ax, B, labels[1], (8, -9)); lab(ax, C, labels[2], (-8, -8))
    if hlabel:
        dim(ax, A, B, hlabel, (0.55 * w + 0.12 * base, 0))
    if blabel:
        dim(ax, B, C, blabel, (0, -0.07 * base - 0.2))
    return A, B, C


# Fig 9.3: Example 1 - tower, 15 m away, 60 degrees
def fig_example1():
    fig, ax = new(3.4, 3.4)
    ground(ax, -0.6, 7)
    basic(ax, 5, 5 * R3, "60°", hlabel="h", blabel="15 m", w=0.6)
    finish(ax, (-1, 7.6), (-1.2, 9.4))
    save(fig, "ch09_fig03_example1.png")


# Fig 9.4: Example 2 - electrician's ladder at 60 degrees reaching 1.3 m below the top of a 5 m pole
def fig_example2():
    fig, ax = new(3.0, 3.4)
    ground(ax, -0.4, 4)
    D, A = P(3, 0), P(3, 5)
    B = P(3, 3.7)
    C = P(3 - 3.7 / R3, 0)
    seg(ax, D, A, INK, 2.4)
    seg(ax, C, B, ACC, 2.0)
    right(ax, D, A, C, 0.18)
    angle(ax, C, D, B, 0.45, "60°")
    lab(ax, A, "A", (8, 4)); lab(ax, B, "B", (9, 0)); lab(ax, D, "D", (8, -9)); lab(ax, C, "C", (-7, -9))
    dim(ax, A, B, "1.3 m", (0.55, 0)); dim(ax, B, D, "3.7 m", (0.55, 0))
    dim(ax, C, B, "ladder", (-0.45, 0.25), rot=60, color=ACC)
    finish(ax, (0.2, 4.4), (-0.7, 5.6))
    save(fig, "ch09_fig04_example2.png")


# Fig 9.5: Example 3 - chimney, observer 1.5 m tall, 28.5 m away, 45 degrees
def fig_example3():
    fig, ax = new(3.8, 3.2)
    ground(ax, -0.5, 6.4)
    sc = 0.17
    A, B = P(5.5, 30 * sc), P(5.5, 0)
    D, C = P(5.5 - 28.5 * sc, 1.5 * sc), P(5.5 - 28.5 * sc, 0)
    E = P(5.5, 1.5 * sc)
    tower(ax, 5.5, 30 * sc, 0.5)
    person(ax, C[0], 1.5 * sc)
    sight(ax, D, A)
    seg(ax, D, E, GREY, 0.9, ":")
    angle(ax, D, E, A, 0.9, "45°")
    lab(ax, A, "A", (8, 6)); lab(ax, B, "B", (8, -9)); lab(ax, C, "C", (-8, -9)); lab(ax, D, "D", (-9, 4)); lab(ax, E, "E", (11, 0))
    dim(ax, C, B, "28.5 m", (0, -0.35))
    dim(ax, C, D, "1.5 m", (-0.75, -0.05), size=8)
    finish(ax, (-0.6, 6.6), (-0.8, 5.6))
    save(fig, "ch09_fig05_example3.png")


# Fig 9.6: Example 4 - building 10 m with a flagstaff; elevations 30 and 45 degrees from P
def fig_example4():
    fig, ax = new(4.2, 3.0)
    ground(ax, -0.6, 7)
    sc = 0.32
    Pp, A = P(0, 0), P(10 * R3 * sc, 0)
    B, D = P(A[0], 10 * sc), P(A[0], (10 + 10 * (R3 - 1)) * sc)
    tower(ax, A[0], 10 * sc, 0.7)
    seg(ax, B, D, ACC, 1.6)
    ax.fill([D[0], D[0] + 0.7, D[0]], [D[1], D[1] - 0.25, D[1] - 0.5], color=HI)
    sight(ax, Pp, B); sight(ax, Pp, D)
    angle(ax, Pp, A, B, 1.4, "30°", tr=1.9)
    angle(ax, Pp, B, D, 2.3, "45°", tr=2.75)
    lab(ax, Pp, "P", (-8, -8)); lab(ax, A, "A", (9, -9)); lab(ax, B, "B", (12, 0)); lab(ax, D, "D", (-9, 4))
    dim(ax, A, B, "10 m", (1.05, 0)); dim(ax, B, D, "$x$", (0.35, 0), color=ACC)
    finish(ax, (-0.8, 7.2), (-0.7, 6.2))
    save(fig, "ch09_fig06_example4.png")


# Fig 9.7: Example 5 - shadows at sun's altitudes 60 and 30 degrees
def fig_example5():
    fig, ax = new(4.8, 2.6)
    ground(ax, -0.6, 8.6)
    sc = 0.115
    h = 20 * R3 * sc
    B = P(8, 0)
    A = P(8, h)
    C, D = P(8 - 20 * sc, 0), P(8 - 60 * sc, 0)
    tower(ax, 8, h, 0.45)
    sight(ax, C, A); sight(ax, D, A)
    angle(ax, C, B, A, 0.55, "60°", tr=0.95)
    angle(ax, D, B, A, 1.2, "30°", tr=1.65)
    lab(ax, A, "A", (8, 5)); lab(ax, B, "B", (8, -9)); lab(ax, C, "C", (0, -11)); lab(ax, D, "D", (-6, -9))
    dim(ax, D, C, "40 m", (0, -0.42)); dim(ax, C, B, "$x$", (0, -0.42))
    dim(ax, A, B, "$h$", (0.45, 0))
    finish(ax, (-0.8, 8.8), (-1.0, 4.6))
    save(fig, "ch09_fig07_example5.png")


# Fig 9.8: Example 6 - angles of depression 30 and 45 degrees of the top and bottom of an 8 m building
def fig_example6():
    fig, ax = new(4.0, 3.6)
    ground(ax, -0.6, 7)
    sc = 0.2
    pc = (4 * (R3 + 1) + 8) * sc
    Pp, C = P(0, pc), P(0, 0)
    Aa = P(pc, 0)
    Bb = P(pc, 8 * sc)
    Dd = P(0, 8 * sc)
    ax.add_patch(Rectangle((-0.5, 0), 0.5, pc, fc=SOFT, ec=INK, lw=1.2))
    ax.add_patch(Rectangle((pc, 0), 0.6, 8 * sc, fc="#F3EAD9", ec=INK, lw=1.2))
    Q = P(pc + 0.6, pc)
    seg(ax, Pp, Q, GREY, 0.9, ":")
    seg(ax, Dd, Bb, GREY, 0.9, ":")
    sight(ax, Pp, Bb); sight(ax, Pp, Aa)
    angle(ax, Pp, Q, Bb, 1.6, "30°", tr=2.1)
    angle(ax, Pp, Q, Aa, 0.75, "45°", tr=1.15)
    lab(ax, Pp, "P", (-9, 5)); lab(ax, C, "C", (-12, -8)); lab(ax, Aa, "A", (-4, -10)); lab(ax, Bb, "B", (-4, 9))
    lab(ax, Dd, "D", (8, -8)); lab(ax, Q, "Q", (6, 6))
    dim(ax, Aa, Bb, "8 m", (1.05, 0))
    finish(ax, (-1.0, 7.4), (-0.7, 6.4))
    save(fig, "ch09_fig08_example6.png")


# Fig 9.9: Example 7 - a bridge 3 m above the banks; angles of depression 30 and 45 degrees
def fig_example7():
    fig, ax = new(4.8, 2.0)
    A, B, D = P(0, 0), P(3 * R3 + 3, 0), P(3 * R3, 0)
    Pp = P(3 * R3, 3)
    ax.add_patch(Rectangle((-0.3, 2.85), B[0] + 0.6, 0.3, fc="#D9DEE5", ec=INK, lw=1))
    ax.fill_between([0, B[0]], [-0.6, -0.6], [0, 0], color="#CFE3F2")
    seg(ax, P(-0.6, 0), P(B[0] + 0.6, 0), GROUND, 1.4)
    sight(ax, Pp, A); sight(ax, Pp, B)
    seg(ax, Pp, D, GREY, 0.9, ":")
    angle(ax, A, D, Pp, 1.6, "30°", tr=2.1)
    angle(ax, B, Pp, D, 0.9, "45°", tr=1.35)
    lab(ax, A, "A", (-6, -9)); lab(ax, B, "B", (6, -9)); lab(ax, D, "D", (0, -10)); lab(ax, Pp, "P", (0, 12))
    dim(ax, Pp, D, "3 m", (0.35, 0))
    finish(ax, (-0.8, B[0] + 0.8), (-1.0, 3.6))
    save(fig, "ch09_fig09_example7.png")


# Fig 9.10: Ex 9.1 Q1 - a 20 m rope from the top of a pole, 30 degrees with the ground
def fig_q1():
    fig, ax = new(3.6, 2.2)
    ground(ax, -0.5, 6)
    B, A, C = P(5, 0), P(5, 2.5), P(5 - 2.5 * R3, 0)
    seg(ax, B, A, INK, 2.4)
    seg(ax, C, A, ACC, 1.5)
    right(ax, B, A, C, 0.2)
    angle(ax, C, B, A, 0.8, "30°")
    lab(ax, A, "A", (8, 4)); lab(ax, B, "B", (8, -9)); lab(ax, C, "C", (-8, -8))
    dim(ax, C, A, "rope 20 m", (-0.25, 0.35), rot=30, color=ACC)
    finish(ax, (-0.6, 6.2), (-0.6, 3.2))
    save(fig, "ch09_fig10_q1_rope.png")


# Fig 9.11: Ex 9.1 Q2 - tree broken by a storm, top touching the ground 8 m from the foot at 30 degrees
def fig_q2():
    fig, ax = new(3.6, 2.4)
    ground(ax, -0.5, 6)
    B = P(0.5, 0)
    C = P(0.5, 8 / R3 * 0.4)
    D = P(0.5 + 8 * 0.4, 0)
    seg(ax, B, C, "#6B4F2A", 3)
    seg(ax, C, D, "#6B4F2A", 2.2)
    right(ax, B, C, D, 0.18)
    angle(ax, D, B, C, 0.7, "30°")
    lab(ax, B, "B", (-8, -8)); lab(ax, C, "C", (-8, 5)); lab(ax, D, "D", (8, -8))
    dim(ax, B, D, "8 m", (0, -0.3))
    dim(ax, C, D, "broken part", (0.35, 0.3), rot=-30, color=ACC)
    finish(ax, (-0.4, 4.4), (-0.6, 2.4))
    save(fig, "ch09_fig11_q2_tree.png")


# Fig 9.12: Ex 9.1 Q6 - a boy walks towards a 30 m building; elevation changes from 30 to 60 degrees
def fig_q6():
    fig, ax = new(4.8, 2.8)
    ground(ax, -0.5, 9.5)
    sc = 0.1
    h = 28.5 * sc
    Bx = 9
    A = P(Bx, 30 * sc)
    E1, E2 = P(Bx - 28.5 * R3 * sc, 1.5 * sc), P(Bx - 28.5 / R3 * sc, 1.5 * sc)
    tower(ax, Bx, 30 * sc, 0.6)
    for E in (E1, E2):
        person(ax, E[0], 1.5 * sc * 2.2)
        sight(ax, E, A)
    seg(ax, E1, P(Bx, 1.5 * sc), GREY, 0.9, ":")
    angle(ax, E1, P(Bx, E1[1]), A, 0.9, "30°", tr=1.3)
    angle(ax, E2, P(Bx, E2[1]), A, 0.5, "60°", tr=0.85)
    dim(ax, P(E1[0], 0), P(E2[0], 0), "distance walked", (0, -0.35), size=8)
    dim(ax, A, P(Bx, 0), "30 m", (0.85, 0))
    ax.text(E1[0] - 0.15, 0.45, "1.5 m", fontsize=7.5, ha="right", color=ACC)
    finish(ax, (-0.6, 10.0), (-0.8, 3.6))
    save(fig, "ch09_fig12_q6_boy.png")


# Fig 9.13: Ex 9.1 Q7 (SSLC 2025 Q52) - tower on top of a 20 m building; elevations 45 and 60 degrees
def fig_q7():
    fig, ax = new(3.6, 3.6)
    ground(ax, -0.5, 4.6)
    sc = 0.11
    Pp = P(0, 0)
    B = P(20 * sc, 20 * sc)
    D = P(20 * sc, 20 * R3 * sc)
    ax.add_patch(Rectangle((B[0], 0), 0.9, B[1], fc=SOFT, ec=INK, lw=1.2))
    seg(ax, B, D, ACC, 2.2)
    sight(ax, Pp, B); sight(ax, Pp, D)
    angle(ax, Pp, P(1, 0), B, 0.7, "45°", tr=1.05)
    angle(ax, Pp, P(1, 0), D, 1.5, "60°", tr=1.85)
    lab(ax, Pp, "P", (-8, -8)); lab(ax, B, "B", (-8, 5)); lab(ax, D, "D", (-8, 5)); lab(ax, P(B[0], 0), "A", (-6, -9))
    dim(ax, B, P(B[0], 0), "20 m", (1.2, 0)); dim(ax, B, D, "tower", (-0.55, 0), color=ACC)
    finish(ax, (-0.6, 4.8), (-0.6, 4.4))
    save(fig, "ch09_fig13_q7_transmission_tower.png")


# Fig 9.14: Ex 9.1 Q9 (SSLC 2026 Q52) - building and 50 m tower; 30 and 60 degrees from each other's foot
def fig_q9():
    fig, ax = new(4.0, 3.2)
    ground(ax, -0.8, 6.2)
    sc = 0.08
    d = 50 / R3 * sc
    T, Bf = P(0, 0), P(d, 0)
    Ttop, Btop = P(0, 50 * sc), P(d, 50 / 3 * sc)
    ax.add_patch(Rectangle((-0.45, 0), 0.45, Ttop[1], fc=SOFT, ec=INK, lw=1.2))
    ax.add_patch(Rectangle((d, 0), 0.7, Btop[1], fc="#F3EAD9", ec=INK, lw=1.2))
    sight(ax, Bf, Ttop); sight(ax, T, Btop)
    angle(ax, T, P(1, 0), Btop, 0.6, "30°", tr=0.9)
    angle(ax, Bf, P(0, 0), Ttop, 0.32, "60°", tr=0.62)
    lab(ax, Ttop, "A", (-13, 4)); lab(ax, T, "B", (-12, -8)); lab(ax, Bf, "C", (6, -9)); lab(ax, Btop, "D", (14, 4))
    dim(ax, Ttop, T, "50 m", (-0.95, 0)); dim(ax, Btop, Bf, "$h$", (0.95, 0))
    ax.text(-0.25, -0.75, "tower", ha="center", fontsize=8); ax.text(d + 0.35, -0.75, "building", ha="center", fontsize=8)
    finish(ax, (-1.6, 5.6), (-1.0, 4.6))
    save(fig, "ch09_fig14_q9_building_tower.png")


# Fig 9.15: Ex 9.1 Q10 - two equal poles on opposite sides of an 80 m road
def fig_q10():
    fig, ax = new(4.8, 2.4)
    ground(ax, -0.4, 8.4)
    sc = 0.1
    h = 20 * R3 * sc
    L, R_ = P(0, 0), P(8, 0)
    Pp = P(2, 0)
    seg(ax, L, P(0, h), INK, 2.4); seg(ax, R_, P(8, h), INK, 2.4)
    sight(ax, Pp, P(0, h)); sight(ax, Pp, P(8, h))
    angle(ax, Pp, P(-1, 0), P(0, h), 0.55, "60°", tr=0.95)
    angle(ax, Pp, P(9, 0), P(8, h), 0.9, "30°", tr=1.3)
    lab(ax, P(0, h), "A", (-8, 4)); lab(ax, L, "B", (-8, -8)); lab(ax, P(8, h), "D", (8, 4)); lab(ax, R_, "C", (8, -8)); lab(ax, Pp, "P", (0, -10))
    dim(ax, L, Pp, "$x$", (0, -0.42)); dim(ax, Pp, R_, "$80 - x$", (0, -0.42))
    finish(ax, (-0.6, 8.6), (-0.9, 4.0))
    save(fig, "ch09_fig15_q10_poles.png")


# Fig 9.16: Ex 9.1 Q11 (sample paper Q54) - TV tower on the bank of a canal
def fig_q11():
    fig, ax = new(4.4, 2.8)
    sc = 0.18
    h = 10 * R3 * sc
    B = P(0, 0)
    A = P(0, h)
    C, D = P(10 * sc * 2.2, 0), P(30 * sc * 2.2, 0)
    xs = 2.2
    C, D = P(10 * sc * xs, 0), P(30 * sc * xs, 0)
    A = P(0, 10 * R3 * sc * xs)
    ax.fill_between([0.05, C[0] - 0.05], [-0.5, -0.5], [0, 0], color="#CFE3F2")
    ground(ax, -0.6, D[0] + 0.6)
    seg(ax, B, A, INK, 2.4)
    sight(ax, C, A); sight(ax, D, A)
    angle(ax, C, P(C[0] - 1, 0), A, 0.6, "60°", tr=1.0)
    angle(ax, D, P(D[0] - 1, 0), A, 1.2, "30°", tr=1.6)
    lab(ax, A, "A", (-8, 4)); lab(ax, B, "B", (-8, -8)); lab(ax, C, "C", (0, -11)); lab(ax, D, "D", (6, -9))
    dim(ax, C, D, "20 m", (0, -0.42)); dim(ax, B, C, "canal", (0, -0.32), size=8)
    finish(ax, (-0.8, D[0] + 0.8), (-0.9, A[1] + 0.5))
    save(fig, "ch09_fig16_q11_canal.png")


# Fig 9.17: Ex 9.1 Q12 - from the top of a 7 m building: elevation 60 to the top of a cable tower, depression 45 to its foot
def fig_q12():
    fig, ax = new(3.6, 3.6)
    ground(ax, -0.8, 5.2)
    sc = 0.22
    d = 7 * sc
    A, B = P(0, 7 * sc), P(0, 0)
    C, E = P(7 * sc * 2.2, 0), P(7 * sc * 2.2, 7 * sc)
    Ttop = P(C[0], (7 + 7 * R3) * sc)
    ax.add_patch(Rectangle((-0.6, 0), 0.6, A[1], fc=SOFT, ec=INK, lw=1.2))
    seg(ax, C, Ttop, INK, 2.4)
    seg(ax, A, E, GREY, 0.9, ":")
    sight(ax, A, Ttop); sight(ax, A, C)
    angle(ax, A, E, Ttop, 0.6, "60°", tr=0.95)
    angle(ax, A, E, C, 0.5, "45°", tr=0.85)
    lab(ax, A, "A", (-9, 5)); lab(ax, B, "B", (-9, -8)); lab(ax, C, "C", (8, -8)); lab(ax, E, "E", (9, -2)); lab(ax, Ttop, "D", (8, 4))
    dim(ax, A, B, "7 m", (-0.95, 0))
    finish(ax, (-1.2, 4.2), (-0.6, 4.6))
    save(fig, "ch09_fig17_q12_cable_tower.png")


# Fig 9.18: Ex 9.1 Q13 - lighthouse 75 m; depressions of two ships 30 and 45 degrees
def fig_q13():
    fig, ax = new(4.8, 2.4)
    sc = 0.025
    h = 75 * sc
    A, B = P(0, h), P(0, 0)
    C, D = P(75 * sc, 0), P(75 * R3 * sc, 0)
    ax.fill_between([0.2, D[0] + 0.6], [-0.4, -0.4], [0, 0], color="#CFE3F2")
    ax.add_patch(Polygon([[-0.3, 0], [0.2, 0], [0.08, h], [-0.18, h]], closed=True, fc="white", ec=INK, lw=1.2))
    for S in (C, D):
        ax.add_patch(Polygon([[S[0] - 0.25, 0.02], [S[0] + 0.25, 0.02], [S[0] + 0.15, -0.1], [S[0] - 0.15, -0.1]], closed=True, fc=GREY))
    Q = P(D[0] + 0.3, h)
    seg(ax, A, Q, GREY, 0.9, ":")
    sight(ax, A, C); sight(ax, A, D)
    angle(ax, A, Q, D, 1.4, "30°", tr=1.75)
    angle(ax, A, Q, C, 0.6, "45°", tr=0.95)
    lab(ax, A, "A", (-10, 4)); lab(ax, B, "B", (-10, -6)); lab(ax, C, "C", (0, -12)); lab(ax, D, "D", (0, -12))
    dim(ax, A, B, "75 m", (-0.75, 0))
    finish(ax, (-1.2, D[0] + 0.8), (-0.8, h + 0.6))
    save(fig, "ch09_fig18_q13_lighthouse.png")


# Fig 9.19: Ex 9.1 Q14 - a balloon moving horizontally at 88.2 m, seen by a 1.2 m girl at 60 then 30 degrees
def fig_q14():
    fig, ax = new(4.6, 2.8)
    ground(ax, -0.6, 6.6)
    sc = 0.035
    eye = P(0, 1.2 * sc * 6)
    h = 87 * sc + eye[1]
    B1 = P(87 / R3 * sc, h)
    B2 = P(87 * R3 * sc, h)
    person(ax, 0, eye[1])
    for Bp in (B1, B2):
        ax.add_patch(plt.Circle(Bp + P(0, 0.22), 0.22, fc="#F4C7C3", ec=INK, lw=1))
        sight(ax, eye, Bp)
    seg(ax, eye, P(B2[0] + 0.3, eye[1]), GREY, 0.9, ":")
    seg(ax, B1, B2, ACC, 1.2, "-")
    angle(ax, eye, P(1, eye[1]), B1, 0.6, "60°", tr=0.9)
    angle(ax, eye, P(1, eye[1]), B2, 1.4, "30°", tr=1.75)
    lab(ax, B1, "P", (-10, 6)); lab(ax, B2, "Q", (10, 6))
    dim(ax, B1, B2, "distance travelled", (0, 0.65), size=8, color=ACC)
    ax.text(B2[0] + 0.45, h / 2, "88.2 m above\nthe ground", fontsize=7.5, va="center")
    finish(ax, (-0.8, 6.8), (-0.4, h + 0.9))
    save(fig, "ch09_fig19_q14_balloon.png")


# Fig 9.20: Ex 9.1 Q15 - a car approaching a tower; depression 30 then 60 degrees
def fig_q15():
    fig, ax = new(4.6, 2.6)
    ground(ax, -0.6, 7.2)
    sc = 1.0
    h = 2.4
    A, B = P(0, h), P(0, 0)
    C1, C2 = P(h * R3, 0), P(h / R3, 0)
    ax.add_patch(Rectangle((-0.45, 0), 0.45, h, fc=SOFT, ec=INK, lw=1.2))
    for c in (C1, C2):
        ax.add_patch(Rectangle((c[0] - 0.22, 0.02), 0.44, 0.18, fc=ACC, ec=INK, lw=0.8))
    Q = P(C1[0] + 0.4, h)
    seg(ax, A, Q, GREY, 0.9, ":")
    sight(ax, A, C1); sight(ax, A, C2)
    angle(ax, A, Q, C1, 1.5, "30°", tr=1.85)
    angle(ax, A, Q, C2, 0.6, "60°", tr=0.95)
    lab(ax, A, "A", (-10, 4)); lab(ax, B, "B", (-10, -8)); lab(ax, C1, "C", (0, -12)); lab(ax, C2, "D", (0, -12))
    dim(ax, C2, C1, "6 seconds", (0, -0.55), size=8); dim(ax, B, C2, "?", (0, -0.55), size=9)
    finish(ax, (-0.8, 5.0), (-0.9, 3.0))
    save(fig, "ch09_fig20_q15_car.png")


if __name__ == "__main__":
    fig_elevation(); fig_depression(); fig_example1(); fig_example2(); fig_example3(); fig_example4()
    fig_example5(); fig_example6(); fig_example7(); fig_q1(); fig_q2(); fig_q6(); fig_q7(); fig_q9()
    fig_q10(); fig_q11(); fig_q12(); fig_q13(); fig_q14(); fig_q15()
