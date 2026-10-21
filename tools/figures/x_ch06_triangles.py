"""Figures for Class X Mathematics, Chapter 6: Triangles.
Run: python x_ch06_triangles.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
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


def foot(p, a, b):
    """Foot of the perpendicular from p to line ab."""
    d = b - a
    return a + d * np.dot(p - a, d) / np.dot(d, d)


def meet(a, b, c, d):
    """Intersection of lines ab and cd."""
    m = np.array([b - a, c - d]).T
    t = np.linalg.solve(m, c - a)
    return a + t[0] * (b - a)


def seg(ax, a, b, color=INK, lw=1.3, ls="-"):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls=ls, solid_capstyle="round")


def poly(ax, pts, fc=SOFT, ec=INK, lw=1.3):
    ax.add_patch(Polygon(np.array(pts), closed=True, fc=fc, ec=ec, lw=lw))


def label(ax, pts, names, centre=None, dist=11, size=11):
    """Write each name next to its point, pushed away from the centre of the figure."""
    c = np.mean([pts[n] for n in names], axis=0) if centre is None else centre
    for n in names:
        v = pts[n] - c
        v = v / (np.linalg.norm(v) or 1)
        ax.annotate(n, pts[n], textcoords="offset points", xytext=(v[0] * dist, v[1] * dist),
                    ha="center", va="center", fontsize=size, color=INK)


def dots(ax, pts, names):
    for n in names:
        ax.plot(*pts[n], "o", ms=3, color=INK)


def right(ax, at, p, q, s=0.28):
    u = (p - at) / np.linalg.norm(p - at) * s
    v = (q - at) / np.linalg.norm(q - at) * s
    ax.plot(*zip(at + u, at + u + v, at + v), color=INK, lw=0.9)


def angle(ax, at, p, q, r=0.45, text=None, color=HI, tr=None, size=9):
    a1 = np.degrees(np.arctan2(*(p - at)[::-1]))
    a2 = np.degrees(np.arctan2(*(q - at)[::-1]))
    if (a2 - a1) % 360 > 180:
        a1, a2 = a2, a1
    ax.add_patch(Arc(at, 2 * r, 2 * r, theta1=a1, theta2=a2, color=color, lw=1.1))
    if text:
        mid = np.radians(a1 + ((a2 - a1) % 360) / 2)
        rr = tr or r + 0.28
        ax.text(at[0] + rr * np.cos(mid), at[1] + rr * np.sin(mid), text, ha="center", va="center",
                fontsize=size, color=color)


def side_text(ax, a, b, text, off=0.25, size=9, color=ACC, centre=None):
    m = (a + b) / 2
    d = b - a
    n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
    if centre is not None and np.dot(m - centre, n) < 0:
        n = -n
    ax.text(*(m + n * off), text, ha="center", va="center", fontsize=size, color=color)


def finish(ax, pad=0.6):
    ax.set_aspect("equal")
    ax.axis("off")
    ax.margins(0.08)


# Fig 6.1: equal angles alone, or proportional sides alone, do not make polygons similar
def fig_not_similar():
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.4))
    sq = [P(0, 0), P(2, 0), P(2, 2), P(0, 2)]
    rect = [P(0, 0), P(3.2, 0), P(3.2, 2), P(0, 2)]
    t = np.radians(60)
    rh = [P(0, 0), P(2, 0), P(2 + 2 * np.cos(t), 2 * np.sin(t)), P(2 * np.cos(t), 2 * np.sin(t))]
    for ax, shape, cap in [(axs[0], sq, "square"), (axs[1], rect, "rectangle:\nangles equal,\nsides not in proportion"),
                           (axs[2], rh, "rhombus:\nsides in proportion,\nangles not equal")]:
        poly(ax, shape)
        ax.text(np.mean([p[0] for p in shape]), -0.35, cap, ha="center", va="top", fontsize=8.5)
        ax.set_xlim(-0.6, 3.8); ax.set_ylim(-1.6, 2.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch06_fig01_not_similar.png")


# Fig 6.2: proof of the Basic Proportionality Theorem
def fig_bpt():
    fig, ax = plt.subplots(figsize=(3.8, 3.2))
    p = {"A": P(2, 4), "B": P(0, 0), "C": P(5, 0)}
    p["D"] = p["A"] + 0.4 * (p["B"] - p["A"])
    p["E"] = p["A"] + 0.4 * (p["C"] - p["A"])
    p["M"] = foot(p["D"], p["A"], p["C"])
    p["N"] = foot(p["E"], p["A"], p["B"])
    poly(ax, [p["A"], p["B"], p["C"]])
    seg(ax, p["D"], p["E"], ACC, 1.6)
    seg(ax, p["B"], p["E"], GREY, 1, "--")
    seg(ax, p["C"], p["D"], GREY, 1, "--")
    seg(ax, p["D"], p["M"], HI, 1)
    seg(ax, p["E"], p["N"], HI, 1)
    right(ax, p["M"], p["D"], p["C"], 0.18)
    right(ax, p["N"], p["E"], p["B"], 0.18)
    dots(ax, p, "ABCDEMN")
    label(ax, p, "ABCDEMN", centre=P(2.4, 1.6))
    finish(ax)
    save(fig, "ch06_fig02_bpt_proof.png")


# Fig 6.3: Example 2 - trapezium ABCD, EF || AB, diagonal AC meets EF at G
def fig_trapezium_ef():
    fig, ax = plt.subplots(figsize=(3.8, 2.6))
    p = {"A": P(1, 3), "B": P(4, 3), "C": P(5.2, 0), "D": P(0, 0)}
    p["E"] = p["A"] + 0.4 * (p["D"] - p["A"])
    p["F"] = p["B"] + 0.4 * (p["C"] - p["B"])
    p["G"] = meet(p["A"], p["C"], p["E"], p["F"])
    poly(ax, [p["A"], p["B"], p["C"], p["D"]])
    seg(ax, p["E"], p["F"], ACC, 1.6)
    seg(ax, p["A"], p["C"], GREY, 1, "--")
    dots(ax, p, "ABCDEFG")
    label(ax, p, "ABCDEF")
    ax.annotate("G", p["G"], textcoords="offset points", xytext=(2, 8), fontsize=11)
    finish(ax)
    save(fig, "ch06_fig03_trapezium_ef.png")


# Fig 6.4: Example 3 - PS/SQ = PT/TR and angle PST = angle PRQ
def fig_example3():
    fig, ax = plt.subplots(figsize=(3.2, 3.0))
    p = {"P": P(2.4, 4), "Q": P(0, 0), "R": P(4.8, 0)}
    p["S"] = p["P"] + 0.42 * (p["Q"] - p["P"])
    p["T"] = p["P"] + 0.42 * (p["R"] - p["P"])
    poly(ax, [p["P"], p["Q"], p["R"]])
    seg(ax, p["S"], p["T"], ACC, 1.6)
    angle(ax, p["S"], p["T"], p["P"], 0.3)
    angle(ax, p["R"], p["P"], p["Q"], 0.4)
    dots(ax, p, "PQRST")
    label(ax, p, "PQRST")
    finish(ax)
    save(fig, "ch06_fig04_example3.png")


# Fig 6.5: Ex 6.2 Q1 - two triangles with DE || BC
def fig_ex62_q1():
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.2))
    data = [("(i)", 1 / 3, ["1.5 cm", "3 cm", "1 cm", "?"]), ("(ii)", 0.25, ["?", "7.2 cm", "1.8 cm", "5.4 cm"])]
    for ax, (tag, t, txt) in zip(axs, data):
        p = {"A": P(1.8, 3.6), "B": P(0, 0), "C": P(4.6, 0)}
        p["D"] = p["A"] + t * (p["B"] - p["A"])
        p["E"] = p["A"] + t * (p["C"] - p["A"])
        poly(ax, [p["A"], p["B"], p["C"]])
        seg(ax, p["D"], p["E"], ACC, 1.6)
        dots(ax, p, "ABCDE")
        label(ax, p, "ABCDE", centre=P(2.1, 1.3))
        # lengths written outside the triangle: AD and DB on the left, AE and EC on the right
        for (u, v), t_, left in zip([("A", "D"), ("D", "B"), ("A", "E"), ("E", "C")], txt, [1, 1, 0, 0]):
            m = (p[u] + p[v]) / 2
            ax.text(m[0] + (-0.3 if left else 0.3), m[1], t_, ha="right" if left else "left", va="center",
                    fontsize=9, color=ACC)
        ax.text(2.3, -0.6, tag, ha="center", fontsize=10)
        finish(ax)
    save(fig, "ch06_fig05_ex62_q1.png")


# Fig 6.6: Ex 6.2 Q3 - quadrilateral ABCD, L on AC, LM || CB, LN || CD
def fig_ex62_q3():
    fig, ax = plt.subplots(figsize=(3.6, 3.2))
    p = {"A": P(0, 0), "B": P(4, -1.4), "C": P(5.4, 1.6), "D": P(1.4, 3.4)}
    t = 0.55
    p["L"], p["M"], p["N"] = t * p["C"], t * p["B"], t * p["D"]
    poly(ax, [p["A"], p["B"], p["C"], p["D"]])
    seg(ax, p["A"], p["C"], GREY, 1.1)
    seg(ax, p["L"], p["M"], ACC, 1.5)
    seg(ax, p["L"], p["N"], ACC, 1.5)
    dots(ax, p, "ABCDLMN")
    label(ax, p, "ABCDMN")
    ax.annotate("L", p["L"], textcoords="offset points", xytext=(8, -2), fontsize=11)
    finish(ax)
    save(fig, "ch06_fig06_ex62_q3.png")


# Fig 6.7: Ex 6.2 Q4 - DE || AC and DF || AE
def fig_ex62_q4():
    fig, ax = plt.subplots(figsize=(3.8, 2.8))
    p = {"A": P(2, 4), "B": P(0, 0), "C": P(6, 0)}
    p["D"] = p["B"] + 0.5 * (p["A"] - p["B"])
    p["E"] = p["B"] + 0.5 * (p["C"] - p["B"])
    p["F"] = p["B"] + 0.5 * (p["E"] - p["B"])
    poly(ax, [p["A"], p["B"], p["C"]])
    seg(ax, p["A"], p["E"], GREY, 1.1)
    seg(ax, p["D"], p["E"], ACC, 1.5)
    seg(ax, p["D"], p["F"], ACC, 1.5)
    dots(ax, p, "ABCDEF")
    label(ax, p, "ABCDEF", centre=P(2.5, 1.2))
    finish(ax)
    save(fig, "ch06_fig07_ex62_q4.png")


# Fig 6.8: Ex 6.2 Q5 - DE || OQ and DF || OR
def fig_ex62_q5():
    fig, ax = plt.subplots(figsize=(3.6, 3.2))
    p = {"P": P(2.4, 4.4), "Q": P(0, 0), "R": P(5.4, 0), "O": P(2.8, 1.5)}
    s = 0.5
    p["D"] = p["P"] + s * (p["O"] - p["P"])
    p["E"] = p["P"] + s * (p["Q"] - p["P"])
    p["F"] = p["P"] + s * (p["R"] - p["P"])
    poly(ax, [p["P"], p["Q"], p["R"]])
    for n in "PQR":
        seg(ax, p["O"], p[n], GREY, 1.1)
    seg(ax, p["D"], p["E"], ACC, 1.5)
    seg(ax, p["D"], p["F"], ACC, 1.5)
    seg(ax, p["E"], p["F"], HI, 1.2, "--")
    dots(ax, p, "PQRODEF")
    label(ax, p, "PQREF", centre=P(2.6, 1.6))
    ax.annotate("O", p["O"], textcoords="offset points", xytext=(0, -12), ha="center", fontsize=11)
    ax.annotate("D", p["D"], textcoords="offset points", xytext=(9, 3), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig08_ex62_q5.png")


# Fig 6.9: Ex 6.2 Q6 - A, B, C on OP, OQ, OR; AB || PQ, AC || PR
def fig_ex62_q6():
    fig, ax = plt.subplots(figsize=(3.6, 3.2))
    p = {"P": P(2.4, 4.4), "Q": P(0, 0), "R": P(5.4, 0), "O": P(2.7, 1.7)}
    s = 0.5
    for src, dst in zip("PQR", "ABC"):
        p[dst] = p["O"] + s * (p[src] - p["O"])
    poly(ax, [p["P"], p["Q"], p["R"]])
    for n in "PQR":
        seg(ax, p["O"], p[n], GREY, 1.1)
    seg(ax, p["A"], p["B"], ACC, 1.5)
    seg(ax, p["A"], p["C"], ACC, 1.5)
    seg(ax, p["B"], p["C"], HI, 1.2, "--")
    dots(ax, p, "PQROABC")
    label(ax, p, "PQR", centre=P(2.6, 1.6))
    ax.annotate("O", p["O"], textcoords="offset points", xytext=(0, 10), ha="center", fontsize=11)
    ax.annotate("A", p["A"], textcoords="offset points", xytext=(-9, 2), ha="center", fontsize=11)
    ax.annotate("B", p["B"], textcoords="offset points", xytext=(-4, -11), ha="center", fontsize=11)
    ax.annotate("C", p["C"], textcoords="offset points", xytext=(4, -11), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig09_ex62_q6.png")


# Fig 6.10: trapezium ABCD (AB || DC) with diagonals meeting at O
def fig_trapezium_o():
    fig, ax = plt.subplots(figsize=(3.8, 2.4))
    p = {"A": P(1.2, 3), "B": P(4.4, 3), "C": P(6, 0), "D": P(0, 0)}
    p["O"] = meet(p["A"], p["C"], p["B"], p["D"])
    poly(ax, [p["A"], p["B"], p["C"], p["D"]])
    seg(ax, p["A"], p["C"], ACC, 1.3)
    seg(ax, p["B"], p["D"], ACC, 1.3)
    dots(ax, p, "ABCDO")
    label(ax, p, "ABCD")
    ax.annotate("O", p["O"], textcoords="offset points", xytext=(0, -12), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig10_trapezium_diagonals.png")


# Fig 6.11: Example 4 - PQ || RS, lines PS and QR meet at O
def fig_bowtie():
    fig, ax = plt.subplots(figsize=(3.4, 2.8))
    p = {"P": P(0, 2.6), "Q": P(2.4, 2.6), "O": P(1.5, 1.5)}
    p["S"] = p["O"] + 1.3 * (p["O"] - p["P"])
    p["R"] = p["O"] + 1.3 * (p["O"] - p["Q"])
    poly(ax, [p["P"], p["O"], p["Q"]], fc=SOFT)
    poly(ax, [p["S"], p["O"], p["R"]], fc="#F6EEDC")
    dots(ax, p, "PQORS")
    label(ax, p, "PQRS", centre=p["O"])
    ax.annotate("O", p["O"], textcoords="offset points", xytext=(12, 0), ha="center", va="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig11_bowtie.png")


# Fig 6.12: Example 5 - find angle P
def fig_example5():
    fig, axs = plt.subplots(1, 2, figsize=(6.6, 2.9), gridspec_kw={"width_ratios": [1, 1.7]})
    a, b, c = 6.0, 3 * np.sqrt(3), 3.8  # BC, CA, AB
    # triangle ABC: B at origin, C on x-axis
    B, C = P(0, 0), P(a, 0)
    cosB = (c * c + a * a - b * b) / (2 * c * a)
    A = P(c * cosB, c * np.sqrt(1 - cosB ** 2))
    ax = axs[0]
    p = {"A": A, "B": B, "C": C}
    poly(ax, [A, B, C])
    label(ax, p, "ABC")
    side_text(ax, A, B, "3.8", 0.42, centre=(A + B + C) / 3)
    side_text(ax, B, C, "6", 0.38, centre=(A + B + C) / 3)
    side_text(ax, A, C, r"$3\sqrt{3}$", 0.62, centre=(A + B + C) / 3)
    angle(ax, A, B, C, 0.45, "80°")
    angle(ax, B, C, A, 0.55, "60°")
    finish(ax)
    ax = axs[1]
    s = 2.0
    Q, R = P(0, 0), P(2 * a * 0 + 12 * 0 + 7.6 * 0, 0)
    # triangle PQR with RQ = 7.6, QP = 12, PR = 6*sqrt(3): R at origin, Q on the x-axis
    R, Q = P(0, 0), P(7.6, 0)
    cosR = (7.6 ** 2 + (6 * np.sqrt(3)) ** 2 - 12 ** 2) / (2 * 7.6 * 6 * np.sqrt(3))
    Pp = P(6 * np.sqrt(3) * cosR, 6 * np.sqrt(3) * np.sqrt(1 - cosR ** 2))
    q = {"P": Pp, "Q": Q, "R": R}
    poly(ax, [Pp, Q, R])
    label(ax, q, "PQR")
    cen = (Pp + Q + R) / 3
    side_text(ax, R, Q, "7.6", 0.6, centre=cen)
    side_text(ax, Q, Pp, "12", 0.7, centre=cen)
    side_text(ax, R, Pp, r"$6\sqrt{3}$", 1.0, centre=cen)
    angle(ax, Pp, Q, R, 0.9, "?", tr=1.35, size=10)
    finish(ax)
    save(fig, "ch06_fig12_example5.png")


# Fig 6.13: Example 6 - lines AB and CD meet at O, with OA.OB = OC.OD
def fig_example6():
    fig, ax = plt.subplots(figsize=(3.4, 2.8))
    u1 = P(np.cos(np.radians(150)), np.sin(np.radians(150)))
    u2 = P(np.cos(np.radians(208)), np.sin(np.radians(208)))
    O = P(0, 0)
    p = {"O": O, "A": 2.0 * u1, "B": -2.4 * u1, "D": 1.6 * u2, "C": -3.0 * u2}
    seg(ax, p["A"], p["B"], INK, 1.2)
    seg(ax, p["C"], p["D"], INK, 1.2)
    seg(ax, p["A"], p["D"], ACC, 1.4)
    seg(ax, p["C"], p["B"], ACC, 1.4)
    dots(ax, p, "OABCD")
    label(ax, p, "ABCD", centre=O)
    ax.annotate("O", O, textcoords="offset points", xytext=(-2, -13), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig13_example6.png")


# Fig 6.14: Example 7 - lamp-post and the girl's shadow
def fig_lamp():
    fig, ax = plt.subplots(figsize=(4.6, 2.8))
    p = {"A": P(0, 3.6), "B": P(0, 0), "C": P(4.8, 0.9), "D": P(4.8, 0), "E": P(6.4, 0)}
    seg(ax, P(-0.4, 0), P(7, 0), GREY, 1)
    seg(ax, p["A"], p["B"], INK, 2.2)
    seg(ax, p["C"], p["D"], ACC, 2.2)
    seg(ax, p["A"], p["E"], HI, 1, "--")
    ax.plot(*p["A"], "o", ms=7, color="#F2C14E", mec=INK)
    right(ax, p["B"], p["A"], p["E"], 0.25)
    right(ax, p["D"], p["C"], p["E"], 0.18)
    ax.text(-0.25, 1.8, "3.6 m", ha="right", va="center", fontsize=9)
    ax.text(4.6, 0.45, "0.9 m", ha="right", va="center", fontsize=9, color=ACC)
    ax.text(2.4, -0.35, "4.8 m", ha="center", fontsize=9)
    ax.text(5.6, -0.35, "$x$", ha="center", fontsize=10)
    for n, off in [("A", (-10, 6)), ("B", (-8, -10)), ("C", (8, 6)), ("D", (0, -16)), ("E", (6, -10))]:
        ax.annotate(n, p[n], textcoords="offset points", xytext=off, ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig14_lamp_post.png")


# Fig 6.15: Ex 6.3 Q2 - triangles ODC and OBA
def fig_ex63_q2():
    fig, ax = plt.subplots(figsize=(3.8, 3.4))
    O = P(0, 0)
    D, B = P(-2, 0), P(3, 0)
    oc = 2 * np.sin(np.radians(70)) / np.sin(np.radians(55))
    C = oc * P(np.cos(np.radians(125)), np.sin(np.radians(125)))
    A = 1.5 * oc * P(np.cos(np.radians(-55)), np.sin(np.radians(-55)))
    p = {"O": O, "D": D, "B": B, "C": C, "A": A}
    seg(ax, D, B)
    seg(ax, C, A)
    seg(ax, D, C, ACC, 1.5)
    seg(ax, A, B, ACC, 1.5)
    angle(ax, O, B, C, 0.4, "125°", tr=0.75)
    angle(ax, D, O, C, 0.4, "70°", tr=0.7)
    dots(ax, p, "ODBCA")
    label(ax, p, "DBCA", centre=O)
    ax.annotate("O", O, textcoords="offset points", xytext=(-10, -11), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig15_ex63_q2.png")


# Fig 6.16: Ex 6.3 Q4 - QR/QS = QT/PR and angle 1 = angle 2
def fig_ex63_q4():
    fig, ax = plt.subplots(figsize=(3.2, 3.6))
    p = {"Q": P(0, 0), "R": P(4.4, 0), "P": P(2.2, 2.6)}
    p["S"] = P(3.0, 0)
    p["T"] = p["Q"] + 1.6 * (p["P"] - p["Q"])
    poly(ax, [p["T"], p["Q"], p["R"]], fc="white")
    seg(ax, p["P"], p["R"])
    seg(ax, p["P"], p["S"], ACC, 1.4)
    angle(ax, p["Q"], p["R"], p["P"], 0.45, "1", tr=0.7)
    angle(ax, p["R"], p["P"], p["Q"], 0.45, "2", tr=0.7)
    dots(ax, p, "PQRST")
    label(ax, p, "QRT", centre=P(2.4, 1.4))
    ax.annotate("P", p["P"], textcoords="offset points", xytext=(-10, 4), ha="center", fontsize=11)
    ax.annotate("S", p["S"], textcoords="offset points", xytext=(0, -12), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig16_ex63_q4.png")


# Fig 6.17: Ex 6.3 Q6 - triangle ABE congruent to triangle ACD
def fig_ex63_q6():
    fig, ax = plt.subplots(figsize=(3.2, 3.0))
    p = {"A": P(2.4, 4), "B": P(0, 0), "C": P(4.8, 0)}
    p["D"] = p["A"] + 0.42 * (p["B"] - p["A"])
    p["E"] = p["A"] + 0.42 * (p["C"] - p["A"])
    poly(ax, [p["A"], p["B"], p["C"]])
    seg(ax, p["B"], p["E"], ACC, 1.3)
    seg(ax, p["C"], p["D"], ACC, 1.3)
    seg(ax, p["D"], p["E"], GREY, 1, "--")
    dots(ax, p, "ABCDE")
    label(ax, p, "ABCDE", centre=P(2.4, 1.4))
    finish(ax)
    save(fig, "ch06_fig17_ex63_q6.png")


# Fig 6.18: Ex 6.3 Q7 - altitudes AD and CE meet at P
def fig_ex63_q7():
    fig, ax = plt.subplots(figsize=(3.6, 3.0))
    p = {"A": P(1.6, 3.8), "B": P(0, 0), "C": P(5, 0)}
    p["D"] = foot(p["A"], p["B"], p["C"])
    p["E"] = foot(p["C"], p["A"], p["B"])
    p["P"] = meet(p["A"], p["D"], p["C"], p["E"])
    poly(ax, [p["A"], p["B"], p["C"]])
    seg(ax, p["A"], p["D"], ACC, 1.3)
    seg(ax, p["C"], p["E"], ACC, 1.3)
    right(ax, p["D"], p["A"], p["C"], 0.22)
    right(ax, p["E"], p["C"], p["A"], 0.22)
    dots(ax, p, "ABCDEP")
    label(ax, p, "ABCDE", centre=P(2.2, 1.4))
    ax.annotate("P", p["P"], textcoords="offset points", xytext=(9, 4), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig18_ex63_q7.png")


# Fig 6.19: Ex 6.3 Q8 - parallelogram ABCD, E on AD produced, BE meets CD at F
def fig_ex63_q8():
    fig, ax = plt.subplots(figsize=(3.8, 3.0))
    p = {"A": P(0, 0), "B": P(4, 0), "C": P(5.2, 2.4), "D": P(1.2, 2.4)}
    p["E"] = p["A"] + 1.6 * (p["D"] - p["A"])
    p["F"] = meet(p["B"], p["E"], p["C"], p["D"])
    poly(ax, [p["A"], p["B"], p["C"], p["D"]])
    seg(ax, p["D"], p["E"], INK, 1.3)
    seg(ax, p["B"], p["E"], ACC, 1.4)
    dots(ax, p, "ABCDEF")
    label(ax, p, "ABCE", centre=P(2.6, 1.6))
    ax.annotate("D", p["D"], textcoords="offset points", xytext=(-10, 2), ha="center", fontsize=11)
    ax.annotate("F", p["F"], textcoords="offset points", xytext=(6, 9), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig19_ex63_q8.png")


# Fig 6.20: Ex 6.3 Q9 (SSLC 2026 Q51) - right triangles ABC and AMP
def fig_ex63_q9():
    fig, ax = plt.subplots(figsize=(3.8, 2.8))
    p = {"A": P(0, 0), "B": P(4, 0), "C": P(4, 3.4), "P": P(5.6, 0)}
    p["M"] = foot(p["P"], p["A"], p["C"])
    seg(ax, p["A"], p["P"])
    seg(ax, p["A"], p["C"])
    seg(ax, p["B"], p["C"])
    seg(ax, p["P"], p["M"])
    right(ax, p["B"], p["A"], p["C"], 0.22)
    right(ax, p["M"], p["A"], p["P"], 0.22)
    dots(ax, p, "ABCPM")
    label(ax, p, "ABCP", centre=P(3.4, 1.2))
    ax.annotate("M", p["M"], textcoords="offset points", xytext=(-9, 6), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig20_ex63_q9.png")


# Fig 6.21: Ex 6.3 Q11 - isosceles ABC, E on CB produced, AD perpendicular BC, EF perpendicular AC
def fig_ex63_q11():
    fig, ax = plt.subplots(figsize=(4.0, 2.8))
    p = {"B": P(2, 0), "C": P(6, 0), "A": P(4, 3.5), "E": P(0.4, 0)}
    p["D"] = foot(p["A"], p["B"], p["C"])
    p["F"] = foot(p["E"], p["A"], p["C"])
    poly(ax, [p["A"], p["B"], p["C"]])
    seg(ax, p["E"], p["B"])
    seg(ax, p["A"], p["D"], ACC, 1.3)
    seg(ax, p["E"], p["F"], ACC, 1.3)
    right(ax, p["D"], p["A"], p["C"], 0.22)
    right(ax, p["F"], p["E"], p["C"], 0.22)
    dots(ax, p, "ABCDEF")
    label(ax, p, "ABCDE", centre=P(3.5, 1.2))
    ax.annotate("F", p["F"], textcoords="offset points", xytext=(8, 6), ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig21_ex63_q11.png")


# Fig 6.22: Ex 6.3 Q13 - D on BC with angle ADC = angle BAC
def fig_ex63_q13():
    fig, ax = plt.subplots(figsize=(3.8, 2.6))
    p = {"A": P(1.5, 3), "B": P(0, 0), "C": P(5, 0)}
    cd = (np.linalg.norm(p["C"] - p["A"]) ** 2) / 5
    p["D"] = P(5 - cd, 0)
    poly(ax, [p["A"], p["B"], p["C"]])
    seg(ax, p["A"], p["D"], ACC, 1.4)
    angle(ax, p["A"], p["B"], p["C"], 0.45)
    angle(ax, p["D"], p["C"], p["A"], 0.45)
    dots(ax, p, "ABCD")
    label(ax, p, "ABCD", centre=P(2.2, 1.0))
    finish(ax)
    save(fig, "ch06_fig22_ex63_q13.png")


# Fig 6.23: SSLC sample paper - PA, QB, RC perpendicular to AC (1/x + 1/y = 1/z)
def fig_sample_q53():
    fig, ax = plt.subplots(figsize=(4.4, 2.8))
    p = {"A": P(0, 0), "C": P(6, 0), "P": P(0, 3), "R": P(6, 2)}
    p["Q"] = meet(p["P"], p["C"], p["A"], p["R"])
    p["B"] = P(p["Q"][0], 0)
    seg(ax, p["A"], p["C"])
    for top, bot in [("P", "A"), ("Q", "B"), ("R", "C")]:
        seg(ax, p[top], p[bot], ACC, 1.5)
    seg(ax, p["P"], p["C"], GREY, 1.1)
    seg(ax, p["A"], p["R"], GREY, 1.1)
    right(ax, p["A"], p["P"], p["C"], 0.22)
    right(ax, p["B"], p["Q"], p["C"], 0.22)
    right(ax, p["C"], p["R"], p["A"], 0.22)
    dots(ax, p, "ABCPQR")
    for n, off in [("A", (-8, -10)), ("B", (0, -13)), ("C", (8, -10)), ("P", (-8, 6)), ("Q", (0, 10)), ("R", (8, 6))]:
        ax.annotate(n, p[n], textcoords="offset points", xytext=off, ha="center", fontsize=11)
    ax.text(-0.25, 1.5, "$x$", ha="right", va="center", fontsize=11, color=ACC)
    ax.text(p["B"][0] + 0.18, 0.55, "$z$", ha="left", va="center", fontsize=11, color=ACC)
    ax.text(6.25, 1.0, "$y$", ha="left", va="center", fontsize=11, color=ACC)
    ax.text(p["B"][0] / 2, -0.45, "$a$", ha="center", fontsize=11)
    ax.text((p["B"][0] + 6) / 2, -0.45, "$b$", ha="center", fontsize=11)
    finish(ax)
    save(fig, "ch06_fig23_three_perpendiculars.png")


if __name__ == "__main__":
    fig_not_similar()
    fig_bpt()
    fig_trapezium_ef()
    fig_example3()
    fig_ex62_q1()
    fig_ex62_q3()
    fig_ex62_q4()
    fig_ex62_q5()
    fig_ex62_q6()
    fig_trapezium_o()
    fig_bowtie()
    fig_example5()
    fig_example6()
    fig_lamp()
    fig_ex63_q2()
    fig_ex63_q4()
    fig_ex63_q6()
    fig_ex63_q7()
    fig_ex63_q8()
    fig_ex63_q9()
    fig_ex63_q11()
    fig_ex63_q13()
    fig_sample_q53()
