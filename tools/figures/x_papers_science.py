"""Figures for the transcribed MBOSE SSLC Science papers (PYQ Papers/Science/figures).
Run: python x_papers_science.py
Diagrams the papers ask students to label are redrawn in the chapter style, with the paper's numbers instead of names.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import x_sci_ch05_life_processes as L  # noqa: E402
from x_sci_ch05_life_processes import (INK, PINK, TAN, GREY, Circle, Ellipse, Rectangle, blob, finish,  # noqa: E402
                                       label, plt, smooth, tube_path)

HERE = os.path.dirname(__file__)
L.OUT = os.path.join(HERE, "..", "..", "Class X Content", "PYQ Papers", "Science", "figures")
os.makedirs(L.OUT, exist_ok=True)
CHAPTER_FIGS = os.path.join(HERE, "..", "..", "Class X Content", "Science", "Generated Content", "figures")


def respiratory(numbers, name):
    """The human respiratory system with numbered pointers: numbers maps a part to its number."""
    fig, ax = plt.subplots(figsize=(5.2, 5.6))
    ax.plot(*smooth([(-0.5, 7.4), (0.0, 7.9), (0.6, 7.8), (0.8, 7.3)], closed=False).T, color=GREY, lw=1.0)
    ax.add_patch(Ellipse((0.3, 7.45), 0.7, 0.25, fc=PINK, ec=INK, lw=0.7))
    tube_path(ax, [(0.15, 7.3), (0.1, 6.8), (0.0, 6.4)], 0.28, PINK)
    ax.add_patch(Rectangle((-0.17, 4.4), 0.34, 2.0, fc="#F7E3DE", ec=INK, lw=0.9))
    for k in range(9):
        ax.plot([-0.17, 0.17], [4.55 + k * 0.2, 4.55 + k * 0.2], color=GREY, lw=1.2)
    tube_path(ax, [(0.0, 4.45), (-0.6, 4.0), (-1.1, 3.6)], 0.22, "#F7E3DE")
    tube_path(ax, [(0.0, 4.45), (0.6, 4.0), (1.1, 3.6)], 0.22, "#F7E3DE")
    blob(ax, [(-0.4, 4.8), (-1.2, 5.1), (-2.2, 4.3), (-2.5, 2.6), (-2.2, 1.5), (-0.6, 1.6), (-0.35, 2.6)], "#F2A7A0", z=0)
    blob(ax, [(0.4, 4.8), (1.2, 5.1), (2.2, 4.3), (2.5, 2.6), (2.2, 1.5), (0.7, 1.6), (0.45, 2.6)], "#F2A7A0", z=0)
    for (x1, y1, x2, y2) in ((-1.1, 3.6, -1.6, 3.0), (-1.1, 3.6, -0.9, 2.6), (-1.6, 3.0, -1.9, 2.4), (-1.6, 3.0, -1.4, 2.2)):
        ax.plot([x1, x2], [y1, y2], color="#B5524A", lw=1.4)
    for x, y in ((-1.9, 2.4), (-1.4, 2.2), (-0.9, 2.6)):
        for dx, dy in ((0, -0.12), (0.1, 0.0), (-0.1, 0.0)):
            ax.add_patch(Circle((x + dx, y + dy), 0.08, fc="#FADBD8", ec="#B5524A", lw=0.6))
    ax.plot(*smooth([(-2.6, 1.2), (-1.3, 1.45), (0, 1.0), (1.3, 1.45), (2.6, 1.2)], closed=False).T, color=INK, lw=2.0)
    for k in range(4):
        ax.plot(*smooth([(-2.7, 4.2 - k * 0.8), (-2.85, 3.8 - k * 0.8), (-2.7, 3.4 - k * 0.8)], closed=False).T, color=TAN, lw=2)
        ax.plot(*smooth([(2.7, 4.2 - k * 0.8), (2.85, 3.8 - k * 0.8), (2.7, 3.4 - k * 0.8)], closed=False).T, color=TAN, lw=2)
    where = {"nasal passage": ((0.3, 7.45), (1.6, 7.8)), "trachea": ((0.17, 5.4), (1.6, 6.1)),
             "lung": ((2.0, 3.0), (3.3, 3.3)), "diaphragm": ((1.3, 1.42), (3.3, 1.4)),
             "bronchus": ((0.6, 4.0), (3.3, 4.8)), "ribs": ((2.75, 2.6), (3.3, 2.4)),
             "pharynx": ((0.08, 6.85), (1.6, 6.95)), "bronchioles": ((-1.6, 3.0), (-3.1, 1.9))}
    for part, num in numbers.items():
        xy, xt = where[part]
        label(ax, xy, f"({num})", xt, ha="left", size=11)
    finish(ax, (-3.2, 4.4), (0.7, 8.1))
    L.save(fig, name)


def copy_chapter(src, name):
    shutil.copy2(os.path.join(CHAPTER_FIGS, src), os.path.join(L.OUT, name))
    print("copied", name)


def sslc2026_q49():
    """A hypermetropic eye as the paper draws it: light from N' focuses behind the retina (no names given)."""
    import x_sci_ch10_eye as E
    from x_sci_ch09_light import R1C, extend, seg

    fig, ax = plt.subplots(figsize=(6.4, 2.1))
    E.eye_outline(ax)
    ret, N, N2, I = 0.96, (-5.0, 0), (-2.9, 0), (1.55, 0)
    ax.plot([N[0], N2[0]], [0, 0], color=INK, lw=1.0)
    for y in (0.3, -0.3):
        seg(ax, N2, (-0.62, y), R1C)
        q = extend((-0.62, y), I, ret)
        seg(ax, (-0.62, y), q, R1C, arrow=False)
        seg(ax, q, I, R1C, arrow=False)
    for pt, t in ((N, "N"), (N2, "N′"), (I, None)):
        ax.plot(*pt, marker="o", ms=4, color=INK)
        if t:
            ax.text(pt[0], -0.2, t, fontsize=10, ha="center", va="top", style="italic")
    finish(ax, (-5.4, 2.0), (-1.15, 1.2))
    L.save(fig, "sslc2026_q49_eye_defect.png")


def sslc2026_q42():
    """Three 2 V cells, a plug key and 5, 8 and 12 ohm resistors, all in series."""
    import x_sci_ch11_electricity as C

    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    C.wire(ax, [(0, 3), (0.9, 3)])
    for k in range(3):
        C.comp(ax, (0.9 + 0.6 * k, 3), (1.5 + 0.6 * k, 3), "cell")
        ax.text(1.2 + 0.6 * k, 2.55, "2 V", fontsize=8.5, ha="center", va="top", color=INK)
    C.wire(ax, [(2.7, 3), (3.2, 3)])
    ax.text(1.8, 3.4, "battery of three cells (6 V)", fontsize=9, ha="center", va="bottom", color=INK)
    C.comp(ax, (3.2, 3), (5.6, 3), "key", text="plug key", at=0.5)
    pts = [(5.6, 1.2), (4.0, 1.2), (2.4, 1.2), (0.8, 1.2)]
    C.wire(ax, [(5.6, 3), pts[0]])
    for i, r in enumerate(("5 Ω", "8 Ω", "12 Ω")):
        C.comp(ax, pts[i], pts[i + 1], "resistor", text=r)
    C.wire(ax, [pts[3], (0, 1.2), (0, 3)])
    finish(ax, (-0.5, 6.1), (0.5, 3.7))
    L.save(fig, "sslc2026_q42_series_circuit.png")


def numbered(chapter_fig, numbers, name):
    """Redraw a chapter figure from x_sci_ch05 with its named labels replaced by the paper's numbers
    (labels not in `numbers` are left out)."""
    real_label, real_save = L.label, L.save

    def label_num(ax, xy, text, xytext, ha="left", size=8.5):
        if text in numbers:
            real_label(ax, xy, f"({numbers[text]})", xytext, ha=ha, size=11)

    L.label = label_num
    L.save = lambda fig, _name: real_save(fig, name)
    try:
        chapter_fig()
    finally:
        L.label, L.save = real_label, real_save


def sslc2023_q17():
    import x_sci_ch09_light as O
    fig, ax = plt.subplots(figsize=(4.8, 2.6))
    O.mirror_case(ax, "concave", -3.0, 0.8, xlim=(-7.6, 1.2), names=("A", "B", "A₁", "B₁"))
    ax.set_xlim(-7.6, 1.2)
    ax.set_ylim(-2.0, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
    L.save(fig, "sslc2023_q17_concave_mirror.png")


def sslc2023_q35():
    fig, ax = plt.subplots(figsize=(4.2, 3.4))
    ax.add_patch(Rectangle((0.5, 0.0), 3.6, 2.4, fc="none", ec=INK, lw=1.4))
    ax.add_patch(Rectangle((0.52, 0.02), 3.56, 1.9, fc="#D9E2EA", ec="none", zorder=0))
    ax.add_patch(Rectangle((1.1, 0.5), 0.35, 2.4, fc="#8C8C8C", ec=INK, lw=1.0))
    ax.add_patch(Rectangle((3.15, 0.5), 0.15, 2.4, fc="#8C8C8C", ec=INK, lw=1.0))
    for k in range(7):
        ax.add_patch(Circle((1.0 + 0.22 * k, 0.12), 0.07, fc="#3A3A3A", ec="none"))
    ax.plot([1.27, 1.27, 2.0], [2.9, 3.4, 3.4], color=INK, lw=1.2)
    ax.plot([3.22, 3.22, 2.6], [2.9, 3.4, 3.4], color=INK, lw=1.2)
    for x, lw, h in ((2.0, 2.0, 0.2), (2.15, 1.2, 0.12), (2.45, 2.0, 0.2), (2.6, 1.2, 0.12)):
        ax.plot([x, x], [3.4 - h, 3.4 + h], color=INK, lw=lw)
    ax.text(2.0, 3.65, "+", ha="center", fontsize=11, color=INK)
    ax.text(2.6, 3.65, "−", ha="center", fontsize=11, color=INK)
    for xy, t, xt in (((1.1, 2.2), "A", (-0.3, 2.2)), ((3.3, 2.2), "B", (4.7, 2.2)),
                      ((3.7, 1.2), "C", (4.7, 1.2)), ((1.0, 0.12), "D", (-0.3, 0.12))):
        ax.annotate(t, xy=xy, xytext=xt, fontsize=12, color=INK, ha="center", va="center",
                    arrowprops=dict(arrowstyle="->", color=INK, lw=0.9))
    ax.text(2.3, -0.45, "Electrorefining of copper", ha="center", fontsize=9.5, style="italic", color=INK)
    finish(ax, (-0.7, 5.1), (-0.7, 3.9))
    L.save(fig, "sslc2023_q35_electrorefining.png")


def sslc2023_q56():
    from matplotlib.patches import FancyBboxPatch
    fig, ax = plt.subplots(figsize=(4.6, 5.0))
    ax.add_patch(FancyBboxPatch((-1.4, 3.8), 2.8, 0.8, boxstyle="round,pad=0.05,rounding_size=0.2", fc="#F2A7A0",
                                ec=INK, lw=1.0))
    ax.add_patch(FancyBboxPatch((-1.4, -1.6), 2.8, 0.8, boxstyle="round,pad=0.05,rounding_size=0.2", fc=TAN,
                                ec=INK, lw=1.0))
    ax.text(0, -1.2, "body organs", ha="center", va="center", fontsize=8.5)
    for (x, y, c) in ((-0.55, 2.0, "#9FB8D9"), (0.55, 2.0, "#E79A93"), (-0.55, 0.9, "#9FB8D9"), (0.55, 0.9, "#E79A93")):
        ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1.0, 1.0, fc=c, ec=INK, lw=1.0))

    def path(pts, col):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=col, lw=2.2)
        ax.annotate("", xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle="->", color=col, lw=2.2))

    path([(-0.55, 0.4), (-0.55, 0.2), (-2.3, 0.2), (-2.3, 4.2), (-1.45, 4.2)], L.BLUE)
    path([(1.45, 4.2), (2.3, 4.2), (2.3, 2.0), (1.05, 2.0)], L.RED)
    path([(0.55, 0.4), (0.55, -0.1), (1.0, -0.1), (1.0, -0.75)], L.RED)
    path([(-1.0, -0.75), (-1.0, -0.2), (-1.6, -0.2), (-1.6, 2.0), (-1.05, 2.0)], L.BLUE)
    for xy, n, xt, ha in (((0.9, 4.4), 1, (2.9, 4.9), "left"), ((1.0, -0.4), 2, (2.9, -0.4), "left"),
                          ((2.3, 3.2), 3, (2.9, 3.2), "left"), ((0.8, 2.2), 4, (2.9, 1.5), "left"),
                          ((-1.6, 1.0), 5, (-2.9, 1.0), "right"), ((-2.3, 3.2), 6, (-2.9, 3.2), "right")):
        label(ax, xy, f"({n})", xt, ha=ha, size=11)
    finish(ax, (-3.6, 3.6), (-1.9, 5.1))
    L.save(fig, "sslc2023_q56_circulation.png")


def numbered_in(mod, chapter_fig, numbers, name):
    """Like numbered(), for a chapter module that imported label/save into its own namespace."""
    real_label, real_save = mod.label, mod.save

    def label_num(ax, xy, text, xytext, ha="left", size=8.5):
        if text in numbers:
            v = numbers[text]
            real_label(ax, xy, f"({v})" if isinstance(v, int) else v, xytext, ha=ha, size=11)

    mod.label = label_num
    mod.save = lambda fig, _name: real_save(fig, name)
    try:
        chapter_fig()
    finally:
        mod.label, mod.save = real_label, real_save


def froth_flotation():
    fig, ax = plt.subplots(figsize=(4.8, 3.6))
    ax.add_patch(Rectangle((0, 0), 3.0, 2.6, fc="none", ec=INK, lw=1.4))
    ax.add_patch(Rectangle((0.02, 0.02), 2.96, 1.9, fc="#DCEBF5", ec="none", zorder=0))
    ax.add_patch(Rectangle((0.02, 1.92), 2.96, 0.45, fc="#F4F1E8", ec=GREY, lw=0.6, zorder=0))
    for k in range(26):
        x, y = 0.12 + (k * 0.113) % 2.8, 2.0 + 0.3 * ((k * 7) % 5) / 5
        ax.add_patch(Circle((x, y), 0.06, fc="white", ec=GREY, lw=0.6))
        if k % 3 == 0:
            ax.add_patch(Circle((x + 0.02, y + 0.01), 0.025, fc="#3A3A3A", ec="none"))
    for k in range(14):
        ax.add_patch(Circle((0.2 + k * 0.2, 0.08 + 0.05 * (k % 2)), 0.05, fc="#9C7A4A", ec="none"))
    for x, y in ((0.7, 0.8), (1.0, 1.3), (2.1, 0.9), (2.4, 1.5), (1.8, 1.6), (0.5, 1.5)):
        ax.add_patch(Circle((x, y), 0.07, fc="white", ec=GREY, lw=0.6))
    ax.plot([1.5, 1.5], [3.0, 0.7], color=INK, lw=2.0)
    ax.plot([1.2, 1.8], [0.7, 0.7], color=INK, lw=3.0)
    ax.plot([-0.6, 0.0], [0.45, 0.45], color=INK, lw=1.4)
    ax.annotate("", (0.15, 0.45), (-0.2, 0.45), arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    for xy, t_, xt in (((1.5, 2.8), "rotating paddle (agitator)", (1.9, 3.2)), ((2.6, 2.2), "froth carrying the\nsulphide ore particles", (3.2, 2.35)),
                       ((2.6, 1.0), "water + pine oil\n(frothing agent)", (3.2, 1.1)), ((2.4, 0.1), "gangue (sand, rock)\nsettles at the bottom", (3.2, 0.25)),
                       ((-0.4, 0.45), "compressed air", (-0.6, 1.0))):
        label(ax, xy, t_, xt, ha="left" if xt[0] > 0 else "right", size=8.5)
    ax.text(1.5, -0.35, "Froth flotation", ha="center", fontsize=9.5, style="italic", color=INK)
    finish(ax, (-1.9, 5.2), (-0.6, 3.5))
    L.save(fig, "froth_flotation.png")


def sslc2021_q17(answer):
    """Concave mirror with the object AB at F and a ray from A parallel to the axis; answer=True adds the reflected ray."""
    import x_sci_ch09_light as O
    fig, ax = plt.subplots(figsize=(4.4, 2.4))
    f, R = 2.0, 4.0
    O.axis_line(ax, -5.2, 0.8)
    O.draw_mirror(ax, "concave", R, 1.8)
    O.tick(ax, -f, "F")
    O.tick(ax, -2 * f, "C")
    O.tick(ax, 0, "P")
    h = 0.8
    O.obj_arrow(ax, -f, h, name="A")
    hit = (O.sag("concave", R, h), h)
    O.seg(ax, (-f, h), hit, O.R1C)
    ax.text(hit[0] + 0.12, hit[1] + 0.08, "D", fontsize=9, color=INK)
    ax.text(-f + 0.1, -0.28, "B", fontsize=9, color=INK)
    if answer:
        O.seg(ax, hit, O.extend(hit, (-f, 0), -4.6), O.R1C)
    ax.set_xlim(-5.3, 1.0)
    ax.set_ylim(-1.9, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    L.save(fig, "sslc2021_q17_mirror_answer.png" if answer else "sslc2021_q17_mirror.png")


def sslc2020_q12():
    import x_sci_ch09_light as O
    fig, ax = plt.subplots(figsize=(4.8, 2.6))
    O.mirror_case(ax, "concave", -4.0, 0.8, xlim=(-6.2, 1.0), names=("A", "B", "A'", "B'"))
    ax.set_xlim(-6.2, 1.0)
    ax.set_ylim(-1.6, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
    L.save(fig, "sslc2020_q12_object_at_c.png")


def electromagnet_circuit():
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    ax.add_patch(Rectangle((0.0, 1.6), 3.0, 0.5, fc="#9AA5B1", ec=INK, lw=1.0))
    for k in range(11):
        x = 0.35 + k * 0.23
        ax.add_patch(Ellipse((x, 1.85), 0.16, 0.85, fill=False, ec="#B5651D", lw=1.6))
    xs, xe = 0.35, 0.35 + 10 * 0.23
    ax.plot([xs, xs, 0.6], [1.42, 0.2, 0.2], color=INK, lw=1.2)
    ax.plot([xe, xe, 2.4], [1.42, 0.2, 0.2], color=INK, lw=1.2)
    for x, h, lw in ((0.8, 0.22, 2.0), (0.92, 0.13, 1.2), (1.08, 0.22, 2.0), (1.2, 0.13, 1.2)):
        ax.plot([x, x], [0.2 - h, 0.2 + h], color=INK, lw=lw)
    ax.plot([0.6, 0.8], [0.2, 0.2], color=INK, lw=1.2)
    ax.plot([1.2, 1.7], [0.2, 0.2], color=INK, lw=1.2)
    ax.add_patch(Circle((1.8, 0.2), 0.08, fc="white", ec=INK, lw=1.0))
    ax.add_patch(Circle((2.15, 0.2), 0.08, fc="white", ec=INK, lw=1.0))
    ax.plot([1.86, 2.09], [0.27, 0.27], color=INK, lw=2.0)
    ax.plot([2.23, 2.4], [0.2, 0.2], color=INK, lw=1.2)
    for xy, t_, xt in (((0.1, 1.85), "soft iron core", (-0.5, 2.7)), ((1.6, 2.25), "coil of insulated\ncopper wire", (1.9, 2.95)),
                       ((1.0, 0.0), "battery", (0.6, -0.55)), ((1.98, 0.3), "plug key", (2.2, -0.55))):
        label(ax, xy, t_, xt, ha="left", size=8.5)
    ax.text(3.15, 1.85, "N", fontsize=10, va="center", color="#C0392B")
    ax.text(-0.25, 1.85, "S", fontsize=10, va="center", color="#2E6DB4")
    finish(ax, (-0.8, 3.8), (-0.9, 3.3))
    L.save(fig, "electromagnet_circuit.png")


def guidebook_q53_flower():
    """CM IMPACT guidebook model paper Q53: the flower with parts lettered A-D as in the book (A ovary, B petal,
    C stigma, D anther), and without the "pistil" and "stamen" brackets that would give the answers away."""
    import matplotlib.axes
    import x_sci_ch07_reproduction as R
    real_text, real_plot = matplotlib.axes.Axes.text, matplotlib.axes.Axes.plot

    def text(self, x, y, s, *args, **kwargs):
        if "pistil" in str(s) or "stamen" in str(s):
            return None
        return real_text(self, x, y, s, *args, **kwargs)

    def plot(self, *args, **kwargs):
        if kwargs.get("color") == R.ACC:  # the brackets beside "pistil" and "stamen"
            return []
        return real_plot(self, *args, **kwargs)

    matplotlib.axes.Axes.text, matplotlib.axes.Axes.plot = text, plot
    try:
        numbered_in(R, R.fig_flower, {"ovary": "A", "petal": "B", "stigma": "C", "anther": "D"},
                    "guidebook_q53_flower.png")
    finally:
        matplotlib.axes.Axes.text, matplotlib.axes.Axes.plot = real_text, real_plot


def sample2025_q9_structure():
    """Sample paper 2025 Q9: ethanol drawn with every bond, unnamed (naming it is the question)."""
    import x_sci_ch04_carbon as C4
    fig, ax = plt.subplots(figsize=(2.6, 1.6))
    a = [(0, 0, "C"), (1, 0, "C"), (2, 0, "O"), (2.8, 0, "H"), (-0.8, 0, "H"), (0, 0.8, "H"), (0, -0.8, "H"),
         (1, 0.8, "H"), (1, -0.8, "H")]
    b = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 4, 1), (0, 5, 1), (0, 6, 1), (1, 7, 1), (1, 8, 1)]
    C4.mol(ax, a, b)
    C4.finish(ax, (-1.2, 3.2), (-1.1, 1.1))
    C4.OUT = L.OUT
    C4.save(fig, "sample2025_q9_structure.png")


def sample2025_q46_structures():
    """Sample paper 2025 Q46: bromopentane, hexanal and butanone, drawn as in Fig. 4.6."""
    import x_sci_ch04_carbon as C4
    fig, axs = plt.subplots(1, 3, figsize=(10.0, 2.5))

    def hs(atoms, bonds, idx, dirs):
        for dxx, dyy in dirs:
            x, y, _ = atoms[idx]
            atoms.append((x + dxx, y + dyy, "H"))
            bonds.append((idx, len(atoms) - 1, 1))

    a = [(k, 0, "C") for k in range(5)] + [(5.0, 0, "Br")]
    b = [(k, k + 1, 1) for k in range(5)]
    hs(a, b, 0, [(-0.8, 0), (0, 0.8), (0, -0.8)])
    for k in range(1, 5):
        hs(a, b, k, [(0, 0.8), (0, -0.8)])
    C4.mol(axs[0], a, b, size=9)
    axs[0].text(2.4, -1.5, "(i) 1-bromopentane, C₅H₁₁Br", ha="center", fontsize=8.5)
    a = [(k, 0, "C") for k in range(6)] + [(5.7, 0.7, "O"), (5.7, -0.7, "H")]
    b = [(k, k + 1, 1) for k in range(5)] + [(5, 6, 2), (5, 7, 1)]
    hs(a, b, 0, [(-0.8, 0), (0, 0.8), (0, -0.8)])
    for k in range(1, 5):
        hs(a, b, k, [(0, 0.8), (0, -0.8)])
    C4.mol(axs[1], a, b, size=9)
    axs[1].text(2.6, -1.5, "(ii) hexanal, CH₃(CH₂)₄CHO", ha="center", fontsize=8.5)
    a = [(0, 0, "C"), (1, 0, "C"), (2, 0, "C"), (3, 0, "C"), (1, 0.85, "O")]
    b = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (1, 4, 2)]
    hs(a, b, 0, [(-0.8, 0), (0, 0.8), (0, -0.8)])
    hs(a, b, 2, [(0, 0.8), (0, -0.8)])
    hs(a, b, 3, [(0.8, 0), (0, 0.8), (0, -0.8)])
    C4.mol(axs[2], a, b)
    axs[2].text(1.5, -1.5, "(iii) butanone, CH₃COCH₂CH₃", ha="center", fontsize=8.5)
    for ax in axs:
        C4.finish(ax, (-1.2, 6.4), (-1.9, 1.4))
    C4.OUT = L.OUT
    C4.save(fig, "sample2025_q46_structures.png")


if __name__ == "__main__":
    sample2025_q9_structure()
    sample2025_q46_structures()
    copy_chapter("sci_ch04_fig07_ester.png", "ester_preparation.png")
    copy_chapter("sci_ch12_fig07_motor.png", "electric_motor.png")
    guidebook_q53_flower()
    copy_chapter("sci_ch10_fig04_prism.png", "prism_refraction.png")
    copy_chapter("sci_ch04_fig06_functional.png", "functional_group_structures.png")
    electromagnet_circuit()
    sslc2020_q12()
    import x_sci_ch06_control as N
    numbered_in(N, N.fig_brain, {"fore-brain (cerebrum):\nthinking, senses, voluntary actions": "A",
                                 "cerebellum: posture,\nbalance, precise movements": "B"}, "sslc2020_q31_brain.png")
    copy_chapter("sci_ch06_fig03_brain.png", "brain_labelled.png")
    copy_chapter("sci_ch12_fig04_solenoid.png", "solenoid_field.png")
    copy_chapter("sci_ch04_fig01_dot_simple.png", "covalent_dot_structures.png")
    sslc2021_q17(False)
    sslc2021_q17(True)
    numbered(L.fig_excretory, {"renal vein": 1, "renal artery": 2, "ureter": 3, "urinary bladder": 4},
             "sslc2021_q52_excretory.png")
    copy_chapter("sci_ch05_fig12_excretory.png", "excretory_system_labelled.png")
    copy_chapter("sci_ch07_fig01_fission.png", "fission_types.png")
    import x_sci_ch10_eye as E
    numbered_in(E, E.fig_eye, {"retina": 1, "cornea": 2, "blind spot": 3, "iris": 4, "optic nerve": 5, "pupil": 6},
                "sslc2022_q20_eye.png")
    respiratory({"nasal passage": 1, "pharynx": 2, "ribs": 3, "bronchioles": 4}, "sslc2022_q52_respiratory.png")
    froth_flotation()
    copy_chapter("sci_ch10_fig01_eye.png", "human_eye_labelled.png")
    copy_chapter("sci_ch03_fig04_ionic_formation.png", "ionic_bond_formation.png")
    copy_chapter("sci_ch07_fig05_rhizopus.png", "rhizopus_spores.png")
    sslc2023_q17()
    sslc2023_q35()
    sslc2023_q56()
    copy_chapter("sci_ch05_fig10_double_circulation.png", "double_circulation_labelled.png")
    copy_chapter("sci_ch03_fig08_refining.png", "electrorefining_labelled.png")
    copy_chapter("sci_ch06_fig01_neuron.png", "neuron_labelled.png")
    copy_chapter("sci_ch10_fig05_dispersion.png", "prism_dispersion.png")
    sslc2026_q49()
    numbered(L.fig_alimentary, {"mouth (buccal cavity)": 1, "oesophagus (food pipe)": 2, "stomach": 3,
                                "small intestine": 4, "pancreas": 5, "liver": 6}, "sslc2024_q35_alimentary.png")
    copy_chapter("sci_ch05_fig06_alimentary.png", "alimentary_canal_labelled.png")
    copy_chapter("sci_ch07_fig07_pollen_tube.png", "pollen_germination.png")
    copy_chapter("sci_ch09_fig03_concave_images.png", "concave_mirror_images.png")
    sslc2026_q42()
    respiratory({"nasal passage": 1, "trachea": 2, "lung": 3, "diaphragm": 4}, "sslc2026_q53_respiratory.png")
    copy_chapter("sci_ch10_fig03_hypermetropia.png", "hypermetropia_correction.png")
    copy_chapter("sci_ch05_fig08_respiratory.png", "respiratory_system_labelled.png")
    copy_chapter("sci_ch07_fig06_flower.png", "flower_longitudinal_section.png")
    copy_chapter("sci_ch09_fig06_glass_slab.png", "refraction_glass_slab.png")
    copy_chapter("sci_ch12_fig01_bar_magnet.png", "bar_magnet_field_lines.png")
