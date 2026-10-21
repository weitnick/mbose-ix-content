"""Figures for Class XII Physics Chapter 7, Alternating Current.
Run: python xii_phy_ch07_ac.py   (writes PNGs into Class XII Content/Physics/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Physics", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, POS, NEG, ACC, GREY, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#E9F0F7"
GREEN = "#2E7D32"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})
PI_TICKS = ([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi, 5 * np.pi / 2], ["0", "π/2", "π", "3π/2", "2π", "5π/2"])


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


def wave_axes(ax, title):
    ax.axhline(0, color=GREY, lw=0.8)
    ax.set_xticks(PI_TICKS[0])
    ax.set_xticklabels(PI_TICKS[1], fontsize=8.5)
    ax.set_yticks([])
    ax.set_xlabel("ωt", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(title, fontsize=10)


def phasor(ax, angles_labels, title, r=1.0):
    blank(ax, (-1.5, 1.5), (-1.4, 1.5))
    ax.add_patch(Circle((0, 0), r, fill=False, ec=GREY, lw=0.8, ls=":"))
    wire(ax, [(-1.3, 0), (1.3, 0)], color=GREY, lw=0.8)
    wire(ax, [(0, -1.25), (0, 1.3)], color=GREY, lw=0.8)
    for ang, lab, col, rr in angles_labels:
        t = np.radians(ang)
        arrow(ax, (0, 0), (rr * np.cos(t), rr * np.sin(t)), col, lw=2)
        ax.text(1.12 * rr * np.cos(t), 1.12 * rr * np.sin(t), lab, color=col, fontsize=10, ha="center", va="center")
    ax.annotate("", (-0.14, -0.79), (-0.57, -0.57), arrowprops=dict(arrowstyle="->", color=GREY, lw=1, connectionstyle="arc3,rad=0.3"))
    ax.text(-0.85, -0.95, "ω", color=GREY, fontsize=10)
    ax.set_title(title, fontsize=10)


# ---- Fig 7.1: a resistor ------------------------------------------------------------------------
def fig_resistor():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 2.9), gridspec_kw={"width_ratios": [1.6, 1]})
    ax = axes[0]
    t = np.linspace(0, 2.5 * np.pi, 300)
    ax.plot(t, np.sin(t), color=NEG, lw=2, label="v")
    ax.plot(t, 0.6 * np.sin(t), color=POS, lw=2, label="i")
    ax.legend(fontsize=8.5, frameon=False, loc="upper right")
    wave_axes(ax, "(a) v and i in phase in a resistor")
    phasor(axes[1], [(50, r"$V$", NEG, 1.0), (50, r"$I$", POS, 0.6)], "(b) Phasors V and I together")
    fig.tight_layout()
    save(fig, "phy_ch07_fig01_resistor.png")


# ---- Fig 7.2: rms value ------------------------------------------------------------------------
def fig_rms():
    fig, ax = plt.subplots(figsize=(7.0, 2.9))
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot(t, np.sin(t), color=POS, lw=2, label=r"$i = i_m\sin\omega t$")
    ax.plot(t, np.sin(t) ** 2, color=NEG, lw=2, label=r"$i^2$")
    ax.plot([0, 2 * np.pi], [0.5, 0.5], color=NEG, ls="--", lw=1.2)
    ax.text(6.4, 0.5, r"$\langle i^2\rangle = i_m^2/2$", color=NEG, fontsize=9.5, va="center")
    ax.plot([0, 2 * np.pi], [1 / np.sqrt(2)] * 2, color=GREEN, ls=":", lw=1.4)
    ax.text(6.4, 0.78, r"$I = i_m/\sqrt{2}$", color=GREEN, fontsize=9.5, va="center")
    ax.legend(fontsize=8.5, frameon=False, loc="lower left")
    ax.set_xlim(0, 7.9)
    wave_axes(ax, "The mean of i over a cycle is zero, but the mean of i² is not")
    ax.set_xticks(PI_TICKS[0][:5])
    ax.set_xticklabels(PI_TICKS[1][:5])
    save(fig, "phy_ch07_fig02_rms.png")


# ---- Fig 7.3: an inductor ---------------------------------------------------------------------
def fig_inductor():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 2.9), gridspec_kw={"width_ratios": [1.6, 1]})
    ax = axes[0]
    t = np.linspace(0, 2.5 * np.pi, 300)
    ax.plot(t, np.sin(t), color=NEG, lw=2, label="v")
    ax.plot(t, 0.6 * np.sin(t - np.pi / 2), color=POS, lw=2, label="i")
    ax.legend(fontsize=8.5, frameon=False, loc="upper right")
    wave_axes(ax, "(a) In an inductor i lags v by π/2")
    phasor(axes[1], [(60, r"$V$", NEG, 1.0), (-30, r"$I$", POS, 0.6)], "(b) I is π/2 behind V")
    fig.tight_layout()
    save(fig, "phy_ch07_fig03_inductor.png")


# ---- Fig 7.4: a capacitor ---------------------------------------------------------------------
def fig_capacitor():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 2.9), gridspec_kw={"width_ratios": [1.6, 1]})
    ax = axes[0]
    t = np.linspace(0, 2.5 * np.pi, 300)
    ax.plot(t, np.sin(t), color=NEG, lw=2, label="v")
    ax.plot(t, 0.6 * np.sin(t + np.pi / 2), color=POS, lw=2, label="i")
    ax.legend(fontsize=8.5, frameon=False, loc="upper right")
    wave_axes(ax, "(a) In a capacitor i leads v by π/2")
    phasor(axes[1], [(30, r"$V$", NEG, 1.0), (120, r"$I$", POS, 0.6)], "(b) I is π/2 ahead of V")
    fig.tight_layout()
    save(fig, "phy_ch07_fig04_capacitor.png")


# ---- Fig 7.5: series LCR: circuit, phasors, impedance triangle ---------------------------------
def res(ax, p0, p1, label, L=0.9, amp=0.12, n=6):
    p0, p1 = np.array(p0, float), np.array(p1, float)
    d = p1 - p0
    length = np.hypot(*d)
    u = d / length
    nrm = np.array([-u[1], u[0]])
    a = p0 + u * (length - L) / 2
    b = a + u * L
    wire(ax, [p0, a])
    wire(ax, [b, p1])
    pts = [a + u * L * t + nrm * amp * (0 if i in (0, 2 * n) else (1 if i % 2 else -1)) for i, t in enumerate(np.linspace(0, 1, 2 * n + 1))]
    wire(ax, pts)
    ax.text(*((a + b) / 2 + nrm * 0.35), label, ha="center", va="center", fontsize=10)


def ind(ax, p0, p1, label, L=0.9, n=4):
    p0, p1 = np.array(p0, float), np.array(p1, float)
    u = (p1 - p0) / np.hypot(*(p1 - p0))
    a = p0 + u * (np.hypot(*(p1 - p0)) - L) / 2
    wire(ax, [p0, a])
    wire(ax, [a + u * L, p1])
    for k in range(n):
        c = a + u * (L / n) * (k + 0.5)
        ax.add_patch(Arc(c, L / n, 0.35, theta1=0, theta2=180, color=INK, lw=1.4))
    ax.text(*((a + a + u * L) / 2 + np.array([0, 0.4])), label, ha="center", fontsize=10)


def fig_lcr():
    fig, axes = plt.subplots(1, 3, figsize=(12.4, 3.6), gridspec_kw={"width_ratios": [1.2, 1, 1]})
    ax = axes[0]
    blank(ax, (-0.4, 4.6), (-1.6, 1.6))
    res(ax, (0, 1), (1.5, 1), "R")
    ind(ax, (1.5, 1), (3.0, 1), "L")
    wire(ax, [(3.0, 1), (3.6, 1)])
    ax.plot([3.6, 3.6], [0.75, 1.25], color=INK, lw=2.4)
    ax.plot([3.75, 3.75], [0.75, 1.25], color=INK, lw=2.4)
    ax.text(3.68, 1.45, "C", ha="center", fontsize=10)
    wire(ax, [(3.75, 1), (4.3, 1), (4.3, -1), (2.45, -1)])
    wire(ax, [(1.85, -1), (0, -1), (0, 1)])
    ax.add_patch(Circle((2.15, -1), 0.3, fill=False, ec=INK, lw=1.4))
    tt = np.linspace(-0.2, 0.2, 40)
    ax.plot(2.15 + tt, -1 + 0.12 * np.sin(tt * np.pi / 0.2), color=INK, lw=1.2)
    ax.text(2.15, -1.5, r"$v = v_m\sin\omega t$", ha="center", fontsize=9.5)
    ax.set_title("(a) A series LCR circuit", fontsize=10)
    ax = axes[1]
    blank(ax, (-0.4, 2.6), (-1.5, 2.1))
    I0 = np.array([0, 0])
    arrow(ax, I0, (2.0, 0), POS, lw=2)
    ax.text(2.1, -0.18, r"$V_R$ (along I)", color=POS, fontsize=9)
    arrow(ax, I0, (0, 1.9), NEG, lw=2)
    ax.text(0.08, 1.9, r"$V_L$", color=NEG, fontsize=10)
    arrow(ax, I0, (0, -0.9), GREEN, lw=2)
    ax.text(0.08, -0.95, r"$V_C$", color=GREEN, fontsize=10)
    arrow(ax, I0, (0, 1.0), ACC, lw=2.6)
    ax.text(-0.38, 0.6, r"$V_L-V_C$", color=ACC, fontsize=9, rotation=90, va="center")
    arrow(ax, I0, (2.0, 1.0), INK, lw=2.4)
    ax.text(1.05, 0.75, "V", fontsize=11, fontweight="bold")
    wire(ax, [(2.0, 0), (2.0, 1.0)], color=GREY, lw=1, ls="--")
    ax.add_patch(Arc((0, 0), 1.0, 1.0, theta1=0, theta2=np.degrees(np.arctan2(1, 2)), color=INK))
    ax.text(0.6, 0.1, "φ", fontsize=11)
    ax.set_title("(b) Phasors (here X_L > X_C)", fontsize=10)
    ax = axes[2]
    blank(ax, (-0.4, 2.8), (-0.6, 1.9))
    wire(ax, [(0, 0), (2.2, 0), (2.2, 1.2), (0, 0)], lw=2)
    ax.text(1.1, -0.3, "R", ha="center", fontsize=11)
    ax.text(2.35, 0.6, r"$X_L - X_C$", fontsize=10)
    ax.text(0.85, 0.85, "Z", fontsize=12, fontweight="bold")
    ax.add_patch(Arc((0, 0), 1.0, 1.0, theta1=0, theta2=np.degrees(np.arctan2(1.2, 2.2)), color=INK))
    ax.text(0.6, 0.1, "φ", fontsize=11)
    ax.text(1.2, 1.65, r"$Z=\sqrt{R^2+(X_L-X_C)^2}$", ha="center", fontsize=10)
    ax.set_title("(c) The impedance triangle", fontsize=10)
    save(fig, "phy_ch07_fig05_lcr.png")


# ---- Fig 7.6: resonance curves ----------------------------------------------------------------
def fig_resonance():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    L, C, vm = 1e-3, 1e-9, 100.0
    w = np.linspace(0.5e6, 1.5e6, 600)
    for R, col in ((100, NEG), (200, POS)):
        Z = np.sqrt(R**2 + (w * L - 1 / (w * C)) ** 2)
        ax.plot(w / 1e6, vm / Z, color=col, lw=2, label=f"R = {R} Ω")
    ax.axvline(1.0, color=GREY, ls=":", lw=1)
    ax.set_xlabel(r"angular frequency ω ($10^6$ rad s⁻¹)", fontsize=9)
    ax.set_ylabel(r"current amplitude $i_m$ (A)", fontsize=9)
    ax.text(1.02, 0.95, r"$\omega_0 = 1/\sqrt{LC}$", fontsize=9.5)
    ax.legend(fontsize=9, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Resonance: L = 1.00 mH, C = 1.00 nF, vm = 100 V", fontsize=10)
    save(fig, "phy_ch07_fig06_resonance.png")


# ---- Fig 7.7: the transformer -----------------------------------------------------------------
def fig_transformer():
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    blank(ax, (-1.6, 6.4), (-1.6, 2.2))
    ax.add_patch(Rectangle((0.5, -0.9), 4.0, 2.8, color="#9AA7B4"))
    ax.add_patch(Rectangle((1.1, -0.3), 2.8, 1.6, color="white"))
    for k in range(6):
        y = -0.1 + k * 0.24
        ax.add_patch(Rectangle((0.38, y), 0.84, 0.1, color=POS, zorder=3))
    for k in range(10):
        y = -0.2 + k * 0.15
        ax.add_patch(Rectangle((3.78, y), 0.84, 0.07, color=NEG, zorder=3))
    wire(ax, [(0.38, -0.05), (-0.6, -0.05)], color=POS)
    wire(ax, [(0.38, 1.15), (-0.6, 1.15)], color=POS)
    ax.text(-0.75, 0.55, r"$V_p$ (ac in)", ha="right", va="center", fontsize=9.5, color=POS)
    ax.text(0.8, -1.25, r"primary, $N_p$ turns", ha="center", fontsize=9, color=POS)
    wire(ax, [(4.62, -0.17), (5.5, -0.17)], color=NEG)
    wire(ax, [(4.62, 1.18), (5.5, 1.18)], color=NEG)
    ax.text(5.6, 0.55, r"$V_s$ (out)", va="center", fontsize=9.5, color=NEG)
    ax.text(4.2, -1.25, r"secondary, $N_s$ turns", ha="center", fontsize=9, color=NEG)
    ax.annotate("", (2.5, 1.62), (1.6, 1.62), arrowprops=dict(arrowstyle="->", color=ACC, lw=1.4))
    ax.annotate("", (3.4, -0.6), (3.4, 1.6), arrowprops=dict(arrowstyle="-", color=ACC, lw=0))
    ax.text(2.5, 2.0, "alternating flux in the laminated soft iron core", ha="center", fontsize=9, color=ACC)
    ax.text(2.5, -1.55, r"$\dfrac{V_s}{V_p}=\dfrac{N_s}{N_p}=\dfrac{I_p}{I_s}$", ha="center", fontsize=11, va="top")
    save(fig, "phy_ch07_fig07_transformer.png")


# ---- Fig 7.8: the graph of HSSLC 2026, Q10 ------------------------------------------------------
def fig_board():
    fig, ax = plt.subplots(figsize=(6.0, 2.8))
    t = np.linspace(0, 5 * np.pi / 2, 300)
    ax.plot(t, np.sin(t), color=NEG, lw=2, label="E")
    ax.plot(t, 0.6 * np.sin(t - np.pi / 2), color=POS, lw=2, label="I")
    ax.legend(fontsize=9, frameon=False, loc="upper right")
    wave_axes(ax, "HSSLC 2026, Q10: E reaches its peak a quarter-cycle before I")
    save(fig, "phy_ch07_fig08_board.png")


if __name__ == "__main__":
    fig_resistor()
    fig_rms()
    fig_inductor()
    fig_capacitor()
    fig_lcr()
    fig_resonance()
    fig_transformer()
    fig_board()
