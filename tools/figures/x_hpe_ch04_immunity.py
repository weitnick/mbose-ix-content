"""Figures for Class X Health and Physical Education, Ch04 (Unit II): Some Defence Measures against Diseases."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import flow, table_fig, tree


def fig_antibodies():
    flow(["Germs enter\nthe body", "Antigens on the\ngerms stimulate\nthe body", "Body produces\nantibodies", "Antibodies\nkill the germs",
          "White blood cells\nswallow the\ndead germs"],
         "hpe_ch04_fig01_antibodies.png", width=10.5, w=1.95, h=1.2, size=8.4,
         title="How the body fights germs")


def fig_types():
    tree("Immunity",
         ["Natural (inborn)", "Natural acquired\n(active)", "Artificial acquired\n(active)", "Passive"],
         "hpe_ch04_fig02_types.png",
         grand={0: ["no prior infection", "species immunity"],
                1: ["after an attack", "e.g. chickenpox"],
                2: ["vaccines with antigens", "e.g. DPT, polio"],
                3: ["ready-made antibodies", "mother to foetus"]},
         width=10.0, child_w=2.2, size=8.6)


def fig_schedule():
    table_fig(["Age", "Vaccines (National Immunization Schedule, simplified)"],
              [["At birth", "BCG, Oral Polio Vaccine (OPV-0), Hepatitis B birth dose"],
               ["6, 10 and 14 weeks", "OPV 1–3, Pentavalent 1–3 (DPT + Hepatitis B + Hib), Rotavirus"],
               ["9–12 months", "Measles–Rubella (MR) 1, Vitamin A; JE-1 in endemic districts"],
               ["16–24 months", "MR 2, DPT booster-1, OPV booster; JE-2 in endemic districts"],
               ["5–6 years", "DPT booster-2"],
               ["10 and 16 years", "Td (tetanus and adult diphtheria)"],
               ["Pregnant women", "Td-1 and Td-2 (or a booster) — not given at birth"]],
              "hpe_ch04_fig03_schedule.png", col_w=[2.6, 8.4],
              title="When vaccines are given", size=8.2)


if __name__ == "__main__":
    fig_antibodies()
    fig_types()
    fig_schedule()
