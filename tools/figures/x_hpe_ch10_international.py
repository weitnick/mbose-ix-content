"""Figures for Class X Health and Physical Education, Ch10 (Unit IV): International Health."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import table_fig, timeline, tree


def fig_orgs():
    tree("International health organisations",
         ["WHO", "UNICEF", "FAO", "CARE"],
         "hpe_ch10_fig01_orgs.png",
         grand={0: ["UN specialised agency", "headquarters: Geneva"],
                1: ["children and mothers", "headquarters: New York"],
                2: ["food and agriculture", "headquarters: Rome"],
                3: ["voluntary relief agency", "not a UN agency"]},
         width=10.0, child_w=2.3, size=8.6)


def fig_timeline():
    timeline([("1851", "First international sanitary conferences in Europe on controlling disease across borders", 0),
              ("1945", "FAO set up (16 October); CARE founded to send relief to war-torn Europe", 2),
              ("1946", "UNICEF established (11 December)", 1),
              ("1948", "WHO constitution comes into force on 7 April — World Health Day", 1),
              ("1951", "International Sanitary Regulations adopted", 0),
              ("1969", "Regulations replaced and renamed the International Health Regulations (IHR)", 0),
              ("2005", "IHR revised; today binding on 196 countries", 1)],
             "hpe_ch10_fig02_timeline.png", title="Milestones in international health", label_w=7.6)


def fig_compare():
    table_fig(["Organisation", "Full form", "Founded", "Main aim"],
              [["WHO", "World Health Organization", "1948", "highest possible level of health for all"],
               ["UNICEF", "United Nations Children's Fund", "1946", "help for children and mothers"],
               ["FAO", "Food and Agriculture Organization", "1945", "better nutrition, food production, rural life"],
               ["CARE", "Cooperative for Assistance and Relief Everywhere", "1945", "relief and development aid"]],
              "hpe_ch10_fig03_compare.png", col_w=[1.9, 5.5, 1.4, 4.4],
              title="Four international organisations compared", size=8.0)


if __name__ == "__main__":
    fig_orgs()
    fig_timeline()
    fig_compare()
