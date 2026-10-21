"""Figures for Class XII Accountancy Chapter 2, Admission of a Partner.
Run: python xii_acc_ch02_admission.py
"""
from xii_acc_ch01_partnership import *


def fig01_adjustments():
    fig, a = canvas(9.6, 3.6, (0, 19.2), (0, 7.2))
    a.text(9.6, 6.8, "Adjustments on the admission of a partner", ha="center", fontsize=10, weight="bold")
    steps = [("1. New profit-\nsharing ratio", SOFT, BLUE), ("2. Sacrificing\nratio\n(old − new)", PALE_AMBER, AMBER),
             ("3. Goodwill\n(premium to\nsacrificers)", PALE_GREEN, GREEN),
             ("4. Reserves and\naccumulated\nprofits (old ratio)", SOFT, BLUE),
             ("5. Revaluation of\nassets and\nliabilities (old ratio)", PALE_AMBER, AMBER),
             ("6. Adjustment\nof capitals", PALE_GREEN, GREEN)]
    for i, (t, fc, ec) in enumerate(steps):
        x = 0.2 + i * 3.17
        box(a, (x, 2.2), 2.75, 3.0, t, fc=fc, ec=ec, fs=8)
        if i < 5:
            arrow(a, (x + 2.75, 3.7), (x + 3.17, 3.7))
    a.text(9.6, 1.0, "Old partners alone share reserves, revaluation profit or loss and goodwill premium; "
                     "the new partner's capital and premium come in cash", ha="center", fontsize=8.2, color=GREY)
    save(fig, "acc_ch02_fig01_adjustments.png")


def fig02_goodwill_methods():
    fig, a = canvas(9.6, 4.6, (0, 19.2), (0, 9.2))
    a.text(9.6, 8.8, "Methods of valuing goodwill", ha="center", fontsize=10, weight="bold")
    box(a, (7.1, 6.6), 5.0, 1.4, "Goodwill", fc=PALE_AMBER, ec=AMBER, fs=10, bold=True)
    items = [((0.3, 1.4), "Average profit\nmethod\n\naverage profit ×\nnumber of years'\npurchase\n(simple or weighted)"),
             ((6.6, 1.4), "Super profit method\n\nsuper profit =\naverage profit −\nnormal profit\ngoodwill = super profit\n× years' purchase"),
             ((12.9, 1.4), "Capitalisation\nmethod\n\n(a) average profit ×\n100/NRR − capital employed\n(b) super profit ×\n100/NRR")]
    for xy, t in items:
        box(a, xy, 6.0, 4.4, t, fc=SOFT, ec=BLUE, fs=8)
    for x in (3.3, 9.6, 15.9):
        arrow(a, (9.6, 6.6), (x, 5.8))
    a.text(9.6, 0.5, "Normal profit = capital employed × normal rate of return (NRR); "
                     "capital employed = total assets − outside liabilities", ha="center", fontsize=8, color=GREY)
    save(fig, "acc_ch02_fig02_goodwill_methods.png")


if __name__ == "__main__":
    fig01_adjustments()
    fig02_goodwill_methods()
