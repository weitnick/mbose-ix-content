"""Figures for Class X Science, Chapter 12: Magnetic Effects of Electric Current.
Run: python x_sci_ch12_magnetic.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
Field-line pictures are computed from the field of the sources (dipole, wire pairs, current sheets) with streamplot.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_sci_ch05_life_processes import ACC, GREY, HI, INK, SOFT, finish, label, save
from x_sci_ch11_electricity import comp, dot, draw_symbol, wire
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle

NRED, SBLUE = "#D9534F", "#4A7BD0"
FIELD = "#2E6DB4"


def wire_field(X, Y, wires):
    """2D field of long straight wires: list of (x, y, I) with I > 0 out of the page."""
    Bx = np.zeros_like(X)
    By = np.zeros_like(Y)
    for x0, y0, I in wires:
        dx, dy = X - x0, Y - y0
        r2 = dx * dx + dy * dy + 1e-6
        Bx += -I * dy / r2
        By += I * dx / r2
    return Bx, By


def current_mark(ax, p, out, r=0.12):
    ax.add_patch(Circle(p, r, fc="white", ec=INK, lw=1.0, zorder=6))
    if out:
        ax.add_patch(Circle(p, r * 0.3, fc=INK, ec=INK, zorder=7))
    else:
        d = r * 0.6
        ax.plot([p[0] - d, p[0] + d], [p[1] - d, p[1] + d], color=INK, lw=1.0, zorder=7)
        ax.plot([p[0] - d, p[0] + d], [p[1] + d, p[1] - d], color=INK, lw=1.0, zorder=7)


# Fig 12.1: field lines around a bar magnet
def fig_bar_magnet():
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    a = 1.3
    x = np.linspace(-5, 5, 300)
    y = np.linspace(-3.6, 3.6, 220)
    X, Y = np.meshgrid(x, y)
    Bx = np.zeros_like(X)
    By = np.zeros_like(Y)
    for q, x0 in ((1, a), (-1, -a)):
        dx, dy = X - x0, Y
        r3 = (dx * dx + dy * dy) ** 1.5 + 1e-3
        Bx += q * dx / r3
        By += q * dy / r3
    inside = (np.abs(X) < a + 0.05) & (np.abs(Y) < 0.42)
    starts = [(a + 0.32 * math.cos(t), 0.32 * math.sin(t)) for t in np.radians(np.linspace(-150, 150, 14))]
    ax.streamplot(X, Y, Bx, By, start_points=starts, color=FIELD, linewidth=1.0, arrowsize=1.0, density=6,
                  integration_direction="forward", broken_streamlines=False)
    ax.add_patch(Rectangle((-a - 0.25, -0.4), a + 0.25, 0.8, fc=SBLUE, ec=INK, lw=1.2, zorder=5))
    ax.add_patch(Rectangle((0, -0.4), a + 0.25, 0.8, fc=NRED, ec=INK, lw=1.2, zorder=5))
    ax.text(a - 0.15, 0, "N", color="white", fontsize=13, fontweight="bold", ha="center", va="center", zorder=6)
    ax.text(-a + 0.15, 0, "S", color="white", fontsize=13, fontweight="bold", ha="center", va="center", zorder=6)
    finish(ax, (-5, 5), (-3.6, 3.6))
    save(fig, "sci_ch12_fig01_bar_magnet.png")


# Fig 12.2: field around a straight wire and the right-hand thumb rule
def fig_straight_wire():
    fig, axs = plt.subplots(1, 2, figsize=(8.0, 3.9))
    ax = axs[0]
    for r in (0.5, 0.9, 1.4, 2.0):
        ax.add_patch(Circle((0, 0), r, fc="none", ec=FIELD, lw=1.1))
        for t in (90, 270):
            a = math.radians(t)
            p = (r * math.cos(a), r * math.sin(a))
            d = (-math.sin(a), math.cos(a))
            ax.annotate("", xy=(p[0] + 0.12 * d[0], p[1] + 0.12 * d[1]), xytext=p,
                        arrowprops=dict(arrowstyle="-|>", color=FIELD, lw=1.1, mutation_scale=11))
    current_mark(ax, (0, 0), True, 0.16)
    ax.text(0, -2.35, "(a) concentric field lines; current out of the page (⊙)", ha="center", fontsize=8.5)
    ax.plot([1.4 * math.cos(math.radians(35))], [1.4 * math.sin(math.radians(35))], "o", ms=4, color=HI)
    ax.text(1.4 * math.cos(math.radians(35)) + 0.12, 1.4 * math.sin(math.radians(35)) + 0.05, "P", fontsize=8.5)
    ax.plot([2.0 * math.cos(math.radians(-30))], [2.0 * math.sin(math.radians(-30))], "o", ms=4, color=HI)
    ax.text(2.0 * math.cos(math.radians(-30)) + 0.12, 2.0 * math.sin(math.radians(-30)), "Q (farther: weaker field)", fontsize=8)
    finish(ax, (-2.4, 3.6), (-2.6, 2.3))
    ax = axs[1]
    ax.annotate("", xy=(0, 2.0), xytext=(0, -2.0), arrowprops=dict(arrowstyle="-|>", color=HI, lw=2.4, mutation_scale=16))
    ax.text(0.15, 1.9, "current (thumb)", fontsize=8.5, color=HI)
    for yc in (-0.9, 0.0, 0.9):
        t = np.linspace(0, 2 * np.pi, 100)
        xs, ys = 0.8 * np.cos(t), yc + 0.22 * np.sin(t)
        front = np.sin(t) < 0
        ax.plot(np.where(front, xs, np.nan), np.where(front, ys, np.nan), color=FIELD, lw=1.4, zorder=5)
        ax.plot(np.where(~front, xs, np.nan), np.where(~front, ys, np.nan), color=FIELD, lw=1.0, ls=(0, (3, 2)), zorder=1)
        ax.annotate("", xy=(0.15, yc - 0.218), xytext=(-0.1, yc - 0.22),
                    arrowprops=dict(arrowstyle="-|>", color=FIELD, lw=1.3, mutation_scale=12), zorder=6)
    ax.text(0.95, -0.9, "field lines\n(curled fingers)", fontsize=8.5, color=FIELD, va="center")
    ax.text(0, -2.35, "(b) right-hand thumb rule", ha="center", fontsize=8.5)
    finish(ax, (-2.0, 2.6), (-2.6, 2.3))
    save(fig, "sci_ch12_fig02_straight_wire.png")


# Fig 12.3: field of a current-carrying circular loop (section through the loop)
def fig_loop():
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    d = 1.0
    # field lines of two antiparallel currents at (0, +d) and (0, -d) are circles centred at (0, c), radius sqrt(c^2 - d^2)
    t = np.linspace(0, 2 * np.pi, 300)
    for s in (1, -1):
        for c in (1.08, 1.3, 1.7, 2.6, 4.5, 9.0):
            r = math.sqrt(c * c - d * d)
            cy = s * c
            ax.plot(r * np.cos(t), cy + r * np.sin(t), color=FIELD, lw=1.0, zorder=2)
            yb = cy - s * r   # point of the circle nearest the centre of the loop
            if abs(yb) < 2.3:
                ax.annotate("", xy=(-0.12, yb), xytext=(0.0, yb),
                            arrowprops=dict(arrowstyle="-|>", color=FIELD, lw=1.0, mutation_scale=10), zorder=3)
            yt = cy + s * r
            if abs(yt) < 2.3:
                ax.annotate("", xy=(0.12, yt), xytext=(0.0, yt),
                            arrowprops=dict(arrowstyle="-|>", color=FIELD, lw=1.0, mutation_scale=10), zorder=3)
    ax.plot([-3, 3], [0, 0], color=FIELD, lw=1.0)
    ax.annotate("", xy=(-1.6, 0), xytext=(-1.45, 0), arrowprops=dict(arrowstyle="-|>", color=FIELD, lw=1.0, mutation_scale=10))
    ax.add_patch(Ellipse((0, 0), 0.5, 2.0, fc="none", ec=GREY, lw=1.0, ls=(0, (4, 3))))
    current_mark(ax, (0, 1.0), False, 0.14)
    current_mark(ax, (0, -1.0), True, 0.14)
    ax.text(0.25, 1.15, "current into the page", fontsize=8)
    ax.text(0.25, -1.2, "current out of the page", fontsize=8)
    ax.text(-2.9, 2.2, "field lines are nearly straight\nat the centre of the loop", fontsize=8, color=FIELD, va="top")
    finish(ax, (-3, 3), (-2.4, 2.4))
    save(fig, "sci_ch12_fig03_loop.png")


# Fig 12.4: field of a current-carrying solenoid
def fig_solenoid():
    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    R, half = 0.8, 2.0
    xs = np.linspace(-half, half, 16)
    wires = [(x0, R, -1.0) for x0 in xs] + [(x0, -R, 1.0) for x0 in xs]
    x = np.linspace(-5.2, 5.2, 320)
    y = np.linspace(-3.2, 3.2, 220)
    X, Y = np.meshgrid(x, y)
    Bx, By = wire_field(X, Y, wires)
    starts = [(0, yy) for yy in np.linspace(-0.45, 0.45, 5)]
    ax.streamplot(X, Y, Bx, By, start_points=starts, color=FIELD, linewidth=1.0, arrowsize=1.0, density=6,
                  broken_streamlines=False)
    for x0 in xs:
        current_mark(ax, (x0, R), False, 0.1)
        current_mark(ax, (x0, -R), True, 0.1)
    # with these currents the field inside points to the left, so the left end is the north pole
    ax.text(-half - 0.3, 0.05, "N", fontsize=13, fontweight="bold", color=NRED, ha="right", va="center")
    ax.text(half + 0.3, 0.05, "S", fontsize=13, fontweight="bold", color=SBLUE, ha="left", va="center")
    ax.text(0, -3.05, "inside: parallel straight lines (uniform field); outside: like a bar magnet", ha="center", fontsize=8.5)
    finish(ax, (-5.2, 5.2), (-3.2, 3.2))
    save(fig, "sci_ch12_fig04_solenoid.png")


def arrow3(ax, o, d, color, text, toff=(0.1, 0.1), lw=2.2):
    ax.annotate("", xy=(o[0] + d[0], o[1] + d[1]), xytext=o, arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=16))
    ax.text(o[0] + d[0] + toff[0], o[1] + d[1] + toff[1], text, color=color, fontsize=8.5, ha="center", va="center")


# Fig 12.5: Fleming's left-hand rule and the force on a current-carrying rod
def fig_fleming():
    fig, axs = plt.subplots(1, 2, figsize=(8.0, 3.8))
    ax = axs[0]
    o = (0, 0)
    arrow3(ax, o, (0, 1.8), "#C0392B", "thumb:\nFORCE (motion)", (0, 0.35))
    arrow3(ax, o, (1.9, 0), FIELD, "forefinger:\nFIELD", (0.1, -0.4))
    arrow3(ax, o, (-1.2, -1.0), "#1F7A3A", "middle finger:\nCURRENT", (-0.15, -0.35))
    ax.text(0, -1.95, "(a) Fleming's left-hand rule: the three\ndirections are mutually perpendicular", ha="center", fontsize=8.5)
    finish(ax, (-2.2, 2.6), (-2.3, 2.6))
    ax = axs[1]
    ax.add_patch(Rectangle((-1.2, 1.2), 2.4, 0.6, fc=SBLUE, ec=INK, lw=1.0))
    ax.add_patch(Rectangle((-1.2, -1.8), 2.4, 0.6, fc=NRED, ec=INK, lw=1.0))
    ax.text(0, 1.5, "S", color="white", fontweight="bold", ha="center", va="center", fontsize=12)
    ax.text(0, -1.5, "N", color="white", fontweight="bold", ha="center", va="center", fontsize=12)
    for xx in (-0.8, 0.8):
        ax.annotate("", xy=(xx, 1.1), xytext=(xx, -1.1), arrowprops=dict(arrowstyle="-|>", color=FIELD, lw=1.1, mutation_scale=11))
    ax.text(1.0, 0.75, "field\n(upwards)", fontsize=8, color=FIELD)
    current_mark(ax, (0, 0), False, 0.22)
    ax.text(0.3, -0.35, "rod AB: current\ninto the page (B to A)", fontsize=8)
    ax.annotate("", xy=(-1.2, 0), xytext=(-0.3, 0), arrowprops=dict(arrowstyle="-|>", color="#C0392B", lw=2.2, mutation_scale=15))
    ax.text(-1.25, 0.25, "force", color="#C0392B", fontsize=8.5)
    ax.text(0, -2.25, "(b) the rod is pushed sideways (to the left)", ha="center", fontsize=8.5)
    finish(ax, (-2.2, 2.4), (-2.5, 2.2))
    save(fig, "sci_ch12_fig05_fleming.png")


# Fig 12.6: a common domestic circuit
def fig_domestic():
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    LIVE, NEU, EARTH = "#C0392B", INK, "#1F7A3A"
    yl, yn, ye = 3.0, 1.0, -0.3
    ax.text(-0.3, yl, "live (red)", color=LIVE, ha="right", va="center", fontsize=8.5)
    ax.text(-0.3, yn, "neutral (black)", color=NEU, ha="right", va="center", fontsize=8.5)
    ax.text(-0.3, ye, "earth (green)", color=EARTH, ha="right", va="center", fontsize=8.5)
    ax.add_patch(Rectangle((0.2, 0.6), 1.2, 2.8, fc=SOFT, ec=INK, lw=1.0))
    ax.text(0.8, 2.0, "electricity\nmeter", ha="center", va="center", fontsize=8)
    ax.plot([0.0, 0.2], [yl, yl], color=LIVE, lw=1.6)
    ax.plot([0.0, 0.2], [yn, yn], color=NEU, lw=1.6)
    # main fuse on the live wire
    ax.plot([1.4, 1.8], [yl, yl], color=LIVE, lw=1.6)
    ax.add_patch(Rectangle((1.8, yl - 0.12), 0.5, 0.24, fc="white", ec=INK, lw=1.0, zorder=5))
    ax.text(2.05, yl + 0.25, "main fuse", ha="center", fontsize=8)
    ax.plot([2.3, 2.7], [yl, yl], color=LIVE, lw=1.6)
    ax.plot([1.4, 2.7], [yn, yn], color=NEU, lw=1.6)
    ax.add_patch(Rectangle((2.7, 0.6), 0.9, 2.8, fc="#FBF3E2", ec=INK, lw=1.0))
    ax.text(3.15, 2.0, "main\nswitch\nand\ndistri-\nbution\nbox", ha="center", va="center", fontsize=7.5)
    xs = [4.6, 6.0, 7.4, 8.8]
    ax.plot([3.6, 9.4], [yl, yl], color=LIVE, lw=1.6)
    ax.plot([3.6, 9.4], [yn, yn], color=NEU, lw=1.6)
    ax.plot([-0.1, 9.4], [ye, ye], color=EARTH, lw=1.6)
    names = ["bulb", "fan", "socket (15 A)", "refrigerator"]
    for x, name in zip(xs, names):
        ax.plot([x, x], [yl, 2.55], color=LIVE, lw=1.3)
        draw_symbol(ax, "switch_closed", (x, 2.35), math.pi / 2)
        ax.plot([x, x], [2.15, 2.0], color=INK, lw=1.3)
        if name == "bulb":
            draw_symbol(ax, "bulb", (x, 1.6), math.pi / 2)
        else:
            ax.add_patch(Rectangle((x - 0.25, 1.2), 0.5, 0.8, fc="white", ec=INK, lw=1.1, zorder=4))
            ax.plot([x, x], [1.2, 1.2], color=INK)
        ax.plot([x, x], [1.2, yn], color=NEU, lw=1.3)
        ax.text(x, 3.25, name, ha="center", fontsize=8)
        if name in ("refrigerator", "socket (15 A)"):
            ax.plot([x + 0.25, x + 0.45, x + 0.45], [1.5, 1.5, ye], color=EARTH, lw=1.1, ls=(0, (3, 2)))
            ax.plot([x + 0.45], [ye], "o", ms=3.5, color=EARTH)
    # earth plate
    ax.plot([-0.1, -0.1], [ye, -0.9], color=EARTH, lw=1.6)
    for k, w in enumerate((0.5, 0.34, 0.18)):
        ax.plot([-0.1 - w / 2, -0.1 + w / 2], [-0.9 - 0.1 * k, -0.9 - 0.1 * k], color=EARTH, lw=1.6)
    ax.text(0.1, -1.05, "metal plate buried deep in the earth", fontsize=8, color=EARTH, va="center")
    ax.text(5.6, -0.65, "appliances are connected in parallel between live and neutral;\n"
            "metal bodies are joined to the earth wire", ha="left", fontsize=8, va="top")
    finish(ax, (-1.9, 9.8), (-1.4, 3.5))
    save(fig, "sci_ch12_fig06_domestic.png")


# Fig 12.7 (supplement): a simple electric motor
def fig_motor():
    fig, ax = plt.subplots(figsize=(6.8, 5.0))
    ax.add_patch(Rectangle((-3.4, 0.6), 1.0, 2.2, fc=NRED, ec=INK, lw=1.2))
    ax.add_patch(Rectangle((2.4, 0.6), 1.0, 2.2, fc=SBLUE, ec=INK, lw=1.2))
    ax.text(-2.9, 1.7, "N", color="white", fontweight="bold", fontsize=14, ha="center", va="center")
    ax.text(2.9, 1.7, "S", color="white", fontweight="bold", fontsize=14, ha="center", va="center")
    A, B, C, D = (-1.6, 2.4), (-1.3, 1.0), (1.3, 1.0), (1.6, 2.4)
    ax.plot([A[0], B[0], C[0], D[0]], [A[1], B[1], C[1], D[1]], color="#B7791F", lw=3.0, zorder=4)
    ax.plot([A[0], -0.25], [A[1], A[1]], color="#B7791F", lw=3.0, zorder=4)
    ax.plot([D[0], 0.25], [D[1], D[1]], color="#B7791F", lw=3.0, zorder=4)
    for p, t in ((A, "A"), (B, "B"), (C, "C"), (D, "D")):
        ax.text(p[0] + (-0.2 if p[0] < 0 else 0.2), p[1] + 0.05, t, fontsize=9, ha="center", va="center")
    ax.plot([-0.25, -0.25, -0.12], [A[1], -0.15, -0.15], color="#B7791F", lw=2.0, zorder=4)
    ax.plot([0.25, 0.25, 0.12], [D[1], -0.15, -0.15], color="#B7791F", lw=2.0, zorder=4)
    from matplotlib.patches import Wedge
    ax.add_patch(Wedge((0, -0.55), 0.5, 100, 260, width=0.16, fc="#D9A441", ec=INK, lw=1.0, zorder=5))
    ax.add_patch(Wedge((0, -0.55), 0.5, -80, 80, width=0.16, fc="#D9A441", ec=INK, lw=1.0, zorder=5))
    ax.text(-0.5, 0.0, "P", fontsize=9, ha="center", va="center")
    ax.text(0.5, 0.0, "Q", fontsize=9, ha="center", va="center")
    for s, t in ((-1, "X"), (1, "Y")):
        ax.add_patch(Rectangle((s * 0.62 - 0.08 + (0.0 if s > 0 else -0.1), -0.75), 0.18, 0.4, fc=GREY, ec=INK, lw=0.9, zorder=6))
        ax.text(s * 0.95, -1.0, t, fontsize=9, ha="center")
    wire(ax, [(-0.68, -0.75), (-0.68, -1.5), (-1.6, -1.5)])
    wire(ax, [(0.7, -0.75), (0.7, -1.5), (1.6, -1.5)])
    comp(ax, (-1.6, -1.5), (-1.6, -2.6), "wire")
    wire(ax, [(-1.6, -2.4), (-1.6, -2.6)])
    comp(ax, (-1.6, -2.6), (1.6, -2.6), "battery", text="battery", flip=True)
    wire(ax, [(1.6, -1.5), (1.6, -2.6)])
    ax.annotate("", xy=(-1.25, 2.6), xytext=(-1.25, 2.0), arrowprops=dict(arrowstyle="-|>", color="#C0392B", lw=1.6), zorder=6)
    ax.annotate("", xy=(1.25, 1.4), xytext=(1.25, 2.0), arrowprops=dict(arrowstyle="-|>", color="#C0392B", lw=1.6), zorder=6)
    ax.text(-1.15, 2.75, "force on AB", color="#C0392B", fontsize=8)
    ax.text(1.75, 1.5, "force\non CD", color="#C0392B", fontsize=8, ha="left")
    ax.annotate("", xy=(2.3, 0.2), xytext=(-2.3, 0.2), arrowprops=dict(arrowstyle="-|>", color=FIELD, lw=1.0))
    ax.text(-2.3, 0.3, "magnetic field", fontsize=8, color=FIELD)
    label(ax, (0.4, -0.3), "split-ring\ncommutator", (2.1, -0.4))
    label(ax, (-0.85, -0.6), "brushes", (-2.5, -0.6), ha="right")
    label(ax, (0.0, 1.0), "axle", (0.0, 0.45))
    finish(ax, (-3.6, 3.8), (-3.2, 3.0))
    save(fig, "sci_ch12_fig07_motor.png")


if __name__ == "__main__":
    fig_bar_magnet()
    fig_straight_wire()
    fig_loop()
    fig_solenoid()
    fig_fleming()
    fig_domestic()
    fig_motor()
