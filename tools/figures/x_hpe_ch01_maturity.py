"""Figures for Class X Health and Physical Education, Ch01 (Unit I): How Mature Are You?"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import flow, table_fig, tree


def fig_stages():
    flow(["Infancy\nbirth to about\n2 years", "Childhood\nabout 2 to\n10–12 years", "Adolescence\nabout 10–12\nto 19 years",
          "Adulthood\nfrom about\n19–20 years"],
         "hpe_ch01_fig01_stages.png", width=9.5, w=2.05, h=1.15, size=8.6,
         title="Stages of growth (striking changes in the body take place in adolescence)")


def fig_aspects():
    tree("Aspects of maturity",
         ["Chronological", "Physical", "Intellectual", "Emotional", "Social", "Philosophical"],
         "hpe_ch01_fig02_aspects.png",
         grand={0: ["age in birthdays", "cannot be hurried"],
                1: ["full height and weight", "full strength"],
                2: ["thinking and judging", "independent decisions"],
                3: ["control of feelings", "charming personality"],
                4: ["gets along with people", "learnt gradually"],
                5: ["values and goals", "a mission in life"]},
         width=11.5, child_w=1.75, size=8.2)


def fig_intellectual():
    table_fig(["An intellectually mature person …", "An immature person …"],
              [["understands words, figures and symbols of his culture", "cannot handle ideas beyond the obvious"],
               ["takes decisions independently", "waits for advice or prompting from others"],
               ["looks at problems impartially and objectively", "sees problems only from his own side"],
               ["accepts his mistakes", "shifts the blame on to others"],
               ["weighs pros and cons before judging", "makes hasty judgements, like a child"]],
              "hpe_ch01_fig03_intellectual.png", col_w=[5.6, 5.0],
              title="How intellectual maturity can be judged", size=8.2)


if __name__ == "__main__":
    fig_stages()
    fig_aspects()
    fig_intellectual()
