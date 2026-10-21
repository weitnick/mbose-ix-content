"""Figures for Class X English skills chapters: the charts in the reading passages (Skill01) and the analytical
paragraph tasks (Skill04). All data are invented for practice and say so in the passages.
Run: python x_english_skills.py   (writes PNGs into Class X Content/English/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "English", "Generated Content", "figures")
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


# ---- Skill01: Reading Comprehension (passages 11–20) -------------------------------------------
bar("skill01_p11_rainfall.png", "Rainfall recorded at a weather station in East Khasi Hills (one year)",
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    [12, 38, 190, 560, 1180, 2840, 2610, 1820, 1270, 480, 55, 18], "Rainfall (mm)", highlight=5)
line("skill01_p12_digital_payments.png", "Stalls accepting digital payments at a weekly market",
     ["2020", "2021", "2022", "2023", "2024", "2025"], [8, 21, 37, 55, 68, 79], "Stalls (per cent)", fmt="{:g}%")
pie("skill01_p13_free_time.png", "How 400 students spend most of their free time",
    ["Social media", "Watching videos", "Outdoor games", "Helping at home", "Reading", "Other"],
    [32, 22, 18, 12, 10, 6])
line("skill01_p15_homestays.png", "Homestays registered in a village", ["2019", "2020", "2021", "2022", "2023", "2024", "2025"],
     [4, 3, 6, 11, 17, 22, 28], "Number of homestays")
bar("skill01_p16_reading.png", "Students who read at least one book a month for pleasure",
    ["Class VI", "Class VII", "Class VIII", "Class IX", "Class X"], [64, 58, 49, 41, 33], "Students (per cent)",
    fmt="{:g}%")
bar("skill01_p17_solar.png", "Households using solar power in a village of 150 households",
    ["2019", "2020", "2021", "2022", "2023", "2024", "2025"], [12, 25, 41, 60, 84, 102, 118], "Households")
pie("skill01_p18_water.png", "How a family of five uses water at home", ["Bathing", "Flushing toilets", "Washing clothes",
    "Cooking and drinking", "Washing utensils", "Other"], [35, 25, 15, 10, 10, 5])
grouped("skill01_p19_sports.png", "Students taking part in school sports", ["Football", "Badminton", "Athletics",
        "Basketball", "Archery"], [("Boys", [62, 30, 25, 18, 10]), ("Girls", [38, 45, 28, 12, 14])], "Students")

# ---- Skill04: Analytical Paragraphs ----------------------------------------------------------------
pie("skill04_t01_transport.png", "How 600 students travel to school", ["Walk", "School bus", "Public bus or taxi",
    "Two-wheeler with a parent", "Bicycle", "Car"], [34, 22, 20, 14, 6, 4])
bar("skill04_t02_library.png", "Books issued by a school library", ["April", "May", "June", "July", "August", "September"],
    [320, 280, 150, 410, 450, 380], "Books issued")
bar("skill04_t03_internet.png", "Hours a week Class X students spend online, by purpose",
    ["Study", "Social media", "Videos", "Games", "News"], [6, 9, 7, 4, 1], "Hours a week")
line("skill04_t04_literacy.png", "Literacy rate of a village", ["2001", "2006", "2011", "2016", "2021"],
     [54, 61, 68, 76, 84], "Literacy rate (per cent)", fmt="{:g}%")
pie("skill04_t05_sports_budget.png", "How a school spent its sports budget", ["Equipment", "Coaching",
    "Travel to tournaments", "Ground upkeep", "Prizes"], [40, 25, 20, 10, 5])
bar("skill04_t06_electricity.png", "Electricity used by a household in Shillong", ["January", "March", "May", "July",
    "September", "November"], [210, 160, 140, 150, 145, 190], "Units (kWh)")
bar("skill04_t08_canteen.png", "Items sold at a school canteen in one week", ["Momos", "Samosas", "Sandwiches", "Juice",
    "Fruit"], [310, 260, 220, 180, 140], "Items sold")
grouped("skill04_t10_trees.png", "A school's tree-planting drive", ["2021", "2022", "2023", "2024", "2025"],
        [("Planted", [200, 250, 300, 300, 350]), ("Still alive in 2025", [90, 140, 210, 240, 330])], "Saplings")
