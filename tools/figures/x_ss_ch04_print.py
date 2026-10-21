"""Figures for Class X Social Science, Ch04 (History 5): Print Culture and Nationalism."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import timeline, tree


def fig_timeline():
    ev = [("594", "Woodblock printing in China (from about AD 594)", 0),
          ("868", "Diamond Sutra printed in Japan, the oldest Japanese book", 0),
          ("1295", "Marco Polo brings knowledge of woodblock printing to Italy", 0),
          ("1448", "Gutenberg perfects the printing press; the Bible is his first book", 1),
          ("1517", "Martin Luther's Ninety-Five Theses; the Reformation begins", 1),
          ("1558", "Roman Church starts the Index of Prohibited Books", 1),
          ("1556", "Portuguese missionaries bring the press to Goa (mid-16th century)", 2),
          ("1579", "First Tamil book printed at Cochin", 2),
          ("1780", "James Augustus Hickey's Bengal Gazette, Calcutta", 3),
          ("1821", "Rammohun Roy's Sambad Kaumudi", 3),
          ("1878", "Vernacular Press Act", 5),
          ("1908", "Tilak imprisoned for writing in Kesari about deported revolutionaries", 5)]
    ev.sort(key=lambda e: int(e[0]))
    timeline(ev, "ss_ch04_fig01_timeline.png", title="Print culture: key dates", label_w=7.4)


def fig_uses():
    tree("Print culture in 19th- and 20th-century India",
         ["Religious reformers", "Women", "The poor and workers", "Nationalists"],
         "ss_ch04_fig02_uses.png",
         grand={0: ["Sambad Kaumudi (1821)", "Deoband fatwas", "Ramcharitmanas (1810)"],
                1: ["Amar Jiban (1876)", "journals for women", "Battala books"],
                2: ["Gulamgiri (1871)", "Kashibaba (1938)", "workers' libraries"],
                3: ["newspapers spread news", "criticised colonial rule", "Kesari (Tilak)"]},
         width=10.0, child_w=2.2)


if __name__ == "__main__":
    fig_timeline()
    fig_uses()
