"""Figures for Class XII Accountancy Chapter 9, Accounting Ratios.
Run: python xii_acc_ch09_ratios.py
"""
from xii_acc_ch01_partnership import *


def fig01_types():
    fig, a = canvas(9.6, 4.8, (0, 19.2), (0, 9.6))
    a.text(9.6, 9.2, "Functional classification of accounting ratios", ha="center", fontsize=10, weight="bold")
    box(a, (6.6, 7.1), 6.0, 1.3, "Accounting ratios", fc=PALE_AMBER, ec=AMBER, fs=9, bold=True)
    groups = [("Liquidity\n(short-term)", "current ratio\n\nquick (liquid)\nratio", SOFT, BLUE),
              ("Solvency\n(long-term)", "debt–equity\ndebt to capital\nemployed\nproprietary\ntotal assets to debt\ninterest coverage", PALE_GREEN, GREEN),
              ("Activity\n(turnover)", "inventory\ntrade receivables\ntrade payables\nworking capital\nnet assets\nfixed assets", SOFT, BLUE),
              ("Profitability", "gross profit\noperating ratio\noperating profit\nnet profit\nreturn on investment\nEPS, P/E, dividend\npayout", PALE_GREEN, GREEN)]
    for i, (h, t, fc, ec) in enumerate(groups):
        x = 0.3 + i * 4.75
        box(a, (x, 4.9), 4.2, 1.3, h, fc=fc, ec=ec, fs=8.4, bold=True)
        box(a, (x, 0.4), 4.2, 4.3, t, fc="white", ec=ec, fs=7.8)
        arrow(a, (9.6, 7.1), (x + 2.1, 6.25))
    save(fig, "acc_ch09_fig01_types.png")


if __name__ == "__main__":
    fig01_types()
