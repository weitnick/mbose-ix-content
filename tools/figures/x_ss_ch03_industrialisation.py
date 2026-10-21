"""Figures for Class X Social Science, Ch03 (History 3): Industrialisation (1850s-1950s)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import ACC, FILLS, HI, INK, save, timeline
import matplotlib.pyplot as plt


def fig_timeline():
    ev = [("1730s", "Earliest factories appear in England", 0),
          ("1764", "James Hargreaves devises the Spinning Jenny", 0),
          ("1772", "Henry Patullo predicts Indian textiles will never lose demand", 1),
          ("1781", "James Watt patents his improved steam engine", 0),
          ("1811–12", "Piece-goods are 33% of India's exports (only 3% by 1850–51)", 5),
          ("1854", "First cotton mill in Bombay (production from 1856)", 2),
          ("1855", "First jute mill in Bengal; Elgin Mill, Kanpur, in the 1860s", 2),
          ("1874", "First spinning and weaving mill of Madras", 2),
          ("1917", "Seth Hukumchand sets up the first Indian jute mill in Calcutta", 3),
          ("1914–18", "First World War: Manchester imports fall, Indian mills expand", 3),
          ("1941", "Over 35% of handlooms fitted with the fly shuttle", 4)]
    timeline(ev, "ss_ch03_fig01_timeline.png", title="Industrialisation: key dates", label_w=7.2)


def fig_trade():
    fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.6))
    ax = axs[0]
    ax.bar(["1811–12", "1850–51"], [33, 3], color=[FILLS[2], FILLS[3]], edgecolor=INK)
    ax.set_ylim(0, 40)
    ax.set_ylabel("% of India's exports", fontsize=9)
    ax.set_title("Indian piece-goods in India's EXPORTS", fontsize=9.5)
    for i, v in enumerate([33, 3]):
        ax.text(i, v + 1, f"{v}%", ha="center", fontsize=9, fontweight="bold")
    ax = axs[1]
    ax.bar(["end of 1700s", "1850", "1870s"], [0, 31, 50], color=[FILLS[0], FILLS[1], FILLS[3]], edgecolor=INK)
    ax.set_ylim(0, 60)
    ax.set_ylabel("% of India's imports", fontsize=9)
    ax.set_title("British cotton piece-goods in India's IMPORTS", fontsize=9.5)
    for i, (v, t) in enumerate(zip([0, 31, 50], ["almost nil", "over 31%", "over 50%"])):
        ax.text(i, v + 1.2, t, ha="center", fontsize=9, fontweight="bold")
    for a in axs:
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
    fig.suptitle("The reversal of India's textile trade", fontsize=10.5, fontweight="bold", color=ACC)
    fig.tight_layout()
    save(fig, "ss_ch03_fig02_textile_trade.png")


if __name__ == "__main__":
    fig_timeline()
    fig_trade()
