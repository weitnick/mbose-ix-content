"""Shared helpers for Class XII Mathematics figures (matplotlib).
Figures are written to Class XII Content/Mathematics/Generated Content/figures.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyArrowPatch, Polygon

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Mathematics", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, RED, BLUE, AMBER, GREY, GREEN, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#2E7D32", "#E9F0F7"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11,
                     "mathtext.fontset": "dejavusans"})


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


def arrow(ax, p0, p1, color=INK, lw=1.3, ms=11, text=None, fs=9):
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle="-|>", mutation_scale=ms, color=color, lw=lw,
                                 shrinkA=6, shrinkB=6))
    if text:
        ax.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + 0.2, text, ha="center", va="bottom", fontsize=fs)


def axes(ax, xr, yr, labels=("x", "y"), ticks=True, color=GREY):
    """Draw x and y axes through the origin of a data-coordinate plot (ax must not be equal-aspect off)."""
    ax.axhline(0, color=color, lw=1)
    ax.axvline(0, color=color, lw=1)
    ax.set_xlim(*xr)
    ax.set_ylim(*yr)
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.text(xr[1], 0, " " + labels[0], va="center", fontsize=10)
    ax.text(0, yr[1], labels[1], ha="center", va="bottom", fontsize=10)
    if not ticks:
        ax.set_xticks([])
        ax.set_yticks([])
    ax.tick_params(labelsize=8, colors=GREY)
