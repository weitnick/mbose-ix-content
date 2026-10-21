"""Figures for Class IX Mathematics, Chapter 9: Circles (2026 rationalised book)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Polygon, Wedge

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


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def foot(p, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    k = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)
    return (a[0] + k * dx, a[1] + k * dy)


def meet(p1, q1, p2, q2):
    d1 = (q1[0] - p1[0], q1[1] - p1[1]); d2 = (q2[0] - p2[0], q2[1] - p2[1])
    det = d1[0] * (-d2[1]) - d1[1] * (-d2[0])
    rx, ry = p2[0] - p1[0], p2[1] - p1[1]
    s = (rx * (-d2[1]) - ry * (-d2[0])) / det
    return (p1[0] + s * d1[0], p1[1] + s * d1[1])


def circ(ax, O, r, color=ACC, lw=1.3, fill=None, dash=False):
    ax.add_patch(Circle(O, r, fill=fill is not None, fc=fill or "none", ec=color, lw=lw, ls="--" if dash else "-"))


def seg(ax, a, b, color=ACC, lw=1.3, dash=False):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls="--" if dash else "-", solid_capstyle="round")


def poly(ax, pts, color=ACC, fill=None, lw=1.3):
    ax.add_patch(Polygon(pts, closed=True, fill=fill is not None, fc=fill or "none", ec=color, lw=lw))


def lab(ax, p, t, dx=0.0, dy=0.0, color=INK, fs=9):
    ax.text(p[0] + dx, p[1] + dy, t, ha="center", va="center", fontsize=fs, weight="bold", color=color)


def out(ax, O, p, t, d=0.2, color=INK):
    """Label a point on a circle, pushed radially outward from the centre O."""
    a = math.atan2(p[1] - O[1], p[0] - O[0])
    lab(ax, (p[0] + d * math.cos(a), p[1] + d * math.sin(a)), t, color=color)


def dot(ax, p, color=INK):
    ax.plot([p[0]], [p[1]], "o", color=color, ms=2.6)


def ticks(ax, a, b, n=1, color=HI, size=0.08, gap=0.05):
    mx, my = mid(a, b)
    L = dist(a, b)
    ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    nx, ny = -uy, ux
    for k in range(n):
        off = (k - (n - 1) / 2) * gap
        cx, cy = mx + ux * off, my + uy * off
        ax.plot([cx - nx * size, cx + nx * size], [cy - ny * size, cy + ny * size], color=color, lw=1.1)


def amark(ax, v, p1, p2, n=1, r=0.22, color=HI, label=None, lr=None, fs=8.5):
    a1, a2 = ang(v, p1), ang(v, p2)
    d = (a2 - a1) % 360
    if d > 180:
        a1, a2 = a2, a1
        d = 360 - d
    for k in range(n):
        ax.add_patch(Arc(v, 2 * (r + 0.05 * k), 2 * (r + 0.05 * k), theta1=a1, theta2=a1 + d, color=color, lw=1))
    if label:
        q = P(v, a1 + d / 2, lr or r + 0.2)
        ax.text(q[0], q[1], label, ha="center", va="center", fontsize=fs, color=INK)


def right(ax, v, p1, p2, s=0.1, color=HI):
    u = P(v, ang(v, p1), s); w = P(v, ang(v, p2), s)
    c = (u[0] + w[0] - v[0], u[1] + w[1] - v[1])
    ax.plot([u[0], c[0], w[0]], [u[1], c[1], w[1]], color=color, lw=1)


def finish(ax, title=None, pad=0.3):
    ax.set_aspect("equal"); ax.axis("off")
    ax.autoscale_view()
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    ax.set_xlim(x0 - pad, x1 + pad); ax.set_ylim(y0 - pad, y1 + pad)
    if title:
        ax.set_title(title, fontsize=8.5, color=MUTED)


O = (0.0, 0.0)
R = 1.0


# ------------------------------------------------------------------ lesson figures
def fig_terms():
    fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.4))
    ax = axs[0]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=-0.1, dy=-0.12)
    A, B = P(O, 200, R), P(O, 20, R)
    seg(ax, A, B, color=HI); out(ax, O, A, "A"); out(ax, O, B, "B")
    C = P(O, 110, R); seg(ax, O, C); out(ax, O, C, "C")
    D, E = P(O, 250, R), P(O, 320, R); seg(ax, D, E, color=ACC); out(ax, O, D, "D"); out(ax, O, E, "E")
    finish(ax, "OC radius, AB diameter, DE chord")
    ax = axs[1]
    circ(ax, O, R, color=MUTED, lw=0.8)
    ax.add_patch(Arc(O, 2 * R, 2 * R, theta1=30, theta2=150, color=HI, lw=2.2))
    ax.add_patch(Arc(O, 2 * R, 2 * R, theta1=150, theta2=390, color=ACC, lw=1.4))
    Pp, Q = P(O, 150, R), P(O, 30, R)
    dot(ax, Pp); dot(ax, Q); out(ax, O, Pp, "P"); out(ax, O, Q, "Q")
    ax.text(0, 1.18, "minor arc PQ", ha="center", fontsize=7.5, color=HI)
    ax.text(0, -1.45, "major arc PRQ", ha="center", fontsize=7.5, color=ACC)
    Rr = P(O, 270, R); out(ax, O, Rr, "R", d=0.12)
    finish(ax, "Minor and major arcs")
    ax = axs[2]
    circ(ax, O, R, color=MUTED, lw=0.8)
    ax.add_patch(Wedge(O, R, 200, 280, fc=SOFT, ec=ACC, lw=1.2))
    A, B = P(O, 40, R), P(O, 140, R)
    th = [math.radians(t) for t in range(40, 141, 5)]
    seg_pts = [(math.cos(t), math.sin(t)) for t in th]
    ax.add_patch(Polygon(seg_pts, closed=True, fc="#F6EBD7", ec=HI, lw=1.2))
    ax.text(0, 0.78, "minor\nsegment", ha="center", fontsize=7, color=INK)
    ax.text(-0.45, -0.55, "minor\nsector", ha="center", fontsize=7, color=INK)
    dot(ax, O); lab(ax, O, "O", dx=0.12, dy=0.05)
    finish(ax, "Segment and sector")
    save(fig, "ch09_fig01_circle_terms.png")


def fig_equal_chords():
    fig, axs = plt.subplots(1, 2, figsize=(5.8, 2.4))
    ax = axs[0]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=0.0, dy=-0.15)
    A, B = P(O, 100, R), P(O, 170, R); C, D = P(O, 290, R), P(O, 0, R)
    for p, q in [(A, B), (C, D)]:
        seg(ax, p, q); seg(ax, O, p, color=HI, lw=1); seg(ax, O, q, color=HI, lw=1)
    ticks(ax, A, B, 1); ticks(ax, C, D, 1)
    amark(ax, O, A, B, 1, r=0.2); amark(ax, O, C, D, 1, r=0.2)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t)
    finish(ax, "Theorem 9.1")
    ax = axs[1]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=-0.12, dy=0.1)
    A, B = P(O, 215, R), P(O, 325, R); M = mid(A, B)
    seg(ax, A, B); seg(ax, O, M, color=HI); seg(ax, O, A, color=MUTED, lw=0.9); seg(ax, O, B, color=MUTED, lw=0.9)
    right(ax, M, B, O); ticks(ax, A, M, 1); ticks(ax, M, B, 1)
    out(ax, O, A, "A"); out(ax, O, B, "B"); lab(ax, M, "M", dy=-0.15)
    finish(ax, "Theorems 9.3 and 9.4")
    save(fig, "ch09_fig02_chords_and_centre.png")


def fig_equidistant():
    fig, ax = plt.subplots(figsize=(2.8, 2.6))
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=-0.12, dy=0.05)
    A, B = P(O, 130, R), P(O, 50, R); C, D = P(O, 220, R), P(O, 300, R)
    L, M = mid(A, B), mid(C, D)
    seg(ax, A, B); seg(ax, C, D); seg(ax, O, L, color=HI); seg(ax, O, M, color=HI)
    right(ax, L, B, O); right(ax, M, D, O); ticks(ax, A, B, 1); ticks(ax, C, D, 1)
    seg(ax, O, B, color=MUTED, lw=0.8, dash=True); seg(ax, O, D, color=MUTED, lw=0.8, dash=True)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t)
    lab(ax, L, "L", dy=0.13); lab(ax, M, "M", dx=-0.12, dy=-0.08)
    finish(ax)
    save(fig, "ch09_fig03_equal_chords_equidistant.png")


def fig_centre_angle():
    fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.4))
    cases = [("(i) minor arc PQ", 220, 320, 90), ("(ii) semicircle PQ", 180, 360, 80), ("(iii) major arc PQ", 300, 240, 270)]
    for ax, (t, a1, a2, ap) in zip(axs, cases):
        circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=0.12, dy=0.1)
        Pp, Q, A = P(O, a1, R), P(O, a2, R), P(O, ap, R)
        Bb = P(O, ap + 180, R)
        seg(ax, A, Pp); seg(ax, A, Q); seg(ax, A, Bb, color=MUTED, lw=0.9, dash=True)
        if "semi" in t:
            seg(ax, Pp, Q, color=HI)
        else:
            seg(ax, O, Pp, color=HI); seg(ax, O, Q, color=HI)
        amark(ax, A, Pp, Q, 1, r=0.25)
        out(ax, O, Pp, "P"); out(ax, O, Q, "Q"); out(ax, O, A, "A"); out(ax, O, Bb, "B", d=0.15)
        finish(ax, t)
    save(fig, "ch09_fig04_angle_at_centre.png")


def fig_same_segment():
    fig, axs = plt.subplots(1, 2, figsize=(5.8, 2.4))
    ax = axs[0]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=0.1, dy=-0.12)
    Pp, Q = P(O, 210, R), P(O, 330, R)
    seg(ax, Pp, Q)
    for a, n in [(70, "A"), (120, "B"), (155, "C")]:
        X = P(O, a, R); seg(ax, X, Pp, color=HI, lw=1.1); seg(ax, X, Q, color=HI, lw=1.1)
        amark(ax, X, Pp, Q, 1, r=0.18); out(ax, O, X, n)
    out(ax, O, Pp, "P"); out(ax, O, Q, "Q")
    finish(ax, "Theorem 9.8: angles in the same segment")
    ax = axs[1]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dy=-0.13)
    A, B = P(O, 180, R), P(O, 0, R); C = P(O, 65, R)
    seg(ax, A, B); seg(ax, A, C, color=HI); seg(ax, B, C, color=HI); right(ax, C, A, B, s=0.1)
    out(ax, O, A, "A"); out(ax, O, B, "B"); out(ax, O, C, "C")
    finish(ax, "Angle in a semicircle is $90^\\circ$")
    save(fig, "ch09_fig05_same_segment_semicircle.png")


def fig_cyclic():
    fig, axs = plt.subplots(1, 2, figsize=(5.8, 2.4))
    ax = axs[0]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=0.12, dy=-0.05)
    A, B, C, D = P(O, 200, R), P(O, 300, R), P(O, 20, R), P(O, 115, R)
    poly(ax, [A, B, C, D]); seg(ax, A, C, color=HI, lw=1); seg(ax, B, D, color=HI, lw=1)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t)
    amark(ax, A, B, D, 1, r=0.2); amark(ax, C, D, B, 2, r=0.2)
    finish(ax, "Theorem 9.10: $\\angle A + \\angle C = 180^\\circ$")
    ax = axs[1]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=-0.14, dy=0.02)
    A, B, C, D = P(O, 200, R), P(O, 300, R), P(O, 20, R), P(O, 115, R)
    poly(ax, [A, B, C, D]); seg(ax, O, B, color=HI); seg(ax, O, D, color=HI)
    ax.add_patch(Arc(O, 0.4, 0.4, theta1=115, theta2=300, color=HI, lw=1))
    ax.add_patch(Arc(O, 0.3, 0.3, theta1=300, theta2=475, color=ACC, lw=1))
    for p_, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p_, t)
    finish(ax, "$\\angle BOD = 2\\angle A$, reflex $\\angle BOD = 2\\angle C$")
    save(fig, "ch09_fig06_cyclic_quadrilateral.png")


def fig_examples_a():
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.4))
    # Example 1: chord at distance 5 from centre, radius 13
    ax = axs[0]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=-0.12, dy=0.05)
    d = 5 / 13
    M = (0, -d); h = math.sqrt(1 - d * d); A, B = (-h, -d), (h, -d)
    seg(ax, A, B); seg(ax, O, M, color=HI); seg(ax, O, B, color=HI); right(ax, M, B, O)
    out(ax, O, A, "A"); out(ax, O, B, "B"); lab(ax, M, "M", dy=-0.14)
    ax.text(0.06, -0.2, "5", fontsize=8.5, color=INK); ax.text(0.42, -0.08, "13", fontsize=8.5, color=INK)
    finish(ax, "Example 1")
    # Example 2: two intersecting circles, line of centres
    ax = axs[1]
    O1, O2, r1, r2 = (0, 0), (1.3, 0), 1.0, 0.8
    circ(ax, O1, r1); circ(ax, O2, r2)
    x = (r1 * r1 - r2 * r2 + 1.3 ** 2) / (2 * 1.3); y = math.sqrt(r1 * r1 - x * x)
    A, B = (x, y), (x, -y)
    seg(ax, O1, O2, color=HI); seg(ax, O1, A, color=MUTED, lw=0.9); seg(ax, O2, A, color=MUTED, lw=0.9)
    seg(ax, O1, B, color=MUTED, lw=0.9); seg(ax, O2, B, color=MUTED, lw=0.9)
    amark(ax, A, O1, O2, 1, r=0.18); amark(ax, B, O1, O2, 1, r=0.18)
    for p, t, dx, dy in [(O1, "O", -0.12, 0), (O2, "O'", 0.15, 0), (A, "A", 0, 0.15), (B, "B", 0, -0.15)]:
        dot(ax, p); lab(ax, p, t, dx, dy)
    finish(ax, "Example 2")
    # Example 3: chords AB and CD meet at E on diameter PQ making equal angles
    ax = axs[2]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dy=-0.13)
    E = (0.35, 0.0); th = 50
    def chord_through(E, deg):
        dx, dy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
        b = E[0] * dx + E[1] * dy; c = E[0] ** 2 + E[1] ** 2 - 1
        t1 = -b + math.sqrt(b * b - c); t2 = -b - math.sqrt(b * b - c)
        return (E[0] + t1 * dx, E[1] + t1 * dy), (E[0] + t2 * dx, E[1] + t2 * dy)
    A, B = chord_through(E, 180 - th); C, D = chord_through(E, 180 + th)
    Pp, Q = (-1, 0), (1, 0)
    seg(ax, Pp, Q, color=MUTED, lw=1); seg(ax, A, B); seg(ax, C, D)
    L = foot(O, A, B); M = foot(O, C, D)
    seg(ax, O, L, color=HI, dash=True); seg(ax, O, M, color=HI, dash=True); right(ax, L, B, O, s=0.08); right(ax, M, D, O, s=0.08)
    amark(ax, E, Pp, A, 1, r=0.18); amark(ax, E, Pp, C, 1, r=0.24)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D"), (Pp, "P"), (Q, "Q")]:
        out(ax, O, p, t, d=0.15)
    lab(ax, E, "E", dx=0.12, dy=0.1); lab(ax, L, "L", dx=-0.05, dy=0.13); lab(ax, M, "M", dx=-0.05, dy=-0.13)
    finish(ax, "Example 3")
    save(fig, "ch09_fig07_examples1_3.png")


def fig_examples_b():
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.6))
    # Example 4: AB diameter, CD = radius; AC and BD meet at E; angle AEB = 60
    ax = axs[0]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dy=-0.13)
    A, B = (-1, 0), (1, 0); C, D = P(O, 120, R), P(O, 60, R)
    E = meet(A, C, B, D)
    seg(ax, A, B); seg(ax, A, E, color=HI); seg(ax, B, E, color=HI); seg(ax, C, D)
    seg(ax, O, C, color=MUTED, lw=0.9, dash=True); seg(ax, O, D, color=MUTED, lw=0.9, dash=True); seg(ax, A, D, color=MUTED, lw=0.9)
    ticks(ax, C, D, 1); ticks(ax, O, C, 1); ticks(ax, O, D, 1)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t, d=0.15)
    lab(ax, E, "E", dy=0.13)
    finish(ax, "Example 4: $CD = OC$")
    # Example 5: cyclic ABCD, angle DBC = 55, angle BAC = 45
    ax = axs[1]
    circ(ax, O, R)
    A, B, C, D = P(O, 160, R), P(O, 250, R), P(O, 340, R), P(O, 70, R)
    poly(ax, [A, B, C, D]); seg(ax, A, C, color=HI, lw=1); seg(ax, B, D, color=HI, lw=1)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t, d=0.15)
    amark(ax, B, D, C, 1, r=0.25, label="$55^\\circ$", lr=0.48); amark(ax, A, B, C, 1, r=0.25, label="$45^\\circ$", lr=0.5)
    finish(ax, "Example 5")
    # Example 6: two circles through A and B; AD and AC diameters
    ax = axs[2]
    O1, O2, r1, r2 = (0, 0), (1.25, 0.1), 1.0, 0.85
    circ(ax, O1, r1); circ(ax, O2, r2)
    dx, dy = O2[0] - O1[0], O2[1] - O1[1]; dd = math.hypot(dx, dy)
    a = (r1 * r1 - r2 * r2 + dd * dd) / (2 * dd); h = math.sqrt(r1 * r1 - a * a)
    base = (O1[0] + a * dx / dd, O1[1] + a * dy / dd)
    A = (base[0] - h * dy / dd, base[1] + h * dx / dd); Bp = (base[0] + h * dy / dd, base[1] - h * dx / dd)
    D = (2 * O1[0] - A[0], 2 * O1[1] - A[1]); C = (2 * O2[0] - A[0], 2 * O2[1] - A[1])
    seg(ax, A, D, color=HI); seg(ax, A, C, color=HI); seg(ax, D, C); seg(ax, A, Bp, color=MUTED, dash=True)
    right(ax, Bp, A, C, s=0.08)
    for p, t, dx_, dy_ in [(A, "A", 0, 0.14), (Bp, "B", 0.05, -0.15), (C, "C", 0.14, -0.05), (D, "D", -0.14, -0.05)]:
        dot(ax, p); lab(ax, p, t, dx_, dy_)
    finish(ax, "Example 6: AD, AC diameters")
    save(fig, "ch09_fig08_examples4_6.png")


# ------------------------------------------------------------------ Exercise figures
def ex92():
    fig, axs = plt.subplots(2, 2, figsize=(6.0, 5.0))
    # Q1: circles radius 5 and 3, centres 4 apart; common chord through the small centre
    ax = axs[0][0]
    s = 0.2
    O1, O2 = (0, 0), (4 * s, 0)
    circ(ax, O1, 5 * s); circ(ax, O2, 3 * s)
    A, B = (4 * s, 3 * s), (4 * s, -3 * s)
    seg(ax, A, B, color=HI); seg(ax, O1, O2, color=MUTED); seg(ax, O1, A, color=MUTED, lw=0.9)
    right(ax, O2, A, O1, s=0.08)
    for p, t, dx, dy in [(O1, "O", -0.12, -0.1), (O2, "O'", 0.14, -0.1), (A, "A", 0.1, 0.12), (B, "B", 0.1, -0.12)]:
        dot(ax, p); lab(ax, p, t, dx, dy)
    finish(ax, "Q1: radii 5 cm and 3 cm, $OO' = 4$ cm")
    # Q2 and Q3: equal chords AB and CD meet at E inside the circle
    ax = axs[0][1]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=-0.12, dy=0.05)
    d = 0.45; h = math.sqrt(1 - d * d)
    L0, M0 = P(O, 60, d), P(O, 120, d)
    A = (L0[0] - h * 0.866, L0[1] + h * 0.5); B = (L0[0] + h * 0.866, L0[1] - h * 0.5)
    C = (M0[0] + h * 0.866, M0[1] + h * 0.5); D = (M0[0] - h * 0.866, M0[1] - h * 0.5)
    E = meet(A, B, C, D)
    seg(ax, A, B); seg(ax, C, D); seg(ax, O, E, color=HI, dash=True)
    L, M = foot(O, A, B), foot(O, C, D)
    seg(ax, O, L, color=MUTED, lw=0.9); seg(ax, O, M, color=MUTED, lw=0.9); right(ax, L, B, O, s=0.07); right(ax, M, C, O, s=0.07)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t, d=0.14)
    lab(ax, E, "E", dy=0.14); lab(ax, L, "L", dx=0.1, dy=-0.1); lab(ax, M, "M", dx=-0.1, dy=-0.1)
    finish(ax, "Q2 and Q3: $AB = CD$ meet at E")
    # Q4: line meets two concentric circles at A, B, C, D
    ax = axs[1][0]
    circ(ax, O, R); circ(ax, O, 0.55); dot(ax, O); lab(ax, O, "O", dx=-0.1, dy=0.1)
    y = -0.35
    xa, xb = math.sqrt(1 - y * y), math.sqrt(0.55 ** 2 - y * y)
    A, B, C, D = (-xa, y), (-xb, y), (xb, y), (xa, y)
    seg(ax, (-1.25, y), (1.25, y)); M = (0, y); seg(ax, O, M, color=HI); right(ax, M, D, O, s=0.07)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        dot(ax, p); lab(ax, p, t, dy=-0.14)
    lab(ax, M, "M", dx=0.1, dy=0.12)
    finish(ax, "Q4: concentric circles")
    # Q5: R, S, M on circle radius 5, RS = SM = 6
    ax = axs[1][1]
    s = 0.2
    circ(ax, O, 5 * s); dot(ax, O); lab(ax, O, "O", dx=0.0, dy=-0.15)
    phi = math.degrees(2 * math.asin(3 / 5))
    Sg = P(O, 90, 5 * s); Rr = P(O, 90 + phi, 5 * s); Mm = P(O, 90 - phi, 5 * s)
    seg(ax, Rr, Sg); seg(ax, Sg, Mm); seg(ax, Rr, Mm, color=HI); seg(ax, O, Sg, color=MUTED, dash=True)
    seg(ax, O, Rr, color=MUTED, lw=0.9)
    Pf = meet(Rr, Mm, O, Sg)
    ticks(ax, Rr, Sg, 1); ticks(ax, Sg, Mm, 1)
    out(ax, O, Rr, "R"); out(ax, O, Sg, "S"); out(ax, O, Mm, "M"); lab(ax, Pf, "P", dx=0.13, dy=0.1)
    finish(ax, "Q5: $RS = SM = 6$ m, radius 5 m")
    save(fig, "ch09_fig09_exercise_9_2.png")


def ex93_a():
    fig, axs = plt.subplots(2, 2, figsize=(6.0, 5.0))
    # Q1: angle BOC = 30, AOB = 60; D on the other arc
    ax = axs[0][0]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=-0.1, dy=-0.12)
    C, B, A = P(O, 0, R), P(O, 30, R), P(O, 90, R); D = P(O, 225, R)
    for X in (A, B, C):
        seg(ax, O, X, color=HI, lw=1)
    seg(ax, D, A); seg(ax, D, C)
    amark(ax, O, B, C, 1, r=0.3, label="$30^\\circ$", lr=0.52); amark(ax, O, A, B, 1, r=0.2, label="$60^\\circ$", lr=0.4)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t, d=0.14)
    finish(ax, "Q1")
    # Q3: angle PQR = 100 with Q on minor arc
    ax = axs[0][1]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dy=0.13)
    Pp, Rr = P(O, 190, R), P(O, 350, R); Q = P(O, 270, R)
    seg(ax, Pp, Q); seg(ax, Q, Rr); seg(ax, Pp, Rr, color=MUTED, lw=1); seg(ax, O, Pp, color=HI); seg(ax, O, Rr, color=HI)
    amark(ax, Q, Pp, Rr, 1, r=0.2, label="$100^\\circ$", lr=0.42)
    for p, t in [(Pp, "P"), (Q, "Q"), (Rr, "R")]:
        out(ax, O, p, t, d=0.14)
    finish(ax, "Q3")
    # Q4: angle ABC = 69, ACB = 31, D on the same side as A
    ax = axs[1][0]
    circ(ax, O, R)
    angA = 80
    B, C = P(O, 270 - angA, R), P(O, 270 + angA, R)
    # position A so that angle ABC = 69: arc AC (not containing B) = 138 degrees
    A = P(O, (270 + angA) + 138, R); D = P(O, 110, R)
    poly(ax, [A, B, C]); seg(ax, D, B, color=HI); seg(ax, D, C, color=HI)
    amark(ax, B, A, C, 1, r=0.2, label="$69^\\circ$", lr=0.42); amark(ax, C, A, B, 1, r=0.2, label="$31^\\circ$", lr=0.44)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t, d=0.14)
    finish(ax, "Q4")
    # Q5: AC and BD meet at E, angle BEC = 130, angle ECD = 20
    ax = axs[1][1]
    circ(ax, O, R)
    # arc AD = 40 gives angle ACD = 20; arc BC = 220 gives angle BEC = (220 + 40)/2 = 130
    D, A, B, C = P(O, 70, R), P(O, 110, R), P(O, 160, R), P(O, 20, R)
    seg(ax, A, C); seg(ax, B, D); seg(ax, A, B, color=MUTED, lw=0.9); seg(ax, C, D, color=MUTED, lw=0.9)
    E = meet(A, C, B, D)
    amark(ax, E, B, C, 1, r=0.16, label="$130^\\circ$", lr=0.4); amark(ax, C, E, D, 1, r=0.25, label="$20^\\circ$", lr=0.47)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t, d=0.14)
    lab(ax, E, "E", dx=0.12, dy=0.1)
    finish(ax, "Q5")
    save(fig, "ch09_fig10_exercise_9_3_q1_q5.png")


def ex93_b():
    fig, axs = plt.subplots(2, 2, figsize=(6.0, 5.0))
    # Q6: cyclic ABCD, diagonals meet at E, angle DBC = 70, angle BAC = 30
    ax = axs[0][0]
    circ(ax, O, R)
    # angle BAC = 30 -> arc BC = 60; angle DBC = 70 -> arc DC = 140
    B = P(O, 250, R); C = P(O, 310, R); D = P(O, 310 + 140, R); A = P(O, 170, R)
    poly(ax, [A, B, C, D]); seg(ax, A, C, color=HI, lw=1); seg(ax, B, D, color=HI, lw=1)
    E = meet(A, C, B, D)
    amark(ax, B, D, C, 1, r=0.25, label="$70^\\circ$", lr=0.47); amark(ax, A, B, C, 1, r=0.3, label="$30^\\circ$", lr=0.52)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t, d=0.14)
    lab(ax, E, "E", dx=0.12, dy=0.05)
    finish(ax, "Q6")
    # Q9: two circles through B and C; ABD and PBQ through B
    ax = axs[0][1]
    O1, O2, r1, r2 = (0, 0), (1.3, 0), 1.0, 0.9
    circ(ax, O1, r1); circ(ax, O2, r2)
    x = (r1 * r1 - r2 * r2 + 1.3 ** 2) / (2 * 1.3); y = math.sqrt(r1 * r1 - x * x)
    Bp, C = (x, y), (x, -y)
    def second(Oc, rc, pnt, deg):
        dx, dy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
        fx, fy = pnt[0] - Oc[0], pnt[1] - Oc[1]
        t = -2 * (fx * dx + fy * dy)
        return (pnt[0] + t * dx, pnt[1] + t * dy)
    A = second(O1, r1, Bp, 200); D = second(O2, r2, Bp, 20)
    Pp = second(O1, r1, Bp, 235); Q = second(O2, r2, Bp, 55)
    seg(ax, A, D, color=HI); seg(ax, Pp, Q, color=HI)
    for X in (A, Pp, Q, D):
        seg(ax, C, X, color=MUTED, lw=0.9)
    for p, t, dx, dy in [(Bp, "B", 0.02, 0.15), (C, "C", 0, -0.15), (A, "A", -0.15, 0), (D, "D", 0.15, 0), (Pp, "P", -0.12, -0.08), (Q, "Q", 0.12, 0.08)]:
        dot(ax, p); lab(ax, p, t, dx, dy)
    finish(ax, "Q9")
    # Q10: circles on AB and AC as diameters meet at D on BC
    ax = axs[1][0]
    A, B, C = (0.3, 1.2), (-0.6, 0), (1.4, 0)
    D = foot(A, B, C)
    for a, b in [(A, B), (A, C)]:
        m = mid(a, b); circ(ax, m, dist(a, b) / 2, color=MUTED, lw=0.9)
    poly(ax, [A, B, C]); seg(ax, A, D, color=HI); right(ax, D, C, A, s=0.08)
    for p, t, dx, dy in [(A, "A", 0, 0.15), (B, "B", -0.12, -0.1), (C, "C", 0.12, -0.1), (D, "D", 0.02, -0.15)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q10")
    # Q11: right triangles ABC and ADC with common hypotenuse AC
    ax = axs[1][1]
    circ(ax, O, R, color=MUTED, lw=0.9, dash=True)
    A, C = (-1, 0), (1, 0); B, D = P(O, 250, R), P(O, 70, R)
    seg(ax, A, C); poly(ax, [A, B, C]); poly(ax, [A, D, C]); seg(ax, B, D, color=HI)
    right(ax, B, A, C, s=0.08); right(ax, D, A, C, s=0.08)
    amark(ax, A, C, D, 1, r=0.25); amark(ax, B, C, D, 1, r=0.25)
    for p, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
        out(ax, O, p, t, d=0.14)
    finish(ax, "Q11")
    save(fig, "ch09_fig11_exercise_9_3_q6_q11.png")


def fig_example3_big():
    fig, ax = plt.subplots(figsize=(3.2, 3.0))
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=-0.02, dy=-0.13)
    E = (0.45, 0.0); th = 55
    def chord_through(E, deg):
        dx, dy = math.cos(math.radians(deg)), math.sin(math.radians(deg))
        b = E[0] * dx + E[1] * dy; c = E[0] ** 2 + E[1] ** 2 - 1
        t1 = -b + math.sqrt(b * b - c); t2 = -b - math.sqrt(b * b - c)
        return (E[0] + t1 * dx, E[1] + t1 * dy), (E[0] + t2 * dx, E[1] + t2 * dy)
    A, B = chord_through(E, 180 - th); C, D = chord_through(E, 180 + th)
    Pp, Q = (-1, 0), (1, 0)
    seg(ax, Pp, Q, color=MUTED, lw=1); seg(ax, A, B); seg(ax, C, D)
    L = foot(O, A, B); M = foot(O, C, D)
    seg(ax, O, L, color=HI, dash=True); seg(ax, O, M, color=HI, dash=True)
    right(ax, L, B, O, s=0.07); right(ax, M, D, O, s=0.07)
    amark(ax, E, Pp, A, 1, r=0.16); amark(ax, E, Pp, C, 1, r=0.22)
    for p_, t in [(A, "A"), (B, "B"), (C, "C"), (D, "D"), (Pp, "P"), (Q, "Q")]:
        out(ax, O, p_, t, d=0.14)
    lab(ax, E, "E", dx=0.12, dy=0.1); lab(ax, L, "L", dx=-0.06, dy=0.13); lab(ax, M, "M", dx=-0.06, dy=-0.13)
    finish(ax)
    save(fig, "ch09_fig07b_example3.png")


def ex_small():
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.4))
    ax = axs[0]
    for c, lb, a1, a2 in [((0, 0), ("O", "A", "B"), 110, 200), ((2.4, 0), ("O'", "C", "D"), 20, 110)]:
        circ(ax, c, R); dot(ax, c); lab(ax, c, lb[0], dy=-0.15)
        X, Y = P(c, a1, R), P(c, a2, R)
        seg(ax, X, Y); seg(ax, c, X, color=HI, lw=1); seg(ax, c, Y, color=HI, lw=1); ticks(ax, X, Y, 1)
        amark(ax, c, X, Y, 1, r=0.2); out(ax, c, X, lb[1], d=0.15); out(ax, c, Y, lb[2], d=0.15)
    finish(ax, "Ex 9.1: congruent circles, $AB = CD$")
    ax = axs[1]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dx=0.12, dy=0.05)
    A_, S_, D_ = P(O, 90, R), P(O, 210, R), P(O, 330, R)
    poly(ax, [A_, S_, D_]); seg(ax, A_, (0, -0.5), color=HI, dash=True)
    ticks(ax, A_, S_, 1); ticks(ax, S_, D_, 1); ticks(ax, D_, A_, 1)
    out(ax, O, A_, "A"); out(ax, O, S_, "S"); out(ax, O, D_, "D"); lab(ax, (0, -0.5), "M", dx=0.12, dy=-0.12)
    finish(ax, "Ex 9.2 Q6: radius 20 m")
    ax = axs[2]
    circ(ax, O, R); dot(ax, O); lab(ax, O, "O", dy=-0.13)
    A_, B_ = P(O, 60, R), P(O, 120, R); Pm = P(O, 90, R); Qm = P(O, 250, R)
    seg(ax, A_, B_); seg(ax, O, A_, color=HI, lw=1); seg(ax, O, B_, color=HI, lw=1)
    ticks(ax, A_, B_, 1); ticks(ax, O, A_, 1); ticks(ax, O, B_, 1)
    seg(ax, Qm, A_, color=MUTED, lw=1); seg(ax, Qm, B_, color=MUTED, lw=1)
    for p_, t in [(A_, "A"), (B_, "B"), (Qm, "Q")]:
        out(ax, O, p_, t, d=0.14)
    lab(ax, Pm, "P", dy=0.2)
    dot(ax, Pm)
    finish(ax, "Ex 9.3 Q2: chord AB = radius")
    save(fig, "ch09_fig12_ex91_ex92q6_ex93q2.png")


if __name__ == "__main__":
    fig_terms(); fig_equal_chords(); fig_equidistant(); fig_centre_angle(); fig_same_segment(); fig_cyclic()
    fig_examples_a(); fig_examples_b(); ex92(); ex93_a(); ex93_b(); fig_example3_big(); ex_small()
