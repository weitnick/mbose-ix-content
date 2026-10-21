"""Figures for Class XII Biology Chapter 11, Organisms and Populations.
Run: python xii_bio_ch11_populations.py
"""
from xii_bio_common import *


def fig01_age_pyramids():
    fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.6))
    shapes = [("(a) Expanding (growing)", [9, 8, 7, 6, 5, 4, 3, 2, 1]),
              ("(b) Stable", [5.2, 5.1, 5, 4.9, 4.8, 4.6, 4.2, 3.4, 2.2]),
              ("(c) Declining", [3, 3.6, 4.2, 4.8, 5, 5, 4.6, 3.8, 2.4])]
    for ax, (title, widths) in zip(axs, shapes):
        ax.set_xlim(-10, 10)
        ax.set_ylim(-0.6, 9.6)
        ax.axis("off")
        for i, w in enumerate(widths):
            fc = PALE_BLUE if i < 3 else (PALE_GREEN if i < 6 else PALE_AMBER)
            ax.add_patch(Rectangle((-w, i), w, 0.9, fc=fc, ec=BLUE, lw=0.8))
            ax.add_patch(Rectangle((0, i), w, 0.9, fc=fc, ec=RED, lw=0.8))
        ax.plot([0, 0], [0, 9], color=INK, lw=1)
        ax.text(-5, -0.5, "males", ha="center", fontsize=8, color=BLUE)
        ax.text(5, -0.5, "females", ha="center", fontsize=8, color=RED)
        ax.set_title(title, fontsize=9.5)
    fig.text(0.5, -0.04, "Bottom bands: pre-reproductive age · middle: reproductive · top: post-reproductive",
             ha="center", fontsize=8.5, color=GREY)
    fig.tight_layout()
    save(fig, "bio_ch11_fig01_age_pyramids.png")


def fig02_density_factors():
    fig, a = canvas(8.0, 4.4, (0, 16), (0, 8.8))
    a.add_patch(Circle((8, 4.6), 2.1, fc=PALE_GREEN, ec=GREEN, lw=1.6))
    a.text(8, 4.9, "Population\ndensity (N)", ha="center", va="center", fontsize=10, weight="bold")
    box(a, (0.4, 6.4), 4.0, 1.6, "Natality (B)\nbirths", fc=PALE_GREEN, ec=GREEN, fs=9)
    box(a, (11.6, 6.4), 4.0, 1.6, "Immigration (I)\ncoming in", fc=PALE_GREEN, ec=GREEN, fs=9)
    box(a, (0.4, 1.2), 4.0, 1.6, "Mortality (D)\ndeaths", fc=PALE_RED, ec=RED, fs=9)
    box(a, (11.6, 1.2), 4.0, 1.6, "Emigration (E)\nleaving", fc=PALE_RED, ec=RED, fs=9)
    arrow(a, (4.4, 7.0), (6.3, 5.8), color=GREEN, text="+", fs=12, dy=0.1)
    arrow(a, (11.6, 7.0), (9.7, 5.8), color=GREEN, text="+", fs=12, dy=0.1)
    arrow(a, (6.3, 3.4), (4.4, 2.2), color=RED, text="−", fs=12, dy=0.1)
    arrow(a, (9.7, 3.4), (11.6, 2.2), color=RED, text="−", fs=12, dy=0.1)
    a.text(8, 0.3, "N(t+1) = N(t) + [(B + I) − (D + E)]", ha="center", fontsize=10.5, weight="bold", color=INK)
    save(fig, "bio_ch11_fig02_density_factors.png")


def fig03_growth_curves():
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    t = np.linspace(0, 10, 300)
    K, N0, r = 100, 2, 0.75
    nexp = N0 * np.exp(r * t)
    nlog = K / (1 + (K / N0 - 1) * np.exp(-r * t))
    ax.plot(t[nexp < 165], nexp[nexp < 165], color=RED, lw=2, ls="--", label="exponential: dN/dt = rN (J-shaped)")
    ax.plot(t, nlog, color=BLUE, lw=2.2, label="logistic: dN/dt = rN (K − N)/K (sigmoid)")
    ax.axhline(K, color=GREY, ls=":", lw=1.2)
    ax.text(10.1, K, "K (carrying\ncapacity)", va="center", fontsize=8.5, color=GREY)
    ax.annotate("lag", xy=(2.0, 8), xytext=(0.6, 30), fontsize=8, arrowprops=dict(arrowstyle="-", color=GREY))
    ax.annotate("acceleration", xy=(4.2, 34), xytext=(5.6, 22), fontsize=8, arrowprops=dict(arrowstyle="-", color=GREY))
    ax.annotate("deceleration", xy=(6.3, 82), xytext=(7.0, 62), fontsize=8, arrowprops=dict(arrowstyle="-", color=GREY))
    ax.annotate("asymptote", xy=(9.0, 99), xytext=(7.4, 120), fontsize=8, arrowprops=dict(arrowstyle="-", color=GREY))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 170)
    ax.set_xlabel("Time (t)")
    ax.set_ylabel("Population density (N)")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=8, frameon=False)
    save(fig, "bio_ch11_fig03_growth_curves.png")


def fig04_interactions():
    fig, a = canvas(9.0, 4.2, (0, 18), (0, 8.4))
    a.text(9, 8.0, "Interactions between two species (+ benefit, − harm, 0 no effect)", ha="center", fontsize=10,
           weight="bold")
    rows = [("Mutualism", "+", "+", "lichen; mycorrhiza; fig and wasp", PALE_GREEN),
            ("Competition", "−", "−", "flamingoes and fishes; Balanus and Chthamalus", PALE_RED),
            ("Predation", "+", "−", "tiger and deer; sparrow eating seeds", PALE_AMBER),
            ("Parasitism", "+", "−", "Cuscuta on hedge plants; lice; liver fluke", PALE_AMBER),
            ("Commensalism", "+", "0", "orchid on mango; cattle egret and cattle", SOFT),
            ("Amensalism", "−", "0", "bacteria (A) inhibited by antibiotic of Penicillium (B)", SOFT)]
    a.text(1.6, 7.0, "Interaction", ha="center", fontsize=9, weight="bold")
    a.text(4.6, 7.0, "Species A", ha="center", fontsize=9, weight="bold")
    a.text(6.6, 7.0, "Species B", ha="center", fontsize=9, weight="bold")
    a.text(12.6, 7.0, "Example", ha="center", fontsize=9, weight="bold")
    for i, (name, sa, sb, ex, fc) in enumerate(rows):
        y = 5.9 - i * 1.05
        a.add_patch(Rectangle((0.1, y - 0.42), 17.8, 0.9, fc=fc, ec="none"))
        a.text(1.6, y, name, ha="center", va="center", fontsize=9)
        a.text(4.6, y, sa, ha="center", va="center", fontsize=13, weight="bold",
               color=GREEN if sa == "+" else RED)
        a.text(6.6, y, sb, ha="center", va="center", fontsize=13, weight="bold",
               color=GREEN if sb == "+" else (RED if sb == "−" else GREY))
        a.text(8.0, y, ex, va="center", fontsize=8.6)
    save(fig, "bio_ch11_fig04_interactions.png")


if __name__ == "__main__":
    fig01_age_pyramids()
    fig02_density_factors()
    fig03_growth_curves()
    fig04_interactions()
