"""Figures for Class XII Biology Chapter 7, Human Health and Disease.
Run: python xii_bio_ch07_health.py
"""
from xii_bio_common import *


def fig01_plasmodium():
    fig, a = canvas(9.4, 5.2, (0, 19), (0, 10.4))
    a.add_patch(FancyBboxPatch((0.3, 0.4), 8.6, 9.2, boxstyle="round,pad=0.1,rounding_size=0.4", fc="#FBF3F2",
                               ec=RED, lw=1.2))
    a.add_patch(FancyBboxPatch((10.1, 0.4), 8.6, 9.2, boxstyle="round,pad=0.1,rounding_size=0.4", fc="#F2F6FB",
                               ec=BLUE, lw=1.2))
    a.text(4.6, 9.0, "In human (asexual stages)", ha="center", fontsize=9.5, weight="bold", color=RED)
    a.text(14.4, 9.0, "In female Anopheles (sexual stages)", ha="center", fontsize=9.5, weight="bold",
           color=BLUE)
    h = [(4.6, 7.6, "sporozoites enter blood\nwith the mosquito bite"), (4.6, 5.8, "multiply in liver cells"),
         (4.6, 4.0, "attack RBCs, multiply; RBCs burst\n→ haemozoin released → chill and fever"),
         (4.6, 1.9, "gametocytes (sexual stages)\ndevelop in RBCs")]
    for x, y, t in h:
        box(a, (x - 3.6, y - 0.6), 7.2, 1.2, t, fc="white", ec=RED, fs=8)
    for i in range(3):
        arrow(a, (4.6, h[i][1] - 0.6), (4.6, h[i + 1][1] + 0.6), color=RED, lw=1.1, ms=9)
    m = [(14.4, 1.9, "gametocytes taken in with blood\nwhen the mosquito bites"),
         (14.4, 4.0, "fertilisation in the\nmosquito's stomach"),
         (14.4, 5.8, "zygote develops on the stomach wall"),
         (14.4, 7.6, "sporozoites move to the\nsalivary glands")]
    for x, y, t in m:
        box(a, (x - 3.6, y - 0.6), 7.2, 1.2, t, fc="white", ec=BLUE, fs=8)
    for i in range(3):
        arrow(a, (14.4, m[i][1] + 0.6), (14.4, m[i + 1][1] - 0.6), color=BLUE, lw=1.1, ms=9)
    arrow(a, (8.2, 1.9), (10.8, 1.9), color=INK, lw=1.4, text="mosquito bites\ninfected person", fs=7.5, dy=0.15)
    arrow(a, (10.8, 7.6), (8.2, 7.6), color=INK, lw=1.4, text="mosquito bites\nhealthy person", fs=7.5, dy=0.15)
    save(fig, "bio_ch07_fig01_plasmodium.png")


def fig02_antibody():
    fig, a = canvas(6.0, 5.6, (-5, 5), (-4.6, 4.8))
    # heavy chains (long, inner)
    for s in (-1, 1):
        a.plot([s * 0.35, s * 0.35], [-4.0, 0.2], color=BLUE, lw=6, solid_capstyle="round")
        a.plot([s * 0.35, s * 2.9], [0.2, 3.6], color=BLUE, lw=6, solid_capstyle="round")
        # light chains (short, outer)
        a.plot([s * 1.05, s * 3.6], [0.0, 3.3], color=AMBER, lw=6, solid_capstyle="round")
        a.add_patch(Circle((s * 3.35, 3.85), 0.42, fc="none", ec=RED, lw=1.6, ls="--"))
    for y in (-0.6, -1.1):
        a.plot([-0.35, 0.35], [y, y], color=INK, lw=1.4)
    for s in (-1, 1):
        a.plot([s * 0.75, s * 1.35], [0.75, 0.55], color=INK, lw=1.4)
    label(a, (-3.35, 3.85), (-4.8, 4.5), "antigen-binding site", ha="left")
    label(a, (3.35, 3.85), (2.2, 4.6), "antigen-binding site", ha="left")
    label(a, (2.4, 2.2), (3.3, 1.2), "light chain")
    label(a, (0.35, -2.5), (1.6, -2.5), "heavy chain")
    label(a, (0.0, -0.85), (-1.6, -1.9), "disulphide (S–S) bonds", ha="right")
    a.text(0, -4.45, "An antibody (H₂L₂): two heavy and two light polypeptide chains", ha="center", fontsize=8.5,
           color=GREY)
    save(fig, "bio_ch07_fig02_antibody.png")


def fig03_hiv():
    fig, a = canvas(9.4, 3.8, (0, 19), (0, 7.6))
    steps = ["HIV (RNA genome)\nenters a\nmacrophage", "reverse\ntranscriptase:\nviral RNA → DNA",
             "viral DNA joins\nhost DNA; cell\nmakes new viruses\n('HIV factory')", "viruses attack\nhelper T-cells\n(T-H) and multiply",
             "T-H cells fall;\nimmune system\nfails → AIDS"]
    for i, t in enumerate(steps):
        x = 0.3 + i * 3.75
        box(a, (x, 2.4), 3.3, 2.6, t, fc=PALE_RED if i == 4 else SOFT, ec=RED if i == 4 else BLUE, fs=8)
        if i < 4:
            arrow(a, (x + 3.3, 3.7), (x + 3.75, 3.7))
    a.text(9.5, 6.6, "How HIV causes immunodeficiency (time-lag 5–10 years)", ha="center", fontsize=9.5,
           weight="bold")
    a.text(9.5, 1.2, "Patient suffers fever, diarrhoea, weight loss and infections by Mycobacterium, viruses, fungi, "
                     "Toxoplasma; diagnosed by ELISA", ha="center", fontsize=8, color=GREY)
    save(fig, "bio_ch07_fig03_hiv.png")


if __name__ == "__main__":
    fig01_plasmodium()
    fig02_antibody()
    fig03_hiv()
