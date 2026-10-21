"""Figures for Class X Mathematics, Chapter 7: Coordinate Geometry.
Run: python x_ch07_coordinate_geometry.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, GRID = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#DDE3EA"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def axes(ax, xr, yr, grid=True, ticks=True, step=1, o_above=False):
    """Draw x and y axes through the origin over the ranges xr, yr, with an optional unit grid.
    o_above puts the O label above-right of the origin instead of below-left."""
    x0, x1 = xr
    y0, y1 = yr
    if grid:
        for gx in np.arange(np.ceil(x0), x1 + 0.01, step):
            ax.plot([gx, gx], [y0, y1], color=GRID, lw=0.6, zorder=0)
        for gy in np.arange(np.ceil(y0), y1 + 0.01, step):
            ax.plot([x0, x1], [gy, gy], color=GRID, lw=0.6, zorder=0)
    ax.annotate("", xy=(x1 + 0.3, 0), xytext=(x0 - 0.3, 0), arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.annotate("", xy=(0, y1 + 0.3), xytext=(0, y0 - 0.3), arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.text(x1 + 0.45, -0.1, "X", fontsize=10, va="center")
    ax.text(0.1, y1 + 0.5, "Y", fontsize=10, ha="left")
    if o_above:
        ax.text(0.15, 0.15, "O", fontsize=10, ha="left", va="bottom")
    else:
        ax.text(-0.15, -0.15, "O", fontsize=10, ha="right", va="top")
    if ticks:
        for t in range(int(np.ceil(x0)), int(x1) + 1, step):
            if t != 0:
                ax.text(t, -0.3, str(t), ha="center", va="top", fontsize=7.5, color=GREY)
        for t in range(int(np.ceil(y0)), int(y1) + 1, step):
            if t != 0:
                ax.text(-0.2, t, str(t), ha="right", va="center", fontsize=7.5, color=GREY)
    ax.set_xlim(x0 - 0.6, x1 + 0.9)
    ax.set_ylim(y0 - 0.6, y1 + 0.9)
    ax.set_aspect("equal")
    ax.axis("off")


def pt(ax, x, y, name, off=(6, 6), color=ACC, size=10):
    ax.plot(x, y, "o", ms=4, color=color, zorder=5)
    ax.annotate(name, (x, y), textcoords="offset points", xytext=off, fontsize=size, color=INK,
                ha="left" if off[0] >= 0 else "right", zorder=6)


# Fig 7.1: town B is 36 km east and 15 km north of town A
def fig_towns():
    fig, ax = plt.subplots(figsize=(4.4, 2.4))
    A, B, C = np.array([0, 0]), np.array([36, 15]), np.array([36, 0])
    ax.plot(*zip(A, C), color=INK, lw=1.2)
    ax.plot(*zip(C, B), color=INK, lw=1.2)
    ax.plot(*zip(A, B), color=ACC, lw=1.8)
    ax.plot(*zip(C + [-1.6, 0], C + [-1.6, 1.6], C + [0, 1.6]), color=INK, lw=0.9)
    for p, n, off in [(A, "A", (-10, -4)), (B, "B", (6, 2))]:
        ax.plot(*p, "o", ms=4, color=HI)
        ax.annotate(n, p, textcoords="offset points", xytext=off, fontsize=11)
    ax.text(18, -2.2, "36 km (east)", ha="center", fontsize=9)
    ax.text(37.2, 7.5, "15 km\n(north)", ha="left", va="center", fontsize=9)
    ax.text(16, 9.2, "?", fontsize=12, color=ACC, ha="center")
    ax.set_xlim(-3, 46); ax.set_ylim(-4, 18); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch07_fig01_two_towns.png")


# Fig 7.2: deriving the distance formula
def fig_distance():
    fig, ax = plt.subplots(figsize=(4.2, 3.4))
    axes(ax, (0, 7), (0, 5.5), grid=False, ticks=False)
    P, Q = np.array([1.5, 1.5]), np.array([5.5, 4.5])
    R, S, T = np.array([1.5, 0]), np.array([5.5, 0]), np.array([5.5, 1.5])
    ax.plot(*zip(P, R), color=GREY, lw=1, ls="--")
    ax.plot(*zip(Q, S), color=GREY, lw=1, ls="--")
    ax.plot(*zip(P, T), color=INK, lw=1.2)
    ax.plot(*zip(T, Q), color=INK, lw=1.2)
    ax.plot(*zip(P, Q), color=ACC, lw=1.8)
    ax.plot(*zip(T + [-0.22, 0], T + [-0.22, 0.22], T + [0, 0.22]), color=INK, lw=0.9)
    pt(ax, *P, r"P$(x_1, y_1)$", (-6, 8), color=HI)
    ax.texts[-1].set_ha("right")
    pt(ax, *Q, r"Q$(x_2, y_2)$", (-4, 8), color=HI)
    ax.texts[-1].set_ha("right")
    for p, n, off in [(R, "R", (-4, -13)), (S, "S", (-4, -13)), (T, "T", (5, -10))]:
        ax.annotate(n, p, textcoords="offset points", xytext=off, fontsize=10)
    ax.text(3.5, 1.15, r"$x_2 - x_1$", ha="center", fontsize=10, color=INK)
    ax.text(5.7, 3.0, r"$y_2 - y_1$", ha="left", va="center", fontsize=10, color=INK)
    save(fig, "ch07_fig02_distance_formula.png")


# Fig 7.3: four friends in a classroom at A(3, 4), B(6, 7), C(9, 4), D(6, 1)
def fig_classroom():
    fig, ax = plt.subplots(figsize=(4.0, 3.6))
    axes(ax, (0, 10), (0, 8))
    pts = {"A": (3, 4), "B": (6, 7), "C": (9, 4), "D": (6, 1)}
    xy = np.array(list(pts.values()) + [pts["A"]])
    ax.plot(xy[:, 0], xy[:, 1], color=ACC, lw=1.4)
    for n, off in [("A", (-12, 2)), ("B", (2, 6)), ("C", (6, 2)), ("D", (4, -12))]:
        pt(ax, *pts[n], n, off, color=HI)
    save(fig, "ch07_fig03_classroom.png")


# Fig 7.4: deriving the section formula
def fig_section():
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    axes(ax, (0, 8), (0, 5.5), grid=False, ticks=False)
    A, B = np.array([1.2, 1.2]), np.array([7, 4.8])
    m1, m2 = 2, 1.4
    P = (m1 * B + m2 * A) / (m1 + m2)
    Q, C = np.array([P[0], A[1]]), np.array([B[0], P[1]])
    for p in (A, P, B):
        ax.plot([p[0], p[0]], [0, p[1]], color=GREY, lw=0.9, ls="--")
    ax.plot(*zip(A, Q), color=INK, lw=1.1)
    ax.plot(*zip(P, C), color=INK, lw=1.1)
    ax.plot(*zip(Q, P), color=INK, lw=1.1)
    ax.plot(*zip(C, B), color=INK, lw=1.1)
    ax.plot(*zip(A, B), color=ACC, lw=1.8)
    pt(ax, *A, r"A$(x_1, y_1)$", (8, -14), color=HI)
    pt(ax, *P, r"P$(x, y)$", (-4, 8), color=HI)
    ax.texts[-1].set_ha("right")
    pt(ax, *B, r"B$(x_2, y_2)$", (-4, 8), color=HI)
    ax.texts[-1].set_ha("right")
    ax.annotate("Q", Q, textcoords="offset points", xytext=(3, -12), fontsize=10)
    ax.annotate("C", C, textcoords="offset points", xytext=(3, -12), fontsize=10)
    ax.text(*((A + P) / 2 + np.array([0.15, -0.35])), r"$m_1$", fontsize=11, color=ACC)
    ax.text(*((P + B) / 2 + np.array([0.15, -0.35])), r"$m_2$", fontsize=11, color=ACC)
    for x, n in [(A[0], "R"), (P[0], "S"), (B[0], "T")]:
        ax.text(x, -0.35, n, ha="center", va="top", fontsize=10)
    save(fig, "ch07_fig04_section_formula.png")


# Fig 7.5: Example 4 - points equidistant from A(7, 1) and B(3, 5) lie on x - y = 2
def fig_bisector():
    fig, ax = plt.subplots(figsize=(3.8, 3.6))
    axes(ax, (-1, 8), (-2, 7))
    xs = np.array([-0.5, 8])
    ax.plot(xs, xs - 2, color=HI, lw=1.5)
    ax.text(6.4, 5.9, "$x - y = 2$", fontsize=10, color=HI, ha="right")
    ax.plot([7, 3], [1, 5], color=ACC, lw=1.4)
    pt(ax, 7, 1, "A(7, 1)", (5, -12), color=ACC)
    pt(ax, 3, 5, "B(3, 5)", (-6, 6), color=ACC)
    ax.texts[-1].set_ha("right")
    pt(ax, 5, 3, "M(5, 3)", (8, -13), color=INK, size=9)
    save(fig, "ch07_fig05_perpendicular_bisector.png")


# Fig 7.6: Ex 7.2 Q3 - sports ground with flags on the 2nd and 8th lines
def fig_sports():
    fig, ax = plt.subplots(figsize=(4.4, 3.8))
    for k in range(0, 11):
        ax.plot([k, k], [0, 30], color=GRID if k else INK, lw=0.8 if k else 1.2)
    ax.plot([0, 10.5], [0, 0], color=INK, lw=1.2)
    for yy in range(0, 31, 5):
        ax.text(-0.3, yy, f"{yy} m", ha="right", va="center", fontsize=7.5, color=GREY)
    for k in range(1, 11):
        ax.text(k, -1.2, str(k), ha="center", va="top", fontsize=7.5, color=GREY)
    ax.text(5, -3.6, "line number (1 m apart)", ha="center", fontsize=8.5)
    ax.text(-2.6, 15, "distance along AD", rotation=90, ha="center", va="center", fontsize=8.5)
    # (x, y, colour, label, label position)
    for (x, y, c, n, lx, ly) in [(2, 25, "#2E8B57", "green (2, 25)", 1.2, 28.6), (8, 20, "#C0392B", "red (8, 20)", 8.0, 17.4),
                                 (5, 22.5, ACC, "blue (5, 22.5)", 4.6, 26.6)]:
        ax.plot([x, x], [y, y + 2.4], color=INK, lw=1)
        ax.fill([x, x + 1.0, x], [y + 2.4, y + 1.9, y + 1.4], color=c)
        ax.plot(x, y, "o", ms=3.5, color=INK)
        ax.text(lx, ly, n, fontsize=8, ha="left", va="bottom" if ly > y else "top",
                bbox=dict(fc="white", ec="none", pad=0.6))
    ax.plot([2, 8], [25, 20], color=GREY, lw=1, ls="--")
    ax.text(0.15, 30.6, "A", fontsize=10)
    ax.set_xlim(-3.2, 11.2); ax.set_ylim(-4.4, 32); ax.set_aspect(0.3); ax.axis("off")
    save(fig, "ch07_fig06_sports_ground.png")


# Fig 7.7: Example 8 - points of trisection of A(2, -2) and B(-7, 4)
def fig_trisection():
    fig, ax = plt.subplots(figsize=(4.2, 3.0))
    axes(ax, (-8, 3), (-3, 5), ticks=False, o_above=True)
    A, B = np.array([2, -2]), np.array([-7, 4])
    P, Q = (2 * A + B) / 3, (A + 2 * B) / 3
    ax.plot(*zip(A, B), color=ACC, lw=1.6)
    pt(ax, *A, "A(2, −2)", (5, -10), color=HI)
    pt(ax, *B, "B(−7, 4)", (-5, 5), color=HI)
    ax.texts[-1].set_ha("right")
    pt(ax, *P, "P(−1, 0)", (-6, -13), color=INK, size=9)
    pt(ax, *Q, "Q(−4, 2)", (4, 6), color=INK, size=9)
    save(fig, "ch07_fig07_trisection.png")


# Fig 7.8: Example 3 - Ashima, Bharti and Camella at A(3, 1), B(6, 4), C(8, 6)
def fig_desks():
    fig, ax = plt.subplots(figsize=(3.6, 3.2))
    axes(ax, (0, 9), (0, 7))
    ax.plot([3, 8], [1, 6], color=ACC, lw=1.2, ls="--")
    for (x, y, n, off) in [(3, 1, "A(3, 1)", (6, -8)), (6, 4, "B(6, 4)", (6, -8)), (8, 6, "C(8, 6)", (-6, 6))]:
        pt(ax, x, y, n, off, color=HI, size=9)
        if off[0] < 0:
            ax.texts[-1].set_ha("right")
    save(fig, "ch07_fig08_desks.png")


if __name__ == "__main__":
    fig_towns()
    fig_distance()
    fig_classroom()
    fig_section()
    fig_bisector()
    fig_sports()
    fig_trisection()
    fig_desks()
