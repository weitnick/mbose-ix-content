"""Figures for Class XII Biology Chapter 3, Reproductive Health.
Run: python xii_bio_ch03_repro_health.py
"""
from xii_bio_common import *


def fig01_contraceptives():
    fig, a = canvas(10.0, 4.6, (0, 20), (0, 9.2))
    box(a, (7.0, 7.6), 6.0, 1.1, "Contraceptive methods", fc=SOFT, ec=BLUE, fs=10, bold=True)
    groups = [
        ("Natural", "periodic abstinence\n(days 10–17)\nwithdrawal\n(coitus interruptus)\nlactational\namenorrhea",
         PALE_GREEN, GREEN),
        ("Barrier", "condoms\n(male, female)\ndiaphragm,\ncervical cap, vault\n+ spermicides", PALE_BLUE, BLUE),
        ("IUDs", "non-medicated:\nLippes loop\ncopper: CuT, Cu7,\nMultiload 375\nhormonal:\nProgestasert, LNG-20",
         PALE_AMBER, AMBER),
        ("Hormonal", "oral pills\n(Saheli: once a week)\ninjections, implants\nemergency pills\n(within 72 hours)",
         PALE_RED, RED),
        ("Surgical", "vasectomy (male):\nvas deferens\ntubectomy (female):\nfallopian tube\nblock gamete\ntransport",
         "#EFE3F2", "#7B3F8C"),
    ]
    w, gap = 3.6, 0.4
    for i, (title, body, fc, ec) in enumerate(groups):
        x = 0.2 + i * (w + gap)
        box(a, (x, 5.0), w, 0.9, title, fc=fc, ec=ec, fs=9.5, bold=True)
        a.add_patch(FancyBboxPatch((x, 0.4), w, 4.2, boxstyle="round,pad=0.05,rounding_size=0.15", fc="white", ec=ec,
                                   lw=1))
        a.text(x + w / 2, 2.5, body, ha="center", va="center", fontsize=7.6, linespacing=1.35)
        arrow(a, (10.0, 7.6), (x + w / 2, 5.9), lw=1.0, ms=8)
    save(fig, "bio_ch03_fig01_contraceptives.png")


def fig02_art():
    fig, a = canvas(10.0, 4.4, (0, 20), (0, 8.8))
    box(a, (0.3, 6.6), 4.6, 1.4, "Ova (wife/donor)\n+ sperms (husband/donor)", fc=PALE_BLUE, ec=BLUE, fs=8.5)
    box(a, (5.9, 6.6), 5.2, 1.4, "IVF: fertilisation in the\nlaboratory (test-tube baby)", fc=SOFT, ec=BLUE, fs=8.5,
        bold=True)
    box(a, (12.6, 7.3), 7.1, 1.0, "ZIFT: zygote / embryo up to 8 blastomeres\n→ fallopian tube", fc=PALE_GREEN,
        ec=GREEN, fs=8)
    box(a, (12.6, 5.9), 7.1, 1.0, "IUT: embryo with more than 8 blastomeres\n→ uterus", fc=PALE_GREEN, ec=GREEN, fs=8)
    arrow(a, (4.9, 7.3), (5.9, 7.3))
    arrow(a, (11.1, 7.5), (12.6, 7.8))
    arrow(a, (11.1, 7.0), (12.6, 6.4))
    box(a, (0.3, 3.4), 9.2, 1.6, "GIFT: ovum from a donor transferred into the fallopian tube\nof a woman who cannot "
        "produce ova but can support\nfertilisation and development", fc=PALE_AMBER, ec=AMBER, fs=8)
    box(a, (10.5, 3.4), 9.2, 1.6, "ICSI: a sperm is injected directly into the ovum\nin the laboratory, then the "
        "embryo is transferred", fc=PALE_RED, ec=RED, fs=8)
    box(a, (0.3, 0.4), 19.4, 1.8, "AI / IUI: semen from the husband or a healthy donor is introduced into the vagina "
        "or uterus\n(when the male cannot inseminate, or the sperm count is very low)", fc="#EFE3F2", ec="#7B3F8C",
        fs=8.5)
    save(fig, "bio_ch03_fig02_art.png")


if __name__ == "__main__":
    fig01_contraceptives()
    fig02_art()
