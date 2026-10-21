"""Figures for Class XII Accountancy Chapter 1, Accounting for Partnership: Basic Concepts.
Run: python xii_acc_ch01_partnership.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "Accountancy", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, RED, BLUE, AMBER, GREY, GREEN, SOFT = "#1D2733", "#B03A2E", "#1F4E79", "#B7791F", "#7A8794", "#2E7D32", "#E9F0F7"
PALE_GREEN, PALE_AMBER, PALE_RED = "#E3F1E4", "#FBF0DC", "#F6E1DE"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})


def canvas(w, h, xl, yl):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xl)
    ax.set_ylim(*yl)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def box(ax, xy, w, h, text, fc=SOFT, ec=BLUE, fs=8.5, bold=False):
    ax.add_patch(FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.05,rounding_size=0.15", fc=fc, ec=ec, lw=1.2))
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center", fontsize=fs,
            weight="bold" if bold else "normal", color=INK)


def arrow(ax, p0, p1, color=INK, text=None, fs=8, dy=0.15):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=10, color=color, lw=1.2,
                                 shrinkA=3, shrinkB=3))
    if text:
        ax.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + dy, text, ha="center", va="bottom", fontsize=fs,
                color=color)


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def fig01_profit_flow():
    fig, a = canvas(9.6, 4.4, (0, 19.2), (0, 8.8))
    a.text(9.6, 8.4, "How the profit of a partnership firm reaches the partners", ha="center", fontsize=10,
           weight="bold")
    box(a, (0.3, 3.4), 4.2, 2.4, "Profit and Loss\nAccount\n(net profit; interest on\npartner's loan is a charge)",
        fc=PALE_AMBER, ec=AMBER)
    box(a, (6.6, 3.0), 5.6, 3.2, "Profit and Loss\nAppropriation Account\n\nCr: net profit, interest on drawings\n"
        "Dr: interest on capital, salary,\ncommission, transfer to reserve,\nshare of profit", fc=SOFT, ec=BLUE)
    box(a, (14.3, 5.0), 4.6, 2.2, "Fixed capital method:\nPartners' Current\nAccounts", fc=PALE_GREEN, ec=GREEN)
    box(a, (14.3, 1.8), 4.6, 2.2, "Fluctuating capital\nmethod: Partners'\nCapital Accounts", fc=PALE_GREEN,
        ec=GREEN)
    arrow(a, (4.5, 4.6), (6.6, 4.6), text="net profit")
    arrow(a, (12.2, 5.0), (14.3, 6.1), color=GREEN)
    arrow(a, (12.2, 4.2), (14.3, 2.9), color=GREEN)
    a.text(9.6, 1.2, "Divisible profit = net profit + interest on drawings − interest on capital − salary/commission "
                     "to partners − reserve", ha="center", fontsize=8.2, color=GREY)
    save(fig, "acc_ch01_fig01_profit_flow.png")


def fig02_drawings_periods():
    fig, a = canvas(9.6, 3.6, (0, 19.2), (0, 7.2))
    a.text(9.6, 6.8, "Average period for interest on equal drawings made regularly through a 12-month year",
           ha="center", fontsize=9.5, weight="bold")
    rows = [("monthly", "6½ months", "6 months", "5½ months"),
            ("quarterly", "7½ months", "6 months", "4½ months"),
            ("half-yearly", "9 months", "6 months", "3 months")]
    heads = ["withdrawn", "at the beginning", "in the middle", "at the end"]
    xs = [1.6, 6.0, 10.6, 15.2]
    for x, t in zip(xs, heads):
        a.text(x + 1.6, 5.6, t, ha="center", fontsize=9, weight="bold", color=BLUE)
    for r, row in enumerate(rows):
        y = 4.4 - r * 1.3
        for x, t in zip(xs, row):
            box(a, (x, y - 0.45), 3.2, 0.9, t, fc=SOFT if r % 2 == 0 else PALE_GREEN, ec=GREY, fs=8.8)
    a.text(9.6, 0.4, "Interest on drawings = total drawings × rate × average period ÷ 12; "
                     "with no dates given, take 6 months", ha="center", fontsize=8.4, color=GREY)
    save(fig, "acc_ch01_fig02_drawings_periods.png")


if __name__ == "__main__":
    fig01_profit_flow()
    fig02_drawings_periods()
