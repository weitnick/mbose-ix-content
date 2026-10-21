"""Figures for Class X Social Science, Ch02 (History 2): Non-Cooperation and Civil Disobedience Movements."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import timeline, tree


def fig_timeline():
    ev = [("1915", "Mahatma Gandhi returns to India from South Africa (January)", 0),
          ("1917", "Champaran satyagraha (Bihar) for indigo cultivators", 0),
          ("1917–18", "Kheda satyagraha (Gujarat) for peasants; 1918 Ahmedabad mill workers", 0),
          ("1919", "Rowlatt Act; Jallianwala Bagh massacre at Amritsar (13 April)", 5),
          ("1920", "Calcutta session (Sept) and Nagpur session (Dec) adopt Non-Cooperation", 1),
          ("1922", "Chauri Chaura violence (February): movement withdrawn", 5),
          ("1928", "Simon Commission arrives; greeted with 'Go back, Simon'", 2),
          ("1929", "Lahore session: demand for Purna Swaraj (December)", 2),
          ("1930", "Salt March to Dandi (12 March–6 April); Civil Disobedience begins", 3),
          ("1931", "Gandhi–Irwin Pact (5 March); Second Round Table Conference", 3),
          ("1932", "Civil Disobedience relaunched; Poona Pact (September)", 3),
          ("1934", "Civil Disobedience Movement loses momentum", 5)]
    timeline(ev, "ss_ch02_fig01_timeline.png", title="The national movement, 1915–1934", label_w=7.4)


def fig_groups():
    tree("Who joined the Civil Disobedience Movement, and why",
         ["Rich peasants", "Poor peasants", "Business classes", "Industrial workers", "Women"],
         "ss_ch02_fig02_groups.png",
         grand={0: ["hit by falling prices", "wanted revenue cut"],
                1: ["wanted unpaid rent", "to be remitted"],
                2: ["wanted protection", "against imports", "opposed rupee ratio"],
                3: ["Nagpur workers", "boycotted foreign goods", "went on strikes"],
                4: ["joined salt protests", "picketed liquor and", "foreign-cloth shops"]},
         width=10.0, child_w=1.85)


if __name__ == "__main__":
    fig_timeline()
    fig_groups()
