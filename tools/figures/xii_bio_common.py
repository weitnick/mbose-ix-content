"""Shared helpers for Class XII Biology figures (matplotlib schematics).
Figures are written to Class XII Content/Biology/Generated Content/figures.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle, Wedge

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Biology", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, RED, BLUE, AMBER, GREY, GREEN, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#2E7D32", "#E9F0F7"
PALE_GREEN, PALE_AMBER, PALE_RED, PALE_BLUE = "#E3F1E4", "#FBF0DC", "#F6E1DE", "#DCE8F4"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def canvas(w=6.0, h=4.0, xlim=(0, 10), ylim=(0, 7)):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def label(ax, xy, txt_xy, text, fs=8.5, color=INK, ha=None):
    """Leader line from a point on the drawing to its label."""
    if ha is None:
        ha = "left" if txt_xy[0] >= xy[0] else "right"
    ax.annotate(text, xy=xy, xytext=txt_xy, fontsize=fs, color=color, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8, shrinkA=0, shrinkB=0))


def arrow(ax, p0, p1, color=INK, lw=1.3, ms=11, text=None, fs=8.5, dy=0.18):
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle="-|>", mutation_scale=ms, color=color, lw=lw,
                                 shrinkA=4, shrinkB=4))
    if text:
        ax.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + dy, text, ha="center", va="bottom", fontsize=fs, color=color)


def box(ax, xy, w, h, text, fc=SOFT, ec=BLUE, fs=9, bold=False):
    ax.add_patch(FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.05,rounding_size=0.15", fc=fc, ec=ec, lw=1.2))
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center", fontsize=fs,
            weight="bold" if bold else "normal", color=INK)
