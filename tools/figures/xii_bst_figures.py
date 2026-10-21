"""Figures for Class XII Business Studies (all chapters).
Run: python xii_bst_figures.py [figure-name ...]   (no names = all)
Writes PNGs to Business Studies\\Generated Content\\figures."""
import os
import sys

from xii_acc_ch01_partnership import *
import xii_acc_ch01_partnership as base

OUT = "D:/MBOSE APP/Class XII Content/Business Studies/Generated Content/figures"
os.makedirs(OUT, exist_ok=True)


def bsave(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(path)


def ch01_levels():
    fig, a = canvas(9.6, 5.0, (0, 19.2), (0, 10.0))
    a.text(9.6, 9.6, "Levels of management", ha="center", fontsize=10, weight="bold")
    tiers = [("Top management\nCEO, MD, board of directors\nobjectives, policies,\ncoordination, survival", 6.6, 7.0, PALE_AMBER, AMBER),
             ("Middle management\ndivisional and departmental heads\ninterpret policies, assign duties, motivate", 3.9, 10.4, SOFT, BLUE),
             ("Supervisory (operational) management\nforemen and supervisors\noversee workers, quality, wastage, safety", 1.2, 13.8, PALE_GREEN, GREEN)]
    for t, y, w, fc, ec in tiers:
        box(a, (9.6 - w / 2, y), w, 2.4, t, fc=fc, ec=ec, fs=8.2, bold=False)
    a.annotate("", xy=(1.2, 8.6), xytext=(1.2, 1.2), arrowprops=dict(arrowstyle="->", lw=1.2))
    a.text(0.6, 4.9, "authority", rotation=90, ha="center", va="center", fontsize=8, style="italic")
    a.annotate("", xy=(18.0, 1.2), xytext=(18.0, 8.6), arrowprops=dict(arrowstyle="->", lw=1.2))
    a.text(18.6, 4.9, "number of managers", rotation=90, ha="center", va="center", fontsize=8, style="italic")
    bsave(fig, "bst_ch01_fig01_levels.png")


def flow(title, steps, name, cols=4, w=4.2, h=1.6):
    """Numbered steps in rows of `cols`, left to right, with arrows."""
    rows = (len(steps) + cols - 1) // cols
    H = 1.6 + rows * (h + 1.2)
    fig, a = canvas(9.6, H / 2, (0, 19.2), (0, H))
    a.text(9.6, H - 0.5, title, ha="center", fontsize=10, weight="bold")
    gap = (19.2 - cols * w) / (cols + 1)
    pos = []
    for i, s in enumerate(steps):
        r, c = divmod(i, cols)
        x = gap + c * (w + gap)
        y = H - 1.4 - (r + 1) * h - r * 1.2
        fc, ec = (PALE_AMBER, AMBER) if i in (0, len(steps) - 1) else (SOFT, BLUE)
        box(a, (x, y), w, h, f"{i + 1}. {s}", fc=fc, ec=ec, fs=8.2)
        pos.append((x, y))
    for i in range(len(steps) - 1):
        (x0, y0), (x1, y1) = pos[i], pos[i + 1]
        if abs(y0 - y1) < 0.01:
            arrow(a, (x0 + w, y0 + h / 2), (x1, y1 + h / 2))
        else:
            arrow(a, (x0 + w / 2, y0), (x1 + w / 2, y1 + h))
    bsave(fig, name)


def ch04_process():
    flow("Steps in the planning process",
         ["Setting\nobjectives", "Developing\npremises", "Identifying\nalternatives", "Evaluating\nalternatives",
          "Selecting an\nalternative", "Implementing\nthe plan", "Follow-up\naction"],
         "bst_ch04_fig01_process.png")


def tree(title, top, kids, name, grandkids=None, w=3.6, h=1.2):
    """Two- or three-level organisation chart."""
    H = 7.0 if grandkids else 5.0
    fig, a = canvas(9.6, H / 2, (0, 19.2), (0, H))
    a.text(9.6, H - 0.4, title, ha="center", fontsize=10, weight="bold")
    ty = H - 2.2
    box(a, (9.6 - w / 2, ty), w, h, top, fc=PALE_AMBER, ec=AMBER, fs=8.4, bold=True)
    n = len(kids)
    gap = (19.2 - n * w) / (n + 1)
    ky = ty - 2.4
    a.plot([9.6, 9.6], [ty, ty - 0.6], color=INK, lw=1.1)
    xs = [gap + i * (w + gap) + w / 2 for i in range(n)]
    a.plot([xs[0], xs[-1]], [ty - 0.6, ty - 0.6], color=INK, lw=1.1)
    for i, (k, x) in enumerate(zip(kids, xs)):
        arrow(a, (x, ty - 0.6), (x, ky + h))
        box(a, (x - w / 2, ky), w, h, k, fc=SOFT, ec=BLUE, fs=8.0)
        if grandkids:
            g = grandkids[i]
            gy = ky - 2.2
            gw = w / len(g) - 0.15
            a.plot([x, x], [ky, ky - 0.5], color=INK, lw=1.0)
            gxs = [x - w / 2 + j * (gw + 0.15) + gw / 2 for j in range(len(g))]
            if len(g) > 1:
                a.plot([gxs[0], gxs[-1]], [ky - 0.5, ky - 0.5], color=INK, lw=1.0)
            for t, gx in zip(g, gxs):
                arrow(a, (gx, ky - 0.5), (gx, gy + h))
                box(a, (gx - gw / 2, gy), gw, h, t, fc=PALE_GREEN, ec=GREEN, fs=6.8)
    bsave(fig, name)


def ch05_structures():
    tree("Functional structure", "Managing Director",
         ["Production", "Marketing", "Finance", "Human\nresources"], "bst_ch05_fig01_functional.png")
    tree("Divisional structure", "Managing Director",
         ["Cosmetics\ndivision", "Garments\ndivision", "Footwear\ndivision"], "bst_ch05_fig02_divisional.png",
         grandkids=[["Prod.", "Mktg.", "Fin."]] * 3, w=4.8)


def ch07_maslow():
    from matplotlib.patches import Polygon
    fig, a = canvas(9.6, 5.2, (0, 19.2), (0, 10.4))
    a.text(9.6, 10.0, "Maslow's need hierarchy", ha="center", fontsize=10, weight="bold")
    levels = [("Self-actualisation needs", "growth, self-fulfilment, achievement"),
              ("Esteem needs", "self-respect, status, recognition, attention"),
              ("Affiliation / belonging needs", "affection, acceptance, friendship"),
              ("Safety / security needs", "stability of income, pension, job security"),
              ("Basic physiological needs", "hunger, thirst, shelter, sleep — basic salary")]
    cols = [(PALE_AMBER, AMBER), (SOFT, BLUE), (PALE_GREEN, GREEN), (SOFT, BLUE), (PALE_AMBER, AMBER)]
    top, base, n = 9.3, 0.5, len(levels)
    hh = (top - base) / n
    for i, ((t, s), (fc, ec)) in enumerate(zip(levels, cols)):
        y1 = top - i * hh
        y0 = y1 - hh
        def half(y):
            return 0.6 + 8.4 * (top - y) / (top - base)
        poly = Polygon([(9.6 - half(y0), y0), (9.6 + half(y0), y0), (9.6 + half(y1), y1), (9.6 - half(y1), y1)],
                       closed=True, fc=fc, ec=ec, lw=1.4)
        a.add_patch(poly)
        if i == 0:
            a.text(9.6, y0 + 0.45 * hh, "Self-\nactualisation", ha="center", va="center", fontsize=7.4, weight="bold")
            continue
        a.text(9.6, (y0 + y1) / 2 + 0.18, t, ha="center", va="center", fontsize=8.2, weight="bold")
        if i:
            a.text(9.6, (y0 + y1) / 2 - 0.42, s, ha="center", va="center", fontsize=7.0)
    a.text(18.6, 4.9, "higher-level needs arise\nonly when lower ones\nare satisfied", ha="center", va="center", fontsize=7.6,
           style="italic")
    bsave(fig, "bst_ch07_fig01_maslow.png")


def ch07_communication():
    flow("Elements of the communication process",
         ["Sender", "Message", "Encoding", "Media", "Decoding", "Receiver", "Feedback"],
         "bst_ch07_fig02_communication.png")


def ch08_process():
    flow("Steps in the controlling process",
         ["Setting\nperformance\nstandards", "Measuring\nactual\nperformance", "Comparing with\nstandards",
          "Analysing\ndeviations", "Taking\ncorrective\naction"],
         "bst_ch08_fig01_process.png", cols=5, w=3.2, h=1.9)


def ch11_channels():
    fig, a = canvas(9.6, 4.6, (0, 19.2), (0, 9.2))
    a.text(9.6, 8.8, "Channels of distribution", ha="center", fontsize=10, weight="bold")
    rows = [("Zero level\n(direct)", ["Manufacturer", "Consumer"]),
            ("One level", ["Manufacturer", "Retailer", "Consumer"]),
            ("Two level", ["Manufacturer", "Wholesaler", "Retailer", "Consumer"]),
            ("Three level", ["Manufacturer", "Agent", "Wholesaler", "Retailer", "Consumer"])]
    for r, (lab, chain) in enumerate(rows):
        y = 6.9 - r * 2.0
        a.text(1.4, y + 0.5, lab, ha="center", va="center", fontsize=8.2, weight="bold")
        w, gap = 2.6, 0.75
        for i, c in enumerate(chain):
            x = 3.0 + i * (w + gap)
            fc, ec = (PALE_AMBER, AMBER) if c in ("Manufacturer", "Consumer") else (SOFT, BLUE)
            box(a, (x, y), w, 1.0, c, fc=fc, ec=ec, fs=7.8)
            if i:
                arrow(a, (x - gap, y + 0.5), (x, y + 0.5))
    bsave(fig, "bst_ch11_fig01_channels.png")


FIGS = {"ch01_levels": ch01_levels, "ch04_process": ch04_process, "ch05_structures": ch05_structures,
        "ch07_maslow": ch07_maslow, "ch07_communication": ch07_communication, "ch08_process": ch08_process,
        "ch11_channels": ch11_channels}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        FIGS[n]()
