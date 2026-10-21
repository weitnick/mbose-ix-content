"""Figures for Class IX Mathematics, Chapter 1: Number Systems.
Run: python ch01_number_systems.py   (writes PNGs into Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyBboxPatch, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "CLASS IX Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def number_line(ax, lo, hi, y=0, labels=True, step=1):
    ax.annotate("", xy=(hi + 0.45, y), xytext=(lo - 0.45, y), arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1))
    x = lo
    while x <= hi + 1e-9:
        ax.plot([x, x], [y - 0.07, y + 0.07], color=INK, lw=1)
        if labels:
            ax.text(x, y - 0.28, f"{x:g}", ha="center", va="center", color=INK)
        x += step


# Fig 1: nested number sets
def fig_sets():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    boxes = [("Real numbers  $\\mathbb{R}$", 0, 0, 10, 5.4, "#F7F9FC"),
             ("Rational numbers  $\\mathbb{Q}$", 0.3, 0.3, 6.4, 4.6, "#EEF3F9"),
             ("Integers  $\\mathbb{Z}$", 0.6, 0.6, 4.9, 3.6, "#E3ECF6"),
             ("Whole numbers  $\\mathbb{W}$", 0.9, 0.9, 3.55, 2.5, "#D6E3F1"),
             ("Natural numbers  $\\mathbb{N}$", 1.2, 1.2, 2.75, 1.3, "#C7D9EC")]
    for label, x, y, w, h, c in boxes:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.25", fc=c, ec=ACC, lw=1))
        ax.text(x + 0.12, y + h - 0.28, label, fontsize=8.5, color=ACC, va="center", weight="bold")
    ax.text(2.55, 1.65, "1, 2, 3, …", ha="center", fontsize=9)
    ax.text(4.15, 1.3, "0", ha="center", fontsize=9)
    ax.text(3.9, 3.62, "−1, −2, −3, …", ha="center", fontsize=9)
    ax.text(6.05, 2.6, "$\\frac{1}{2}$", ha="center", fontsize=11)
    ax.text(6.05, 1.7, "$-\\frac{3}{4}$", ha="center", fontsize=11)
    ax.text(6.05, 3.5, "$0.\\overline{3}$", ha="center", fontsize=10)
    ax.add_patch(FancyBboxPatch((6.8, 0.3), 2.9, 4.6, boxstyle="round,pad=0.02,rounding_size=0.25", fc="#FDF7EA", ec=HI, lw=1))
    ax.text(6.92, 4.62, "Irrational numbers", fontsize=8.5, color=HI, weight="bold", va="center")
    for i, t in enumerate(["$\\sqrt{2}$", "$\\sqrt{3}$", "$\\pi$", "$0.1010010001\\ldots$"]):
        ax.text(8.25, 3.8 - i * 0.9, t, ha="center", fontsize=11 if i < 3 else 9)
    ax.set_xlim(-0.1, 10.1); ax.set_ylim(-0.1, 5.5); ax.axis("off")
    save(fig, "ch01_fig01_number_sets.png")


# Fig 2: locating sqrt 2 and sqrt 3
def fig_root2_root3():
    fig, ax = plt.subplots(figsize=(6.2, 2.6))
    number_line(ax, -1, 3)
    # unit square OABC on the line
    ax.add_patch(Rectangle((0, 0), 1, 1, fill=False, ec=ACC, lw=1.2))
    ax.plot([0, 1], [0, 1], color=ACC, lw=1.4)
    # BD perpendicular to OB of unit length, D = B + unit vector perpendicular to OB
    import math
    bx, by = 1, 1
    ux, uy = -1 / math.sqrt(2), 1 / math.sqrt(2)
    dx, dy = bx + ux, by + uy
    ax.plot([bx, dx], [by, dy], color=HI, lw=1.4)
    ax.plot([0, dx], [0, dy], color=HI, lw=1.4, ls="-")
    r2, r3 = math.sqrt(2), math.sqrt(3)
    ax.add_patch(Arc((0, 0), 2 * r2, 2 * r2, theta1=0, theta2=45, color=ACC, lw=1, ls="--"))
    ax.add_patch(Arc((0, 0), 2 * r3, 2 * r3, theta1=0, theta2=math.degrees(math.atan2(dy, dx)), color=HI, lw=1, ls="--"))
    ax.plot([r2], [0], "o", color=ACC, ms=4); ax.plot([r3], [0], "o", color=HI, ms=4)
    ax.text(r2, 0.2, "P", ha="center", color=ACC); ax.text(r3 + 0.05, 0.2, "Q", ha="center", color=HI)
    ax.text(r2 - 0.02, -0.62, "$\\sqrt{2}$", ha="center", color=ACC, fontsize=11)
    ax.text(r3 + 0.08, -0.62, "$\\sqrt{3}$", ha="center", color=HI, fontsize=11)
    for (x, y, t, dxo, dyo) in [(0, 0, "O", -0.14, 0.12), (1, 0, "A", 0.1, 0.12), (1, 1, "B", 0.12, 0.02), (0, 1, "C", -0.14, 0.02), (dx, dy, "D", -0.02, 0.14)]:
        ax.text(x + dxo, y + dyo, t, ha="center", color=INK, fontsize=9, weight="bold")
    ax.text(0.28, 0.62, "$\\sqrt{2}$", color=ACC, fontsize=10)
    ax.text(0.5, 1.22, "1", color=HI, fontsize=9)
    ax.set_xlim(-1.6, 3.6); ax.set_ylim(-0.9, 1.9); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch01_fig02_locating_root2_root3.png")


# Fig 3: square root spiral
def fig_spiral():
    import math
    fig, ax = plt.subplots(figsize=(4.4, 4.4))
    pts = [(0.0, 0.0), (1.0, 0.0)]
    ang = 0.0
    for n in range(1, 11):
        r = math.sqrt(n)
        ang = math.atan2(pts[-1][1], pts[-1][0])
        px, py = pts[-1]
        nx, ny = px + math.cos(ang + math.pi / 2), py + math.sin(ang + math.pi / 2)
        pts.append((nx, ny))
    for i in range(1, len(pts)):
        ax.plot([0, pts[i][0]], [0, pts[i][1]], color=ACC, lw=1)
        if i >= 2:
            ax.plot([pts[i - 1][0], pts[i][0]], [pts[i - 1][1], pts[i][1]], color=HI, lw=1.4)
    for i in range(1, len(pts)):
        x, y = pts[i]
        ax.plot([x], [y], "o", color=INK, ms=2.5)
        ax.text(x * 1.08, y * 1.08, f"$P_{{{i}}}$", fontsize=8, ha="center", va="center")
        lab = "1" if i == 1 else f"$\\sqrt{{{i}}}$"
        ax.text(x * 0.55 + 0.0, y * 0.55, lab, fontsize=7.5, color=ACC, ha="center", va="center",
                bbox=dict(fc="white", ec="none", pad=0.3))
    ax.text(-0.15, -0.2, "O", fontsize=9, weight="bold")
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch01_fig03_square_root_spiral.png")


# Fig 4: sqrt 5 on the number line
def fig_root5():
    import math
    fig, ax = plt.subplots(figsize=(6.0, 2.5))
    number_line(ax, -1, 3)
    ax.plot([2, 2], [0, 1], color=HI, lw=1.4)
    ax.plot([0, 2], [0, 1], color=ACC, lw=1.4)
    r5 = math.sqrt(5)
    ax.add_patch(Arc((0, 0), 2 * r5, 2 * r5, theta1=0, theta2=math.degrees(math.atan2(1, 2)), color=ACC, lw=1, ls="--"))
    ax.plot([r5], [0], "o", color=ACC, ms=4)
    ax.text(r5 + 0.02, 0.2, "C", ha="center", color=ACC, weight="bold")
    ax.text(r5, -0.62, "$\\sqrt{5}$", ha="center", color=ACC, fontsize=11)
    ax.text(-0.14, 0.12, "O", weight="bold"); ax.text(1.8, 0.1, "A", weight="bold"); ax.text(2.08, 1.02, "B", weight="bold")
    ax.text(1.84, 0.45, "1", color=HI); ax.text(0.8, 0.55, "$\\sqrt{5}$", color=ACC, fontsize=10)
    ax.text(1.0, 0.14, "2", color=INK, fontsize=9)
    ax.set_xlim(-1.6, 3.6); ax.set_ylim(-0.9, 1.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch01_fig04_locating_root5.png")


# Fig 5: geometric construction of sqrt(x), drawn for x = 3.5 (general) and x = 9.3 (exercise)
def fig_sqrt_x(x, name, scale_note):
    import math
    fig, ax = plt.subplots(figsize=(6.2, 3.0))
    A, B, Cc = 0.0, x, x + 1
    O = (A + Cc) / 2
    r = (x + 1) / 2
    ax.plot([A - 0.3, Cc + 0.6], [0, 0], color=INK, lw=1)
    ax.add_patch(Arc((O, 0), 2 * r, 2 * r, theta1=0, theta2=180, color=ACC, lw=1.2))
    h = math.sqrt(x)
    ax.plot([B, B], [0, h], color=HI, lw=1.6)
    ax.plot([O, B], [0, h], color=ACC, lw=0.9, ls="--")
    # arc from B with radius BD down to the line (point E)
    ax.add_patch(Arc((B, 0), 2 * h, 2 * h, theta1=0, theta2=90, color=HI, lw=1, ls=":"))
    ax.plot([B + h], [0], "o", color=HI, ms=4)
    for px, t in [(A, "A"), (B, "B"), (Cc, "C"), (O, "O"), (B + h, "E")]:
        ax.plot([px], [0], "o", color=INK, ms=2.5)
        ax.text(px, -0.35 * r / 2.25, t, ha="center", weight="bold", fontsize=9)
    ax.text(B, h + 0.12 * r / 2.25, "D", ha="center", weight="bold", fontsize=9)
    ax.text((A + B) / 2, 0.1 * r / 2.25, f"{x:g} units", ha="center", fontsize=8.5)
    ax.text((B + Cc) / 2, -0.35 * r / 2.25, "1", ha="center", fontsize=8.5, color=HI)
    ax.text(B - 0.1 * r / 2.25, h / 2, f"$\\sqrt{{{x:g}}}$", fontsize=11, color=HI, ha="right")
    ax.set_aspect("equal"); ax.axis("off")
    if scale_note:
        ax.set_title(scale_note, fontsize=8, color="#5D6B7A")
    save(fig, name)


# Fig 6: long division showing remainders for 1/7
def fig_remainders():
    fig, ax = plt.subplots(figsize=(6.2, 1.9))
    rem = [1, 3, 2, 6, 4, 5, 1]
    digs = [1, 4, 2, 8, 5, 7]
    for i, r in enumerate(rem):
        ax.add_patch(FancyBboxPatch((i * 0.9, 0), 0.7, 0.6, boxstyle="round,pad=0.02,rounding_size=0.1",
                                    fc=SOFT if i < 6 else "#FDF7EA", ec=ACC if i < 6 else HI, lw=1))
        ax.text(i * 0.9 + 0.35, 0.3, str(r), ha="center", va="center", fontsize=11, color=INK)
        if i < 6:
            ax.text(i * 0.9 + 0.35, 0.95, str(digs[i]), ha="center", va="center", fontsize=11, color=ACC, weight="bold")
    ax.text(-0.5, 0.3, "Remainder", ha="right", va="center", fontsize=9)
    ax.text(-0.5, 0.95, "Quotient digit", ha="right", va="center", fontsize=9)
    ax.annotate("remainder 1 again:\nthe block repeats", xy=(6 * 0.9 + 0.35, 0.62), xytext=(6.6, 1.35),
                fontsize=8, color=HI, ha="center", arrowprops=dict(arrowstyle="->", color=HI))
    ax.set_xlim(-2.6, 7.4); ax.set_ylim(-0.1, 1.8); ax.axis("off")
    save(fig, "ch01_fig07_remainders_1_by_7.png")


if __name__ == "__main__":
    fig_sets()
    fig_root2_root3()
    fig_spiral()
    fig_root5()
    fig_sqrt_x(3.5, "ch01_fig05_sqrt_x_construction.png", "")
    fig_sqrt_x(9.3, "ch01_fig06_sqrt_9_3.png", "")
    fig_remainders()
