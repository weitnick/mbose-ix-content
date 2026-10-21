"""Figures for Class X Health and Physical Education, Ch13 (Unit V): Basic Facts about HIV/AIDS."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import flow, table_fig, tree


def fig_progress():
    flow(["HIV enters the\nbody (infection)", "Virus attacks cells\nof the immune\nsystem", "Immune system\nslowly weakens",
          "Other infections\nand cancers\ntake hold", "AIDS — the final,\nmost severe stage"],
         "hpe_ch13_fig01_progress.png", width=10.5, w=1.95, h=1.2, size=8.2,
         title="From HIV infection to AIDS (about 8–10 years without treatment)")


def fig_routes():
    table_fig(["HIV IS passed on through", "HIV is NOT passed on through"],
              [["unprotected sex with an infected person", "shaking hands, hugging or kissing"],
               ["contaminated blood, blood products or transfusions", "coughs and sneezes"],
               ["shared needles and syringes (injecting drug users)", "sharing food, utensils or water fountains"],
               ["semen donation, skin grafts or organ transplants", "swimming pools and toilet seats"],
               ["infected mother to baby: pregnancy, delivery, breastfeeding", "mosquitoes, other insects or animals"]],
              "hpe_ch13_fig02_routes.png", col_w=[6.3, 5.0],
              title="How HIV is and is not transmitted", size=8.2)


def fig_cofactors():
    tree("Cofactors that speed up HIV disease",
         ["Genetic\nfactors", "Age", "Gender", "Route of\ninfection", "Smoking", "Nutrition", "Other\ninfections"],
         "hpe_ch13_fig03_cofactors.png",
         width=11.0, child_w=1.35, size=8.2)


if __name__ == "__main__":
    fig_progress()
    fig_routes()
    fig_cofactors()
