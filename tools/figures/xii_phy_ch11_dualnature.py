"""Figures for Class XII Physics Chapter 11, Dual Nature of Radiation and Matter.
Run: python xii_phy_ch11_dualnature.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

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


def line(ax, pts, color=INK, lw=1.3, ls="-"):
    xs, ys = zip(*[tuple(p) for p in pts])
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_capstyle="round")


def graph_axes(ax, xlabel, ylabel):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.set_xticks([])
    ax.set_yticks([])
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ax.text(x1, -0.03 * (y1 - y0), xlabel, ha="right", va="top", fontsize=9)
    ax.text(0.02 * (x1 - x0), y1, ylabel, ha="left", va="top", fontsize=9)


def iv_curve(v, v0, isat, k=1.6):
    """A smooth photocurrent curve: zero at -v0, saturating at isat."""
    x = np.clip((v + v0) * k, 0, None)
    return isat * np.tanh(x)


# ---- Fig 11.1: the photoelectric apparatus -----------------------------------------------------
def fig_apparatus():
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(-3.2, 3.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((1.4, -0.3), 5.2, 2.4, boxstyle="round,pad=0.1,rounding_size=1.0", fc=SOFT, ec=NEG, lw=1.5))
    ax.text(4.0, 2.35, "evacuated glass / quartz tube", fontsize=8.5, ha="center", color=NEG)
    ax.add_patch(Rectangle((1.9, 0.0), 0.18, 1.8, color=POS))
    ax.add_patch(Rectangle((5.9, 0.0), 0.18, 1.8, color=NEG))
    ax.text(1.65, 0.85, "C", fontsize=11, ha="center", color=POS)
    ax.text(6.35, 0.85, "A", fontsize=11, ha="center", color=NEG)
    ax.text(1.85, -0.55, "emitter", fontsize=8.5, ha="right")
    ax.text(6.15, -0.55, "collector", fontsize=8.5, ha="left")
    # light from the source through the window W
    ax.plot([3.4], [2.95], "o", color=ACC, ms=10)
    ax.text(3.7, 2.95, "S (source)", fontsize=8.5, va="center")
    for dx in (-0.25, 0.0, 0.25):
        arrow(ax, (3.4 + dx, 2.75), (2.15, 1.3 + dx), ACC, lw=1.2, ms=9)
    ax.text(2.6, 1.95, "W", fontsize=9, color=ACC)
    # photoelectrons
    for y in (0.4, 0.9, 1.4):
        arrow(ax, (2.3, y), (5.7, y), INK, lw=0.9, ms=8)
    ax.text(4.0, 1.55, "photoelectrons", fontsize=8.5, ha="center")
    # external circuit: microammeter in series with the tube, voltmeter across the battery
    line(ax, [(1.98, 0.0), (1.98, -1.6), (3.6, -1.6)])
    for x, h in ((3.6, 0.5), (3.8, 0.28), (4.0, 0.5), (4.2, 0.28)):
        line(ax, [(x, -1.6 - h / 2), (x, -1.6 + h / 2)], INK, lw=2)
    line(ax, [(4.2, -1.6), (4.85, -1.6)])
    ax.add_patch(plt.Circle((5.2, -1.6), 0.35, fill=False, ec=INK, lw=1.3))
    ax.text(5.2, -1.6, "μA", fontsize=8.5, ha="center", va="center")
    line(ax, [(5.55, -1.6), (6.0, -1.6), (6.0, 0.0)])
    line(ax, [(3.0, -1.6), (3.0, -2.6), (3.58, -2.6)])
    line(ax, [(4.22, -2.6), (4.6, -2.6), (4.6, -1.6)])
    ax.add_patch(plt.Circle((3.9, -2.6), 0.32, fc="white", ec=INK, lw=1.3))
    ax.text(3.9, -2.6, "V", fontsize=9, ha="center", va="center")
    ax.text(3.9, -1.05, "battery and commutator", fontsize=8.5, ha="center")
    fig.tight_layout()
    save(fig, "phy_ch11_fig01_apparatus.png")


# ---- Fig 11.2: photocurrent and intensity / collector potential --------------------------------
def fig_intensity():
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 3.4), gridspec_kw={"width_ratios": [1, 1.5]})
    ax = axes[0]
    x = np.linspace(0, 1, 10)
    ax.plot(x, 0.9 * x, color=POS, lw=2)
    ax.set_xlim(-0.05, 1.1)
    ax.set_ylim(-0.05, 1.0)
    graph_axes(ax, "intensity of light", "photoelectric current")
    ax.set_title("(a) Current ∝ intensity\n(fixed frequency and potential)", fontsize=10)
    ax = axes[1]
    v = np.linspace(-2.5, 4, 400)
    v0 = 1.5
    for isat, col, lab in ((0.5, GREEN, "$I_1$"), (0.8, NEG, "$I_2$"), (1.1, POS, "$I_3$")):
        ax.plot(v, iv_curve(v, v0, isat), color=col, lw=2)
        ax.text(4.05, isat, lab, color=col, fontsize=10, va="center")
    ax.plot([-v0], [0], "o", color=INK, ms=4)
    ax.text(-v0, -0.12, "$-V_0$", fontsize=10, ha="center", va="top")
    ax.text(-2.4, 0.95, "retarding\npotential", fontsize=8.5, color=GREY)
    ax.text(1.0, 1.25, "saturation currents", fontsize=8.5, color=GREY)
    ax.set_xlim(-2.6, 4.6)
    ax.set_ylim(-0.25, 1.4)
    graph_axes(ax, "collector plate potential V", "photocurrent")
    ax.set_title("(b) Same frequency, intensities $I_3 > I_2 > I_1$:\nsame stopping potential", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch11_fig02_intensity.png")


# ---- Fig 11.3: photocurrent for different frequencies; V0 against frequency -------------------
def fig_frequency():
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 3.4))
    ax = axes[0]
    v = np.linspace(-3.2, 3.5, 400)
    for v0, col, lab in ((1.0, GREEN, "$\\nu_1$"), (1.8, NEG, "$\\nu_2$"), (2.6, POS, "$\\nu_3$")):
        ax.plot(v, iv_curve(v, v0, 1.0), color=col, lw=2)
        ax.plot([-v0], [0], "o", color=col, ms=4)
        ax.text(-v0, -0.1, "$-V_{0%s}$" % lab[-2], fontsize=9, ha="center", va="top", color=col)
    ax.text(0.6, 1.1, "same saturation current", fontsize=8.5, color=GREY)
    ax.set_xlim(-3.4, 3.8)
    ax.set_ylim(-0.3, 1.3)
    graph_axes(ax, "collector plate potential V", "photocurrent")
    ax.set_title("(a) Same intensity, $\\nu_3 > \\nu_2 > \\nu_1$:\nhigher frequency, larger $V_0$", fontsize=10)
    ax = axes[1]
    nu = np.linspace(0, 12, 50)
    for nu0, col, lab in ((4.0, POS, "metal 1"), (6.5, NEG, "metal 2")):
        y = 0.414 * (nu - nu0)
        m = nu >= nu0
        ax.plot(nu[m], y[m], color=col, lw=2)
        ax.plot(nu[~m], y[~m], color=col, lw=1, ls=":")
        ax.text(nu0, -0.35, f"$\\nu_0$", fontsize=9, ha="center", color=col)
        ax.text(11.2, 0.414 * (11.2 - nu0) + 0.15, lab, fontsize=8.5, color=col, ha="right")
    ax.text(1.0, -1.5, "intercepts on the V₀ axis: −φ₀/e", fontsize=8.5, color=GREY)
    ax.text(0.8, 2.6, "slope = h/e (the same for all metals)", fontsize=8.5, color=INK)
    ax.set_xlim(-0.3, 12.5)
    ax.set_ylim(-2.0, 3.6)
    graph_axes(ax, "frequency ν", "stopping potential $V_0$")
    ax.set_title("(b) $V_0$ against ν: straight lines of equal slope,\nzero at the threshold frequency $\\nu_0$", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch11_fig03_frequency.png")


# ---- Fig 11.4: board graphs, HSSLC 2024 Q18 and HSSLC 2026 Q30 ---------------------------------
def fig_board():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.4))
    ax = axes[0]
    for nu0, col, lab in ((5, POS, "A"), (10, NEG, "B")):
        nu = np.linspace(nu0, nu0 + 8, 10)
        ax.plot(nu, 0.5 * (nu - nu0), color=col, lw=2)
        ax.text(nu0 + 8.2, 4.0, lab, fontsize=11, color=col)
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 6.5)
    ax.set_xticks([5, 10, 15, 20])
    ax.set_yticks([0, 1, 2, 3, 4, 5, 6])
    ax.set_xlabel("ν (10¹⁴ Hz)", fontsize=9)
    ax.set_ylabel("$V_0$ (volt)", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("(a) HSSLC 2024, Q18", fontsize=10)
    ax = axes[1]
    v = np.linspace(-3.0, 3.0, 400)
    ax.plot(v, iv_curve(v, 2.2, 1.0, k=0.9), color=POS, lw=2)
    ax.plot(v, iv_curve(v, 1.1, 1.0, k=1.4), color=NEG, lw=2)
    ax.text(-2.6, 0.35, "Metal A", fontsize=9, color=POS)
    ax.text(0.25, 0.45, "Metal B", fontsize=9, color=NEG)
    ax.text(-2.2, -0.1, "$-V_2$", fontsize=9, ha="center", va="top")
    ax.text(-1.1, -0.1, "$-V_1$", fontsize=9, ha="center", va="top")
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-0.25, 1.2)
    graph_axes(ax, "V", "I")
    ax.set_title("(b) HSSLC 2026, Q30", fontsize=10)
    fig.tight_layout()
    save(fig, "phy_ch11_fig04_board.png")


if __name__ == "__main__":
    fig_apparatus()
    fig_intensity()
    fig_frequency()
    fig_board()
