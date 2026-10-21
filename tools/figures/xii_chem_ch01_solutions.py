"""Figures for Class XII Chemistry Chapter 1, Solutions.
Run: python xii_chem_ch01_solutions.py   (writes PNGs into Class XII Content/Chemistry/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Chemistry", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, RED, BLUE, AMBER, GREY, SOFT, GREEN = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#E9F0F7", "#2E7D32"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def arrow(ax, p0, p1, color=INK, lw=1.4, ms=11, style="-|>"):
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0))


def vp_axes(ax, title):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.05)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["x₁ = 1\nx₂ = 0", "x₁ = 0\nx₂ = 1"])
    ax.set_yticks([])
    ax.set_ylabel("Vapour pressure", labelpad=16)
    ax.set_xlabel("Mole fraction")
    ax.set_title(title)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def fig01_raoult_ideal():
    fig, ax = plt.subplots(figsize=(5.2, 3.8))
    vp_axes(ax, "Ideal solution (Raoult's law)")
    x2 = np.linspace(0, 1, 50)
    p1o, p2o = 0.55, 0.9
    p1, p2 = p1o * (1 - x2), p2o * x2
    ax.plot(x2, p1, color=BLUE, lw=2, label="p₁ = p₁° x₁")
    ax.plot(x2, p2, color=RED, lw=2, label="p₂ = p₂° x₂")
    ax.plot(x2, p1 + p2, color=INK, lw=2.4, label="p_total = p₁ + p₂")
    ax.text(-0.02, p1o, "p₁°", ha="right", va="center", color=BLUE)
    ax.text(1.02, p2o, "p₂°", ha="left", va="center", color=RED)
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    save(fig, "chem_ch01_fig01_raoult_ideal.png")


def fig02_deviations():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.8))
    x2 = np.linspace(0, 1, 60)
    p1o, p2o = 0.55, 0.85
    for ax, sign, title in ((axs[0], 1, "(a) Positive deviation"), (axs[1], -1, "(b) Negative deviation")):
        vp_axes(ax, title)
        bump = sign * 0.28 * x2 * (1 - x2)
        p1 = p1o * (1 - x2) * (1 + sign * 0.55 * x2 ** 1.6)
        p2 = p2o * x2 * (1 + sign * 0.55 * (1 - x2) ** 1.6)
        ideal = p1o * (1 - x2) + p2o * x2
        ax.plot(x2, ideal, color=GREY, lw=1.2, ls="--", label="ideal (Raoult)")
        ax.plot(x2, p1, color=BLUE, lw=1.8, label="p₁")
        ax.plot(x2, p2, color=RED, lw=1.8, label="p₂")
        ax.plot(x2, p1 + p2, color=INK, lw=2.4, label="p_total")
        ax.legend(loc="upper left" if sign > 0 else "upper left", frameon=False, fontsize=8)
    axs[0].text(0.5, 0.06, "e.g. ethanol + acetone,\nCS₂ + acetone", ha="center", fontsize=8.5, color=INK)
    axs[1].text(0.5, 0.06, "e.g. chloroform + acetone,\nHNO₃ + water", ha="center", fontsize=8.5, color=INK)
    save(fig, "chem_ch01_fig02_deviations.png")


def fig03_bp_elevation():
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    T = np.linspace(0, 1, 100)
    ax.plot(T, 0.08 + 0.85 * T ** 2.2, color=BLUE, lw=2, label="pure solvent")
    ax.plot(T, 0.08 + 0.85 * (T - 0.1).clip(0) ** 2.2 * 1.0, color=RED, lw=2, label="solution")
    ax.axhline(0.6, color=GREY, ls="--", lw=1)
    ax.text(0.01, 0.62, "1 atm (1.013 bar)", fontsize=8.5, color=GREY)
    tb0 = (0.52 / 0.85) ** (1 / 2.2)
    tb = tb0 + 0.1
    for t, c in ((tb0, BLUE), (tb, RED)):
        ax.plot([t, t], [0, 0.6], color=c, lw=1, ls=":")
    ax.set_xticks([tb0, tb])
    ax.set_xticklabels(["T_b°", "T_b"])
    arrow(ax, (tb0, 0.2), (tb, 0.2), color=INK, style="<|-|>", ms=8)
    ax.text((tb0 + tb) / 2, 0.23, "ΔT_b", ha="center", fontsize=9)
    ax.set_yticks([])
    ax.set_ylabel("Vapour pressure")
    ax.set_xlabel("Temperature / K")
    ax.set_title("Elevation of boiling point")
    ax.legend(frameon=False, loc="upper left", fontsize=9)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "chem_ch01_fig03_bp_elevation.png")


def fig04_fp_depression():
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    T = np.linspace(0, 1, 100)
    solid = 0.05 + 1.6 * T ** 2.5
    liquid = 0.18 + 0.55 * T ** 1.6
    liquid_sol = liquid - 0.07
    ax.plot(T, solid, color=GREY, lw=2, label="frozen solvent (solid)")
    ax.plot(T, liquid, color=BLUE, lw=2, label="liquid solvent")
    ax.plot(T, liquid_sol, color=RED, lw=2, label="solution")
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 1)

    def cross(a, b):
        i = np.argmin(abs(a - b))
        return T[i], a[i]

    tf0, p0 = cross(solid, liquid)
    tf, p = cross(solid, liquid_sol)
    for t, c in ((tf0, BLUE), (tf, RED)):
        ax.plot([t, t], [0, np.interp(t, T, solid)], color=c, lw=1, ls=":")
    ax.set_xticks([tf, tf0])
    ax.set_xticklabels(["T_f", "T_f°"])
    arrow(ax, (tf, 0.06), (tf0, 0.06), color=INK, style="<|-|>", ms=8)
    ax.text((tf + tf0) / 2, 0.09, "ΔT_f", ha="center", fontsize=9)
    ax.set_yticks([])
    ax.set_ylabel("Vapour pressure")
    ax.set_xlabel("Temperature / K")
    ax.set_title("Depression of freezing point")
    ax.legend(frameon=False, loc="upper left", fontsize=8.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "chem_ch01_fig04_fp_depression.png")


def fig05_osmosis():
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 4.0))
    for ax, rev in ((axs[0], False), (axs[1], True)):
        ax.set_xlim(0, 10)
        ax.set_ylim(-0.8, 8)
        ax.axis("off")
        # vessel
        ax.add_patch(Rectangle((1, 0.5), 8, 4.2, fill=False, lw=1.8, ec=INK))
        ax.plot([5, 5], [0.5, 4.7], color=AMBER, lw=3, ls=(0, (2, 1.2)))
        lv_left, lv_right = (3.2, 3.2) if rev else (2.7, 3.7)
        ax.add_patch(Rectangle((1, 0.5), 4, lv_left - 0.5, color="#D6E6F5"))
        ax.add_patch(Rectangle((5, 0.5), 4, lv_right - 0.5, color="#F5DAD6"))
        ax.text(3, 1.4, "solvent\n(water)", ha="center", fontsize=9)
        ax.text(7, 1.4, "solution", ha="center", fontsize=9)
        ax.text(5, 5.0, "semipermeable\nmembrane", ha="center", fontsize=8.5, color=AMBER)
        if not rev:
            ax.set_title("(a) Osmosis")
            arrow(ax, (3.6, 2.4), (6.4, 2.4), color=BLUE, lw=2)
            ax.text(3.0, 2.0, "solvent flows in", ha="center", fontsize=8.5, color=BLUE)
            arrow(ax, (7, 5.4), (7, lv_right + 0.05), color=RED, lw=2)
            ax.text(7, 5.6, "pressure needed to stop\nthe flow = osmotic pressure π", ha="center", fontsize=8.5, color=RED)
        else:
            ax.set_title("(b) Reverse osmosis")
            arrow(ax, (6.4, 2.4), (3.6, 2.4), color=BLUE, lw=2)
            ax.text(3.0, 2.0, "pure water out", ha="center", fontsize=8.5, color=BLUE)
            ax.add_patch(Rectangle((5.4, lv_right), 3.2, 0.35, color=GREY))
            arrow(ax, (7, 6.2), (7, lv_right + 0.4), color=RED, lw=2.4)
            ax.text(7, 6.4, "pressure > π", ha="center", fontsize=9, color=RED)
    save(fig, "chem_ch01_fig05_osmosis.png")


def fig06_acetone_chloroform():
    x = np.array([0, 11.8, 23.4, 36.0, 50.8, 58.2, 64.5, 72.1]) / 100
    pa = np.array([0, 54.9, 110.1, 202.4, 322.7, 405.9, 454.1, 521.1])
    pc = np.array([632.8, 548.1, 469.4, 359.7, 257.7, 193.6, 161.2, 120.7])
    xx = np.linspace(0, 1, 50)
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    ax.plot(xx, 741.8 * xx, color=BLUE, lw=1, ls="--")
    ax.plot(xx, 632.8 * (1 - xx), color=RED, lw=1, ls="--")
    ax.plot(xx, 632.8 + 109.0 * xx, color=INK, lw=1, ls="--", label="ideal (Raoult's law)")
    ax.plot(x, pa, "o-", color=BLUE, ms=4, label="p_acetone (observed)")
    ax.plot(x, pc, "s-", color=RED, ms=4, label="p_chloroform (observed)")
    ax.plot(x, pa + pc, "^-", color=INK, ms=4, lw=2, label="p_total (observed)")
    ax.set_xlabel("Mole fraction of acetone, x_acetone")
    ax.set_ylabel("Vapour pressure / mm Hg")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 800)
    ax.set_title("Acetone–chloroform at 328 K: negative deviation")
    ax.legend(frameon=False, fontsize=8, loc="center right")
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
    save(fig, "chem_ch01_fig06_acetone_chloroform.png")


if __name__ == "__main__":
    fig01_raoult_ideal()
    fig02_deviations()
    fig03_bp_elevation()
    fig04_fp_depression()
    fig05_osmosis()
    fig06_acetone_chloroform()
