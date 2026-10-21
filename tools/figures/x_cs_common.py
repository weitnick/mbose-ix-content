"""Shared drawing helpers for Class X Computer Science figures (copy of x_ss_common).
Figures go to Class X Content/Computer Science/Generated Content/figures as cs_chNN_figMM_*.png.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Computer Science", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, GREY = "#1D2733", "#1F4E79", "#B7791F", "#7A8794"
FILLS = ["#DCEBF8", "#FCE7B2", "#CDE8C5", "#F8CFC0", "#E7C9E8", "#E2E2E2", "#C9F0EC"]
plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.08, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def finish(ax, xl, yl):
    ax.set_xlim(*xl)
    ax.set_ylim(*yl)
    ax.axis("off")


def box(ax, c, text, fc=FILLS[0], w=2.0, h=0.7, size=8.5, bold=False, ec=INK):
    ax.add_patch(FancyBboxPatch((c[0] - w / 2, c[1] - h / 2), w, h, boxstyle="round,pad=0.04", fc=fc, ec=ec, lw=0.9, zorder=3))
    ax.text(c[0], c[1], text, ha="center", va="center", fontsize=size, zorder=4, fontweight="bold" if bold else "normal",
            wrap=True)


def arrow(ax, p0, p1, color=INK, lw=1.1, rad=0.0, style="-|>"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=11, color=color, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}", zorder=2, shrinkA=1, shrinkB=1))


def timeline(events, name, title=None, width=9.0, row_h=0.62, label_w=6.6, colors=None):
    """events: list of (year_text, description[, fill_index]). Drawn as a vertical timeline, top to bottom."""
    n = len(events)
    fig, ax = plt.subplots(figsize=(width, 0.55 + row_h * n))
    x0 = 1.15
    ax.plot([x0, x0], [0.2, n * row_h + 0.1], color=GREY, lw=2, zorder=1)
    for i, ev in enumerate(events):
        year, desc = ev[0], ev[1]
        fi = ev[2] if len(ev) > 2 else 0
        y = n * row_h - (i + 0.5) * row_h + 0.15
        ax.plot([x0], [y], "o", ms=7, color=ACC, zorder=3)
        ax.text(x0 - 0.18, y, year, ha="right", va="center", fontsize=9, fontweight="bold", color=ACC)
        ax.add_patch(FancyBboxPatch((x0 + 0.3, y - row_h * 0.38), label_w, row_h * 0.76, boxstyle="round,pad=0.02",
                                    fc=FILLS[fi % len(FILLS)], ec="none", zorder=2))
        ax.text(x0 + 0.42, y, desc, ha="left", va="center", fontsize=8.6, zorder=3)
    if title:
        ax.text(0.0, n * row_h + 0.35, title, fontsize=10, fontweight="bold", color=INK)
    finish(ax, (-0.4, x0 + label_w + 0.5), (0.0, n * row_h + 0.55 if title else n * row_h + 0.25))
    save(fig, name)


def tree(root, children, name, grand=None, width=9.0, title=None, child_w=2.0, size=8.3):
    """root: text; children: list of texts; grand: dict child_index -> list of texts (shown under that child)."""
    grand = grand or {}
    n = len(children)
    depth = max((len(v) for v in grand.values()), default=0)
    hgt = 2.0 + 0.62 * depth
    fig, ax = plt.subplots(figsize=(width, 1.0 + hgt * 0.75))
    span = max(n * (child_w + 0.25), 4)
    xs = [-(span / 2) + (i + 0.5) * span / n for i in range(n)]
    top = hgt
    box(ax, (0, top), root, FILLS[0], w=max(2.6, len(root) * 0.115), h=0.6, size=9, bold=True)
    for i, (x, t) in enumerate(zip(xs, children)):
        box(ax, (x, top - 1.15), t, FILLS[(i + 1) % len(FILLS)], w=child_w, h=0.62, size=size)
        arrow(ax, (0, top - 0.3), (x, top - 0.84))
        for j, g in enumerate(grand.get(i, [])):
            y = top - 1.85 - j * 0.62
            ax.text(x, y, "• " + g, ha="center", va="center", fontsize=size - 0.5)
    if title:
        ax.text(-span / 2, top + 0.6, title, fontsize=10, fontweight="bold")
    finish(ax, (-span / 2 - 0.2, span / 2 + 0.2), (top - 1.6 - 0.62 * depth, top + (0.85 if title else 0.45)))
    save(fig, name)


def flow(steps, name, width=9.0, fills=None, title=None, w=1.9, h=0.85, size=8.2, vertical=False):
    """A left-to-right (or top-to-bottom) chain of boxes joined by arrows."""
    n = len(steps)
    if vertical:
        fig, ax = plt.subplots(figsize=(width, 0.4 + n * 0.9))
        for i, s in enumerate(steps):
            y = (n - 1 - i) * 1.15
            box(ax, (0, y), s, FILLS[(fills[i] if fills else i) % len(FILLS)], w=w, h=h, size=size)
            if i:
                arrow(ax, (0, y + 1.15 - h / 2), (0, y + h / 2))
        if title:
            ax.text(-w / 2, (n - 1) * 1.15 + 0.75, title, fontsize=10, fontweight="bold")
        finish(ax, (-w / 2 - 0.2, w / 2 + 0.2), (-h / 2 - 0.1, (n - 1) * 1.15 + (1.0 if title else 0.55)))
    else:
        gap = 0.45
        fig, ax = plt.subplots(figsize=(width, 1.6 if not title else 2.0))
        for i, s in enumerate(steps):
            x = i * (w + gap)
            box(ax, (x, 0), s, FILLS[(fills[i] if fills else i) % len(FILLS)], w=w, h=h, size=size)
            if i:
                arrow(ax, (x - w - gap + w / 2, 0), (x - w / 2, 0))
        if title:
            ax.text(-w / 2, h / 2 + 0.35, title, fontsize=10, fontweight="bold")
        finish(ax, (-w / 2 - 0.1, (n - 1) * (w + gap) + w / 2 + 0.1), (-h / 2 - 0.1, h / 2 + (0.6 if title else 0.15)))
    save(fig, name)


def table_fig(headers, rows, name, col_w=None, width=9.0, title=None, size=8.3, header_fill=FILLS[0]):
    """A simple drawn table, used where a figure reads better than a Markdown table (e.g. comparisons)."""
    ncol = len(headers)
    col_w = col_w or [width / ncol] * ncol
    rh = 0.42
    fig, ax = plt.subplots(figsize=(sum(col_w) * 0.75, 0.4 + rh * (len(rows) + 1) * 0.9))
    x = 0
    xs = []
    for w in col_w:
        xs.append(x)
        x += w
    total_w = x
    for j, htext in enumerate(headers):
        ax.add_patch(FancyBboxPatch((xs[j], -rh), col_w[j], rh, boxstyle="square,pad=0", fc=header_fill, ec=INK, lw=0.6))
        ax.text(xs[j] + 0.08, -rh / 2, htext, va="center", fontsize=size, fontweight="bold")
    for i, row in enumerate(rows):
        y = -(i + 2) * rh
        for j, cell in enumerate(row):
            ax.add_patch(FancyBboxPatch((xs[j], y), col_w[j], rh, boxstyle="square,pad=0", fc="white", ec=INK, lw=0.5))
            ax.text(xs[j] + 0.08, y + rh / 2, cell, va="center", fontsize=size)
    if title:
        ax.text(0, 0.25, title, fontsize=10, fontweight="bold")
    finish(ax, (-0.05, total_w + 0.05), (-(len(rows) + 1) * rh - 0.05, 0.55 if title else 0.05))
    save(fig, name)
