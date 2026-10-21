"""Figures for Class X Mathematics, Chapter 4: Quadratic Equations.
Run: python x_ch04_quadratic_equations.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


# Fig 4.1: the prayer hall, breadth x and length 2x + 1
def fig_hall():
    fig, ax = plt.subplots(figsize=(4.8, 2.6))
    ax.add_patch(Rectangle((0, 0), 5, 2.2, fc=SOFT, ec=ACC, lw=1.4))
    ax.text(2.5, 1.1, "Area = 300 m²", ha="center", va="center", fontsize=11, color=ACC)
    ax.annotate("", xy=(0, -0.35), xytext=(5, -0.35), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
    ax.text(2.5, -0.65, "$(2x + 1)$ m", ha="center", fontsize=11)
    ax.annotate("", xy=(5.35, 0), xytext=(5.35, 2.2), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
    ax.text(5.5, 1.1, "$x$ m", va="center", fontsize=11)
    ax.set_xlim(-0.3, 6.2); ax.set_ylim(-1.0, 2.5); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch04_fig01_prayer_hall.png")


# Fig 4.2: the pole P on a circular park with diameter AB = 13 m (BP = 5, AP = 12)
def fig_park():
    fig, ax = plt.subplots(figsize=(4.4, 4.0))
    r = 6.5
    ax.add_patch(Circle((0, 0), r, fc="#F3F8F1", ec=ACC, lw=1.4))
    A, B = np.array([-r, 0]), np.array([r, 0])
    # P on the circle with BP = 5 and AP = 12: angle APB = 90 degrees.
    px = (12 ** 2 - 5 ** 2) / (2 * 13)  # distance of the foot of P from the centre towards B
    P = np.array([px, np.sqrt(r ** 2 - px ** 2)])
    ax.plot(*zip(A, B), color=INK, lw=1)
    ax.plot(*zip(A, P), color=ACC, lw=1.4)
    ax.plot(*zip(B, P), color=ACC, lw=1.4)
    for pt, lab, off in [(A, "A", (-14, -4)), (B, "B", (6, -4)), (P, "P", (4, 6))]:
        ax.plot(*pt, "o", ms=4, color=HI)
        ax.annotate(lab, pt, textcoords="offset points", xytext=off, fontsize=11, color=INK)
    ax.text(0, -0.7, "AB = 13 m (diameter)", ha="center", fontsize=9)
    # Side labels: (x + 7) above AP, parallel to it; x just inside PB, clear of the circle.
    d_ap = (P - A) / np.linalg.norm(P - A)
    up = np.array([-d_ap[1], d_ap[0]])
    ang = np.degrees(np.arctan2(d_ap[1], d_ap[0]))
    ax.text(*((A + P) / 2 + up * 0.75), "$(x + 7)$ m", fontsize=10, color=ACC,
            ha="center", va="center", rotation=ang, rotation_mode="anchor")
    d_bp = (P - B) / np.linalg.norm(P - B)
    inward = np.array([d_bp[1], -d_bp[0]])
    if inward[0] > 0:
        inward = -inward
    ax.text(*((B + P) / 2 + inward * 0.85), "$x$ m", fontsize=10, color=ACC, ha="center", va="center")
    # right-angle mark at P
    u = (A - P) / np.linalg.norm(A - P) * 0.6
    v = (B - P) / np.linalg.norm(B - P) * 0.6
    ax.plot(*zip(P + u, P + u + v, P + v), color=INK, lw=0.9)
    ax.set_xlim(-7.6, 7.6); ax.set_ylim(-7, 7.2); ax.set_aspect("equal"); ax.axis("off")
    save(fig, "ch04_fig02_pole_in_park.png")


if __name__ == "__main__":
    fig_hall()
    fig_park()
