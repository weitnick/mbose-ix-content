"""Figures for Class X Health and Physical Education, Ch11 (Unit V): Life Skills Education and Teenage Pregnancy."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import table_fig, tree


def fig_life_skills():
    tree("Five areas of life skills (WHO)",
         ["Self-awareness\nand empathy", "Communication and\ninterpersonal\nrelationships", "Decision making\nand problem\nsolving",
          "Creative thinking\nand critical\nthinking", "Coping with\nemotions and\nstress"],
         "hpe_ch11_fig01_life_skills.png",
         grand={0: ["know yourself", "feel for others"],
                1: ["express clearly", "build relationships"],
                2: ["weigh the options", "act on the best one"],
                3: ["new ideas", "analyse information"],
                4: ["recognise stress", "take remedial steps"]},
         width=11.0, child_w=1.95, size=8.0)


def fig_effects():
    table_fig(["Health effects on the teenage mother", "Health effects on her baby"],
              [["anaemia (iron deficiency)", "premature birth"],
               ["pregnancy-induced high blood pressure", "low birth weight"],
               ["lower genital tract infections", "acute infections"],
               ["caesarean section; baby too large for a small pelvis", "accidental injury and poisoning"],
               ["foetal distress; risk of infant death", "delay in development"]],
              "hpe_ch11_fig02_effects.png", col_w=[6.0, 4.6],
              title="Health risks of teenage pregnancy", size=8.4)


def fig_prevention():
    table_fig(["Risk factor (behaviour pattern)", "Protective step"],
              [["early dating behaviour", "education on abstinence and responsible behaviour"],
               ["lack of a support group; few friends", "trusted adults, counsellors, school clubs"],
               ["unhealthy environment at home", "open communication with parents"],
               ["stress and depression", "life skills: coping with stress; help from counsellors"],
               ["financial constraints", "staying in school; schemes for girls"]],
              "hpe_ch11_fig03_prevention.png", col_w=[5.0, 6.2],
              title="Teenage pregnancy: risk factors and protective steps", size=8.3)


if __name__ == "__main__":
    fig_life_skills()
    fig_effects()
    fig_prevention()
