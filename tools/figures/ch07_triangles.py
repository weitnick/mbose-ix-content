"""Figures for Class IX Mathematics, Chapter 7: Triangles (2026 rationalised book).
Equal sides carry matching tick marks and equal angles carry matching arcs."""
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
INK, ACC, HI, SOFT, MUTED, RED = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#5D6B7A", "#9B2C2C"
plt.rcParams.update({"font.size": 9, "mathtext.fontset": "cm"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def P(o, deg, r):
    return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))


def ang(a, b):
    return math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) % 360


def seg(ax, a, b, color=ACC, lw=1.3, dash=False):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls="--" if dash else "-", solid_capstyle="round")


def poly(ax, pts, color=ACC, fill=None, lw=1.3):
    ax.add_patch(Polygon(pts, closed=True, fill=fill is not None, fc=fill or "none", ec=color, lw=lw))


def lab(ax, p, t, dx=0.0, dy=0.0, color=INK, fs=9, bold=True):
    ax.text(p[0] + dx, p[1] + dy, t, ha="center", va="center", fontsize=fs, weight="bold" if bold else "normal", color=color)


def names(ax, pts, labels, d=0.2, centre=None):
    """Label points, pushing each label away from the centre of the figure."""
    cx = centre[0] if centre else sum(p[0] for p in pts) / len(pts)
    cy = centre[1] if centre else sum(p[1] for p in pts) / len(pts)
    for p, t in zip(pts, labels):
        a = math.atan2(p[1] - cy, p[0] - cx)
        lab(ax, (p[0] + d * math.cos(a), p[1] + d * math.sin(a)), t)


def ticks(ax, a, b, n=1, color=HI, size=0.09, gap=0.05):
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    L = math.hypot(b[0] - a[0], b[1] - a[1])
    ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    nx, ny = -uy, ux
    for k in range(n):
        off = (k - (n - 1) / 2) * gap
        cx, cy = mx + ux * off, my + uy * off
        ax.plot([cx - nx * size, cx + nx * size], [cy - ny * size, cy + ny * size], color=color, lw=1.1)


def amark(ax, v, p1, p2, n=1, r=0.28, color=HI, label=None, lr=None):
    """Arc(s) at vertex v for the angle between rays v->p1 and v->p2 (the smaller angle)."""
    a1, a2 = ang(v, p1), ang(v, p2)
    d = (a2 - a1) % 360
    if d > 180:
        a1, a2 = a2, a1
        d = 360 - d
    for k in range(n):
        ax.add_patch(Arc(v, 2 * (r + 0.06 * k), 2 * (r + 0.06 * k), theta1=a1, theta2=a1 + d, color=color, lw=1))
    if label:
        m = a1 + d / 2
        q = P(v, m, lr or r + 0.22)
        ax.text(q[0], q[1], label, ha="center", va="center", fontsize=8.5, color=INK)


def right(ax, v, p1, p2, s=0.13, color=HI):
    a1, a2 = ang(v, p1), ang(v, p2)
    u = P(v, a1, s); w = P(v, a2, s)
    c = (u[0] + w[0] - v[0], u[1] + w[1] - v[1])
    ax.plot([u[0], c[0], w[0]], [u[1], c[1], w[1]], color=color, lw=1)


def dot(ax, p, color=INK):
    ax.plot([p[0]], [p[1]], "o", color=color, ms=2.8)


def finish(ax, title=None, pad=0.3):
    ax.set_aspect("equal"); ax.axis("off")
    ax.autoscale_view()
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    ax.set_xlim(x0 - pad, x1 + pad); ax.set_ylim(y0 - pad, y1 + pad)
    if title:
        ax.set_title(title, fontsize=8.5, color=MUTED)


# ------------------------------------------------------------------ lesson figures
def fig_congruent():
    fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.0))
    A, B, C = (0.9, 1.6), (0, 0), (2.2, 0)
    tri = [A, B, C]
    for ax, pts, lb, title in [
        (axs[0], tri, "ABC", "$\\triangle ABC$"),
        (axs[1], [(p[0] + 0.0, p[1]) for p in tri], "PQR", "$\\triangle PQR \\cong \\triangle ABC$"),
        (axs[2], [(2.2 - p[0], p[1]) for p in [A, B, C]], "FDE", "$\\triangle FDE \\cong \\triangle ABC$ (turned over)"),
    ]:
        poly(ax, pts)
        names(ax, pts, list(lb))
        ticks(ax, pts[0], pts[1], 1); ticks(ax, pts[1], pts[2], 2); ticks(ax, pts[2], pts[0], 3)
        amark(ax, pts[1], pts[0], pts[2], 1); amark(ax, pts[2], pts[0], pts[1], 2)
        finish(ax, title)
    save(fig, "ch07_fig01_congruent_triangles.png")


def fig_criteria():
    fig, axs = plt.subplots(1, 5, figsize=(7.4, 1.8))
    A, B, C = (0.8, 1.4), (0, 0), (2.0, 0)
    for ax, t in zip(axs, ["SAS", "ASA", "AAS", "SSS", "RHS"]):
        if t == "RHS":
            A2, B2, C2 = (0, 1.4), (0, 0), (2.0, 0)
            poly(ax, [A2, B2, C2]); right(ax, B2, A2, C2)
            ticks(ax, A2, C2, 1); ticks(ax, A2, B2, 2)
            names(ax, [A2, B2, C2], ["", "", ""])
        else:
            poly(ax, [A, B, C])
            if t == "SAS":
                ticks(ax, A, B, 1); ticks(ax, B, C, 2); amark(ax, B, A, C, 1)
            elif t == "ASA":
                amark(ax, B, A, C, 1); amark(ax, C, A, B, 2); ticks(ax, B, C, 1)
            elif t == "AAS":
                amark(ax, B, A, C, 1); amark(ax, C, A, B, 2); ticks(ax, A, B, 1)
            elif t == "SSS":
                ticks(ax, A, B, 1); ticks(ax, B, C, 2); ticks(ax, C, A, 3)
        ax.set_title(t, fontsize=10, color=ACC, weight="bold")
        finish(ax)
    save(fig, "ch07_fig02_congruence_rules.png")


def fig_not_rules():
    fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.0))
    ax = axs[0]
    for s, dx in [(1.0, 0), (1.6, 1.9)]:
        B = (dx, 0); C = (dx + 1.4 * s, 0); A = (dx + 0.5 * s, 1.0 * s)
        poly(ax, [A, B, C]); amark(ax, B, A, C, 1, r=0.2); amark(ax, C, A, B, 2, r=0.2); amark(ax, A, B, C, 3, r=0.18)
    finish(ax, "AAA: same angles, different sizes")
    ax = axs[1]
    B = (0, 0); A = P(B, 50, 2.0)
    # two positions of C with AC = 1.7 on the base line
    ax.plot([-0.1, 3.2], [0, 0], color=MUTED, lw=0.8)
    h = A[1]; dx = math.sqrt(1.7 ** 2 - h ** 2)
    C1 = (A[0] - dx, 0); C2 = (A[0] + dx, 0)
    seg(ax, B, A); seg(ax, A, C1, color=HI); seg(ax, A, C2, color=HI); seg(ax, B, C2)
    amark(ax, B, A, C2, 1, r=0.3)
    ticks(ax, A, C1, 1); ticks(ax, A, C2, 1)
    lab(ax, A, "A", dy=0.18); lab(ax, B, "B", dx=-0.12, dy=-0.15); lab(ax, C1, "C", dy=-0.18); lab(ax, C2, "C'", dy=-0.18)
    finish(ax, "SSA: AB, AC and $\\angle B$ fixed, yet two triangles")
    save(fig, "ch07_fig03_not_congruence_rules.png")


def fig_example1():
    fig, ax = plt.subplots(figsize=(3.2, 2.2))
    O = (0, 0)
    A = P(O, 150, 1.2); B = P(O, 330, 1.2); D = P(O, 210, 0.9); C = P(O, 30, 0.9)
    seg(ax, A, B); seg(ax, D, C); seg(ax, A, D, color=HI); seg(ax, B, C, color=HI)
    ticks(ax, O, A, 1); ticks(ax, O, B, 1); ticks(ax, O, D, 2); ticks(ax, O, C, 2)
    lab(ax, A, "A", dx=-0.12, dy=0.1); lab(ax, B, "B", dx=0.12, dy=-0.1); lab(ax, D, "D", dx=-0.14, dy=-0.05); lab(ax, C, "C", dx=0.14, dy=0.05)
    lab(ax, O, "O", dy=-0.2)
    finish(ax)
    save(fig, "ch07_fig04_example1.png")


def fig_example2():
    fig, ax = plt.subplots(figsize=(2.8, 2.4))
    A, B, C = (-1.2, 0), (1.2, 0), (0, 0)
    Pp = (0, 1.6)
    seg(ax, A, B); seg(ax, (0, -0.4), (0, 2.0), color=MUTED, lw=1)
    seg(ax, Pp, A, color=HI); seg(ax, Pp, B, color=HI)
    right(ax, C, B, Pp); ticks(ax, A, C, 1); ticks(ax, C, B, 1)
    for p, t, dx, dy in [(A, "A", -0.15, 0), (B, "B", 0.15, 0), (C, "C", -0.15, -0.18), (Pp, "P", 0.18, 0.1)]:
        dot(ax, p); lab(ax, p, t, dx, dy)
    lab(ax, (0.12, 2.05), "l", color=MUTED)
    finish(ax)
    save(fig, "ch07_fig05_example2.png")


def fig_asa_proof():
    fig, axs = plt.subplots(1, 2, figsize=(5.4, 2.0))
    A, B, C = (0.7, 1.5), (0, 0), (2.0, 0)
    ax = axs[0]
    poly(ax, [A, B, C]); Pp = (A[0] * 0.65, A[1] * 0.65)
    seg(ax, Pp, C, color=HI, dash=True); dot(ax, Pp); lab(ax, Pp, "P", dx=-0.15)
    names(ax, [A, B, C], ["A", "B", "C"])
    amark(ax, B, A, C, 1); amark(ax, C, A, B, 2, r=0.35); ticks(ax, B, C, 1)
    finish(ax, "Case (ii): P on AB with PB = DE")
    ax = axs[1]
    D, E, F = (0.455, 0.975), (0, 0), (2.0, 0)
    poly(ax, [D, E, F]); names(ax, [D, E, F], ["D", "E", "F"])
    amark(ax, E, D, F, 1); amark(ax, F, D, E, 2, r=0.35); ticks(ax, E, F, 1)
    finish(ax, "$\\angle B = \\angle E$, $\\angle C = \\angle F$, $BC = EF$")
    save(fig, "ch07_fig06_asa_proof.png")


def fig_example3():
    fig, ax = plt.subplots(figsize=(2.8, 2.4))
    A, B, O = (0, 1), (1.6, 1), (0.8, 0)
    D, C = (1.6, -1), (0, -1)
    seg(ax, A, B); seg(ax, C, D); seg(ax, A, D, color=HI); seg(ax, B, C, color=HI)
    ticks(ax, A, O, 1); ticks(ax, O, D, 1)
    amark(ax, B, A, O, 1, r=0.25); amark(ax, C, D, O, 1, r=0.25)
    for p, t, dx, dy in [(A, "A", -0.12, 0.12), (B, "B", 0.12, 0.12), (C, "C", -0.12, -0.12), (D, "D", 0.12, -0.12), (O, "O", 0.22, 0)]:
        lab(ax, p, t, dx, dy)
    finish(ax)
    save(fig, "ch07_fig07_example3.png")


def iso(base=2.0, h=1.8, x0=0.0):
    return (x0 + base / 2, h), (x0, 0), (x0 + base, 0)


def fig_isosceles():
    fig, axs = plt.subplots(1, 2, figsize=(5.0, 2.2))
    for ax, t in zip(axs, ["Theorem 7.2: AD bisects $\\angle A$", "Example 4: AD bisects $\\angle A$, $AD \\perp BC$"]):
        A, B, C = iso()
        D = (1.0, 0)
        poly(ax, [A, B, C]); seg(ax, A, D, color=HI)
        names(ax, [A, B, C], ["A", "B", "C"]); lab(ax, D, "D", dy=-0.2)
        amark(ax, A, B, D, 1, r=0.35); amark(ax, A, D, C, 1, r=0.42)
        if "Theorem" in t:
            ticks(ax, A, B, 1); ticks(ax, A, C, 1)
        else:
            right(ax, D, C, A)
        finish(ax, t)
    save(fig, "ch07_fig08_isosceles.png")


def fig_ex5_ex6():
    fig, axs = plt.subplots(1, 2, figsize=(5.2, 2.3))
    ax = axs[0]
    A, B, C = iso(2.0, 2.0)
    E = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2); F = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
    poly(ax, [A, B, C]); seg(ax, B, F, color=HI); seg(ax, C, E, color=HI)
    names(ax, [A, B, C], ["A", "B", "C"]); lab(ax, E, "E", dx=-0.18); lab(ax, F, "F", dx=0.18)
    ticks(ax, A, E, 1); ticks(ax, E, B, 1); ticks(ax, A, F, 1); ticks(ax, F, C, 1)
    finish(ax, "Example 5")
    ax = axs[1]
    A, B, C = iso(2.4, 1.8)
    D, E = (0.8, 0), (1.6, 0)
    poly(ax, [A, B, C]); seg(ax, A, D, color=HI); seg(ax, A, E, color=HI)
    names(ax, [A, B, C], ["A", "B", "C"]); lab(ax, D, "D", dy=-0.2); lab(ax, E, "E", dy=-0.2)
    ticks(ax, A, B, 1); ticks(ax, A, C, 1)
    finish(ax, "Example 6: $BE = CD$")
    save(fig, "ch07_fig09_examples5_6.png")


def fig_ex7_ex8():
    fig, axs = plt.subplots(1, 2, figsize=(5.4, 2.4))
    ax = axs[0]
    A, B = (-1.1, 0), (1.1, 0); Pp = (0.3, 1.4); Q = (-0.25, -1.0)
    # choose P and Q on the perpendicular bisector x = 0 but draw generically
    Pp = (0, 1.4); Q = (0, -1.0)
    seg(ax, A, B); seg(ax, Pp, Q, color=MUTED, dash=True)
    for X in (A, B):
        seg(ax, Pp, X, color=HI); seg(ax, Q, X, color=ACC)
    ticks(ax, Pp, A, 1); ticks(ax, Pp, B, 1); ticks(ax, Q, A, 2); ticks(ax, Q, B, 2)
    Cc = (0, 0)
    for p, t, dx, dy in [(A, "A", -0.15, 0), (B, "B", 0.15, 0), (Pp, "P", 0, 0.18), (Q, "Q", 0, -0.18), (Cc, "C", 0.15, 0.15)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Example 7: $PA = PB$, $QA = QB$")
    ax = axs[1]
    A = (0, 0); l_dir, m_dir = 10, 60
    seg(ax, P(A, l_dir + 180, 0.4), P(A, l_dir, 2.4)); seg(ax, P(A, m_dir + 180, 0.4), P(A, m_dir, 2.4))
    lab(ax, P(A, l_dir, 2.55), "l", color=MUTED); lab(ax, P(A, m_dir, 2.55), "m", color=MUTED)
    Pp = P(A, (l_dir + m_dir) / 2, 1.9)
    Bf = P(A, l_dir, 1.9 * math.cos(math.radians((m_dir - l_dir) / 2)))
    Cf = P(A, m_dir, 1.9 * math.cos(math.radians((m_dir - l_dir) / 2)))
    seg(ax, A, Pp, color=HI, dash=True); seg(ax, Pp, Bf, color=HI); seg(ax, Pp, Cf, color=HI)
    right(ax, Bf, A, Pp); right(ax, Cf, A, Pp); ticks(ax, Pp, Bf, 1); ticks(ax, Pp, Cf, 1)
    for p, t, dx, dy in [(A, "A", -0.12, -0.15), (Pp, "P", 0.15, 0.08), (Bf, "B", 0.05, -0.2), (Cf, "C", -0.18, 0.08)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Example 8: $PB = PC$")
    save(fig, "ch07_fig10_examples7_8.png")


# ------------------------------------------------------------------ Exercise 7.1
def ex71():
    figA, axA = plt.subplots(2, 2, figsize=(6.0, 4.8))
    figB, axB = plt.subplots(2, 2, figsize=(6.0, 4.8))
    axs = [[axA[0][0], axA[0][1], axA[1][0], axA[1][1]], [axB[0][0], axB[0][1], axB[1][0], axB[1][1]]]
    # Q1: quadrilateral ACBD, AB bisects angle A, AC = AD
    ax = axs[0][0]
    A, B = (0, 0), (2.2, 0); C = P(A, 35, 1.5); D = P(A, -35, 1.5)
    poly(ax, [A, C, B, D]); seg(ax, A, B, color=HI)
    ticks(ax, A, C, 1); ticks(ax, A, D, 1); amark(ax, A, C, B, 1, r=0.35); amark(ax, A, B, D, 1, r=0.42)
    for p, t, dx, dy in [(A, "A", -0.15, 0), (B, "B", 0.15, 0), (C, "C", 0, 0.16), (D, "D", 0, -0.16)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q1")
    # Q2: ABCD with AD = BC and angle DAB = angle CBA
    ax = axs[0][1]
    A, B = (0, 0), (2.0, 0); D = P(A, 100, 1.4); C = P(B, 80, 1.4)
    poly(ax, [A, B, C, D]); seg(ax, A, C, color=HI); seg(ax, B, D, color=HI)
    ticks(ax, A, D, 1); ticks(ax, B, C, 1); amark(ax, A, B, D, 1, r=0.25); amark(ax, B, C, A, 1, r=0.25)
    for p, t, dx, dy in [(A, "A", -0.12, -0.12), (B, "B", 0.12, -0.12), (C, "C", 0.12, 0.12), (D, "D", -0.12, 0.12)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q2")
    # Q3: AD and BC equal perpendiculars to AB on opposite sides; CD meets AB at O
    ax = axs[0][2]
    A, B = (0, 0), (2.0, 0); D = (0, -1.0); C = (2.0, 1.0); O = (1.0, 0)
    seg(ax, A, B); seg(ax, A, D); seg(ax, B, C); seg(ax, C, D, color=HI)
    right(ax, A, B, D); right(ax, B, A, C); ticks(ax, A, D, 1); ticks(ax, B, C, 1)
    for p, t, dx, dy in [(A, "A", -0.15, 0.05), (B, "B", 0.15, -0.05), (C, "C", 0.12, 0.1), (D, "D", -0.12, -0.1), (O, "O", 0.0, 0.2)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q3")
    # Q4: l || m, p || q forming parallelogram ABCD with diagonal AC
    ax = axs[0][3]
    A, B = (0.6, 1.3), (2.4, 1.3); D = (0, 0); C = (1.8, 0)
    seg(ax, (-0.6, 1.3), (3.0, 1.3)); seg(ax, (-0.9, 0), (2.7, 0))
    for a, b in [(A, D), (B, C)]:
        dx, dy = a[0] - b[0], a[1] - b[1]
        seg(ax, (a[0] + dx * 0.4, a[1] + dy * 0.4), (b[0] - dx * 0.3, b[1] - dy * 0.3))
    seg(ax, A, C, color=HI)
    for p, t, dx, dy in [(A, "A", -0.22, 0.17), (B, "B", -0.22, 0.17), (C, "C", 0.24, -0.17), (D, "D", -0.24, -0.17)]:
        lab(ax, p, t, dx, dy)
    lab(ax, (3.18, 1.3), "l", color=MUTED); lab(ax, (2.88, 0), "m", color=MUTED)
    lab(ax, (0.98, 2.0), "p", color=MUTED); lab(ax, (2.78, 2.0), "q", color=MUTED)
    finish(ax, "Q4")
    # Q5: l bisects angle A; BP and BQ perpendicular to the arms
    ax = axs[1][0]
    A = (0, 0); h = 25
    seg(ax, A, P(A, h, 2.2)); seg(ax, A, P(A, -h, 2.2)); seg(ax, A, P(A, 0, 2.3), color=MUTED, dash=True)
    Bp = (1.8, 0); Pf = P(A, h, 1.8 * math.cos(math.radians(h))); Qf = P(A, -h, 1.8 * math.cos(math.radians(h)))
    seg(ax, Bp, Pf, color=HI); seg(ax, Bp, Qf, color=HI); right(ax, Pf, A, Bp); right(ax, Qf, A, Bp)
    for p, t, dx, dy in [(A, "A", -0.15, 0), (Bp, "B", 0.18, 0.02), (Pf, "P", -0.05, 0.18), (Qf, "Q", -0.05, -0.18)]:
        lab(ax, p, t, dx, dy)
    lab(ax, (2.45, 0), "l", color=MUTED)
    finish(ax, "Q5")
    # Q6: AC = AE, AB = AD, angle BAD = angle EAC
    ax = axs[1][1]
    A = (0, 1.9)
    B = P(A, 237, 2.0); D = P(A, 257, 2.0); C = P(A, 290, 2.1); E = P(A, 310, 2.1)
    for X in (B, D, C, E):
        seg(ax, A, X)
    seg(ax, B, C, color=HI); seg(ax, D, E, color=HI)
    ticks(ax, A, B, 1); ticks(ax, A, D, 1); ticks(ax, A, C, 2); ticks(ax, A, E, 2)
    for p, t in [(B, "B"), (D, "D"), (C, "C"), (E, "E")]:
        q = P(A, ang(A, p), math.hypot(p[0] - A[0], p[1] - A[1]) + 0.2)
        lab(ax, q, t)
    lab(ax, A, "A", dy=0.18)
    finish(ax, "Q6")
    # Q7: AB with mid-point P; D and E above
    ax = axs[1][2]
    A, B, Pm = (0, 0), (2.4, 0), (1.2, 0)
    D, E = (0.55, 1.3), (1.85, 1.3)
    seg(ax, A, B); seg(ax, A, D); seg(ax, B, E); seg(ax, Pm, D, color=HI); seg(ax, Pm, E, color=HI)
    ticks(ax, A, Pm, 1); ticks(ax, Pm, B, 1); amark(ax, A, B, D, 1, r=0.25); amark(ax, B, E, A, 1, r=0.25)
    for p, t, dx, dy in [(A, "A", -0.12, -0.12), (B, "B", 0.12, -0.12), (Pm, "P", 0, -0.2), (D, "D", -0.1, 0.15), (E, "E", 0.1, 0.15)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q7")
    # Q8: right angle at C, M mid-point of AB, D with DM = CM
    ax = axs[1][3]
    C, B, A = (0, 0), (2.4, 0), (0, 1.6); M = (1.2, 0.8); D = (2.4, 1.6)
    poly(ax, [A, B, C]); seg(ax, C, D, color=HI); seg(ax, D, B, color=HI); seg(ax, A, D, color=MUTED, dash=True)
    right(ax, C, A, B); ticks(ax, C, M, 1); ticks(ax, M, D, 1); ticks(ax, A, M, 2); ticks(ax, M, B, 2)
    for p, t, dx, dy in [(A, "A", -0.12, 0.1), (B, "B", 0.12, -0.12), (C, "C", -0.12, -0.12), (D, "D", 0.12, 0.1), (M, "M", -0.05, 0.2)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q8")
    save(figA, "ch07_fig11_exercise_7_1_q1_q4.png")
    save(figB, "ch07_fig11b_exercise_7_1_q5_q8.png")


# ------------------------------------------------------------------ Exercise 7.2
def ex72():
    fig, axs = plt.subplots(2, 3, figsize=(7.0, 4.4))
    # Q1: bisectors of B and C meet at O
    ax = axs[0][0]
    A, B, C = iso(2.4, 2.2)
    poly(ax, [A, B, C])
    b = ang(B, C); bb = (ang(B, A) + b) / 2
    O = (1.2, math.tan(math.radians(bb)) * 1.2)
    seg(ax, B, O, color=HI); seg(ax, C, O, color=HI); seg(ax, A, O, color=MUTED, dash=True)
    amark(ax, B, C, O, 1, r=0.35); amark(ax, B, O, A, 1, r=0.42); amark(ax, C, O, B, 2, r=0.35); amark(ax, C, A, O, 2, r=0.42)
    ticks(ax, A, B, 1); ticks(ax, A, C, 1)
    names(ax, [A, B, C], ["A", "B", "C"]); lab(ax, O, "O", dx=0.2, dy=0.1)
    finish(ax, "Q1")
    # Q2: AD perpendicular bisector of BC (A off-centre looks general but is isosceles)
    ax = axs[0][1]
    A, B, C = iso(2.2, 2.0); D = (1.1, 0)
    poly(ax, [A, B, C]); seg(ax, A, D, color=HI); right(ax, D, C, A); ticks(ax, B, D, 1); ticks(ax, D, C, 1)
    names(ax, [A, B, C], ["A", "B", "C"]); lab(ax, D, "D", dy=-0.2)
    finish(ax, "Q2")
    # Q3 and Q4: altitudes BE and CF
    for ax, t, tk in [(axs[0][2], "Q3", True), (axs[1][0], "Q4", False)]:
        A, B, C = iso(2.2, 2.2)
        poly(ax, [A, B, C])
        def foot(p, a, b):
            dx, dy = b[0] - a[0], b[1] - a[1]
            k = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)
            return (a[0] + k * dx, a[1] + k * dy)
        E = foot(B, A, C); F = foot(C, A, B)
        seg(ax, B, E, color=HI); seg(ax, C, F, color=HI); right(ax, E, C, B, s=0.11); right(ax, F, C, A, s=0.11)
        if tk:
            ticks(ax, A, B, 1); ticks(ax, A, C, 1)
        else:
            ticks(ax, B, E, 2); ticks(ax, C, F, 2)
        names(ax, [A, B, C], ["A", "B", "C"]); lab(ax, E, "E", dx=0.18, dy=0.05); lab(ax, F, "F", dx=-0.18, dy=0.05)
        finish(ax, t)
    # Q5: two isosceles triangles ABC and DBC on the same base, A above and D below
    ax = axs[1][1]
    B, C = (0, 0), (2.0, 0); A = (1.0, 1.6); D = (1.0, -0.9)
    poly(ax, [A, B, C]); poly(ax, [D, B, C]); seg(ax, A, D, color=MUTED, dash=True)
    ticks(ax, A, B, 1); ticks(ax, A, C, 1); ticks(ax, D, B, 2); ticks(ax, D, C, 2)
    for p, t, dx, dy in [(A, "A", 0, 0.18), (B, "B", -0.18, 0), (C, "C", 0.18, 0), (D, "D", 0, -0.18)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q5")
    # Q6: BA produced to D with AD = AB
    ax = axs[1][2]
    B, C = (0, 0), (2.0, 0); A = (1.0, 1.0); D = (2.0, 2.0)
    poly(ax, [A, B, C]); seg(ax, A, D); seg(ax, C, D, color=HI)
    ticks(ax, A, B, 1); ticks(ax, A, C, 1); ticks(ax, A, D, 1)
    for p, t, dx, dy in [(A, "A", -0.2, 0.08), (B, "B", -0.15, -0.1), (C, "C", 0.15, -0.1), (D, "D", 0.12, 0.15)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q6")
    save(fig, "ch07_fig12_exercise_7_2.png")


# ------------------------------------------------------------------ Exercise 7.3
def ex73():
    fig, axg = plt.subplots(2, 2, figsize=(6.0, 4.8))
    axs = [axg[0][0], axg[0][1], axg[1][0], axg[1][1]]
    # Q1: ABC and DBC isosceles, same base, same side; AD produced meets BC at P
    ax = axs[0]
    B, C = (0, 0), (2.2, 0); A = (1.1, 2.0); D = (1.1, 0.9); Pp = (1.1, 0)
    poly(ax, [A, B, C]); seg(ax, B, D); seg(ax, C, D); seg(ax, A, Pp, color=HI)
    ticks(ax, A, B, 1); ticks(ax, A, C, 1); ticks(ax, D, B, 2); ticks(ax, D, C, 2)
    for p, t, dx, dy in [(A, "A", 0, 0.18), (B, "B", -0.15, -0.1), (C, "C", 0.15, -0.1), (D, "D", 0.2, 0.05), (Pp, "P", 0, -0.2)]:
        lab(ax, p, t, dx, dy)
    finish(ax, "Q1")
    # Q2 and Q5: altitude AD (AP) in isosceles ABC
    ax = axs[1]
    A, B, C = iso(2.2, 2.0); D = (1.1, 0)
    poly(ax, [A, B, C]); seg(ax, A, D, color=HI); right(ax, D, C, A); ticks(ax, A, B, 1); ticks(ax, A, C, 1)
    names(ax, [A, B, C], ["A", "B", "C"]); lab(ax, D, "D (or P)", dy=-0.22, fs=8)
    finish(ax, "Q2 and Q5")
    # Q3: two triangles with medians AM and PN
    for ax, (a, b, c, m) in zip(axs[2:], [("A", "B", "C", "M"), ("P", "Q", "R", "N")]):
        B, C, A = (0, 0), (2.2, 0), (0.6, 1.6); M = (1.1, 0)
        poly(ax, [A, B, C]); seg(ax, A, M, color=HI)
        ticks(ax, A, B, 1); ticks(ax, B, M, 2); ticks(ax, M, C, 2); ticks(ax, A, M, 3)
        for p, t, dx, dy in [(A, a, 0, 0.18), (B, b, -0.15, -0.1), (C, c, 0.15, -0.1), (M, m, 0, -0.2)]:
            lab(ax, p, t, dx, dy)
        finish(ax, "Q3" if a == "A" else "Q3 (second triangle)")
    save(fig, "ch07_fig13_exercise_7_3.png")


def fig_river():
    fig, ax = plt.subplots(figsize=(4.4, 2.8))
    A, O, B = (0, 0), (2.0, 0), (4.0, 0)
    T = (0, 3.5 * 0.5); D = (4.0, -3.5 * 0.5)
    ax.add_patch(Polygon([(-0.6, 0.0), (4.6, 0.0), (4.6, T[1]), (-0.6, T[1])], closed=True, fc=SOFT, ec="none"))
    seg(ax, (-0.6, T[1]), (4.6, T[1]), color=MUTED, lw=1)
    ax.text(3.2, 1.0, "river", fontsize=8.5, color=MUTED, style="italic")
    seg(ax, (-0.6, 0), (4.6, 0), color=MUTED, lw=1)
    seg(ax, A, T); seg(ax, T, D, color=HI); seg(ax, B, D); seg(ax, A, B)
    right(ax, A, B, T, s=0.15); right(ax, B, A, D, s=0.15)
    ticks(ax, A, O, 1); ticks(ax, O, B, 1)
    for p, t, dx, dy in [(A, "A", -0.2, -0.15), (O, "O", 0.05, -0.25), (B, "B", 0.2, 0.15), (T, "T", -0.2, 0.1), (D, "D", 0.2, -0.1)]:
        dot(ax, p); lab(ax, p, t, dx, dy)
    ax.text(1.0, -0.3, "20 m", fontsize=8, color=INK, ha="center"); ax.text(3.0, 0.12, "20 m", fontsize=8, color=INK, ha="center")
    finish(ax)
    save(fig, "ch07_fig14_river_width.png")


def fig_golden():
    fig, ax = plt.subplots(figsize=(2.6, 3.0))
    B, C = (0, 0), (1.3, 0)
    h = 0.65 * math.tan(math.radians(72))
    A = (0.65, h)
    # D on AC with angle DBC = 36 degrees
    t = math.tan(math.radians(36))
    # line BD: y = t x ; line AC from C to A
    dx, dy = A[0] - C[0], A[1] - C[1]
    k = (t * C[0] - C[1]) / (dy - t * dx)
    D = (C[0] + k * dx, C[1] + k * dy)
    poly(ax, [A, B, C]); seg(ax, B, D, color=HI)
    ticks(ax, A, B, 1); ticks(ax, A, C, 1)
    amark(ax, A, B, C, 1, r=0.35, label="$36^\\circ$", lr=0.6)
    amark(ax, B, C, D, 1, r=0.25); amark(ax, B, D, A, 1, r=0.32)
    names(ax, [A, B, C], ["A", "B", "C"]); lab(ax, D, "D", dx=0.18, dy=0.05)
    finish(ax)
    save(fig, "ch07_fig15_golden_triangle.png")


if __name__ == "__main__":
    fig_congruent(); fig_criteria(); fig_not_rules(); fig_example1(); fig_example2(); fig_asa_proof(); fig_example3()
    fig_isosceles(); fig_ex5_ex6(); fig_ex7_ex8(); ex71(); ex72(); ex73(); fig_river(); fig_golden()
