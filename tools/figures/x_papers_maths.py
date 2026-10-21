"""Figures for the transcribed MBOSE SSLC Mathematics papers (PYQ Papers/Maths/figures).
Run: python x_papers_maths.py
Drawn afresh in the chapter-figure style, to the papers' own lettering.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import numpy as np  # noqa: E402

import x_ch06_triangles as t
from x_ch06_triangles import ACC, INK, P, dots, finish, label, plt, right, seg

t.OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "PYQ Papers", "Maths", "figures")
os.makedirs(t.OUT, exist_ok=True)


def circle(ax, c, r, color=ACC, lw=1.6):
    ax.add_patch(plt.Circle(c, r, fill=False, color=color, lw=lw))
    ax.plot(*c, "o", ms=3, color=INK)


def tangent_points(p, c, r):
    """The two points where tangents from p touch the circle (centre c, radius r)."""
    d = p - c
    dist = np.linalg.norm(d)
    base = np.arctan2(d[1], d[0])
    a = np.arccos(r / dist)
    return [c + r * np.array([np.cos(base + s * a), np.sin(base + s * a)]) for s in (1, -1)]


def sslc2026_q37():
    fig, ax = plt.subplots(figsize=(4.2, 2.2))
    p = {"A": P(1, 1.5), "B": P(0, 0), "C": P(2, 0), "D": P(5.6, 3), "E": P(3.6, 0), "F": P(7.6, 0)}
    for tri in ("ABC", "DEF"):
        for i in range(3):
            seg(ax, p[tri[i]], p[tri[(i + 1) % 3]])
    label(ax, {k: p[k] for k in "ABC"}, list("ABC"))
    label(ax, {k: p[k] for k in "DEF"}, list("DEF"))
    finish(ax)
    t.save(fig, "sslc2026_q37_similar_triangles.png")


def sslc2026_q44():
    fig, ax = plt.subplots(figsize=(4.6, 2.8))
    c, r = P(3.2, 0), 1.0
    A = P(0, 0)
    Q, R = tangent_points(A, c, r)  # R on the upper line AC, Q on the lower line AB
    Pt = c + P(-r, 0)
    up, low = R - A, Q - A
    # BC is the tangent at P (vertical), meeting AC at C and AB at B.
    C = A + up * (Pt[0] - A[0]) / up[0]
    B = A + low * (Pt[0] - A[0]) / low[0]
    for end in (R, Q):
        d = end - A
        tip = A + d * 1.35
        seg(ax, A, tip - d * 0.02)
        ax.annotate("", tip, tip - d * 0.08, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    seg(ax, B, C)
    circle(ax, c, r)
    pts = {"A": A, "B": B, "C": C, "P": Pt, "Q": Q, "R": R}
    dots(ax, pts, ["B", "C", "P", "Q", "R"])
    for n, off in {"A": (-10, 0), "B": (-6, -10), "C": (-6, 9), "P": (-9, 0), "Q": (2, -11), "R": (2, 10)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11, color=INK)
    finish(ax)
    t.save(fig, "sslc2026_q44_excircle.png")


def sslc2026_q45():
    fig, ax = plt.subplots(figsize=(3.0, 3.0))
    A, B, C = P(0, 3.4), P(-2, 0), P(2, 0)
    a, b, c = np.linalg.norm(B - C), np.linalg.norm(C - A), np.linalg.norm(A - B)
    I = (a * A + b * B + c * C) / (a + b + c)
    s = (a + b + c) / 2
    area = abs((B - A)[0] * (C - A)[1] - (B - A)[1] * (C - A)[0]) / 2
    r = area / s
    for u, v in ((A, B), (B, C), (C, A)):
        seg(ax, u, v)
    circle(ax, I, r)
    D, E, F = t.foot(I, A, B), t.foot(I, B, C), t.foot(I, C, A)
    pts = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}
    label(ax, pts, list("ABCDEF"), centre=I, dist=11)
    finish(ax)
    t.save(fig, "sslc2026_q45_incircle.png")


def sslc2026_q51():
    fig, ax = plt.subplots(figsize=(3.8, 2.8))
    A, B = P(0, 0), P(3.2, 0)
    C = P(3.2, 2.8)
    # M on AC with PM ⟂ AC, P on AB produced.
    u = (C - A) / np.linalg.norm(C - A)
    M = A + u * 3.0
    n = np.array([u[1], -u[0]])  # perpendicular to AC, pointing down-right
    Pp = M + n * (M[1] / -n[1]) if n[1] else M
    seg(ax, A, Pp)
    seg(ax, A, C)
    seg(ax, B, C)
    seg(ax, M, Pp)
    right(ax, B, A, C, s=0.2)
    right(ax, M, A, Pp, s=0.2)
    pts = {"A": A, "B": B, "C": C, "M": M, "P": Pp}
    for nme, off in {"A": (-9, -4), "B": (0, -11), "C": (0, 10), "M": (-10, 6), "P": (9, -4)}.items():
        ax.annotate(nme, pts[nme], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11,
                    color=INK)
    finish(ax)
    t.save(fig, "sslc2026_q51_right_triangles.png")


def sslc2026_q50():
    fig, ax = plt.subplots(figsize=(4.2, 2.6))
    O, r = P(0, 0), 1.0
    Pp = P(3.0, 0)
    Q, R = tangent_points(Pp, O, r)
    circle(ax, O, r)
    seg(ax, Pp, Q)
    seg(ax, Pp, R)
    seg(ax, O, Q, color=INK, lw=1.0)
    seg(ax, O, R, color=INK, lw=1.0)
    seg(ax, O, Pp, color=INK, lw=1.0, ls="--")
    right(ax, Q, O, Pp, s=0.14)
    right(ax, R, O, Pp, s=0.14)
    pts = {"O": O, "P": Pp, "Q": Q, "R": R}
    dots(ax, pts, ["P", "Q", "R"])
    for n, off in {"O": (-9, 0), "P": (10, 0), "Q": (0, 11), "R": (0, -11)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11, color=INK)
    finish(ax)
    t.save(fig, "sslc2026_q50_tangents.png")


def sslc2026_q52():
    fig, ax = plt.subplots(figsize=(3.6, 3.2))
    B, C = P(0, 0), P(2.6, 0)
    A, D = P(0, 2.6 / np.sqrt(3)), P(2.6, 2.6 * np.sqrt(3))
    seg(ax, B, C)
    seg(ax, B, A, lw=2.4)
    seg(ax, C, D, lw=2.4)
    seg(ax, C, A, color=ACC, lw=1.0, ls="--")
    seg(ax, B, D, color=ACC, lw=1.0, ls="--")
    t.angle(ax, C, B, A, r=0.55, text="30°", size=8.5)
    t.angle(ax, B, C, D, r=0.45, text="60°", size=8.5)
    pts = {"A": A, "B": B, "C": C, "D": D}
    for n, off in {"A": (-9, 2), "B": (-6, -10), "C": (6, -10), "D": (9, 2)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11, color=INK)
    ax.text(-0.35, A[1] / 2, "$h$", ha="center", fontsize=11, color=INK)
    ax.text(2.95, D[1] / 2, "50 m", ha="left", fontsize=9.5, color=INK)
    ax.text(1.3, -0.35, "$x$", ha="center", fontsize=11, color=INK)
    finish(ax)
    t.save(fig, "sslc2026_q52_building_tower.png")


def sslc2025_q35():
    fig, ax = plt.subplots(figsize=(4.0, 2.6))
    A, B, C = P(2.7, 2.6), P(0, 0), P(3.9, -0.1)
    t_ = 1.8 / 7.2  # AD : DB = AE : EC = 1 : 3, so D and E are a quarter of the way down
    D, E = A + (B - A) * t_, A + (C - A) * t_
    for u, v in ((A, B), (B, C), (C, A), (D, E)):
        seg(ax, u, v)
    for u, v in ((D, E), (B, C)):  # arrow marks for DE || BC
        m = (u + v) / 2
        d = (v - u) / np.linalg.norm(v - u) * 0.12
        ax.annotate("", m + d, m - d, arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
    pts = {"A": A, "B": B, "C": C, "D": D, "E": E}
    for n, off in {"A": (0, 9), "B": (-9, 0), "C": (8, -4), "D": (-9, 3), "E": (8, -2)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11, color=INK)
    ax.text(*((B + D) / 2 + P(-0.45, 0.15)), "7·2 cm", fontsize=9, color=INK)
    ax.text(*((A + E) / 2 + P(0.12, 0.05)), "1·8 cm", fontsize=9, color=INK)
    ax.text(*((E + C) / 2 + P(0.15, 0.0)), "5·4 cm", fontsize=9, color=INK)
    finish(ax)
    t.save(fig, "sslc2025_q35_bpt.png")


def copy_chapter(src, name):
    import shutil
    here = os.path.dirname(__file__)
    shutil.copy2(os.path.join(here, "..", "..", "Class X Content", "Math", "Generated Content", "figures", src),
                 os.path.join(t.OUT, name))
    print("copied", name)


def parallel_marks(ax, pairs):
    for u, v in pairs:
        m = (u + v) / 2
        d = (v - u) / np.linalg.norm(v - u) * 0.12
        ax.annotate("", m + d, m - d, arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))


def sslc2024_q14():
    fig, ax = plt.subplots(figsize=(3.4, 2.4))
    A, B, C = P(1.6, 2.4), P(0, 0), P(3.4, 0)
    D, E = A + (B - A) * 4 / 11, A + (C - A) * 4 / 11
    for u, v in ((A, B), (B, C), (C, A), (D, E)):
        seg(ax, u, v)
    parallel_marks(ax, [(D, E), (B, C)])
    pts = {"A": A, "B": B, "C": C, "D": D, "E": E}
    for n, off in {"A": (0, 9), "B": (-8, -4), "C": (8, -4), "D": (-9, 2), "E": (9, 2)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11, color=INK)
    finish(ax)
    t.save(fig, "sslc2024_q14_bpt.png")


def sslc2024_q15():
    fig, ax = plt.subplots(figsize=(3.6, 3.0))
    O = P(0, 0.55)
    R1, R2 = 1.6, 0.95
    ax.add_patch(plt.Circle(O, R1, fill=False, color=INK, lw=1.2))
    ax.add_patch(plt.Circle(O, R2, fill=False, color=INK, lw=1.2))
    y = 0.0
    dx1, dx2 = np.sqrt(R1**2 - O[1]**2), np.sqrt(R2**2 - O[1]**2)
    seg(ax, P(-2.25, y), P(2.25, y), lw=1.1)
    for end, d in ((P(2.3, y), P(-0.15, 0)), (P(-2.3, y), P(0.15, 0))):
        ax.annotate("", end, end + d, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
    M = P(0, y)
    seg(ax, O, M, lw=1.0)
    right(ax, M, O, P(1, y), s=0.12)
    pts = {"P": P(-dx1, y), "Q": P(-dx2, y), "M": M, "R": P(dx2, y), "S": P(dx1, y), "O": O}
    dots(ax, pts, ["P", "Q", "M", "R", "S", "O"])
    for n, off in {"P": (-7, -10), "Q": (-6, -10), "M": (0, -11), "R": (6, -10), "S": (7, -10), "O": (0, 9)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5, color=INK)
    ax.text(2.35, y, "$l$", fontsize=11, va="center", color=INK)
    finish(ax)
    t.save(fig, "sslc2024_q15_concentric.png")


def sslc2024_q17():
    fig, ax = plt.subplots(figsize=(3.8, 1.9))
    B, C = P(0, 0), P(3.6, 0.55)
    A = P(2.3, 1.45)
    # D divides BC in the ratio AB : AC = 5 : 3.
    D = B + (C - B) * 5 / 8
    for u, v in ((A, B), (B, C), (C, A), (A, D)):
        seg(ax, u, v)
    t.angle(ax, A, B, D, r=0.22)
    t.angle(ax, A, D, C, r=0.26)
    pts = {"A": A, "B": B, "C": C, "D": D}
    for n, off in {"A": (0, 9), "B": (-8, -2), "C": (8, -2), "D": (2, -10)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11, color=INK)
    finish(ax)
    t.save(fig, "sslc2024_q17_bisector.png")


def sslc2024_q28():
    fig, ax = plt.subplots(figsize=(4.6, 3.6))
    xs = np.linspace(-4.5, 5.5, 50)
    ax.axhline(0, color=INK, lw=1.0)
    ax.axvline(0, color=INK, lw=1.0)
    ax.plot(xs, (2 * xs + 6) / 3, color=ACC, lw=1.6, label="$2x - 3y + 6 = 0$")
    ax.plot(xs, 16 - 4 * xs, color="#B7791F", lw=1.6, label="$4x + y - 16 = 0$")
    ax.add_patch(plt.Polygon([[-3, 0], [4, 0], [3, 4]], closed=True, fc="#E9F0F7", ec="none", zorder=0))
    for x, y in ((-3, 0), (0, 2), (3, 4), (4, 0), (2, 8)):
        ax.plot(x, y, "o", ms=3.5, color=INK)
    for (x, y), lab, off in (((3, 4), "(3, 4)", (12, 6)), ((-3, 0), "(−3, 0)", (-6, -11)), ((4, 0), "(4, 0)", (10, -10)),
                             ((0, 2), "(0, 2)", (-16, 6)), ((2, 8), "(2, 8)", (16, 0))):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha="center", fontsize=8.5, color=INK)
    ax.set_xlim(-4.5, 5.5)
    ax.set_ylim(-1.5, 9)
    ax.set_xticks(range(-4, 6))
    ax.set_yticks(range(-1, 10))
    ax.grid(True, color="#DDE3EA", lw=0.6)
    ax.tick_params(labelsize=7.5)
    ax.legend(fontsize=8, loc="upper left")
    t.save(fig, "sslc2024_q28_graph.png")


def sslc2023_q14():
    fig, ax = plt.subplots(figsize=(3.4, 2.0))
    A, B, C = P(2.4, 1.6), P(0, 0), P(3.4, 0)
    D, E = A + (B - A) * 0.375, A + (C - A) * 0.375
    for u, v in ((A, B), (B, C), (C, A), (D, E)):
        seg(ax, u, v)
    pts = {"A": A, "B": B, "C": C, "D": D, "E": E}
    for n, off in {"A": (0, 9), "B": (-8, 0), "C": (8, -2), "D": (-9, 3), "E": (9, 3)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11, color=INK)
    finish(ax)
    t.save(fig, "sslc2023_q14_bpt_check.png")


def sslc2023_q15():
    fig, ax = plt.subplots(figsize=(3.8, 2.2))
    O, r = P(0, 0), 0.9
    Pp = P(3.2, 0)
    T, T2 = tangent_points(Pp, O, r)  # T above, T' below
    Rr = O + P(r, 0)  # the point of the circle nearest P; AB is the tangent there
    A = Pp + (T - Pp) * (Pp[0] - Rr[0]) / (Pp[0] - T[0])
    B = Pp + (T2 - Pp) * (Pp[0] - Rr[0]) / (Pp[0] - T2[0])
    for end in (T, T2):
        seg(ax, Pp, Pp + (end - Pp) * 1.25)
    seg(ax, A, B)
    circle(ax, O, r)
    pts = {"O": O, "P": Pp, "T": T, "T'": T2, "A": A, "B": B, "R": Rr}
    dots(ax, pts, ["P", "T", "T'", "A", "B", "R"])
    for n, off in {"O": (-9, 0), "P": (9, 0), "T": (-3, 10), "T'": (-3, -11), "A": (4, 10), "B": (4, -11),
                   "R": (8, 0)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5, color=INK)
    finish(ax)
    t.save(fig, "sslc2023_q15_tangents.png")


def sslc2023_q17():
    fig, ax = plt.subplots(figsize=(4.4, 2.3))
    c, r = P(3.2, 0), 0.9
    O = P(0, 0)
    B, A = tangent_points(O, c, r)  # A on the upper tangent, B on the lower
    Pt = c + P(-r, 0)
    C = O + (A - O) * (Pt[0] - O[0]) / (A[0] - O[0])
    D = O + (B - O) * (Pt[0] - O[0]) / (B[0] - O[0])
    for end in (A, B):
        d = end - O
        tip = O + d * 1.45
        seg(ax, O, tip - d * 0.02)
        ax.annotate("", tip, tip - d * 0.08, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    seg(ax, C, D)
    ax.add_patch(plt.Circle(c, r, fill=False, color=ACC, lw=1.6))
    pts = {"O": O, "A": A, "B": B, "C": C, "D": D, "P": Pt}
    dots(ax, pts, ["A", "B", "C", "D", "P"])
    for n, off in {"O": (-9, 0), "A": (3, 10), "B": (3, -11), "C": (-7, 9), "D": (-7, -10), "P": (8, 0)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5, color=INK)
    finish(ax)
    t.save(fig, "sslc2023_q17_tangents.png")


def sslc2023_q17_or():
    fig, ax = plt.subplots(figsize=(3.4, 2.0))
    A, B, C = P(2.5, 1.7), P(0, 0), P(3.3, 0)
    Pp, Q = A + (B - A) * 0.25, A + (C - A) * 0.25
    for u, v in ((A, B), (B, C), (C, A), (Pp, Q)):
        seg(ax, u, v)
    parallel_marks(ax, [(Pp, Q), (B, C)])
    pts = {"A": A, "B": B, "C": C, "P": Pp, "Q": Q}
    for n, off in {"A": (0, 9), "B": (-8, 0), "C": (8, -2), "P": (-9, 3), "Q": (9, 2)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11, color=INK)
    finish(ax)
    t.save(fig, "sslc2023_q17or_bpt.png")


def sslc2023_q28():
    fig, ax = plt.subplots(figsize=(4.4, 3.8))
    xs = np.linspace(-1.5, 5.5, 50)
    ax.axhline(0, color=INK, lw=1.0)
    ax.axvline(0, color=INK, lw=1.0)
    ax.plot(xs, 4 * xs - 4, color=ACC, lw=1.6, label="$4x - y - 4 = 0$")
    ax.plot(xs, (14 - 3 * xs) / 2, color="#B7791F", lw=1.6, label="$3x + 2y - 14 = 0$")
    ax.add_patch(plt.Polygon([[0, -4], [0, 7], [2, 4]], closed=True, fc="#E9F0F7", ec="none", zorder=0))
    for x, y in ((0, -4), (1, 0), (2, 4), (0, 7), (4, 1)):
        ax.plot(x, y, "o", ms=3.5, color=INK)
    for (x, y), lab, off in (((2, 4), "(2, 4)", (16, 2)), ((0, -4), "(0, −4)", (-20, -2)), ((0, 7), "(0, 7)", (-18, 0)),
                             ((1, 0), "(1, 0)", (14, -10)), ((4, 1), "(4, 1)", (10, 6))):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha="center", fontsize=8.5, color=INK)
    ax.set_xlim(-1.5, 5.5)
    ax.set_ylim(-5.5, 8.5)
    ax.set_xticks(range(-1, 6))
    ax.set_yticks(range(-5, 9))
    ax.grid(True, color="#DDE3EA", lw=0.6)
    ax.tick_params(labelsize=7.5)
    ax.legend(fontsize=8, loc="lower right")
    t.save(fig, "sslc2023_q28_graph.png")


def sslc2022_q15():
    fig, ax = plt.subplots(figsize=(3.8, 2.2))
    O, r = P(0, 0), 0.9
    Cc = P(3.2, 0)
    Q, Pt = tangent_points(Cc, O, r)  # Q above, P below
    Rr = O + P(r, 0)
    B = Cc + (Q - Cc) * (Cc[0] - Rr[0]) / (Cc[0] - Q[0])
    A = Cc + (Pt - Cc) * (Cc[0] - Rr[0]) / (Cc[0] - Pt[0])
    for end in (Q, Pt):
        d = end - Cc
        tip = Cc + d * 1.35
        seg(ax, Cc, tip - d * 0.02)
        ax.annotate("", tip, tip - d * 0.06, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
    seg(ax, A, B)
    circle(ax, O, r)
    pts = {"O": O, "C": Cc, "Q": Q, "P": Pt, "A": A, "B": B, "R": Rr}
    dots(ax, pts, ["C", "Q", "P", "A", "B", "R"])
    for n, off in {"O": (-9, 0), "C": (9, 0), "Q": (-3, 10), "P": (-3, -11), "B": (4, 10), "A": (4, -11),
                   "R": (8, 0)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5, color=INK)
    finish(ax)
    t.save(fig, "sslc2022_q15_tangents.png")


def sslc2022_q17():
    fig, ax = plt.subplots(figsize=(3.6, 2.9))
    B, C = P(0, 0), P(10, 0)
    A = P(1.4, np.sqrt(49 - 1.96))
    I, r = P(3.0, 34.29 / 14), 34.29 / 14
    Rr = B + (A - B) * 3 / 7
    Q = A + (C - A) * 4 / 11
    Pp = P(3, 0)
    for u, v in ((A, B), (B, C), (C, A)):
        seg(ax, u, v)
    circle(ax, I, r, color=ACC)
    ax.plot(*I, "o", ms=0)
    pts = {"A": A, "B": B, "C": C, "P": Pp, "Q": Q, "R": Rr}
    dots(ax, pts, ["P", "Q", "R"])
    for n, off in {"A": (0, 9), "B": (-8, -4), "C": (8, -4), "P": (0, -10), "Q": (7, 6), "R": (-9, 2)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5, color=INK)
    for u, v, txt, off in ((A, Rr, "4 cm", P(-0.9, 0.0)), (Rr, B, "3 cm", P(-0.9, 0.0)), (A, C, "11 cm", P(0.7, 0.5))):
        m = (u + v) / 2 + off
        ax.text(*m, txt, fontsize=9, color=INK, ha="center", va="center")
    finish(ax)
    t.save(fig, "sslc2022_q17_incircle.png")


def sslc2022_q17_or():
    fig, ax = plt.subplots(figsize=(3.8, 1.9))
    O = P(0, 0)
    B, C = P(-3.2, 0), P(1.75, 0)
    A = 2.8 * P(np.cos(np.radians(210)), np.sin(np.radians(210)))
    D = 2.0 * P(np.cos(np.radians(30)), np.sin(np.radians(30)))
    for u, v in ((B, C), (A, D), (A, B), (C, D)):
        seg(ax, u, v)
    pts = {"O": O, "A": A, "B": B, "C": C, "D": D}
    for n, off in {"O": (0, -10), "A": (0, -10), "B": (-8, 2), "C": (8, -2), "D": (4, 9)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5, color=INK)
    finish(ax)
    t.save(fig, "sslc2022_q17or_similar.png")


def sslc2022_q18():
    fig, ax = plt.subplots(figsize=(3.4, 2.4))
    B, A, D, C = P(0, 0), P(4.0, 0), P(4.0, 2.8), P(0, 2.8)
    for u, v in ((B, A), (A, D), (D, C), (C, B)):
        seg(ax, u, v)
    th = np.linspace(np.pi / 2, 3 * np.pi / 2, 60)
    xs, ys = 4.0 + 1.4 * np.cos(th), 1.4 + 1.4 * np.sin(th)
    ax.fill(np.r_[xs, 4.0], np.r_[ys, 0.0], facecolor="none", edgecolor=INK, hatch="////", lw=1.0)
    pts = {"A": A, "B": B, "C": C, "D": D}
    for n, off in {"A": (6, -8), "B": (-6, -8), "C": (-6, 8), "D": (6, 8)}.items():
        ax.annotate(n, pts[n], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5, color=INK)
    ax.text(2.0, -0.3, "40 cm", ha="center", fontsize=9, color=INK)
    ax.text(4.15, 1.4, "28 cm", ha="left", va="center", fontsize=9, color=INK)
    finish(ax)
    t.save(fig, "sslc2022_q18_semicircle.png")


def sslc2022_q28():
    fig, ax = plt.subplots(figsize=(4.4, 3.6))
    xs = np.linspace(-5.5, 4, 50)
    ax.axhline(0, color=INK, lw=1.0)
    ax.axvline(0, color=INK, lw=1.0)
    ax.plot(xs, 3 * xs - 3, color=ACC, lw=1.6, label="$3x - y = 3$")
    ax.plot(xs, (xs + 4) / 2, color="#B7791F", lw=1.6, label="$x - 2y = -4$")
    ax.add_patch(plt.Polygon([[-4, 0], [1, 0], [2, 3]], closed=True, fc="#E9F0F7", ec="none", zorder=0))
    for x, y in ((0, -3), (1, 0), (2, 3), (-4, 0), (0, 2)):
        ax.plot(x, y, "o", ms=3.5, color=INK)
    for (x, y), lab, off in (((2, 3), "(2, 3)", (16, -2)), ((1, 0), "(1, 0)", (14, -10)), ((-4, 0), "(−4, 0)", (-4, -12)),
                             ((0, -3), "(0, −3)", (-20, -4)), ((0, 2), "(0, 2)", (-16, 6))):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha="center", fontsize=8.5, color=INK)
    ax.set_xlim(-5.5, 4)
    ax.set_ylim(-4.5, 5.5)
    ax.set_xticks(range(-5, 5))
    ax.set_yticks(range(-4, 6))
    ax.grid(True, color="#DDE3EA", lw=0.6)
    ax.tick_params(labelsize=7.5)
    ax.legend(fontsize=8, loc="upper left")
    t.save(fig, "sslc2022_q28_graph.png")


def sslc2021_q14():
    fig, ax = plt.subplots(figsize=(3.8, 2.4))
    r1, r2 = 1.0, 0.8
    O1, O2 = P(0, 0), P(r1 + r2, 0)
    Tt = P(r1, 0)
    # external common tangent above both circles
    d = r1 + r2
    s = (r1 - r2) / d
    n = P(s, np.sqrt(1 - s * s))  # unit normal of the tangent line, pointing up
    A, B = O1 + r1 * n, O2 + r2 * n
    u = (B - A) / np.linalg.norm(B - A)
    Pp = A + u * np.dot(Tt - A, u) / 1.0
    # P is where the tangent at T (vertical line x = r1) meets AB
    Pp = A + u * (Tt[0] - A[0]) / u[0]
    circle(ax, O1, r1)
    circle(ax, O2, r2)
    for end, sgn in ((A, -1), (B, 1)):
        tip = end + u * sgn * 0.9
        seg(ax, end, tip - u * sgn * 0.02)
        ax.annotate("", tip, tip - u * sgn * 0.08, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
    seg(ax, A, B)
    seg(ax, Pp, Tt, lw=1.0)
    pts = {"A": A, "B": B, "P": Pp, "T": Tt}
    dots(ax, pts, ["A", "B", "P", "T"])
    for nme, off in {"A": (0, 9), "B": (2, 9), "P": (0, 9), "T": (8, -6)}.items():
        ax.annotate(nme, pts[nme], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5,
                    color=INK)
    finish(ax)
    t.save(fig, "sslc2021_q14_touching_circles.png")


def sslc2021_q15():
    fig, ax = plt.subplots(figsize=(3.2, 2.2))
    A, B, C = P(1.2, 2.2), P(0, 0), P(3.0, 0)
    D, E = A + (B - A) * 0.45, A + (C - A) * 0.45
    for u, v in ((A, B), (B, C), (C, A), (D, E)):
        seg(ax, u, v)
    parallel_marks(ax, [(D, E), (B, C)])
    pts = {"A": A, "B": B, "C": C, "D": D, "E": E}
    for nme, off in {"A": (0, 9), "B": (-8, -2), "C": (8, -2), "D": (-9, 2), "E": (9, 2)}.items():
        ax.annotate(nme, pts[nme], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11,
                    color=INK)
    finish(ax)
    t.save(fig, "sslc2021_q15_bpt.png")


def sslc2021_q17():
    fig, ax = plt.subplots(figsize=(4.0, 2.0))
    O, r = P(3.0, 0), 0.75
    Pp = P(0, 0)
    B_, A_ = tangent_points(Pp, O, r)
    circle(ax, O, r)
    seg(ax, Pp, A_)
    seg(ax, Pp, B_)
    seg(ax, O, A_, lw=1.0)
    seg(ax, O, B_, lw=1.0)
    t.angle(ax, Pp, A_, B_, r=0.6, text="70°", size=8.5, tr=0.95)
    pts = {"P": Pp, "A": A_, "B": B_, "O": O}
    dots(ax, pts, ["A", "B"])
    for nme, off in {"P": (-8, 0), "A": (0, 9), "B": (0, -10), "O": (9, 0)}.items():
        ax.annotate(nme, pts[nme], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5,
                    color=INK)
    finish(ax)
    t.save(fig, "sslc2021_q17_tangents.png")


def sslc2021_q17_or():
    fig, ax = plt.subplots(figsize=(2.6, 2.6))
    B, C = P(0, 0), P(2.0, 0.2)
    A = P(1.0, 2.4)
    D = B + (C - B) * 5 / 9.2
    for u, v in ((A, B), (B, C), (C, A), (A, D)):
        seg(ax, u, v)
    pts = {"A": A, "B": B, "C": C, "D": D}
    for nme, off in {"A": (0, 9), "B": (-8, -4), "C": (8, -2), "D": (0, -10)}.items():
        ax.annotate(nme, pts[nme], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=11,
                    color=INK)
    finish(ax)
    t.save(fig, "sslc2021_q17or_bisector.png")


def sslc2021_q28():
    fig, ax = plt.subplots(figsize=(4.4, 3.6))
    xs = np.linspace(-4, 5, 50)
    ax.axhline(0, color=INK, lw=1.0)
    ax.axvline(0, color=INK, lw=1.0)
    ax.plot(xs, 2 * xs - 4, color=ACC, lw=1.6, label="$2x - y = 4$")
    ax.plot(xs, (xs + 3) / 3, color="#B7791F", lw=1.6, label="$3y - x = 3$")
    for x, y in ((0, -4), (1, -2), (2, 0), (3, 2), (0, 1), (-3, 0)):
        ax.plot(x, y, "o", ms=3.5, color=INK)
    for (x, y), lab, off in (((3, 2), "(3, 2)", (16, -4)), ((0, -4), "(0, −4)", (-20, -2)), ((0, 1), "(0, 1)", (-16, 6)),
                             ((2, 0), "(2, 0)", (14, -10)), ((-3, 0), "(−3, 0)", (0, 8)), ((1, -2), "(1, −2)", (18, -4))):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha="center", fontsize=8.5, color=INK)
    ax.set_xlim(-4, 5)
    ax.set_ylim(-5.5, 5)
    ax.set_xticks(range(-4, 6))
    ax.set_yticks(range(-5, 6))
    ax.grid(True, color="#DDE3EA", lw=0.6)
    ax.tick_params(labelsize=7.5)
    ax.legend(fontsize=8, loc="upper left")
    t.save(fig, "sslc2021_q28_graph.png")


def sslc2020_q17_or():
    fig, ax = plt.subplots(figsize=(4.4, 2.3))
    c, r = P(3.2, 0), 0.9
    Pp = P(0, 0)
    T, S = tangent_points(Pp, c, r)  # S upper, T lower
    Q = c + P(-r, 0)
    C = Pp + (S - Pp) * (Q[0] - Pp[0]) / (S[0] - Pp[0])
    D = Pp + (T - Pp) * (Q[0] - Pp[0]) / (T[0] - Pp[0])
    for end in (S, T):
        d = end - Pp
        tip = Pp + d * 1.45
        seg(ax, Pp, tip - d * 0.02)
        ax.annotate("", tip, tip - d * 0.08, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    seg(ax, C, D)
    ax.add_patch(plt.Circle(c, r, fill=False, color=ACC, lw=1.6))
    pts = {"P": Pp, "S": S, "T": T, "C": C, "D": D, "Q": Q}
    dots(ax, pts, ["S", "T", "C", "D", "Q"])
    for nme, off in {"P": (-9, 0), "S": (3, 10), "T": (3, -11), "C": (-7, 9), "D": (-7, -10), "Q": (8, 0)}.items():
        ax.annotate(nme, pts[nme], textcoords="offset points", xytext=off, ha="center", va="center", fontsize=10.5,
                    color=INK)
    finish(ax)
    t.save(fig, "sslc2020_q17or_tangents.png")


def sslc2020_q28():
    fig, ax = plt.subplots(figsize=(4.2, 4.0))
    xs = np.linspace(-1.5, 5, 50)
    ax.axhline(0, color=INK, lw=1.0)
    ax.axvline(0, color=INK, lw=1.0)
    ax.plot(xs, 11 - 3 * xs, color=ACC, lw=1.6, label="$3x + y - 11 = 0$")
    ax.plot(xs, xs - 1, color="#B7791F", lw=1.6, label="$x - y - 1 = 0$")
    ax.add_patch(plt.Polygon([[0, 11], [0, -1], [3, 2]], closed=True, fc="#E9F0F7", ec="none", zorder=0))
    for x, y in ((2, 5), (3, 2), (4, -1), (1, 0), (0, -1), (0, 11)):
        ax.plot(x, y, "o", ms=3.5, color=INK)
    for (x, y), lab, off in (((3, 2), "(3, 2)", (16, 2)), ((0, 11), "(0, 11)", (20, -2)), ((0, -1), "(0, −1)", (-20, -6)),
                             ((2, 5), "(2, 5)", (16, 2)), ((4, -1), "(4, −1)", (16, 2)), ((1, 0), "(1, 0)", (14, -10))):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha="center", fontsize=8.5, color=INK)
    ax.set_xlim(-1.5, 5)
    ax.set_ylim(-3, 12)
    ax.set_xticks(range(-1, 6))
    ax.set_yticks(range(-3, 13))
    ax.grid(True, color="#DDE3EA", lw=0.6)
    ax.tick_params(labelsize=7.5)
    ax.legend(fontsize=8, loc="upper right")
    t.save(fig, "sslc2020_q28_graph.png")


if __name__ == "__main__":
    sslc2020_q17_or()
    sslc2020_q28()
    sslc2021_q14()
    sslc2021_q15()
    sslc2021_q17()
    sslc2021_q17_or()
    sslc2021_q28()
    sslc2022_q15()
    sslc2022_q17()
    sslc2022_q17_or()
    sslc2022_q18()
    sslc2022_q28()
    sslc2023_q14()
    sslc2023_q15()
    sslc2023_q17()
    sslc2023_q17_or()
    sslc2023_q28()
    sslc2024_q14()
    sslc2024_q15()
    sslc2024_q17()
    sslc2024_q28()
    sslc2025_q35()
    copy_chapter("ch06_fig02_bpt_proof.png", "bpt_proof.png")
    copy_chapter("ch06_fig10_trapezium_diagonals.png", "trapezium_diagonals.png")
    copy_chapter("ch10_fig08_quadrilateral.png", "quadrilateral_circumscribing.png")
    copy_chapter("ch09_fig13_q7_transmission_tower.png", "transmission_tower_on_building.png")
    copy_chapter("ch12_fig08_conical_cavity.png", "cylinder_conical_cavity.png")
    sslc2026_q37()
    sslc2026_q44()
    sslc2026_q45()
    sslc2026_q51()
    sslc2026_q50()
    sslc2026_q52()
