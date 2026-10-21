"""Figures for Class X Health and Physical Education, Ch08 (Unit III): Systems of Medicine and Quackery."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import table_fig, tree


def fig_systems():
    tree("Systems of medicine practised in India",
         ["Ayurveda", "Unani", "Siddha", "Naturopathy", "Homoeopathy", "Allopathy"],
         "hpe_ch08_fig01_systems.png",
         grand={0: ["vayu, pitta, kapha"],
                1: ["four humours"],
                2: ["Tamil Nadu"],
                3: ["natural philosophy"],
                4: ["likes cure likes"],
                5: ["most widely used"]},
         width=11.0, child_w=1.7, size=8.4)


def fig_compare():
    table_fig(["System", "Basis", "Founder or origin", "Key facts"],
              [["Ayurveda", "three doshas: vayu, pitta, kapha", "Charaka and Susruta", "removes toxins; restores balance"],
               ["Unani", "four humours", "Greek; came with Muslim rulers", "books in Arabic, Persian"],
               ["Siddha", "similar to Ayurveda", "Tamil siddhars", "Tamil Nadu, Kerala; books in Tamil"],
               ["Naturopathy", "natural philosophy", "nature cure movement", "fasting, hydrotherapy, enema, diet"],
               ["Homoeopathy", "law of similars", "Dr Samuel Hahnemann", "very small doses"],
               ["Allopathy", "deviations from the normal", "modern science", "most specialities, careers"]],
              "hpe_ch08_fig02_compare.png", col_w=[2.2, 3.9, 3.9, 3.6],
              title="The systems of medicine compared", size=7.8)


def fig_quack():
    table_fig(["Warning signs of a quack", "What a qualified doctor does"],
              [["claims a 'secret' or 'exclusive' formula or machine", "uses proven, published treatments"],
               ["sells cure-alls 'blessed by saints and sages'", "treats each disease by its cause"],
               ["uses psychological suggestion to push remedies", "explains the facts honestly"],
               ["guarantees a quick cure in a fixed time, on contract", "makes no guarantee of cure"],
               ["advertises with case histories and testimonials", "is registered; displays a registration number"]],
              "hpe_ch08_fig03_quack.png", col_w=[6.0, 5.2],
              title="How to identify a quack", size=8.2)


if __name__ == "__main__":
    fig_systems()
    fig_compare()
    fig_quack()
