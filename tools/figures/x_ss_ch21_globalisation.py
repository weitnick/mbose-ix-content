"""Figures for Class X Social Science, Ch21 (Economics 4): Globalisation and the Indian Economy."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import flow, table_fig, tree


def fig_mnc_chain():
    flow(["Design\nresearch centres\nin the USA", "Components\nmade in\nChina", "Assembly\nin Mexico and\nEastern Europe",
          "Sales\nall over\nthe world", "Customer care\ncall centres\nin India"],
         "ss_ch21_fig01_mnc_chain.png", width=10.5, w=1.95, h=1.15, size=8.2,
         title="How an MNC spreads production across countries (NCERT example)")


def fig_ways():
    tree("How MNCs link production across countries",
         ["Joint production with\nlocal companies", "Buying up local\ncompanies", "Orders to small\nproducers"],
         "ss_ch21_fig02_ways.png",
         grand={0: ["money and new technology"],
                1: ["Cargill bought Parakh Foods"],
                2: ["garments, shoes, sports goods"]},
         width=9.5, child_w=2.9, size=8.6)


def fig_impact():
    table_fig(["Gained from globalisation", "Lost or faced hardship"],
              [["Urban consumers: more choice, quality, lower prices", "Small producers: batteries, capacitors, toys, dairy, oil"],
               ["Top Indian companies: new technology, collaborations", "Workers: insecure jobs, long hours, less protection"],
               ["Indian MNCs: Tata Motors, Infosys, Asian Paints", "Farmers in poor countries facing subsidised imports"],
               ["IT and service firms: new jobs", "Developing countries pressed to remove barriers"]],
              "ss_ch21_fig03_impact.png", col_w=[6.2, 6.2], title="Impact of globalisation in India", size=8.0)


if __name__ == "__main__":
    fig_mnc_chain()
    fig_ways()
    fig_impact()
