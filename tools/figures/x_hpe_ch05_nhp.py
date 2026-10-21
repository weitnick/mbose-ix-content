"""Figures for Class X Health and Physical Education, Ch05 (Unit II): National Health Programmes."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import table_fig, timeline, tree


def fig_areas():
    tree("Five broad areas of the National Health Programmes",
         ["Reproductive, maternal,\nneonatal, child and\nadolescent health", "Nutrition", "Communicable\ndiseases",
          "Non-communicable\ndiseases", "Health system\nstrengthening"],
         "hpe_ch05_fig01_areas.png",
         grand={0: ["family planning", "immunization"],
                1: ["mid-day meals", "vitamin A, iron"],
                2: ["TB, leprosy", "malaria, AIDS"],
                3: ["cancer, diabetes", "heart disease"],
                4: ["PHCs, ASHAs", "training, supplies"]},
         width=11.0, child_w=2.0, size=8.2)


def fig_timeline():
    timeline([("1952", "Family Planning Programme — India the first country with an official programme", 0),
              ("1953", "National Malaria Control Programme", 1),
              ("1955", "National Leprosy Control Programme (sulfone treatment at home)", 1),
              ("1960", "Applied Nutrition Programme begins", 2),
              ("1962", "National Tuberculosis Control Programme", 1),
              ("1963", "National Trachoma Control Programme", 1),
              ("1985", "Universal Immunization Programme", 0),
              ("1987", "National AIDS Control Programme (NACO set up in 1992)", 1),
              ("2000", "National Population Policy — stabilise population by 2045", 0),
              ("2003–04", "National Vector Borne Disease Control Programme", 1),
              ("2014", "Mission Indradhanush", 0)],
             "hpe_ch05_fig02_timeline.png", title="Some national health programmes and when they began", label_w=7.4)


def fig_participation():
    table_fig(["Programme", "How the public can help"],
              [["Vector-borne diseases (malaria, dengue)", "no stagnant water; one dry day a week; help spraying; report fevers"],
               ["Tuberculosis", "report a cough lasting over two weeks; complete the treatment"],
               ["Leprosy", "report pale, numb skin patches early; do not shun patients"],
               ["Immunization", "take every child for every dose on time"],
               ["Nutrition", "use iron, folic acid and vitamin A supplements; eat local foods"],
               ["Family welfare", "plan a small family; space births"]],
              "hpe_ch05_fig03_participation.png", col_w=[4.1, 8.0],
              title="Public participation in health programmes", size=8.2)


if __name__ == "__main__":
    fig_areas()
    fig_timeline()
    fig_participation()
