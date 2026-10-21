"""Figures for Class XII Physics Chapter 3, Current Electricity.
Run: python xii_phy_ch03_current.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Physics", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, POS, NEG, ACC, GREY, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#E9F0F7"
GREEN = "#2E7D32"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def arrow(ax, p0, p1, color=INK, lw=1.6, ms=12, style="-|>"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, color=color, lw=lw, shrinkA=0, shrinkB=0))


def blank(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")


def wire(ax, pts, color=INK, lw=1.4):
    xs, ys = zip(*[tuple(p) for p in pts])
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="round")


def _frame(p0, p1):
    p0, p1 = np.array(p0, float), np.array(p1, float)
    d = p1 - p0
    length = float(np.hypot(*d))
    u = d / length
    return p0, p1, length, u, np.array([-u[1], u[0]])


def res(ax, p0, p1, label=None, side=1, L=0.8, amp=0.12, n=6, fs=9, color=INK, rheo=False):
    """Zigzag resistor in the middle of segment p0-p1, with wires to both ends."""
    p0, p1, length, u, nrm = _frame(p0, p1)
    L = min(L, 0.8 * length)
    a = p0 + u * (length - L) / 2
    b = a + u * L
    wire(ax, [p0, a])
    wire(ax, [b, p1])
    pts = []
    for i, t in enumerate(np.linspace(0, 1, 2 * n + 1)):
        off = 0 if i in (0, 2 * n) else (1 if i % 2 else -1)
        pts.append(a + u * L * t + nrm * amp * off)
    wire(ax, pts, color=color)
    if rheo:
        m = (a + b) / 2
        arrow(ax, m - u * L * 0.45 - nrm * 0.3, m + u * L * 0.45 + nrm * 0.3, INK, lw=1.1, ms=9)
    if label:
        m = (a + b) / 2 + nrm * side * (amp + 0.2)
        ax.text(*m, label, ha="center", va="center", fontsize=fs)


def cell(ax, p0, p1, label=None, plus_first=True, side=1, gap=0.1, hl=0.4, hs=0.22, fs=9, signs=False):
    """Cell centred on segment p0-p1. The long plate (+) is on the p0 side when plus_first."""
    p0, p1, length, u, nrm = _frame(p0, p1)
    m = (p0 + p1) / 2
    a, b = m - u * gap / 2, m + u * gap / 2
    wire(ax, [p0, a])
    wire(ax, [b, p1])
    lp, sp = (a, b) if plus_first else (b, a)
    wire(ax, [lp - nrm * hl / 2, lp + nrm * hl / 2], lw=1.6)
    wire(ax, [sp - nrm * hs / 2, sp + nrm * hs / 2], lw=3.4)
    if label:
        t = m + nrm * side * (hl / 2 + 0.2)
        ax.text(*t, label, ha="center", va="center", fontsize=fs)
    if signs:
        for q, s in ((lp, "+"), (sp, "−")):
            t = q + (q - m) / max(np.hypot(*(q - m)), 1e-9) * 0.16 - nrm * side * 0.28
            ax.text(*t, s, ha="center", va="center", fontsize=9, color=POS if s == "+" else NEG)


def lamp(ax, p0, p1, label=None, r=0.2, side=1, fs=9):
    p0, p1, length, u, nrm = _frame(p0, p1)
    m = (p0 + p1) / 2
    wire(ax, [p0, m - u * r])
    wire(ax, [m + u * r, p1])
    ax.add_patch(Circle(m, r, fill=False, color=INK, lw=1.4))
    k = r * 0.7
    wire(ax, [m + np.array([-k, -k]), m + np.array([k, k])], lw=1.1)
    wire(ax, [m + np.array([-k, k]), m + np.array([k, -k])], lw=1.1)
    if label:
        ax.text(*(m + nrm * side * (r + 0.22)), label, ha="center", va="center", fontsize=fs)


def node(ax, xy, label=None, dx=0.0, dy=0.22, fs=10):
    ax.plot([xy[0]], [xy[1]], "o", color=INK, ms=4.5, zorder=5)
    if label:
        ax.text(xy[0] + dx, xy[1] + dy, label, ha="center", va="center", fontsize=fs, style="italic")


def carrow(ax, xy, direction, label=None, color=POS, off=(0, 0.22), fs=9):
    """Small current arrowhead at xy pointing along direction."""
    u = np.array(direction, float)
    u = u / np.hypot(*u)
    xy = np.array(xy, float)
    arrow(ax, xy - u * 0.13, xy + u * 0.13, color, lw=1.4, ms=11)
    if label:
        ax.text(xy[0] + off[0], xy[1] + off[1], label, ha="center", va="center", fontsize=fs, color=color)


# ---- Fig 3.1: drift of electrons -------------------------------------------------------------
def fig_drift():
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 3.3), gridspec_kw={"width_ratios": [1, 1, 1.25]})
    rng = np.random.default_rng(7)
    steps = rng.normal(size=(9, 2))
    steps = steps / np.hypot(steps[:, 0], steps[:, 1])[:, None] * rng.uniform(0.45, 0.8, size=(9, 1))
    steps = steps - steps.mean(axis=0)
    for k, ax in enumerate(axes[:2]):
        blank(ax, (-2.3, 2.3), (-1.7, 1.9))
        for x in np.arange(-2, 2.01, 0.8):
            for y in np.arange(-1.4, 1.41, 0.7):
                ax.add_patch(Circle((x, y), 0.07, color=GREY, alpha=0.6))
        pos = np.array([0.0 if k == 0 else 1.0, -0.2])
        path = [pos.copy()]
        for i, s in enumerate(steps):
            seg = s + (np.array([-0.24, 0.0]) if k == 1 else 0)
            # in a field the path between collisions is a curve; draw it as a gentle arc
            pts = [pos + seg * t + (np.array([-0.06, 0]) * t * (1 - t) * 4 if k == 1 else 0) for t in np.linspace(0, 1, 8)]
            wire(ax, pts, color=NEG, lw=1.1)
            pos = pos + seg
            path.append(pos.copy())
        ax.plot(*path[0], "o", color=GREEN, ms=6, zorder=6)
        ax.plot(*path[-1], "s", color=POS, ms=6, zorder=6)
        if k == 0:
            ax.set_title("(a) No field: random motion", fontsize=10)
            ax.text(0, -1.65, "net displacement over many collisions = 0", ha="center", fontsize=8.5, color=GREY)
        else:
            ax.set_title("(b) Field E: random motion + drift", fontsize=10)
            arrow(ax, (-1.6, 1.65), (-0.2, 1.65), ACC, lw=2)
            ax.text(0.05, 1.65, r"$\vec E$", color=ACC, va="center", fontsize=11)
            arrow(ax, path[0], path[-1], GREEN, lw=1.8)
            ax.text(-0.2, -1.65, r"net drift opposite to $\vec E$ (electrons)", ha="center", fontsize=8.5, color=GREEN)
    ax = axes[2]
    blank(ax, (-0.4, 5.2), (-1.7, 1.9))
    ax.add_patch(Rectangle((0.8, -0.8), 3.0, 1.6, color=SOFT, ec=NEG, lw=1.4))
    ax.add_patch(Ellipse((0.8, 0), 0.5, 1.6, color="white", ec=NEG, lw=1.4, zorder=3))
    ax.add_patch(Ellipse((3.8, 0), 0.5, 1.6, color=SOFT, ec=NEG, lw=1.4, ls="--", zorder=3))
    wire(ax, [(-0.3, 0.55), (0.8, 0.55)], color=GREY, lw=1)
    wire(ax, [(-0.3, -0.55), (0.8, -0.55)], color=GREY, lw=1)
    for x in (1.3, 1.9, 2.5, 3.1):
        for y in (-0.4, 0.15, 0.5):
            ax.plot([x + 0.12 * (y > 0)], [y], "o", color=NEG, ms=4)
    ax.text(0.8, -1.05, "area A", ha="center", fontsize=9)
    ax.annotate("", (0.8, -1.35), (3.8, -1.35), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1))
    ax.text(2.3, -1.6, r"length $v_d\,\Delta t$", ha="center", fontsize=9)
    arrow(ax, (3.2, 1.2), (1.4, 1.2), NEG, lw=1.6)
    ax.text(2.3, 1.45, r"electrons drift at $v_d$", ha="center", fontsize=9, color=NEG)
    arrow(ax, (4.2, 0.0), (5.1, 0.0), POS, lw=2)
    ax.text(4.65, 0.25, "I", ha="center", color=POS, style="italic")
    ax.set_title(r"(c) Charge crossing A in $\Delta t$: $neAv_d\Delta t$, so $I = neAv_d$", fontsize=10)
    save(fig, "phy_ch03_fig01_drift.png")


# ---- Fig 3.2: V-I graphs ---------------------------------------------------------------------
def _axes(ax, xl, yl):
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(xl, fontsize=9)
    ax.set_ylabel(yl, fontsize=9, rotation=0, labelpad=8)


def fig_vi():
    fig, axes = plt.subplots(1, 4, figsize=(12, 2.8))
    ax = axes[0]
    v = np.linspace(0, 1, 50)
    ax.plot(v, 0.8 * v, color=NEG, lw=2)
    ax.text(0.55, 0.25, "slope = 1/R\n(R constant)", fontsize=8.5)
    _axes(ax, "V", "I")
    ax.set_title("(a) Ohmic conductor", fontsize=10)
    ax = axes[1]
    i = np.linspace(0, 1, 50)
    ax.plot(i, i, "--", color=GREY, lw=1.4, label="Ohm's law")
    ax.plot(i, i + 0.6 * i**3, color=POS, lw=2, label="real wire")
    ax.legend(fontsize=7.5, frameon=False, loc="upper left")
    _axes(ax, "I", "V")
    ax.set_title("(b) V not proportional to I", fontsize=10)
    ax = axes[2]
    vf = np.linspace(0, 0.75, 60)
    ax.plot(vf, 0.02 * (np.exp(vf / 0.12) - 1) / 10, color=NEG, lw=2)
    vr = np.linspace(-0.8, 0, 30)
    ax.plot(vr, -0.04 + 0 * vr, color=NEG, lw=2)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.axvline(0, color=GREY, lw=0.8)
    ax.set_ylim(-0.25, 1.0)
    ax.text(-0.75, 0.25, "reverse:\ntiny current", fontsize=8)
    ax.text(0.05, 0.75, "forward", fontsize=8)
    _axes(ax, "V", "I")
    ax.set_title("(c) Diode: depends on sign of V", fontsize=10)
    ax = axes[3]
    vv = np.linspace(0, 1, 200)
    ax.plot(vv, 1.2 * vv * np.exp(-((vv - 0.25) / 0.25) ** 2) + 0.9 * vv**3, color=GREEN, lw=2)
    ax.axhline(0.33, color=GREY, ls=":", lw=1)
    ax.text(0.62, 0.38, "same I at\nthree values of V", fontsize=8)
    _axes(ax, "V", "I")
    ax.set_title("(d) GaAs: V not unique", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch03_fig02_vi.png")


# ---- Fig 3.3: resistivity and temperature ----------------------------------------------------
def fig_resistivity():
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 2.9))
    ax = axes[0]
    T = np.linspace(1, 500, 300)
    rho = 0.02 + 1.7 * (T / 293) * (1 - np.exp(-((T / 70) ** 2)))
    ax.plot(T, rho, color=POS, lw=2)
    ax.set_xlabel("T (K)", fontsize=9)
    ax.set_ylabel(r"$\rho$ ($10^{-8}\,\Omega$ m)", fontsize=9)
    ax.set_title("(a) Copper: rises with T", fontsize=10)
    ax.text(250, 0.6, "nearly linear here:\n" + r"$\rho_T=\rho_0[1+\alpha(T-T_0)]$", fontsize=8)
    ax = axes[1]
    T = np.linspace(0, 1000, 100)
    ax.plot(T, 100 + 0.01 * T, color=ACC, lw=2)
    ax.set_ylim(0, 130)
    ax.set_xlabel("T (K)", fontsize=9)
    ax.set_ylabel(r"$\rho$ ($10^{-8}\,\Omega$ m)", fontsize=9)
    ax.set_title("(b) Nichrome: almost constant", fontsize=10)
    ax.text(80, 40, "large ρ, very small α\n(heating elements,\nstandard resistors)", fontsize=8)
    ax = axes[2]
    T = np.linspace(250, 600, 200)
    ax.plot(T, np.exp(3000 / T) / np.exp(3000 / 250), color=NEG, lw=2)
    ax.set_xlabel("T (K)", fontsize=9)
    ax.set_ylabel(r"$\rho$ (relative)", fontsize=9)
    ax.set_title("(c) Semiconductor: falls with T", fontsize=10)
    ax.text(380, 0.55, "n rises faster\nthan τ falls", fontsize=8)
    for a in axes:
        a.spines[["top", "right"]].set_visible(False)
        a.tick_params(labelsize=8)
    fig.tight_layout()
    save(fig, "phy_ch03_fig03_resistivity.png")


# ---- Fig 3.4: emf and internal resistance ----------------------------------------------------
def fig_cell():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.2), gridspec_kw={"width_ratios": [1.1, 1]})
    ax = axes[0]
    blank(ax, (-0.6, 4.6), (-0.9, 2.8))
    ax.add_patch(Rectangle((0.55, 1.6), 2.9, 0.9, fill=False, ec=GREY, ls="--", lw=1))
    ax.text(2.0, 2.65, "the cell", ha="center", fontsize=9, color=GREY)
    wire(ax, [(0, 2.0), (0.55, 2.0)])
    cell(ax, (0.55, 2.0), (1.6, 2.0), r"$\varepsilon$", plus_first=True, signs=False)
    res(ax, (1.6, 2.0), (3.45, 2.0), "r", L=0.8)
    wire(ax, [(3.45, 2.0), (4, 2.0)])
    node(ax, (0, 2.0), "P (+)", dx=-0.05, dy=0.3)
    node(ax, (4, 2.0), "N (−)", dx=0.05, dy=0.3)
    wire(ax, [(0, 2.0), (0, 0)])
    wire(ax, [(4, 2.0), (4, 0)])
    res(ax, (4, 0), (0, 0), "R", side=-1, L=1.0)
    carrow(ax, (0, 1.0), (0, -1), "I", off=(-0.25, 0))
    ax.text(2.0, -0.65, r"$V=\varepsilon-Ir=IR\;\Rightarrow\;I=\dfrac{\varepsilon}{R+r}$", ha="center", fontsize=10.5)
    ax.set_title("(a) A cell of emf ε and internal resistance r", fontsize=10)
    ax = axes[1]
    i = np.linspace(0, 1, 10)
    ax.plot(i, 1 - i, color=NEG, lw=2)
    ax.set_xlim(0, 1.15)
    ax.set_ylim(0, 1.2)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["0", r"$\varepsilon/r$"])
    ax.set_yticks([1])
    ax.set_yticklabels([r"$\varepsilon$"])
    ax.set_xlabel("current I", fontsize=9)
    ax.set_ylabel("terminal voltage V", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.03, 1.05, "open circuit: V = ε", fontsize=8.5)
    ax.text(0.5, 0.62, "slope = −r", fontsize=9)
    ax.text(0.8, 0.42, "short circuit:\n" + r"$I_{max}=\varepsilon/r$", fontsize=8.5)
    ax.set_title("(b) V falls as the current rises", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch03_fig04_cell.png")


# ---- Fig 3.5: cells in series and in parallel ------------------------------------------------
def fig_cells():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.0))
    ax = axes[0]
    blank(ax, (-0.4, 6.4), (-1.2, 1.4))
    cell(ax, (0, 0.4), (1.2, 0.4), r"$\varepsilon_1$", True)
    res(ax, (1.2, 0.4), (2.6, 0.4), r"$r_1$", L=0.7)
    cell(ax, (3.2, 0.4), (4.4, 0.4), r"$\varepsilon_2$", True)
    res(ax, (4.4, 0.4), (6.0, 0.4), r"$r_2$", L=0.7)
    wire(ax, [(2.6, 0.4), (3.2, 0.4)])
    for x, l in ((0, "A"), (2.9, "B"), (6.0, "C")):
        node(ax, (x, 0.4), l, dy=-0.3)
    ax.text(3.0, -0.75, r"$\varepsilon_{eq}=\varepsilon_1+\varepsilon_2,\quad r_{eq}=r_1+r_2$", ha="center", fontsize=10.5)
    ax.set_title("(a) In series (+ of one joined to − of the next)", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.8, 6.0), (-1.4, 2.6))
    for y, k in ((1.9, 1), (0.6, 2)):
        wire(ax, [(1.0, y), (1.3, y)])
        cell(ax, (1.3, y), (2.5, y), rf"$\varepsilon_{k}$", True)
        res(ax, (2.5, y), (4.0, y), rf"$r_{k}$", L=0.7)
        wire(ax, [(4.0, y), (4.3, y)])
        carrow(ax, (1.15, y), (-1, 0), rf"$I_{k}$", off=(0, 0.25))
    wire(ax, [(1.0, 1.9), (1.0, 0.6)])
    wire(ax, [(4.3, 1.9), (4.3, 0.6)])
    node(ax, (1.0, 1.25), r"$B_1$", dx=0.35, dy=0)
    node(ax, (4.3, 1.25), r"$B_2$", dx=-0.35, dy=0)
    wire(ax, [(1.0, 1.25), (-0.4, 1.25)])
    wire(ax, [(4.3, 1.25), (5.6, 1.25)])
    carrow(ax, (0.2, 1.25), (-1, 0), "I", off=(0, -0.28))
    ax.text(2.6, -0.65, r"$\dfrac{1}{r_{eq}}=\dfrac{1}{r_1}+\dfrac{1}{r_2},\quad \dfrac{\varepsilon_{eq}}{r_{eq}}=\dfrac{\varepsilon_1}{r_1}+\dfrac{\varepsilon_2}{r_2}$", ha="center", fontsize=10.5)
    ax.set_title("(b) In parallel (+ to +, − to −)", fontsize=10)
    save(fig, "phy_ch03_fig05_cells.png")


# ---- Fig 3.6: Kirchhoff's rules --------------------------------------------------------------
def fig_kirchhoff():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.2), gridspec_kw={"width_ratios": [0.8, 1.2]})
    ax = axes[0]
    blank(ax, (-2.0, 2.0), (-1.6, 1.8))
    o = np.array([0.0, 0.0])
    for ang, lab, inn in ((150, r"$I_1$", True), (210, r"$I_2$", True), (0, r"$I_3$", False)):
        d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        wire(ax, [o, o + 1.6 * d])
        mid = o + 0.9 * d
        carrow(ax, mid, -d if inn else d, lab, off=tuple(0.3 * np.array([-d[1], d[0]]) + np.array([0, 0.05])))
    node(ax, o, "a", dy=0.3)
    ax.text(0, -1.4, r"$I_1+I_2=I_3$  (charge conserved)", ha="center", fontsize=10)
    ax.set_title("(a) Junction rule", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.8, 5.4), (-1.6, 2.6))
    cell(ax, (0, 0), (0, 2), r"$\varepsilon$", plus_first=False, side=1)
    wire(ax, [(0, 2), (1.0, 2)])
    res(ax, (1.0, 2), (4.0, 2), r"$R_1$", L=1.0)
    wire(ax, [(4.0, 2), (4.6, 2), (4.6, 0)])
    res(ax, (4.6, 0), (0, 0), r"$R_2$", side=-1, L=1.0)
    carrow(ax, (1.9, 2), (1, 0), "I", off=(0, 0.3))
    ax.text(-0.45, 1.75, "+", color=POS, fontsize=11)
    ax.text(-0.45, 0.15, "−", color=NEG, fontsize=11)
    ax.annotate("", (3.0, 1.3), (1.6, 1.3), arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.4, connectionstyle="arc3,rad=-0.4"))
    ax.text(2.3, 0.8, "go round", ha="center", fontsize=8.5, color=GREEN)
    ax.text(2.3, -0.75, r"$+\varepsilon - IR_1 - IR_2 = 0$", ha="center", fontsize=11)
    ax.text(2.3, -1.3, "cell − to +: +ε;   resistor along I: −IR", ha="center", fontsize=8.5, color=GREY)
    ax.set_title("(b) Loop rule (energy conserved)", fontsize=10)
    save(fig, "phy_ch03_fig06_kirchhoff.png")


# ---- Fig 3.7: Wheatstone bridge --------------------------------------------------------------
def fig_wheatstone():
    fig, ax = plt.subplots(figsize=(5.4, 4.2))
    blank(ax, (-0.8, 4.8), (-2.4, 2.9))
    A, D, C, B = (0, 0.6), (2, 2.4), (4, 0.6), (2, -1.0)
    D = (2, 2.2)
    res(ax, A, D, r"$R_1$", side=1, L=0.9)
    res(ax, D, C, r"$R_3$", side=1, L=0.9)
    res(ax, A, B, r"$R_2$", side=-1, L=0.9)
    res(ax, B, C, r"$R_4$", side=-1, L=0.9)
    wire(ax, [D, (2, 1.0)])
    wire(ax, [(2, 0.2), B])
    ax.add_patch(Circle((2, 0.6), 0.28, fill=False, color=INK, lw=1.4))
    ax.text(2, 0.6, "G", ha="center", va="center", fontsize=10, fontweight="bold")
    wire(ax, [(2, 0.88), (2, 1.0)])
    wire(ax, [(2, 0.32), (2, 0.2)])
    for p, l, dx, dy in ((A, "A", -0.15, 0.3), (D, "D", 0, 0.28), (C, "C", 0.15, 0.3), (B, "B", 0.3, -0.2)):
        node(ax, p, l, dx=dx, dy=dy)
    wire(ax, [A, (-0.5, 0.6), (-0.5, -1.8), (1.6, -1.8)])
    cell(ax, (1.6, -1.8), (2.4, -1.8), r"$\varepsilon$", plus_first=True, side=-1)
    wire(ax, [(2.4, -1.8), (4.5, -1.8), (4.5, 0.6), C])
    carrow(ax, (0.7, 1.32), (1, 0.9), r"$I_1$", off=(-0.25, 0.25))
    carrow(ax, (0.7, -0.12), (1, -0.8), r"$I_2$", off=(-0.3, -0.2))
    ax.text(2, 2.75, r"balanced ($I_g=0$):  $\dfrac{R_2}{R_1}=\dfrac{R_4}{R_3}$", ha="center", fontsize=10.5, color=GREEN)
    save(fig, "phy_ch03_fig07_wheatstone.png")


# ---- Fig 3.8: NCERT Exercise 3.7 network, solved ---------------------------------------------
def fig_ex37():
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    blank(ax, (-0.9, 4.9), (-1.6, 3.9))
    A, B, C, D = (0, 1.6), (2, 3.3), (4, 1.6), (2, -0.1)
    res(ax, A, B, r"10 Ω", side=1)
    res(ax, B, C, r"5 Ω", side=1)
    res(ax, A, D, r"5 Ω", side=-1)
    res(ax, D, C, r"10 Ω", side=-1)
    res(ax, B, D, r"5 Ω", side=1, L=0.9)
    for p, l, dx, dy in ((A, "A", -0.15, 0.3), (B, "B", 0, 0.3), (C, "C", 0.15, 0.3), (D, "D", 0, -0.3)):
        node(ax, p, l, dx=dx, dy=dy)
    wire(ax, [A, (-0.6, 1.6), (-0.6, -1.2), (1.3, -1.2)])
    res(ax, (1.3, -1.2), (2.4, -1.2), "10 Ω", side=-1, L=0.7)
    cell(ax, (2.4, -1.2), (3.2, -1.2), "10 V", plus_first=True, side=-1)
    wire(ax, [(3.2, -1.2), (4.6, -1.2), (4.6, 1.6), C])
    carrow(ax, (-0.6, 0.3), (0, 1), "10/17 A", off=(0.5, 0), fs=8.5)
    carrow(ax, (0.62, 2.13), (1, 0.85), "4/17", off=(-0.45, 0.2), fs=8.5)
    carrow(ax, (3.38, 2.13), (1, -0.85), "6/17", off=(0.45, 0.2), fs=8.5)
    carrow(ax, (0.62, 1.07), (1, -0.85), "6/17", off=(-0.45, -0.2), fs=8.5)
    carrow(ax, (3.38, 1.07), (1, 0.85), "4/17", off=(0.45, -0.2), fs=8.5)
    carrow(ax, (2, 2.5), (0, 1), "2/17", off=(-0.38, 0), fs=8.5)
    ax.text(2, 3.75, "currents in ampere (D to B in the 5 Ω diagonal)", ha="center", fontsize=8.5, color=GREY)
    save(fig, "phy_ch03_fig08_ex37.png")


# ---- Fig 3.9: board bridges ------------------------------------------------------------------
def fig_board_bridges():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.8), gridspec_kw={"width_ratios": [1.15, 1]})
    ax = axes[0]
    blank(ax, (-0.5, 8.5), (-1.7, 2.6))
    A, D, B, C = (1, 1), (3, 1), (5, 1), (7, 1)
    res(ax, A, D, "6", side=-1, L=0.9)
    res(ax, D, B, "4", side=1, L=0.9)
    res(ax, B, C, "2", side=1, L=0.9)
    wire(ax, [A, (1, 2.0)])
    res(ax, (1, 2.0), (5, 2.0), "2", side=1, L=0.9)
    wire(ax, [(5, 2.0), B])
    wire(ax, [D, (3, 0.0)])
    res(ax, (3, 0.0), (7, 0.0), "6", side=-1, L=0.9)
    wire(ax, [(7, 0.0), C])
    for p, l, dx, dy in ((A, "A", -0.05, -0.3), (D, "D", 0, 0.28), (B, "B", 0, -0.3), (C, "C", 0, 0.28)):
        node(ax, p, l, dx=dx, dy=dy)
    wire(ax, [A, (0, 1), (0, -1.0), (3.6, -1.0)])
    cell(ax, (3.6, -1.0), (4.4, -1.0), "6 V", plus_first=True, side=-1)
    wire(ax, [(4.4, -1.0), (8, -1.0), (8, 1), C])
    carrow(ax, (0, 0), (0, 1), "I", off=(-0.3, 0))
    ax.text(6.2, -1.45, "(resistances in ohm)", ha="center", fontsize=8.5, color=GREY)
    ax.set_title("(a) HSSLC 2019, Q27(b)", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.7, 5.0), (-1.0, 4.0))
    A, B, C, O = (2.2, 3.5), (0, 0), (4.4, 0), (2.2, 1.3)
    res(ax, B, A, "2 Ω", side=1, L=0.8)
    res(ax, A, C, "4 Ω", side=1, L=0.8)
    res(ax, A, O, "10 Ω", side=1, L=0.8)
    res(ax, B, O, "3 Ω", side=-1, L=0.8)
    res(ax, O, C, "X", side=1, L=0.8)
    cell(ax, (0, 0), (1.6, 0), "6 V", plus_first=True, side=-1)
    res(ax, (1.6, 0), (4.4, 0), "2.4 Ω", side=-1, L=0.8)
    for p, l, dx, dy in ((A, "A", 0, 0.28), (B, "B", -0.28, 0), (C, "C", 0.28, 0), (O, "O", 0.0, -0.32)):
        node(ax, p, l, dx=dx, dy=dy)
    ax.set_title("(b) HSSLC 2020 (Old Course), Q26 (second choice)", fontsize=10)
    save(fig, "phy_ch03_fig09_board_bridges.png")


# ---- Fig 3.10: board two-node networks ------------------------------------------------------
def fig_board_networks():
    fig, axes = plt.subplots(1, 3, figsize=(12.6, 3.6))
    ax = axes[0]
    blank(ax, (-0.7, 4.7), (-0.6, 2.7))
    C, B, A, D, E, F = (0, 2), (0, 1), (0, 0), (4, 2), (4, 1), (4, 0)
    cell(ax, C, D, "14 V", plus_first=True, side=1)
    carrow(ax, (1.0, 2), (-1, 0), r"$I_2$", off=(0, -0.28))
    res(ax, C, B, "4 Ω", side=1, L=0.6)
    wire(ax, [B, (0.7, 1)])
    cell(ax, (0.7, 1), (1.7, 1), "10 V", plus_first=False, side=-1)
    res(ax, (1.7, 1), E, "6 Ω", side=1, L=0.8)
    carrow(ax, (0.35, 1), (1, 0), r"$I_1$", off=(0, -0.28))
    wire(ax, [B, A])
    carrow(ax, (0, 0.5), (0, -1), r"$I_3$", off=(-0.3, 0))
    res(ax, A, F, "2 Ω", side=-1, L=0.8)
    wire(ax, [D, E, F])
    for p, l, dx, dy in ((C, "C", -0.25, 0.15), (B, "B", -0.28, 0), (A, "A", -0.25, -0.15), (D, "D", 0.25, 0.15), (E, "E", 0.28, 0), (F, "F", 0.25, -0.15)):
        node(ax, p, l, dx=dx, dy=dy)
    ax.set_title("(a) HSSLC 2020 (Old Course), Q26 (first choice)", fontsize=9.5)
    ax = axes[1]
    blank(ax, (-0.7, 4.7), (-0.6, 2.7))
    L1, L2, L3, R1, R2, R3 = (0, 2), (0, 1), (0, 0), (4, 2), (4, 1), (4, 0)
    cell(ax, L1, (2.0, 2), r"$E_1$ = 12 V", plus_first=True, side=1)
    res(ax, (2.0, 2), R1, r"$R_1$ = 2 Ω", side=1, L=0.7)
    carrow(ax, (0.5, 2), (-1, 0), r"$I_1$", off=(0, -0.28))
    res(ax, L2, R2, r"$R_2$ = 4 Ω", side=1, L=0.8)
    carrow(ax, (3.3, 1), (1, 0), r"$I_1+I_2$", off=(0, -0.3))
    cell(ax, L3, (2.0, 0), r"$E_2$ = 6 V", plus_first=True, side=-1)
    res(ax, (2.0, 0), R3, r"$R_3$ = 1 Ω", side=-1, L=0.7)
    carrow(ax, (0.5, 0), (-1, 0), r"$I_2$", off=(0, 0.28))
    wire(ax, [L1, L2, L3])
    wire(ax, [R1, R2, R3])
    carrow(ax, (0, 1.5), (0, -1), None)
    carrow(ax, (0, 0.5), (0, 1), None)
    node(ax, L2)
    node(ax, R2)
    ax.set_title("(b) HSSLC 2024, Q26", fontsize=9.5)
    ax = axes[2]
    blank(ax, (-0.7, 4.7), (-0.6, 2.7))
    T, M, Bt = (0, 2), (0, 1), (0, 0)
    res(ax, T, M, "2 Ω", side=1, L=0.6)
    res(ax, M, Bt, "4 Ω", side=1, L=0.6)
    cell(ax, T, (2.0, 2), "4 V", plus_first=True, side=1)
    res(ax, (2.0, 2), (4, 2), "6 Ω", side=1, L=0.8)
    res(ax, M, (4, 1), "8 Ω", side=1, L=0.8)
    cell(ax, Bt, (2.0, 0), "6 V", plus_first=True, side=-1)
    res(ax, (2.0, 0), (4, 0), "1 Ω", side=-1, L=0.6)
    wire(ax, [(4, 2), (4, 1), (4, 0)])
    node(ax, M, "M", dx=-0.3, dy=0)
    node(ax, (4, 1), "N", dx=0.3, dy=0)
    ax.set_title("(c) HSSLC 2020 (New Course), Q28", fontsize=9.5)
    save(fig, "phy_ch03_fig10_board_networks.png")


# ---- Fig 3.11: simple board circuits ---------------------------------------------------------
def fig_board_simple():
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.0))
    ax = axes[0]
    blank(ax, (-0.5, 4.5), (-0.7, 2.6))
    wire(ax, [(0, 0), (0, 1.4), (0.8, 1.4)])
    wire(ax, [(0.8, 2.0), (0.8, 0.85)])
    res(ax, (0.8, 2.0), (3.2, 2.0), "R", side=1)
    res(ax, (0.8, 0.85), (3.2, 0.85), "2 Ω", side=-1)
    wire(ax, [(3.2, 2.0), (3.2, 0.85)])
    wire(ax, [(3.2, 1.4), (4, 1.4), (4, 0)])
    wire(ax, [(0, 0), (1.6, 0)])
    cell(ax, (1.6, 0), (2.4, 0), "15 V", plus_first=True, side=-1)
    wire(ax, [(2.4, 0), (4, 0)])
    ax.set_title("(a) HSSLC 2018, Q4: power 150 W", fontsize=9.5)
    ax = axes[1]
    blank(ax, (-0.8, 4.5), (-0.7, 2.6))
    res(ax, (0, 1.8), (4, 1.8), "R", side=1, L=1.0)
    wire(ax, [(0, 1.8), (0, 0), (1.3, 0)])
    cell(ax, (1.3, 0), (1.9, 0), None, plus_first=True)
    cell(ax, (1.9, 0), (2.5, 0), None, plus_first=True)
    wire(ax, [(2.5, 0), (4, 0), (4, 1.8)])
    ax.text(1.9, -0.45, "each cell: 2 V, 1 Ω", ha="center", fontsize=8.5)
    carrow(ax, (0, 0.9), (0, 1), "I = 0.5 A", off=(-0.75, 0), fs=8.5)
    ax.set_title("(b) HSSLC 2023 and 2025, Q2", fontsize=9.5)
    ax = axes[2]
    blank(ax, (-0.5, 4.6), (-0.7, 2.6))
    wire(ax, [(0, 2), (1.4, 2)])
    cell(ax, (1.4, 2), (2.0, 2), "B", plus_first=True, side=1)
    wire(ax, [(2.0, 2), (4, 2), (4, 0)])
    wire(ax, [(0, 2), (0, 0)])
    lamp(ax, (0, 0), (2.8, 0), "P", side=-1)
    res(ax, (2.8, 0), (4, 0), "Rh", side=-1, L=0.7, rheo=True)
    wire(ax, [(2.8, 0), (2.8, 1.1)])
    lamp(ax, (2.8, 1.1), (4, 1.1), "Q", side=1)
    node(ax, (2.8, 0), "A", dx=-0.2, dy=-0.28)
    node(ax, (4, 1.1))
    ax.set_title("(c) HSSLC 2018, Q26: lamps and a rheostat", fontsize=9.5)
    save(fig, "phy_ch03_fig11_board_simple.png")


if __name__ == "__main__":
    fig_drift()
    fig_vi()
    fig_resistivity()
    fig_cell()
    fig_cells()
    fig_kirchhoff()
    fig_wheatstone()
    fig_ex37()
    fig_board_bridges()
    fig_board_networks()
    fig_board_simple()
