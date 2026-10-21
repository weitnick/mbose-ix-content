"""Figures for Class X Social Science, Ch01 (History 1): The Rise of Nationalism in Europe."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import FILLS, INK, ACC, arrow, box, finish, save, timeline
import matplotlib.pyplot as plt


def fig_timeline():
    ev = [("1789", "French Revolution: sovereignty passes from the monarch to the citizens", 0),
          ("1804", "Napoleonic Civil Code: equality before the law, right to property", 0),
          ("1815", "Defeat of Napoleon; Treaty of Vienna restores conservative monarchies", 5),
          ("1821", "Greek struggle for independence begins (independent by 1832)", 1),
          ("1830", "July Revolution in France; Belgium breaks away from the Netherlands", 1),
          ("1834", "Zollverein: customs union of German states led by Prussia", 2),
          ("1848", "Revolution of the liberals; Frankfurt Parliament meets (May)", 2),
          ("1859–70", "Unification of Italy: Cavour, Garibaldi; Rome joins in 1870", 3),
          ("1866–71", "Unification of Germany under Prussia and Bismarck", 3),
          ("1871", "William I proclaimed German Emperor at Versailles (January)", 3)]
    timeline(ev, "ss_ch01_fig01_timeline.png", title="Rise of nationalism in Europe: key dates", label_w=7.2)


def fig_unification():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.4))
    for ax, title, steps, fill in (
            (axs[0], "Unification of Germany", [
                "Liberal attempt: Frankfurt\nParliament (1848) fails",
                "Prussia takes the lead;\nBismarck, the chief minister",
                "Three wars in seven years\nwith Denmark, Austria, France",
                "1871: William I proclaimed\nGerman Emperor at Versailles"], 2),
            (axs[1], "Unification of Italy", [
                "Mazzini's Young Italy;\nfailed revolts of 1831, 1848",
                "Sardinia-Piedmont under\nVictor Emmanuel II and Cavour",
                "1859: alliance with France\ndefeats Austria; 1860:\nGaribaldi's Red Shirts take\nthe south",
                "1861: Victor Emmanuel II\nking of united Italy;\n1870: Rome joins"], 3)):
        for i, s in enumerate(steps):
            y = 3.6 - i * 1.2
            box(ax, (0, y), s, FILLS[fill] if i < 3 else FILLS[0], w=3.6, h=0.95, size=8.2)
            if i:
                arrow(ax, (0, y + 1.2 - 0.48), (0, y + 0.48))
        ax.text(-1.8, 4.35, title, fontsize=10, fontweight="bold", color=ACC)
        finish(ax, (-2.0, 2.0), (-0.6, 4.6))
    save(fig, "ss_ch01_fig02_unification.png")


if __name__ == "__main__":
    fig_timeline()
    fig_unification()
