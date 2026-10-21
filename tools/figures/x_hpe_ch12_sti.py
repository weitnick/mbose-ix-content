"""Figures for Class X Health and Physical Education, Ch12 (Unit V): Sexually Transmitted Infections."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_hpe_common import flow, table_fig, tree


def fig_germs():
    tree("Germs that cause sexually transmitted infections",
         ["Bacteria", "Viruses", "Parasites"],
         "hpe_ch12_fig01_germs.png",
         grand={0: ["chlamydia", "gonorrhoea", "syphilis", "non-specific urethritis"],
                1: ["genital herpes (HSV)", "genital warts (HPV)", "HIV", "hepatitis B"],
                2: ["trichomoniasis", "pubic lice"]},
         width=9.5, child_w=2.8, size=8.6)


def fig_table():
    table_fig(["Infection", "Caused by", "Treatment"],
              [["Chlamydia (most common STI)", "bacterium Chlamydia trachomatis", "antibiotics"],
               ["Gonorrhoea", "bacterium", "antibiotics"],
               ["Syphilis", "bacterium Treponema pallidum", "antibiotics (penicillin)"],
               ["Genital herpes", "herpes simplex virus", "cooling, lidocaine gel, acyclovir"],
               ["Genital warts", "human papilloma virus", "cryotherapy (liquid nitrogen)"],
               ["Trichomoniasis", "parasite Trichomonas vaginalis", "antibiotics"],
               ["Non-specific urethritis", "various germs", "antibiotics"],
               ["Pubic lice", "tiny insects (lice)", "medicated shampoo"]],
              "hpe_ch12_fig02_table.png", col_w=[3.9, 4.2, 3.9],
              title="Common STIs, their causes and treatment", size=8.0)


def fig_steps():
    flow(["Notice a symptom\nor a risk", "See a qualified\ndoctor early", "Examination and\ntests: swabs,\nblood, urine",
          "Complete the\ntreatment", "Partner tested\nand treated;\nprevent reinfection"],
         "hpe_ch12_fig03_steps.png", width=10.5, w=1.95, h=1.2, size=8.2,
         title="What to do if an STI is suspected")


if __name__ == "__main__":
    fig_germs()
    fig_table()
    fig_steps()
