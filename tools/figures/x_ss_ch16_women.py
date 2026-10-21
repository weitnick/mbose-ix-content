"""Figures for Class X Social Science, Ch16 (Civics 7): Women's Rights in India."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import table_fig, timeline, tree


def fig_constitution():
    tree("Women's rights in the Constitution",
         ["Fundamental Rights", "Directive Principles", "Fundamental Duty", "Local government"],
         "ss_ch16_fig01_constitution.png",
         grand={0: ["Art. 14: equality before law", "Art. 15: no discrimination by sex", "Art. 16: equal job chances",
                    "Art. 21: life with dignity", "Art. 23: no trafficking, forced labour"],
                1: ["Art. 39(a): equal livelihood", "Art. 39(d): equal pay", "Art. 42: maternity relief"],
                2: ["Art. 51A(e): respect women"],
                3: ["Art. 243D: 1/3 panchayat seats", "Art. 243T: 1/3 municipal seats"]},
         width=11.0, child_w=2.5, size=8.0)


def fig_laws():
    ev = [("1856", "Hindu Widows' Remarriage Act", 0),
          ("1961", "Dowry Prohibition Act; Maternity Benefit Act", 1),
          ("1976", "Equal Remuneration Act: equal pay for equal work", 1),
          ("1992", "National Commission for Women; 73rd–74th Amendments", 2),
          ("1994", "PCPNDT Act: bans sex selection", 2),
          ("2005", "Protection of Women from Domestic Violence Act", 3),
          ("2006", "Prohibition of Child Marriage Act", 3),
          ("2013", "Sexual Harassment of Women at Workplace Act", 4),
          ("2023", "106th Amendment: 1/3 seats for women in legislatures", 5)]
    timeline(ev, "ss_ch16_fig02_laws.png", title="Some laws for women's rights", label_w=7.2)


def fig_challenges():
    table_fig(["Challenge", "Measure"],
              [["Girls kept out of school", "free education, scholarships, Beti Bachao Beti Padhao"],
               ["Unequal pay and jobs", "equal pay laws; equal opportunity; skills and credit"],
               ["Domestic violence, dowry", "strict enforcement; helplines; one-stop centres"],
               ["Harassment at work", "internal complaints committees (2013 Act)"],
               ["Few women in politics", "1/3 seats in local bodies; reservation in legislatures"],
               ["Stereotypes and customs", "awareness through schools, media, community"]],
              "ss_ch16_fig03_challenges.png", col_w=[4.4, 7.2], title="Challenges to women's equality and measures",
              size=8.4)


if __name__ == "__main__":
    fig_constitution()
    fig_laws()
    fig_challenges()
