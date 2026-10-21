"""Figures for Class X Science, Chapter 2: Acids, Bases and Salts.
Run: python x_sci_ch02_acids_bases_salts.py   (writes PNGs into Class X Content/Science/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Science", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, SHADE = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#BFD3E6"
WATER, FLAME = "#D6E9F8", "#F4A300"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def label(ax, xy, text, xytext, ha="left"):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=9, color=INK, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8), annotation_clip=False)


def tube(ax, x, y_top, y_bot, w, fill_to=None, fill=WATER):
    r = w / 2
    ax.plot([x - r, x - r], [y_top, y_bot + r], color=INK, lw=1.3)
    ax.plot([x + r, x + r], [y_top, y_bot + r], color=INK, lw=1.3)
    t = np.linspace(np.pi, 2 * np.pi, 40)
    ax.plot(x + r * np.cos(t), y_bot + r + r * np.sin(t), color=INK, lw=1.3)
    if fill_to is not None:
        xs = list(x + r * np.cos(t)) + [x + r, x - r]
        ys = list(y_bot + r + r * np.sin(t)) + [fill_to, fill_to]
        ax.add_patch(Polygon(np.c_[xs, ys], closed=True, fc=fill, ec="none", zorder=0))


def stopper(ax, x, y, w):
    ax.add_patch(Polygon([[x - w / 2 - 0.05, y + 0.25], [x + w / 2 + 0.05, y + 0.25], [x + w / 2 - 0.03, y - 0.05], [x - w / 2 + 0.03, y - 0.05]],
                         closed=True, fc="#8B5A2B", ec=INK, lw=0.8, zorder=3))


def finish(ax, xl, yl):
    ax.set_xlim(*xl)
    ax.set_ylim(*yl)
    ax.set_aspect("equal")
    ax.axis("off")


# Fig 2.1: zinc granules with dilute sulphuric acid; hydrogen bubbles in soap solution burn with a pop
def fig_zinc_acid():
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    tube(ax, 1.0, 3.0, 0.3, 0.8, fill_to=1.6)
    for gx, gy in ((0.85, 0.55), (1.1, 0.5), (1.0, 0.75)):
        ax.add_patch(Polygon([[gx - 0.12, gy - 0.08], [gx + 0.1, gy - 0.1], [gx + 0.13, gy + 0.08], [gx - 0.05, gy + 0.12]], closed=True, fc="#9AA3AD", ec=INK, lw=0.6))
    for k in range(6):
        ax.add_patch(Circle((0.8 + 0.08 * k, 1.0 + 0.1 * k), 0.035, fc="white", ec=ACC, lw=0.6))
    stopper(ax, 1.0, 3.0, 0.8)
    # delivery tube
    ax.plot([1.0, 1.0, 3.3, 3.3], [3.25, 3.7, 3.7, 1.3], color=INK, lw=1.4)
    # trough with soap solution
    ax.add_patch(Rectangle((2.6, 0.3), 1.6, 1.4, fc="none", ec=INK, lw=1.3))
    ax.add_patch(Rectangle((2.62, 0.32), 1.56, 1.1, fc="#EDE3F7", ec="none", zorder=0))
    for k, (bx, by, rr) in enumerate(((3.2, 1.55, 0.12), (3.45, 1.6, 0.14), (3.0, 1.58, 0.1), (3.65, 1.62, 0.11))):
        ax.add_patch(Circle((bx, by), rr, fc="white", ec="#8E6CB5", lw=0.8))
    # candle and pop
    ax.add_patch(Rectangle((4.8, 0.3), 0.25, 1.1, fc="#F5F0E1", ec=INK, lw=1.0))
    ax.add_patch(Polygon([[4.86, 1.4], [4.925, 1.75], [4.99, 1.4]], closed=True, fc=FLAME, ec="#C46A00", lw=0.6))
    ax.text(4.55, 2.15, "“pop”", fontsize=10, color=HI, fontweight="bold")
    label(ax, (0.75, 0.55), "zinc granules", (-1.9, 0.4))
    label(ax, (0.62, 1.3), "dilute sulphuric acid", (-1.9, 1.9))
    label(ax, (2.0, 3.7), "delivery tube", (1.4, 4.2))
    label(ax, (4.1, 0.9), "soap solution", (4.6, -0.2))
    label(ax, (3.45, 1.74), "bubbles filled\nwith hydrogen", (4.3, 2.9))
    label(ax, (4.93, 0.9), "burning candle", (5.5, 1.2))
    finish(ax, (-2.0, 6.6), (-0.4, 4.4))
    save(fig, "sci_ch02_fig01_zinc_acid.png")


# Fig 2.2: carbon dioxide from a carbonate and acid passed through lime water
def fig_lime_water():
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    tube(ax, 1.0, 3.0, 0.3, 0.8, fill_to=1.4)
    for k in range(5):
        ax.add_patch(Circle((0.85 + 0.07 * k, 0.9 + 0.1 * k), 0.035, fc="white", ec=ACC, lw=0.6))
    stopper(ax, 1.0, 3.0, 0.8)
    ax.plot([1.0, 1.0, 3.2, 3.2], [3.25, 3.6, 3.6, 0.9], color=INK, lw=1.4)
    tube(ax, 3.2, 2.6, 0.3, 0.8, fill_to=1.6, fill="#F2F2F2")
    for k in range(4):
        ax.add_patch(Circle((3.15 + 0.06 * k, 1.0 + 0.12 * k), 0.035, fc="white", ec=GREY, lw=0.6))
    label(ax, (0.62, 0.8), "sodium carbonate\n+ dilute HCl", (-2.0, 1.0))
    label(ax, (2.2, 3.6), "CO₂ gas", (1.9, 4.1))
    label(ax, (3.5, 1.2), "lime water,\nCa(OH)₂, turns milky", (4.2, 1.2))
    finish(ax, (-2.1, 5.9), (-0.1, 4.3))
    save(fig, "sci_ch02_fig02_lime_water.png")


# Fig 2.3: an acid solution conducts electricity
def fig_conductivity():
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    ax.add_patch(Polygon([[0.8, 2.4], [1.0, 0.2], [3.0, 0.2], [3.2, 2.4]], closed=True, fc="none", ec=INK, lw=1.4))
    ax.add_patch(Polygon([[0.85, 1.8], [1.0, 0.22], [3.0, 0.22], [3.15, 1.8]], closed=True, fc=WATER, ec="none", zorder=0))
    ax.add_patch(Rectangle((1.4, 2.25), 1.2, 0.3, fc="#C9A27A", ec=INK, lw=0.9, zorder=3))
    for x in (1.7, 2.3):
        ax.plot([x, x], [0.6, 2.25], color="#555555", lw=2.2)
    # circuit
    ax.plot([1.7, 1.7, 0.6, 0.6], [2.55, 3.4, 3.4, 4.0], color=INK, lw=1.2)
    ax.plot([2.3, 2.3, 4.6, 4.6], [2.55, 3.4, 3.4, 4.0], color=INK, lw=1.2)
    ax.plot([0.6, 1.5], [4.0, 4.0], color=INK, lw=1.2)
    ax.add_patch(Circle((1.85, 4.0), 0.3, fc="#FFF3B0", ec=INK, lw=1.2))
    ax.plot([1.7, 2.0], [3.85, 4.15], color=INK, lw=0.9)
    ax.plot([1.7, 2.0], [4.15, 3.85], color=INK, lw=0.9)
    ax.plot([2.15, 2.8], [4.0, 4.0], color=INK, lw=1.2)
    ax.plot([2.8, 3.25], [4.0, 4.25], color=INK, lw=1.2)
    ax.plot([3.3, 3.6], [4.0, 4.0], color=INK, lw=1.2)
    for x0, tall in ((3.6, True), (3.8, False), (4.0, True), (4.2, False)):
        ax.plot([x0, x0], [3.75, 4.25] if tall else [3.85, 4.15], color=INK, lw=2.0 if tall else 1.2)
    ax.plot([4.2, 4.6], [4.0, 4.0], color=INK, lw=1.2)
    for a in range(0, 360, 45):
        ax.plot([1.85 + 0.38 * np.cos(np.radians(a)), 1.85 + 0.55 * np.cos(np.radians(a))],
                [4.0 + 0.38 * np.sin(np.radians(a)), 4.0 + 0.55 * np.sin(np.radians(a))], color=HI, lw=1.0)
    label(ax, (1.85, 3.7), "bulb glows", (-0.6, 3.0))
    label(ax, (3.0, 4.1), "switch", (2.5, 4.9))
    label(ax, (3.9, 4.25), "6 V battery", (4.3, 4.9))
    label(ax, (1.7, 1.2), "iron nails", (-0.6, 1.6))
    label(ax, (1.8, 2.4), "cork", (-0.6, 2.4))
    label(ax, (2.9, 0.9), "dilute HCl\n(ions carry\nthe current)", (3.7, 1.2))
    finish(ax, (-0.8, 5.4), (0.0, 5.2))
    save(fig, "sci_ch02_fig03_conductivity.png")


# Fig 2.4: the pH scale with some common substances
def fig_ph_scale():
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    cols = ["#C0392B", "#D9472B", "#E8602C", "#F07F2B", "#F5A623", "#F7C948", "#C9D94B", "#7DC36B",
            "#43A88C", "#2E8FA8", "#2C6FB5", "#3355A8", "#4A3F9A", "#5B2D8C", "#4B1F70"]
    for v in range(15):
        ax.add_patch(Rectangle((v * 0.5, 1.2), 0.5, 0.5, fc=cols[v], ec="white", lw=0.8))
        ax.text(v * 0.5 + 0.25, 1.45, str(v), ha="center", va="center", fontsize=9, color="white", fontweight="bold")
    ax.annotate("", xy=(0.0, 0.95), xytext=(3.4, 0.95), arrowprops=dict(arrowstyle="->", color="#C0392B", lw=1.3))
    ax.text(1.7, 0.75, "increasingly acidic (more H⁺)", ha="center", va="top", fontsize=8.5, color="#C0392B")
    ax.annotate("", xy=(7.5, 0.95), xytext=(4.1, 0.95), arrowprops=dict(arrowstyle="->", color="#3355A8", lw=1.3))
    ax.text(5.8, 0.75, "increasingly basic (more OH⁻)", ha="center", va="top", fontsize=8.5, color="#3355A8")
    ax.text(3.75, 0.75, "neutral", ha="center", va="top", fontsize=8.5, color="#2E7D32")
    items = [(1.2, "gastric juice ~1.2", 0), (2.2, "lemon juice ~2.2", 1), (4.2, "tomato juice ~4.2", 2),
             (6.5, "milk ~6.5", 0), (7.0, "pure water 7", 1), (7.4, "blood ~7.4", 2),
             (10.0, "milk of magnesia ~10", 0), (14.0, "1 M NaOH ~14", 1)]
    for v, t, lvl in items:
        x = v * 0.5 + 0.25
        y = 2.0 + 0.34 * lvl
        ax.plot([x, x], [1.72, y - 0.04], color=GREY, lw=0.8)
        ax.text(x, y, t, ha="center", va="bottom", fontsize=8, color=INK)
    finish(ax, (-0.3, 7.8), (0.3, 3.1))
    save(fig, "sci_ch02_fig04_ph_scale.png")


# Fig 2.5: products of the chlor-alkali process and their uses
def fig_chlor_alkali():
    fig, ax = plt.subplots(figsize=(7.0, 3.8))

    def box(x, y, w, h, title, body, fc, tc=INK):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.12", fc=fc, ec=ACC, lw=1.1))
        ax.text(x + w / 2, y + h - 0.2, title, ha="center", va="top", fontsize=9, color=tc, fontweight="bold")
        if body:
            ax.text(x + w / 2, y + h - 0.6, body, ha="center", va="top", fontsize=8.2, color=INK, linespacing=1.35)

    box(2.2, 3.2, 3.0, 1.0, "Brine (NaCl solution)", "electrolysis", HI, "white")
    ax.text(3.7, 2.95, "2NaCl + 2H₂O → 2NaOH + Cl₂ + H₂", ha="center", va="center", fontsize=8.5, color=INK)
    w = 2.45
    items = [(0.0, "Hydrogen (cathode)", "fuels; margarine\n(hydrogenation of oils);\nammonia for fertilisers"),
             (2.55, "Chlorine (anode)", "water treatment; PVC;\ndisinfectants; pesticides;\nbleaching powder"),
             (5.1, "Sodium hydroxide", "soaps and detergents;\npaper making;\nartificial fibres;\ndegreasing metals")]
    for x, t, b in items:
        box(x, 0.0, w, 2.2, t, b, SOFT)
        ax.annotate("", xy=(x + w / 2, 2.25), xytext=(3.7, 2.75), arrowprops=dict(arrowstyle="->", color=GREY, lw=1.0))
    finish(ax, (-0.2, 7.8), (-0.2, 4.4))
    save(fig, "sci_ch02_fig05_chlor_alkali.png")


if __name__ == "__main__":
    fig_zinc_acid()
    fig_lime_water()
    fig_conductivity()
    fig_ph_scale()
    fig_chlor_alkali()
