"""Figures for Class IX Mathematics, Chapter 12: Statistics (graphical representation of data)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "CLASS IX Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, MUTED, GREEN = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#5D6B7A", "#4A7C59"
BAR = "#9DB9D6"
plt.rcParams.update({"font.size": 8.5, "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def style(ax, xlabel, ylabel, title=None):
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.grid(axis="y", color="#DDE3EA", lw=0.6); ax.set_axisbelow(True)
    if title:
        ax.set_title(title, fontsize=9, color=MUTED)


def kink(ax, x0, y=0):
    """Draw a small zig-zag on the x-axis to show a break in the scale."""
    ax.plot([x0 - 1.2, x0 - 0.6, x0, x0 + 0.6], [y, y + 0.4, y - 0.4, y], color=MUTED, lw=1, clip_on=False)


def bar_chart(names, values, xlabel, ylabel, fname, title=None, rot=0, figsize=(5.6, 2.8), fmt="{:g}", color=BAR):
    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.bar(range(len(names)), values, width=0.6, color=color, edgecolor=ACC, lw=0.8)
    ax.set_xticks(range(len(names))); ax.set_xticklabels(names, rotation=rot, ha="right" if rot else "center")
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height(), fmt.format(v), ha="center", va="bottom", fontsize=7.5, color=INK)
    style(ax, xlabel, ylabel, title)
    save(fig, fname)


def histogram(edges, freqs, xlabel, ylabel, fname, title=None, heights=None, polygon=False, kink_at=None, figsize=(5.2, 2.9), labels_on_bars=True, extra_poly=None):
    fig, ax = plt.subplots(figsize=figsize)
    hs = heights if heights is not None else freqs
    for a, b, h, f in zip(edges[:-1], edges[1:], hs, freqs):
        ax.bar(a, h, width=b - a, align="edge", color=BAR, edgecolor=ACC, lw=0.8)
        if labels_on_bars:
            ax.text((a + b) / 2, h, f"{h:g}", ha="center", va="bottom", fontsize=7.5)
    ax.set_xticks(edges); ax.set_xticklabels([f"{e:g}" for e in edges], fontsize=7.5)
    if polygon:
        w0 = edges[1] - edges[0]; wn = edges[-1] - edges[-2]
        xs = [edges[0] - w0 / 2] + [(a + b) / 2 for a, b in zip(edges[:-1], edges[1:])] + [edges[-1] + wn / 2]
        ys = [0] + list(hs) + [0]
        ax.plot(xs, ys, color=HI, lw=1.6, marker="o", ms=3)
        letters = "ABCDEFGHIJKLMNOP"
        for i, (x, y) in enumerate(zip(xs, ys)):
            ax.text(x, y + max(hs) * 0.06, letters[i], ha="center", fontsize=7.5, color=HI, weight="bold")
        ax.set_xlim(xs[0] - w0 * 0.3, xs[-1] + wn * 0.3)
    if kink_at is not None:
        kink(ax, kink_at)
    style(ax, xlabel, ylabel, title)
    save(fig, fname)


def polygons(marks, series, xlabel, ylabel, fname, title=None, step=None, figsize=(5.4, 2.9)):
    fig, ax = plt.subplots(figsize=figsize)
    step = step or (marks[1] - marks[0])
    xs = [marks[0] - step] + list(marks) + [marks[-1] + step]
    from matplotlib.ticker import MaxNLocator
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    for (name, ys), col in zip(series, [ACC, HI, GREEN]):
        yy = [0] + list(ys) + [0]
        ax.plot(xs, yy, color=col, lw=1.6, marker="o", ms=3, label=name)
        if len(series) == 1:
            for x, y, t in zip(xs, yy, "ABCDEFGHIJKLMNOP"):
                ax.text(x, y + max(yy) * 0.05, t, ha="center", fontsize=7.5, color=HI, weight="bold")
    ax.set_xticks(xs); ax.set_xticklabels([f"{x:g}" for x in xs], fontsize=7.5)
    if len(series) > 1:
        ax.legend(frameon=False, fontsize=8)
    style(ax, xlabel, ylabel, title)
    save(fig, fname)


# ------------------------------------------------------------------ lesson figures
def lesson():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    births = [3, 4, 2, 2, 5, 1, 2, 6, 3, 4, 4, 4]
    bar_chart(months, births, "Month of birth", "Number of students", "ch12_fig01_example1_birth_months.png",
              title="Example 1: months of birth of 40 students")
    heads = ["Grocery", "Rent", "Education", "Medicine", "Fuel", "Entertainment", "Misc."]
    spend = [4, 5, 5, 2, 2, 1, 1]
    bar_chart(heads, spend, "Heads of expenditure", "Expenditure (thousand ₹)", "ch12_fig02_example2_expenditure.png",
              title="Example 2: monthly expenditure of a family", rot=25)
    edges = [30.5, 35.5, 40.5, 45.5, 50.5, 55.5, 60.5]
    freqs = [9, 6, 15, 3, 1, 2]
    histogram(edges, freqs, "Weight (kg)", "Number of students", "ch12_fig03_histogram_weights.png",
              title="Histogram: weights of 36 students", kink_at=None)
    histogram(edges, freqs, "Weight (kg)", "Number of students", "ch12_fig05_polygon_weights.png",
              title="Frequency polygon ABCDEFGH on the histogram", polygon=True, labels_on_bars=False)
    # Example 3: varying widths, wrong and correct
    e = [0, 20, 30, 40, 50, 60, 70, 100]
    f = [7, 10, 10, 20, 20, 15, 8]
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 2.7))
    for ax, hs, t in [(axs[0], f, "Wrong: heights = frequencies"),
                      (axs[1], [7 / 20 * 10, 10, 10, 20, 20, 15, 8 / 30 * 10], "Correct: heights per 10-mark interval")]:
        for a, b, h in zip(e[:-1], e[1:], hs):
            ax.bar(a, h, width=b - a, align="edge", color=BAR if "Correct" in t else "#F2D7D5", edgecolor=ACC, lw=0.8)
            ax.text((a + b) / 2, h, f"{h:.3g}", ha="center", va="bottom", fontsize=7)
        ax.set_xticks(e); ax.set_xticklabels([str(v) for v in e], fontsize=7.5)
        style(ax, "Marks", "Students" if "Wrong" in t else "Proportion of students per 10 marks", t)
    save(fig, "ch12_fig04_example3_varying_widths.png")
    # Example 4: 51 students, polygon starting at O with A on the y-axis
    e = list(range(0, 101, 10))
    f = [5, 10, 4, 6, 7, 3, 2, 2, 3, 9]
    fig, ax = plt.subplots(figsize=(5.8, 2.9))
    for a, b, h in zip(e[:-1], e[1:], f):
        ax.bar(a, h, width=10, align="edge", color=BAR, edgecolor=ACC, lw=0.8)
    xs = [-5] + [a + 5 for a in e[:-1]] + [105]; ys = [0] + f + [0]
    ax.plot(xs, ys, color=HI, lw=1.2, ls=":")
    ax.plot([0] + xs[1:], [2.5] + ys[1:], color=HI, lw=1.6, marker="o", ms=3)
    ax.plot([0], [0], "o", color=INK, ms=3)
    for x, y, t in [(0, 0, "O"), (0, 2.5, "A")] + list(zip(xs[1:], ys[1:], "BCDEFGHIJKL")):
        ax.text(x + (1.8 if t in "OA" else 0), y + 0.6, t, ha="center", fontsize=7.5, color=HI, weight="bold")
    ax.set_xlim(-12, 112); ax.axvline(0, color=MUTED, lw=0.8)
    ax.set_xticks([-10] + e + [110]); ax.set_xticklabels(["–10"] + [str(v) for v in e] + ["110"], fontsize=7.5)
    style(ax, "Marks", "Number of students", "Example 4: polygon OABC...L (51 students)")
    save(fig, "ch12_fig06_example4_polygon.png")
    polygons([145, 155, 165, 175, 185, 195], [("weeks", [5, 10, 20, 9, 6, 2])], "Cost of living index (class-marks)",
             "Number of weeks", "ch12_fig07_example5_polygon.png", title="Example 5: polygon ABCDEFGH from class-marks")


# ------------------------------------------------------------------ Exercise 12.1
def exercises():
    bar_chart(["Reproductive\nhealth", "Neuro-\npsychiatric", "Injuries", "Cardio-\nvascular", "Respiratory", "Other"],
              [31.8, 25.4, 12.4, 4.3, 4.1, 22.0], "Cause", "Female fatality rate (%)", "ch12_fig08_ex_q1.png",
              title="Q1: causes of illness and death (women aged 15–44)", figsize=(6.0, 2.9))
    bar_chart(["SC", "ST", "Non SC/ST", "Backward districts", "Non-backward districts", "Rural", "Urban"],
              [940, 970, 920, 950, 920, 930, 910], "Section of society", "Girls per 1000 boys", "ch12_fig09_ex_q2.png",
              title="Q2: girls per thousand boys", figsize=(6.0, 3.0), rot=25)
    bar_chart(list("ABCDEF"), [75, 55, 37, 29, 10, 37], "Political party", "Seats won", "ch12_fig10_ex_q3.png",
              title="Q3: seats won", figsize=(4.6, 2.6))
    histogram([117.5, 126.5, 135.5, 144.5, 153.5, 162.5, 171.5, 180.5], [3, 5, 9, 12, 5, 4, 2], "Length (mm)",
              "Number of leaves", "ch12_fig11_ex_q4.png", title="Q4: lengths of 40 leaves (continuous classes)")
    histogram(list(range(300, 1001, 100)), [14, 56, 60, 86, 74, 62, 48], "Life time (hours)", "Number of lamps",
              "ch12_fig12_ex_q5.png", title="Q5: life times of 400 neon lamps")
    polygons([5, 15, 25, 35, 45], [("Section A", [3, 9, 17, 12, 9]), ("Section B", [5, 19, 15, 10, 1])], "Marks (class-marks)",
             "Number of students", "ch12_fig13_ex_q6.png", title="Q6: marks of two sections")
    polygons([3.5 + 6 * k for k in range(10)], [("Team A", [2, 1, 8, 9, 4, 5, 6, 10, 6, 2]), ("Team B", [5, 6, 2, 10, 5, 6, 3, 4, 8, 10])],
             "Number of balls (class-marks)", "Runs", "ch12_fig14_ex_q7.png", title="Q7: runs on the first 60 balls", figsize=(6.2, 2.9))
    e = [1, 2, 3, 5, 7, 10, 15, 17]; f = [5, 3, 6, 12, 9, 10, 4]
    hs = [fi / (b - a) * 1 for a, b, fi in zip(e[:-1], e[1:], f)]
    histogram(e, f, "Age (years)", "Children per 1-year interval", "ch12_fig15_ex_q8.png",
              title="Q8: adjusted heights (minimum class size 1)", heights=hs)
    e = [1, 4, 6, 8, 12, 20]; f = [6, 30, 44, 16, 4]
    hs = [fi / (b - a) * 2 for a, b, fi in zip(e[:-1], e[1:], f)]
    histogram(e, f, "Number of letters", "Surnames per 2-letter interval", "ch12_fig16_ex_q9.png",
              title="Q9: adjusted heights (minimum class size 2)", heights=hs)


def practice():
    histogram([10, 20, 30, 40, 50, 60, 70], [3, 5, 9, 12, 7, 4], "Height (cm)", "Number of plants",
              "ch12_fig17_plants_histogram_polygon.png", title="Heights of 40 plants: histogram and polygon", polygon=True,
              labels_on_bars=False)
    e = [0, 10, 20, 25, 30, 40, 60]; f = [12, 16, 8, 6, 10, 8]
    hs = [fi / (b - a) * 5 for a, b, fi in zip(e[:-1], e[1:], f)]
    histogram(e, f, "Age (years)", "People per 5-year interval", "ch12_fig18_health_camp.png",
              title="Ages of 60 people at a health camp (adjusted heights)", heights=hs)
    polygons([10, 30, 50, 70, 90], [("Class IX A", [4, 10, 16, 14, 6]), ("Class IX B", [6, 14, 12, 10, 8])], "Marks (class-marks)",
             "Number of students", "ch12_fig19_two_sections.png", title="Marks of two sections (50 students each)")


if __name__ == "__main__":
    lesson(); exercises(); practice()
