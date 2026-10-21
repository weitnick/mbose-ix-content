"""Figures for Class XII English Core skills chapters: the charts in the case-based reading passages (Skill01).
All data are invented for practice and say so in the passages.
Run: python xii_english_skills.py   (writes PNGs into Class XII Content/English Core/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class XII Content", "English Core", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, GRID = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#DDE3EA"
PALETTE = ["#1F4E79", "#B7791F", "#2E7D5B", "#9C3D54", "#5B6BBF", "#7A8794"]
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.edgecolor": GREY, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK, "axes.titleweight": "bold", "axes.titlesize": 11.5})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def _style(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def bar(name, title, labels, values, ylabel, fmt="{:g}", color=ACC, highlight=None):
    fig, ax = plt.subplots(figsize=(7, 3.6))
    colors = [HI if highlight is not None and i == highlight else color for i in range(len(values))]
    bars = ax.bar(labels, values, color=colors, width=0.62)
    for b, v in zip(bars, values):
        ax.annotate(fmt.format(v), (b.get_x() + b.get_width() / 2, b.get_height()), ha="center", va="bottom",
                    fontsize=9, color=INK, xytext=(0, 2), textcoords="offset points")
    ax.set_title(title, color=INK)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, max(values) * 1.15)
    _style(ax)
    save(fig, name)


def grouped(name, title, labels, series, ylabel):
    fig, ax = plt.subplots(figsize=(7, 3.6))
    n = len(series)
    width = 0.8 / n
    for i, (label, values) in enumerate(series):
        xs = [x + (i - (n - 1) / 2) * width for x in range(len(labels))]
        bars = ax.bar(xs, values, width=width * 0.95, color=PALETTE[i], label=label)
        for b, v in zip(bars, values):
            ax.annotate(f"{v:g}", (b.get_x() + b.get_width() / 2, b.get_height()), ha="center", va="bottom",
                        fontsize=8.5, color=INK, xytext=(0, 2), textcoords="offset points")
    ax.set_xticks(range(len(labels)), labels)
    ax.set_title(title, color=INK)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, max(max(v) for _, v in series) * 1.32)
    ax.legend(frameon=False, ncols=n, loc="upper right")
    _style(ax)
    save(fig, name)


def line(name, title, labels, values, ylabel, fmt="{:g}"):
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot(labels, values, color=ACC, linewidth=2.2, marker="o", markersize=6, markerfacecolor="white",
            markeredgewidth=2)
    for x, v in zip(labels, values):
        ax.annotate(fmt.format(v), (x, v), ha="center", va="bottom", fontsize=9, color=INK, xytext=(0, 7),
                    textcoords="offset points")
    ax.set_title(title, color=INK)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, max(values) * 1.18)
    _style(ax)
    save(fig, name)


def pie(name, title, labels, values):
    fig, ax = plt.subplots(figsize=(7, 3.8))
    wedges, _ = ax.pie(values, colors=PALETTE[:len(values)], startangle=90, counterclock=False,
                       wedgeprops={"linewidth": 1.5, "edgecolor": "white"})
    ax.legend(wedges, [f"{l}: {v}%" for l, v in zip(labels, values)], frameon=False, loc="center left",
              bbox_to_anchor=(1.0, 0.5), fontsize=10)
    for w, v in zip(wedges, values):
        if v >= 8:
            import math
            ang = math.radians((w.theta1 + w.theta2) / 2)
            ax.text(0.68 * math.cos(ang), 0.68 * math.sin(ang), f"{v}%", ha="center", va="center", color="white",
                    fontsize=10, fontweight="bold")
    ax.set_title(title, color=INK)
    ax.axis("equal")
    save(fig, name)


# ---- Skill01: Reading Comprehension (case-based passages C1–C6) ---------------------------------
bar("skill01_c1_careers.png", "Career choices of 500 Class XII students in a district",
    ["Engineering\nand IT", "Medicine", "Business", "Teaching", "Civil\nservices", "Arts and\nmedia", "Undecided"], [22, 18, 16, 14, 12, 8, 10], "Students (per cent)", fmt="{:g}%", highlight=0)
pie("skill01_c2_sleep.png", "Hours of sleep on school nights (600 students)",
    ["Less than 6 hours", "6 to 7 hours", "7 to 8 hours", "More than 8 hours", "It varies"], [18, 34, 30, 12, 6])
pie("skill01_c3_plastic.png", "Plastic waste collected in a hill town, by type",
    ["Food wrappers and sachets", "Carry bags", "Bottles", "Disposable cups and plates", "Other"], [30, 26, 18, 14, 12])
grouped("skill01_c4_screen.png", "Average hours a day: screens versus outdoor activity", ["Age 13", "Age 15", "Age 17"],
        [("Screen time", [3.1, 4.2, 5.0]), ("Outdoor activity", [1.8, 1.2, 0.7])], "Hours a day")
line("skill01_c5_visitors.png", "Visitors to a hill district, by month (thousands)",
     ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
     [18, 22, 30, 41, 52, 34, 21, 24, 29, 47, 43, 38], "Visitors (thousands)")
pie("skill01_c6_news.png", "Main source of news for 18–25-year-olds",
    ["Social media", "News apps and websites", "Television", "Newspapers", "Friends and family"], [46, 22, 17, 9, 6])
