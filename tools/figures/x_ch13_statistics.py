"""Figures for Class X Mathematics, Chapter 13: Statistics.
Run: python x_ch13_statistics.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, SHADE = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#BFD3E6"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def frame(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9)


# Fig 13.1: histogram of the hospital data with the modal class and its neighbours marked
def fig_modal_class():
    edges = [5, 15, 25, 35, 45, 55, 65]
    f = [6, 11, 21, 23, 14, 5]
    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    for i, fi in enumerate(f):
        if i == 3:
            fc, ec = HI, INK
        elif i in (2, 4):
            fc, ec = SHADE, ACC
        else:
            fc, ec = SOFT, ACC
        ax.bar(edges[i], fi, width=10, align="edge", color=fc, edgecolor=ec, lw=1.1)
        ax.text(edges[i] + 5, fi + 0.5, str(fi), ha="center", va="bottom", fontsize=9, color=INK)
    ax.text(30, 10.5, "$f_0 = 21$", ha="center", fontsize=10, color=ACC)
    ax.text(40, 12.0, "$f_1 = 23$", ha="center", fontsize=10, color="white")
    ax.text(50, 7.0, "$f_2 = 14$", ha="center", fontsize=10, color=ACC)
    ax.annotate("modal class 35-45\n$l = 35,\\ h = 10$", xy=(40, 23), xytext=(57, 21.5), fontsize=9, color=INK,
                ha="left", va="center", arrowprops=dict(arrowstyle="->", color=INK, lw=0.9))
    ax.set_xticks(edges)
    ax.set_xlim(3, 77)
    ax.set_ylim(0, 27)
    ax.set_xlabel("Age (in years)", color=INK)
    ax.set_ylabel("Number of patients", color=INK)
    frame(ax)
    save(fig, "ch13_fig01_modal_class.png")


# Fig 13.2: cumulative frequencies of the electricity data, with n/2 = 34 locating the median class
def fig_median_class():
    edges = [65, 85, 105, 125, 145, 165, 185, 205]
    cf = [4, 9, 22, 42, 56, 64, 68]
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    for i, c in enumerate(cf):
        fc = HI if i == 3 else SOFT
        ax.bar(edges[i], c, width=20, align="edge", color=fc, edgecolor=ACC if i != 3 else INK, lw=1.1)
        ax.text(edges[i] + 10, c + 1, str(c), ha="center", va="bottom", fontsize=9, color=INK)
    ax.axhline(34, color=ACC, lw=1.2, ls="--")
    ax.text(66, 35.5, "$\\frac{n}{2} = 34$", fontsize=11, color=ACC, ha="left", va="bottom")
    ax.annotate("first cf greater than 34:\nmedian class 125-145", xy=(131, 42), xytext=(68, 60), fontsize=9,
                color=INK, ha="left", va="center", arrowprops=dict(arrowstyle="->", color=INK, lw=0.9))
    ax.set_xticks(edges)
    ax.set_xlim(60, 210)
    ax.set_ylim(0, 76)
    ax.set_xlabel("Monthly consumption (in units)", color=INK)
    ax.set_ylabel("Cumulative frequency", color=INK)
    frame(ax)
    save(fig, "ch13_fig02_median_class.png")


if __name__ == "__main__":
    fig_modal_class()
    fig_median_class()
