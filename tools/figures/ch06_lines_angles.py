"""Figures for Class IX Mathematics, Chapter 6: Lines and Angles.
All exercise figures are redrawn so that their angles match the textbook's answers."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Polygon

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "CLASS IX Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, MUTED = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#5D6B7A"
plt.rcParams.update({"font.size": 9, "mathtext.fontset": "cm"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def pt(o, deg, r):
    return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))


def ray(ax, o, deg, r, name=None, color=ACC, lw=1.3, arrow=False, lab_r=None, dash=False):
    e = pt(o, deg, r)
    if arrow:
        ax.annotate("", xy=e, xytext=o, arrowprops=dict(arrowstyle="-|>", color=color, lw=lw))
    else:
        ax.plot([o[0], e[0]], [o[1], e[1]], color=color, lw=lw, ls="--" if dash else "-")
    if name:
        lp = pt(o, deg, (lab_r or r + 0.22))
        ax.text(lp[0], lp[1], name, ha="center", va="center", fontsize=9, weight="bold", color=INK)
    return e


def line(ax, a, b, color=ACC, lw=1.3, ext=0.0, arrows=False, dash=False):
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    p = (a[0] - ux * ext, a[1] - uy * ext); q = (b[0] + ux * ext, b[1] + uy * ext)
    if arrows:
        ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="<|-|>", color=color, lw=lw))
    else:
        ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, ls="--" if dash else "-")


def arc(ax, o, a1, a2, r=0.35, label=None, color=HI, lr=None, fs=9, la=None):
    """Angle mark from direction a1 to a2 (degrees, counter-clockwise)."""
    a1 %= 360; a2 %= 360
    while a2 <= a1:
        a2 += 360
    ax.add_patch(Arc(o, 2 * r, 2 * r, theta1=a1, theta2=a2, color=color, lw=1))
    if label:
        mid = (a1 + a2) / 2 if la is None else la
        p = pt(o, mid, lr or r + 0.2)
        ax.text(p[0], p[1], label, ha="center", va="center", fontsize=fs, color=INK)


def right_mark(ax, o, d1, s=0.14, color=HI):
    a = pt(o, d1, s); c = pt(o, d1 + 90, s); b = (a[0] + c[0] - o[0], a[1] + c[1] - o[1])
    ax.plot([a[0], b[0], c[0]], [a[1], b[1], c[1]], color=color, lw=1)


def label(ax, p, t, dx=0, dy=0, color=INK):
    ax.text(p[0] + dx, p[1] + dy, t, ha="center", va="center", fontsize=9, weight="bold", color=color)


def finish(ax, xlim=None, ylim=None, title=None):
    if xlim: ax.set_xlim(*xlim)
    if ylim: ax.set_ylim(*ylim)
    ax.set_aspect("equal"); ax.axis("off")
    if title: ax.set_title(title, fontsize=8.5, color=MUTED)


# ------------------------------------------------------------------ lesson figures
def fig_basic_terms():
    fig, axs = plt.subplots(1, 3, figsize=(6.6, 1.2))
    a = axs[0]; a.plot([0, 2], [0, 0], color=ACC, lw=1.6); label(a, (0, 0.25), "A"); label(a, (2, 0.25), "B")
    a.plot([0, 2], [0, 0], "o", color=INK, ms=3); finish(a, (-0.3, 2.3), (-0.3, 0.5), "Line segment AB")
    a = axs[1]; a.annotate("", xy=(2.2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=ACC, lw=1.4))
    a.plot([0], [0], "o", color=INK, ms=3); label(a, (0, 0.25), "A"); label(a, (1.4, 0.25), "B")
    a.plot([1.4], [0], "o", color=INK, ms=3); finish(a, (-0.3, 2.4), (-0.3, 0.5), "Ray AB")
    a = axs[2]; a.annotate("", xy=(2.3, 0), xytext=(-0.3, 0), arrowprops=dict(arrowstyle="<|-|>", color=ACC, lw=1.4))
    for x, n in [(0.5, "A"), (1.5, "B")]:
        a.plot([x], [0], "o", color=INK, ms=3); label(a, (x, 0.25), n)
    finish(a, (-0.5, 2.5), (-0.3, 0.5), "Line AB")
    save(fig, "ch06_fig01_basic_terms.png")


def fig_angle_types():
    fig, axs = plt.subplots(1, 5, figsize=(7.0, 1.7))
    data = [(40, "acute\n$0^\\circ < x < 90^\\circ$"), (90, "right\n$y = 90^\\circ$"), (130, "obtuse\n$90^\\circ < z < 180^\\circ$"),
            (180, "straight\n$s = 180^\\circ$"), (240, "reflex\n$180^\\circ < t < 360^\\circ$")]
    for a, (deg, t) in zip(axs, data):
        o = (0, 0)
        ray(a, o, 0, 1.0); ray(a, o, deg, 1.0)
        if deg == 90:
            right_mark(a, o, 0, 0.18)
        else:
            arc(a, o, 0, deg, r=0.3)
        a.set_title(t, fontsize=7.5, color=INK, y=-0.45)
        finish(a, (-1.1, 1.1), (-1.0, 1.1))
    save(fig, "ch06_fig02_angle_types.png")


def fig_pairs():
    fig, axs = plt.subplots(1, 3, figsize=(6.8, 2.0))
    a = axs[0]; B = (0, 0)
    ray(a, B, 15, 1.2, "A"); ray(a, B, 70, 1.2, "D"); ray(a, B, 150, 1.2, "C"); label(a, (0, -0.2), "B")
    arc(a, B, 15, 70, r=0.35, color=ACC); arc(a, B, 70, 150, r=0.45)
    finish(a, (-1.3, 1.4), (-0.4, 1.4), "Adjacent angles ABD and DBC")
    a = axs[1]; O = (0, 0)
    ray(a, O, 0, 1.2, "B"); ray(a, O, 180, 1.2, "A"); ray(a, O, 60, 1.2, "C"); label(a, (0, -0.2), "O")
    arc(a, O, 0, 60, r=0.3, color=ACC); arc(a, O, 60, 180, r=0.4)
    finish(a, (-1.5, 1.5), (-0.4, 1.3), "Linear pair AOC and COB")
    a = axs[2]; O = (0, 0)
    for d, n in [(25, "B"), (205, "A"), (120, "D"), (300, "C")]:
        ray(a, O, d, 1.2, n)
    arc(a, O, 25, 120, r=0.3, color=ACC); arc(a, O, 205, 300, r=0.3, color=ACC)
    arc(a, O, 120, 205, r=0.42); arc(a, O, 300, 385, r=0.42)
    label(a, (0.25, -0.02), "O")
    finish(a, (-1.4, 1.4), (-1.3, 1.3), "Vertically opposite angles")
    save(fig, "ch06_fig03_angle_pairs.png")


def fig_intersecting_parallel():
    fig, axs = plt.subplots(1, 2, figsize=(5.8, 1.9))
    a = axs[0]
    line(a, (-1.2, -0.6), (1.2, 0.6), arrows=True); line(a, (-1.2, 0.6), (1.2, -0.6), arrows=True)
    label(a, (-1.35, -0.72), "P"); label(a, (1.35, 0.72), "Q"); label(a, (-1.35, 0.72), "R"); label(a, (1.35, -0.72), "S")
    finish(a, (-1.6, 1.6), (-1.0, 1.0), "Intersecting lines")
    a = axs[1]
    line(a, (-1.2, 0.5), (1.2, 0.5), arrows=True); line(a, (-1.2, -0.5), (1.2, -0.5), arrows=True)
    label(a, (-1.4, 0.5), "P"); label(a, (1.4, 0.5), "Q"); label(a, (-1.4, -0.5), "R"); label(a, (1.4, -0.5), "S")
    for x in (-0.6, 0.6):
        a.plot([x, x], [-0.5, 0.5], color=HI, lw=0.9, ls="--")
    a.text(0.72, 0.0, "equal\ndistance", fontsize=7, color=MUTED, va="center")
    finish(a, (-1.6, 1.8), (-1.0, 1.0), "Non-intersecting (parallel) lines")
    save(fig, "ch06_fig04_intersecting_parallel.png")


def fig_transversal():
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    P, Q = (0.35, 1.0), (-0.35, -1.0)
    line(ax, (-2, 1.0), (2, 1.0), arrows=True); line(ax, (-2, -1.0), (2, -1.0), arrows=True)
    line(ax, (0.7, 2.0), (-0.7, -2.0), color=HI, arrows=True)
    up = math.degrees(math.atan2(1.0, 0.35))  # direction of transversal going up
    dn = up + 180
    # angles at P: 1 (between right and up), 2 (up and left), 3 (left and down), 4 (down and right)
    for o, labels in [(P, ("1", "2", "3", "4")), (Q, ("5", "6", "7", "8"))]:
        dirs = [0, up, 180, dn, 360]
        for k in range(4):
            mid = (dirs[k] + dirs[k + 1]) / 2
            p = pt(o, mid, 0.42)
            ax.text(p[0], p[1], labels[k], ha="center", va="center", fontsize=9, color=INK)
    label(ax, (2.25, 1.0), "m"); label(ax, (2.25, -1.0), "n"); label(ax, (0.85, 2.05), "l", color=HI)
    finish(ax, (-2.3, 2.5), (-2.2, 2.3))
    save(fig, "ch06_fig05_transversal_angles.png")


def fig_parallel_same_line():
    fig, ax = plt.subplots(figsize=(3.8, 2.8))
    ys = [(1.0, "m"), (0.0, "l"), (-1.0, "n")]
    for y, n in ys:
        line(ax, (-1.6, y), (1.6, y), arrows=True); label(ax, (1.8, y), n)
    line(ax, (0.6, 1.8), (-0.6, -1.8), color=HI, arrows=True); label(ax, (0.75, 1.9), "t", color=HI)
    up = math.degrees(math.atan2(1.8, 0.6))
    for (y, n), k in zip(ys, ("2", "1", "3")):
        x = y / 3.0
        arc(ax, (x, y), 0, up, r=0.28, label=k, lr=0.45)
    finish(ax, (-1.9, 2.0), (-2.0, 2.1))
    save(fig, "ch06_fig06_parallel_to_same_line.png")


def fig_example1():
    fig, ax = plt.subplots(figsize=(3.4, 2.4))
    O = (0, 0)
    ray(ax, O, 0, 1.4, "Q"); ray(ax, O, 180, 1.4, "P"); ray(ax, O, 105, 1.3, "R"); ray(ax, O, 285, 1.3, "S")
    arc(ax, O, 105, 180, r=0.35, label="$5x$", lr=0.6); arc(ax, O, 0, 105, r=0.28, label="$7x$", lr=0.55, color=ACC)
    label(ax, (0.18, -0.2), "O")
    finish(ax, (-1.7, 1.7), (-1.5, 1.5))
    save(fig, "ch06_fig07_example1.png")


def fig_example2():
    fig, ax = plt.subplots(figsize=(3.6, 2.2))
    O = (0, 0); x = 70
    ray(ax, O, 0, 1.5, "Q"); ray(ax, O, 180, 1.5, "P")
    ray(ax, O, 180 - x, 1.4, "S"); ray(ax, O, 180 - x / 2, 1.3, "R", color=HI); ray(ax, O, (180 - x) / 2, 1.3, "T", color=HI)
    arc(ax, O, 180 - x, 180, r=0.4, label="$x$", lr=0.6, la=165)
    label(ax, (0, -0.2), "O")
    finish(ax, (-1.8, 1.8), (-0.4, 1.6))
    save(fig, "ch06_fig08_example2.png")


def fig_example4():
    fig, ax = plt.subplots(figsize=(4.4, 2.8))
    # PQ || RS horizontal; M to the left between them; X on PQ, Y on RS
    X, Y, M = (0.1, 1.0), (-0.9 + 1 / math.tan(math.radians(40)), -1.0), (-0.9, 0.0)
    line(ax, (-1.8, 1.0), (1.8, 1.0), arrows=True); line(ax, (-1.8, -1.0), (1.8, -1.0), arrows=True)
    label(ax, (-2.0, 1.0), "P"); label(ax, (2.0, 1.0), "Q"); label(ax, (-2.0, -1.0), "R"); label(ax, (2.0, -1.0), "S")
    ax.plot([X[0], M[0], Y[0]], [X[1], M[1], Y[1]], color=HI, lw=1.4)
    line(ax, (-1.8, 0.0), (1.2, 0.0), color=ACC, lw=0.9, dash=True)
    label(ax, (-2.0, 0.0), "A", color=MUTED); label(ax, (1.4, 0.0), "B", color=MUTED)
    for p, n, dy in [(X, "X", 0.2), (Y, "Y", -0.2), (M, "M", 0.0)]:
        ax.plot([p[0]], [p[1]], "o", color=INK, ms=3); label(ax, (p[0] + (-0.2 if n == "M" else 0.15), p[1] + dy), n)
    dXM = math.degrees(math.atan2(M[1] - X[1], M[0] - X[0]))
    dYM = math.degrees(math.atan2(M[1] - Y[1], M[0] - Y[0]))
    arc(ax, X, dXM, 360, r=0.3, label="$135^\\circ$", lr=0.62)
    arc(ax, Y, dYM, 180, r=0.3, label="$40^\\circ$", lr=0.55)
    finish(ax, (-2.2, 2.2), (-1.4, 1.4))
    save(fig, "ch06_fig09_example4.png")


def fig_example6():
    fig, ax = plt.subplots(figsize=(3.8, 3.2))
    E = (0, 0)
    ang = 55
    t = math.tan(math.radians(ang))
    yD, yB = 1.0, 2.0
    D = (yD / t, yD); B = (yB / t, yB); A = (0, yB)
    line(ax, (-0.6, 0), (2.4, 0), arrows=True); label(ax, (2.55, 0), "F"); label(ax, (-0.2, -0.2), "E")
    line(ax, (-0.6, yD), (2.4, yD), arrows=True); label(ax, (2.55, yD), "C"); label(ax, (D[0] - 0.12, yD + 0.18), "D")
    line(ax, (-0.6, yB), (2.4, yB), arrows=True); label(ax, (-0.2, yB + 0.18), "A"); label(ax, (B[0] + 0.1, yB + 0.2), "B")
    ax.plot([E[0], B[0] + 0.3], [E[1], B[1] + 0.3 * t], color=HI, lw=1.3)
    ax.plot([0, 0], [0, yB], color=HI, lw=1.3)
    right_mark(ax, A, 270, 0.15)
    arc(ax, E, 0, ang, r=0.35, label="$55^\\circ$", lr=0.6)
    arc(ax, E, ang, 90, r=0.5, label="$z$", lr=0.7)
    arc(ax, D, 180 + ang, 360, r=0.25, label="$y$", lr=0.45)
    arc(ax, B, 180 + ang, 360, r=0.25, label="$x$", lr=0.42)
    finish(ax, (-0.8, 2.8), (-0.4, 2.6))
    save(fig, "ch06_fig10_example6.png")


# ------------------------------------------------------------------ Exercise 6.1
def ex61():
    fig, axs = plt.subplots(2, 3, figsize=(7.2, 4.8))
    # Q1: AB and CD intersect at O; angle BOD = 40, AOC = 40; E with BOE = 30
    a = axs[0][0]; O = (0, 0)
    ray(a, O, 0, 1.3, "B"); ray(a, O, 180, 1.3, "A"); ray(a, O, 140, 1.3, "C"); ray(a, O, 320, 1.3, "D"); ray(a, O, 30, 1.25, "E")
    arc(a, O, 320, 360, r=0.35, label="$40^\\circ$", lr=0.62); arc(a, O, 0, 30, r=0.5); label(a, (0.05, -0.22), "O")
    finish(a, (-1.6, 1.6), (-1.2, 1.2), "Q1")
    # Q2: XY and MN intersect at O; OP perpendicular to XY; a = MOP, b = XOM, c = XON
    a = axs[0][1]; O = (0, 0)
    ray(a, O, 0, 1.3, "Y"); ray(a, O, 180, 1.3, "X"); ray(a, O, 90, 1.2, "P"); ray(a, O, 126, 1.3, "M"); ray(a, O, 306, 1.3, "N")
    right_mark(a, O, 0, 0.15)
    arc(a, O, 90, 126, r=0.45, label="$a$", lr=0.62); arc(a, O, 126, 180, r=0.35, label="$b$", lr=0.55)
    arc(a, O, 180, 306, r=0.3, label="$c$", lr=0.5); label(a, (0.2, -0.2), "O")
    finish(a, (-1.6, 1.6), (-1.2, 1.4), "Q2")
    # Q3: triangle PQR with QR produced to S and T
    a = axs[0][2]
    Q, R, P = (-0.6, 0), (0.6, 0), (0, 1.1)
    a.add_patch(Polygon([P, Q, R], closed=True, fill=False, ec=ACC, lw=1.3))
    a.plot([-1.4, 1.4], [0, 0], color=ACC, lw=1.3)
    label(a, (0, 1.28), "P"); label(a, (-0.6, -0.2), "Q"); label(a, (0.6, -0.2), "R"); label(a, (-1.5, -0.05), "S"); label(a, (1.5, -0.05), "T")
    dQP = math.degrees(math.atan2(1.1, 0.6)); dRP = 180 - dQP
    arc(a, Q, 0, dQP, r=0.22, color=ACC); arc(a, R, dRP, 180, r=0.22, color=ACC)
    finish(a, (-1.7, 1.7), (-0.5, 1.5), "Q3")
    # Q4: rays OA, OB and two others with x, y above and w, z below
    a = axs[1][0]; O = (0, 0)
    ray(a, O, 180, 1.3, "A"); ray(a, O, 0, 1.3, "B"); ray(a, O, 70, 1.2, "C"); ray(a, O, 250, 1.2, "D")
    arc(a, O, 70, 180, r=0.3, label="$x$", lr=0.52); arc(a, O, 0, 70, r=0.3, label="$y$", lr=0.52)
    arc(a, O, 250, 360, r=0.3, label="$z$", lr=0.52); arc(a, O, 180, 250, r=0.3, label="$w$", lr=0.52); label(a, (0.12, 0.62), "O")
    a.plot([0], [0], "o", color=INK, ms=2.5)
    finish(a, (-1.6, 1.6), (-1.4, 1.4), "Q4")
    # Q5: POQ a line, OR perpendicular, OS between OP and OR
    a = axs[1][1]; O = (0, 0)
    ray(a, O, 0, 1.3, "Q"); ray(a, O, 180, 1.3, "P"); ray(a, O, 90, 1.2, "R"); ray(a, O, 135, 1.25, "S")
    right_mark(a, O, 0, 0.15); label(a, (0.05, -0.22), "O")
    finish(a, (-1.6, 1.6), (-0.5, 1.5), "Q5")
    # Q6: angle XYZ = 64, XY produced to P, YQ bisects ZYP
    a = axs[1][2]; Y = (0, 0)
    ray(a, Y, 180, 1.3, "X"); ray(a, Y, 0, 1.3, "P"); ray(a, Y, 116, 1.25, "Z"); ray(a, Y, 58, 1.25, "Q", color=HI)
    arc(a, Y, 116, 180, r=0.35, label="$64^\\circ$", lr=0.62); arc(a, Y, 0, 58, r=0.3, color=ACC); arc(a, Y, 58, 116, r=0.36, color=ACC)
    label(a, (0.05, -0.22), "Y")
    finish(a, (-1.6, 1.6), (-0.5, 1.5), "Q6")
    save(fig, "ch06_fig11_exercise_6_1.png")


# ------------------------------------------------------------------ Exercise 6.2
def ex62():
    fig, axs = plt.subplots(2, 3, figsize=(7.4, 5.2))
    # Q1: AB, CD horizontal; transversal with up-direction 130 degrees
    a = axs[0][0]
    up = 130; Qp, Rp = (0.0, 0.8), (0.0, -0.8)
    Rp = (Qp[0] - 1.6 / math.tan(math.radians(up)), -0.8)
    line(a, (-1.5, 0.8), (1.5, 0.8), arrows=True); line(a, (-1.5, -0.8), (1.5, -0.8), arrows=True)
    label(a, (-1.65, 0.8), "A"); label(a, (1.65, 0.8), "B"); label(a, (-1.65, -0.8), "C"); label(a, (1.65, -0.8), "D")
    e1 = pt(Qp, up, 0.8); e2 = pt(Rp, up + 180, 0.8)
    a.plot([e1[0], e2[0]], [e1[1], e2[1]], color=HI, lw=1.3)
    arc(a, Qp, up, 180, r=0.28, label="$50^\\circ$", lr=0.5)
    arc(a, Qp, 180, up + 180, r=0.3, label="$x$", lr=0.48)
    arc(a, Rp, 0, up, r=0.3, label="$y$", lr=0.48)
    arc(a, Rp, 180, up + 180, r=0.28, label="$130^\\circ$", lr=0.55)
    finish(a, (-1.9, 1.9), (-1.7, 1.7), "Q1")
    # Q2: AB || CD || EF; transversal up-direction 126 degrees
    a = axs[0][1]
    up = 126; ys = [0.9, 0.0, -0.9]
    xs = [y / math.tan(math.radians(up)) for y in ys]
    for y, n1, n2 in zip(ys, "ACE", "BDF"):
        line(a, (-1.5, y), (1.5, y), arrows=True); label(a, (-1.65, y), n1); label(a, (1.65, y), n2)
    e1 = pt((xs[0], ys[0]), up, 0.6); e2 = pt((xs[2], ys[2]), up + 180, 0.6)
    a.plot([e1[0], e2[0]], [e1[1], e2[1]], color=HI, lw=1.3)
    arc(a, (xs[0], ys[0]), 180, up + 180, r=0.26, label="$x$", lr=0.44)
    arc(a, (xs[1], ys[1]), up + 180, 360, r=0.26, label="$y$", lr=0.44)
    arc(a, (xs[2], ys[2]), 0, up, r=0.26, label="$z$", lr=0.44)
    finish(a, (-1.9, 1.9), (-1.6, 1.6), "Q2")
    # Q3: AB || CD, EF perpendicular to CD, angle GED = 126
    a = axs[0][2]
    E = (0.3, -0.8); dirEG = 126
    G = (E[0] + 1.6 / math.tan(math.radians(dirEG)), 0.8); F = (E[0], 0.8)
    line(a, (-1.5, 0.8), (1.5, 0.8), arrows=True); line(a, (-1.5, -0.8), (1.5, -0.8), arrows=True)
    label(a, (-1.65, 0.8), "A"); label(a, (1.65, 0.8), "B"); label(a, (-1.65, -0.8), "C"); label(a, (1.65, -0.8), "D")
    a.plot([E[0], G[0]], [E[1], G[1]], color=HI, lw=1.3); a.plot([E[0], F[0]], [E[1], F[1]], color=HI, lw=1.3)
    label(a, (E[0] + 0.05, E[1] - 0.2), "E"); label(a, (G[0] - 0.05, G[1] + 0.2), "G"); label(a, (F[0] + 0.05, F[1] + 0.2), "F")
    right_mark(a, E, 0, 0.14)
    arc(a, E, 0, dirEG, r=0.42, label="$126^\\circ$", lr=0.66)
    finish(a, (-1.9, 1.9), (-1.4, 1.3), "Q3")
    # Q4: PQ || ST, V shape with R at the bottom: angle PQR = 110, angle RST = 130
    a = axs[1][0]
    R = (0, -1.0); Q = pt(R, 110, 2.0); S = pt(R, 50, 1.6)
    line(a, (Q[0] - 1.2, Q[1]), Q, lw=1.3); line(a, S, (S[0] + 1.2, S[1]), lw=1.3)
    a.plot([Q[0], R[0], S[0]], [Q[1], R[1], S[1]], color=HI, lw=1.3)
    label(a, (Q[0] - 1.3, Q[1]), "P"); label(a, (Q[0] + 0.05, Q[1] + 0.2), "Q"); label(a, (R[0], R[1] - 0.2), "R")
    label(a, (S[0] - 0.05, S[1] + 0.2), "S"); label(a, (S[0] + 1.32, S[1]), "T")
    arc(a, Q, 180, 290, r=0.26, label="$110^\\circ$", lr=0.5)
    arc(a, S, 230, 360, r=0.22, label="$130^\\circ$", lr=0.46)
    line(a, (-1.2, R[1]), (1.2, R[1]), color=MUTED, lw=0.8, dash=True)
    finish(a, (-2.0, 2.4), (-1.5, 1.3), "Q4")
    # Q5: AB || CD; P on AB; Q, R on CD; angle APQ = 50, angle PRD = 127
    a = axs[1][1]
    P = (0.0, 0.8); Qp = pt(P, 230, 1.6 / math.sin(math.radians(50))); Rp = pt(P, 307, 1.6 / math.sin(math.radians(53)))
    line(a, (-2.1, 0.8), (2.0, 0.8), arrows=True); line(a, (-2.1, -0.8), (2.0, -0.8), arrows=True)
    label(a, (-2.25, 0.8), "A"); label(a, (2.15, 0.8), "B"); label(a, (-2.25, -0.8), "C"); label(a, (2.15, -0.8), "D")
    a.plot([Qp[0], P[0], Rp[0]], [Qp[1], P[1], Rp[1]], color=HI, lw=1.3)
    label(a, (P[0], P[1] + 0.2), "P"); label(a, (Qp[0], Qp[1] - 0.2), "Q"); label(a, (Rp[0], Rp[1] - 0.2), "R")
    arc(a, P, 180, 230, r=0.3, label="$50^\\circ$", lr=0.5)
    arc(a, P, 230, 307, r=0.24, label="$y$", lr=0.42)
    arc(a, Qp, 0, 50, r=0.24, label="$x$", lr=0.42)
    arc(a, Rp, 0, 127, r=0.22, label="$127^\\circ$", lr=0.46)
    finish(a, (-2.4, 2.3), (-1.3, 1.2), "Q5")
    # Q6: parallel mirrors PQ (top) and RS (bottom); ray A-B-C-D
    a = axs[1][2]
    B, C = (0.0, 0.8), (0.8, -0.8); A = (-0.55, -0.3); D = (1.35, 0.3)
    line(a, (-1.4, 0.8), (1.8, 0.8), lw=2.0, color=ACC); line(a, (-1.4, -0.8), (1.8, -0.8), lw=2.0, color=ACC)
    label(a, (-1.55, 0.8), "P"); label(a, (1.95, 0.8), "Q"); label(a, (-1.55, -0.8), "R"); label(a, (1.95, -0.8), "S")
    for p, q in [(A, B), (B, C), (C, D)]:
        a.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=HI, lw=1.2))
    a.plot([B[0], B[0]], [0.8, 0.1], color=MUTED, ls="--", lw=0.8); a.plot([C[0], C[0]], [-0.8, -0.1], color=MUTED, ls="--", lw=0.8)
    label(a, (A[0] - 0.12, A[1] - 0.12), "A"); label(a, (B[0], B[1] + 0.2), "B"); label(a, (C[0], C[1] - 0.2), "C"); label(a, (D[0] + 0.12, D[1] + 0.1), "D")
    label(a, (B[0] + 0.12, 0.05), "M", color=MUTED); label(a, (C[0] - 0.12, -0.05), "N", color=MUTED)
    finish(a, (-1.8, 2.2), (-1.2, 1.2), "Q6")
    save(fig, "ch06_fig12_exercise_6_2.png")


def fig_example3():
    fig, ax = plt.subplots(figsize=(3.2, 2.5))
    O = (0, 0)
    ray(ax, O, 0, 1.3, "Q"); ray(ax, O, 80, 1.2, "P"); ray(ax, O, 215, 1.2, "S"); ray(ax, O, 290, 1.2, "R")
    ray(ax, O, 180, 1.3, "T", color=MUTED, dash=True)
    arc(ax, O, 0, 80, r=0.3, color=ACC); arc(ax, O, 80, 215, r=0.36); arc(ax, O, 215, 290, r=0.3, color=ACC); arc(ax, O, 290, 360, r=0.36)
    label(ax, (0.2, 0.16), "O")
    finish(ax, (-1.6, 1.6), (-1.4, 1.5), "TOQ is ray OQ produced backwards")
    save(fig, "ch06_fig13_example3.png")


def fig_example5():
    fig, ax = plt.subplots(figsize=(3.8, 3.0))
    up = 60
    B = (0.0, 0.8); C = (B[0] - 1.6 / math.tan(math.radians(up)), -0.8)
    line(ax, (-2.0, 0.8), (1.6, 0.8), arrows=True); line(ax, (-2.0, -0.8), (1.6, -0.8), arrows=True)
    label(ax, (-2.15, 0.8), "P"); label(ax, (1.75, 0.8), "Q"); label(ax, (-2.15, -0.8), "R"); label(ax, (1.75, -0.8), "S")
    A = pt(B, up, 0.9); D = pt(C, up + 180, 0.7)
    ax.plot([A[0], D[0]], [A[1], D[1]], color=HI, lw=1.3)
    label(ax, (A[0] + 0.1, A[1] + 0.12), "A"); label(ax, (D[0] - 0.1, D[1] - 0.12), "D")
    label(ax, (B[0] - 0.15, B[1] - 0.2), "B"); label(ax, (C[0] - 0.15, C[1] - 0.2), "C")
    ray(ax, B, up / 2, 1.0, "E", color=ACC, lab_r=1.15); ray(ax, C, up / 2, 1.0, "G", color=ACC, lab_r=1.15)
    arc(ax, B, 0, up / 2, r=0.35, color=HI); arc(ax, B, up / 2, up, r=0.42, color=HI)
    arc(ax, C, 0, up / 2, r=0.35, color=HI); arc(ax, C, up / 2, up, r=0.42, color=HI)
    finish(ax, (-2.3, 2.0), (-1.5, 1.8))
    save(fig, "ch06_fig14_example5.png")


def fig_bend():
    fig, ax = plt.subplots(figsize=(3.8, 2.6))
    A = (0.0, 1.0); E = pt(A, 320, 1 / math.sin(math.radians(40)))
    C = (E[0] - 1 / math.tan(math.radians(35)), -1.0)
    line(ax, (-1.4, 1.0), (2.4, 1.0), arrows=True); line(ax, (-1.4, -1.0), (2.4, -1.0), arrows=True)
    ax.plot([A[0], E[0], C[0]], [A[1], E[1], C[1]], color=HI, lw=1.4)
    line(ax, (-0.6, 0.0), E, color=ACC, lw=0.9, dash=True)
    for p, n, dx, dy in [(A, "A", -0.05, 0.2), (C, "C", -0.05, -0.22), (E, "E", 0.2, 0.0)]:
        ax.plot([p[0]], [p[1]], "o", color=INK, ms=3); label(ax, (p[0] + dx, p[1] + dy), n)
    label(ax, (2.6, 1.0), "B"); label(ax, (2.6, -1.0), "D"); label(ax, (-0.8, 0.0), "F", color=MUTED)
    arc(ax, A, 320, 360, r=0.38, label="$40^\\circ$", lr=0.62)
    arc(ax, C, 0, 35, r=0.38, label="$35^\\circ$", lr=0.62)
    arc(ax, E, 140, 215, r=0.3)
    finish(ax, (-1.6, 2.8), (-1.4, 1.4))
    save(fig, "ch06_fig15_bend_between_parallels.png")


def fig_alt_bisectors():
    fig, ax = plt.subplots(figsize=(3.8, 2.8))
    G = (0.0, 0.8); H = pt(G, 300, 1.6 / math.sin(math.radians(60)))
    line(ax, (-1.8, 0.8), (2.2, 0.8), arrows=True); line(ax, (-1.8, -0.8), (2.2, -0.8), arrows=True)
    label(ax, (-1.95, 0.8), "A"); label(ax, (2.35, 0.8), "B"); label(ax, (-1.95, -0.8), "C"); label(ax, (2.35, -0.8), "D")
    Et = pt(G, 120, 0.7); Fb = pt(H, 300, 0.7)
    ax.plot([Et[0], Fb[0]], [Et[1], Fb[1]], color=HI, lw=1.3)
    label(ax, (Et[0] - 0.12, Et[1] + 0.1), "E"); label(ax, (Fb[0] + 0.12, Fb[1] - 0.1), "F")
    label(ax, (G[0] + 0.2, G[1] + 0.18), "G"); label(ax, (H[0] - 0.2, H[1] - 0.2), "H")
    ray(ax, G, 240, 1.1, "M", color=ACC, lab_r=1.25); ray(ax, H, 60, 1.1, "N", color=ACC, lab_r=1.25)
    arc(ax, G, 180, 240, r=0.3); arc(ax, G, 240, 300, r=0.36)
    arc(ax, H, 0, 60, r=0.3); arc(ax, H, 60, 120, r=0.36)
    finish(ax, (-2.1, 2.5), (-1.6, 1.6))
    save(fig, "ch06_fig16_bisectors_of_alternate_angles.png")


if __name__ == "__main__":
    fig_basic_terms(); fig_angle_types(); fig_pairs(); fig_intersecting_parallel(); fig_transversal()
    fig_parallel_same_line(); fig_example1(); fig_example2(); fig_example3(); fig_example4(); fig_example5(); fig_example6(); ex61(); ex62(); fig_bend(); fig_alt_bisectors()
