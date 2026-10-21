"""Figures for Class X Health and Physical Education, Ch07 (Unit III): Consumer Education."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import table_fig, tree


def fig_rights():
    tree("Rights of a consumer",
         ["Right to\nsafety", "Right to be\ninformed", "Right to\nchoose", "Right to be\nheard", "Right to seek\nredressal",
          "Right to consumer\neducation"],
         "hpe_ch07_fig01_rights.png",
         grand={0: ["no harmful goods"],
                1: ["price, quality, expiry"],
                2: ["many brands, fair price"],
                3: ["complaints considered"],
                4: ["compensation for loss"],
                5: ["learn to buy wisely"]},
         width=11.5, child_w=1.75, size=8.0)


def fig_adulteration():
    table_fig(["Food", "Common adulterant", "Simple test or effect"],
              [["Milk", "water, starch", "drop slides fast leaving no trail; iodine turns starch blue"],
               ["Turmeric powder", "metanil yellow (a dye)", "a few drops of acid turn it pink; dye may cause cancer"],
               ["Chilli powder", "brick powder", "brick powder sinks quickly in water"],
               ["Black pepper", "dried papaya seeds", "papaya seeds float on water"],
               ["Mustard oil", "argemone oil", "causes epidemic dropsy"],
               ["Arhar dal", "kesari dal", "causes lathyrism (paralysis of legs)"],
               ["Tea leaves", "used, coloured leaves", "colour runs on wet white paper"]],
              "hpe_ch07_fig02_adulteration.png", col_w=[2.4, 3.4, 6.2],
              title="Some common food adulterants", size=8.0)


def fig_marks():
    table_fig(["Mark", "Found on", "Given by"],
              [["ISI", "electrical goods, cement, helmets, gas cylinders", "Bureau of Indian Standards (BIS)"],
               ["AGMARK", "honey, ghee, spices, pulses", "Directorate of Marketing and Inspection"],
               ["FSSAI licence number", "all packaged food", "Food Safety and Standards Authority of India"],
               ["Hallmark", "gold and silver jewellery", "Bureau of Indian Standards (BIS)"],
               ["Ecomark", "eco-friendly products", "Bureau of Indian Standards (BIS)"]],
              "hpe_ch07_fig03_marks.png", col_w=[2.6, 4.8, 5.4],
              title="Quality marks a wise consumer looks for", size=8.0)


if __name__ == "__main__":
    fig_rights()
    fig_adulteration()
    fig_marks()
