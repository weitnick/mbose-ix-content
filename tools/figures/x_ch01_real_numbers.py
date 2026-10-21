"""Figures for Class X Mathematics, Chapter 1: Real Numbers.
Run: python x_ch01_real_numbers.py   (writes PNGs into Class X Content/Math/Generated Content/figures)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "pylib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Class X Content", "Math", "Generated Content", "figures")
os.makedirs(OUT, exist_ok=True)
INK, ACC, HI, SOFT = "#1D2733", "#1F4E79", "#B7791F", "#E9F0F7"
plt.rcParams.update({"font.size": 10, "mathtext.fontset": "cm", "font.family": "DejaVu Sans"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def node(ax, x, y, t, prime=False):
    ax.text(x, y, t, ha="center", va="center", fontsize=10.5,
            color=HI if prime else INK, weight="bold" if prime else "normal",
            bbox=dict(boxstyle="circle,pad=0.25" if prime else "round,pad=0.25",
                      fc="#FDF7EA" if prime else SOFT, ec=HI if prime else ACC, lw=1))


def edge(ax, x1, y1, x2, y2):
    ax.plot([x1, x2], [y1 + 0.18, y2 - 0.18], color=ACC, lw=1)


# Fig 1: factor tree of 32760 (each step splits off the smallest prime)
def fig_factor_tree():
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    chain = [32760, 16380, 8190, 4095, 1365, 455, 91]
    primes = [2, 2, 2, 3, 3, 5, 7]
    x, y = 0.0, 0.0
    node(ax, x, y, str(chain[0]))
    for i, p in enumerate(primes):
        ny = y - 0.62
        edge(ax, x, y, x - 0.55, ny)
        edge(ax, x, y, x + 0.55, ny)
        node(ax, x - 0.55, ny, str(p), prime=True)
        nxt = chain[i + 1] if i + 1 < len(chain) else 13
        node(ax, x + 0.55, ny, str(nxt), prime=(nxt == 13))
        x, y = x + 0.55, ny
    ax.text(4.3, -1.0, r"$32760 = 2^3 \times 3^2 \times 5 \times 7 \times 13$", fontsize=12, color=INK)
    ax.text(4.3, -1.6, "Circled numbers are primes:\nthe branches stop there.", fontsize=9, color=HI)
    ax.set_xlim(-1.0, 7.2); ax.set_ylim(-4.8, 0.45); ax.axis("off")
    save(fig, "ch01_fig01_factor_tree_32760.png")


# Fig 2: the steps of a proof by contradiction (root 2 is irrational)
def fig_contradiction():
    steps = [
        ("Assume the opposite", r"$\sqrt{2} = \frac{a}{b}$, with $a, b$ coprime, $b \neq 0$"),
        ("Square and rearrange", r"$2b^2 = a^2$, so 2 divides $a^2$, hence 2 divides $a$"),
        ("Substitute $a = 2c$", r"$2b^2 = 4c^2 \Rightarrow b^2 = 2c^2$, so 2 divides $b$"),
        ("Clash with the assumption", "2 divides both $a$ and $b$, but they were coprime"),
        ("Conclude", r"the assumption is false: $\sqrt{2}$ is irrational"),
    ]
    fig, ax = plt.subplots(figsize=(6.4, 5.4))
    gap = 1.25
    for i, (h, t) in enumerate(steps):
        y = (len(steps) - 1 - i) * gap
        last = i == len(steps) - 1
        ax.add_patch(FancyBboxPatch((0, y - 0.45), 9.6, 0.9, boxstyle="round,pad=0.02,rounding_size=0.15",
                                    fc="#FDF7EA" if last else SOFT, ec=HI if last else ACC, lw=1))
        ax.text(0.25, y + 0.2, f"{i + 1}. {h}", fontsize=9.5, weight="bold", color=HI if last else ACC, va="center")
        ax.text(0.45, y - 0.2, t, fontsize=10.5, color=INK, va="center")
        if not last:
            ax.annotate("", xy=(4.8, y - gap + 0.47), xytext=(4.8, y - 0.47),
                        arrowprops=dict(arrowstyle="-|>", color=ACC, lw=1))
    ax.set_xlim(-0.1, 9.7); ax.set_ylim(-0.6, (len(steps) - 1) * gap + 0.6); ax.axis("off")
    save(fig, "ch01_fig02_proof_by_contradiction.png")


if __name__ == "__main__":
    fig_factor_tree()
    fig_contradiction()
