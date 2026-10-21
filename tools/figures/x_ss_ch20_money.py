"""Figures for Class X Social Science, Ch20 (Economics 3): Money and Financial System."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_ss_common import ACC, FILLS, GREY, INK, arrow, box, flow, save, table_fig
import matplotlib.pyplot as plt


def fig_bank():
    fig, ax = plt.subplots(figsize=(10.0, 3.0))
    box(ax, (1.3, 1.2), "Depositors\n(people with\nextra money)", FILLS[0], w=2.2, h=1.1, size=8.8)
    box(ax, (5.5, 1.2), "Bank\nkeeps about 15% as cash;\nlends the rest", FILLS[1], w=2.6, h=1.1, size=8.8)
    box(ax, (9.7, 1.2), "Borrowers\n(farmers, traders,\nbusinesses)", FILLS[2], w=2.2, h=1.1, size=8.8)
    arrow(ax, (2.45, 1.45), (4.15, 1.45))
    ax.text(3.3, 1.6, "deposits", ha="center", fontsize=8)
    arrow(ax, (4.15, 0.95), (2.45, 0.95), color=GREY)
    ax.text(3.3, 0.55, "interest\n(lower rate)", ha="center", fontsize=7.6, color=GREY)
    arrow(ax, (6.85, 1.45), (8.55, 1.45))
    ax.text(7.7, 1.6, "loans", ha="center", fontsize=8)
    arrow(ax, (8.55, 0.95), (6.85, 0.95), color=GREY)
    ax.text(7.7, 0.55, "repayment +\ninterest (higher)", ha="center", fontsize=7.6, color=GREY)
    ax.text(5.5, 0.05, "The difference between the two interest rates is the bank's main income.", ha="center",
            fontsize=8.2, color=ACC)
    ax.set_xlim(0, 11)
    ax.set_ylim(-0.1, 2.2)
    ax.axis("off")
    ax.set_title("Banks: a bridge between depositors and borrowers", fontsize=10.5, fontweight="bold", color=ACC)
    save(fig, "ss_ch20_fig01_bank.png")


def fig_credit():
    table_fig(["", "Formal sources", "Informal sources"],
              [["Who lends", "banks, co-operatives", "moneylenders, traders, employers, relatives"],
               ["Supervised by", "Reserve Bank of India", "no one"],
               ["Interest rate", "lower, fixed by rules", "often very high"],
               ["Collateral, papers", "usually needed", "often not needed"],
               ["Risk for the poor", "low", "debt trap; harsh recovery"],
               ["Who mostly uses them", "richer households", "poorer households"]],
              "ss_ch20_fig02_credit.png", col_w=[3.0, 4.0, 5.6], title="Formal and informal sources of credit", size=8.4)


def fig_shg():
    flow(["15–20 members from\none neighbourhood\nmeet and save regularly",
          "Small loans to\nmembers from pooled\nsavings, at low interest",
          "After 1–2 years of\nregular saving, a bank\nloan to the group",
          "Self-employment:\nsewing machines,\nlooms, cattle, seeds"],
         "ss_ch20_fig03_shg.png", width=10.5, w=2.35, h=1.25, size=8.0,
         title="How a Self Help Group works")


if __name__ == "__main__":
    fig_bank()
    fig_credit()
    fig_shg()
