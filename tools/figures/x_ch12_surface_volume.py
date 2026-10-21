"""Figures for Class X Mathematics, Chapter 12: Surface Areas and Volumes.
Solids are drawn as front views with elliptical rims (hidden edges dashed).
Run: python x_ch12_surface_volume.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Ellipse, Polygon, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT, GREY = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7", "#7A8794"
FILL = "#DCE8F3"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})
K = 0.28  # ellipse squash (vertical/horizontal) for circular rims


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def rim(ax, cx, y, r, front=True, back=True, color=INK, lw=1.2):
    """Ellipse for a circular edge of radius r centred at (cx, y); back half dashed."""
    if back:
        ax.add_patch(Arc((cx, y), 2 * r, 2 * r * K, theta1=0, theta2=180, color=color, lw=lw * 0.8, ls="--"))
    if front:
        ax.add_patch(Arc((cx, y), 2 * r, 2 * r * K, theta1=180, theta2=360, color=color, lw=lw))


def top_rim(ax, cx, y, r, color=INK, lw=1.2, fc=None):
    """A fully visible ellipse (an open or upper face)."""
    ax.add_patch(Ellipse((cx, y), 2 * r, 2 * r * K, fc=fc or "none", ec=color, lw=lw))


def cylinder(ax, cx, y0, r, h, fc=FILL, top=True, bottom_hidden=True, ec=INK):
    ax.add_patch(Rectangle((cx - r, y0), 2 * r, h, fc=fc, ec="none"))
    ax.plot([cx - r, cx - r], [y0, y0 + h], color=ec, lw=1.2)
    ax.plot([cx + r, cx + r], [y0, y0 + h], color=ec, lw=1.2)
    rim(ax, cx, y0, r, back=bottom_hidden, color=ec)
    if top:
        top_rim(ax, cx, y0 + h, r, color=ec, fc=fc)


def cone(ax, cx, y0, r, h, fc=FILL, base_hidden=True, ec=INK):
    """Cone standing on its base at height y0 with apex at y0 + h (h < 0 points down)."""
    ax.add_patch(Polygon([[cx - r, y0], [cx + r, y0], [cx, y0 + h]], closed=True, fc=fc, ec="none"))
    ax.plot([cx - r, cx, cx + r], [y0, y0 + h, y0], color=ec, lw=1.2)
    rim(ax, cx, y0, r, back=base_hidden, color=ec)


def hemisphere(ax, cx, y0, r, down=True, fc=FILL, ec=INK, rim_on=True):
    """Hemisphere with its flat face at height y0, bulging down (or up)."""
    t = np.linspace(180, 360, 100) if down else np.linspace(0, 180, 100)
    xs, ys = cx + r * np.cos(np.radians(t)), y0 + r * np.sin(np.radians(t))
    ax.fill(np.r_[xs, cx + r], np.r_[ys, y0], color=fc, lw=0)
    ax.plot(xs, ys, color=ec, lw=1.2)
    if rim_on:
        rim(ax, cx, y0, r, color=ec)


def dim_v(ax, x, y0, y1, text, side=1, color=ACC):
    ax.annotate("", xy=(x, y0), xytext=(x, y1), arrowprops=dict(arrowstyle="<->", color=color, lw=0.9), annotation_clip=False)
    ax.text(x + 0.08 * side, (y0 + y1) / 2, text, ha="left" if side > 0 else "right", va="center", fontsize=8.5, color=color)


def dim_h(ax, x0, x1, y, text, color=ACC):
    ax.annotate("", xy=(x0, y), xytext=(x1, y), arrowprops=dict(arrowstyle="<->", color=color, lw=0.9), annotation_clip=False)
    ax.text((x0 + x1) / 2, y - 0.12, text, ha="center", va="top", fontsize=8.5, color=color)


def finish(ax, pad=0.1):
    ax.set_aspect("equal"); ax.axis("off"); ax.margins(pad)


# Fig 12.1: the basic solids
def fig_basic():
    fig, ax = plt.subplots(figsize=(7.2, 2.0))
    # cuboid
    ax.add_patch(Polygon([[0, 0], [1.6, 0], [1.6, 1.1], [0, 1.1]], closed=True, fc=FILL, ec=INK, lw=1.2))
    ax.add_patch(Polygon([[0, 1.1], [0.4, 1.4], [2.0, 1.4], [1.6, 1.1]], closed=True, fc="#C9DBEC", ec=INK, lw=1.2))
    ax.add_patch(Polygon([[1.6, 0], [2.0, 0.3], [2.0, 1.4], [1.6, 1.1]], closed=True, fc="#B9CFE4", ec=INK, lw=1.2))
    cylinder(ax, 3.0, 0, 0.5, 1.3)
    cone(ax, 4.6, 0, 0.6, 1.4)
    t = np.linspace(0, 360, 200)
    ax.add_patch(plt.Circle((6.2, 0.65), 0.65, fc=FILL, ec=INK, lw=1.2))
    rim(ax, 6.2, 0.65, 0.65)
    hemisphere(ax, 7.8, 0.65, 0.65, down=True)
    top_rim(ax, 7.8, 0.65, 0.65, fc=FILL)
    for x, n in [(1.0, "cuboid"), (3.0, "cylinder"), (4.6, "cone"), (6.2, "sphere"), (7.8, "hemisphere")]:
        ax.text(x, -0.45, n, ha="center", fontsize=8.5)
    finish(ax, 0.04)
    save(fig, "ch12_fig01_basic_solids.png")


# Fig 12.2: Example 1 - a top: cone on a hemisphere, total height 5 cm, diameter 3.5 cm
def fig_top():
    fig, ax = plt.subplots(figsize=(2.6, 3.4))
    r = 1.75
    hemisphere(ax, 0, 0, r, down=True)
    cone(ax, 0, 0, r, 3.25, base_hidden=True)
    dim_v(ax, 2.3, -r, 3.25, "5 cm")
    dim_h(ax, -r, r, -2.25, "3.5 cm")
    finish(ax)
    save(fig, "ch12_fig02_top.png")


# Fig 12.3: Example 2 - a cube of edge 5 cm with a hemisphere of diameter 4.2 cm on top
def fig_block():
    fig, ax = plt.subplots(figsize=(3.0, 3.0))
    a, d = 5.0, 0.9
    ax.add_patch(Polygon([[0, 0], [a, 0], [a, a], [0, a]], closed=True, fc=FILL, ec=INK, lw=1.2))
    ax.add_patch(Polygon([[0, a], [d, a + d * 0.7], [a + d, a + d * 0.7], [a, a]], closed=True, fc="#C9DBEC", ec=INK, lw=1.2))
    ax.add_patch(Polygon([[a, 0], [a + d, d * 0.7], [a + d, a + d * 0.7], [a, a]], closed=True, fc="#B9CFE4", ec=INK, lw=1.2))
    hemisphere(ax, (a + d) / 2, a + d * 0.35, 2.1, down=False, fc="#F3E3C3")
    dim_h(ax, 0, a, -0.3, "5 cm")
    ax.text((a + d) / 2, a + 2.85, "diameter 4.2 cm", ha="center", fontsize=8.5, color=ACC)
    finish(ax)
    save(fig, "ch12_fig03_block.png")


# Fig 12.4: Example 3 - toy rocket: cone (diameter 5 cm, height 6 cm) on a cylinder (diameter 3 cm, height 20 cm)
def fig_rocket():
    fig, ax = plt.subplots(figsize=(2.4, 4.2))
    s = 0.2
    cylinder(ax, 0, 0, 1.5 * s * 3, 20 * s, fc="#F7E7A8", top=False)
    cone(ax, 0, 20 * s, 2.5 * s * 3, 6 * s, fc="#F6C08F", base_hidden=False)
    rim(ax, 0, 20 * s, 2.5 * s * 3, back=False)
    dim_v(ax, 1.9, 0, 20 * s, "20 cm")
    dim_v(ax, 1.9, 20 * s, 26 * s, "6 cm")
    ax.text(0, -0.55, "diameter 3 cm", ha="center", fontsize=8, color=ACC)
    ax.text(0, 26 * s + 0.35, "cone base diameter 5 cm", ha="center", fontsize=8, color=ACC)
    finish(ax)
    save(fig, "ch12_fig04_rocket.png")


# Fig 12.5: Example 4 - bird-bath: cylinder with a hemispherical depression at the top
def fig_birdbath():
    fig, ax = plt.subplots(figsize=(2.6, 3.6))
    r, h = 0.6, 2.9
    cylinder(ax, 0, 0, r, h)
    hemisphere(ax, 0, h, r, down=True, fc="#BFD9EC", rim_on=False)
    top_rim(ax, 0, h, r)
    dim_v(ax, 1.0, 0, h, "1.45 m")
    ax.text(0, -0.45, "radius 30 cm", ha="center", fontsize=8.5, color=ACC)
    finish(ax)
    save(fig, "ch12_fig05_birdbath.png")


# Fig 12.6: Ex 12.1 Q6 - capsule: cylinder with two hemispherical ends (length 14 mm, diameter 5 mm)
def fig_capsule():
    fig, ax = plt.subplots(figsize=(3.8, 1.6))
    r, L = 0.5, 1.8
    ax.add_patch(Rectangle((-L / 2, -r), L, 2 * r, fc="#F3C6C6", ec="none"))
    ax.plot([-L / 2, L / 2], [r, r], color=INK, lw=1.2); ax.plot([-L / 2, L / 2], [-r, -r], color=INK, lw=1.2)
    for sgn in (-1, 1):
        t = np.linspace(-90, 90, 60) if sgn > 0 else np.linspace(90, 270, 60)
        xs, ys = sgn * L / 2 + r * np.cos(np.radians(t)), r * np.sin(np.radians(t))
        ax.fill(xs, ys, color="#F3C6C6", lw=0)
        ax.plot(xs, ys, color=INK, lw=1.2)
        ax.plot([sgn * L / 2, sgn * L / 2], [-r, r], color=GREY, lw=0.8, ls="--")
    dim_h(ax, -L / 2 - r, L / 2 + r, -0.75, "14 mm")
    dim_v(ax, L / 2 + r + 0.25, -r, r, "5 mm")
    finish(ax, 0.06)
    save(fig, "ch12_fig06_capsule.png")


# Fig 12.7: Ex 12.1 Q7 - tent: cylinder (height 2.1 m, diameter 4 m) with a conical top (slant height 2.8 m)
def fig_tent():
    fig, ax = plt.subplots(figsize=(3.4, 3.2))
    r, h = 2.0, 2.1
    hc = np.sqrt(2.8 ** 2 - r ** 2)
    cylinder(ax, 0, 0, r, h, fc="#E7F0DA", top=False)
    cone(ax, 0, h, r, hc, fc="#E7F0DA", base_hidden=True)
    dim_v(ax, 2.5, 0, h, "2.1 m")
    ax.text(1.25, h + hc / 2 + 0.1, "2.8 m", fontsize=8.5, color=ACC, rotation=-np.degrees(np.arctan2(hc, r)))
    dim_h(ax, -r, r, -0.75, "4 m")
    finish(ax)
    save(fig, "ch12_fig07_tent.png")


# Fig 12.8: Ex 12.1 Q8 - a cylinder (height 2.4 cm, diameter 1.4 cm) with a conical cavity of the same size
def fig_cavity():
    fig, ax = plt.subplots(figsize=(2.6, 3.4))
    r, h = 0.7, 2.4
    cylinder(ax, 0, 0, r, h)
    ax.add_patch(Polygon([[-r, h], [r, h], [0, 0]], closed=True, fc="#BFD9EC", ec="none", alpha=0.9))
    ax.plot([-r, 0, r], [h, 0, h], color=INK, lw=1.0, ls="--")
    top_rim(ax, 0, h, r)
    dim_v(ax, 1.1, 0, h, "2.4 cm")
    ax.text(0, -0.45, "diameter 1.4 cm", ha="center", fontsize=8.5, color=ACC)
    finish(ax)
    save(fig, "ch12_fig08_conical_cavity.png")


# Fig 12.9: Ex 12.1 Q9 - hemispheres scooped out of both ends of a cylinder
def fig_scooped():
    fig, ax = plt.subplots(figsize=(2.6, 3.6))
    r, h = 0.7, 2.0
    cylinder(ax, 0, 0, r, h, top=False)
    hemisphere(ax, 0, h, r, down=True, fc="#BFD9EC", rim_on=False)
    top_rim(ax, 0, h, r)
    t = np.linspace(0, 180, 60)
    ax.plot(r * np.cos(np.radians(t)), r * np.sin(np.radians(t)), color=INK, lw=1.0, ls="--")
    dim_v(ax, 1.1, 0, h, "10 cm")
    ax.text(0, -0.45, "radius 3.5 cm", ha="center", fontsize=8.5, color=ACC)
    finish(ax)
    save(fig, "ch12_fig09_scooped.png")


# Fig 12.10: Example 5 - shed: cuboid 15 m x 7 m x 8 m with a half cylinder on top
def fig_shed():
    fig, ax = plt.subplots(figsize=(4.0, 3.0))
    w, h, d = 3.5, 4.0, 2.4
    dx, dy = d * 0.8, d * 0.45
    ax.add_patch(Polygon([[0, 0], [w, 0], [w, h], [0, h]], closed=True, fc=FILL, ec=INK, lw=1.2))
    ax.add_patch(Polygon([[w, 0], [w + dx, dy], [w + dx, h + dy], [w, h]], closed=True, fc="#C9DBEC", ec=INK, lw=1.2))
    t = np.linspace(0, 180, 80)
    xs, ys = w / 2 + (w / 2) * np.cos(np.radians(t)), h + (w / 2) * np.sin(np.radians(t))
    ax.fill(xs, ys, color="#E5EEF7", lw=0); ax.plot(xs, ys, color=INK, lw=1.2)
    ax.plot(xs + dx, ys + dy, color=INK, lw=1.0)
    ax.plot([w / 2, w / 2 + dx], [h + w / 2, h + w / 2 + dy], color=INK, lw=1.0)
    ax.plot([w, w + dx], [h, h + dy], color=INK, lw=1.0)
    dim_h(ax, 0, w, -0.3, "7 m"); dim_v(ax, -0.3, 0, h, "8 m", side=-1)
    ax.text(w + dx / 2 + 0.25, dy / 2 - 0.1, "15 m", fontsize=8.5, color=ACC, rotation=29)
    finish(ax)
    save(fig, "ch12_fig10_shed.png")


# Fig 12.11: Example 6 - a juice glass with a raised hemispherical bottom
def fig_glass():
    fig, ax = plt.subplots(figsize=(2.4, 3.6))
    r, h = 1.25, 5.0
    s = 0.6
    cylinder(ax, 0, 0, r * s, h * s, fc="#FDEBC8")
    hemisphere(ax, 0, 0, r * s, down=False, fc="white", rim_on=False)
    dim_v(ax, r * s + 0.3, 0, h * s, "10 cm")
    ax.text(0, -0.5, "inner diameter 5 cm", ha="center", fontsize=8.5, color=ACC)
    finish(ax)
    save(fig, "ch12_fig11_glass.png")


# Fig 12.12: Example 7 - a toy (cone on a hemisphere) in a circumscribing cylinder
def fig_toy_cylinder():
    fig, ax = plt.subplots(figsize=(2.6, 3.4))
    r = 1.0
    ax.add_patch(Rectangle((-r, -r), 2 * r, 2 * r, fc="none", ec=GREY, lw=1.0, ls="--"))
    hemisphere(ax, 0, 0, r, down=True)
    cone(ax, 0, 0, r, r)
    for (x, y, n) in [(0, r, "A"), (-r, 0, "B"), (r, 0, "C"), (0, -r, "P"), (0, 0, "O")]:
        ax.annotate(n, (x, y), textcoords="offset points", xytext=(0 if x == 0 else 9 * np.sign(x), 8 if y >= 0 and x == 0 else (-9 if y < 0 else 0)),
                    ha="center", va="center", fontsize=9.5)
    ax.text(-r, r + 0.12, "E", fontsize=9, ha="center"); ax.text(r, r + 0.12, "F", fontsize=9, ha="center")
    ax.text(-r, -r - 0.2, "H", fontsize=9, ha="center"); ax.text(r, -r - 0.2, "G", fontsize=9, ha="center")
    finish(ax)
    save(fig, "ch12_fig12_toy_in_cylinder.png")


# Fig 12.13: Ex 12.1 Q1 - two cubes of edge 4 cm joined end to end
def fig_two_cubes():
    fig, ax = plt.subplots(figsize=(3.6, 2.0))
    a, d = 1.6, 0.6
    for x0 in (0, a):
        ax.add_patch(Polygon([[x0, 0], [x0 + a, 0], [x0 + a, a], [x0, a]], closed=True, fc=FILL, ec=INK, lw=1.2))
        ax.add_patch(Polygon([[x0, a], [x0 + d, a + d * 0.6], [x0 + a + d, a + d * 0.6], [x0 + a, a]], closed=True, fc="#C9DBEC", ec=INK, lw=1.2))
    ax.add_patch(Polygon([[2 * a, 0], [2 * a + d, d * 0.6], [2 * a + d, a + d * 0.6], [2 * a, a]], closed=True, fc="#B9CFE4", ec=INK, lw=1.2))
    dim_h(ax, 0, 2 * a, -0.25, "8 cm"); dim_v(ax, -0.25, 0, a, "4 cm", side=-1)
    finish(ax)
    save(fig, "ch12_fig13_two_cubes.png")


# Fig 12.14: Ex 12.1 Q2 - vessel: hollow hemisphere (diameter 14 cm) with a hollow cylinder; total height 13 cm
def fig_vessel():
    fig, ax = plt.subplots(figsize=(2.8, 3.4))
    r = 1.4
    hemisphere(ax, 0, 0, r, down=True, rim_on=False)
    cylinder(ax, 0, 0, r, 1.2, top=True, bottom_hidden=False)
    rim(ax, 0, 0, r, front=False)
    dim_v(ax, r + 0.35, -r, 1.2, "13 cm")
    dim_h(ax, -r, r, -r - 0.35, "14 cm")
    finish(ax)
    save(fig, "ch12_fig14_vessel.png")


# Fig 12.15: Ex 12.2 Q4 - pen stand: cuboid with four conical depressions
def fig_pen_stand():
    fig, ax = plt.subplots(figsize=(4.0, 2.2))
    w, h, d = 4.5, 1.05, 3.0
    dx, dy = d * 0.55, d * 0.3
    ax.add_patch(Polygon([[0, 0], [w, 0], [w, h], [0, h]], closed=True, fc="#E8D5B5", ec=INK, lw=1.2))
    ax.add_patch(Polygon([[0, h], [dx, h + dy], [w + dx, h + dy], [w, h]], closed=True, fc="#F1E3C9", ec=INK, lw=1.2))
    ax.add_patch(Polygon([[w, 0], [w + dx, dy], [w + dx, h + dy], [w, h]], closed=True, fc="#D9C29C", ec=INK, lw=1.2))
    for k in range(4):
        cx = 0.9 + 0.95 * k + dx * 0.5
        top_rim(ax, cx, h + dy * 0.5, 0.22, fc="#8B6F47")
    ax.text(w / 2, -0.35, "15 cm", ha="center", fontsize=8.5, color=ACC)
    ax.text(w + dx / 2 + 0.25, dy / 2 - 0.1, "10 cm", fontsize=8.5, color=ACC, rotation=28)
    ax.text(-0.15, h / 2, "3.5 cm", fontsize=8.5, color=ACC, ha="right", va="center")
    finish(ax, 0.05)
    save(fig, "ch12_fig15_pen_stand.png")


# Fig 12.16: Ex 12.2 Q7 - cone on a hemisphere placed in a cylinder full of water
def fig_water():
    fig, ax = plt.subplots(figsize=(2.6, 3.6))
    r = 1.0
    ax.add_patch(Rectangle((-r, -r), 2 * r, 3 * r, fc="#CFE3F2", ec="none"))
    ax.plot([-r, -r], [-r, 2 * r], color=INK, lw=1.2); ax.plot([r, r], [-r, 2 * r], color=INK, lw=1.2)
    rim(ax, 0, -r, r)
    top_rim(ax, 0, 2 * r, r)
    hemisphere(ax, 0, 0, r, down=True, fc="#F3E3C3")
    cone(ax, 0, 0, r, 2 * r, fc="#F3E3C3")
    dim_v(ax, r + 0.25, -r, 2 * r, "180 cm")
    ax.text(0, -r - 0.45, "radius 60 cm", ha="center", fontsize=8.5, color=ACC)
    finish(ax)
    save(fig, "ch12_fig16_cone_hemisphere_in_cylinder.png")


# Fig 12.17: Ex 12.2 Q8 - spherical glass vessel with a cylindrical neck
def fig_flask():
    fig, ax = plt.subplots(figsize=(2.4, 3.6))
    R, r, L = 1.0, 0.24, 0.95
    ax.add_patch(plt.Circle((0, 0), R, fc="#E3F0F8", ec=INK, lw=1.2))
    neck_y = np.sqrt(R ** 2 - r ** 2)
    ax.add_patch(Rectangle((-r, neck_y), 2 * r, L, fc="#E3F0F8", ec="none"))
    ax.plot([-r, -r], [neck_y, neck_y + L], color=INK, lw=1.2); ax.plot([r, r], [neck_y, neck_y + L], color=INK, lw=1.2)
    top_rim(ax, 0, neck_y + L, r)
    dim_v(ax, r + 0.2, neck_y, neck_y + L, "8 cm")
    dim_h(ax, -R, R, -R - 0.2, "8.5 cm")
    ax.text(0, neck_y + L + 0.3, "neck diameter 2 cm", ha="center", fontsize=8, color=ACC)
    finish(ax)
    save(fig, "ch12_fig17_flask.png")


if __name__ == "__main__":
    fig_basic(); fig_top(); fig_block(); fig_rocket(); fig_birdbath(); fig_capsule(); fig_tent(); fig_cavity()
    fig_scooped(); fig_shed(); fig_glass(); fig_toy_cylinder(); fig_two_cubes(); fig_vessel(); fig_pen_stand()
    fig_water(); fig_flask()
