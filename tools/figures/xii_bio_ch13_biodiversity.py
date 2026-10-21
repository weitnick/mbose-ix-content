"""Figures for Class XII Biology Chapter 13, Biodiversity and Conservation.
Run: python xii_bio_ch13_biodiversity.py
"""
from xii_bio_common import *


def fig01_latitude():
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    places = ["Colombia\n(near equator)", "India\n(mostly tropical)", "New York\n(41° N)", "Greenland\n(71° N)"]
    birds = [1400, 1200, 105, 56]
    bars = ax.bar(places, birds, color=[GREEN, GREEN, AMBER, BLUE], edgecolor=INK, width=0.6)
    for b, v in zip(bars, birds):
        ax.text(b.get_x() + b.get_width() / 2, v + 30, ("about " if v == 1400 else ("over " if v == 1200 else ""))
                + f"{v:,}", ha="center", fontsize=8.5)
    ax.set_ylabel("Number of bird species")
    ax.set_ylim(0, 1600)
    ax.set_title("Latitudinal gradient: species diversity falls from the equator to the poles", fontsize=9.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="x", labelsize=8.5)
    save(fig, "bio_ch13_fig01_latitude.png")


def fig02_species_area():
    fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.6))
    A = np.linspace(1, 100, 300)
    C, Z = 10, 0.15
    S = C * A ** Z
    axs[0].plot(A, S, color=BLUE, lw=2.2)
    axs[0].set_xlabel("Area (A)")
    axs[0].set_ylabel("Species richness (S)")
    axs[0].set_title("(a) Rectangular hyperbola", fontsize=9.5)
    axs[0].set_xticks([])
    axs[0].set_yticks([])
    la = np.linspace(0, 3, 50)
    for z, col, lab in [(0.15, BLUE, "Z = 0.1–0.2 (within a region)"), (1.0, RED, "Z = 0.6–1.2 (whole continents)")]:
        axs[1].plot(la, 1 + z * la, color=col, lw=2.2, label=lab)
    axs[1].set_xlabel("log A")
    axs[1].set_ylabel("log S")
    axs[1].set_title("(b) On log scales: log S = log C + Z log A", fontsize=9.5)
    axs[1].set_xticks([])
    axs[1].set_yticks([])
    axs[1].legend(fontsize=7.8, frameon=False, loc="upper left")
    axs[1].set_ylim(0, 4.3)
    axs[1].annotate("intercept = log C", xy=(0, 1), xytext=(0.5, 0.35), fontsize=8,
                    arrowprops=dict(arrowstyle="-", color=GREY))
    for ax in axs:
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    fig.tight_layout()
    save(fig, "bio_ch13_fig02_species_area.png")


def fig03_evil_quartet():
    fig, a = canvas(9.0, 4.6, (0, 18), (0, 9.2))
    a.add_patch(Circle((9, 4.8), 1.9, fc=PALE_RED, ec=RED, lw=1.6))
    a.text(9, 4.8, "Loss of\nbiodiversity\n(the evil\nquartet)", ha="center", va="center", fontsize=9, weight="bold")
    items = [((0.3, 6.0), "1. Habitat loss and fragmentation\n(most important): rain forests\n14 % → 6 % of land; Amazon\ncleared for soya and cattle"),
             ((12.0, 6.0), "2. Over-exploitation ('greed'):\nSteller's sea cow, passenger\npigeon; over-harvested\nmarine fish"),
             ((0.3, 0.6), "3. Alien species invasions:\nNile perch → 200+ cichlids lost\n(Lake Victoria); Parthenium,\nLantana, water hyacinth;\nAfrican catfish"),
             ((12.0, 0.6), "4. Co-extinctions: a host fish\ndies → its parasites die;\nplant–pollinator partners\ndie together")]
    for xy, t in items:
        box(a, xy, 5.7, 2.6, t, fc=SOFT, ec=BLUE, fs=7.8)
    for p0, p1 in [((6.0, 7.0), (7.4, 5.8)), ((12.0, 7.0), (10.6, 5.8)), ((6.0, 2.0), (7.4, 3.6)),
                   ((12.0, 2.0), (10.6, 3.6))]:
        arrow(a, p0, p1, color=RED, ms=9)
    save(fig, "bio_ch13_fig03_evil_quartet.png")


def fig04_conservation():
    fig, a = canvas(9.4, 4.4, (0, 19), (0, 8.8))
    box(a, (6.5, 7.0), 6.0, 1.3, "Biodiversity conservation", fc=PALE_AMBER, ec=AMBER, fs=10, bold=True)
    box(a, (0.4, 0.4), 8.4, 5.4, "In situ (on site)\nprotect the whole ecosystem\n(save the forest to save the tiger)\n\n"
        "• biodiversity hotspots (34 in the world;\n   3 cover India)\n• biosphere reserves, national parks,\n   wildlife sanctuaries\n"
        "• sacred groves (Khasi and Jaintia Hills)", fc=PALE_GREEN, ec=GREEN, fs=8)
    box(a, (10.2, 0.4), 8.4, 5.4, "Ex situ (off site)\nthreatened species taken out of the\nwild and given special care\n\n"
        "• zoological parks, botanical gardens,\n   wildlife safari parks\n• cryopreservation of gametes; IVF\n"
        "• tissue culture; seed banks", fc=SOFT, ec=BLUE, fs=8)
    arrow(a, (8.0, 7.0), (5.0, 5.8), ms=10)
    arrow(a, (11.0, 7.0), (14.0, 5.8), ms=10)
    save(fig, "bio_ch13_fig04_conservation.png")


def fig05_biosphere_reserve():
    fig, a = canvas(6.4, 4.6, (0, 12.8), (0, 9.2))
    a.add_patch(Circle((4.6, 4.6), 4.1, fc=PALE_AMBER, ec=AMBER, lw=1.4))
    a.add_patch(Circle((4.6, 4.6), 2.7, fc=PALE_GREEN, ec=GREEN, lw=1.4))
    a.add_patch(Circle((4.6, 4.6), 1.3, fc="#B9DDBB", ec=GREEN, lw=1.6))
    a.text(4.6, 4.6, "Core", ha="center", va="center", fontsize=9, weight="bold")
    a.text(4.6, 6.6, "Buffer", ha="center", va="center", fontsize=9)
    a.text(4.6, 8.0, "Transition", ha="center", va="center", fontsize=9)
    label(a, (5.6, 4.0), (9.0, 2.0), "Core: fully protected;\nno human activity", fs=8)
    label(a, (6.8, 5.8), (9.0, 5.0), "Buffer: limited activity —\nresearch, education", fs=8)
    label(a, (8.3, 6.9), (9.0, 8.0), "Transition: people live and\nwork; farming, settlements", fs=8)
    save(fig, "bio_ch13_fig05_biosphere_reserve.png")


if __name__ == "__main__":
    fig01_latitude()
    fig02_species_area()
    fig03_evil_quartet()
    fig04_conservation()
    fig05_biosphere_reserve()
