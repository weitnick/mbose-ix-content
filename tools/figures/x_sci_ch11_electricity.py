"""Figures for Class X Science, Chapter 11: Electricity.
Run: python x_sci_ch11_electricity.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
Circuit helpers (wire, comp, ...) draw the standard NCERT symbols and are reused by Chapter 12.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_sci_ch05_life_processes import ACC, GREY, HI, INK, SOFT, finish, save
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Rectangle

LW = 1.4
L = 0.8   # length of a component along its wire


def wire(ax, pts, lw=LW, color=INK):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="round", zorder=2)


def dot(ax, p, r=0.045):
    ax.add_patch(Circle(p, r, fc=INK, ec=INK, zorder=5))


def _T(c, ang):
    ca, sa = math.cos(ang), math.sin(ang)
    return lambda x, y: (c[0] + x * ca - y * sa, c[1] + x * sa + y * ca)


def _line(ax, T, pts, lw=LW, color=INK, ls="-", z=4):
    g = [T(x, y) for x, y in pts]
    xs, ys = zip(*g)
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_capstyle="butt", zorder=z)


def draw_symbol(ax, kind, c, ang=0.0, text=None, closed=True, flip=False):
    """Draw a component centred at c, oriented along angle ang (radians). Occupies -L/2..L/2 along its axis."""
    T = _T(c, ang)
    h = L / 2
    if kind == "cell":
        _line(ax, T, [(-h, 0), (-0.05, 0)])
        _line(ax, T, [(0.05, 0), (h, 0)])
        _line(ax, T, [(-0.05, -0.26), (-0.05, 0.26)], lw=1.3)
        _line(ax, T, [(0.05, -0.13), (0.05, 0.13)], lw=3.2)
    elif kind == "battery":
        _line(ax, T, [(-h, 0), (-0.25, 0)])
        _line(ax, T, [(0.25, 0), (h, 0)])
        for x0 in (-0.25, 0.13):
            _line(ax, T, [(x0, -0.26), (x0, 0.26)], lw=1.3)
            _line(ax, T, [(x0 + 0.1, -0.13), (x0 + 0.1, 0.13)], lw=3.2)
        _line(ax, T, [(-0.15, 0), (0.13, 0)], lw=1.0, ls=(0, (2, 2)))
    elif kind == "resistor":
        n = 6
        xs = np.linspace(-0.32, 0.32, 2 * n + 1)
        pts = [(-h, 0), (-0.32, 0)] + [(x, (0.13 if i % 2 else -0.13) if 0 < i < 2 * n else 0) for i, x in enumerate(xs)] + [(h, 0)]
        _line(ax, T, pts, lw=1.3)
    elif kind == "rheostat":
        draw_symbol(ax, "resistor", c, ang)
        a, b = T(-0.3, -0.28), T(0.3, 0.3)
        ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1, mutation_scale=10), zorder=5)
    elif kind == "bulb":
        _line(ax, T, [(-h, 0), (-0.2, 0)])
        _line(ax, T, [(0.2, 0), (h, 0)])
        p = T(0, 0)
        ax.add_patch(Circle(p, 0.2, fc="white", ec=INK, lw=1.3, zorder=4))
        r = 0.2 / math.sqrt(2)
        _line(ax, T, [(-r, -r), (r, r)], lw=1.1, z=5)
        _line(ax, T, [(-r, r), (r, -r)], lw=1.1, z=5)
    elif kind in ("ammeter", "voltmeter", "galvanometer"):
        _line(ax, T, [(-h, 0), (-0.22, 0)])
        _line(ax, T, [(0.22, 0), (h, 0)])
        p = T(0, 0)
        ax.add_patch(Circle(p, 0.22, fc="white", ec=INK, lw=1.3, zorder=4))
        ax.text(p[0], p[1], {"ammeter": "A", "voltmeter": "V", "galvanometer": "G"}[kind], ha="center", va="center",
                fontsize=10, fontweight="bold", zorder=6)
        if kind != "galvanometer":
            sp, sm = (T(-0.3, 0.17), T(0.3, 0.17)) if not flip else (T(0.3, 0.17), T(-0.3, 0.17))
            ax.text(*sp, "+", ha="center", va="center", fontsize=8, zorder=6)
            ax.text(*sm, "−", ha="center", va="center", fontsize=8, zorder=6)
    elif kind == "key":
        _line(ax, T, [(-h, 0), (-0.12, 0)])
        _line(ax, T, [(0.12, 0), (h, 0)])
        for x0 in (-0.12, 0.12):
            ax.add_patch(Circle(T(x0, 0), 0.035, fc="white", ec=INK, lw=1.0, zorder=5))
        p = T(0, 0)
        ax.add_patch(Arc(p, 0.5, 0.42, angle=math.degrees(ang), theta1=120, theta2=240, color=INK, lw=1.1, zorder=5))
        ax.add_patch(Arc(p, 0.5, 0.42, angle=math.degrees(ang), theta1=-60, theta2=60, color=INK, lw=1.1, zorder=5))
        if closed:
            ax.add_patch(Circle(p, 0.05, fc=INK, ec=INK, zorder=5))
    elif kind == "switch_open":
        _line(ax, T, [(-h, 0), (-0.15, 0)])
        _line(ax, T, [(0.15, 0), (h, 0)])
        _line(ax, T, [(-0.15, 0), (0.15, 0.17)], lw=1.3)
        ax.add_patch(Circle(T(-0.15, 0), 0.035, fc=INK, ec=INK, zorder=5))
        ax.add_patch(Circle(T(0.15, 0), 0.035, fc="white", ec=INK, zorder=5))
    elif kind == "switch_closed":
        _line(ax, T, [(-h, 0), (h, 0)])
        ax.add_patch(Circle(T(-0.15, 0), 0.035, fc=INK, ec=INK, zorder=5))
        ax.add_patch(Circle(T(0.15, 0), 0.035, fc=INK, ec=INK, zorder=5))
    elif kind == "wire":
        _line(ax, T, [(-h, 0), (h, 0)])
    if text:
        off = 0.42
        if abs(math.sin(ang)) < 0.5:
            p = T(0, off if not flip else -off)
            ax.text(*p, text, ha="center", va="center", fontsize=8.5, zorder=6)
        else:
            p = (c[0] + (0.42 if not flip else -0.42), c[1])
            ax.text(*p, text, ha="left" if not flip else "right", va="center", fontsize=8.5, zorder=6)


def comp(ax, p0, p1, kind, at=0.5, **kw):
    """Draw wire p0 -> p1 (horizontal or vertical) with a component centred at fraction `at`."""
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    c = (p0[0] + at * (p1[0] - p0[0]), p0[1] + at * (p1[1] - p0[1]))
    a = (c[0] - L / 2 * math.cos(ang), c[1] - L / 2 * math.sin(ang))
    b = (c[0] + L / 2 * math.cos(ang), c[1] + L / 2 * math.sin(ang))
    wire(ax, [p0, a])
    wire(ax, [b, p1])
    draw_symbol(ax, kind, c, ang, **kw)
    return c


def current_arrow(ax, p, d, color=HI):
    ax.annotate("", xy=(p[0] + 0.25 * d[0], p[1] + 0.25 * d[1]), xytext=p,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.3, mutation_scale=12), zorder=6)


# Fig 11.1: symbols of commonly used components (Table 11.1)
def fig_symbols():
    items = [("cell", "an electric cell", {}), ("battery", "a battery (combination of cells)", {}),
             ("key", "plug key or switch (open)", {"closed": False}), ("key", "plug key or switch (closed)", {"closed": True}),
             ("joint", "a wire joint", {}), ("cross", "wires crossing without joining", {}),
             ("bulb", "electric bulb", {}), ("resistor", "a resistor of resistance R", {}),
             ("rheostat", "variable resistance (rheostat)", {}), ("ammeter", "ammeter", {}), ("voltmeter", "voltmeter", {})]
    fig, ax = plt.subplots(figsize=(7.4, 6.4))
    for i, (kind, name, kw) in enumerate(items):
        col, row = i % 2, i // 2
        x0, y0 = col * 4.2, -row * 1.15
        c = (x0 + 0.8, y0)
        if kind == "joint":
            wire(ax, [(c[0] - 0.45, c[1]), (c[0] + 0.45, c[1])])
            wire(ax, [c, (c[0], c[1] - 0.35)])
            dot(ax, c, 0.06)
        elif kind == "cross":
            wire(ax, [(c[0] - 0.45, c[1]), (c[0] + 0.45, c[1])])
            wire(ax, [(c[0], c[1] + 0.35), (c[0], c[1] - 0.35)])
        else:
            draw_symbol(ax, kind, c, 0.0, **kw)
        ax.text(x0 + 1.45, y0, f"{i + 1}. {name}", fontsize=8.5, va="center")
    finish(ax, (-0.1, 8.4), (-6.2, 0.6))
    save(fig, "sci_ch11_fig01_symbols.png")


# Fig 11.2: a simple electric circuit
def fig_simple_circuit():
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    A, B, C, D = (0, 0), (4, 0), (4, 2.6), (0, 2.6)
    comp(ax, D, (2, 2.6), "cell", text="cell", at=0.55)
    comp(ax, (2, 2.6), C, "key", text="plug key", at=0.45)
    comp(ax, C, B, "bulb", text="bulb")
    comp(ax, B, A, "ammeter", text="ammeter", flip=True)
    wire(ax, [A, D])
    current_arrow(ax, (3.95, 1.9), (0, -1))
    ax.text(3.65, 2.0, "I", color=HI, fontsize=9, ha="right")
    finish(ax, (-0.6, 5.2), (-0.8, 3.3))
    save(fig, "sci_ch11_fig02_simple_circuit.png")


# Fig 11.3: circuit for studying Ohm's law
def fig_ohm_circuit():
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    comp(ax, (0, 3), (2.6, 3), "battery", text="battery", at=0.45)
    comp(ax, (2.6, 3), (4.6, 3), "key", text="key", at=0.45)
    comp(ax, (4.6, 3), (4.6, 1.2), "ammeter", text="A", flip=False)
    X, Y = (3.4, 1.2), (1.2, 1.2)
    wire(ax, [(4.6, 1.2), X])
    comp(ax, X, Y, "resistor", text="nichrome wire")
    wire(ax, [Y, (0, 1.2), (0, 3)])
    for p, t in ((X, "X"), (Y, "Y")):
        dot(ax, p)
        ax.text(p[0], p[1] + 0.18, t, fontsize=8.5, ha="center")
    wire(ax, [X, (X[0], 0.0)])
    wire(ax, [Y, (Y[0], 0.0)])
    comp(ax, (X[0], 0.0), (Y[0], 0.0), "voltmeter", text="voltmeter", flip=True)
    finish(ax, (-0.6, 5.6), (-0.7, 3.6))
    save(fig, "sci_ch11_fig03_ohm_circuit.png")


# Fig 11.4: V-I graph (data of NCERT Exercise 7)
def fig_vi_graph():
    I = np.array([0.5, 1.0, 2.0, 3.0, 4.0])
    V = np.array([1.6, 3.4, 6.7, 10.2, 13.2])
    k = (I @ V) / (I @ I)
    fig, ax = plt.subplots(figsize=(4.8, 3.8))
    ax.plot([0, 4.4], [0, 4.4 * k], color=ACC, lw=1.5, zorder=2)
    ax.plot(I, V, "o", color=HI, ms=6, mec=INK, zorder=3)
    ax.set_xlim(0, 4.6)
    ax.set_ylim(0, 15.5)
    ax.set_xlabel("current I (A)", fontsize=9)
    ax.set_ylabel("potential difference V (V)", fontsize=9)
    ax.grid(True, color="#DDE3EA", lw=0.6)
    ax.plot([1.0, 4.0, 4.0], [1.0 * k, 1.0 * k, 4.0 * k], color=GREY, lw=0.9, ls=(0, (3, 2)))
    ax.text(2.5, 1.0 * k - 0.9, "ΔI = 3.0 A", fontsize=8, ha="center", color=INK)
    ax.text(4.08, 2.5 * k, f"ΔV ≈ {3 * k:.1f} V", fontsize=8, va="center", color=INK)
    ax.text(0.25, 13.6, f"slope = ΔV/ΔI = R ≈ {k:.1f} Ω", fontsize=9, color=ACC)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    save(fig, "sci_ch11_fig04_vi_graph.png")


# Fig 11.5: resistors in series
def fig_series():
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    comp(ax, (0, 3), (3.0, 3), "battery", text="battery", at=0.5)
    comp(ax, (3.0, 3), (5.6, 3), "key", text="key", at=0.5)
    comp(ax, (5.6, 3), (5.6, 1.2), "ammeter", text="A")
    xs = [5.6, 4.6, 3.6, 2.6, 1.6, 0.6]
    wire(ax, [(5.6, 1.2), (5.05, 1.2)])
    pts = [(5.05, 1.2), (3.85, 1.2), (2.65, 1.2), (1.45, 1.2)]
    labels = ["R₁", "R₂", "R₃"]
    for i in range(3):
        comp(ax, pts[i], pts[i + 1], "resistor", text=labels[i])
    wire(ax, [(1.45, 1.2), (0, 1.2), (0, 3)])
    for p, t in ((pts[0], "X"), (pts[1], "P"), (pts[2], "Q"), (pts[3], "Y")):
        dot(ax, p)
        ax.text(p[0], p[1] + 0.16, t, fontsize=8.5, ha="center", va="bottom")
    wire(ax, [pts[0], (pts[0][0], 0.0)])
    wire(ax, [pts[3], (pts[3][0], 0.0)])
    comp(ax, (pts[0][0], 0.0), (pts[3][0], 0.0), "voltmeter", text="V (across X and Y)", flip=True)
    finish(ax, (-0.6, 6.6), (-0.8, 3.6))
    save(fig, "sci_ch11_fig05_series.png")


# Fig 11.6: resistors in parallel
def fig_parallel():
    fig, ax = plt.subplots(figsize=(6.2, 5.0))
    comp(ax, (0, 4.2), (2.8, 4.2), "battery", text="battery", at=0.5)
    comp(ax, (2.8, 4.2), (5.4, 4.2), "key", text="key", at=0.5)
    wire(ax, [(5.4, 4.2), (5.4, 2.4)])
    comp(ax, (0, 4.2), (0, 2.4), "ammeter", text="A", flip=True)
    X, Y = (4.4, 2.4), (1.0, 2.4)
    wire(ax, [(5.4, 2.4), X])
    wire(ax, [(0, 2.4), Y])
    ys = [3.2, 2.4, 1.6]
    for y, t in zip(ys, ("R₁", "R₂", "R₃")):
        comp(ax, (X[0], y), (Y[0], y), "resistor", text=t)
    wire(ax, [(X[0], ys[0]), (X[0], ys[-1])])
    wire(ax, [(Y[0], ys[0]), (Y[0], ys[-1])])
    for p, t in ((X, "X"), (Y, "Y")):
        dot(ax, p)
        ax.text(p[0] + (0.15 if p == X else -0.15), p[1] + 0.12, t, fontsize=8.5, ha="left" if p == X else "right")
    wire(ax, [(X[0], ys[-1]), (X[0], 0.3)])
    wire(ax, [(Y[0], ys[-1]), (Y[0], 0.3)])
    comp(ax, (X[0], 0.3), (Y[0], 0.3), "voltmeter", text="V", flip=True)
    finish(ax, (-0.8, 6.0), (-0.4, 4.8))
    save(fig, "sci_ch11_fig06_parallel.png")


# Fig 11.7: a combination of series and parallel resistors (Example 11.9)
def fig_combination():
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    comp(ax, (0, 3.4), (6.6, 3.4), "battery", text="12 V", at=0.5)
    wire(ax, [(6.6, 3.4), (6.6, 1.6), (6.0, 1.6)])
    wire(ax, [(0, 3.4), (0, 1.6), (0.6, 1.6)])
    # group 1: R1, R2 in parallel (left); group 2: R3, R4, R5 in parallel (right)
    g1 = [(2.1, "R₁ = 10 Ω"), (1.1, "R₂ = 40 Ω")]
    g2 = [(2.4, "R₃ = 30 Ω"), (1.6, "R₄ = 20 Ω"), (0.8, "R₅ = 60 Ω")]
    for y, t in g1:
        comp(ax, (0.6, y), (2.8, y), "resistor", text=t)
    wire(ax, [(0.6, g1[0][0]), (0.6, g1[-1][0])])
    wire(ax, [(2.8, g1[0][0]), (2.8, g1[-1][0])])
    wire(ax, [(2.8, 1.6), (3.8, 1.6)])
    for y, t in g2:
        comp(ax, (3.8, y), (6.0, y), "resistor", text=t)
    wire(ax, [(3.8, g2[0][0]), (3.8, g2[-1][0])])
    wire(ax, [(6.0, g2[0][0]), (6.0, g2[-1][0])])
    for p in ((0.6, 1.6), (2.8, 1.6), (3.8, 1.6), (6.0, 1.6)):
        dot(ax, p)
    finish(ax, (-0.5, 7.2), (0.2, 4.0))
    save(fig, "sci_ch11_fig07_combination.png")


if __name__ == "__main__":
    fig_symbols()
    fig_simple_circuit()
    fig_ohm_circuit()
    fig_vi_graph()
    fig_series()
    fig_parallel()
    fig_combination()
