"""Figures for Class X Health and Physical Education, Ch06 (Unit II): Primary Health Care Set-up in Urban and Rural Areas."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import flow, table_fig, tree


def fig_levels():
    flow(["Centre\nHealth Ministry\nand DGHS", "State\nHealth Department\nand Directorate", "District\nChief Medical\nOfficer",
          "Block\nCHC and PHC", "Sub-centre\nANM and\nhealth worker", "Village\nASHA and\nthe people"],
         "hpe_ch06_fig01_levels.png", width=12.0, w=1.75, h=1.15, size=8.2,
         title="Levels of health administration in India")


def fig_rural():
    tree("Rural health care set-up",
         ["Sub-centre", "Primary Health Centre (PHC)", "Community Health Centre (CHC)"],
         "hpe_ch06_fig02_rural.png",
         grand={0: ["first contact point", "about 10,000 people (textbook)", "ANM and male health worker"],
                1: ["one for each development block", "60,000–1,00,000 people (textbook)", "medical officer and staff"],
                2: ["referral centre for PHCs", "specialists and 30 beds", "X-ray and laboratory"]},
         width=10.0, child_w=3.0, size=8.4)


def fig_phc():
    table_fig(["Function of the PHC", "What it includes"],
              [["Medical care", "elementary treatment of minor ailments; emergency care; out-patients"],
               ["Control of communicable diseases", "watch on outbreaks, particularly malaria; national programmes"],
               ["Maternal and child welfare; family planning", "care of mothers and children; immunization; spacing of births"],
               ["Environmental sanitation", "safe drinking water; sanitary disposal of wastes"],
               ["School health and nutrition education", "growth checks, early detection, healthy school living"],
               ["Vital statistics and health education", "recording births and deaths; teaching healthy habits"]],
              "hpe_ch06_fig03_phc.png", col_w=[4.9, 7.8],
              title="Functions of a Primary Health Centre", size=8.2)


if __name__ == "__main__":
    fig_levels()
    fig_rural()
    fig_phc()
