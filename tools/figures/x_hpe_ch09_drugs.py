"""Figures for Class X Health and Physical Education, Ch09 (Unit III): Drugs, Medicines and Self-Medication."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import table_fig, tree


def fig_categories():
    tree("Categories of drugs with abuse potential",
         ["Narcotics", "Depressants", "Stimulants", "Hallucinogens"],
         "hpe_ch09_fig01_categories.png",
         grand={0: ["sleep, numbness, pain relief", "codeine, novocaine, morphine"],
                1: ["soothing; less anxiety", "bromides, barbiturates, alcohol"],
                2: ["excitement; less sleep", "amphetamines"],
                3: ["change mental and visual perception", "used only in medical research"]},
         width=10.5, child_w=2.4, size=8.3)


def fig_alcohols():
    table_fig(["Alcohol", "Other name", "Use or effect"],
              [["Ethyl alcohol", "ethanol", "the alcohol in wine, beer and spirits (drinking)"],
               ["Methyl alcohol", "methanol", "deadly poisonous; causes blindness and even death"],
               ["Isopropyl alcohol", "rubbing alcohol", "solvent and cleaning agent"]],
              "hpe_ch09_fig02_alcohols.png", col_w=[2.8, 2.6, 6.0],
              title="Three alcohols to know", size=8.6)


def fig_safe_use():
    table_fig(["Do", "Do not"],
              [["consult a qualified doctor in illness", "go to an uninformed quack"],
               ["take medicines exactly as prescribed", "use medicine prescribed for someone else"],
               ["read the label of non-prescription drugs", "use non-prescription drugs indiscriminately"],
               ["see a doctor if symptoms persist or repeat", "use leftover medicine from an earlier illness"],
               ["seek help at once for chest pain or blackout", "ignore side effects or allergies (e.g. penicillin)"]],
              "hpe_ch09_fig03_safe_use.png", col_w=[5.6, 5.6],
              title="Safe use of medicines", size=8.4)


if __name__ == "__main__":
    fig_categories()
    fig_alcohols()
    fig_safe_use()
