"""Figures for Class X Science, Chapter 13: Our Environment.
Run: python x_sci_ch13_environment.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_sci_ch05_life_processes import ACC, GREEN, GREY, HI, INK, LGREEN, SOFT, TAN, finish, save
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

LEVEL_COLS = ["#CDE8C5", "#FCE7B2", "#F8CFC0", "#E7C9E8", "#C9DDF2"]


def box(ax, c, text, fc, w=1.5, h=0.6, size=8.5):
    ax.add_patch(FancyBboxPatch((c[0] - w / 2, c[1] - h / 2), w, h, boxstyle="round,pad=0.04", fc=fc, ec=INK, lw=0.9, zorder=3))
    ax.text(c[0], c[1], text, ha="center", va="center", fontsize=size, zorder=4)


def arr(ax, p0, p1, color=INK, lw=1.2, rad=0.0, z=2):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=12, color=color, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}", zorder=z, shrinkA=2, shrinkB=2))


# Fig 13.1: food chains in (a) a forest, (b) a grassland and (c) a pond
def fig_food_chains():
    chains = [("(a) forest", ["trees and\nshrubs", "deer", "tiger"]),
              ("(b) grassland", ["grass", "grasshopper", "frog", "snake", "eagle"]),
              ("(c) pond", ["phytoplankton\n(algae)", "zooplankton", "small fish", "large fish"])]
    fig, ax = plt.subplots(figsize=(8.6, 3.8))
    for r, (name, items) in enumerate(chains):
        y = 2.4 - r * 1.2
        ax.text(-0.3, y, name, ha="right", va="center", fontsize=9, fontweight="bold")
        for i, t in enumerate(items):
            x = 0.9 + i * 1.95
            box(ax, (x, y), t, LEVEL_COLS[i], w=1.55, h=0.7, size=8)
            if i:
                arr(ax, (x - 1.95 + 0.8, y), (x - 0.8, y))
    ax.text(5.0, -0.75, "arrows show the direction of flow of food (energy): the eaten → the eater", ha="center", fontsize=8.5, color=ACC)
    finish(ax, (-2.0, 9.6), (-1.0, 2.9))
    save(fig, "sci_ch13_fig01_food_chains.png")


# Fig 13.2: trophic levels and the 10 per cent law
def fig_trophic():
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    levels = [("producers (green plants)", "first trophic level", "10 000 J"),
              ("primary consumers (herbivores)", "second trophic level", "1000 J"),
              ("secondary consumers (small carnivores)", "third trophic level", "100 J"),
              ("tertiary consumers (large carnivores)", "fourth trophic level", "10 J")]
    base, hgt = 7.0, 0.85
    for i, (who, lvl, en) in enumerate(levels):
        w = base - i * 1.6
        y = i * hgt
        ax.add_patch(Polygon([(-w / 2, y), (w / 2, y), (w / 2 - 0.8, y + hgt), (-w / 2 + 0.8, y + hgt)], closed=True,
                             fc=LEVEL_COLS[i], ec=INK, lw=1.0))
        ax.text(0, y + hgt / 2, who, ha="center", va="center", fontsize=8.3)
        ax.text(-base / 2 - 0.2, y + hgt / 2, lvl, ha="right", va="center", fontsize=8.3)
        ax.text(base / 2 + 0.2, y + hgt / 2, en, ha="left", va="center", fontsize=8.5, color=HI, fontweight="bold")
        if i:
            ax.text(base / 2 + 1.85, y, "10%", ha="left", va="center", fontsize=8, color=HI)
            arr(ax, (base / 2 + 1.7, y - hgt / 2 + 0.15), (base / 2 + 1.7, y + hgt / 2 - 0.15), color=HI)
    ax.text(base / 2 + 0.2, 4 * hgt + 0.25, "energy available", ha="left", fontsize=8.5, color=HI)
    ax.text(0, -0.35, "only about 10% of the energy at one level reaches the next", ha="center", va="top", fontsize=8.5)
    finish(ax, (-6.2, 6.9), (-0.7, 3.9))
    save(fig, "sci_ch13_fig02_trophic_levels.png")


# Fig 13.3: a food web
def fig_food_web():
    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    bird = "insect-eating\nbird"
    nodes = {"grass": (0.5, 0.4), "grain plants": (3.0, 0.4), "fruit trees": (5.6, 0.4),
             "grasshopper": (0.0, 1.9), "rabbit": (1.8, 1.9), "rat": (3.6, 1.9), "deer": (5.4, 1.9),
             "frog": (0.0, 3.3), "snake": (1.8, 3.3), bird: (3.6, 3.3), "lion": (5.6, 3.3),
             "eagle": (2.7, 4.6)}
    fcs = {0.4: LEVEL_COLS[0], 1.9: LEVEL_COLS[1], 3.3: LEVEL_COLS[2], 4.6: LEVEL_COLS[3]}
    w, h = 1.35, 0.55
    for k, (x, y) in nodes.items():
        box(ax, (x, y), k, fcs[y], w=w, h=h, size=7.8)
    edges = [("grass", "grasshopper"), ("grass", "rabbit"), ("grass", "deer"), ("grain plants", "rat"), ("grain plants", "rabbit"),
             ("fruit trees", "deer"), ("grasshopper", "frog"), ("grasshopper", bird), ("frog", "snake"), ("rat", "snake"),
             ("rabbit", "snake"), ("rabbit", "lion"), ("deer", "lion"), ("snake", "eagle"), (bird, "eagle")]

    def edge_t(ux, uy):
        tx = (w / 2 + 0.06) / abs(ux) if abs(ux) > 1e-9 else 1e9
        ty = (h / 2 + 0.06) / abs(uy) if abs(uy) > 1e-9 else 1e9
        return min(tx, ty)

    for a, b in edges:
        (x0, y0), (x1, y1) = nodes[a], nodes[b]
        d = math.hypot(x1 - x0, y1 - y0)
        ux, uy = (x1 - x0) / d, (y1 - y0) / d
        t = edge_t(ux, uy)
        arr(ax, (x0 + t * ux, y0 + t * uy), (x1 - t * ux, y1 - t * uy), color=GREY, lw=1.0, z=4)
    ax.text(3.5, -0.25, "many food chains linked together form a food web", ha="center", va="top", fontsize=8.5)
    finish(ax, (-0.9, 7.9), (-0.6, 5.0))
    save(fig, "sci_ch13_fig03_food_web.png")


# Fig 13.4: flow of energy in an ecosystem
def fig_energy_flow():
    fig, ax = plt.subplots(figsize=(8.2, 4.0))
    ax.add_patch(Circle((-0.3, 2.3), 0.55, fc="#F9D56E", ec=INK, lw=1.0))
    ax.text(-0.3, 2.3, "Sun", ha="center", va="center", fontsize=9, fontweight="bold")
    xs = [1.9, 3.9, 5.9, 7.9]
    names = ["producers", "herbivores", "carnivores", "top\ncarnivores"]
    for i, (x, n) in enumerate(zip(xs, names)):
        box(ax, (x, 2.3), n, LEVEL_COLS[i], w=1.45, h=0.75)
        ax.annotate("", xy=(x, 1.25), xytext=(x, 1.9), arrowprops=dict(arrowstyle="-|>", color="#C0392B", lw=1.2))
        ax.text(x, 1.12, "heat lost", ha="center", va="top", fontsize=7.8, color="#C0392B")
        ax.annotate("", xy=(4.9 + (x - 4.9) * 0.25, 0.2), xytext=(x, 1.92), arrowprops=dict(arrowstyle="-|>", color=GREY, lw=0.8, ls=(0, (3, 2))))
    arr(ax, (0.25, 2.3), (1.15, 2.3), color=HI, lw=1.6)
    for a, b in zip(xs[:-1], xs[1:]):
        arr(ax, (a + 0.75, 2.3), (b - 0.75, 2.3), color=HI, lw=1.6)
    ax.text(0.7, 2.55, "about 1%\ncaptured", fontsize=7.8, ha="center", color=HI)
    for a, b in zip(xs[:-1], xs[1:]):
        ax.text((a + b) / 2, 2.55, "10%", fontsize=8, ha="center", color=HI)
    box(ax, (4.9, 0.0), "decomposers (dead remains and wastes)", "#E2E2E2", w=4.2, h=0.5, size=8)
    ax.text(4.9, 3.25, "energy flows in one direction only (unidirectional) and decreases at each level", ha="center", fontsize=8.5, color=ACC)
    finish(ax, (-1.0, 8.8), (-0.4, 3.5))
    save(fig, "sci_ch13_fig04_energy_flow.png")


# Fig 13.5: biological magnification (illustrative values from a classic DDT study)
def fig_magnification():
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    labels = ["water", "zooplankton", "small fish", "large fish", "fish-eating\nbirds"]
    ppm = [0.00005, 0.04, 0.5, 2.0, 25.0]
    cols = ["#C9DDF2", LEVEL_COLS[0], LEVEL_COLS[1], LEVEL_COLS[2], LEVEL_COLS[3]]
    ax.bar(range(5), ppm, color=cols, edgecolor=INK, lw=0.9)
    ax.set_yscale("log")
    ax.set_ylim(1e-5, 200)
    ax.set_xticks(range(5))
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel("pesticide (DDT) concentration, ppm\n(log scale)", fontsize=8.5)
    for i, v in enumerate(ppm):
        ax.text(i, v * 1.6, ("%.5f" % v).rstrip("0").rstrip(".") if v < 0.01 else f"{v:g}", ha="center", va="bottom", fontsize=8.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_title("concentration increases at each trophic level (illustrative values)", fontsize=9)
    fig.tight_layout()
    save(fig, "sci_ch13_fig05_magnification.png")


# Fig 13.6: formation of ozone and the ozone shield
def fig_ozone():
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    ax.add_patch(Rectangle((-4, 0), 8, 0.5, fc="#9CC48A", ec="none"))
    ax.text(-3.8, 0.25, "Earth's surface", fontsize=8.5, va="center")
    ax.add_patch(Rectangle((-4, 2.6), 8, 0.6, fc="#C9DDF2", ec="none"))
    ax.text(-3.8, 2.9, "ozone layer (stratosphere)", fontsize=8.5, va="center", color=ACC)
    ax.add_patch(Circle((3.4, 4.3), 0.45, fc="#F9D56E", ec=INK))
    ax.text(3.4, 4.3, "Sun", ha="center", va="center", fontsize=8.5, fontweight="bold")
    for x in (-1.5, 0.0, 1.5):
        ax.annotate("", xy=(x, 3.25), xytext=(x + 1.2, 4.4), arrowprops=dict(arrowstyle="-|>", color="#8E44AD", lw=1.5))
        ax.plot([x - 0.08, x + 0.08], [3.15, 3.35], color="#C0392B", lw=2)
        ax.plot([x - 0.08, x + 0.08], [3.35, 3.15], color="#C0392B", lw=2)
    ax.text(-1.0, 4.45, "harmful ultraviolet (UV) rays", fontsize=8.5, color="#8E44AD", ha="center")
    ax.text(0.0, 1.95, "O₂  —UV→  O + O          O + O₂  →  O₃ (ozone)", ha="center", fontsize=10)
    ax.text(0.0, 1.35, "ozone absorbs most UV radiation, protecting life from skin cancer and other damage", ha="center", fontsize=8.3)
    ax.text(0.0, 0.85, "CFCs (refrigerants, fire extinguishers) destroy ozone → thinning of the layer", ha="center", fontsize=8.3, color="#C0392B")
    finish(ax, (-4, 4), (0, 4.9))
    save(fig, "sci_ch13_fig06_ozone.png")


if __name__ == "__main__":
    fig_food_chains()
    fig_trophic()
    fig_food_web()
    fig_energy_flow()
    fig_magnification()
    fig_ozone()
