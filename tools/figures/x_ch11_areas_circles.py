"""Figures for Class X Mathematics, Chapter 11: Areas Related to Circles.
Run: python x_ch11_areas_circles.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Polygon, Rectangle, Wedge

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY, SHADE = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794", "#BFD3E6"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def U(deg):
    t = np.radians(deg)
    return np.array([np.cos(t), np.sin(t)])


def P(*xy):
    return np.array(xy, dtype=float)


def seg(ax, a, b, color=INK, lw=1.3, ls="-"):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls=ls)


def lab(ax, p, s, off, size=10, color=INK):
    ax.annotate(s, p, textcoords="offset points", xytext=off, ha="center", va="center", fontsize=size, color=color)


def segment_patch(c, r, a1, a2, **kw):
    """Region between the chord and the arc from angle a1 to a2 (degrees, counter-clockwise)."""
    t = np.radians(np.linspace(a1, a2, 120))
    pts = np.c_[c[0] + r * np.cos(t), c[1] + r * np.sin(t)]
    return Polygon(pts, closed=True, **kw)


def finish(ax, pad=0.12):
    ax.set_aspect("equal"); ax.axis("off"); ax.margins(pad)


# Fig 11.1: minor and major sectors; minor and major segments
def fig_sector_segment():
    fig, axs = plt.subplots(1, 2, figsize=(6.6, 3.0))
    O, r = P(0, 0), 1.5
    ax = axs[0]
    ax.add_patch(Wedge(O, r, 30, 110, fc=SHADE, ec=ACC, lw=1.3))
    ax.add_patch(Circle(O, r, fc="none", ec=ACC, lw=1.3))
    A, B = O + r * U(30), O + r * U(110)
    seg(ax, O, A); seg(ax, O, B)
    ax.add_patch(Arc(O, 0.6, 0.6, theta1=30, theta2=110, color=HI))
    ax.text(0.05, 0.42, r"$\theta$", color=HI, ha="center")
    lab(ax, A, "A", (8, 4)); lab(ax, B, "B", (-6, 8)); lab(ax, O, "O", (0, -11))
    lab(ax, O + r * U(70), "P", (0, 10)); lab(ax, O + r * U(250), "Q", (0, -10))
    ax.text(0, 1.0, "minor\nsector", ha="center", fontsize=8, color=ACC)
    ax.text(0, -0.75, "major sector", ha="center", fontsize=8, color=GREY)
    finish(ax)
    ax = axs[1]
    ax.add_patch(Circle(O, r, fc="none", ec=ACC, lw=1.3))
    ax.add_patch(segment_patch(O, r, 20, 160, fc=SHADE, ec="none"))
    A, B = O + r * U(20), O + r * U(160)
    seg(ax, A, B)
    lab(ax, A, "A", (8, 0)); lab(ax, B, "B", (-8, 0))
    lab(ax, O + r * U(90), "P", (0, 10)); lab(ax, O + r * U(270), "Q", (0, -10))
    ax.plot(*O, "o", ms=3, color=INK); lab(ax, O, "O", (0, -11))
    ax.text(0, 0.95, "minor segment", ha="center", fontsize=8, color=ACC)
    ax.text(0, -0.75, "major segment", ha="center", fontsize=8, color=GREY)
    finish(ax)
    save(fig, "ch11_fig01_sector_segment.png")


# Fig 11.2: Example 2 - segment AYB with angle AOB = 120 degrees; OM perpendicular to AB
def fig_example2():
    fig, ax = plt.subplots(figsize=(3.4, 3.2))
    O, r = P(0, 0), 1.6
    A, B = O + r * U(210), O + r * U(330)
    M = (A + B) / 2
    ax.add_patch(Circle(O, r, fc="none", ec=ACC, lw=1.3))
    ax.add_patch(segment_patch(O, r, 210, 330, fc=SHADE, ec="none"))
    seg(ax, O, A); seg(ax, O, B); seg(ax, A, B); seg(ax, O, M, GREY, 1.0, "--")
    ax.add_patch(Arc(O, 0.6, 0.6, theta1=210, theta2=330, color=HI))
    ax.text(0.34, -0.42, "120°", ha="left", fontsize=8.5, color=HI)
    lab(ax, O, "O", (0, 9)); lab(ax, A, "A", (-8, -4)); lab(ax, B, "B", (8, -4)); lab(ax, M, "M", (-9, 8))
    lab(ax, O + r * U(270), "Y", (0, -10))
    ax.text(-0.75, -0.25, "21 cm", fontsize=8, color=ACC, rotation=30)
    finish(ax)
    save(fig, "ch11_fig02_example2.png")


# Fig 11.3: Ex 11.1 Q8 - a horse tied at a corner of a 15 m square field with a 5 m (and 10 m) rope
def fig_horse():
    fig, ax = plt.subplots(figsize=(3.4, 3.4))
    ax.add_patch(Rectangle((0, 0), 15, 15, fc="#EEF5E6", ec=INK, lw=1.3))
    ax.add_patch(Wedge((0, 0), 10, 0, 90, fc="#F6EEDC", ec=HI, lw=1.0, ls="--"))
    ax.add_patch(Wedge((0, 0), 5, 0, 90, fc=SHADE, ec=ACC, lw=1.3))
    ax.plot(0, 0, "o", ms=5, color=INK)
    ax.text(2.0, 1.6, "5 m rope", fontsize=8, color=ACC)
    ax.text(6.0, 5.6, "10 m rope", fontsize=8, color=HI)
    ax.text(7.5, -1.3, "15 m", ha="center", fontsize=9)
    ax.text(-0.8, -0.8, "peg", fontsize=8, ha="center")
    finish(ax, 0.05)
    save(fig, "ch11_fig03_horse.png")


# Fig 11.4: Ex 11.1 Q9 - brooch with 5 diameters making 10 equal sectors
def fig_brooch():
    fig, ax = plt.subplots(figsize=(2.8, 2.8))
    r = 1.75
    ax.add_patch(Circle((0, 0), r, fc="#F5F5F5", ec=GREY, lw=2.0))
    for k in range(5):
        a = 18 + 36 * k
        seg(ax, r * U(a), r * U(a + 180), GREY, 1.6)
    ax.add_patch(Wedge((0, 0), r, 18, 54, fc=SHADE, ec="none", alpha=0.9))
    ax.text(0, -2.15, "diameter 35 mm", ha="center", fontsize=8.5)
    finish(ax)
    save(fig, "ch11_fig04_brooch.png")


# Fig 11.5: Ex 11.1 Q10 - umbrella with 8 equally spaced ribs
def fig_umbrella():
    fig, ax = plt.subplots(figsize=(2.8, 2.8))
    r = 1.5
    pts = [r * U(22.5 + 45 * k) for k in range(8)]
    ax.add_patch(Polygon(np.array(pts), closed=True, fc="#F3E0E8", ec=INK, lw=1.2))
    for p in pts:
        seg(ax, P(0, 0), p, INK, 1.0)
    ax.add_patch(Polygon(np.array([[0, 0], pts[0], pts[1]]), closed=True, fc=SHADE, ec="none", alpha=0.9))
    ax.text(0, -1.95, "radius 45 cm, 8 ribs", ha="center", fontsize=8.5)
    finish(ax)
    save(fig, "ch11_fig05_umbrella.png")


# Fig 11.6: Ex 11.1 Q11 - two car wipers, each sweeping 115 degrees with a 25 cm blade
def fig_wipers():
    fig, ax = plt.subplots(figsize=(4.4, 2.2))
    for cx in (0, 5.6):
        ax.add_patch(Wedge((cx, 0), 2.5, 32.5, 147.5, fc=SHADE, ec=ACC, lw=1.2))
        ax.plot(cx, 0, "o", ms=4, color=INK)
        ax.add_patch(Arc((cx, 0), 1.0, 1.0, theta1=32.5, theta2=147.5, color=HI))
        ax.text(cx, 0.75, "115°", ha="center", fontsize=8.5, color=HI)
    ax.text(2.8, -0.45, "blade 25 cm", ha="center", fontsize=8.5)
    ax.plot([-2.8, 8.4], [0, 0], color=GREY, lw=0.8)
    finish(ax, 0.06)
    save(fig, "ch11_fig06_wipers.png")


# Fig 11.7: Ex 11.1 Q12 - lighthouse spreading red light over an 80 degree sector, 16.5 km
def fig_lighthouse():
    fig, ax = plt.subplots(figsize=(3.6, 2.6))
    ax.add_patch(Wedge((0, 0), 3.3, -40, 40, fc="#F7C9C3", ec="#B03A2E", lw=1.2))
    ax.add_patch(Polygon([[-0.25, -0.3], [0.25, -0.3], [0.12, 0.5], [-0.12, 0.5]], closed=True, fc="white", ec=INK, lw=1.2))
    ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=-40, theta2=40, color=HI))
    ax.text(0.85, 0.05, "80°", fontsize=9, color=HI, va="center")
    ax.text(1.8, -1.85, "16.5 km", fontsize=9, color="#B03A2E", rotation=-40)
    finish(ax, 0.08)
    save(fig, "ch11_fig07_lighthouse.png")


# Fig 11.8: Ex 11.1 Q13 - round table cover with six equal designs (segments)
def fig_table_cover():
    fig, ax = plt.subplots(figsize=(2.9, 2.9))
    r = 1.4
    ax.add_patch(Circle((0, 0), r, fc="white", ec=ACC, lw=1.3))
    for k in range(6):
        ax.add_patch(segment_patch(P(0, 0), r, 60 * k, 60 * (k + 1), fc="#F3D9A4", ec="none"))
    hexagon = [r * U(60 * k) for k in range(6)]
    ax.add_patch(Polygon(np.array(hexagon), closed=True, fc="none", ec=INK, lw=1.1))
    seg(ax, P(0, 0), r * U(0), GREY, 1.0, "--")
    ax.text(0.7, -0.18, "28 cm", fontsize=8.5, ha="center", color=ACC)
    finish(ax)
    save(fig, "ch11_fig08_table_cover.png")


# Fig 11.9: Ex 11.1 Q3 - minute hand of 14 cm sweeping for 5 minutes (30 degrees)
def fig_clock():
    fig, ax = plt.subplots(figsize=(2.8, 2.8))
    r = 1.4
    ax.add_patch(Circle((0, 0), r * 1.08, fc="#FAFAFA", ec=INK, lw=1.4))
    for k in range(12):
        ax.plot(*zip(r * 0.95 * U(90 - 30 * k), r * 1.05 * U(90 - 30 * k)), color=INK, lw=1)
    ax.add_patch(Wedge((0, 0), r, 60, 90, fc=SHADE, ec=ACC, lw=1.2))
    seg(ax, P(0, 0), r * U(90), INK, 2.2); seg(ax, P(0, 0), r * U(60), GREY, 1.6, "--")
    ax.text(0.5, 1.45, "5 min", fontsize=8.5, color=ACC)
    ax.text(0, -0.55, "minute hand 14 cm", fontsize=8, ha="center")
    finish(ax, 0.06)
    save(fig, "ch11_fig09_clock.png")


# Fig 11.10: Ex 11.1 Q4 - a chord subtending a right angle at the centre (r = 10 cm)
def fig_right_chord():
    fig, ax = plt.subplots(figsize=(3.0, 3.0))
    O, r = P(0, 0), 1.5
    A, B = O + r * U(0), O + r * U(90)
    ax.add_patch(Wedge(O, r, 90, 360, fc="#F6EEDC", ec="none"))
    ax.add_patch(segment_patch(O, r, 0, 90, fc=SHADE, ec="none"))
    ax.add_patch(Circle(O, r, fc="none", ec=ACC, lw=1.3))
    seg(ax, O, A); seg(ax, O, B); seg(ax, A, B)
    ax.plot(*zip(O + P(0.18, 0), O + P(0.18, 0.18), O + P(0, 0.18)), color=INK, lw=0.8)
    lab(ax, O, "O", (-8, -8)); lab(ax, A, "A", (8, 0)); lab(ax, B, "B", (0, 9))
    ax.text(1.45, 1.4, "minor segment", fontsize=7.5, color=ACC, ha="center")
    ax.text(-0.55, -0.55, "major sector", fontsize=8, color=HI, ha="center")
    ax.text(0.7, -0.18, "10 cm", fontsize=8, color=ACC, ha="center")
    finish(ax)
    save(fig, "ch11_fig10_right_chord.png")


if __name__ == "__main__":
    fig_sector_segment(); fig_example2(); fig_horse(); fig_brooch(); fig_umbrella()
    fig_wipers(); fig_lighthouse(); fig_table_cover(); fig_clock(); fig_right_chord()
