"""Figures for Class XII Biology Chapter 6, Evolution.
Run: python xii_bio_ch06_evolution.py
"""
from xii_bio_common import *


def fig01_miller():
    fig, a = canvas(7.4, 4.8, (0, 15), (0, 9.6))
    a.add_patch(Circle((4.0, 6.4), 1.9, fc=PALE_BLUE, ec=BLUE, lw=1.6))
    a.text(4.0, 5.7, "CH₄, NH₃, H₂,\nH₂O vapour", ha="center", va="center", fontsize=8.5)
    a.plot([3.0, 3.5], [7.9, 7.0], color=INK, lw=2)
    a.plot([5.0, 4.5], [7.9, 7.0], color=INK, lw=2)
    a.text(4.0, 8.75, "electrodes (electric discharge)", ha="center", fontsize=8.5)
    a.plot([3.5, 3.7, 3.9, 4.1, 4.3, 4.5], [7.0, 6.8, 7.1, 6.8, 7.1, 7.0], color=AMBER, lw=1.4)
    a.plot([5.9, 9.0, 9.0], [6.4, 6.4, 3.2], color=GREY, lw=3)
    a.add_patch(Rectangle((8.6, 4.0), 0.8, 2.0, fc="#E3F1F7", ec=BLUE, lw=1.2))
    a.text(9.6, 5.0, "condenser\n(cooling)", fontsize=8.5, va="center")
    a.add_patch(Polygon([(8.4, 3.2), (9.6, 3.2), (9.2, 2.2), (8.8, 2.2)], closed=True, fc=PALE_AMBER, ec=AMBER))
    a.text(9.8, 2.6, "water with organic compounds\n(amino acids) collects here", fontsize=8.5, va="center")
    a.plot([8.8, 1.2, 1.2, 2.2], [2.2, 2.2, 3.4, 3.4], color=GREY, lw=3)
    a.add_patch(Ellipse((2.6, 3.2), 1.4, 1.0, fc="#E3F1F7", ec=BLUE))
    a.text(2.6, 3.2, "boiling\nwater", ha="center", va="center", fontsize=7.5)
    a.plot([2.6, 2.6, 3.0], [3.7, 4.6, 4.9], color=GREY, lw=3)
    a.text(2.6, 1.5, "heat ↑", ha="center", fontsize=8.5, color=RED)
    a.text(7.5, 9.2, "Miller's experiment (1953): chemical evolution in the laboratory", ha="center", fontsize=9.5,
           weight="bold")
    save(fig, "bio_ch06_fig01_miller.png")


def fig02_selection():
    x = np.linspace(-4, 4, 300)
    g = lambda mu, s: np.exp(-((x - mu) / s) ** 2 / 2)
    fig, axs = plt.subplots(1, 3, figsize=(10.0, 3.2), sharey=True)
    data = [("(a) Stabilising", g(0, 1.4), g(0, 0.7)), ("(b) Directional", g(0, 1.2), g(1.5, 1.0)),
            ("(c) Disruptive", g(0, 1.4), 0.75 * (g(-2.2, 0.8) + g(2.2, 0.8)))]
    for ax, (t, before, after) in zip(axs, data):
        ax.fill_between(x, before, color=PALE_BLUE)
        ax.plot(x, before, color=BLUE, lw=1.2, label="before")
        ax.plot(x, after, color=RED, lw=2, label="after selection")
        ax.set_title(t, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel("character value (e.g. size)", fontsize=8.5)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    axs[0].set_ylabel("number of individuals", fontsize=8.5)
    axs[2].legend(fontsize=8, frameon=False, loc="upper right")
    fig.tight_layout()
    save(fig, "bio_ch06_fig02_natural_selection.png")


def fig03_human_timeline():
    fig, a = canvas(10.0, 4.0, (0, 20), (0, 8.0))
    a.plot([0.8, 19.2], [3.0, 3.0], color=INK, lw=2)
    stages = [
        (1.6, "15 mya", "Dryopithecus\n(ape-like) and\nRamapithecus\n(man-like)"),
        (5.0, "3–4 mya / 2 mya", "Australopithecines\n(East African\ngrasslands; stone tools,\nate fruit)"),
        (8.6, "about 2 mya", "Homo habilis\n650–800 cc\n(first human-like;\nno meat)"),
        (11.8, "1.5 mya", "Homo erectus\n900 cc\n(ate meat;\nJava fossils)"),
        (15.0, "1,00,000–40,000\nyears ago", "Neanderthal man\n1400 cc\n(hides; buried dead)"),
        (18.3, "75,000–10,000\nyears ago", "Homo sapiens\n(modern man;\ncave art 18,000 y;\nfarming 10,000 y)"),
    ]
    for x, t, n in stages:
        a.plot([x], [3.0], "o", color=BLUE, ms=7)
        a.text(x, 2.4, t, ha="center", va="top", fontsize=8, color=RED)
        a.text(x, 3.5, n, ha="center", va="bottom", fontsize=8)
    a.text(10.0, 7.6, "Origin and evolution of man (brain capacity in cc)", ha="center", fontsize=9.5, weight="bold")
    a.annotate("", xy=(19.6, 3.0), xytext=(18.9, 3.0), arrowprops=dict(arrowstyle="-|>", color=INK))
    save(fig, "bio_ch06_fig03_human_evolution.png")


def fig04_finches():
    fig, a = canvas(7.0, 4.6, (-7, 7), (-4.4, 4.8))
    box(a, (-2.2, -0.6), 4.4, 1.2, "ancestral\nseed-eating finch", fc=PALE_AMBER, ec=AMBER, fs=8.5, bold=True)
    kinds = [("large ground finch\n(large seeds)", 90), ("cactus finch\n(cactus flowers)", 30),
             ("warbler finch\n(insects)", -30), ("woodpecker finch\n(insects in bark)", -90),
             ("tree finch\n(fruits, buds)", -150), ("small ground finch\n(small seeds)", 150)]
    for name, ang in kinds:
        t = np.radians(ang)
        x, y = 4.7 * np.cos(t), 3.4 * np.sin(t)
        arrow(a, (1.6 * np.cos(t), 0.9 * np.sin(t)), (x * 0.78, y * 0.78), color=GREEN, lw=1.2, ms=9)
        a.text(x, y, name, ha="center", va="center", fontsize=8)
    a.text(0, -4.3, "Adaptive radiation: Darwin's finches of the Galapagos Islands", ha="center", fontsize=9,
           weight="bold")
    save(fig, "bio_ch06_fig04_finches.png")


if __name__ == "__main__":
    fig01_miller()
    fig02_selection()
    fig03_human_timeline()
    fig04_finches()
