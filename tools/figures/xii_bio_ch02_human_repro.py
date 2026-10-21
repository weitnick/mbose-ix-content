"""Figures for Class XII Biology Chapter 2, Human Reproduction.
Run: python xii_bio_ch02_human_repro.py
"""
from xii_bio_common import *


def fig01_gametogenesis():
    fig, a = canvas(9.6, 6.0, (0, 16), (0, 10))
    a.text(4.0, 9.6, "Spermatogenesis (testis)", ha="center", fontsize=10, weight="bold", color=BLUE)
    a.text(12.0, 9.6, "Oogenesis (ovary)", ha="center", fontsize=10, weight="bold", color=RED)
    left = [("spermatogonium (2n = 46)", 8.6), ("primary spermatocyte (2n)", 6.9), ("2 secondary spermatocytes (n = 23)", 5.2),
            ("4 spermatids (n)", 3.5), ("4 spermatozoa (n)", 1.8)]
    right = [("oogonium (2n = 46)\n(formed before birth)", 8.6), ("primary oocyte (2n)\narrested in prophase I", 6.9),
             ("secondary oocyte (n) + 1st polar body", 5.2), ("ovum (n) + 2nd polar body", 3.5),
             ("1 functional egg per oogonium", 1.8)]
    for (txt, y), fc in zip(left, [PALE_BLUE] * 5):
        box(a, (1.0, y - 0.45), 6.0, 0.9, txt, fc=fc, ec=BLUE, fs=8.5)
    for (txt, y), fc in zip(right, [PALE_RED] * 5):
        box(a, (9.0, y - 0.45), 6.0, 0.9, txt, fc=fc, ec=RED, fs=8.5)
    lsteps = ["mitosis / growth", "meiosis I", "meiosis II", "spermiogenesis"]
    rsteps = ["growth (in primary follicle)", "meiosis I (before ovulation)", "meiosis II (at fertilisation)", ""]
    for i in range(4):
        y0, y1 = left[i][1] - 0.45, left[i + 1][1] + 0.45
        arrow(a, (4.0, y0), (4.0, y1))
        a.text(4.25, (y0 + y1) / 2, lsteps[i], fontsize=8, color=INK, va="center")
        if rsteps[i]:
            arrow(a, (12.0, right[i][1] - 0.45), (12.0, right[i + 1][1] + 0.45))
            a.text(12.25, (right[i][1] + right[i + 1][1]) / 2, rsteps[i], fontsize=8, color=INK, va="center")
    a.text(8.0, 0.55, "Sperms are released from the seminiferous tubules (spermiation); the secondary oocyte is released at ovulation.",
           ha="center", fontsize=8.5, color=INK)
    save(fig, "bio_ch02_fig01_gametogenesis.png")


def fig02_sperm():
    fig, a = canvas(8.0, 2.6, (0, 16), (0, 4.4))
    a.add_patch(Ellipse((2.0, 2.2), 2.6, 1.6, fc=PALE_BLUE, ec=BLUE, lw=1.2))
    a.add_patch(Ellipse((1.35, 2.2), 1.3, 1.75, fc=PALE_AMBER, ec=AMBER, lw=1.2))      # acrosome cap
    a.add_patch(Ellipse((2.15, 2.2), 1.8, 1.25, fc="#C9D9EC", ec=BLUE, lw=0.8))         # nucleus
    a.add_patch(Rectangle((3.3, 2.0), 0.4, 0.4, fc="#DDDDDD", ec=INK, lw=0.8))           # neck
    a.add_patch(Rectangle((3.7, 1.85), 2.6, 0.7, fc=PALE_GREEN, ec=GREEN, lw=1))         # middle piece
    for x in np.arange(3.85, 6.2, 0.33):
        a.add_patch(Ellipse((x + 0.12, 2.2), 0.28, 0.5, fc="#BFDDBF", ec=GREEN, lw=0.6))
    t = np.linspace(6.3, 15.0, 300)
    a.plot(t, 2.2 + 0.35 * np.sin((t - 6.3) * 1.4) * np.exp(-(t - 6.3) / 12), color=INK, lw=1.6)
    label(a, (0.9, 2.6), (0.0, 3.9), "acrosome (enzymes)", ha="left")
    label(a, (2.3, 2.0), (3.4, 0.45), "nucleus (n)", ha="left")
    label(a, (3.5, 2.4), (4.6, 3.9), "neck", ha="left")
    label(a, (5.0, 2.5), (6.6, 3.9), "middle piece (mitochondria: energy)", ha="left")
    label(a, (8.0, 1.95), (8.6, 0.45), "tail (motility)", ha="left")
    a.text(1.4, 0.45, "head", ha="center", fontsize=9, color=GREY)
    a.plot([0.7, 3.3], [0.95, 0.95], color=GREY, lw=0.8)
    save(fig, "bio_ch02_fig02_sperm.png")


def fig03_menstrual_hormones():
    d = np.linspace(0, 28, 300)
    g = lambda mu, s, h: h * np.exp(-((d - mu) / s) ** 2)
    lh = 0.12 + g(14, 0.9, 1.0)
    fsh = 0.18 + g(13.5, 1.2, 0.35) + g(2, 4, 0.1)
    est = 0.12 + g(12.5, 2.4, 0.6) + g(21, 3.0, 0.25)
    prog = 0.05 + g(21, 3.4, 0.75)
    fig, (a, b) = plt.subplots(2, 1, figsize=(8.0, 5.2), sharex=True, gridspec_kw=dict(height_ratios=[3, 1]))
    a.plot(d, lh, color=RED, lw=1.8, label="LH")
    a.plot(d, fsh, color=AMBER, lw=1.8, label="FSH")
    a.plot(d, est, color=BLUE, lw=1.8, label="estrogen")
    a.plot(d, prog, color=GREEN, lw=1.8, label="progesterone")
    a.axvline(14, color=GREY, ls=":", lw=1)
    a.text(14.3, 1.05, "ovulation (LH surge)", fontsize=8.5, color=GREY)
    a.set_ylabel("relative level")
    a.set_yticks([])
    a.legend(fontsize=8.5, loc="upper left", frameon=False)
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
    phases = [(0, 5, "menstrual", PALE_RED), (5, 14, "follicular (proliferative)", PALE_BLUE),
              (14, 15, "", "#DDDDDD"), (15, 28, "luteal (secretory)", PALE_GREEN)]
    for x0, x1, txt, c in phases:
        b.add_patch(Rectangle((x0, 0), x1 - x0, 1, fc=c, ec="white"))
        if txt:
            b.text((x0 + x1) / 2, 0.5, txt, ha="center", va="center", fontsize=8.5)
    b.set_ylim(0, 1)
    b.set_yticks([])
    b.set_xlim(0, 28)
    b.set_xticks([0, 5, 14, 28])
    b.set_xlabel("day of the cycle")
    for s in ("top", "right", "left"):
        b.spines[s].set_visible(False)
    a.set_title("Hormone levels during a 28-day menstrual cycle (schematic)", fontsize=10)
    fig.tight_layout()
    save(fig, "bio_ch02_fig03_menstrual_cycle.png")


def fig04_ovum_sperms():
    fig, a = canvas(6.4, 5.2, (-4.6, 4.6), (-3.6, 3.8))
    rng = np.random.default_rng(5)
    for t in np.linspace(0, 2 * np.pi, 22, endpoint=False):
        r = 2.55 + 0.15 * rng.random()
        a.add_patch(Ellipse((r * np.cos(t), r * np.sin(t)), 0.75, 0.5, angle=np.degrees(t), fc=PALE_AMBER,
                            ec=AMBER, lw=0.7))
    a.add_patch(Circle((0, 0), 2.15, fc=PALE_BLUE, ec=BLUE, lw=2.4))     # zona pellucida
    a.add_patch(Circle((0, 0), 1.95, fc="white", ec=BLUE, lw=0.6))       # perivitelline space
    a.add_patch(Circle((0, 0), 1.8, fc="#FBEFEF", ec=RED, lw=1.0))        # oocyte
    a.add_patch(Circle((0.2, 0.1), 0.45, fc="#F2C9C3", ec=RED))
    a.add_patch(Circle((1.55, 1.1), 0.22, fc="#F2C9C3", ec=RED))          # first polar body
    for ang, L in ((200, 1.4), (120, 1.2), (60, 1.3)):
        t = np.radians(ang)
        x0, y0 = 2.95 * np.cos(t), 2.95 * np.sin(t)
        a.add_patch(Ellipse((x0, y0), 0.32, 0.2, angle=ang, fc=INK, ec=INK))
        a.plot([x0 + 0.15 * np.cos(t), x0 + L * np.cos(t)], [y0 + 0.15 * np.sin(t), y0 + L * np.sin(t)], color=INK, lw=1)
    label(a, (-3.0, 2.0), (-4.4, 3.2), "corona radiata cells")
    label(a, (-1.5, -1.5), (-4.4, -2.8), "zona pellucida")
    label(a, (1.9, -0.5), (3.2, -2.8), "perivitelline space")
    label(a, (1.6, 1.2), (3.3, 3.2), "first polar body")
    label(a, (0.2, 0.1), (3.4, 0.4), "secondary oocyte\n(nucleus)")
    label(a, (-2.8, -1.0), (-4.4, -0.9), "sperms")
    save(fig, "bio_ch02_fig04_ovum_sperms.png")


def fig05_female_system():
    fig, a = canvas(7.0, 4.8, (-7, 7), (-5.2, 4.2))
    uterus = Polygon([(-1.8, 2.2), (1.8, 2.2), (1.2, -0.8), (0.45, -1.8), (-0.45, -1.8), (-1.2, -0.8)], closed=True,
                     fc=PALE_RED, ec=RED, lw=1.4)
    a.add_patch(uterus)
    a.add_patch(Polygon([(-1.1, 1.8), (1.1, 1.8), (0.7, -0.6), (0.25, -1.5), (-0.25, -1.5), (-0.7, -0.6)], closed=True,
                        fc="white", ec=RED, lw=0.8))
    a.add_patch(Rectangle((-0.45, -3.6), 0.9, 1.8, fc=PALE_AMBER, ec=AMBER, lw=1.2))             # vagina
    for s in (-1, 1):
        xs = np.linspace(1.8, 5.2, 50)
        a.plot(s * xs, 2.0 + 0.5 * np.sin((xs - 1.8) / 3.4 * np.pi), color=RED, lw=3)
        for k in range(5):
            ang = np.radians(-60 + k * 25)
            a.plot([s * 5.2, s * (5.2 + 0.6 * np.cos(ang))], [2.0, 2.0 + 0.6 * np.sin(ang)], color=RED, lw=1.2)
        a.add_patch(Ellipse((s * 4.3, 0.6), 1.6, 0.9, fc="#F3E6CF", ec=AMBER, lw=1.2))
    label(a, (5.6, 2.1), (5.9, 3.6), "fimbriae / infundibulum")
    label(a, (3.8, 2.45), (2.6, 3.8), "ampulla (fertilisation)")
    label(a, (2.3, 2.2), (1.8, 3.2), "isthmus")
    label(a, (4.3, 0.6), (5.4, -0.6), "ovary")
    label(a, (0.0, 2.1), (-1.4, 3.8), "fundus")
    label(a, (1.5, 1.0), (2.6, -1.5), "perimetrium / myometrium", ha="left")
    label(a, (-0.9, 0.6), (-3.6, -1.1), "endometrium")
    label(a, (0.0, -1.6), (-3.6, -2.0), "cervix")
    label(a, (0.3, -2.9), (2.2, -3.4), "vagina")
    a.text(0, -4.6, "Front view (schematic): oviduct → uterus → cervix → vagina", ha="center", fontsize=8.5, color=GREY)
    save(fig, "bio_ch02_fig05_female_system.png")


def fig06_cleavage():
    fig, a = canvas(9.6, 3.0, (0, 20), (0, 5.6))
    xs = [1.6, 5.2, 8.8, 12.6, 17.2]
    names = ["zygote", "2-cell stage", "4-cell stage", "morula\n(8–16 blastomeres)", "blastocyst"]
    for x, n in zip(xs, names):
        a.add_patch(Circle((x, 3.0), 1.3, fc="white", ec=BLUE, lw=1.6))
        a.text(x, 0.75, n, ha="center", fontsize=8.5)
    a.add_patch(Circle((xs[0], 3.0), 0.3, fc=PALE_RED, ec=RED))
    for dx in (-0.55, 0.55):
        a.add_patch(Circle((xs[1] + dx, 3.0), 0.55, fc=PALE_BLUE, ec=BLUE))
    for dx, dy in ((-0.5, 0.5), (0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)):
        a.add_patch(Circle((xs[2] + dx, 3.0 + dy), 0.48, fc=PALE_BLUE, ec=BLUE))
    for dx in (-0.7, 0, 0.7):
        for dy in (-0.7, 0, 0.7):
            if dx * dx + dy * dy < 1.0:
                a.add_patch(Circle((xs[3] + dx, 3.0 + dy), 0.36, fc=PALE_BLUE, ec=BLUE))
    for t in np.linspace(0, 2 * np.pi, 18, endpoint=False):
        a.add_patch(Circle((xs[4] + 1.1 * np.cos(t), 3.0 + 1.1 * np.sin(t)), 0.2, fc=PALE_AMBER, ec=AMBER, lw=0.7))
    for dx, dy in ((-0.45, 0.55), (-0.1, 0.65), (-0.6, 0.2), (-0.3, 0.25)):
        a.add_patch(Circle((xs[4] + dx, 3.0 + dy), 0.2, fc="#D5E6D6", ec=GREEN, lw=0.7))
    for i in range(4):
        arrow(a, (xs[i] + 1.35, 3.0), (xs[i + 1] - 1.35, 3.0))
    label(a, (xs[4] + 1.05, 2.4), (19.8, 1.4), "trophoblast", ha="right")
    label(a, (xs[4] - 0.3, 3.4), (15.0, 5.3), "inner cell mass", ha="left")
    a.text(7.0, 5.25, "Mitotic divisions while moving through the isthmus towards the uterus", ha="center",
           fontsize=8.5, color=GREY)
    save(fig, "bio_ch02_fig06_cleavage.png")


if __name__ == "__main__":
    fig01_gametogenesis()
    fig02_sperm()
    fig03_menstrual_hormones()
    fig04_ovum_sperms()
    fig05_female_system()
    fig06_cleavage()
