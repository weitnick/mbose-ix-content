"""Figures for Class X Science, Chapter 6: Control and Coordination.
Run: python x_sci_ch06_control.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_sci_ch05_life_processes import (ACC, GREEN, GREY, HI, INK, LGREEN, PINK, SHADE, SOFT, TAN, blob, finish, label, save,
                                       smooth, tube_path)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle

NERVE = "#E9D9F2"
NERVE_EC = "#7B4F9E"


# Fig 6.1: structure of a neuron and a neuromuscular junction
def fig_neuron():
    fig, axs = plt.subplots(2, 1, figsize=(7.4, 5.6), gridspec_kw={"height_ratios": [1.4, 1]})
    ax = axs[0]
    # dendrites
    for a in (110, 140, 170, 200, 230, 250):
        r = math.radians(a)
        p0 = (0.55 * math.cos(r), 0.55 * math.sin(r))
        p1 = (1.3 * math.cos(r), 1.3 * math.sin(r))
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=NERVE_EC, lw=1.6)
        for da in (-25, 25):
            r2 = math.radians(a + da)
            ax.plot([p1[0], p1[0] + 0.4 * math.cos(r2)], [p1[1], p1[1] + 0.4 * math.sin(r2)], color=NERVE_EC, lw=1.0)
    blob(ax, [(-0.6, 0.0), (-0.3, 0.55), (0.3, 0.5), (0.65, 0.15), (0.6, -0.25), (0.2, -0.55), (-0.35, -0.5)], NERVE, ec=NERVE_EC)
    ax.add_patch(Circle((0.0, 0.0), 0.2, fc="#B48CC8", ec=NERVE_EC, lw=0.8))
    # axon with myelin segments
    ax.plot([0.62, 6.0], [0.0, 0.0], color=NERVE_EC, lw=1.4)
    for k in range(6):
        ax.add_patch(FancyBboxPatch((1.0 + k * 0.82, -0.14), 0.68, 0.28, boxstyle="round,pad=0.01,rounding_size=0.12", fc="#F6EEF9", ec=NERVE_EC, lw=0.8))
    # nerve endings
    for a in (-40, -15, 15, 40):
        r = math.radians(a)
        ax.plot([6.0, 6.0 + 0.6 * math.cos(r)], [0.0, 0.6 * math.sin(r)], color=NERVE_EC, lw=1.2)
        ax.add_patch(Circle((6.0 + 0.65 * math.cos(r), 0.65 * math.sin(r)), 0.07, fc=NERVE_EC, ec="none"))
    ax.annotate("", xy=(4.4, 0.55), xytext=(2.2, 0.55), arrowprops=dict(arrowstyle="->", color=HI, lw=1.4))
    ax.text(3.3, 0.72, "direction of the impulse", ha="center", fontsize=8.5, color=HI)
    label(ax, (-1.2, 0.8), "dendrites (receive\ninformation)", (-2.3, 1.6), ha="right")
    label(ax, (-0.35, 0.35), "cell body", (-2.3, 0.4), ha="right")
    label(ax, (0.0, -0.05), "nucleus", (-2.3, -0.6), ha="right")
    label(ax, (2.6, -0.1), "axon (carries the electrical impulse)", (2.0, -1.0))
    label(ax, (6.4, -0.4), "nerve endings (impulse\nturned into a chemical signal)", (5.0, -1.6))
    ax.text(-2.8, 2.2, "(a) Structure of a neuron", fontsize=9.5, color=INK, fontweight="bold")
    finish(ax, (-4.6, 7.2), (-2.0, 2.4))
    ax = axs[1]
    ax.plot([-1.5, 1.2], [0.3, 0.3], color=NERVE_EC, lw=1.4)
    ax.add_patch(Ellipse((1.45, 0.3), 0.55, 0.8, fc=NERVE, ec=NERVE_EC, lw=1.0))
    for k in range(5):
        ax.add_patch(Circle((1.55, 0.05 + k * 0.13), 0.05, fc=HI, ec="none"))
    ax.add_patch(Rectangle((1.95, -0.6), 3.2, 1.8, fc="#F2B8A2", ec=INK, lw=1.0))
    for k in range(6):
        ax.plot([1.95, 5.15], [-0.45 + k * 0.3, -0.45 + k * 0.3], color="#D98C72", lw=0.8)
    label(ax, (1.55, 0.6), "axon ending with\nchemical messengers", (2.0, 1.55))
    label(ax, (1.82, 0.0), "synapse (gap)", (0.0, -0.6), ha="right")
    label(ax, (3.6, 0.4), "muscle cell", (5.5, 1.0))
    ax.text(-2.4, 1.65, "(b) Neuromuscular junction", fontsize=9.5, color=INK, fontweight="bold")
    finish(ax, (-2.6, 7.2), (-1.0, 1.9))
    save(fig, "sci_ch06_fig01_neuron.png")


# Fig 6.2: reflex arc
def fig_reflex_arc():
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    # spinal cord cross-section
    ax.add_patch(Ellipse((4.6, 2.2), 2.2, 1.8, fc="#F7F1E0", ec=INK, lw=1.2))
    blob(ax, [(4.1, 2.9), (4.6, 2.5), (5.1, 2.9), (5.0, 2.2), (5.1, 1.5), (4.6, 1.9), (4.1, 1.5), (4.2, 2.2)], "#D9CDE6", ec=NERVE_EC)
    ax.text(4.6, 3.3, "spinal cord", ha="center", fontsize=9)
    # arm / hand with skin receptor and muscle
    ax.add_patch(FancyBboxPatch((0.0, 0.5), 2.2, 0.7, boxstyle="round,pad=0.05,rounding_size=0.3", fc="#F3D3BE", ec=INK, lw=1.0))
    ax.add_patch(Ellipse((0.9, 1.9), 1.5, 0.55, fc="#E58C77", ec=INK, lw=1.0))
    ax.add_patch(Circle((0.35, 1.1), 0.1, fc=HI, ec=INK, lw=0.8))
    # flame
    ax.add_patch(Polygon([[-0.3, 0.6], [-0.15, 1.1], [0.0, 0.6]], closed=True, fc="#F4A300", ec="#C46A00", lw=0.8))
    # sensory neuron
    ax.plot(*smooth([(0.35, 1.1), (1.5, 1.35), (2.8, 2.8), (3.8, 2.85), (4.3, 2.55)], closed=False).T, color="#2E6DB4", lw=1.8)
    # relay neuron
    ax.plot([4.3, 4.6, 4.9], [2.55, 2.2, 1.85], color=HI, lw=1.8)
    # motor neuron back to muscle
    ax.plot(*smooth([(4.9, 1.85), (3.8, 1.5), (2.6, 1.6), (1.6, 1.85)], closed=False).T, color="#C0392B", lw=1.8)
    ax.annotate("", xy=(1.62, 1.86), xytext=(2.0, 1.75), arrowprops=dict(arrowstyle="->", color="#C0392B", lw=1.8))
    ax.annotate("", xy=(3.5, 2.85), xytext=(3.1, 2.84), arrowprops=dict(arrowstyle="->", color="#2E6DB4", lw=1.8))
    label(ax, (0.35, 1.1), "receptor in the skin\n(detects heat)", (-1.5, -0.2), ha="left")
    label(ax, (2.6, 2.4), "sensory neuron", (1.4, 3.6), ha="left")
    label(ax, (4.6, 2.2), "relay neuron", (6.3, 2.6))
    label(ax, (3.2, 1.55), "motor neuron", (6.3, 1.2))
    label(ax, (0.9, 2.1), "effector: muscle\n(pulls the hand away)", (-1.6, 3.2), ha="left")
    finish(ax, (-1.8, 8.4), (-0.6, 3.9))
    save(fig, "sci_ch06_fig02_reflex_arc.png")


# Fig 6.3: human brain
def fig_brain():
    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    blob(ax, [(-2.6, 0.6), (-2.4, 1.9), (-1.2, 2.8), (0.6, 2.9), (2.0, 2.3), (2.6, 1.2), (2.2, 0.4), (0.8, 0.2), (-0.6, 0.0), (-1.9, -0.1)], "#F4C7C3")
    for pts in ([(-1.8, 1.9), (-1.2, 2.3), (-0.6, 1.9)], [(-0.2, 2.5), (0.3, 2.0), (0.9, 2.4)], [(1.2, 1.7), (1.7, 1.3), (2.1, 1.6)],
                [(-2.1, 1.0), (-1.4, 1.3), (-0.8, 0.9)], [(-0.2, 1.3), (0.4, 1.1), (1.0, 1.4)]):
        ax.plot(*smooth(pts, closed=False).T, color="#C98A86", lw=1.0)
    blob(ax, [(0.8, 0.3), (1.4, 0.1), (2.1, -0.3), (2.2, -0.9), (1.6, -1.2), (0.9, -0.9)], "#E7B0A9")
    for k in range(5):
        ax.plot([1.0, 2.05], [-0.2 - k * 0.18, -0.4 - k * 0.15], color="#C98A86", lw=0.8)
    ax.add_patch(FancyBboxPatch((0.15, -0.3), 0.55, 0.55, boxstyle="round,pad=0.02,rounding_size=0.15", fc="#D9A3B8", ec=INK, lw=0.9))
    ax.add_patch(Ellipse((0.35, -0.75), 0.45, 0.4, fc="#C98FB0", ec=INK, lw=0.9))
    tube_path(ax, [(0.55, -0.95), (0.6, -1.6), (0.65, -2.4)], 0.32, "#D9C7E6")
    ax.add_patch(Ellipse((-0.15, -0.05), 0.3, 0.2, fc="#F3D58A", ec=INK, lw=0.8))
    ax.add_patch(Circle((-0.35, -0.38), 0.11, fc="#E8A13A", ec=INK, lw=0.8))
    labels = [((-1.2, 1.8), "fore-brain (cerebrum):\nthinking, senses, voluntary actions", (-6.6, 2.9)),
              ((-0.15, -0.05), "hypothalamus", (-5.2, 0.6)),
              ((-0.35, -0.38), "pituitary gland", (-5.2, -0.2)),
              ((0.45, 0.0), "mid-brain", (3.0, 0.9)),
              ((1.6, -0.6), "cerebellum: posture,\nbalance, precise movements", (3.0, -0.2)),
              ((0.35, -0.8), "pons", (3.0, -1.2)),
              ((0.6, -1.4), "medulla: involuntary actions\n(heartbeat, BP, salivation, vomiting)", (3.0, -2.0)),
              ((0.65, -2.2), "spinal cord", (-5.2, -2.2))]
    for xy, t, xt in labels:
        label(ax, xy, t, xt, ha="left" if xt[0] > 0 else "left", size=8.5)
    ax.text(-5.2, -2.95, "Hind-brain = cerebellum + pons + medulla", fontsize=8.5, color=HI)
    finish(ax, (-6.8, 6.4), (-3.2, 3.4))
    save(fig, "sci_ch06_fig03_brain.png")


# Fig 6.4: the sensitive plant before and after touch
def fig_sensitive():
    fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.8))
    for ax, closed in zip(axs, (False, True)):
        ax.plot([0, 3.2], [0, 0.4], color="#6B4F2A", lw=2)
        for k in range(9):
            x = 0.3 + k * 0.33
            y = x * 0.125
            if not closed:
                ax.add_patch(Ellipse((x, y + 0.28), 0.14, 0.45, angle=8, fc=GREEN, ec="none"))
                ax.add_patch(Ellipse((x, y - 0.28), 0.14, 0.45, angle=-8, fc=GREEN, ec="none"))
            else:
                ax.add_patch(Ellipse((x, y + 0.08), 0.12, 0.3, angle=60, fc=GREEN, ec="none"))
                ax.add_patch(Ellipse((x, y - 0.08), 0.12, 0.3, angle=-60, fc=GREEN, ec="none"))
        ax.text(1.6, -0.9, "(a) leaflets open" if not closed else "(b) leaflets fold after touch", ha="center", fontsize=8.5)
        finish(ax, (-0.3, 3.5), (-1.2, 1.1))
    save(fig, "sci_ch06_fig04_sensitive.png")


# Fig 6.5: phototropism set-up and the action of auxin
def fig_phototropism():
    fig, axs = plt.subplots(1, 2, figsize=(7.6, 3.8))
    ax = axs[0]
    ax.add_patch(Polygon([[0, 0], [2.6, 0], [2.6, 3.0], [0, 3.0]], closed=True, fc="none", ec="#8B6B45", lw=1.4))
    ax.plot([2.6, 2.6], [0, 3.0], color="white", lw=3)
    ax.add_patch(Polygon([[0.6, 0.1], [1.6, 0.1], [1.25, 1.2], [0.95, 1.2]], closed=True, fc="#D6E9F8", ec=INK, lw=1.0))
    ax.plot([0.9, 1.3], [1.3, 1.3], color=GREY, lw=2)
    ax.plot(*smooth([(1.1, 1.3), (1.15, 1.8), (1.5, 2.3), (1.95, 2.55)], closed=False).T, color=GREEN, lw=2)
    ax.add_patch(Ellipse((2.0, 2.6), 0.3, 0.14, angle=20, fc=GREEN, ec="none"))
    ax.plot(*smooth([(1.1, 1.3), (0.95, 0.9), (0.75, 0.6)], closed=False).T, color="#8B6B45", lw=1.6)
    for k in range(3):
        ax.annotate("", xy=(2.7, 1.2 + k * 0.6), xytext=(3.5, 1.2 + k * 0.6), arrowprops=dict(arrowstyle="->", color=HI, lw=1.4))
    ax.text(3.6, 1.8, "light from\nthe window", fontsize=8.5, color=HI, va="center")
    ax.text(1.3, -0.4, "shoot bends towards light,\nroot away from it", ha="center", va="top", fontsize=8.5)
    label(ax, (0.3, 2.8), "box open on one side", (-0.4, 3.4))
    finish(ax, (-0.6, 4.8), (-1.3, 3.7))
    ax = axs[1]
    ax.add_patch(Polygon([[0.8, 0], [1.2, 0], [1.25, 1.8], [1.6, 2.6], [1.3, 2.75], [0.9, 2.0]], closed=True, fc=LGREEN, ec=GREEN, lw=1.2))
    for k in range(5):
        ax.add_patch(Circle((0.95 + 0.04 * k, 1.0 + 0.3 * k), 0.06, fc=HI, ec="none"))
    for k in range(3):
        ax.annotate("", xy=(1.6, 0.8 + k * 0.6), xytext=(2.6, 0.8 + k * 0.6), arrowprops=dict(arrowstyle="->", color=HI, lw=1.4))
    ax.text(2.7, 1.4, "light", fontsize=8.5, color=HI, va="center")
    label(ax, (0.95, 1.6), "auxin collects on the\nshady side; cells there\ngrow longer", (-3.0, 2.6))
    label(ax, (1.4, 2.6), "shoot tip makes auxin", (1.8, 3.3))
    finish(ax, (-3.2, 3.6), (-0.4, 3.6))
    save(fig, "sci_ch06_fig05_phototropism.png")


# Fig 6.6: geotropism
def fig_geotropism():
    fig, ax = plt.subplots(figsize=(4.6, 3.6))
    ax.add_patch(Polygon([[-1.0, -0.1], [1.0, -0.1], [0.75, -2.0], [-0.75, -2.0]], closed=True, fc="#B5743B", ec=INK, lw=1.0))
    ax.add_patch(Rectangle((-1.0, -0.4), 2.0, 0.3, fc="#8B6B45", ec="none"))
    ax.plot([0, 0], [-0.25, 1.6], color=GREEN, lw=2)
    for y in (0.6, 1.1, 1.5):
        ax.add_patch(Ellipse((0.25, y), 0.45, 0.16, angle=25, fc=GREEN, ec="none"))
        ax.add_patch(Ellipse((-0.25, y), 0.45, 0.16, angle=-25, fc=GREEN, ec="none"))
    for x in (-0.4, -0.15, 0.15, 0.4):
        ax.plot(*smooth([(0, -0.3), (x * 0.6, -0.9), (x, -1.6)], closed=False).T, color="#F3E5B8", lw=1.6)
    ax.annotate("", xy=(0, 2.3), xytext=(0, 1.75), arrowprops=dict(arrowstyle="->", color=HI, lw=1.4))
    ax.annotate("", xy=(1.6, -2.0), xytext=(1.6, -0.9), arrowprops=dict(arrowstyle="->", color=ACC, lw=1.6))
    ax.text(1.75, -1.45, "gravity", fontsize=8.5, color=ACC, va="center")
    label(ax, (0.05, 1.3), "shoot grows up, away\nfrom gravity (negative\ngeotropism)", (1.0, 1.4))
    label(ax, (-0.3, -1.3), "roots grow down, towards\ngravity (positive geotropism)", (-5.4, -1.5))
    finish(ax, (-5.6, 3.6), (-2.2, 2.5))
    save(fig, "sci_ch06_fig06_geotropism.png")


# Fig 6.7: endocrine glands in human beings
def fig_endocrine():
    fig, ax = plt.subplots(figsize=(6.4, 6.6))
    ax.add_patch(Circle((0, 5.2), 0.75, fc="#F6E3D6", ec=INK, lw=1.0))
    blob(ax, [(-0.35, 4.45), (0.35, 4.45), (1.4, 3.9), (1.25, 1.2), (0.8, 0.2), (-0.8, 0.2), (-1.25, 1.2), (-1.4, 3.9)], "#F6E3D6")
    glands = [((0.0, 5.45), 0.12, "#E8A13A", "hypothalamus: releasing hormones", (1.6, 6.2)),
              ((0.05, 5.15), 0.1, "#C98FB0", "pituitary: growth hormone", (1.6, 5.5)),
              ((0.0, 4.25), 0.16, "#E06A5F", "thyroid: thyroxin (needs iodine)", (1.6, 4.6)),
              ((0.0, 3.6), 0.16, "#F3D58A", "thymus", (1.6, 3.8)),
              ((-0.55, 2.35), 0.12, "#B5743B", "adrenal glands: adrenaline", (1.6, 2.9)),
              ((0.3, 2.0), 0.14, "#F1C27D", "pancreas: insulin", (1.6, 2.0)),
              ((0.0, 0.45), 0.13, "#9FB8D9", "testes (male): testosterone /\novaries (female): oestrogen", (1.6, 0.9))]
    for (x, y), r, c, t, xt in glands:
        ax.add_patch(Circle((x, y), r, fc=c, ec=INK, lw=0.7))
        label(ax, (x + r, y), t, xt, size=8.5)
    ax.add_patch(Circle((0.55, 2.35), 0.12, fc="#B5743B", ec=INK, lw=0.7))
    ax.add_patch(Ellipse((-0.55, 2.0), 0.25, 0.4, fc="#D99A8A", ec=INK, lw=0.6))
    ax.add_patch(Ellipse((0.55, 2.0), 0.25, 0.4, fc="#D99A8A", ec=INK, lw=0.6))
    label(ax, (-0.62, 1.95), "kidneys", (-3.0, 1.2), ha="left")
    finish(ax, (-3.8, 5.6), (-0.1, 6.5))
    save(fig, "sci_ch06_fig07_endocrine.png")


if __name__ == "__main__":
    fig_neuron()
    fig_reflex_arc()
    fig_brain()
    fig_sensitive()
    fig_phototropism()
    fig_geotropism()
    fig_endocrine()
