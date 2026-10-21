"""Figures for Class X Health and Physical Education, Ch02 (Unit I): You and Your Family."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import table_fig, tree


def fig_types():
    tree("Types of family",
         ["Nuclear family", "Joint (extended) family"],
         "hpe_ch02_fig01_types.png",
         grand={0: ["husband, wife and their unmarried children", "small, more privacy",
                    "common in towns and cities"],
                1: ["grandparents, parents, uncles, aunts and cousins", "share one home, kitchen and income",
                    "support in crisis, help in raising children"]},
         width=9.0, child_w=3.6, size=8.8)


def fig_compare():
    table_fig(["Joint family", "Nuclear family"],
              [["economic help from many earning members", "less economic support in hard times"],
               ["refuge in events of crisis", "family must face a crisis largely alone"],
               ["help in bringing up the children", "both parents may struggle if both work"],
               ["advice and guidance from elders", "more independence in decisions"],
               ["little privacy; adjustment problems", "more privacy; fewer adjustment problems"]],
              "hpe_ch02_fig02_compare.png", col_w=[5.2, 5.2],
              title="Joint and nuclear families compared", size=8.4)


def fig_expectations():
    table_fig(["What parents expect of you", "What you may expect of your parents"],
              [["have polite manners", "love, care and a sense of security"],
               ["be well-groomed", "trust and understanding"],
               ["maintain good relations with people around you", "guidance and advice when needed"],
               ["be respectful to elders and parents", "respect for your views and some privacy"],
               ["behave in a responsible way; be truthful and honest", "freedom that grows with your responsibility"]],
              "hpe_ch02_fig03_expectations.png", col_w=[5.4, 5.0],
              title="Expectations on both sides", size=8.4)


if __name__ == "__main__":
    fig_types()
    fig_compare()
    fig_expectations()
