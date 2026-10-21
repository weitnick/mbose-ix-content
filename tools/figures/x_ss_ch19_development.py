"""Figures for Class X Social Science, Ch19 (Economics 2): The Story of Development."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import flow, table_fig, tree


def fig_goals():
    table_fig(["Category of person", "Possible developmental goals"],
              [["Landless rural labourer", "more days of work, better wages, a local school"],
               ["Prosperous farmer", "assured high income, higher support prices"],
               ["Farmer relying on rain", "irrigation; protection from crop failure"],
               ["Urban unemployed youth", "a good, secure job"],
               ["Girl from a rich urban family", "as much freedom as her brother"],
               ["Tribal family near a dam site", "no displacement; land and forest rights"]],
              "ss_ch19_fig01_goals.png", col_w=[4.6, 7.0], title="Different people, different goals", size=8.5)


def fig_indicators():
    tree("Measuring development",
         ["Income measures", "Health", "Education", "Composite"],
         "ss_ch19_fig02_indicators.png",
         grand={0: ["National income", "Real national income", "Per capita income"],
                1: ["Infant mortality rate", "Life expectancy"],
                2: ["Literacy rate", "Net attendance ratio"],
                3: ["HDI (UNDP)"]},
         width=10.0, child_w=2.4, size=8.4)


def fig_hdi():
    tree("Human Development Index (UNDP)",
         ["A long and healthy life", "Knowledge", "A decent standard of living"],
         "ss_ch19_fig03_hdi.png",
         grand={0: ["life expectancy at birth"], 1: ["years of schooling"], 2: ["per capita income"]},
         width=9.0, child_w=2.9, size=8.6)


if __name__ == "__main__":
    fig_goals()
    fig_indicators()
    fig_hdi()
