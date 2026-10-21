"""Figures for Class XII Accountancy Chapter 6, Issue and Redemption of Debentures.
Run: python xii_acc_ch06_debentures.py
"""
from xii_acc_ch01_partnership import *


def fig01_types():
    fig, a = canvas(9.6, 4.4, (0, 19.2), (0, 8.8))
    a.text(9.6, 8.4, "Types of debentures", ha="center", fontsize=10, weight="bold")
    groups = [("Security", "secured\n(mortgage)\n\nunsecured\n(naked)"), ("Tenure", "redeemable\n\nirredeemable\n(perpetual)"),
              ("Convertibility", "convertible\n(fully / partly)\n\nnon-convertible"), ("Coupon rate", "specific rate\n\nzero-coupon\n(issued at a\ndeep discount)"),
              ("Registration", "registered\n\nbearer\n(transfer by\ndelivery)")]
    for i, (h, t) in enumerate(groups):
        x = 0.2 + i * 3.8
        box(a, (x, 5.9), 3.4, 1.2, h, fc=PALE_AMBER, ec=AMBER, fs=8.4, bold=True)
        box(a, (x, 0.8), 3.4, 4.6, t, fc=SOFT, ec=BLUE, fs=7.8)
        arrow(a, (x + 1.7, 5.9), (x + 1.7, 5.4))
    save(fig, "acc_ch06_fig01_types.png")


def fig02_terms():
    fig, a = canvas(9.6, 4.6, (0, 19.2), (0, 9.2))
    a.text(9.6, 8.8, "Terms of issue and redemption (debenture of ₹100)", ha="center", fontsize=10, weight="bold")
    cases = [("1. Par / par", "Bank 100\nTo Debentures 100"),
             ("2. Discount 10% / par", "Bank 90\nDiscount on Issue 10\nTo Debentures 100"),
             ("3. Premium 10% / par", "Bank 110\nTo Debentures 100\nTo Sec. Premium 10"),
             ("4. Par / premium 10%", "Bank 100, Loss 10\nTo Debentures 100\nTo Prem. on Redemption 10"),
             ("5. Discount 10% / premium 10%", "Bank 90, Loss 20\nTo Debentures 100\nTo Prem. on Redemption 10"),
             ("6. Premium 10% / premium 10%", "Bank 110, Loss 10\nTo Debentures 100\nTo Sec. Premium 10\nTo Prem. on Redemption 10")]
    for i, (h, t) in enumerate(cases):
        r, c = divmod(i, 3)
        x = 0.3 + c * 6.3
        y = 4.6 - r * 4.0
        box(a, (x, y + 2.4), 5.9, 1.0, h, fc=PALE_AMBER, ec=AMBER, fs=8, bold=True)
        box(a, (x, y), 5.9, 2.3, t, fc=SOFT if i < 3 else PALE_GREEN, ec=BLUE if i < 3 else GREEN, fs=7.6)
    save(fig, "acc_ch06_fig02_terms.png")


if __name__ == "__main__":
    fig01_types()
    fig02_terms()
