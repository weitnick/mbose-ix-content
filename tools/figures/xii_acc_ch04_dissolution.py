"""Figures for Class XII Accountancy Chapter 4, Dissolution of a Partnership Firm.
Run: python xii_acc_ch04_dissolution.py
"""
from xii_acc_ch01_partnership import *


def fig01_two_dissolutions():
    fig, a = canvas(9.6, 3.9, (0, 19.2), (0, 7.8))
    a.text(9.6, 7.4, "Dissolution of partnership and dissolution of the firm", ha="center", fontsize=10, weight="bold")
    box(a, (0.3, 1.4), 8.6, 5.3,
        "Dissolution of PARTNERSHIP\n\nthe agreement among partners changes\n(admission, retirement, death,\nchange in ratio)\n\n"
        "the FIRM CONTINUES\nbooks are not closed\nassets revalued (Revaluation A/c)",
        fc=SOFT, ec=BLUE, fs=8.2)
    box(a, (10.3, 1.4), 8.6, 5.3,
        "Dissolution of the FIRM\n\nrelation among ALL partners ends\n\nthe BUSINESS CLOSES\nbooks are closed\n"
        "assets sold, liabilities paid\n(Realisation A/c)",
        fc=PALE_AMBER, ec=AMBER, fs=8.2)
    a.text(9.6, 0.6, "Dissolution of the firm always dissolves the partnership; the reverse is not true",
           ha="center", fontsize=8.2, color=GREY)
    save(fig, "acc_ch04_fig01_two_dissolutions.png")


def fig02_modes():
    fig, a = canvas(9.6, 4.2, (0, 19.2), (0, 8.4))
    a.text(9.6, 8.0, "Modes of dissolution of a firm (Indian Partnership Act, 1932)", ha="center", fontsize=10, weight="bold")
    box(a, (6.9, 5.8), 5.4, 1.4, "Dissolution of the firm", fc=PALE_AMBER, ec=AMBER, fs=9.5, bold=True)
    opts = [((0.1, 0.8), "By agreement\n(Sec 40)\n\nconsent of all\npartners or\nas per contract"),
            ((3.92, 0.8), "Compulsory\n(Sec 41)\n\nall but one\ninsolvent;\nbusiness\nbecomes illegal"),
            ((7.74, 0.8), "On contingencies\n(Sec 42)\n\nexpiry of term;\ncompletion of\nventure; death;\ninsolvency"),
            ((11.56, 0.8), "By notice\n(Sec 43)\n\npartnership at\nwill: written\nnotice by\nany partner"),
            ((15.38, 0.8), "By court\n(Sec 44)\n\nunsound mind;\nmisconduct;\npersistent breach;\ncontinued losses")]
    for xy, t in opts:
        box(a, xy, 3.7, 4.3, t, fc=SOFT, ec=BLUE, fs=7.4)
        arrow(a, (9.6, 5.8), (xy[0] + 1.85, 5.15))
    save(fig, "acc_ch04_fig02_modes.png")


def fig03_realisation():
    fig, a = canvas(9.6, 4.6, (0, 19.2), (0, 9.2))
    a.text(9.6, 8.8, "What goes into the Realisation Account", ha="center", fontsize=10, weight="bold")
    box(a, (0.3, 1.5), 8.6, 6.6,
        "DEBIT side (Dr.)\n\n• all assets at book value\n   (except cash, bank, fictitious assets\n   and partners' loans/capitals)\n"
        "• liabilities paid (cash or by a partner)\n• unrecorded liabilities paid\n• realisation expenses\n"
        "• profit on realisation (balance)",
        fc=PALE_AMBER, ec=AMBER, fs=8)
    box(a, (10.3, 1.5), 8.6, 6.6,
        "CREDIT side (Cr.)\n\n• all outside liabilities at book value\n• provisions on assets (e.g. for\n   doubtful debts, depreciation)\n"
        "• cash from assets sold\n• assets taken over by partners\n• unrecorded assets realised\n"
        "• loss on realisation (balance)",
        fc=PALE_GREEN, ec=GREEN, fs=8)
    a.text(9.6, 0.7, "The balance (profit or loss) is shared by the partners in their profit-sharing ratio",
           ha="center", fontsize=8.2, color=GREY)
    save(fig, "acc_ch04_fig03_realisation.png")


def fig04_order():
    fig, a = canvas(9.6, 4.0, (0, 19.2), (0, 8.0))
    a.text(9.6, 7.6, "Order of settlement of accounts (Section 48)", ha="center", fontsize=10, weight="bold")
    steps = [("1. Outside debts\n(third-party\nliabilities)", PALE_AMBER, AMBER), ("2. Partners' loans\nand advances\n(rateably)", SOFT, BLUE),
             ("3. Partners'\ncapitals\n(rateably)", PALE_GREEN, GREEN), ("4. Surplus, if any,\nin the profit-\nsharing ratio", SOFT, BLUE)]
    for i, (t, fc, ec) in enumerate(steps):
        x = 0.3 + i * 4.75
        box(a, (x, 2.6), 4.0, 3.6, t, fc=fc, ec=ec, fs=8.4)
        if i < 3:
            arrow(a, (x + 4.0, 4.4), (x + 4.75, 4.4))
    a.text(9.6, 1.5, "Losses (including capital deficiency) are paid first out of profits, then out of capital,",
           ha="center", fontsize=8.2, color=GREY)
    a.text(9.6, 0.9, "and lastly by the partners individually in their profit-sharing ratio",
           ha="center", fontsize=8.2, color=GREY)
    save(fig, "acc_ch04_fig04_order.png")


if __name__ == "__main__":
    fig01_two_dissolutions()
    fig02_modes()
    fig03_realisation()
    fig04_order()
