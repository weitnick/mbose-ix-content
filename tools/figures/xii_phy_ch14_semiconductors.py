"""Figures for Class XII Physics Chapter 14, Semiconductor Electronics.
Run: python xii_phy_ch14_semiconductors.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

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
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle=style, mutation_scale=ms, color=color, lw=lw, shrinkA=0, shrinkB=0))


def blank(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")


def wire(ax, pts, color=INK, lw=1.4, ls="-"):
    xs, ys = zip(*[tuple(p) for p in pts])
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_capstyle="round")


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
        m = (a + b) / 2 + nrm * side * (amp + 0.22)
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
        t = m + nrm * side * (hl / 2 + 0.22)
        ax.text(*t, label, ha="center", va="center", fontsize=fs)
    if signs:
        for q, s in ((lp, "+"), (sp, "−")):
            t = q + (q - m) / max(np.hypot(*(q - m)), 1e-9) * 0.16 - nrm * side * 0.3
            ax.text(*t, s, ha="center", va="center", fontsize=10, color=POS if s == "+" else NEG)


def diode(ax, p0, p1, label=None, side=1, s=0.34, fs=9, color=INK):
    """Diode on segment p0-p1: anode (p) on the p0 side, arrow pointing to p1 (conventional current p0 -> p1)."""
    p0, p1, length, u, nrm = _frame(p0, p1)
    m = (p0 + p1) / 2
    a, b = m - u * s / 2, m + u * s / 2
    wire(ax, [p0, a])
    wire(ax, [b, p1])
    h = s * 0.58
    ax.add_patch(Polygon([a + nrm * h, a - nrm * h, b], closed=True, facecolor=color, edgecolor=color, lw=1.0, zorder=4))
    wire(ax, [b + nrm * h, b - nrm * h], color=color, lw=2.0)
    if label:
        ax.text(*(m + nrm * side * (h + 0.24)), label, ha="center", va="center", fontsize=fs)


def cap(ax, p0, p1, label=None, side=1, gap=0.14, hl=0.42, fs=9):
    p0, p1, length, u, nrm = _frame(p0, p1)
    m = (p0 + p1) / 2
    a, b = m - u * gap / 2, m + u * gap / 2
    wire(ax, [p0, a])
    wire(ax, [b, p1])
    for q in (a, b):
        wire(ax, [q - nrm * hl / 2, q + nrm * hl / 2], lw=2.0)
    if label:
        ax.text(*(m + nrm * side * (hl / 2 + 0.22)), label, ha="center", va="center", fontsize=fs)


def meter(ax, p0, p1, label, r=0.24, fs=8.5):
    p0, p1, length, u, nrm = _frame(p0, p1)
    m = (p0 + p1) / 2
    wire(ax, [p0, m - u * r])
    wire(ax, [m + u * r, p1])
    ax.add_patch(Circle(m, r, fill=True, facecolor="white", edgecolor=INK, lw=1.4, zorder=4))
    ax.text(*m, label, ha="center", va="center", fontsize=fs, zorder=5)


def ground(ax, xy, w=0.36):
    x, y = xy
    for i, k in enumerate([1.0, 0.62, 0.28]):
        wire(ax, [(x - w / 2 * k, y - i * 0.09), (x + w / 2 * k, y - i * 0.09)], lw=1.5)


def coil(ax, x, y0, y1, bulge=1, n=4):
    """Vertical coil from y0 to y1 made of n half-loops bulging towards +x (bulge=1) or -x (bulge=-1)."""
    h = (y1 - y0) / n
    t = np.linspace(-np.pi / 2, np.pi / 2, 40)
    for i in range(n):
        yc = y0 + h * (i + 0.5)
        ax.plot(x + bulge * (h / 2) * np.cos(t), yc + (h / 2) * np.sin(t), color=INK, lw=1.4)


def terminal(ax, xy, r=0.07):
    ax.add_patch(Circle(xy, r, fill=True, facecolor="white", edgecolor=INK, lw=1.3, zorder=5))


def transformer(ax, x0, y0, y1, n_pri=4, n_sec=4, sec_y=None):
    """Primary coil at x0 + 0.5 (bulging right), core, secondary at x0 + 1.5 (bulging left).
    Returns the x of the secondary and draws the ac-input leads on the left."""
    xp, xs = x0 + 0.5, x0 + 1.5
    sy0, sy1 = sec_y if sec_y else (y0, y1)
    coil(ax, xp, y0, y1, bulge=1, n=n_pri)
    for xc in (x0 + 0.92, x0 + 1.04):
        wire(ax, [(xc, min(y0, sy0) - 0.15), (xc, max(y1, sy1) + 0.15)], lw=1.2)
    coil(ax, xs, sy0, sy1, bulge=-1, n=n_sec)
    wire(ax, [(xp, y1), (x0 - 0.2, y1)])
    wire(ax, [(xp, y0), (x0 - 0.2, y0)])
    terminal(ax, (x0 - 0.2, y1))
    terminal(ax, (x0 - 0.2, y0))
    ax.text(x0 - 0.45, (y0 + y1) / 2, "ac\ninput", ha="center", va="center", fontsize=8.5)
    return xs


def dot(ax, xy, color=NEG, ms=5.5):
    ax.plot([xy[0]], [xy[1]], "o", color=color, ms=ms, zorder=6)


def hole(ax, xy, color=POS, ms=6.5):
    ax.plot([xy[0]], [xy[1]], "o", mfc="white", mec=color, mew=1.5, ms=ms, zorder=6)


# ---- Fig 14.1: energy bands of metals, insulators and semiconductors --------------------------
def fig_bands():
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6))
    titles = ["(a) Metal", "(b) Insulator", "(c) Semiconductor"]
    rng = np.random.default_rng(3)
    for k, ax in enumerate(axes):
        ax.set_xlim(0, 4)
        ax.set_ylim(-0.4, 6.4)
        ax.axis("off")
        ax.set_title(titles[k], fontsize=10)
        if k == 0:
            ax.add_patch(Rectangle((0.6, 0.4), 2.4, 2.4, facecolor="#C9D7E6", edgecolor=INK, lw=1.2))
            ax.add_patch(Rectangle((0.6, 2.2), 2.4, 2.6, facecolor="none", edgecolor=INK, lw=1.2, ls="--"))
            ax.text(1.8, 1.2, "valence band", ha="center", fontsize=8.5)
            ax.text(1.8, 4.1, "conduction band", ha="center", fontsize=8.5)
            ax.text(3.15, 2.5, "overlap", fontsize=8, color=POS, va="center")
            for _ in range(10):
                dot(ax, (rng.uniform(0.8, 2.8), rng.uniform(2.3, 3.3)), ms=4)
            ax.text(1.8, -0.25, "bands overlap: many free electrons", ha="center", fontsize=8, color=GREY)
        else:
            top_vb, bot_cb = (1.6, 4.4) if k == 1 else (1.6, 2.9)
            ax.add_patch(Rectangle((0.6, 0.2), 2.4, top_vb - 0.2, facecolor="#C9D7E6", edgecolor=INK, lw=1.2))
            ax.add_patch(Rectangle((0.6, bot_cb), 2.4, 1.6, facecolor="white", edgecolor=INK, lw=1.2))
            ax.text(1.8, 0.75, "valence band", ha="center", fontsize=8.5)
            ax.text(1.8, bot_cb + 1.0, "conduction band", ha="center", fontsize=8.5)
            arrow(ax, (3.25, top_vb), (3.25, bot_cb), INK, lw=1.0, ms=8, style="<|-|>")
            ax.text(3.35, (top_vb + bot_cb) / 2, "$E_g$", fontsize=9.5, va="center")
            ax.text(1.8, (top_vb + bot_cb) / 2, "$E_g$ > 3 eV" if k == 1 else "$E_g$ < 3 eV", ha="center", va="center", fontsize=9, color=POS)
            ax.text(0.45, bot_cb, "$E_C$", ha="right", va="center", fontsize=9)
            ax.text(0.45, top_vb, "$E_V$", ha="right", va="center", fontsize=9)
            if k == 2:
                for x in (1.0, 1.6, 2.2, 2.7):
                    dot(ax, (x, bot_cb + 0.3), ms=4.5)
                    hole(ax, (x - 0.05, top_vb - 0.3), ms=5)
                ax.text(1.8, -0.25, "a few electrons cross the gap at room temperature", ha="center", fontsize=8, color=GREY)
            else:
                ax.text(1.8, -0.25, "gap too wide: no free electrons", ha="center", fontsize=8, color=GREY)
    arrow(axes[0], (0.25, 0.4), (0.25, 5.4), GREY, lw=1.0, ms=8)
    axes[0].text(0.12, 2.9, "electron energy", rotation=90, ha="center", va="center", fontsize=8, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch14_fig01_bands.png")


# ---- lattice helpers ---------------------------------------------------------------------------
def lattice(ax, centre_label=None, centre_charge="+4", broken=False, extra_e=False, hole_bond=False):
    sp = 1.7
    pos = {(i, j): (i * sp, j * sp) for i in range(3) for j in range(3)}
    for (i, j), (x, y) in pos.items():
        for di, dj in ((1, 0), (0, 1)):
            if (i + di, j + dj) in pos:
                x2, y2 = pos[(i + di, j + dj)]
                wire(ax, [(x, y), (x2, y2)], color=GREY, lw=1.0)
                mx, my = (x + x2) / 2, (y + y2) / 2
                off = np.array([0.0, 0.17]) if di else np.array([0.17, 0.0])
                elec = [np.array([mx, my]) + off, np.array([mx, my]) - off]
                for q, e in enumerate(elec):
                    if broken and (i, j, di) == (0, 0, 0) and q == 1:
                        hole(ax, e)
                    elif hole_bond and (i, j, di) == (1, 1, 1) and q == 0:
                        hole(ax, e)
                    else:
                        dot(ax, e, ms=4.5)
    for (i, j), (x, y) in pos.items():
        c = (i, j) == (1, 1) and centre_label
        ax.add_patch(Circle((x, y), 0.38, facecolor="#F6E7C8" if c else SOFT, edgecolor=INK, lw=1.2, zorder=5))
        ax.text(x, y + (0.08 if c else 0), centre_label if c else "+4", ha="center", va="center", fontsize=8.5 if c else 9, zorder=7)
        if c:
            ax.text(x, y - 0.18, centre_charge, ha="center", va="center", fontsize=7.5, zorder=7)
    if extra_e:
        x, y = pos[(1, 1)]
        ax.add_patch(Circle((x, y), 0.62, fill=False, edgecolor=NEG, lw=1.0, ls="--", zorder=6))
        dot(ax, (x + 0.44, y + 0.44), ms=5.5)
        ax.annotate("fifth electron,\nweakly bound", (x + 0.48, y + 0.48), (x + 0.9, y + 1.2), fontsize=7.5, color=NEG, ha="center", va="center",
                    arrowprops=dict(arrowstyle="->", color=NEG, lw=0.9))
    return pos


# ---- Fig 14.2: intrinsic silicon --------------------------------------------------------------
def fig_lattice():
    fig, ax = plt.subplots(figsize=(5.6, 3.7))
    blank(ax, (-2.6, 4.1), (-0.9, 3.9))
    lattice(ax, broken=True)
    ax.annotate("hole (+q)", (-0.24, 0.85), (-1.05, 0.35), fontsize=8.5, color=POS, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=POS, lw=0.9))
    dot(ax, (-0.8, 1.3), ms=6)
    arrow(ax, (-0.27, 0.95), (-0.72, 1.24), NEG, lw=1.0, ms=8)
    ax.text(-0.95, 1.45, "free electron (−q)", fontsize=8.5, color=NEG, ha="right", va="bottom")
    ax.text(1.7, -0.75, "+4 = core of a Si (or Ge) atom; dots = shared valence electrons", ha="center", fontsize=8, color=GREY)
    save(fig, "phy_ch14_fig02_lattice.png")


# ---- Fig 14.3: n-type and p-type doping ------------------------------------------------------
def fig_doping():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.3))
    ax = axes[0]
    blank(ax, (-0.8, 4.8), (-1.0, 4.2))
    lattice(ax, centre_label="As", centre_charge="+5", extra_e=True)
    ax.set_title("(a) n-type: pentavalent donor (As, Sb, P)", fontsize=9.5)
    ax.text(1.7, -0.8, "the donor gives one free electron", ha="center", fontsize=8.5, color=GREY)
    ax = axes[1]
    blank(ax, (-0.8, 4.8), (-1.0, 4.2))
    lattice(ax, centre_label="B", centre_charge="+3", hole_bond=True)
    ax.annotate("hole", (2.55, 1.95), (2.55, 2.75), fontsize=8.5, ha="center", color=POS, arrowprops=dict(arrowstyle="->", color=POS, lw=0.9))
    ax.set_title("(b) p-type: trivalent acceptor (B, Al, In)", fontsize=9.5)
    ax.text(1.7, -0.8, "the acceptor leaves one bond with a hole", ha="center", fontsize=8.5, color=GREY)
    fig.tight_layout()
    save(fig, "phy_ch14_fig03_doping.png")


# ---- Fig 14.4: energy bands of doped semiconductors -------------------------------------------
def fig_doped_bands():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.6))
    for k, ax in enumerate(axes):
        ax.set_xlim(-0.4, 4.4)
        ax.set_ylim(-0.6, 5.6)
        ax.axis("off")
        ax.add_patch(Rectangle((0.6, 0.0), 2.6, 1.4, facecolor="#C9D7E6", edgecolor=INK, lw=1.2))
        ax.add_patch(Rectangle((0.6, 3.4), 2.6, 1.4, facecolor="white", edgecolor=INK, lw=1.2))
        ax.text(1.9, 0.5, "valence band", ha="center", fontsize=8.5)
        ax.text(1.9, 4.25, "conduction band", ha="center", fontsize=8.5)
        ax.text(0.45, 3.4, "$E_C$", ha="right", va="center", fontsize=9)
        ax.text(0.45, 1.4, "$E_V$", ha="right", va="center", fontsize=9)
        if k == 0:
            yd = 3.05
            for x in np.linspace(0.85, 2.95, 8):
                wire(ax, [(x - 0.09, yd), (x + 0.09, yd)], color=NEG, lw=2.0)
            ax.text(3.3, yd, "$E_D$ (donor level)", fontsize=8.5, color=NEG, va="center")
            for x in np.linspace(0.9, 2.9, 6):
                dot(ax, (x, 3.7), ms=4.5)
            hole(ax, (1.5, 1.15), ms=5)
            ax.text(1.9, -0.45, "electrons from donors fill the conduction band", ha="center", fontsize=8, color=GREY)
            ax.set_title("(a) n-type", fontsize=10)
        else:
            ya = 1.75
            for x in np.linspace(0.85, 2.95, 8):
                wire(ax, [(x - 0.09, ya), (x + 0.09, ya)], color=POS, lw=2.0)
            ax.text(3.3, ya, "$E_A$ (acceptor level)", fontsize=8.5, color=POS, va="center")
            for x in np.linspace(0.9, 2.9, 6):
                hole(ax, (x, 1.1), ms=5)
            dot(ax, (2.3, 3.7), ms=4.5)
            ax.text(1.9, -0.45, "electrons jump to acceptors, leaving holes", ha="center", fontsize=8, color=GREY)
            ax.set_title("(b) p-type", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch14_fig04_doped_bands.png")


# ---- Fig 14.5: p-n junction formation and barrier potential -----------------------------------
def fig_junction():
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(7.6, 5.6), gridspec_kw=dict(height_ratios=[1.5, 1.0]))
    blank(ax, (-0.3, 8.3), (-1.4, 3.1))
    ax.add_patch(Rectangle((0, 0), 8, 2, facecolor="white", edgecolor=INK, lw=1.4))
    ax.add_patch(Rectangle((3.3, 0), 1.4, 2, facecolor="#F3EBD9", edgecolor="none"))
    wire(ax, [(4, 0), (4, 2)], color=GREY, lw=1.0, ls="--")
    rng = np.random.default_rng(5)
    for _ in range(18):
        hole(ax, (rng.uniform(0.25, 3.05), rng.uniform(0.25, 1.75)), ms=6)
        dot(ax, (rng.uniform(4.95, 7.75), rng.uniform(0.25, 1.75)), ms=5)
    for y in (0.35, 0.85, 1.35, 1.8):
        ax.text(3.65, y - 0.1, "⊖", ha="center", va="center", fontsize=11, color=NEG)
        ax.text(4.35, y - 0.1, "⊕", ha="center", va="center", fontsize=11, color=POS)
    ax.text(1.6, 2.25, "p-region (holes)", ha="center", fontsize=9)
    ax.text(6.4, 2.25, "n-region (electrons)", ha="center", fontsize=9)
    ax.text(4.0, 2.75, "depletion region", ha="center", fontsize=9, color=ACC)
    wire(ax, [(3.3, 2.55), (3.3, 2.05)], color=ACC, lw=0.9)
    wire(ax, [(4.7, 2.55), (4.7, 2.05)], color=ACC, lw=0.9)
    arrow(ax, (4.6, -0.35), (3.4, -0.35), POS, lw=1.6, ms=11)
    ax.text(4.0, -0.62, "E (from n to p)", ha="center", va="top", fontsize=8.5, color=POS)
    arrow(ax, (0.4, -0.35), (2.2, -0.35), INK, lw=1.2, ms=9)
    ax.text(1.3, -0.62, "diffusion current (p → n):\nholes p → n, electrons n → p", ha="center", va="top", fontsize=8)
    arrow(ax, (7.6, -0.35), (5.8, -0.35), INK, lw=1.2, ms=9)
    ax.text(6.7, -0.62, "drift current (n → p),\ncaused by E", ha="center", va="top", fontsize=8)
    ax.set_title("(a) Formation of the depletion region", fontsize=10)
    x = np.linspace(0, 8, 400)
    V = 0.5 * (1 + np.tanh((x - 4) / 0.32))
    bx.plot(x, V, color=NEG, lw=2)
    bx.set_xlim(-0.3, 8.3)
    bx.set_ylim(-0.25, 1.35)
    bx.axvspan(3.3, 4.7, color="#F3EBD9")
    bx.annotate("", (7.2, 1.0), (7.2, 0.0), arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1.0))
    bx.axhline(0, color=GREY, lw=0.6, ls=":")
    bx.axhline(1, color=GREY, lw=0.6, ls=":")
    bx.text(7.35, 0.5, "$V_0$ (barrier\npotential)", fontsize=8.5, va="center")
    bx.text(1.6, 0.12, "p-side", ha="center", fontsize=8.5)
    bx.text(6.0, 1.1, "n-side (positive relative to p)", ha="center", fontsize=8.5)
    bx.set_xticks([])
    bx.set_yticks([])
    bx.set_ylabel("potential", fontsize=9)
    bx.set_xlabel("distance across the junction", fontsize=9)
    bx.spines[["top", "right"]].set_visible(False)
    bx.set_title("(b) Barrier potential with no bias", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch14_fig05_junction.png")


# ---- Fig 14.6: diode symbol, forward and reverse bias -----------------------------------------
def _pn_block(ax, x0, dep_w, forward):
    ax.add_patch(Rectangle((x0, 1.0), 3.6, 1.2, facecolor="white", edgecolor=INK, lw=1.3))
    ax.add_patch(Rectangle((x0 + 1.8 - dep_w / 2, 1.0), dep_w, 1.2, facecolor="#F3EBD9", edgecolor="none"))
    wire(ax, [(x0 + 1.8, 1.0), (x0 + 1.8, 2.2)], color=GREY, lw=0.9, ls="--")
    ax.text(x0 + 0.55, 1.6, "p", ha="center", va="center", fontsize=14, style="italic")
    ax.text(x0 + 3.05, 1.6, "n", ha="center", va="center", fontsize=14, style="italic")
    wire(ax, [(x0, 1.6), (x0 - 0.4, 1.6), (x0 - 0.4, 0.0), (x0 + 1.5, 0.0)])
    cell(ax, (x0 + 1.5, 0.0), (x0 + 2.1, 0.0), "V", plus_first=forward, side=-1, signs=True)
    wire(ax, [(x0 + 2.1, 0.0), (x0 + 4.0, 0.0), (x0 + 4.0, 1.6), (x0 + 3.6, 1.6)])


def fig_bias():
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.4), gridspec_kw=dict(width_ratios=[0.8, 1.2, 1.2]))
    ax = axes[0]
    blank(ax, (-0.3, 3.3), (-0.6, 2.6))
    diode(ax, (0.2, 1.3), (2.8, 1.3), s=0.6)
    ax.text(0.5, 1.75, "p (anode)", ha="center", fontsize=11)
    ax.text(2.5, 1.75, "n (cathode)", ha="center", fontsize=11)
    arrow(ax, (0.9, 0.55), (2.1, 0.55), POS, lw=1.3, ms=10)
    ax.text(1.5, 0.15, "conventional current\nin forward bias", ha="center", va="top", fontsize=9.5, color=POS)
    ax.set_title("(a) Diode symbol", fontsize=11)
    ax = axes[1]
    blank(ax, (-0.8, 4.3), (-0.9, 2.9))
    _pn_block(ax, 0.0, 0.4, True)
    ax.text(1.8, 2.5, "narrow depletion layer", ha="center", fontsize=10, color=ACC)
    ax.text(1.8, -0.75, "barrier falls to $V_0 - V$: large current (mA)", ha="center", fontsize=11)
    ax.set_title("(b) Forward bias: p to +, n to −", fontsize=11)
    ax = axes[2]
    blank(ax, (-0.8, 4.3), (-0.9, 2.9))
    _pn_block(ax, 0.0, 1.4, False)
    ax.text(1.8, 2.5, "wide depletion layer", ha="center", fontsize=10, color=ACC)
    ax.text(1.8, -0.75, "barrier rises to $V_0 + V$: tiny current (μA)", ha="center", fontsize=11)
    ax.set_title("(c) Reverse bias: p to −, n to +", fontsize=11)
    fig.tight_layout()
    save(fig, "phy_ch14_fig06_bias.png")


# ---- Fig 14.7: circuits for the V-I characteristic --------------------------------------------
def _vi_circuit(ax, forward):
    wire(ax, [(0, 0), (0, 2.0), (0.6, 2.0)])
    res(ax, (0.6, 2.0), (1.8, 2.0), "rheostat", side=1, L=0.8, rheo=True)
    meter(ax, (1.8, 2.0), (2.6, 2.0), "mA" if forward else "μA")
    if forward:
        diode(ax, (2.6, 2.0), (3.8, 2.0), "D", side=1)
    else:
        diode(ax, (3.8, 2.0), (2.6, 2.0), "D", side=-1)
    wire(ax, [(3.8, 2.0), (4.4, 2.0), (4.4, 0.0), (2.5, 0.0)])
    cell(ax, (2.5, 0.0), (1.9, 0.0), None, plus_first=False, side=-1, signs=True)
    wire(ax, [(1.9, 0.0), (0, 0)])
    wire(ax, [(2.8, 2.0), (2.8, 1.0), (3.0, 1.0)])
    meter(ax, (3.0, 1.0), (3.4, 1.0), "V", r=0.2)
    wire(ax, [(3.4, 1.0), (3.6, 1.0), (3.6, 2.0)])
    ax.plot([2.8, 3.6], [2.0, 2.0], "o", color=INK, ms=3.5)


def fig_vi_circuits():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.0))
    for ax, fwd, t in ((axes[0], True, "(a) Forward bias (milliammeter)"), (axes[1], False, "(b) Reverse bias (microammeter)")):
        blank(ax, (-0.4, 4.8), (-0.7, 2.8))
        _vi_circuit(ax, fwd)
        ax.set_title(t, fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch14_fig07_vi_circuits.png")


# ---- Fig 14.8: V-I characteristic of a silicon diode ------------------------------------------
def fig_vi_curve():
    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    ax.set_xlim(-3.4, 1.6)
    ax.set_ylim(-2.4, 3.4)
    ax.axis("off")
    arrow(ax, (-3.3, 0), (1.55, 0), INK, lw=1.1, ms=10)
    arrow(ax, (0, -2.35), (0, 3.35), INK, lw=1.1, ms=10)
    xf = np.linspace(0, 0.92, 200)
    k = 3.0 / np.exp(0.92 / 0.055)
    If = k * (np.exp(xf / 0.055) - 1)
    ax.plot(xf, If, color=POS, lw=2.2)
    xr = np.linspace(-2.62, 0, 300)
    Ir = -0.18 * (1 - np.exp(xr / 0.08)) - 0.04 * np.exp((-2.5 - xr) / 0.035) + 0.04 * np.exp(-2.5 / 0.035)
    m = Ir > -2.3
    ax.plot(xr[m], Ir[m], color=NEG, lw=2.2)
    wire(ax, [(0.7, -0.08), (0.7, 0.08)], lw=1.2)
    ax.text(0.7, -0.22, "0.7", ha="center", va="top", fontsize=8.5)
    ax.annotate("threshold (cut-in)\nvoltage ≈ 0.7 V (Si)", (0.72, 0.15), (0.98, 1.0), fontsize=8, arrowprops=dict(arrowstyle="->", color=GREY))
    ax.text(1.55, -0.2, "V (volts)", ha="right", va="top", fontsize=8.5)
    ax.text(0.08, 3.3, "I (mA)", ha="left", va="top", fontsize=8.5)
    ax.text(0.08, -2.3, "I (μA)", ha="left", va="bottom", fontsize=8.5)
    ax.text(-3.3, 0.15, "reverse voltage (volts)", ha="left", va="bottom", fontsize=8.5)
    ax.annotate("breakdown\nvoltage $V_{br}$", (-2.5, -0.5), (-3.25, -1.6), fontsize=8, arrowprops=dict(arrowstyle="->", color=GREY))
    ax.annotate("reverse saturation current\n(tiny, nearly constant)", (-1.2, -0.18), (-2.0, -1.05), fontsize=8, color=NEG,
                arrowprops=dict(arrowstyle="->", color=NEG, lw=0.9))
    ax.text(0.45, 2.6, "forward bias", fontsize=8.5, color=POS, ha="right")
    ax.text(-1.2, 0.45, "reverse bias", fontsize=8.5, color=NEG, ha="center")
    ax.text(-1.6, 3.2, "(the two quadrants have different scales)", fontsize=7.5, color=GREY, ha="center")
    save(fig, "phy_ch14_fig08_vi_curve.png")


# ---- waveform helper ---------------------------------------------------------------------------
def wave_ax(ax, t, y, label, color=NEG, ylim=(-1.2, 1.9), dashed=None):
    if dashed is not None:
        ax.plot(t, dashed, color=GREY, lw=1.0, ls="--")
    ax.plot(t, y, color=color, lw=1.8)
    ax.axhline(0, color=GREY, lw=0.7)
    ax.set_ylim(*ylim)
    ax.set_xlim(0, t[-1])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.01, 0.99, label, transform=ax.transAxes, fontsize=8.5, va="top")
    ax.text(1.01, (0 - ylim[0]) / (ylim[1] - ylim[0]), "t", transform=ax.transAxes, fontsize=8.5, ha="left", va="center", style="italic")


# ---- Fig 14.9: half-wave rectifier ------------------------------------------------------------
def fig_halfwave():
    fig = plt.figure(figsize=(10.0, 3.6))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.25, 1.0], hspace=0.45)
    ax = fig.add_subplot(gs[:, 0])
    blank(ax, (-0.9, 5.5), (-0.5, 3.4))
    xs = transformer(ax, 0.0, 0.5, 2.5)
    wire(ax, [(xs, 2.5), (xs, 2.9), (2.1, 2.9)])
    diode(ax, (2.1, 2.9), (3.5, 2.9), "D", side=1)
    wire(ax, [(3.5, 2.9), (4.2, 2.9)])
    res(ax, (4.2, 2.9), (4.2, 0.1), "$R_L$", side=1, L=1.0)
    wire(ax, [(4.2, 0.1), (xs, 0.1), (xs, 0.5)])
    ax.text(xs - 0.12, 2.98, "A", ha="right", fontsize=9.5, style="italic")
    ax.text(xs - 0.12, 0.02, "B", ha="right", fontsize=9.5, style="italic")
    wire(ax, [(4.2, 2.9), (5.0, 2.9)])
    wire(ax, [(4.2, 0.1), (5.0, 0.1)])
    terminal(ax, (5.0, 2.9))
    terminal(ax, (5.0, 0.1))
    ax.text(5.15, 1.5, "output", rotation=90, ha="center", va="center", fontsize=8.5)
    arrow(ax, (3.85, 1.9), (3.85, 1.1), POS, lw=1.2, ms=9)
    ax.set_title("(a) Half-wave rectifier", fontsize=10)
    t = np.linspace(0, 4 * np.pi, 600)
    wave_ax(fig.add_subplot(gs[0, 1]), t, np.sin(t), "input ac (across AB)")
    wave_ax(fig.add_subplot(gs[1, 1]), t, np.maximum(np.sin(t), 0), "output across $R_L$", color=POS, ylim=(-0.3, 1.6))
    fig.text(0.78, 0.97, "(b) Waveforms", ha="center", fontsize=10, weight="bold")
    save(fig, "phy_ch14_fig09_halfwave.png")


# ---- Fig 14.10: full-wave rectifier -----------------------------------------------------------
def fig_fullwave():
    fig = plt.figure(figsize=(10.4, 4.2))
    gs = fig.add_gridspec(3, 2, width_ratios=[1.2, 1.0], hspace=0.55)
    ax = fig.add_subplot(gs[:, 0])
    blank(ax, (-0.9, 5.4), (-0.9, 4.1))
    xs = transformer(ax, 0.0, 0.6, 2.6, n_pri=4, n_sec=6, sec_y=(0.0, 3.2))
    wire(ax, [(xs, 3.2), (xs, 3.6), (2.2, 3.6)])
    diode(ax, (2.2, 3.6), (3.6, 3.6), "$D_1$", side=1)
    wire(ax, [(3.6, 3.6), (4.4, 3.6), (4.4, -0.4), (3.6, -0.4)])
    diode(ax, (2.2, -0.4), (3.6, -0.4), "$D_2$", side=-1)
    wire(ax, [(2.2, -0.4), (xs, -0.4), (xs, 0.0)])
    wire(ax, [(xs, 1.6), (2.2, 1.6)])
    res(ax, (4.4, 1.6), (2.2, 1.6), "$R_L$", side=-1, L=1.0)
    ax.plot([4.4], [1.6], "o", color=INK, ms=4)
    ax.plot([xs], [1.6], "o", color=INK, ms=4)
    ax.text(xs - 0.12, 3.68, "A", ha="right", fontsize=9.5, style="italic")
    ax.text(xs - 0.12, -0.48, "B", ha="right", fontsize=9.5, style="italic")
    ax.text(xs + 0.12, 1.38, "centre tap", fontsize=8, ha="left", va="top")
    ax.text(4.55, 1.6, "X", fontsize=9.5, style="italic", va="center")
    arrow(ax, (3.85, 2.5), (2.75, 2.5), POS, lw=1.2, ms=9)
    ax.text(3.3, 2.65, "same direction in both halves", ha="center", fontsize=7.5, color=POS)
    ax.text(3.55, 1.12, "output across $R_L$", ha="center", fontsize=8)
    ax.set_title("(a) Full-wave rectifier (centre-tap transformer)", fontsize=10)
    t = np.linspace(0, 4 * np.pi, 600)
    wave_ax(fig.add_subplot(gs[0, 1]), t, np.sin(t), "voltage at A (input to $D_1$)")
    wave_ax(fig.add_subplot(gs[1, 1]), t, -np.sin(t), "voltage at B (input to $D_2$)", color=GREEN)
    cx = fig.add_subplot(gs[2, 1])
    wave_ax(cx, t, np.abs(np.sin(t)), "output across $R_L$", color=POS, ylim=(-0.3, 1.75))
    for i, lab in enumerate(["$D_1$", "$D_2$", "$D_1$", "$D_2$"]):
        cx.text((i + 0.5) * np.pi, 1.12, lab, ha="center", fontsize=7.5)
    fig.text(0.78, 0.96, "(b) Waveforms", ha="center", fontsize=10, weight="bold")
    save(fig, "phy_ch14_fig10_fullwave.png")


# ---- Fig 14.11: capacitor filter --------------------------------------------------------------
def fig_filter():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.0), gridspec_kw=dict(width_ratios=[1.0, 1.1]))
    ax = axes[0]
    blank(ax, (-0.6, 5.2), (-0.5, 2.7))
    ax.add_patch(Rectangle((0.4, 0.3), 1.6, 1.8, facecolor=SOFT, edgecolor=INK, lw=1.2))
    ax.text(1.2, 1.2, "full-wave\nrectifier", ha="center", va="center", fontsize=8.5)
    wire(ax, [(-0.2, 1.6), (0.4, 1.6)])
    wire(ax, [(-0.2, 0.8), (0.4, 0.8)])
    terminal(ax, (-0.2, 1.6))
    terminal(ax, (-0.2, 0.8))
    ax.text(-0.35, 1.2, "ac", ha="right", va="center", fontsize=8.5)
    wire(ax, [(2.0, 1.8), (4.4, 1.8)])
    wire(ax, [(2.0, 0.6), (4.4, 0.6)])
    cap(ax, (3.0, 1.8), (3.0, 0.6), "C", side=-1)
    res(ax, (4.4, 1.8), (4.4, 0.6), "$R_L$", side=-1, L=0.7)
    ax.plot([3.0, 3.0], [1.8, 0.6], "o", color=INK, ms=3.5)
    ax.set_title("(a) Capacitor across the load", fontsize=10)
    bx = axes[1]
    t = np.linspace(0, 4 * np.pi, 1200)
    rect = np.abs(np.sin(t))
    tau = 3.0
    out = np.zeros_like(t)
    v = 0.0
    for i in range(len(t)):
        if i:
            v = v * np.exp(-(t[i] - t[i - 1]) / tau)
        v = max(v, rect[i])
        out[i] = v
    wave_ax(bx, t, out, "output with the filter", color=POS, ylim=(-0.2, 1.5), dashed=rect)
    bx.text(0.98, 0.98, "dashed: without the filter", transform=bx.transAxes, fontsize=8, color=GREY, ha="right", va="top")
    bx.set_title("(b) Smoothed output (small ripple)", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch14_fig11_filter.png")


# ---- Fig 14.12: board circuits (HSSLC 2018 Q36(b), HSSLC 2020 New Course Q18) ----------------
def fig_board():
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 3.6))
    ax = axes[0]
    blank(ax, (-0.7, 4.7), (-0.8, 3.6))
    wire(ax, [(0, 0), (0, 2.0), (0.9, 2.0)])
    wire(ax, [(0.9, 2.5), (0.9, 1.5)])
    diode(ax, (0.9, 2.5), (3.1, 2.5), "$D_1$", side=1)
    diode(ax, (3.1, 1.5), (0.9, 1.5), "$D_2$", side=-1)
    wire(ax, [(3.1, 2.5), (3.1, 1.5)])
    wire(ax, [(3.1, 2.0), (4.0, 2.0)])
    diode(ax, (4.0, 2.0), (4.0, 0.0), "$D_3$", side=-1)
    wire(ax, [(0, 0), (0.5, 0)])
    cell(ax, (0.5, 0), (1.1, 0), "V = 10 V", plus_first=True, side=-1, signs=True)
    res(ax, (1.1, 0), (4.0, 0), "R = 2 Ω", side=-1, L=0.9)
    arrow(ax, (0, 0.8), (0, 1.25), POS, lw=1.4, ms=11)
    ax.text(-0.25, 1.0, "i", fontsize=10, style="italic", color=POS, ha="right")
    ax.text(2.0, 3.4, "each diode: $r_f$ = 1 Ω", ha="center", fontsize=8.5)
    ax.set_title("(a) HSSLC 2018, Q36(b)", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.7, 4.7), (-0.8, 3.6))
    wire(ax, [(0, 0), (0, 2.4)])
    wire(ax, [(4, 0), (4, 2.4)])
    diode(ax, (0, 2.4), (1.9, 2.4), "$D_1$", side=1)
    res(ax, (1.9, 2.4), (4, 2.4), "3 Ω", side=1, L=0.8)
    res(ax, (0, 1.2), (2.2, 1.2), "2 Ω", side=1, L=0.8)
    cell(ax, (2.2, 1.2), (4.0, 1.2), "20 V", plus_first=True, side=-1, signs=True)
    diode(ax, (1.9, 0), (0, 0), "$D_2$", side=-1)
    res(ax, (1.9, 0), (4, 0), "4 Ω", side=-1, L=0.8)
    ax.set_title("(b) HSSLC 2020 (New Course), Q18: ideal diodes", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch14_fig12_board.png")


# ---- Fig 14.13: MBOSE Sample Paper 2026-27, Q30 -----------------------------------------------
def _q30(ax, left, right):
    wire(ax, [(0, 0.6), (0, 2.0), (1.1, 2.0)])
    diode(ax, (1.1, 2.0), (1.9, 2.0), s=0.3)
    wire(ax, [(1.9, 2.0), (3.0, 2.0), (3.0, 0.6)])
    ax.text(1.32, 1.68, "p", ha="center", fontsize=9, style="italic")
    ax.text(1.72, 1.68, "n", ha="center", fontsize=9, style="italic")
    for x, kind in ((0, left), (3.0, right)):
        if kind == "R":
            res(ax, (x, 1.75), (x, 0.6), None, L=0.6, amp=0.1)
        elif kind == "cells+top":
            cell(ax, (x, 1.75), (x, 1.2), None, plus_first=True, gap=0.1, hl=0.4, hs=0.2)
            cell(ax, (x, 1.2), (x, 0.6), None, plus_first=True, gap=0.1, hl=0.4, hs=0.2)
            ax.text(x + 0.32, 1.53, "+", fontsize=10, color=POS, va="center")
        elif kind == "cell+bottom":
            cell(ax, (x, 1.75), (x, 0.6), None, plus_first=False, gap=0.1, hl=0.4, hs=0.2)
            ax.text(x + 0.32, 1.27, "−", fontsize=10, color=NEG, va="center")
        ground(ax, (x, 0.6))


def fig_sample_q30():
    fig, axes = plt.subplots(1, 3, figsize=(8.0, 2.6))
    cases = [("(i)", "R", "cells+top", "n at +, p at 0: reverse"), ("(ii)", "cells+top", "R", "p at +, n at 0: forward"),
             ("(iii)", "cells+top", "cell+bottom", "p at +, n at −: forward")]
    for ax, (t, l, r, note) in zip(axes, cases):
        blank(ax, (-0.8, 3.8), (-0.2, 2.5))
        _q30(ax, l, r)
        ax.set_title(t, fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch14_fig13_sample_q30.png")


if __name__ == "__main__":
    fig_bands()
    fig_lattice()
    fig_doping()
    fig_doped_bands()
    fig_junction()
    fig_bias()
    fig_vi_circuits()
    fig_vi_curve()
    fig_halfwave()
    fig_fullwave()
    fig_filter()
    fig_board()
    fig_sample_q30()
