"""Figures for Class X Health and Physical Education, Ch03 (Unit I): Marriage and Family Life."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import table_fig, tree


def fig_requisites():
    tree("Requisites for a happy married life",
         ["Loving and\nbeing loved", "Emotional\ninterdependence", "Compatibility", "Common\ninterests", "Cooperation"],
         "hpe_ch03_fig01_requisites.png",
         grand={0: ["a loving attitude", "no hostility"],
                1: ["reliance on each other", "a sense of security"],
                2: ["traits always differ", "accept differences"],
                3: ["similar tastes", "reading, music, culture"],
                4: ["share domestic chores", "a cooperative home"]},
         width=10.5, child_w=1.85, size=8.4)


def fig_qualities():
    table_fig(["Qualities looked for in a bride-to-be", "Qualities looked for in a groom-to-be"],
              [["good health and healthy habits", "good physical health and healthy habits"],
               ["well educated", "well educated"],
               ["interests similar to those of the boy", "interests similar to those of the girl"],
               ["emotionally mature and balanced", "economically independent"],
               ["respect for the family she joins", "emotionally mature and balanced"]],
              "hpe_ch03_fig02_qualities.png", col_w=[5.3, 5.3],
              title="Choosing a life partner", size=8.4)


def fig_age():
    table_fig(["Marriage at the right age", "Early (child) marriage"],
              [["legal: 21 for a man, 18 for a woman", "illegal below these ages (Act of 2006)"],
               ["body fully grown; safer pregnancy", "teenage pregnancy; risk to mother and baby"],
               ["emotionally mature partners", "immature partners; more quarrels"],
               ["education completed; can earn", "education stops; poverty more likely"],
               ["family can be planned", "large family, little spacing"]],
              "hpe_ch03_fig03_age.png", col_w=[5.2, 5.4],
              title="Why the age at marriage matters", size=8.4)


if __name__ == "__main__":
    fig_requisites()
    fig_qualities()
    fig_age()
