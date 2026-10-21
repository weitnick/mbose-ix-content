"""Figures for Class XII Biology Chapter 12, Ecosystem.
Run: python xii_bio_ch12_ecosystem.py
"""
from xii_bio_common import *


def fig01_decomposition():
    fig, a = canvas(9.0, 5.4, (0, 18), (0, 10.8))
    a.text(9, 10.3, "Decomposition of detritus in a terrestrial ecosystem", ha="center", fontsize=10, weight="bold")
    box(a, (6.2, 7.6), 5.6, 1.8, "Detritus\n(dead leaves, bark, flowers,\ndead animals, faecal matter)", fc=PALE_AMBER,
        ec=AMBER, fs=8.4, bold=False)
    steps = [((0.4, 4.4), "1. Fragmentation\ndetritivores (earthworm)\nbreak detritus into\nsmall pieces"),
             ((4.8, 4.4), "2. Leaching\nwater-soluble nutrients\nmove down into soil;\nprecipitate as salts"),
             ((9.2, 4.4), "3. Catabolism\nbacterial and fungal\nenzymes degrade detritus\ninto simpler substances"),
             ((13.6, 4.4), "4. Humification\ndark, amorphous humus;\nresists microbes; a\nreservoir of nutrients")]
    for xy, t in steps:
        box(a, xy, 4.0, 2.4, t, fc=SOFT, ec=BLUE, fs=7.8)
        arrow(a, (9.0, 7.6), (xy[0] + 2.0, xy[1] + 2.4), color=GREY, lw=1, ms=8)
    box(a, (4.6, 0.8), 8.8, 2.0, "5. Mineralisation\nhumus degraded by microbes → inorganic\nnutrients (CO₂, water, minerals) released into soil",
        fc=PALE_GREEN, ec=GREEN, fs=8.2)
    arrow(a, (15.6, 4.4), (13.4, 2.2), color=GREEN, lw=1.2, ms=9)
    a.text(2.2, 1.6, "Fast: detritus rich in\nnitrogen and sugars;\nwarm, moist, aerobic", ha="center", fontsize=7.6,
           color=GREEN)
    a.text(16.0, 1.6, "Slow: rich in lignin\nand chitin; cold,\nanaerobic", ha="center", fontsize=7.6, color=RED)
    save(fig, "bio_ch12_fig01_decomposition.png")


def fig02_energy_flow():
    fig, a = canvas(9.4, 4.8, (0, 19), (0, 9.6))
    a.text(9.5, 9.1, "Energy flow through trophic levels is unidirectional (10 per cent law)", ha="center",
           fontsize=10, weight="bold")
    a.add_patch(Circle((1.3, 6.0), 0.9, fc="#F6D365", ec=AMBER, lw=1.4))
    a.text(1.3, 6.0, "Sun", ha="center", va="center", fontsize=8.5, weight="bold")
    levels = [("Producers\n(1st trophic level)\ngreen plants", "10,000 J", PALE_GREEN, GREEN),
              ("Primary consumers\n(2nd) herbivores", "1,000 J", PALE_AMBER, AMBER),
              ("Secondary consumers\n(3rd) carnivores", "100 J", PALE_RED, RED),
              ("Tertiary consumers\n(4th) top carnivores", "10 J", SOFT, BLUE)]
    for i, (t, e, fc, ec) in enumerate(levels):
        x = 2.8 + i * 4.1
        box(a, (x, 5.0), 3.5, 2.0, t, fc=fc, ec=ec, fs=7.8)
        a.text(x + 1.75, 7.3, e, ha="center", fontsize=8.5, weight="bold", color=ec)
        a.annotate("", xy=(x + 2.6, 3.6), xytext=(x + 2.6, 5.0),
                   arrowprops=dict(arrowstyle="-|>", color=RED, lw=1, ls="--"))
        a.text(x + 2.6, 3.2, "heat", ha="center", fontsize=7.6, color=RED)
        a.annotate("", xy=(x + 0.8, 1.7), xytext=(x + 0.8, 5.0),
                   arrowprops=dict(arrowstyle="-|>", color=GREY, lw=0.9))
        if i < 3:
            arrow(a, (x + 3.5, 6.0), (x + 4.1, 6.0), ms=9)
    arrow(a, (2.2, 6.0), (2.8, 6.0), ms=9)
    box(a, (3.0, 0.3), 15.0, 1.3, "Decomposers (bacteria, fungi) receive dead remains of every level — detritus food chain",
        fc=PALE_AMBER, ec=AMBER, fs=8.2)
    a.text(1.3, 3.4, "PAR < 50 %\nof sunlight;\nplants fix\n2–10 % of PAR", ha="center", fontsize=7.2, color=GREY)
    save(fig, "bio_ch12_fig02_energy_flow.png")


def _pyramid(ax, bars, title, inverted=False, unit=""):
    ax.set_xlim(-6, 6)
    ax.set_ylim(-0.4, len(bars) + 0.6)
    ax.axis("off")
    widths = [b[1] for b in bars]
    for i, (lab, w, val) in enumerate(bars):
        ax.add_patch(Rectangle((-w / 2, i), w, 0.85, fc=[PALE_GREEN, PALE_AMBER, PALE_RED, PALE_BLUE][i],
                               ec=[GREEN, AMBER, RED, BLUE][i], lw=1))
        if w < 0.42 * len(val):
            ax.text(w / 2 + 0.2, i + 0.42, val, ha="left", va="center", fontsize=7.6)
        else:
            ax.text(0, i + 0.42, val, ha="center", va="center", fontsize=7.6)
        ax.text(-5.9, i + 0.42, lab, ha="left", va="center", fontsize=7.6, color=GREY)
    ax.set_title(title, fontsize=8.8)


def fig03_pyramids():
    fig, axs = plt.subplots(2, 2, figsize=(9.6, 6.0))
    _pyramid(axs[0, 0], [("PP", 8.4, "5,842,424"), ("PC", 6.0, "708,624"), ("SC", 4.0, "354,904"),
                         ("TC", 1.2, "3")], "(a) Pyramid of numbers — grassland (upright)")
    _pyramid(axs[0, 1], [("PP", 8.4, "809"), ("PC", 4.6, "37"), ("SC", 2.8, "11"), ("TC", 1.6, "1.5")],
             "(b) Pyramid of biomass, kg m⁻² dry weight (upright)")
    _pyramid(axs[1, 0], [("PP", 2.4, "4 (phytoplankton)"), ("PC", 8.4, "21 (zooplankton)")],
             "(c) Pyramid of biomass in the sea, g m⁻² (inverted)")
    _pyramid(axs[1, 1], [("PP", 8.4, "10,000 J"), ("PC", 6.0, "1,000 J"), ("SC", 3.8, "100 J"),
                         ("TC", 1.8, "10 J")], "(d) Pyramid of energy (always upright)")
    axs[1, 1].text(0, 4.35, "1,000,000 J of sunlight", ha="center", fontsize=7.6, color=AMBER)
    fig.text(0.5, 0.0, "PP producers · PC primary consumers · SC secondary consumers · TC tertiary consumers",
             ha="center", fontsize=8.2, color=GREY)
    fig.tight_layout()
    save(fig, "bio_ch12_fig03_pyramids.png")


def fig04_food_chains():
    fig, a = canvas(9.4, 4.0, (0, 19), (0, 8.0))
    a.text(9.5, 7.6, "Grazing food chain (GFC) and detritus food chain (DFC)", ha="center", fontsize=10,
           weight="bold")
    gfc = [("Grass\n(producer)", PALE_GREEN, GREEN), ("Goat\n(primary\nconsumer)", PALE_AMBER, AMBER),
           ("Man\n(secondary\nconsumer)", PALE_RED, RED)]
    for i, (t, fc, ec) in enumerate(gfc):
        x = 1.0 + i * 4.4
        box(a, (x, 4.3), 3.2, 2.3, t, fc=fc, ec=ec, fs=8.2)
        if i < 2:
            arrow(a, (x + 3.2, 5.45), (x + 4.4, 5.45), ms=9)
    a.text(14.6, 5.45, "GFC: begins with living\nplants; major conduit of\nenergy in aquatic\necosystems", ha="left",
           va="center", fontsize=8)
    dfc = [("Dead leaves,\ndead animals\n(detritus)", PALE_AMBER, AMBER),
           ("Decomposers\n(bacteria, fungi;\nsaprotrophs)", SOFT, BLUE),
           ("Inorganic\nnutrients\n(to plants)", PALE_GREEN, GREEN)]
    for i, (t, fc, ec) in enumerate(dfc):
        x = 1.0 + i * 4.4
        box(a, (x, 0.6), 3.2, 2.3, t, fc=fc, ec=ec, fs=8.2)
        if i < 2:
            arrow(a, (x + 3.2, 1.75), (x + 4.4, 1.75), ms=9)
    a.text(14.6, 1.75, "DFC: begins with dead\norganic matter; larger\nenergy share in\nterrestrial ecosystems",
           ha="left", va="center", fontsize=8)
    save(fig, "bio_ch12_fig04_food_chains.png")


if __name__ == "__main__":
    fig01_decomposition()
    fig02_energy_flow()
    fig03_pyramids()
    fig04_food_chains()
