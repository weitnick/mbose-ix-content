"""Figures for Class XII Accountancy Chapter 8, Analysis of Financial Statements.
Run: python xii_acc_ch08_analysis.py
"""
from xii_acc_ch01_partnership import *


def fig01_tools():
    fig, a = canvas(9.6, 4.2, (0, 19.2), (0, 8.4))
    a.text(9.6, 8.0, "Tools of analysis of financial statements", ha="center", fontsize=10, weight="bold")
    box(a, (6.6, 5.9), 6.0, 1.3, "Financial statement analysis", fc=PALE_AMBER, ec=AMBER, fs=9, bold=True)
    tools = [("Comparative\nstatements\n\nhorizontal:\nyear-on-year\nchange in ₹ and %", SOFT, BLUE),
             ("Common-size\nstatements\n\nvertical:\neach item as %\nof a total", PALE_GREEN, GREEN),
             ("Trend\nanalysis\n\nitems as % of a\nbase year over\nseveral years", SOFT, BLUE),
             ("Ratio\nanalysis\n\nrelationship\nbetween two\nitems", PALE_GREEN, GREEN),
             ("Cash flow\nanalysis\n\nsources and\nuses of cash", SOFT, BLUE)]
    for i, (t, fc, ec) in enumerate(tools):
        x = 0.2 + i * 3.8
        box(a, (x, 0.8), 3.4, 4.4, t, fc=fc, ec=ec, fs=7.8)
        arrow(a, (9.6, 5.9), (x + 1.7, 5.25))
    save(fig, "acc_ch08_fig01_tools.png")


if __name__ == "__main__":
    fig01_tools()
