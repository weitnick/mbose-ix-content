"""Figures for Class X Social Science, Ch18 (Economics 1): Sectors of the Indian Economy."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import flow, table_fig, tree


def fig_classify():
    tree("Ways of classifying the economy",
         ["Nature of activity", "Conditions of employment", "Ownership of assets"],
         "ss_ch18_fig01_classify.png",
         grand={0: ["Primary: from nature", "Secondary: manufacturing", "Tertiary: services"],
                1: ["Organised: regular, registered", "Unorganised: small, scattered"],
                2: ["Public: government owns", "Private: individuals, companies"]},
         width=10.0, child_w=3.0, size=8.4)


def fig_chain():
    flow(["Primary\ncotton grown\non a farm", "Secondary\ncotton spun and\nwoven into cloth",
          "Tertiary\ncloth transported,\nstored and sold"],
         "ss_ch18_fig02_chain.png", width=9.0, w=2.6, h=1.1, size=8.6,
         title="How the three sectors depend on each other")


def fig_compare():
    table_fig(["Organised sector", "Unorganised sector"],
              [["Registered with the government", "Small, scattered, outside government control"],
               ["Follows laws (Factories Act, Minimum Wages Act)", "Rules exist but are not followed"],
               ["Regular, secure jobs; fixed hours", "Low-paid, irregular, insecure jobs"],
               ["Paid leave, provident fund, medical benefits", "No paid leave or benefits"],
               ["Overtime pay", "No overtime pay; can be dismissed any time"]],
              "ss_ch18_fig03_organised.png", col_w=[5.8, 5.8], title="Organised and unorganised sectors", size=8.4)


if __name__ == "__main__":
    fig_classify()
    fig_chain()
    fig_compare()
