"""Figures for Class XII Chemistry Chapter 2, Electrochemistry.
Run: python xii_chem_ch02_electrochemistry.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle, Polygon, Circle, FancyBboxPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Chemistry", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, RED, BLUE, AMBER, GREY, GREEN = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#2E7D32"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.titleweight": "bold", "axes.titlesize": 11})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def arrow(ax, p0, p1, color=INK, lw=1.4, ms=11, style="-|>"):
    ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0))


def beaker(ax, x, y, w, h, fill, label):
    ax.add_patch(Rectangle((x, y), w, h * 0.72, color=fill, zorder=1))
    ax.plot([x, x, x + w, x + w], [y + h, y, y, y + h], color=INK, lw=1.8, zorder=3)
    ax.text(x + w / 2, y + 0.25, label, ha="center", fontsize=8.5, zorder=4)


def fig01_daniell():
    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    beaker(ax, 0.8, 0.6, 3.6, 4.0, "#DCE6F2", "ZnSO₄(aq)")
    beaker(ax, 7.6, 0.6, 3.6, 4.0, "#D3E7F7", "CuSO₄(aq)")
    ax.add_patch(Rectangle((2.3, 1.3), 0.6, 4.4, color="#9AA5B1", zorder=2))
    ax.add_patch(Rectangle((9.1, 1.3), 0.6, 4.4, color="#C77B4A", zorder=2))
    ax.text(2.6, 6.0, "Zn rod\nanode (−)", ha="center", fontsize=9)
    ax.text(9.4, 6.0, "Cu rod\ncathode (+)", ha="center", fontsize=9)
    # salt bridge
    ax.plot([3.6, 3.6, 8.4, 8.4], [2.0, 4.9, 4.9, 2.0], color=AMBER, lw=9, solid_capstyle="butt", zorder=2)
    ax.text(6.0, 5.2, "salt bridge (KCl or KNO₃ in agar)", ha="center", fontsize=8.5, color=AMBER)
    # wire and voltmeter
    ax.plot([2.6, 2.6, 5.4], [5.7, 7.2, 7.2], color=INK, lw=1.4)
    ax.plot([6.6, 9.4, 9.4], [7.2, 7.2, 5.7], color=INK, lw=1.4)
    ax.add_patch(Circle((6.0, 7.2), 0.55, fill=False, lw=1.6, ec=INK))
    ax.text(6.0, 7.2, "V", ha="center", va="center", fontsize=11, weight="bold")
    arrow(ax, (3.6, 7.5), (5.0, 7.5), color=BLUE)
    ax.text(4.3, 7.75, "e⁻ flow", ha="center", fontsize=8.5, color=BLUE)
    ax.text(2.6, 3.4, "Zn → Zn²⁺ + 2e⁻", ha="center", fontsize=8.5, color=RED, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(9.4, 3.4, "Cu²⁺ + 2e⁻ → Cu", ha="center", fontsize=8.5, color=GREEN, bbox=dict(fc="white", ec="none", pad=1))
    ax.set_title("Daniell cell: Zn(s)|Zn²⁺(aq)||Cu²⁺(aq)|Cu(s),  E°cell = 1.10 V")
    save(fig, "chem_ch02_fig01_daniell.png")


def fig02_she():
    fig, ax = plt.subplots(figsize=(4.4, 4.8))
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 8)
    ax.axis("off")
    beaker(ax, 0.8, 0.5, 4.4, 4.0, "#E3ECF5", "H⁺(aq), a = 1 (1 M)")
    ax.add_patch(Rectangle((2.6, 1.4), 0.8, 5.6, fill=False, lw=1.6, ec=INK))
    ax.add_patch(Rectangle((2.75, 1.7), 0.5, 0.8, color="#6B6B6B"))
    ax.text(3.6, 2.1, "Pt foil coated\nwith Pt black", fontsize=8, va="center")
    for yy in (2.9, 3.4, 3.9):
        ax.add_patch(Circle((2.85 + 0.15 * (yy % 1), yy), 0.08, fill=False, ec=BLUE))
    arrow(ax, (1.2, 6.4), (2.55, 6.4), color=BLUE)
    ax.text(0.2, 6.7, "H₂ gas, 1 bar", fontsize=9, color=BLUE)
    ax.text(3.0, 7.3, "Pt wire", ha="center", fontsize=8.5)
    ax.set_title("Standard hydrogen electrode\nPt(s)|H₂(g, 1 bar)|H⁺(aq, 1 M);  E° = 0.00 V", fontsize=10)
    save(fig, "chem_ch02_fig02_she.png")


def fig03_molar_conductivity():
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    c = np.linspace(0.0, 0.35, 100)
    ax.plot(c, 150 - 95 * c, color=BLUE, lw=2.2, label="KCl (strong electrolyte)")
    ax.plot([0, 0.05], [150, 150 - 95 * 0.05], color=BLUE, lw=1, ls="--")
    cw = np.linspace(0.006, 0.35, 120)
    ax.plot(cw, 390 / (1 + 260 * cw ** 1.5) * 0.12 + 8, color=RED, lw=2.2, label="CH₃COOH (weak electrolyte)")
    ax.text(0.01, 156, "Λ°m(KCl): extrapolate to c½ = 0", fontsize=8.5, color=BLUE)
    ax.text(0.09, 60, "weak electrolyte rises steeply on dilution;\ncannot be extrapolated to c½ = 0", fontsize=8.5, color=RED)
    ax.set_xlabel("c½ / (mol L⁻¹)½")
    ax.set_ylabel("Λm / S cm² mol⁻¹")
    ax.set_xlim(0, 0.35)
    ax.set_ylim(0, 175)
    ax.set_title("Molar conductivity against √c")
    ax.legend(frameon=False, fontsize=8.5, loc="upper right")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "chem_ch02_fig03_molar_conductivity.png")


def fig04_nacl_plot():
    c = np.array([0.001, 0.010, 0.020, 0.050, 0.100])
    kappa = np.array([1.237, 11.85, 23.15, 55.53, 106.74]) * 1e-2 * 1e-2  # S m^-1 -> S cm^-1
    lam = 1000 * kappa / c
    x = np.sqrt(c)
    b, a = np.polyfit(x, lam, 1)
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    ax.plot(x, lam, "o", color=BLUE, ms=6, label="data (Exercise 2.10)")
    xx = np.linspace(0, 0.33, 50)
    ax.plot(xx, a + b * xx, color=RED, lw=1.6, ls="--", label=f"best line; intercept Λ°m ≈ {a:.0f}")
    for xi, li in zip(x, lam):
        ax.annotate(f"{li:.1f}", (xi, li), textcoords="offset points", xytext=(4, 5), fontsize=8)
    ax.set_xlabel("c½ / (mol L⁻¹)½")
    ax.set_ylabel("Λm / S cm² mol⁻¹")
    ax.set_xlim(0, 0.34)
    ax.set_ylim(100, 130)
    ax.set_title("NaCl at 298 K")
    ax.legend(frameon=False, fontsize=8.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "chem_ch02_fig04_nacl_plot.png")
    print("intercept", a, "slope", b, "lam", lam)


def fig05_rusting():
    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.add_patch(Rectangle((0.5, 0.5), 11, 1.6, color="#9AA5B1"))
    ax.text(6, 1.0, "iron (metal conducts electrons)", ha="center", fontsize=9, color="white", weight="bold")
    drop = Polygon([[2.0, 2.1], [10.0, 2.1], [9.0, 3.6], [3.0, 3.6]], closed=True, color="#D6E6F5")
    ax.add_patch(drop)
    ax.text(6, 3.25, "water drop with dissolved O₂ and CO₂ (H⁺)", ha="center", fontsize=8.5, color=BLUE)
    ax.text(4.0, 2.45, "anode spot", ha="center", fontsize=8.5, color=RED, weight="bold")
    ax.text(8.6, 2.45, "cathode spot", ha="center", fontsize=8.5, color=GREEN, weight="bold")
    arrow(ax, (4.5, 1.6), (8.0, 1.6), color="white", lw=1.8)
    ax.text(6.2, 1.75, "e⁻", fontsize=9, color="white")
    ax.text(2.6, 4.5, "Fe(s) → Fe²⁺(aq) + 2e⁻\nE° = −0.44 V", ha="center", fontsize=8.5, color=RED)
    ax.text(9.4, 4.5, "O₂ + 4H⁺ + 4e⁻ → 2H₂O\nE° = +1.23 V", ha="center", fontsize=8.5, color=GREEN)
    ax.text(6.0, 5.4, "Fe²⁺ is oxidised further by air → Fe₂O₃·xH₂O (rust)", ha="center", fontsize=9)
    ax.set_title("Rusting of iron as an electrochemical cell (E°cell = 1.67 V)")
    save(fig, "chem_ch02_fig05_rusting.png")


if __name__ == "__main__":
    fig01_daniell()
    fig02_she()
    fig03_molar_conductivity()
    fig04_nacl_plot()
    fig05_rusting()
