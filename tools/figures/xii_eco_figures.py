"""Figures for Class XII Economics (Introductory Macroeconomics + Indian Economic Development).
Run: python xii_eco_figures.py [figure-name ...]   (no names = all)
Writes PNGs to Economics\\Generated Content\\figures."""
import os
import sys

from xii_acc_ch01_partnership import *
from matplotlib.patches import FancyArrowPatch

OUT = "D:/MBOSE APP/Class XII Content/Economics/Generated Content/figures"
os.makedirs(OUT, exist_ok=True)


def esave(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(path)


def axes(xlabel, ylabel, xmax, ymax, ymin=0.0, w=5.6, h=4.2, title=None):
    """Plain economics axes: origin O, arrow-headed X and Y axes, no ticks."""
    fig, a = plt.subplots(figsize=(w, h))
    a.set_xlim(-0.06 * xmax, xmax * 1.16)
    a.set_ylim(ymin - 0.06 * ymax if ymin < 0 else -0.2 * ymax, ymax * 1.16)
    for s in a.spines.values():
        s.set_visible(False)
    a.set_xticks([])
    a.set_yticks([])
    a.annotate("", xy=(xmax * 1.06, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", lw=1.1, color=INK))
    a.annotate("", xy=(0, ymax * 1.06), xytext=(0, ymin if ymin < 0 else 0),
               arrowprops=dict(arrowstyle="-|>", lw=1.1, color=INK))
    a.text(-0.03 * xmax, -0.04 * ymax, "O", ha="right", va="top", fontsize=9)
    a.text(xmax * 1.06, -0.13 * ymax, xlabel, ha="right", va="top", fontsize=9)
    a.text(0.02 * xmax, ymax * 1.07, ylabel, ha="left", va="bottom", fontsize=9)
    if title:
        a.set_title(title, fontsize=10, weight="bold")
    return fig, a


def dot(a, x, y, label, dx=0.0, dy=0.0, ha="left", va="bottom"):
    a.plot([x], [y], "o", color=INK, ms=3.5)
    a.text(x + dx, y + dy, label, ha=ha, va=va, fontsize=9)


def guide(a, x, y, xl=None, yl=None, ymin=0.0):
    a.plot([x, x], [ymin, y], ls="--", lw=0.8, color=GREY)
    a.plot([0, x], [y, y], ls="--", lw=0.8, color=GREY)
    if xl:
        a.text(x, -0.03 * a.get_ylim()[1], xl, ha="center", va="top", fontsize=9)
    if yl:
        a.text(-0.02 * a.get_xlim()[1], y, yl, ha="right", va="center", fontsize=9)


def ch02_circular():
    fig, a = canvas(9.6, 5.9, (0, 19.2), (-0.8, 11.0))
    a.text(9.6, 10.7, "Circular flow of income in a two-sector economy", ha="center", fontsize=10, weight="bold")
    box(a, (0.6, 3.9), 4.6, 2.4, "HOUSEHOLDS\n(owners of land, labour,\ncapital, enterprise)", fc=PALE_AMBER, ec=AMBER, fs=8.6, bold=True)
    box(a, (14.0, 3.9), 4.6, 2.4, "FIRMS\n(producers of goods\nand services)", fc=PALE_GREEN, ec=GREEN, fs=8.6, bold=True)
    # real flows (inner)
    a.add_patch(FancyArrowPatch((5.4, 5.8), (13.8, 5.8), connectionstyle="arc3,rad=-0.25", arrowstyle="-|>",
                                mutation_scale=11, color=BLUE, lw=1.4))
    a.text(9.6, 7.25, "factor services (real flow)", ha="center", fontsize=8.4, color=BLUE)
    a.add_patch(FancyArrowPatch((13.8, 4.4), (5.4, 4.4), connectionstyle="arc3,rad=-0.25", arrowstyle="-|>",
                                mutation_scale=11, color=BLUE, lw=1.4))
    a.text(9.6, 2.95, "goods and services (real flow)", ha="center", fontsize=8.4, color=BLUE)
    # money flows (outer)
    a.add_patch(FancyArrowPatch((16.3, 6.5), (2.9, 6.5), connectionstyle="arc3,rad=0.45", arrowstyle="-|>",
                                mutation_scale=11, color=RED, lw=1.4))
    a.text(9.6, 9.75, "factor payments: rent, wages, interest, profit (money flow)", ha="center", fontsize=8.4, color=RED)
    a.add_patch(FancyArrowPatch((2.9, 3.7), (16.3, 3.7), connectionstyle="arc3,rad=0.45", arrowstyle="-|>",
                                mutation_scale=11, color=RED, lw=1.4))
    a.text(9.6, 0.05, "consumption expenditure (money flow)", ha="center", va="top", fontsize=8.4, color=RED)
    esave(fig, "eco_ch02_fig01_circular_flow.png")


def ch04_consumption():
    fig, a = axes("Income (Y)", "Consumption (C)", 10, 10)
    a.plot([0, 10], [0, 10], color=GREY, lw=1.1)
    a.text(9.3, 9.75, "45° line (C = Y)", fontsize=8.5, ha="right", color=GREY)
    a.plot([0, 10], [2, 2 + 0.6 * 10], color=BLUE, lw=1.8)
    a.text(10.15, 8.0, "C = C̄ + cY", fontsize=9, color=BLUE, va="center", ha="left")
    dot(a, 5, 5, "B (break-even: C = Y, S = 0)", dx=0.2, dy=-0.55)
    guide(a, 5, 5, xl="Y₀")
    a.text(0.15, 2.0, "C̄", fontsize=9, va="bottom")
    a.annotate("", xy=(7.5, 7.5), xytext=(7.5, 6.5), arrowprops=dict(arrowstyle="<->", lw=0.9, color=GREEN))
    a.text(7.35, 7.0, "saving", fontsize=8, color=GREEN, ha="right")
    a.annotate("", xy=(1.8, 3.08), xytext=(1.8, 1.8), arrowprops=dict(arrowstyle="<->", lw=0.9, color=RED))
    a.text(1.95, 2.25, "dissaving", fontsize=8, color=RED)
    esave(fig, "eco_ch04_fig01_consumption.png")


def ch04_saving():
    fig, a = axes("Income (Y)", "Saving (S)", 10, 6, ymin=-2.6)
    a.plot([0, 10], [-2, -2 + 0.4 * 10], color=GREEN, lw=1.8)
    a.text(10, 2.1, "S = −C̄ + (1 − c)Y", fontsize=9, color=GREEN, ha="right", va="bottom")
    dot(a, 5, 0, "B (S = 0)", dx=0.15, dy=0.15)
    a.text(0.15, -2.0, "−C̄", fontsize=9, va="center")
    a.text(1.4, -0.75, "dissaving", fontsize=8, color=RED)
    a.text(7.6, 0.25, "positive saving", fontsize=8, color=GREEN)
    esave(fig, "eco_ch04_fig02_saving.png")


def ch04_adas():
    fig, a = axes("Income / output (Y)", "AD, AS", 10, 10)
    a.plot([0, 10], [0, 10], color=GREY, lw=1.2)
    a.text(9.6, 9.75, "AS (45° line)", fontsize=8.5, ha="right", color=GREY)
    a.plot([0, 10], [2.5, 2.5 + 0.5 * 10], color=BLUE, lw=1.8)
    a.text(10, 7.6, "AD = C̄ + Ī + cY", fontsize=9, color=BLUE, ha="right", va="bottom")
    dot(a, 5, 5, "E", dx=-0.25, dy=0.2, ha="right")
    guide(a, 5, 5, xl="Y* (equilibrium)")
    a.text(0.15, 2.5, "C̄ + Ī", fontsize=9, va="bottom")
    a.text(2.2, 6.4, "AD > AS:\noutput rises", fontsize=7.8, color=GREEN, ha="center")
    a.text(8.2, 4.6, "AD < AS:\noutput falls", fontsize=7.8, color=RED, ha="center")
    esave(fig, "eco_ch04_fig03_ad_as.png")


def ch04_si():
    fig, a = axes("Income (Y)", "Saving, Investment", 10, 6, ymin=-2.6)
    a.plot([0, 10], [-2, -2 + 0.4 * 10], color=GREEN, lw=1.8)
    a.text(10, 2.1, "S", fontsize=9, color=GREEN, ha="left", va="bottom")
    a.plot([0, 10], [1.2, 1.2], color=BLUE, lw=1.8)
    a.text(10, 1.25, "I", fontsize=9, color=BLUE, ha="left", va="bottom")
    dot(a, 8, 1.2, "E", dx=0.0, dy=0.25, ha="center")
    a.plot([8, 8], [0, 1.2], ls="--", lw=0.8, color=GREY)
    a.text(8, -0.25, "Y*", ha="center", va="top", fontsize=9)
    a.text(3.5, 1.45, "I > S: income rises", fontsize=7.8, color=GREEN)
    esave(fig, "eco_ch04_fig04_saving_investment.png")


def ch04_gaps():
    fig, axs = plt.subplots(1, 2, figsize=(10, 4.2))
    for a, (title, ad, lab) in zip(axs, [("Excess demand (inflationary gap)", 3.3, "AD₁"),
                                         ("Deficient demand (deflationary gap)", 1.7, "AD₁")]):
        a.set_xlim(-0.5, 10.6)
        a.set_ylim(-0.5, 10.6)
        for s in a.spines.values():
            s.set_visible(False)
        a.set_xticks([])
        a.set_yticks([])
        a.annotate("", xy=(10.4, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", lw=1.1))
        a.annotate("", xy=(0, 10.4), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", lw=1.1))
        a.text(10.4, -0.35, "Output (Y)", ha="right", va="top", fontsize=9)
        a.text(-0.35, 10.4, "AD, AS", ha="right", va="top", fontsize=9, rotation=90)
        a.plot([0, 10], [0, 10], color=GREY, lw=1.1)
        a.text(9.8, 9.9, "AS", fontsize=8.5, color=GREY, ha="right")
        a.plot([0, 10], [2.5, 7.5], color=BLUE, lw=1.6)
        a.text(10, 7.55, "AD (full employment)", fontsize=7.8, color=BLUE, ha="right", va="bottom")
        a.plot([0, 10], [ad, ad + 5], color=RED, lw=1.6)
        a.text(10, ad + 5.05, lab, fontsize=8.5, color=RED, ha="right", va="bottom")
        a.plot([5, 5], [0, 5], ls="--", color=GREY, lw=0.8)
        a.text(5, -0.35, "Y_F", fontsize=9, ha="center", va="top")
        a.plot([5], [5], "o", color=INK, ms=3.5)
        a.plot([5], [ad + 2.5], "o", color=INK, ms=3.5)
        a.annotate("", xy=(5.25, ad + 2.5), xytext=(5.25, 5), arrowprops=dict(arrowstyle="<->", lw=1.0, color=AMBER))
        a.text(5.45, (ad + 2.5 + 5) / 2, "gap", fontsize=8.5, color=AMBER, va="center")
        a.set_title(title, fontsize=9.5, weight="bold")
    esave(fig, "eco_ch04_fig05_gaps.png")


def ch06_exchange():
    fig, a = axes("Quantity of foreign exchange ($)", "Exchange rate (₹ per $)", 10, 10)
    a.plot([1, 9], [9, 1], color=BLUE, lw=1.8)
    a.text(9, 1.0, "D$", fontsize=9, color=BLUE, va="top")
    a.plot([1, 9], [1, 9], color=GREEN, lw=1.8)
    a.text(9, 9.0, "S$", fontsize=9, color=GREEN, va="bottom")
    dot(a, 5, 5, "E", dx=0.3, dy=0.0, va="center")
    guide(a, 5, 5, xl="Q*", yl="e*")
    esave(fig, "eco_ch06_fig01_exchange_rate.png")


def ch06_supply_rise():
    fig, a = axes("Quantity of foreign exchange ($)", "Exchange rate (₹ per $)", 10, 10)
    a.plot([1, 9], [9, 1], color=BLUE, lw=1.8)
    a.text(9, 1.0, "D$", fontsize=9, color=BLUE, va="top")
    a.plot([1, 9], [1, 9], color=GREEN, lw=1.8)
    a.text(9, 9.0, "S$", fontsize=9, color=GREEN, va="bottom")
    a.plot([3, 10], [1, 8], color=GREEN, lw=1.8, ls="--")
    a.text(10, 8.0, "S$₁", fontsize=9, color=GREEN, va="bottom")
    dot(a, 5, 5, "E", dx=0.3, va="center")
    dot(a, 6, 4, "E₁", dx=0.3, va="center")
    guide(a, 5, 5, xl="Q", yl="e")
    guide(a, 6, 4, xl="Q₁", yl="e₁")
    esave(fig, "eco_ch06_fig02_supply_increase.png")


def skill_ppc():
    import numpy as np
    fig, a = axes("Good X (cloth)", "Good Y (wheat)", 10, 10)
    x = np.linspace(0, 9, 200)
    y = 9 * np.sqrt(1 - (x / 9) ** 2)
    a.plot(x, y, color=BLUE, lw=1.8)
    a.text(7.6, 6.0, "PPC", fontsize=9, color=BLUE)
    for px, lab in [(0, "A"), (4, "B"), (6.5, "C"), (9, "D")]:
        py = 9 * np.sqrt(max(0.0, 1 - (px / 9) ** 2))
        dot(a, px, py, lab, dx=0.15, dy=0.15)
    dot(a, 3, 4, "U (unemployment / inefficiency)", dx=0.15, dy=-0.5)
    dot(a, 8, 8, "F (not attainable)", dx=-0.2, dy=0.2, ha="right")
    esave(fig, "eco_skill01_fig01_ppc.png")


def skill_dmu():
    fig, a = axes("Units consumed", "Marginal utility", 7, 11, ymin=-4)
    pts = [(1, 10), (2, 8), (3, 6), (4, 4), (5, 0), (6, -3)]
    a.plot([p[0] for p in pts], [p[1] for p in pts], color=BLUE, lw=1.8, marker="o", ms=4)
    for x, y in pts:
        a.text(x + 0.1, y + 0.3, str(y), fontsize=8)
    a.text(5.2, 0.6, "MU = 0 (TU maximum)", fontsize=8, color=RED)
    a.text(4.9, -2.0, "negative MU", fontsize=8, color=RED, ha="right")
    esave(fig, "eco_skill01_fig02_dmu.png")


def skill_pc_price():
    fig, a = axes("Quantity", "Price", 10, 10)
    a.plot([1, 9], [9, 1], color=BLUE, lw=1.8)
    a.text(9, 1, "D", fontsize=9, color=BLUE, va="top")
    a.plot([1, 9], [1, 9], color=GREEN, lw=1.8)
    a.text(9, 9, "S", fontsize=9, color=GREEN, va="bottom")
    dot(a, 5, 5, "E", dx=0.3, va="center")
    guide(a, 5, 5, xl="Q*", yl="P*")
    a.plot([1.8, 8.2], [7, 7], ls=":", color=RED, lw=1.0)
    a.text(8.3, 7, "excess supply", fontsize=8, color=RED, va="center")
    a.plot([1.8, 8.2], [3, 3], ls=":", color=AMBER, lw=1.0)
    a.text(8.3, 3, "excess demand", fontsize=8, color=AMBER, va="center")
    esave(fig, "eco_skill01_fig03_pc_price.png")


def skill_monopoly():
    import numpy as np
    fig, a = axes("Output", "Cost / revenue", 10, 10)
    q = np.linspace(0.3, 9.5, 200)
    a.plot(q, 9 - 0.8 * q, color=BLUE, lw=1.8)
    a.text(9.5, 9 - 0.8 * 9.5, "AR = D", fontsize=9, color=BLUE, va="bottom", ha="right")
    qm = np.linspace(0.3, 5.5, 100)
    a.plot(qm, 9 - 1.6 * qm, color=BLUE, lw=1.4, ls="--")
    a.text(5.5, 9 - 1.6 * 5.5, "MR", fontsize=9, color=BLUE, va="top")
    a.plot(q, 1.5 + 0.12 * (q - 3) ** 2, color=RED, lw=1.6)
    a.text(9.5, 1.5 + 0.12 * 6.5 ** 2, "MC", fontsize=9, color=RED, va="bottom", ha="right")
    a.plot(q, 3.3 + 0.08 * (q - 4.5) ** 2, color=GREEN, lw=1.6)
    a.text(0.4, 3.3 + 0.08 * 4.2 ** 2, "AC", fontsize=9, color=GREEN, va="bottom")
    lo, hi = 3.0, 9.0  # solve MR = MC on the rising part of MC by bisection
    for _ in range(60):
        mid = (lo + hi) / 2
        if (9 - 1.6 * mid) - (1.5 + 0.12 * (mid - 3) ** 2) > 0:
            lo = mid
        else:
            hi = mid
    qe = (lo + hi) / 2
    mr = 9 - 1.6 * qe
    p = 9 - 0.8 * qe
    dot(a, qe, mr, "E (MR = MC)", dx=0.15, dy=-0.55)
    a.plot([qe, qe], [0, p], ls="--", color=GREY, lw=0.8)
    a.plot([0, qe], [p, p], ls="--", color=GREY, lw=0.8)
    dot(a, qe, p, "P", dx=0.15, dy=0.1)
    a.text(qe, -0.3, "OQ", ha="center", va="top", fontsize=9)
    a.text(-0.15, p, "OP", ha="right", va="center", fontsize=9)
    esave(fig, "eco_skill01_fig04_monopoly.png")


def skill_point_elasticity():
    fig, a = axes("Quantity demanded", "Price", 10, 10)
    a.plot([0, 9], [9, 0], color=BLUE, lw=1.8)
    dot(a, 0, 9, "A (e = infinity)", dx=0.3, va="center")
    dot(a, 2.25, 6.75, "e > 1", dx=0.3, va="center")
    dot(a, 4.5, 4.5, "M — mid-point (e = 1)", dx=0.3, va="center")
    dot(a, 6.75, 2.25, "e < 1", dx=0.3, va="center")
    dot(a, 9, 0, "B (e = 0)", dx=-0.2, dy=0.35, ha="right")
    a.text(6.6, 7.4, "e at a point =\nlower segment ÷ upper segment", fontsize=8.5, ha="center")
    esave(fig, "eco_skill01_fig05_point_elasticity.png")


def skill_supply_changes():
    fig, axs = plt.subplots(1, 2, figsize=(10, 4.2))
    for a, title in zip(axs, ["Extension and contraction (movement along S)",
                              "Increase and decrease (shift of S)"]):
        a.set_xlim(-0.5, 10.6)
        a.set_ylim(-0.8, 10.6)
        for s in a.spines.values():
            s.set_visible(False)
        a.set_xticks([])
        a.set_yticks([])
        a.annotate("", xy=(10.4, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", lw=1.1))
        a.annotate("", xy=(0, 10.4), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", lw=1.1))
        a.text(10.4, -0.4, "Quantity supplied", ha="right", va="top", fontsize=8.5)
        a.text(0.2, 10.4, "Price", ha="left", va="top", fontsize=8.5)
        a.set_title(title, fontsize=9.5, weight="bold")
    a = axs[0]
    a.plot([1, 9], [1, 9], color=GREEN, lw=1.8)
    a.text(9, 9, "S", fontsize=9, color=GREEN)
    for x, lab in [(3, "B (contraction)"), (5, "A"), (7, "C (extension)")]:
        a.plot([x], [x], "o", color=INK, ms=3.5)
        a.text(x + 0.25, x - 0.4, lab, fontsize=8)
    a = axs[1]
    a.plot([1, 8], [1, 8], color=GREEN, lw=1.8)
    a.text(8, 8, "S", fontsize=9, color=GREEN)
    a.plot([3, 10], [1, 8], color=GREEN, lw=1.6, ls="--")
    a.text(10.3, 7.6, "S₁ (increase)", fontsize=8.5, color=GREEN, ha="right", va="top")
    a.plot([0.2, 6], [2.2, 8], color=RED, lw=1.6, ls="--")
    a.text(5.8, 8.1, "S₂ (decrease)", fontsize=8.5, color=RED, ha="right", va="bottom")
    a.plot([0, 9], [5, 5], ls=":", color=GREY, lw=0.8)
    a.text(0.1, 5.15, "same price", fontsize=8, color=GREY)
    esave(fig, "eco_skill01_fig06_supply_changes.png")


FIGS = {"ch02_circular": ch02_circular, "ch04_consumption": ch04_consumption, "ch04_saving": ch04_saving,
        "ch04_adas": ch04_adas, "ch04_si": ch04_si, "ch04_gaps": ch04_gaps, "ch06_exchange": ch06_exchange,
        "ch06_supply_rise": ch06_supply_rise, "skill_ppc": skill_ppc, "skill_dmu": skill_dmu,
        "skill_pc_price": skill_pc_price, "skill_monopoly": skill_monopoly,
        "skill_point_elasticity": skill_point_elasticity, "skill_supply_changes": skill_supply_changes}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        FIGS[n]()
