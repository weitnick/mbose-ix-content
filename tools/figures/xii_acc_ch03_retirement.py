"""Figures for Class XII Accountancy Chapter 3, Retirement/Death of a Partner.
Run: python xii_acc_ch03_retirement.py
"""
from xii_acc_ch01_partnership import *


def fig01_amount_due():
    fig, a = canvas(9.6, 4.3, (0, 19.2), (0, 8.6))
    a.text(9.6, 8.2, "Amount due to a retiring partner (or a deceased partner's executors)", ha="center", fontsize=10, weight="bold")
    box(a, (0.3, 1.6), 8.6, 5.9,
        "ADD (credited to his capital)\n\n• balance of capital (and current) account\n• share of goodwill\n"
        "• share of reserves and undistributed profit\n• share of revaluation profit\n"
        "• share of profit up to the date of\n   retirement/death\n• interest on capital, salary, commission\n   up to that date",
        fc=PALE_GREEN, ec=GREEN, fs=8)
    box(a, (10.3, 1.6), 8.6, 5.9,
        "LESS (debited to his capital)\n\n• debit balance of current account\n• share of goodwill already in the books\n   (written off)\n"
        "• share of accumulated losses (debit P&L)\n• share of revaluation loss\n"
        "• share of loss up to the date\n• drawings and interest on drawings",
        fc=PALE_AMBER, ec=AMBER, fs=8)
    a.text(9.6, 0.7, "Net balance = amount payable: paid in cash, transferred to his loan account, or partly both",
           ha="center", fontsize=8.2, color=GREY)
    save(fig, "acc_ch03_fig01_amount_due.png")


def fig02_ratios():
    fig, a = canvas(9.6, 3.9, (0, 19.2), (0, 7.8))
    a.text(9.6, 7.4, "Sacrificing ratio and gaining ratio", ha="center", fontsize=10, weight="bold")
    box(a, (0.3, 1.5), 8.6, 5.2,
        "Sacrificing ratio\n\n= old share − new share\n\nused on ADMISSION\n(and change in ratio)\n\n"
        "old partners who give up a share\nreceive the goodwill premium",
        fc=SOFT, ec=BLUE, fs=8.4)
    box(a, (10.3, 1.5), 8.6, 5.2,
        "Gaining ratio\n\n= new share − old share\n\nused on RETIREMENT and DEATH\n(and change in ratio)\n\n"
        "remaining partners who gain a share\npay the outgoing partner's goodwill",
        fc=PALE_GREEN, ec=GREEN, fs=8.4)
    a.text(9.6, 0.6, "If no new ratio is given, the remaining partners keep their old ratio, so the gaining ratio = their old ratio",
           ha="center", fontsize=8, color=GREY)
    save(fig, "acc_ch03_fig02_ratios.png")


def fig03_settlement():
    fig, a = canvas(9.6, 4.2, (0, 19.2), (0, 8.4))
    a.text(9.6, 8.0, "Settling the amount due to a retiring partner", ha="center", fontsize=10, weight="bold")
    box(a, (6.6, 5.6), 6.0, 1.6, "Retiring partner's capital A/c\n(final credit balance)", fc=PALE_AMBER, ec=AMBER, fs=8.5, bold=True)
    opts = [((0.2, 0.9), "Paid in full\n\nRetiring Partner's\nCapital A/c Dr.\nTo Cash/Bank A/c"),
            ((5.0, 0.9), "Whole amount\ntreated as loan\n\nCapital A/c Dr.\nTo Retiring Partner's\nLoan A/c"),
            ((9.8, 0.9), "Part cash,\npart loan\n\nCapital A/c Dr.\nTo Cash/Bank A/c\nTo Loan A/c"),
            ((14.6, 0.9), "Loan repaid in\ninstalments\n\nInterest A/c Dr. To Loan;\nLoan A/c Dr.\nTo Cash/Bank A/c")]
    for xy, t in opts:
        box(a, xy, 4.4, 4.0, t, fc=SOFT, ec=BLUE, fs=7.6)
        arrow(a, (9.6, 5.6), (xy[0] + 2.2, 4.9))
    save(fig, "acc_ch03_fig03_settlement.png")


def fig04_profit_to_death():
    fig, a = canvas(9.6, 4.0, (0, 19.2), (0, 8.0))
    a.text(9.6, 7.6, "Deceased partner's share of profit up to the date of death", ha="center", fontsize=10, weight="bold")
    box(a, (0.3, 1.6), 8.6, 5.2,
        "Time basis\n\nlast year's (or average) profit\n× months up to death ÷ 12\n× deceased partner's share\n\n"
        "e.g. ₹1,00,000 × 3/12 × 4/10\n= ₹10,000",
        fc=SOFT, ec=BLUE, fs=8.4)
    box(a, (10.3, 1.6), 8.6, 5.2,
        "Turnover (sales) basis\n\nsales up to death\n× last year's profit ÷ last year's sales\n× deceased partner's share\n\n"
        "e.g. ₹1,50,000 × 1,00,000/8,00,000\n× 4/10 = ₹7,500",
        fc=PALE_GREEN, ec=GREEN, fs=8.4)
    a.text(9.6, 0.7, "Entry: Profit and Loss Suspense A/c Dr. To Deceased Partner's Capital A/c "
                     "(or Gaining Partners' Capital A/cs Dr.)", ha="center", fontsize=8, color=GREY)
    save(fig, "acc_ch03_fig04_profit_to_death.png")


if __name__ == "__main__":
    fig01_amount_due()
    fig02_ratios()
    fig03_settlement()
    fig04_profit_to_death()
