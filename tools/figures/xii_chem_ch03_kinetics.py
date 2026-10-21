"""Figures for Class XII Chemistry Chapter 3, Chemical Kinetics.
Run: python xii_chem_ch03_kinetics.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Chemistry", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, RED, BLUE, AMBER, GREY, GREEN = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#2E7D32"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def arrow(ax, p0, p1, color=INK, lw=1.3, ms=10, style="<|-|>"):
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0))


def clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def fig01_rates():
    fig, ax = plt.subplots(figsize=(5.6, 3.9))
    t = np.linspace(0, 10, 200)
    R = np.exp(-0.25 * t)
    P = 1 - R
    ax.plot(t, R, color=BLUE, lw=2.2, label="[R] reactant")
    ax.plot(t, P, color=RED, lw=2.2, label="[P] product")
    t0 = 3.0
    r0 = np.exp(-0.25 * t0)
    slope = -0.25 * r0
    tt = np.linspace(0.8, 5.6, 10)
    ax.plot(tt, r0 + slope * (tt - t0), color=INK, ls="--", lw=1.2)
    ax.plot([t0], [r0], "o", color=INK)
    ax.text(t0 + 0.2, r0 + 0.05, "slope of tangent at t\n= instantaneous rate", fontsize=8.5)
    ax.set_xlabel("time")
    ax.set_ylabel("concentration")
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_title("Instantaneous rate from a concentration–time curve")
    ax.legend(frameon=False, fontsize=9, loc="center right")
    clean(ax)
    save(fig, "chem_ch03_fig01_rates.png")


def fig02_orders():
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.6))
    t = np.linspace(0, 10, 50)
    axs[0].plot(t, 1 - 0.08 * t, color=BLUE, lw=2.2)
    axs[0].set_title("Zero order: [R] against t")
    axs[0].set_xlabel("t")
    axs[0].set_ylabel("[R]")
    axs[0].text(5.2, 0.62, "slope = −k\nintercept = [R]₀", fontsize=9)
    axs[1].plot(t, -0.18 * t, color=RED, lw=2.2)
    axs[1].set_title("First order: ln[R] against t")
    axs[1].set_xlabel("t")
    axs[1].set_ylabel("ln[R]")
    axs[1].text(5.2, -0.6, "slope = −k\n(log[R]₀/[R] against t:\nslope = k/2.303)", fontsize=9)
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])
        clean(ax)
    save(fig, "chem_ch03_fig02_orders.png")


def fig03_energy():
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    x = np.linspace(0, 10, 400)
    base = 0.6 - 0.35 / (1 + np.exp(-(x - 5) * 1.5))
    uncat = base + 1.4 * np.exp(-((x - 5) / 1.2) ** 2)
    cat = base + 0.75 * np.exp(-((x - 5) / 1.2) ** 2)
    ax.plot(x, uncat, color=RED, lw=2.2, label="without catalyst")
    ax.plot(x, cat, color=GREEN, lw=2.2, ls="--", label="with catalyst")
    ax.axhline(0.6, xmin=0.02, xmax=0.42, color=GREY, lw=1)
    ax.axhline(0.25, xmin=0.58, xmax=0.98, color=GREY, lw=1)
    peak = uncat.max()
    arrow(ax, (2.6, 0.6), (2.6, peak), color=RED)
    ax.text(2.0, (0.6 + peak) / 2, "Ea", color=RED, fontsize=10, weight="bold")
    arrow(ax, (3.6, 0.6), (3.6, cat.max()), color=GREEN)
    ax.text(3.75, (0.6 + cat.max()) / 2 - 0.08, "Ea (cat.)", color=GREEN, fontsize=9)
    arrow(ax, (8.4, 0.25), (8.4, 0.6), color=BLUE)
    ax.text(8.55, 0.4, "ΔrH", color=BLUE, fontsize=9)
    ax.text(0.4, 0.68, "reactants", fontsize=9)
    ax.text(8.6, 0.12, "products", fontsize=9)
    ax.text(5.0, peak + 0.06, "activated complex", ha="center", fontsize=9)
    ax.set_xlabel("reaction coordinate")
    ax.set_ylabel("potential energy")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, peak + 0.25)
    ax.legend(frameon=False, fontsize=9, loc="upper right")
    ax.set_title("Activation energy and the effect of a catalyst")
    clean(ax)
    save(fig, "chem_ch03_fig03_energy.png")


def fig04_distribution():
    fig, ax = plt.subplots(figsize=(6.0, 3.9))
    E = np.linspace(0, 10, 400)

    def mb(E, T):
        return np.sqrt(E) * np.exp(-E / T) / T ** 1.5

    y1, y2 = mb(E, 1.4), mb(E, 2.0)
    ax.plot(E, y1, color=BLUE, lw=2.2, label="T")
    ax.plot(E, y2, color=RED, lw=2.2, label="T + 10 K")
    Ea = 5.0
    m = E >= Ea
    ax.fill_between(E[m], 0, y2[m], color=RED, alpha=0.25)
    ax.fill_between(E[m], 0, y1[m], color=BLUE, alpha=0.35)
    ax.axvline(Ea, color=INK, ls="--", lw=1)
    ax.text(Ea + 0.1, max(y1) * 0.9, "Ea", fontsize=10)
    ax.text(6.0, max(y1) * 0.35, "shaded: molecules with E ≥ Ea\n(about doubles for a 10 K rise)", fontsize=8.5)
    ax.set_xlabel("kinetic energy")
    ax.set_ylabel("fraction of molecules")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend(frameon=False, fontsize=9)
    ax.set_title("Distribution of molecular energies")
    clean(ax)
    save(fig, "chem_ch03_fig04_distribution.png")


def fig05_n2o5():
    t = np.array([0, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200.])
    c = np.array([1.63, 1.36, 1.14, 0.93, 0.78, 0.64, 0.53, 0.43, 0.35])
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.6))
    axs[0].plot(t, c, "o-", color=BLUE)
    axs[0].axhline(1.63 / 2, color=GREY, ls="--", lw=1)
    axs[0].axvline(1440, color=GREY, ls="--", lw=1)
    axs[0].text(1500, 1.4, "t½ ≈ 1440 s", fontsize=9)
    axs[0].set_xlabel("t / s")
    axs[0].set_ylabel("10² [N₂O₅] / mol L⁻¹")
    axs[0].set_title("(i) [N₂O₅] against t")
    lg = np.log10(c * 1e-2)
    b, a = np.polyfit(t, lg, 1)
    axs[1].plot(t, lg, "o", color=RED)
    axs[1].plot(t, a + b * t, color=RED, lw=1.2)
    axs[1].text(1300, -1.9, f"straight line: first order\nslope = {b:.2e} s⁻¹ = −k/2.303", fontsize=8.5)
    axs[1].set_xlabel("t / s")
    axs[1].set_ylabel("log [N₂O₅]")
    axs[1].set_title("(iii) log[N₂O₅] against t")
    for ax in axs:
        clean(ax)
    save(fig, "chem_ch03_fig05_n2o5.png")


def fig06_arrhenius():
    T = np.array([0, 20, 40, 60, 80]) + 273.15
    k = np.array([0.0787, 1.70, 25.7, 178, 2140]) * 1e-5
    x = 1e3 / T
    y = np.log(k)
    b, a = np.polyfit(1 / T, y, 1)
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    ax.plot(x, y, "o", color=BLUE)
    xx = np.linspace(2.8, 3.7, 20)
    ax.plot(xx, a + b * xx / 1e3, color=BLUE, lw=1.2)
    ax.set_xlabel("10³/T / K⁻¹")
    ax.set_ylabel("ln k")
    ax.set_title("ln k against 1/T for N₂O₅ (Exercise 3.22)")
    ax.text(2.85, -14.5, f"slope = −Ea/R = {b:.3g} K\nEa ≈ {(-b * 8.314) / 1000:.0f} kJ mol⁻¹", fontsize=9)
    clean(ax)
    save(fig, "chem_ch03_fig06_arrhenius.png")


if __name__ == "__main__":
    fig01_rates()
    fig02_orders()
    fig03_energy()
    fig04_distribution()
    fig05_n2o5()
    fig06_arrhenius()
