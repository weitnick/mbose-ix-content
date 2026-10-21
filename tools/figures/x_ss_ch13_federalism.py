"""Figures for Class X Social Science, Ch13 (Civics 2): Nature of Indian Federal Structure."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import table_fig, tree


def fig_lists():
    tree("Division of legislative powers",
         ["Union List", "State List", "Concurrent List", "Residuary subjects"],
         "ss_ch13_fig01_lists.png",
         grand={0: ["Parliament makes laws", "defence, foreign affairs", "banking, currency", "communications"],
                1: ["State legislatures make laws", "police, trade, commerce", "agriculture, irrigation"],
                2: ["both can make laws", "Union law prevails", "education, forest", "marriage, trade unions"],
                3: ["not in any list", "Union has power", "e.g. computer software"]},
         width=10.0, child_w=2.3, size=8.2)


def fig_routes():
    table_fig(["", "Coming together federation", "Holding together federation"],
              [["How formed", "independent states join", "a large country divides power"],
               ["Units' strength", "states strong and equal", "Centre stronger"],
               ["Units' powers", "usually equal", "can be unequal; some special"],
               ["Examples", "USA, Switzerland, Australia", "India, Spain, Belgium"]],
              "ss_ch13_fig02_routes.png", col_w=[2.6, 4.4, 4.4], title="Two routes to federation", size=8.6)


def fig_features():
    table_fig(["Federal features", "Unitary features"],
              [["Two (now three) tiers of government", "Strong Centre; residuary powers with the Union"],
               ["Written, supreme Constitution", "Single Constitution and single citizenship"],
               ["Union, State and Concurrent Lists", "Emergency provisions (Articles 352, 356, 360)"],
               ["Independent judiciary as umpire", "Governor appointed by the President"],
               ["Separate sources of revenue", "Parliament can alter state boundaries"],
               ["Rigid amendment of key provisions", "All India Services; integrated judiciary"]],
              "ss_ch13_fig03_features.png", col_w=[5.4, 6.0], title="India: a federation with unitary features",
              size=8.4)


def fig_local():
    tree("Local self-government (73rd and 74th Amendments, 1992)",
         ["Rural: Panchayati Raj", "Urban local bodies"],
         "ss_ch13_fig04_local.png",
         grand={0: ["Gram Sabha: all voters of the village", "Gram Panchayat: sarpanch and panches",
                    "Panchayat Samiti (block)", "Zila Parishad (district): apex body"],
                1: ["Municipality (towns): chairperson", "Municipal Corporation (cities): mayor",
                    "elected by the people", "share powers and revenue"]},
         width=9.6, child_w=3.6, size=8.4)


if __name__ == "__main__":
    fig_lists()
    fig_routes()
    fig_features()
    fig_local()
