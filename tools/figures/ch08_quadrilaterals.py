"""Figures for Class IX Mathematics, Chapter 8: Quadrilaterals (2026 rationalised book).
Equal sides carry matching tick marks; equal angles carry matching arcs."""
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


def P(o, deg, r):
    return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))


def ang(a, b):
    return math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) % 360


def mid(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def meet(p1, d1, p2, d2):
    """Intersection of line p1 + s*d1 with line p2 + t*d2 (d given as points or direction degrees)."""
    if not isinstance(d1, tuple):
        d1 = (math.cos(math.radians(d1)), math.sin(math.radians(d1)))
    if not isinstance(d2, tuple):
        d2 = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    det = d1[0] * (-d2[1]) - d1[1] * (-d2[0])
    rx, ry = p2[0] - p1[0], p2[1] - p1[1]
    s = (rx * (-d2[1]) - ry * (-d2[0])) / det
    return (p1[0] + s * d1[0], p1[1] + s * d1[1])


def vec(a, b):
    return (b[0] - a[0], b[1] - a[1])


def seg(ax, a, b, color=ACC, lw=1.3, dash=False):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls="--" if dash else "-", solid_capstyle="round")


def poly(ax, pts, color=ACC, fill=None, lw=1.3):
    ax.add_patch(Polygon(pts, closed=True, fill=fill is not None, fc=fill or "none", ec=color, lw=lw))


def lab(ax, p, t, dx=0.0, dy=0.0, color=INK, fs=9):
    ax.text(p[0] + dx, p[1] + dy, t, ha="center", va="center", fontsize=fs, weight="bold", color=color)


def names(ax, pts, labels, d=0.2, centre=None):
    cx = centre[0] if centre else sum(p[0] for p in pts) / len(pts)
    cy = centre[1] if centre else sum(p[1] for p in pts) / len(pts)
    for p, t in zip(pts, labels):
        a = math.atan2(p[1] - cy, p[0] - cx)
        lab(ax, (p[0] + d * math.cos(a), p[1] + d * math.sin(a)), t)


def ticks(ax, a, b, n=1, color=HI, size=0.08, gap=0.05):
    mx, my = mid(a, b)
    L = math.hypot(b[0] - a[0], b[1] - a[1])
    ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    nx, ny = -uy, ux
    for k in range(n):
        off = (k - (n - 1) / 2) * gap
        cx, cy = mx + ux * off, my + uy * off
        ax.plot([cx - nx * size, cx + nx * size], [cy - ny * size, cy + ny * size], color=color, lw=1.1)


def arrows(ax, a, b, n=1, color=HI):
    """Parallel marks (small chevrons) at the middle of segment ab."""
    mx, my = mid(a, b)
    L = math.hypot(b[0] - a[0], b[1] - a[1])
    ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    nx, ny = -uy, ux
    for k in range(n):
        cx, cy = mx + ux * (k * 0.07 - (n - 1) * 0.035), my + uy * (k * 0.07 - (n - 1) * 0.035)
        tip = (cx + ux * 0.05, cy + uy * 0.05)
        ax.plot([cx - ux * 0.03 + nx * 0.06, tip[0], cx - ux * 0.03 - nx * 0.06],
                [cy - uy * 0.03 + ny * 0.06, tip[1], cy - uy * 0.03 - ny * 0.06], color=color, lw=1.1)


def amark(ax, v, p1, p2, n=1, r=0.25, color=HI, label=None, lr=None):
    a1, a2 = ang(v, p1), ang(v, p2)
    d = (a2 - a1) % 360
    if d > 180:
        a1, a2 = a2, a1
        d = 360 - d
    for k in range(n):
        ax.add_patch(Arc(v, 2 * (r + 0.05 * k), 2 * (r + 0.05 * k), theta1=a1, theta2=a1 + d, color=color, lw=1))
    if label:
        q = P(v, a1 + d / 2, lr or r + 0.2)
        ax.text(q[0], q[1], label, ha="center", va="center", fontsize=8.5, color=INK)


def right(ax, v, p1, p2, s=0.12, color=HI):
    u = P(v, ang(v, p1), s); w = P(v, ang(v, p2), s)
    c = (u[0] + w[0] - v[0], u[1] + w[1] - v[1])
    ax.plot([u[0], c[0], w[0]], [u[1], c[1], w[1]], color=color, lw=1)


def dot(ax, p, color=INK):
    ax.plot([p[0]], [p[1]], "o", color=color, ms=2.6)


def finish(ax, title=None, pad=0.3):
    ax.set_aspect("equal"); ax.axis("off")
    ax.autoscale_view()
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    ax.set_xlim(x0 - pad, x1 + pad); ax.set_ylim(y0 - pad, y1 + pad)
    if title:
        ax.set_title(title, fontsize=8.5, color=MUTED)


PA, PB, PC, PD = (0, 0), (3.0, 0), (3.9, 1.7), (0.9, 1.7)


def para(ax, pts=(PA, PB, PC, PD), lb="ABCD", marks=True):
    poly(ax, list(pts)); names(ax, list(pts), list(lb))
    if marks:
        arrows(ax, pts[0], pts[1], 1); arrows(ax, pts[3], pts[2], 1); arrows(ax, pts[0], pts[3], 2); arrows(ax, pts[1], pts[2], 2)


# ------------------------------------------------------------------ lesson figures
def fig_types():
    fig, axs = plt.subplots(1, 6, figsize=(7.6, 1.6))
    shapes = [
        ("Trapezium", [(0, 0), (2.0, 0), (1.5, 1.1), (0.4, 1.1)]),
        ("Parallelogram", [(0, 0), (1.6, 0), (2.2, 1.1), (0.6, 1.1)]),
        ("Rectangle", [(0, 0), (2.0, 0), (2.0, 1.1), (0, 1.1)]),
        ("Rhombus", [(0, 0), (1.3, 0), (1.3 + 1.3 * math.cos(math.radians(60)), 1.3 * math.sin(math.radians(60))), (1.3 * math.cos(math.radians(60)), 1.3 * math.sin(math.radians(60)))]),
        ("Square", [(0, 0), (1.2, 0), (1.2, 1.2), (0, 1.2)]),
        ("Kite", [(0.8, -0.2), (1.6, 0.8), (0.8, 1.4), (0.0, 0.8)]),
    ]
    for ax, (t, pts) in zip(axs, shapes):
        poly(ax, pts, fill=SOFT)
        if t in ("Parallelogram", "Rectangle"):
            ticks(ax, pts[0], pts[1], 1); ticks(ax, pts[3], pts[2], 1); ticks(ax, pts[0], pts[3], 2); ticks(ax, pts[1], pts[2], 2)
        if t in ("Rhombus", "Square"):
            for i in range(4):
                ticks(ax, pts[i], pts[(i + 1) % 4], 1)
        if t in ("Rectangle", "Square"):
            for i in range(4):
                right(ax, pts[i], pts[(i + 1) % 4], pts[i - 1], s=0.1)
        if t == "Trapezium":
            arrows(ax, pts[0], pts[1]); arrows(ax, pts[3], pts[2])
        if t == "Kite":
            ticks(ax, pts[1], pts[2], 1); ticks(ax, pts[3], pts[2], 1); ticks(ax, pts[0], pts[1], 2); ticks(ax, pts[0], pts[3], 2)
        finish(ax, t, pad=0.15)
    save(fig, "ch08_fig01_types_of_quadrilaterals.png")


def fig_parallelogram():
    fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.0))
    ax = axs[0]
    para(ax); seg(ax, PA, PC, color=HI)
    amark(ax, PA, PB, PC, 1, r=0.45); amark(ax, PC, PD, PA, 1, r=0.45)
    amark(ax, PA, PC, PD, 2, r=0.3); amark(ax, PC, PA, PB, 2, r=0.3)
    finish(ax, "Diagonal AC: $\\triangle ABC \\cong \\triangle CDA$")
    ax = axs[1]
    para(ax, marks=False); seg(ax, PA, PC, color=HI); seg(ax, PB, PD, color=HI)
    O = mid(PA, PC); lab(ax, O, "O", dy=-0.2)
    ticks(ax, PA, PB, 1); ticks(ax, PD, PC, 1); ticks(ax, PA, PD, 2); ticks(ax, PB, PC, 2)
    ticks(ax, PA, O, 3, size=0.06); ticks(ax, O, PC, 3, size=0.06)
    finish(ax, "Opposite sides equal; diagonals bisect each other")
    save(fig, "ch08_fig02_parallelogram_properties.png")


def fig_example3():
    fig, ax = plt.subplots(figsize=(3.2, 2.4))
    A, B, C = (1.0, 1.8), (0, 0), (2.0, 0)
    Pp = lerp(B, A, 1.5); D = (3.0, 1.8)
    poly(ax, [A, B, C]); seg(ax, A, Pp); seg(ax, A, D, color=HI); seg(ax, C, D, color=HI)
    ticks(ax, A, B, 1); ticks(ax, A, C, 1)
    amark(ax, A, Pp, D, 1, r=0.3); amark(ax, A, D, C, 1, r=0.36)
    for p, t, dx, dy in [(A, "A", -0.15, 0.1), (B, "B", -0.15, -0.1), (C, "C", 0.05, -0.2), (D, "D", 0.15, 0.1), (Pp, "P", -0.12, 0.1)]:
        lab(ax, p, t, dx, dy)
    finish(ax)
    save(fig, "ch08_fig03_example3.png")


def fig_example4():
    fig, ax = plt.subplots(figsize=(4.2, 2.6))
    A, C = (0.9, 1.6), (0.0, 0.0)
    up = ang(C, A)
    seg(ax, (-2.0, 1.6), (2.8, 1.6)); seg(ax, (-2.0, 0), (2.8, 0))
    seg(ax, P(C, up + 180, 0.4), P(A, up, 0.4), color=MUTED)
    lab(ax, (-2.15, 1.6), "P"); lab(ax, (2.95, 1.6), "S"); lab(ax, (-2.15, 0), "Q"); lab(ax, (2.95, 0), "R")
    lab(ax, (3.2, 1.6), "l", color=MUTED); lab(ax, (3.2, 0), "m", color=MUTED); lab(ax, P(A, up, 0.55), "p", color=MUTED)
    # bisectors: angle PAC (A->left 180, A->C) and ACQ (C->left 180, C->A)
    dAC = ang(A, C)
    bPAC = (180 + dAC) / 2; bSAC = (dAC + 360) / 2
    bACQ = (up + 180) / 2; bACR = up / 2
    B = meet(A, bPAC, C, bACQ); D = meet(A, bSAC, C, bACR)
    poly(ax, [A, B, C, D], color=HI)
    amark(ax, A, (-1, 1.6), B, 1, r=0.3); amark(ax, A, B, C, 1, r=0.36)
    amark(ax, C, (-1, 0), B, 2, r=0.3); amark(ax, C, B, A, 2, r=0.36)
    for p, t, dx, dy in [(A, "A", 0.1, 0.18), (C, "C", -0.1, -0.18), (B, "B", -0.2, 0), (D, "D", 0.2, 0)]:
        lab(ax, p, t, dx, dy)
    finish(ax)
    save(fig, "ch08_fig04_example4.png")


def fig_example5():
    fig, ax = plt.subplots(figsize=(4.0, 2.2))
    A, B, C, D = (0, 0), (3.2, 0), (4.2, 1.6), (1.0, 1.6)
    poly(ax, [A, B, C, D]); names(ax, [A, B, C, D], list("ABCD"))
    bis = {}
    for v, a, b in [(A, B, D), (B, C, A), (C, D, B), (D, A, C)]:
        a1, a2 = ang(v, a), ang(v, b)
        d = (a2 - a1) % 360
        if d > 180:
            a1, d = a2, 360 - d
        bis[v] = a1 + d / 2
    Pp = meet(A, bis[A], B, bis[B]); Q = meet(B, bis[B], C, bis[C]); R = meet(C, bis[C], D, bis[D]); S = meet(D, bis[D], A, bis[A])
    # draw bisector segments from each vertex to the farther intersection point on it
    for v, pts in [(A, (Pp, S)), (B, (Pp, Q)), (C, (Q, R)), (D, (R, S))]:
        far = max(pts, key=lambda q: math.hypot(q[0] - v[0], q[1] - v[1]))
        seg(ax, v, far, color=HI, lw=1.1)
    poly(ax, [Pp, Q, R, S], color=HI, fill=SOFT, lw=1.4)
    for p, t in [(Pp, "P"), (Q, "Q"), (R, "R"), (S, "S")]:
        lab(ax, p, t, dx=0.0, dy=0.18 if t in "PS" else -0.18)
    finish(ax)
    save(fig, "ch08_fig05_example5.png")


def fig_example6():
    fig, ax = plt.subplots(figsize=(4.0, 2.2))
    A, B, C, D = PA, PB, PC, PD
    Pp = mid(A, B); Q = mid(D, C)
    para(ax, marks=False)
    for a, b in [(A, Q), (D, Pp), (B, Q), (C, Pp)]:
        seg(ax, a, b, color=HI)
    S = meet(A, vec(A, Q), D, vec(D, Pp)); R = meet(B, vec(B, Q), C, vec(C, Pp))
    ticks(ax, A, Pp, 1); ticks(ax, Pp, B, 1); ticks(ax, D, Q, 1); ticks(ax, Q, C, 1)
    lab(ax, Pp, "P", dy=-0.2); lab(ax, Q, "Q", dy=0.2); lab(ax, S, "S", dx=-0.2); lab(ax, R, "R", dx=0.2)
    finish(ax)
    save(fig, "ch08_fig06_example6.png")


def fig_midpoint_theorems():
    fig, axs = plt.subplots(1, 2, figsize=(6.0, 2.4))
    A, B, C = (1.0, 2.0), (0, 0), (2.6, 0)
    ax = axs[0]
    E = mid(A, B); F = mid(A, C); D = (F[0] * 2 - E[0], F[1] * 2 - E[1])
    poly(ax, [A, B, C]); seg(ax, E, D, color=HI); seg(ax, C, D, color=HI, dash=True)
    ticks(ax, A, E, 1); ticks(ax, E, B, 1); ticks(ax, A, F, 2); ticks(ax, F, C, 2)
    for p, t, dx, dy in [(A, "A", 0, 0.18), (B, "B", -0.15, -0.1), (C, "C", 0.15, -0.1), (E, "E", -0.2, 0), (F, "F", 0.02, 0.2), (D, "D", 0.18, 0.05)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Theorem 8.9")
    ax = axs[1]
    E = mid(A, B); F = mid(A, C); D = (E[0] + 2.6, E[1])
    poly(ax, [A, B, C]); seg(ax, (E[0] - 0.4, E[1]), (D[0] + 0.3, D[1]), color=HI); seg(ax, C, D, color=MUTED, dash=True)
    ticks(ax, A, E, 1); ticks(ax, E, B, 1)
    lab(ax, (D[0] + 0.45, D[1]), "l", color=HI)
    for p, t, dx, dy in [(A, "A", 0, 0.18), (B, "B", -0.15, -0.1), (C, "C", 0.15, -0.1), (E, "E", -0.2, 0.1), (F, "F", 0.05, 0.2), (D, "D", 0.0, 0.2)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Theorem 8.10")
    save(fig, "ch08_fig07_midpoint_theorems.png")


def fig_ex7_ex8():
    fig, axs = plt.subplots(1, 2, figsize=(6.2, 2.6))
    ax = axs[0]
    A, B, C = (1.1, 2.0), (0, 0), (2.8, 0)
    D, E, F = mid(A, B), mid(B, C), mid(C, A)
    poly(ax, [A, B, C]); poly(ax, [D, E, F], color=HI, fill=SOFT)
    for p, t, dx, dy in [(A, "A", 0, 0.18), (B, "B", -0.15, -0.1), (C, "C", 0.15, -0.1), (D, "D", -0.2, 0), (E, "E", 0, -0.2), (F, "F", 0.2, 0.02)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Example 7: D, E, F are mid-points")
    ax = axs[1]
    ys = [1.8, 0.9, 0.0]
    for y, n in zip(ys, "lmn"):
        seg(ax, (-0.4, y), (3.4, y)); lab(ax, (3.6, y), n, color=MUTED)
    Ap, Bp, Cp = (0.3, 1.8), (0.65, 0.9), (1.0, 0.0)
    Dq, Eq, Fq = (2.9, 1.8), (2.2, 0.9), (1.5, 0.0)
    seg(ax, lerp(Ap, Cp, -0.15), lerp(Ap, Cp, 1.15), color=HI); seg(ax, lerp(Dq, Fq, -0.15), lerp(Dq, Fq, 1.15), color=HI)
    seg(ax, Ap, Fq, color=MUTED, dash=True)
    G = meet(Ap, vec(Ap, Fq), (0, 0.9), (1, 0))
    ticks(ax, Ap, Bp, 1); ticks(ax, Bp, Cp, 1)
    for p, t, dx, dy in [(Ap, "A", 0.2, 0.15), (Bp, "B", -0.18, 0.12), (Cp, "C", -0.18, -0.15), (Dq, "D", -0.2, 0.15), (Eq, "E", 0.2, 0.12), (Fq, "F", 0.2, -0.15), (G, "G", 0.08, 0.18)]:
        lab(ax, p, t, dx, dy)
    lab(ax, lerp(Ap, Cp, -0.2), "p", dx=-0.15, color=HI); lab(ax, lerp(Dq, Fq, -0.2), "q", dx=0.15, color=HI)
    finish(ax, "Example 8: $l \\parallel m \\parallel n$, $AB = BC$")
    save(fig, "ch08_fig08_examples7_8.png")


# ------------------------------------------------------------------ Exercise 8.1
def ex81():
    fig, axs = plt.subplots(2, 2, figsize=(6.0, 4.4))
    # Q5: diagonal AC bisects angle A (a rhombus)
    ax = axs[0][0]
    A = (0, 0); B = (2.0, 0); D = P(A, 65, 2.0); C = (B[0] + D[0], D[1])
    poly(ax, [A, B, C, D]); seg(ax, A, C, color=HI); names(ax, [A, B, C, D], list("ABCD"))
    amark(ax, A, B, C, 1, r=0.35); amark(ax, A, C, D, 1, r=0.42)
    finish(ax, "Q5")
    # Q8: P and Q on diagonal BD with DP = BQ
    ax = axs[0][1]
    A, B, C, D = PA, PB, PC, PD
    para(ax, marks=False); seg(ax, B, D, color=MUTED)
    Pp = lerp(D, B, 0.28); Q = lerp(B, D, 0.28)
    for a, b in [(A, Pp), (Pp, C), (C, Q), (Q, A)]:
        seg(ax, a, b, color=HI)
    ticks(ax, D, Pp, 1); ticks(ax, B, Q, 1)
    lab(ax, Pp, "P", dx=0.02, dy=0.22); lab(ax, Q, "Q", dx=0.0, dy=-0.22)
    finish(ax, "Q8")
    # Q9: AP and CQ perpendicular to BD
    ax = axs[1][0]
    A, B, C, D = (0, 0), (2.6, 0), (3.4, 1.7), (0.8, 1.7)
    para(ax, (A, B, C, D), marks=False); seg(ax, B, D, color=MUTED)
    def foot(p, a, b):
        dx, dy = b[0] - a[0], b[1] - a[1]
        k = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)
        return (a[0] + k * dx, a[1] + k * dy)
    Pf = foot(A, B, D); Qf = foot(C, B, D)
    seg(ax, A, Pf, color=HI); seg(ax, C, Qf, color=HI); right(ax, Pf, B, A, s=0.1); right(ax, Qf, D, C, s=0.1)
    lab(ax, Pf, "P", dx=0.08, dy=0.2); lab(ax, Qf, "Q", dx=-0.08, dy=-0.2)
    finish(ax, "Q9")
    # Q11: trapezium ABCD with AB || CD and AD = BC; CE || DA meets AB produced at E
    ax = axs[1][1]
    A, B = (0.7, 0), (2.3, 0); D, C = (0, 1.4), (3.0, 1.4); E = (C[0] + (A[0] - D[0]), 0)
    poly(ax, [A, B, C, D]); seg(ax, B, (E[0] + 0.2, 0)); seg(ax, C, E, color=HI, dash=True)
    seg(ax, A, C, color=MUTED, lw=0.9); seg(ax, B, D, color=MUTED, lw=0.9)
    ticks(ax, A, D, 1); ticks(ax, B, C, 1)
    for p, t, dx, dy in [(A, "A", -0.15, -0.12), (B, "B", 0.05, -0.2), (C, "C", 0.12, 0.15), (D, "D", -0.12, 0.15), (E, "E", 0.1, -0.2)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q11")
    save(fig, "ch08_fig09_exercise_8_1.png")


def ex81_q10():
    fig, ax = plt.subplots(figsize=(4.4, 2.4))
    A, B, C = (0.6, 1.4), (0, 0), (1.6, 0.1)
    t = (2.2, 0.5)
    D, E, F = [(p[0] + t[0], p[1] + t[1]) for p in (A, B, C)]
    poly(ax, [A, B, C]); poly(ax, [D, E, F])
    for a, b in [(A, D), (B, E), (C, F)]:
        seg(ax, a, b, color=HI, dash=True)
    ticks(ax, A, B, 1); ticks(ax, D, E, 1); ticks(ax, B, C, 2); ticks(ax, E, F, 2)
    for p, t_, dx, dy in [(A, "A", -0.1, 0.15), (B, "B", -0.15, -0.1), (C, "C", 0.05, -0.2), (D, "D", -0.05, 0.18), (E, "E", -0.05, -0.2), (F, "F", 0.15, -0.1)]:
        lab(ax, p, t_, dx, dy)
    finish(ax, "Ex 8.1 Q10: $AB \\parallel DE$, $AB = DE$, $BC \\parallel EF$, $BC = EF$")
    save(fig, "ch08_fig10_exercise_8_1_q10.png")


# ------------------------------------------------------------------ Exercise 8.2
def ex82():
    fig, axs = plt.subplots(2, 2, figsize=(6.0, 4.4))
    # Q1 (and Q6): quadrilateral with mid-points and diagonal AC
    ax = axs[0][0]
    A, B, C, D = (0, 0), (2.8, 0.2), (2.3, 1.9), (0.4, 1.5)
    Pp, Q, R, S = mid(A, B), mid(B, C), mid(C, D), mid(D, A)
    poly(ax, [A, B, C, D]); poly(ax, [Pp, Q, R, S], color=HI); seg(ax, A, C, color=MUTED, dash=True)
    names(ax, [A, B, C, D], list("ABCD"))
    for p, t, dx, dy in [(Pp, "P", 0, -0.2), (Q, "Q", 0.2, 0), (R, "R", 0, 0.2), (S, "S", -0.2, 0)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q1 (also Q6)")
    # Q2 and Q3: rhombus and rectangle with mid-points
    ax = axs[0][1]
    A, B, C, D = (0, 0.9), (1.3, 0), (2.6, 0.9), (1.3, 1.8)
    poly(ax, [A, B, C, D]); poly(ax, [mid(A, B), mid(B, C), mid(C, D), mid(D, A)], color=HI)
    seg(ax, A, C, color=MUTED, dash=True); seg(ax, B, D, color=MUTED, dash=True)
    names(ax, [A, B, C, D], list("ABCD"))
    for p, t in [(mid(A, B), "P"), (mid(B, C), "Q"), (mid(C, D), "R"), (mid(D, A), "S")]:
        lab(ax, p, t, dx=0.15 if t in "QR" else -0.15, dy=0.12 if t in "RS" else -0.12)
    finish(ax, "Q2: rhombus ABCD")
    # Q4: trapezium with E mid-point of AD and EF || AB
    ax = axs[1][0]
    A, B = (0, 0), (3.0, 0); D, C = (0.6, 1.6), (2.0, 1.6)
    E = mid(A, D); F = mid(B, C); G = mid(B, D)
    poly(ax, [A, B, C, D]); seg(ax, B, D, color=MUTED); seg(ax, E, F, color=HI)
    ticks(ax, A, E, 1); ticks(ax, E, D, 1)
    for p, t, dx, dy in [(A, "A", -0.15, -0.1), (B, "B", 0.15, -0.1), (C, "C", 0.12, 0.12), (D, "D", -0.12, 0.12), (E, "E", -0.2, 0), (F, "F", 0.2, 0), (G, "G", 0.05, 0.18)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q4")
    # Q5: parallelogram with E, F mid-points of AB, CD; AF and EC meet BD at P and Q
    ax = axs[1][1]
    A, B, C, D = PA, PB, PC, PD
    E = mid(A, B); F = mid(D, C)
    para(ax, marks=False); seg(ax, B, D, color=MUTED); seg(ax, A, F, color=HI); seg(ax, E, C, color=HI)
    Pp = meet(A, vec(A, F), D, vec(D, B)); Q = meet(E, vec(E, C), D, vec(D, B))
    ticks(ax, A, E, 1); ticks(ax, E, B, 1); ticks(ax, D, F, 2); ticks(ax, F, C, 2)
    lab(ax, E, "E", dy=-0.2); lab(ax, F, "F", dy=0.2); lab(ax, Pp, "P", dx=-0.18, dy=0.05); lab(ax, Q, "Q", dx=0.2, dy=-0.02)
    finish(ax, "Q5")
    save(fig, "ch08_fig11_exercise_8_2.png")


def ex82_q7():
    fig, axs = plt.subplots(1, 2, figsize=(5.4, 2.2))
    ax = axs[0]
    A, B, C, D = (0, 1.6), (2.8, 1.6), (2.8, 0), (0, 0)
    poly(ax, [A, B, C, D]); poly(ax, [mid(A, B), mid(B, C), mid(C, D), mid(D, A)], color=HI)
    names(ax, [D, C, B, A], list("ABCD"))
    for p, t, dx, dy in [(mid(D, C), "P", 0, -0.2), (mid(C, B), "Q", 0.2, 0), (mid(B, A), "R", 0, 0.2), (mid(A, D), "S", -0.2, 0)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q3: rectangle ABCD")
    ax = axs[1]
    C, B, A = (0, 0), (2.6, 0), (0, 1.9)
    M = mid(A, B); D = (0, M[1])
    poly(ax, [A, B, C]); seg(ax, M, D, color=HI); seg(ax, C, M, color=MUTED, dash=True)
    right(ax, C, A, B); ticks(ax, A, M, 1); ticks(ax, M, B, 1)
    for p, t, dx, dy in [(A, "A", -0.15, 0.1), (B, "B", 0.15, -0.1), (C, "C", -0.15, -0.1), (M, "M", 0.12, 0.15), (D, "D", -0.18, 0)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q7: $MD \\parallel BC$")
    save(fig, "ch08_fig12_exercise_8_2_q3_q7.png")


if __name__ == "__main__":
    fig_types(); fig_parallelogram(); fig_example3(); fig_example4(); fig_example5(); fig_example6()
    fig_midpoint_theorems(); fig_ex7_ex8(); ex81(); ex81_q10(); ex82(); ex82_q7()
