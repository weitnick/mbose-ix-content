"""Figures for Class XII Accountancy Chapter 5, Accounting for Share Capital.
Run: python xii_acc_ch05_share_capital.py
"""
from xii_acc_ch01_partnership import *


def fig01_categories():
    fig, a = canvas(9.6, 5.4, (0, 19.2), (0, 10.8))
    a.text(9.6, 10.4, "Categories of share capital", ha="center", fontsize=10, weight="bold")
    box(a, (6.1, 8.4), 7.0, 1.3, "Authorised (nominal) capital", fc=PALE_AMBER, ec=AMBER, fs=9, bold=True)
    box(a, (2.2, 6.2), 6.0, 1.3, "Issued capital", fc=SOFT, ec=BLUE, fs=8.6)
    box(a, (11.0, 6.2), 6.0, 1.3, "Unissued capital", fc="white", ec=GREY, fs=8.6)
    box(a, (2.2, 4.0), 6.0, 1.3, "Subscribed capital", fc=SOFT, ec=BLUE, fs=8.6)
    box(a, (11.0, 4.0), 6.0, 1.3, "Unsubscribed capital", fc="white", ec=GREY, fs=8.6)
    box(a, (0.3, 1.8), 5.6, 1.3, "Called-up capital", fc=PALE_GREEN, ec=GREEN, fs=8.4)
    box(a, (6.6, 1.8), 5.6, 1.3, "Uncalled capital\n(part may be reserve capital)", fc="white", ec=GREY, fs=7.8)
    box(a, (0.3, 0.1), 5.6, 1.3, "Paid-up capital\n= called-up − calls in arrears", fc=PALE_GREEN, ec=GREEN, fs=7.6)
    box(a, (6.6, 0.1), 5.6, 1.3, "Calls in arrears\n(called but not paid)", fc=PALE_AMBER, ec=AMBER, fs=7.8)
    arrow(a, (9.6, 8.4), (5.2, 7.5))
    arrow(a, (9.6, 8.4), (14.0, 7.5))
    arrow(a, (5.2, 6.2), (5.2, 5.3))
    arrow(a, (5.2, 6.2), (14.0, 5.3))
    arrow(a, (5.2, 4.0), (3.1, 3.1))
    arrow(a, (5.2, 4.0), (9.4, 3.1))
    arrow(a, (3.1, 1.8), (3.1, 1.4))
    arrow(a, (4.6, 1.8), (7.6, 1.4))
    save(fig, "acc_ch05_fig01_categories.png")


def fig02_shares():
    fig, a = canvas(9.6, 4.4, (0, 19.2), (0, 8.8))
    a.text(9.6, 8.4, "Classes of shares (Section 43, Companies Act 2013)", ha="center", fontsize=10, weight="bold")
    box(a, (0.3, 1.0), 8.6, 6.6,
        "Preference shares\n\npreferential right to a FIXED dividend\nand to repayment of capital on winding up\n\n"
        "kinds:\n• cumulative / non-cumulative\n• participating / non-participating\n• convertible / non-convertible\n"
        "• redeemable (irredeemable not allowed)",
        fc=SOFT, ec=BLUE, fs=7.9)
    box(a, (10.3, 1.0), 8.6, 6.6,
        "Equity (ordinary) shares\n\nshares that are NOT preference shares\n\ndividend varies with profit;\n"
        "paid after preference dividend\n\nvoting rights (or differential rights);\nbear the greatest risk —\nthe real owners",
        fc=PALE_GREEN, ec=GREEN, fs=7.9)
    save(fig, "acc_ch05_fig02_shares.png")


def fig03_forfeiture():
    fig, a = canvas(9.6, 4.2, (0, 19.2), (0, 8.4))
    a.text(9.6, 8.0, "Forfeiture and reissue of shares", ha="center", fontsize=10, weight="bold")
    steps = [("1. Forfeit\n\nShare Capital Dr (called-up)\nSec. Premium Dr (if unpaid)\nTo Calls-in-Arrears\nTo Share Forfeiture", PALE_AMBER, AMBER),
             ("2. Reissue\n\nBank Dr (price)\nShare Forfeiture Dr (discount)\nTo Share Capital\n(To Sec. Premium if above\npaid-up value)", SOFT, BLUE),
             ("3. Transfer gain\n\nShare Forfeiture Dr\nTo Capital Reserve\n\n(forfeited amount on reissued\nshares − discount allowed)", PALE_GREEN, GREEN)]
    for i, (t, fc, ec) in enumerate(steps):
        x = 0.3 + i * 6.4
        box(a, (x, 1.4), 5.8, 5.6, t, fc=fc, ec=ec, fs=7.8)
        if i < 2:
            arrow(a, (x + 5.8, 4.2), (x + 6.4, 4.2))
    a.text(9.6, 0.6, "Discount on reissue can never exceed the amount forfeited on those shares",
           ha="center", fontsize=8.2, color=GREY)
    save(fig, "acc_ch05_fig03_forfeiture.png")


if __name__ == "__main__":
    fig01_categories()
    fig02_shares()
    fig03_forfeiture()
