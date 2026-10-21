"""Figures for Class IX Mathematics, Chapter 11: Surface Areas and Volumes (cone, sphere, hemisphere)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Ellipse, Polygon, Wedge

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "CLASS IX Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, MUTED, SAND = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#5D6B7A", "#F6EBD7"
plt.rcParams.update({"font.size": 9, "mathtext.fontset": "cm"})
K = 0.28  # ellipse flattening for circles seen in perspective


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def finish(ax, title=None, pad=0.25):
    ax.set_aspect("equal"); ax.axis("off")
    ax.autoscale_view()
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    ax.set_xlim(x0 - pad, x1 + pad); ax.set_ylim(y0 - pad, y1 + pad)
    if title:
        ax.set_title(title, fontsize=8.5, color=MUTED)


def txt(ax, x, y, t, color=INK, fs=8.5, **kw):
    ax.text(x, y, t, ha="center", va="center", fontsize=fs, color=color, **kw)


def base_ellipse(ax, cx, cy, r, color=ACC, lw=1.3, front=True, back=True, k=None):
    k = K if k is None else k
    if back:
        ax.add_patch(Arc((cx, cy), 2 * r, 2 * r * k, theta1=0, theta2=180, color=color, lw=lw * 0.8, ls="--"))
    if front:
        ax.add_patch(Arc((cx, cy), 2 * r, 2 * r * k, theta1=180, theta2=360, color=color, lw=lw))


def cone(ax, cx, cy, r, h, fill=SOFT, labels=True, show_h=True, show_l=True, names=True, k=None):
    k = K if k is None else k
    V = (cx, cy + h)
    ax.add_patch(Polygon([(cx - r, cy), V, (cx + r, cy)], closed=True, fc=fill, ec="none"))
    ax.add_patch(Ellipse((cx, cy), 2 * r, 2 * r * k, fc=fill, ec="none"))
    ax.plot([cx - r, cx, cx + r], [cy, cy + h, cy], color=ACC, lw=1.3)
    base_ellipse(ax, cx, cy, r, k=k)
    if show_h:
        ax.plot([cx, cx], [cy, cy + h], color=HI, lw=1.1, ls="--")
        ax.plot([cx, cx + r], [cy, cy], color=HI, lw=1.1)
        s = 0.1 * min(r, h) + 0.02
        ax.plot([cx + s, cx + s, cx], [cy, cy + s, cy + s], color=HI, lw=0.9)
    if labels:
        if show_h:
            txt(ax, cx - 0.14, cy + h * 0.45, "$h$")
            txt(ax, cx + r / 2, cy - 0.13, "$r$")
        if show_l:
            txt(ax, cx + r / 2 + 0.16, cy + h / 2 + 0.05, "$l$")
    if names:
        txt(ax, V[0], V[1] + 0.13, "A", weight="bold"); txt(ax, cx - 0.12, cy + 0.08, "B", weight="bold", fs=8)
        txt(ax, cx + r + 0.12, cy, "C", weight="bold")


def sphere(ax, cx, cy, r, fill=SOFT, label=True):
    ax.add_patch(Circle((cx, cy), r, fc=fill, ec=ACC, lw=1.3))
    base_ellipse(ax, cx, cy, r, color=MUTED, lw=1)
    ax.plot([cx], [cy], "o", color=INK, ms=2.5)
    ax.plot([cx, cx + r * math.cos(math.radians(35))], [cy, cy + r * math.sin(math.radians(35))], color=HI, lw=1.1)
    if label:
        txt(ax, cx + 0.45 * r, cy + 0.4 * r, "$r$"); txt(ax, cx - 0.1, cy - 0.1, "O", weight="bold", fs=8)


def hemisphere(ax, cx, cy, r, fill=SOFT, bowl=False):
    th = [math.radians(t) for t in range(180, 361, 3)] if bowl else [math.radians(t) for t in range(0, 181, 3)]
    pts = [(cx + r * math.cos(t), cy + r * math.sin(t)) for t in th]
    ax.add_patch(Polygon(pts, closed=True, fc=fill, ec=ACC, lw=1.3))
    ax.add_patch(Ellipse((cx, cy), 2 * r, 2 * r * K, fc="#D5E3F0" if not bowl else "#FFFFFF", ec=ACC, lw=1.2))
    ax.plot([cx, cx + r], [cy, cy], color=HI, lw=1.1)
    txt(ax, cx + r / 2, cy + 0.1, "$r$")


def cylinder(ax, cx, cy, r, h, fill="none"):
    ax.plot([cx - r, cx - r], [cy, cy + h], color=ACC, lw=1.3)
    ax.plot([cx + r, cx + r], [cy, cy + h], color=ACC, lw=1.3)
    ax.add_patch(Ellipse((cx, cy + h), 2 * r, 2 * r * K, fc="none", ec=ACC, lw=1.3))
    base_ellipse(ax, cx, cy, r)


# ------------------------------------------------------------------ lesson figures
def fig_cone_parts():
    fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.4))
    ax = axs[0]
    cone(ax, 0, 0, 0.8, 1.9)
    finish(ax, "Vertex A, height AB, radius BC, slant height AC")
    ax = axs[1]
    # net of the curved surface: a sector of radius l and arc 2*pi*r
    l, r = 1.6, 0.8
    ang = 360 * r / l
    ax.add_patch(Wedge((0, 0), l, 90 - ang / 2, 90 + ang / 2, fc=SOFT, ec=ACC, lw=1.3))
    txt(ax, 0.35, 0.55, "$l$"); txt(ax, 0, l + 0.18, "arc $= 2\\pi r$")
    finish(ax, "Cut open: a sector of radius $l$")
    ax = axs[2]
    l, r = 1.6, 0.8
    ax.add_patch(Wedge((0, 0), l, 90 - ang / 2, 90 + ang / 2, fc=SOFT, ec=ACC, lw=1.0))
    for k in range(1, 12):
        a = math.radians(90 - ang / 2 + k * ang / 12)
        ax.plot([0, l * math.cos(a)], [0, l * math.sin(a)], color=MUTED, lw=0.6)
    txt(ax, 0, -0.35, "many thin triangles of height $l$", fs=7.5)
    finish(ax, "CSA $= \\frac{1}{2} \\times l \\times 2\\pi r = \\pi r l$")
    save(fig, "ch11_fig01_cone_parts_and_net.png")


def fig_sphere_parts():
    fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.3))
    ax = axs[0]
    sphere(ax, 0, 0, 1.0)
    finish(ax, "Sphere: SA $= 4\\pi r^2$")
    ax = axs[1]
    hemisphere(ax, 0, 0, 1.0)
    finish(ax, "Hemisphere: CSA $= 2\\pi r^2$, TSA $= 3\\pi r^2$")
    ax = axs[2]
    cylinder(ax, 0, -1.0, 1.0, 2.0)
    ax.add_patch(Circle((0, 0), 1.0, fc=SOFT, ec=HI, lw=1.2))
    base_ellipse(ax, 0, 0, 1.0, color=MUTED, lw=0.8)
    txt(ax, 1.25, 0, "$2r$", color=INK)
    ax.annotate("", xy=(1.12, 1.0), xytext=(1.12, -1.0), arrowprops=dict(arrowstyle="<->", color=MUTED, lw=0.8))
    finish(ax, "Cylinder just enclosing a sphere")
    save(fig, "ch11_fig02_sphere_hemisphere.png")


def fig_cone_volume():
    fig, axs = plt.subplots(1, 2, figsize=(5.4, 2.3))
    ax = axs[0]
    cylinder(ax, 0, 0, 0.8, 1.8)
    cone(ax, 0, 0, 0.8, 1.8, fill=SAND, labels=False, show_h=False, names=False)
    txt(ax, 0, -0.45, "same $r$ and same $h$", fs=8)
    finish(ax, "Cone inside a cylinder")
    ax = axs[1]
    for k, frac in enumerate([1 / 3, 2 / 3, 1.0]):
        x = k * 1.25
        cylinder(ax, x, 0, 0.45, 1.3)
        ax.add_patch(Polygon([(x - 0.45, 0), (x + 0.45, 0), (x + 0.45, 1.3 * frac), (x - 0.45, 1.3 * frac)], closed=True, fc=SAND, ec="none", zorder=0))
        txt(ax, x, -0.35, ["1 cone", "2 cones", "3 cones"][k], fs=7.5)
    finish(ax, "Three cones of sand fill the cylinder")
    save(fig, "ch11_fig03_cone_volume.png")


def fig_examples():
    fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.4))
    ax = axs[0]
    cone(ax, 0, 0, 0.35, 2.0, fill="#F3E3A0", labels=False, show_h=True, names=False)
    txt(ax, -0.2, 1.0, "20 cm", fs=7.5, rotation=90); txt(ax, 0.2, -0.2, "2.1 cm", fs=7.5)
    finish(ax, "Example 6: corn cob")
    ax = axs[1]
    ax.add_patch(Polygon([(-1.3, -0.9), (1.3, -0.9), (1.3, 0), (-1.3, 0)], closed=True, fc="#EFEFEF", ec=MUTED, lw=1))
    hemisphere(ax, 0, 0, 1.0, fill="#DCEFD8")
    txt(ax, 0, -0.5, "circumference 17.6 m", fs=7.5)
    finish(ax, "Example 10: hemispherical dome")
    ax = axs[2]
    cone(ax, 0, 0, 1.0, 1.4, fill="#FBE3E0", labels=False, show_h=True, names=False)
    txt(ax, -0.18, 0.7, "$h$"); txt(ax, 0.5, -0.17, "7 m"); txt(ax, 0.7, 0.85, "$l$")
    finish(ax, "Example 16: conical tent")
    save(fig, "ch11_fig04_examples.png")


def fig_exercises():
    fig, axs = plt.subplots(1, 4, figsize=(7.4, 2.4))
    ax = axs[0]
    cone(ax, 0, 0, 0.5, 1.2, labels=False, show_h=True, names=False)
    txt(ax, -0.15, 0.6, "12", fs=8); txt(ax, 0.25, -0.15, "5", fs=8); txt(ax, 0.42, 0.7, "13", fs=8)
    finish(ax, "Ex 11.3 Q7: about 12 cm")
    ax = axs[1]
    cone(ax, 0, 0, 1.2, 0.6, labels=False, show_h=True, names=False, k=0.14)
    txt(ax, -0.12, 0.3, "5", fs=8); txt(ax, 0.6, -0.25, "12", fs=8); txt(ax, 0.72, 0.45, "13", fs=8)
    finish(ax, "Ex 11.3 Q8: about 5 cm")
    ax = axs[2]
    hemisphere(ax, 0, 0, 1.0, fill="#DDE7F0", bowl=True)
    th = [math.radians(t) for t in range(180, 361, 3)]
    ax.plot([1.12 * math.cos(t) for t in th], [1.12 * math.sin(t) for t in th], color=ACC, lw=1.3)
    txt(ax, 0, -1.35, "inner 5 cm, thickness 0.25 cm", fs=7)
    finish(ax, "Ex 11.2 Q8: steel bowl")
    ax = axs[3]
    cone(ax, 0, 0, 1.1, 0.7, fill=SAND, labels=False, show_h=True, names=False, k=0.14)
    txt(ax, -0.25, 0.35, "3 m", fs=7.5); txt(ax, 0.55, -0.27, "5.25 m", fs=7.5)
    finish(ax, "Ex 11.3 Q9: heap of wheat")
    save(fig, "ch11_fig05_exercise_figures.png")


if __name__ == "__main__":
    fig_cone_parts(); fig_sphere_parts(); fig_cone_volume(); fig_examples(); fig_exercises()
