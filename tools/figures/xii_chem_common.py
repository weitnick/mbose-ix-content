"""Shared drawing helpers for Class XII Chemistry figures (structures drawn with matplotlib).

draw(ax, atoms, bonds): atoms = {key: (x, y, label)}; label "" draws a bare skeletal vertex.
  bonds = [(a, b, kind)], kind: 1, 2, 3, "dash" (hashed), "wedge" (solid wedge from a to b), "dot" (dotted / partial).
ring(ax, cx, cy, r, n=6, start=90, aromatic=True): draws a benzene-type ring and returns its vertex list.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Chemistry", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, RED, BLUE, AMBER, GREY, GREEN, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#2E7D32", "#E9F0F7"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def canvas(w=6.0, h=3.6, xlim=(0, 10), ylim=(0, 6)):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def _shrink(p, q, s):
    p, q = np.array(p, float), np.array(q, float)
    d = q - p
    n = np.linalg.norm(d)
    if n == 0:
        return p, q
    u = d / n
    return p + u * s[0], q - u * s[1]


def draw(ax, atoms, bonds, color=INK, fs=11, lw=1.6, gap=0.09, pad=0.28):
    for a, b, kind in bonds:
        xa, ya, la = atoms[a]
        xb, yb, lb = atoms[b]
        sa = pad if la else 0.0
        sb = pad if lb else 0.0
        p, q = _shrink((xa, ya), (xb, yb), (sa, sb))
        d = q - p
        nrm = np.array([-d[1], d[0]]) / (np.linalg.norm(d) or 1)
        if kind == 1:
            ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, solid_capstyle="round")
        elif kind == 2:
            for s in (-1, 1):
                o = nrm * gap * s
                ax.plot([p[0] + o[0], q[0] + o[0]], [p[1] + o[1], q[1] + o[1]], color=color, lw=lw)
        elif kind == "2in":  # ring double bond drawn inside (second line shorter)
            ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw)
        elif kind == 3:
            for s in (-1.4, 0, 1.4):
                o = nrm * gap * s
                ax.plot([p[0] + o[0], q[0] + o[0]], [p[1] + o[1], q[1] + o[1]], color=color, lw=lw * 0.9)
        elif kind == "dot":
            ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, ls=(0, (1.5, 2)))
        elif kind == "wedge":
            w = nrm * 0.12
            ax.add_patch(Polygon([p, q + w, q - w], closed=True, color=color))
        elif kind == "dash":
            for t in np.linspace(0.1, 1, 7):
                c = p + d * t
                w = nrm * 0.12 * t
                ax.plot([c[0] - w[0], c[0] + w[0]], [c[1] - w[1], c[1] + w[1]], color=color, lw=1.1)
    for k, (x, y, lab) in atoms.items():
        if lab:
            ax.text(x, y, lab, ha="center", va="center", fontsize=fs, color=color,
                    bbox=dict(fc="white", ec="none", pad=0.4))


def ring(ax, cx, cy, r=0.8, n=6, start=90, aromatic=True, color=INK, lw=1.6, kekule=False, doubles=None):
    ang = np.radians(start + np.arange(n) * 360 / n)
    pts = [(cx + r * np.cos(a), cy + r * np.sin(a)) for a in ang]
    for i in range(n):
        p, q = pts[i], pts[(i + 1) % n]
        ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw)
        if (kekule and i % 2 == 0) or (doubles is not None and i in doubles):
            m = np.array([(p[0] + q[0]) / 2, (p[1] + q[1]) / 2])
            c = np.array([cx, cy])
            pi, qi = np.array(p) + (c - np.array(p)) * 0.2, np.array(q) + (c - np.array(q)) * 0.2
            ax.plot([pi[0], qi[0]], [pi[1], qi[1]], color=color, lw=lw)
    if aromatic and not kekule and doubles is None:
        ax.add_patch(Circle((cx, cy), r * 0.58, fill=False, ec=color, lw=lw * 0.9))
    return pts


def arrow(ax, p0, p1, color=INK, lw=1.4, ms=12, style="-|>", text=None, above=None, fs=9):
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0))
    if text:
        ax.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + 0.25, text, ha="center", va="bottom", fontsize=fs)
    if above:
        ax.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 - 0.25, above, ha="center", va="top", fontsize=fs)


def tetra(ax, cx, cy, centre, ligands, r=1.0, fs=11, charge=None, bonds=None):
    """Tetrahedral oxo-anion drawn flat: centre atom with four ligands at up, right, down, left."""
    pos = [(cx, cy + r), (cx + r, cy), (cx, cy - r), (cx - r, cy)]
    atoms = {"M": (cx, cy, centre)}
    bl = []
    for i, (lab, p) in enumerate(zip(ligands, pos)):
        atoms[f"L{i}"] = (p[0], p[1], lab)
        bl.append(("M", f"L{i}", (bonds or [1, 1, 1, 1])[i]))
    draw(ax, atoms, bl, fs=fs)
    if charge:
        ax.text(cx + r + 0.35, cy + r * 0.85, charge, fontsize=fs - 1)
    return atoms
