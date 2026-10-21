"""Figures for Class XII Mathematics Chapter 2, Inverse Trigonometric Functions.
Run: python xii_math_ch02_inverse_trig.py
"""
from xii_math_common import *


def fig01_graphs():
    fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.6))
    x1 = np.linspace(-1, 1, 400)
    xt = np.linspace(-4, 4, 400)
    specs = [
        (x1, np.arcsin(x1), "y = sin⁻¹x", "domain [−1, 1], range [−π/2, π/2]", (-1.6, 1.6), (-2.0, 2.0)),
        (x1, np.arccos(x1), "y = cos⁻¹x", "domain [−1, 1], range [0, π]", (-1.6, 1.6), (-0.6, 3.6)),
        (xt, np.arctan(xt), "y = tan⁻¹x", "domain R, range (−π/2, π/2)", (-4.2, 4.2), (-2.0, 2.0)),
    ]
    for a, (x, y, t, n, xr, yr) in zip(axs, specs):
        axes(a, xr, yr, ticks=True)
        a.plot(x, y, color=BLUE, lw=2.2)
        a.set_title(t, fontsize=10, pad=12)
        for v, lab in [(np.pi / 2, "π/2"), (-np.pi / 2, "−π/2"), (np.pi, "π")]:
            if yr[0] < v < yr[1]:
                a.axhline(v, color=GREY, lw=0.7, ls=":")
                a.text(xr[0] + 0.05, v + 0.06, lab, fontsize=8, color=GREY)
        a.set_xticks([t for t in a.get_xticks() if xr[0] < t < xr[1] and t != 0])
        a.set_yticks([])
        a.text(0.5, -0.12, n, ha="center", va="top", fontsize=8.5, color=INK, transform=a.transAxes)
    fig.suptitle("Principal value branches of inverse trigonometric functions", fontsize=11, weight="bold")
    fig.tight_layout()
    save(fig, "math_ch02_fig01_principal_branches.png")


if __name__ == "__main__":
    fig01_graphs()
