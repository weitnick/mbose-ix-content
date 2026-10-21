"""Figures for Class X Computer Science, Ch07: HTML Images, Links, Tables and Frames."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import INK, FILLS, plt, save, table_fig  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

MONO = "DejaVu Sans Mono"


def _cell(ax, x, y, w, h, text, fc="white", bold=False, size=10):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=INK, lw=1.0))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, fontweight="bold" if bold else "normal")


def _note(ax, xy, xytext, text):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=8.8, family=MONO, color="#7A2E1B", ha="center", va="center",
                arrowprops=dict(arrowstyle="-|>", color="#7A2E1B", lw=1.0))


def fig_table():
    fig, ax = plt.subplots(figsize=(10, 4.6))
    x0, y0 = 1.6, 0.4
    cw = [2.2, 1.6, 1.6, 1.6]
    rh = 0.62
    xs = [x0]
    for w in cw:
        xs.append(xs[-1] + w)
    top = y0 + 5 * rh
    ax.text((xs[0] + xs[-1]) / 2, top + 0.3, "Marks of Class X", ha="center", va="center", fontsize=11, fontweight="bold")
    # header rows
    _cell(ax, xs[0], top - 2 * rh, cw[0], 2 * rh, "Name", FILLS[0], True)
    _cell(ax, xs[1], top - rh, cw[1] + cw[2], rh, "Marks", FILLS[0], True)
    _cell(ax, xs[3], top - 2 * rh, cw[3], 2 * rh, "Total", FILLS[0], True)
    _cell(ax, xs[1], top - 2 * rh, cw[1], rh, "English", FILLS[0], True)
    _cell(ax, xs[2], top - 2 * rh, cw[2], rh, "Maths", FILLS[0], True)
    data = [["Bari", "72", "85", "157"], ["Iba", "81", "90", "171"], ["Dari", "66", "78", "144"]]
    for r, row in enumerate(data):
        y = top - (3 + r) * rh
        for c, v in enumerate(row):
            _cell(ax, xs[c], y, cw[c], rh, v)
    _note(ax, ((xs[0] + xs[-1]) / 2 - 1.6, top + 0.3), (0.2, top + 0.3), "<CAPTION>")
    _note(ax, (xs[2], top - rh / 2), (xs[2] + 0.2, top + 0.95), 'COLSPAN="2"')
    _note(ax, (xs[0] + 0.1, top - 1.4 * rh), (0.35, top - 1.4 * rh), 'ROWSPAN="2"')
    _note(ax, (xs[3] + cw[3] - 0.1, top - 1.4 * rh), (xs[-1] + 1.15, top - 1.4 * rh), 'ROWSPAN="2"')
    _note(ax, (xs[-1] - 0.1, top - 3.5 * rh), (xs[-1] + 1.15, top - 3.5 * rh), "<TD> data")
    _note(ax, (xs[-1] - 0.1, top - 0.15), (xs[-1] + 1.15, top + 0.55), "<TH> heading")
    _note(ax, (xs[0] + 0.05, top - 4.5 * rh), (0.35, top - 4.5 * rh), "<TR> row")
    ax.set_xlim(-0.6, xs[-1] + 2.1)
    ax.set_ylim(y0 - 0.2, top + 1.3)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "cs_ch07_fig01_table.png")


def _window(ax, x, y, w, h, title, parts):
    ax.add_patch(Rectangle((x, y), w, h, fc="white", ec=INK, lw=1.2))
    for (px, py, pw, ph, lab, fc) in parts:
        ax.add_patch(Rectangle((x + px * w, y + py * h), pw * w, ph * h, fc=fc, ec=INK, lw=0.9))
        ax.text(x + (px + pw / 2) * w, y + (py + ph / 2) * h, lab, ha="center", va="center", fontsize=9.5)
    ax.text(x + w / 2, y - 0.18, title, ha="center", va="top", fontsize=8.6, family=MONO)


def fig_frames():
    fig, ax = plt.subplots(figsize=(11, 3.3))
    w, h, gap = 2.3, 1.7, 0.55
    _window(ax, 0, 0.5, w, h, '<FRAMESET COLS="30%,70%">',
            [(0, 0, 0.3, 1, "1", FILLS[0]), (0.3, 0, 0.7, 1, "2", FILLS[2])])
    _window(ax, w + gap, 0.5, w, h, '<FRAMESET ROWS="25%,75%">',
            [(0, 0.75, 1, 0.25, "1", FILLS[0]), (0, 0, 1, 0.75, "2", FILLS[2])])
    _window(ax, 2 * (w + gap), 0.5, w, h, 'ROWS="50%,50%" COLS="50%,50%"',
            [(0, 0.5, 0.5, 0.5, "1", FILLS[0]), (0.5, 0.5, 0.5, 0.5, "2", FILLS[1]),
             (0, 0, 0.5, 0.5, "3", FILLS[2]), (0.5, 0, 0.5, 0.5, "4", FILLS[3])])
    _window(ax, 3 * (w + gap), 0.5, w, h, 'ROWS="25%,*" + nested COLS',
            [(0, 0.75, 1, 0.25, "heading", FILLS[0]), (0, 0, 0.35, 0.75, "menu", FILLS[1]),
             (0.35, 0, 0.65, 0.75, "content", FILLS[2])])
    ax.set_xlim(-0.1, 4 * w + 3 * gap + 0.1)
    ax.set_ylim(-0.1, 2.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Dividing the browser window with FRAMESET", fontsize=11, fontweight="bold", color=INK)
    save(fig, "cs_ch07_fig02_frames.png")


def fig_links():
    table_fig(["Kind of link", "Example code", "Where it goes"],
              [["External link", '<A HREF="https://www.mbose.in">MBOSE</A>', "another website (absolute URL)"],
               ["Internal link", '<A HREF="page2.html">Next</A>', "another page of the same site (relative URL)"],
               ["Link within a page", '<A NAME="top">  …  <A HREF="#top">Top</A>', "a named spot on the same page"],
               ["Email link", '<A HREF="mailto:office@school.in">Mail</A>', "opens a new email to that address"],
               ["Picture as a link", '<A HREF="map.html"><IMG SRC="map.jpg"></A>', "clicking the picture opens the page"],
               ["Open in new window", '<A HREF="a.html" TARGET="_blank">', "the page opens in a new window or tab"]],
              "cs_ch07_fig03_links.png", col_w=[2.6, 5.9, 5.1], title="Kinds of hyperlinks with the anchor tag <A>",
              size=8.6)


def fig_timetable():
    fig, ax = plt.subplots(figsize=(9.5, 3.4))
    cw = [1.9, 1.7, 1.7, 1.0, 1.9]
    xs = [0]
    for w in cw:
        xs.append(xs[-1] + w)
    rh = 0.6
    top = 4 * rh
    ax.text(xs[-1] / 2, top + 0.3, "Class X Timetable", ha="center", va="center", fontsize=11, fontweight="bold")
    for c, t in enumerate(["Day", "Period 1", "Period 2"]):
        _cell(ax, xs[c], top - rh, cw[c], rh, t, FILLS[0], True)
    _cell(ax, xs[3], 0, cw[3], 4 * rh, "\n".join("BREAK"), FILLS[1], True)
    _cell(ax, xs[4], top - rh, cw[4], rh, "Period 3", FILLS[0], True)
    _cell(ax, xs[0], top - 2 * rh, cw[0], rh, "Monday")
    _cell(ax, xs[1], top - 2 * rh, cw[1], rh, "English")
    _cell(ax, xs[2], top - 2 * rh, cw[2], rh, "Maths")
    _cell(ax, xs[4], top - 2 * rh, cw[4], rh, "Science")
    _cell(ax, xs[0], top - 3 * rh, cw[0], rh, "Tuesday")
    _cell(ax, xs[1], top - 3 * rh, cw[1] + cw[2], rh, "Computer Practical")
    _cell(ax, xs[4], top - 3 * rh, cw[4], rh, "Social Science")
    _cell(ax, xs[0], top - 4 * rh, cw[0], rh, "Wednesday")
    _cell(ax, xs[1], top - 4 * rh, cw[1], rh, "Maths")
    _cell(ax, xs[2], top - 4 * rh, cw[2], rh, "English")
    _cell(ax, xs[4], top - 4 * rh, cw[4], rh, "HPE")
    _note(ax, (xs[3] + cw[3] / 2, 0.05), (xs[3] + cw[3] / 2, -0.55), 'ROWSPAN="4"')
    _note(ax, (xs[1] + 0.3, top - 3 * rh + 0.05), (xs[1] - 0.2, -0.55), 'COLSPAN="2"')
    ax.set_xlim(-0.3, xs[-1] + 0.3)
    ax.set_ylim(-0.85, top + 0.6)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "cs_ch07_fig04_timetable.png")


if __name__ == "__main__":
    fig_table()
    fig_frames()
    fig_links()
    fig_timetable()
