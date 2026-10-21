"""Figures for Class X Social Science, Ch17 (Civics 9): The Rights of Persons with Disabilities Act, 2016."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import table_fig, tree


def fig_features():
    tree("The RPwD Act, 2016: key provisions",
         ["Who is covered", "Education", "Employment", "Accessibility", "Institutions"],
         "ss_ch17_fig01_features.png",
         grand={0: ["21 types of disability", "benchmark: 40% or more", "certificate from authority"],
                1: ["free education, 6–18 yrs", "inclusive schools", "5% seats in colleges"],
                2: ["4% of govt vacancies", "no discrimination", "incentives to employers"],
                3: ["barrier-free buildings", "accessible transport", "accessible voting"],
                4: ["Chief Commissioner", "State Commissioners", "Special Courts", "disability funds"]},
         width=11.0, child_w=2.1, size=8.0)


def fig_compare():
    table_fig(["", "1995 Act", "RPwD Act, 2016"],
              [["Types of disability", "7", "21"],
               ["Reservation in government jobs", "3%", "4%"],
               ["Reservation in higher education", "3%", "5%"],
               ["Free education", "up to 18 years", "6 to 18 years (benchmark disability)"],
               ["Approach", "welfare and charity", "rights, dignity and inclusion (UNCRPD)"],
               ["Penalties for violations", "limited", "fines and imprisonment; Special Courts"]],
              "ss_ch17_fig02_compare.png", col_w=[4.2, 3.0, 5.0], title="From the 1995 Act to the 2016 Act", size=8.4)


def fig_principles():
    tree("Principles of the Act",
         ["Dignity and\nautonomy", "Non-\ndiscrimination", "Inclusion and\nparticipation", "Equality of\nopportunity",
          "Accessibility"],
         "ss_ch17_fig03_principles.png",
         grand={0: ["own choices"], 1: ["equal treatment"], 2: ["full community life"], 3: ["equal chances"],
                4: ["no barriers"]},
         width=11.0, child_w=2.1, size=8.0)


if __name__ == "__main__":
    fig_features()
    fig_compare()
    fig_principles()
