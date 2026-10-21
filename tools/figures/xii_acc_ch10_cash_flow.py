"""Figures for Class XII Accountancy Chapter 10, Cash Flow Statement.
Run: python xii_acc_ch10_cash_flow.py
"""
from xii_acc_ch01_partnership import *


def fig01_activities():
    fig, a = canvas(9.6, 5.0, (0, 19.2), (0, 10.0))
    a.text(9.6, 9.6, "Classification of cash flows (AS-3 Revised)", ha="center", fontsize=10, weight="bold")
    box(a, (6.1, 7.5), 7.0, 1.3, "Cash flows of the year", fc=PALE_AMBER, ec=AMBER, fs=9, bold=True)
    groups = [("A. Operating activities",
               "principal revenue-producing\nactivities\n\ncash from customers\ncash to suppliers\nand employees\nincome tax paid",
               SOFT, BLUE),
              ("B. Investing activities",
               "purchase and sale of\nlong-term assets and\ninvestments\n\ninterest and dividend\nreceived\n(non-financial firm)",
               PALE_GREEN, GREEN),
              ("C. Financing activities",
               "changes in owners' capital\nand borrowings\n\nissue of shares,\ndebentures, loans;\nrepayment; interest\nand dividend paid",
               SOFT, BLUE)]
    for i, (h, t, fc, ec) in enumerate(groups):
        x = 0.4 + i * 6.25
        box(a, (x, 5.3), 5.9, 1.2, h, fc=fc, ec=ec, fs=8.6, bold=True)
        box(a, (x, 0.9), 5.9, 4.2, t, fc="white", ec=ec, fs=7.8)
        arrow(a, (9.6, 7.5), (x + 2.95, 6.55))
    a.text(9.6, 0.35, "A + B + C = net increase or decrease in cash and cash equivalents",
           ha="center", fontsize=8.4, style="italic")
    save(fig, "acc_ch10_fig01_activities.png")


def fig02_indirect():
    fig, a = canvas(9.6, 5.4, (0, 19.2), (0, 10.8))
    a.text(9.6, 10.4, "Indirect method: cash flow from operating activities", ha="center", fontsize=10, weight="bold")
    steps = [("Net profit before tax and extraordinary items", PALE_AMBER, AMBER),
             ("+ non-cash and non-operating charges (depreciation, goodwill and\n"
              "patents written off, loss on sale of assets, interest paid)\n"
              "− non-operating incomes (profit on sale of assets, interest and dividend received)", SOFT, BLUE),
             ("= Operating profit before working capital changes", PALE_GREEN, GREEN),
             ("+ decrease in current assets / increase in current liabilities\n"
              "− increase in current assets / decrease in current liabilities", SOFT, BLUE),
             ("= Cash generated from operations  − income tax paid", PALE_GREEN, GREEN),
             ("= Net cash from operating activities", PALE_AMBER, AMBER)]
    hs = [0.9, 1.5, 0.9, 1.2, 0.9, 0.9]
    y = 9.8
    prev = None
    for (t, fc, ec), h in zip(steps, hs):
        y -= h
        box(a, (2.2, y), 14.8, h, t, fc=fc, ec=ec, fs=8.2, bold=(fc != SOFT))
        if prev is not None:
            arrow(a, (9.6, prev), (9.6, y + h))
        prev = y
        y -= 0.45
    save(fig, "acc_ch10_fig02_indirect.png")


if __name__ == "__main__":
    fig01_activities()
    fig02_indirect()
