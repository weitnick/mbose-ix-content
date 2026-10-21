"""Figures for Class X Health and Physical Education, Ch14 (Unit V): Prevention against HIV/AIDS."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import flow, table_fig, tree


def fig_abc():
    tree("The ABC of safety against sexual transmission",
         ["A — Abstain\nfrom sex", "B — Be faithful\nto one partner", "C — Condoms used\nconsistently and\ncorrectly"],
         "hpe_ch14_fig01_abc.png",
         grand={0: ["the surest protection", "for young people"],
                1: ["one uninfected partner", "faithful to each other"],
                2: ["every time", "the right way"]},
         width=9.5, child_w=2.8, size=8.6)


def fig_routes():
    table_fig(["Route of transmission", "How to prevent it"],
              [["Sexual contact", "abstinence; faithfulness; condoms; treat other STIs; male circumcision lowers risk"],
               ["Blood and needles", "screen all donated blood; sterile, disposable syringes; never share needles"],
               ["Health care settings", "universal precautions: hand washing, gloves, masks, safe disposal"],
               ["Mother to child", "antiretroviral drugs; caesarean section; safe feeding choices"],
               ["All routes", "awareness and education; counselling and testing; antiretroviral treatment"]],
              "hpe_ch14_fig02_routes.png", col_w=[3.4, 9.2],
              title="Preventing HIV route by route", size=8.2)


def fig_pmtct():
    flow(["Prevent HIV in\nwomen and avoid\nunwanted pregnancy", "Antiretroviral drugs\nin pregnancy\nand labour", "Caesarean section\nto reduce exposure",
          "Antiretroviral drugs\nfor the newborn", "Safe feeding as\nadvised by\nthe doctor"],
         "hpe_ch14_fig03_pmtct.png", width=11.0, w=2.05, h=1.25, size=8.0,
         title="Protecting the baby of an HIV-positive mother")


if __name__ == "__main__":
    fig_abc()
    fig_routes()
    fig_pmtct()
