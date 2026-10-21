"""Figures for Class X Social Science, Ch15 (Civics 4): Political Parties."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import table_fig, tree


def fig_functions():
    tree("Functions of political parties",
         ["Contest\nelections", "Offer\npolicies", "Make\nlaws", "Form and run\ngovernments", "Act as\nopposition",
          "Shape public\nopinion", "Give access to\ngovernment"],
         "ss_ch15_fig01_functions.png", width=11.5, child_w=1.55, size=7.8)


def fig_systems():
    table_fig(["Party system", "What it means", "Examples"],
              [["One-party", "only one party is allowed to rule", "China"],
               ["Two-party", "power usually alternates between two main parties", "USA, UK"],
               ["Multi-party", "several parties compete; alone or in alliances", "India"]],
              "ss_ch15_fig02_systems.png", col_w=[2.4, 6.6, 2.4], title="Party systems", size=8.6)


def fig_national():
    table_fig(["National party", "Founded", "Remember"],
              [["Indian National Congress (INC)", "1885", "oldest party; led the freedom movement"],
               ["Bharatiya Janata Party (BJP)", "1980", "revived the Bharatiya Jana Sangh (1951)"],
               ["Communist Party of India (Marxist)", "1964", "Marxism-Leninism; socialism"],
               ["Bahujan Samaj Party (BSP)", "1984", "founded by Kanshi Ram; Dalit and weaker sections"],
               ["Aam Aadmi Party (AAP)", "2012", "anti-corruption movement; national party 2023"],
               ["National People's Party (NPP)", "2013", "P. A. Sangma; first NE party to go national (2019)"]],
              "ss_ch15_fig03_national.png", col_w=[4.6, 1.6, 5.6], title="Recognised national parties (2023)",
              size=8.4)


def fig_reforms():
    table_fig(["Challenge", "Reform or remedy"],
              [["Lack of internal democracy", "regular organisational elections; membership registers"],
               ["Dynastic succession", "open, rule-based choice of leaders and candidates"],
               ["Money and muscle power", "affidavits on assets and criminal cases; transparent funding"],
               ["No meaningful choice", "clear policies; pressure from people, media, movements"],
               ["Defection by MLAs and MPs", "Anti-Defection Law: a member who switches loses the seat"],
               ["Few women in parties", "suggested: one-third tickets and posts for women"]],
              "ss_ch15_fig04_reforms.png", col_w=[4.2, 7.4], title="Challenges to parties and reforms", size=8.4)


if __name__ == "__main__":
    fig_functions()
    fig_systems()
    fig_national()
    fig_reforms()
