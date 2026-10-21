"""Figures for Class X Mathematics, Chapter 10: Circles.
Run: python x_ch10_circles.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Polygon

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


def U(deg):
    t = np.radians(deg)
    return np.array([np.cos(t), np.sin(t)])


def circ(ax, c, r, fc="none", ec=ACC, lw=1.5):
    ax.add_patch(Circle(c, r, fc=fc, ec=ec, lw=lw))


def seg(ax, a, b, color=INK, lw=1.3, ls="-"):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls=ls, solid_capstyle="round")


def dot(ax, p, c=INK, ms=3.2):
    ax.plot(*p, "o", ms=ms, color=c)


def lab(ax, p, s, off, size=10.5, color=INK):
    ax.annotate(s, p, textcoords="offset points", xytext=off, ha="center", va="center", fontsize=size, color=color)


def right(ax, at, p, q, s=0.22):
    u = (p - at) / np.linalg.norm(p - at) * s
    v = (q - at) / np.linalg.norm(q - at) * s
    ax.plot(*zip(at + u, at + u + v, at + v), color=INK, lw=0.8)


def angle(ax, at, p, q, r, text, tr=None, size=9, color=HI):
    a1 = np.degrees(np.arctan2(*(p - at)[::-1]))
    a2 = np.degrees(np.arctan2(*(q - at)[::-1]))
    if (a2 - a1) % 360 > 180:
        a1, a2 = a2, a1
    ax.add_patch(Arc(at, 2 * r, 2 * r, theta1=a1, theta2=a2, color=color, lw=1.1))
    if text:
        mid = np.radians(a1 + ((a2 - a1) % 360) / 2)
        rr = tr or r + 0.3
        ax.text(at[0] + rr * np.cos(mid), at[1] + rr * np.sin(mid), text, ha="center", va="center", fontsize=size, color=color)


def tangent_points(o, r, t):
    """Points of contact of the two tangents from external point t to the circle (o, r)."""
    d = t - o
    dist = np.linalg.norm(d)
    a = np.degrees(np.arccos(r / dist))
    base = np.degrees(np.arctan2(d[1], d[0]))
    return o + r * U(base + a), o + r * U(base - a)


def tangent_vertex(o, r, a, b):
    """Meeting point of the tangents at the points of the circle at angles a and b (degrees)."""
    return o + r / np.cos(np.radians((b - a) / 2)) * U((a + b) / 2)


def finish(ax, pad=0.15):
    ax.set_aspect("equal")
    ax.axis("off")
    ax.margins(pad)


# Fig 10.1: a line and a circle - no common point, a secant, a tangent
def fig_positions():
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.4))
    for ax, y, cap, pts in [(axs[0], 1.45, "(i) non-intersecting", 0), (axs[1], 0.45, "(ii) secant", 2), (axs[2], 1.0, "(iii) tangent", 1)]:
        circ(ax, P(0, 0), 1.0)
        seg(ax, P(-1.6, y), P(1.6, y), INK, 1.3)
        lab(ax, P(-1.6, y), "P", (-8, 0)); lab(ax, P(1.6, y), "Q", (8, 0))
        if pts == 2:
            x = np.sqrt(1 - y * y)
            for xx, nm in [(-x, "A"), (x, "B")]:
                dot(ax, P(xx, y)); lab(ax, P(xx, y), nm, (0, 9))
        if pts == 1:
            dot(ax, P(0, 1)); lab(ax, P(0, 1), "A", (0, 9))
        ax.text(0, -1.45, cap, ha="center", fontsize=9)
        ax.set_xlim(-1.9, 1.9); ax.set_ylim(-1.7, 1.8); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch10_fig01_line_and_circle.png")


# Fig 10.2: Theorem 10.1 - the tangent is perpendicular to the radius at the point of contact
def fig_thm1():
    fig, ax = plt.subplots(figsize=(3.6, 3.0))
    O = P(0, 0)
    r = 1.6
    Pp = P(0, -r)
    X, Y = P(-2.6, -r), P(2.6, -r)
    Q = P(1.6, -r)
    circ(ax, O, r)
    seg(ax, X, Y)
    seg(ax, O, Pp, ACC, 1.3)
    seg(ax, O, Q, GREY, 1.1, "--")
    right(ax, Pp, O, Y, 0.18)
    for p, n, off in [(O, "O", (-8, 6)), (Pp, "P", (-2, -12)), (Q, "Q", (2, -12)), (X, "X", (-8, 0)), (Y, "Y", (8, 0))]:
        dot(ax, p); lab(ax, p, n, off)
    finish(ax)
    save(fig, "ch10_fig02_theorem1.png")


# Fig 10.3: Theorem 10.2 - tangents PQ and PR from an external point P
def fig_thm2():
    fig, ax = plt.subplots(figsize=(4.4, 2.8))
    O, r, T = P(0, 0), 1.4, P(4.2, 0)
    Q, R = tangent_points(O, r, T)
    circ(ax, O, r)
    seg(ax, T, Q, INK); seg(ax, T, R, INK)
    seg(ax, O, Q, ACC); seg(ax, O, R, ACC); seg(ax, O, T, GREY, 1.1, "--")
    right(ax, Q, O, T, 0.18); right(ax, R, O, T, 0.18)
    for p, n, off in [(O, "O", (-9, 0)), (Q, "Q", (-4, 10)), (R, "R", (-4, -11)), (T, "P", (9, 0))]:
        dot(ax, p); lab(ax, p, n, off)
    finish(ax)
    save(fig, "ch10_fig03_theorem2.png")


# Fig 10.4: Example 1 - concentric circles; the chord AB of the larger circle touches the smaller at P
def fig_concentric():
    fig, ax = plt.subplots(figsize=(3.2, 3.2))
    O = P(0, 0)
    R1, r2 = 2.0, 1.2
    circ(ax, O, R1); circ(ax, O, r2, ec=HI)
    x = np.sqrt(R1 ** 2 - r2 ** 2)
    A, B, Pp = P(-x, -r2), P(x, -r2), P(0, -r2)
    seg(ax, A, B); seg(ax, O, Pp, ACC, 1.2)
    right(ax, Pp, O, B, 0.16)
    for p, n, off in [(O, "O", (-8, 6)), (A, "A", (-9, -4)), (B, "B", (9, -4)), (Pp, "P", (0, -11))]:
        dot(ax, p); lab(ax, p, n, off)
    ax.text(-1.05, 1.2, "$C_2$", color=HI, fontsize=10); ax.text(1.35, 1.55, "$C_1$", color=ACC, fontsize=10)
    finish(ax)
    save(fig, "ch10_fig04_concentric.png")


# Fig 10.5: Example 2 - tangents TP and TQ; angle PTQ = 2 angle OPQ
def fig_example2():
    fig, ax = plt.subplots(figsize=(4.4, 2.8))
    O, r, T = P(0, 0), 1.4, P(4.0, 0)
    Pp, Q = tangent_points(O, r, T)
    circ(ax, O, r)
    seg(ax, T, Pp); seg(ax, T, Q); seg(ax, Pp, Q, GREY, 1.1)
    seg(ax, O, Pp, ACC); seg(ax, O, Q, ACC)
    right(ax, Pp, O, T, 0.16); right(ax, Q, O, T, 0.16)
    angle(ax, T, Pp, Q, 0.55, r"$\theta$", tr=0.85)
    for p, n, off in [(O, "O", (-9, 0)), (Pp, "P", (-4, 10)), (Q, "Q", (-4, -11)), (T, "T", (9, 0))]:
        dot(ax, p); lab(ax, p, n, off)
    finish(ax)
    save(fig, "ch10_fig05_example2.png")


# Fig 10.6: Example 3 - chord PQ = 8 cm in a circle of radius 5 cm; tangents at P and Q meet at T
def fig_example3():
    fig, ax = plt.subplots(figsize=(4.4, 2.8))
    O, r = P(0, 0), 5.0
    Pp, Q = P(3, 4), P(3, -4)
    T = P(25 / 3, 0)
    R = P(3, 0)
    sc = 0.32
    O, Pp, Q, T, R = O * sc, Pp * sc, Q * sc, T * sc, R * sc
    circ(ax, O, r * sc)
    seg(ax, T, Pp); seg(ax, T, Q); seg(ax, Pp, Q, GREY, 1.1)
    seg(ax, O, Pp, ACC); seg(ax, O, T, GREY, 1.1, "--")
    right(ax, R, Pp, T, 0.12)
    for p, n, off in [(O, "O", (-8, 6)), (Pp, "P", (-2, 10)), (Q, "Q", (-2, -11)), (T, "T", (9, 0)), (R, "R", (8, 8))]:
        dot(ax, p); lab(ax, p, n, off)
    ax.text(*(O + Pp) / 2 + P(-0.25, 0.1), "5", color=ACC, fontsize=9)
    finish(ax)
    save(fig, "ch10_fig06_example3.png")


# Fig 10.7: Ex 10.2 Q2 - tangents TP, TQ with angle POQ = 110 degrees
def fig_ex102_q2():
    fig, ax = plt.subplots(figsize=(4.2, 2.6))
    O, r = P(0, 0), 1.3
    Pp, Q = O + r * U(55), O + r * U(-55)
    T = tangent_vertex(O, r, 55, -55)
    circ(ax, O, r)
    seg(ax, T, Pp); seg(ax, T, Q); seg(ax, O, Pp, ACC); seg(ax, O, Q, ACC)
    right(ax, Pp, O, T, 0.15); right(ax, Q, O, T, 0.15)
    angle(ax, O, Pp, Q, 0.35, "110°", tr=0.62, size=8.5)
    angle(ax, T, Pp, Q, 0.45, "?", tr=0.72)
    for p, n, off in [(O, "O", (-9, 0)), (Pp, "P", (-2, 10)), (Q, "Q", (-2, -11)), (T, "T", (9, 0))]:
        dot(ax, p); lab(ax, p, n, off)
    finish(ax)
    save(fig, "ch10_fig07_ex102_q2.png")


# Fig 10.8: Ex 10.2 Q8 - quadrilateral ABCD circumscribing a circle (P, Q, R, S points of contact)
def fig_quad():
    fig, ax = plt.subplots(figsize=(3.6, 3.4))
    O, r = P(0, 0), 1.3
    angs = [-100, -10, 75, 175]  # points of contact on AB, BC, CD, DA
    names = ["P", "Q", "R", "S"]
    verts = [tangent_vertex(O, r, angs[i - 1], angs[i]) for i in range(4)]  # A between S and P, B between P and Q ...
    circ(ax, O, r)
    ax.add_patch(Polygon(np.array(verts), closed=True, fc="none", ec=INK, lw=1.3))
    for v, n in zip(verts, "ABCD"):
        dot(ax, v); lab(ax, v, n, tuple(10 * (v - O) / np.linalg.norm(v - O)))
    for a, n in zip(angs, names):
        p = O + r * U(a)
        dot(ax, p, ACC); lab(ax, p, n, tuple(-11 * U(a)), color=ACC, size=9.5)
    dot(ax, O); lab(ax, O, "O", (8, 6))
    finish(ax)
    save(fig, "ch10_fig08_quadrilateral.png")


# Fig 10.9: Ex 10.2 Q9 - parallel tangents XY, X'Y' and a third tangent AB touching at C
def fig_parallel():
    fig, ax = plt.subplots(figsize=(3.8, 3.2))
    O, r = P(0, 0), 1.2
    C = O + r * U(30)
    A = tangent_vertex(O, r, 90, 30)
    B = tangent_vertex(O, r, 30, -90)
    Pp, Q = P(0, r), P(0, -r)
    circ(ax, O, r)
    seg(ax, P(-2.2, r), P(2.6, r)); seg(ax, P(-2.2, -r), P(2.6, -r))
    seg(ax, A, B, INK); seg(ax, O, A, ACC); seg(ax, O, B, ACC); seg(ax, O, C, GREY, 1.0, "--")
    for p, n, off in [(O, "O", (-9, 0)), (A, "A", (2, 10)), (B, "B", (2, -11)), (C, "C", (10, 0)), (Pp, "P", (0, 10)), (Q, "Q", (0, -11))]:
        dot(ax, p); lab(ax, p, n, off)
    lab(ax, P(-2.2, r), "X", (-8, 0)); lab(ax, P(2.6, r), "Y", (8, 0)); lab(ax, P(-2.2, -r), "X'", (-9, 0)); lab(ax, P(2.6, -r), "Y'", (9, 0))
    finish(ax)
    save(fig, "ch10_fig09_parallel_tangents.png")


# Fig 10.10: Ex 10.2 Q12 - triangle ABC circumscribing a circle of radius 4 cm; BD = 8 cm, DC = 6 cm
def fig_triangle_incircle():
    fig, ax = plt.subplots(figsize=(3.6, 3.6))
    sc = 0.22
    A, B, C, I, D = P(1, 12) * sc, P(-8, 0) * sc, P(6, 0) * sc, P(0, 4) * sc, P(0, 0) * sc
    ax.add_patch(Polygon(np.array([A, B, C]), closed=True, fc="none", ec=INK, lw=1.3))
    circ(ax, I, 4 * sc)
    seg(ax, I, D, GREY, 1.0, "--")
    for p, n, off in [(A, "A", (0, 9)), (B, "B", (-9, -5)), (C, "C", (9, -5)), (I, "O", (8, 4)), (D, "D", (0, -11))]:
        dot(ax, p); lab(ax, p, n, off)
    ax.text(*(B + D) / 2 + P(0, -0.32), "8 cm", ha="center", fontsize=9, color=ACC)
    ax.text(*(D + C) / 2 + P(0, -0.32), "6 cm", ha="center", fontsize=9, color=ACC)
    ax.text(*(I + D) / 2 + P(0.28, 0), "4", fontsize=9, color=ACC)
    finish(ax)
    save(fig, "ch10_fig10_triangle_incircle.png")


# Fig 10.11: SSLC 2026 Q45 - incircle of triangle ABC with AB = AC touching BC at E
def fig_isosceles_incircle():
    fig, ax = plt.subplots(figsize=(3.0, 3.2))
    A, B, C = P(0, 6), P(-3, 0), P(3, 0)
    a, b, c = np.linalg.norm(B - C), np.linalg.norm(C - A), np.linalg.norm(A - B)
    I = (a * A + b * B + c * C) / (a + b + c)
    s = (a + b + c) / 2
    r = 18 / s
    def foot(p, u, v):
        d = v - u
        return u + d * np.dot(p - u, d) / np.dot(d, d)
    D, E, F = foot(I, A, B), foot(I, B, C), foot(I, A, C)
    ax.add_patch(Polygon(np.array([A, B, C]), closed=True, fc="none", ec=INK, lw=1.3))
    circ(ax, I, r)
    for p, n, off in [(A, "A", (0, 9)), (B, "B", (-9, -5)), (C, "C", (9, -5)), (D, "D", (-9, 2)), (E, "E", (0, -11)), (F, "F", (9, 2))]:
        dot(ax, p); lab(ax, p, n, off)
    dot(ax, I)
    finish(ax)
    save(fig, "ch10_fig11_isosceles_incircle.png")


# Fig 10.12: SSLC 2026 Q44 - circle touching BC at P and AB, AC produced at Q and R
def fig_excircle():
    fig, ax = plt.subplots(figsize=(4.6, 3.0))
    A = P(0, 0)
    half = 24
    c = 6.0
    O = P(c, 0)
    rho = c * np.sin(np.radians(half))
    Q = A + c * np.cos(np.radians(half)) * U(half)
    R = A + c * np.cos(np.radians(half)) * U(-half)
    Pp = O + rho * U(168)
    n = U(168)  # BC is perpendicular to OP at P
    def meet_ray(ang):
        u = U(ang)
        t = np.dot(Pp - A, n) / np.dot(u, n)
        return A + t * u
    B, C = meet_ray(half), meet_ray(-half)
    circ(ax, O, rho)
    seg(ax, A, Q + 0.6 * U(half)); seg(ax, A, R + 0.6 * U(-half)); seg(ax, B, C, INK, 1.4)
    for p, nm, off in [(A, "A", (-9, 0)), (B, "B", (-3, 10)), (C, "C", (-3, -11)), (Pp, "P", (-10, -2)), (Q, "Q", (-2, 10)), (R, "R", (-2, -11))]:
        dot(ax, p); lab(ax, p, nm, off)
    dot(ax, O)
    finish(ax)
    save(fig, "ch10_fig12_excircle.png")


# Fig 10.13: Ex 10.1 Q3 - tangent PQ at P meets the line through the centre at Q; r = 5 cm, OQ = 12 cm
def fig_ex101_q3():
    fig, ax = plt.subplots(figsize=(4.2, 2.4))
    sc = 0.2
    O, r = P(0, 0), 5 * sc
    Q = P(12 * sc, 0)
    Pp, _ = tangent_points(O, r, Q)
    circ(ax, O, r)
    seg(ax, O, Q, GREY, 1.1); seg(ax, O, Pp, ACC); seg(ax, Pp, Q)
    right(ax, Pp, O, Q, 0.12)
    for p, n, off in [(O, "O", (-8, -6)), (Pp, "P", (-4, 10)), (Q, "Q", (9, 0))]:
        dot(ax, p); lab(ax, p, n, off)
    ax.text(*(O + Pp) / 2 + P(-0.22, 0.05), "5 cm", fontsize=8.5, color=ACC, ha="right")
    ax.text(*(O + Q) / 2 + P(0.45, -0.22), "12 cm", fontsize=8.5, color=ACC, ha="center")
    finish(ax)
    save(fig, "ch10_fig13_ex101_q3.png")


# Fig 10.14: Ex 10.2 Q13 - opposite sides of a circumscribed quadrilateral subtend supplementary angles at O
def fig_quad_centre():
    fig, ax = plt.subplots(figsize=(3.6, 3.4))
    O, r = P(0, 0), 1.3
    angs = [-100, -10, 75, 175]
    verts = [tangent_vertex(O, r, angs[i - 1], angs[i]) for i in range(4)]
    circ(ax, O, r)
    ax.add_patch(Polygon(np.array(verts), closed=True, fc="none", ec=INK, lw=1.3))
    for v, n in zip(verts, "ABCD"):
        seg(ax, O, v, GREY, 1.0, "--")
        dot(ax, v); lab(ax, v, n, tuple(10 * (v - O) / np.linalg.norm(v - O)))
    for a, n in zip(angs, "PQRS"):
        p = O + r * U(a)
        seg(ax, O, p, ACC, 1.0)
        dot(ax, p, ACC); lab(ax, p, n, tuple(-11 * U(a + 18)), color=ACC, size=9.5)
    dot(ax, O); lab(ax, O, "O", (11, -4))
    finish(ax)
    save(fig, "ch10_fig14_quad_centre.png")


if __name__ == "__main__":
    fig_positions(); fig_thm1(); fig_thm2(); fig_concentric(); fig_example2(); fig_example3(); fig_ex102_q2()
    fig_quad(); fig_parallel(); fig_triangle_incircle(); fig_isosceles_incircle(); fig_excircle(); fig_ex101_q3(); fig_quad_centre()
