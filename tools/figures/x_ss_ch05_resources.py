"""Figures for Class X Social Science, Ch05 (Geography 1): Resources."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import flow, timeline, tree


def fig_classification():
    tree("Classification of resources",
         ["On the basis of\norigin", "On the basis of\nexhaustibility", "On the basis of\nownership",
          "On the basis of\nstatus of development"],
         "ss_ch05_fig01_classification.png",
         grand={0: ["Biotic", "Abiotic"],
                1: ["Renewable", "Non-renewable"],
                2: ["Individual", "Community", "National", "International"],
                3: ["Potential", "Developed", "Stock", "Reserves"]},
         width=10.0, child_w=2.25)


def fig_planning():
    flow(["1. Identify resources and\nprepare an inventory\n(surveying, mapping, measuring)",
          "2. Build a planning structure\n(appropriate technology, skills\nand institutions)",
          "3. Match resource plans\nwith the overall national\ndevelopment plans"],
         "ss_ch05_fig02_planning.png", width=10.0, w=3.0, h=1.25, size=8.4,
         title="Resource planning in India: three stages")


def fig_conservation():
    ev = [("1968", "Club of Rome advocates resource conservation in a systematic way", 0),
          ("1974", "Schumacher's 'Small is Beautiful' repeats Gandhi's ideas on conservation", 1),
          ("1987", "Brundtland Report 'Our Common Future' introduces sustainable development", 2),
          ("1992", "Earth Summit at Rio de Janeiro: Forest Principles and Agenda 21 adopted", 3)]
    timeline(ev, "ss_ch05_fig03_conservation.png", title="Steps towards resource conservation", label_w=8.0)


if __name__ == "__main__":
    fig_classification()
    fig_planning()
    fig_conservation()
