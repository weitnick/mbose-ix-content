"""Figures for Class X Social Science, Ch14 (Civics 3): Popular Struggles and Movements."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import table_fig, tree


def fig_cases():
    table_fig(["", "Nepal (2006)", "Bolivia (2000)"],
              [["Issue", "King Gyanendra dissolved Parliament", "water of Cochabamba sold to an MNC"],
               ["Type of struggle", "to restore democracy", "against a government policy"],
               ["Who led it", "Seven Party Alliance, Maoists, others", "FEDECOR, unions, farmers, students"],
               ["Method", "strike, mass protest, ultimatum", "general strikes, mass protest"],
               ["Result", "king gave in; monarchy ended 2008", "contract cancelled; old water rates"]],
              "ss_ch14_fig01_cases.png", col_w=[2.6, 4.6, 4.6], title="Two popular struggles compared", size=8.5)


def fig_groups():
    tree("Organisations that influence politics",
         ["Sectional interest groups", "Public interest groups", "Single-issue movements",
          "Long-term movements"],
         "ss_ch14_fig02_groups.png",
         grand={0: ["serve one section", "trade unions", "business associations", "doctors, lawyers"],
                1: ["serve the common good", "BAMCEF", "against bonded labour", "human rights groups"],
                2: ["one goal, short life", "Narmada Bachao Andolan", "Nepal's 2006 movement", "Bolivia water war"],
                3: ["many issues, umbrella", "environmental movement", "women's movement", "NAPM"]},
         width=10.5, child_w=2.4, size=8.2)


def fig_compare():
    table_fig(["Political parties", "Pressure groups"],
              [["Aim to win and use political power", "Do not aim to control political power"],
               ["Contest elections", "Do not contest elections"],
               ["Face the people in elections", "Not directly accountable to voters"],
               ["Take a stand on many issues", "Usually focus on particular interests"],
               ["Form governments or opposition", "Influence policies from outside"]],
              "ss_ch14_fig03_compare.png", col_w=[5.6, 5.6], title="Political parties and pressure groups", size=8.5)


if __name__ == "__main__":
    fig_cases()
    fig_groups()
    fig_compare()
