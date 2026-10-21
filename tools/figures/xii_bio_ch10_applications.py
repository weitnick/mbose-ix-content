"""Figures for Class XII Biology Chapter 10, Biotechnology and its Applications.
Run: python xii_bio_ch10_applications.py
"""
from xii_bio_common import *


def fig01_tissue_culture():
    fig, a = canvas(10.0, 4.6, (0, 20), (0, 9.2))
    a.text(10.0, 8.7, "Plant tissue culture and micropropagation", ha="center", fontsize=10, weight="bold")
    steps = [("explant\n(leaf, stem, root\nor meristem piece)", SOFT, BLUE),
             ("sterilise; place on\nnutrient medium\n(sterile, in vitro)", PALE_AMBER, AMBER),
             ("callus\n(undifferentiated\nmass of cells)", PALE_GREEN, GREEN),
             ("shoots and roots\nform (cytokinin,\nauxin ratio)", SOFT, BLUE),
             ("plantlets\n(somaclones)", PALE_GREEN, GREEN),
             ("hardening in\npots, then\nfield", PALE_AMBER, AMBER)]
    for i, (t, fc, ec) in enumerate(steps):
        x = 0.2 + i * 3.3
        box(a, (x, 4.6), 2.9, 2.9, t, fc=fc, ec=ec, fs=8)
        if i < 5:
            arrow(a, (x + 2.9, 6.05), (x + 3.3, 6.05), ms=9)
    a.text(10.0, 3.6, "Medium: carbon source (sucrose), inorganic salts, vitamins, amino acids and growth regulators "
                      "(auxins, cytokinins)", ha="center", fontsize=8.2)
    a.text(10.0, 2.7, "Totipotency: the capacity of any cell or explant to grow into a whole plant", ha="center",
           fontsize=8.2, color=BLUE)
    a.text(10.0, 1.8, "Meristem (apical, axillary) is free of virus → meristem culture gives virus-free banana, "
                      "sugarcane, potato", ha="center", fontsize=8.2, color=GREEN)
    a.text(10.0, 0.9, "Protoplasts of two plants fused → somatic hybrid (tomato + potato = pomato)", ha="center",
           fontsize=8.2, color=AMBER)
    save(fig, "bio_ch10_fig01_tissue_culture.png")


def fig02_bt_toxin():
    fig, a = canvas(10.0, 4.2, (0, 20), (0, 8.4))
    a.text(10.0, 7.9, "How Bt toxin kills an insect (but not the bacterium)", ha="center", fontsize=10, weight="bold")
    steps = [("Bacillus thuringiensis\nforms protein crystals\n(inactive protoxin)", PALE_AMBER, AMBER),
             ("insect larva eats\nthe crystals (on Bt\ncotton leaves, bolls)", SOFT, BLUE),
             ("alkaline pH of the\ninsect gut dissolves\ncrystals → active toxin", PALE_GREEN, GREEN),
             ("toxin binds midgut\nepithelial cells and\nmakes pores", PALE_RED, RED),
             ("cells swell and\nburst (lysis) →\ninsect dies", PALE_RED, RED)]
    for i, (t, fc, ec) in enumerate(steps):
        x = 0.2 + i * 4.0
        box(a, (x, 3.6), 3.5, 3.2, t, fc=fc, ec=ec, fs=8.2)
        if i < 4:
            arrow(a, (x + 3.5, 5.2), (x + 4.0, 5.2), ms=9)
    a.text(10.0, 2.4, "cry genes code the toxin: cryIAc and cryIIAb control cotton bollworms; cryIAb controls corn borer",
           ha="center", fontsize=8.4)
    a.text(10.0, 1.4, "The bacterium is safe because the toxin stays inactive (protoxin) inside it", ha="center",
           fontsize=8.4, color=BLUE)
    save(fig, "bio_ch10_fig02_bt_toxin.png")


def fig03_rnai():
    fig, a = canvas(10.0, 4.6, (0, 20), (0, 9.2))
    a.text(10.0, 8.7, "RNA interference protects tobacco from the nematode Meloidogyne incognita", ha="center",
           fontsize=10, weight="bold")
    box(a, (0.3, 4.9), 3.6, 2.8, "nematode-specific\ngene put into\ntobacco using an\nAgrobacterium vector",
        fc=SOFT, ec=BLUE, fs=8.2)
    box(a, (4.6, 4.9), 3.6, 2.8, "plant makes sense\nand antisense RNA\nof that gene", fc=PALE_AMBER, ec=AMBER, fs=8.2)
    # dsRNA drawn as two coloured strands
    box(a, (8.9, 4.9), 3.6, 2.8, "", fc="white", ec=GREEN, fs=8.2)
    a.plot([9.3, 12.1], [6.65, 6.65], color=RED, lw=2.4)
    a.plot([9.3, 12.1], [6.25, 6.25], color=BLUE, lw=2.4)
    for xx in np.arange(9.5, 12.0, 0.3):
        a.plot([xx, xx], [6.28, 6.62], color=GREY, lw=0.8)
    a.text(10.7, 5.4, "dsRNA forms\n(sense + antisense)", ha="center", va="center", fontsize=8.2)
    box(a, (13.2, 4.9), 3.0, 2.8, "nematode feeds;\ndsRNA silences its\nspecific mRNA", fc=PALE_GREEN, ec=GREEN,
        fs=8.2)
    box(a, (16.9, 4.9), 2.9, 2.8, "no translation\n→ parasite\ncannot survive", fc=PALE_RED, ec=RED, fs=8.2,
        bold=True)
    for x0, x1 in [(3.9, 4.6), (8.2, 8.9), (12.5, 13.2), (16.2, 16.9)]:
        arrow(a, (x0, 6.3), (x1, 6.3), ms=9)
    a.text(10.0, 3.6, "RNAi: silencing of a specific mRNA by a complementary dsRNA that binds it and blocks translation",
           ha="center", fontsize=8.4)
    a.text(10.0, 2.7, "It occurs in all eukaryotes as a cellular defence; natural sources of dsRNA are RNA viruses and "
                      "transposons", ha="center", fontsize=8.2, color=GREY)
    a.text(10.0, 1.6, "Result: transgenic tobacco roots stay healthy even after deliberate infection", ha="center",
           fontsize=8.4, color=GREEN)
    save(fig, "bio_ch10_fig03_rnai.png")


def fig04_insulin():
    fig, a = canvas(10.0, 4.6, (0, 20), (0, 9.2))
    a.text(10.0, 8.7, "Maturation of pro-insulin into insulin, and the rDNA route", ha="center", fontsize=10,
           weight="bold")
    # pro-insulin: B chain - C peptide - A chain as one loop
    a.plot([0.8, 5.0], [6.6, 6.6], color=BLUE, lw=5, solid_capstyle="round")
    a.text(2.9, 7.1, "B chain", ha="center", fontsize=8.5, color=BLUE)
    a.plot([5.0, 5.6, 5.6, 5.0], [6.6, 6.6, 4.6, 4.6], color=AMBER, lw=5, solid_capstyle="round")
    a.text(6.0, 5.6, "C peptide", fontsize=8.5, color=AMBER, va="center")
    a.plot([5.0, 1.6], [4.6, 4.6], color=RED, lw=5, solid_capstyle="round")
    a.text(3.3, 4.0, "A chain", ha="center", fontsize=8.5, color=RED)
    for xx in (2.0, 3.8):
        a.plot([xx, xx], [4.75, 6.45], color=GREY, lw=1.2, ls="--")
    a.text(3.0, 3.2, "pro-insulin (pro-hormone)", ha="center", fontsize=8.5, weight="bold")
    arrow(a, (7.9, 5.6), (9.8, 5.6), text="C peptide\nremoved", fs=8, dy=0.25)
    a.plot([10.2, 14.4], [6.6, 6.6], color=BLUE, lw=5, solid_capstyle="round")
    a.plot([11.0, 14.4], [4.6, 4.6], color=RED, lw=5, solid_capstyle="round")
    for xx in (11.4, 13.2):
        a.plot([xx, xx], [4.75, 6.45], color=GREY, lw=1.2, ls="--")
    a.text(12.3, 7.1, "B chain", ha="center", fontsize=8.5, color=BLUE)
    a.text(12.7, 4.0, "A chain", ha="center", fontsize=8.5, color=RED)
    a.text(12.3, 3.2, "mature insulin", ha="center", fontsize=8.5, weight="bold")
    label(a, (13.2, 5.6), (15.2, 5.6), "disulphide bridges", fs=8)
    a.text(10.0, 1.9, "Eli Lilly (1983): DNA sequences for chains A and B put into separate E. coli plasmids → "
                      "chains made separately,", ha="center", fontsize=8.2)
    a.text(10.0, 1.1, "extracted and joined by disulphide bonds → human insulin (Humulin), no allergy unlike "
                      "cattle or pig insulin", ha="center", fontsize=8.2)
    save(fig, "bio_ch10_fig04_insulin.png")


def fig05_gene_therapy():
    fig, a = canvas(10.0, 3.8, (0, 20), (0, 7.6))
    a.text(10.0, 7.1, "Gene therapy for ADA deficiency (first clinical gene therapy, 1990)", ha="center",
           fontsize=10, weight="bold")
    steps = [("lymphocytes taken\nfrom the patient's\nblood", PALE_RED, RED),
             ("grown in culture\noutside the body", SOFT, BLUE),
             ("functional ADA cDNA\nput in using a\nretroviral vector", PALE_GREEN, GREEN),
             ("engineered\nlymphocytes returned\nto the patient", PALE_AMBER, AMBER),
             ("cells are not\nimmortal → periodic\ninfusion needed", SOFT, BLUE)]
    for i, (t, fc, ec) in enumerate(steps):
        x = 0.2 + i * 4.0
        box(a, (x, 3.0), 3.5, 3.0, t, fc=fc, ec=ec, fs=8.2)
        if i < 4:
            arrow(a, (x + 3.5, 4.5), (x + 4.0, 4.5), ms=9)
    a.text(10.0, 1.8, "Permanent cure: introduce the ADA gene from marrow cells into cells at an early embryonic stage",
           ha="center", fontsize=8.4, color=GREEN)
    a.text(10.0, 0.9, "Other treatments (not fully curative): bone-marrow transplantation; enzyme replacement therapy "
                      "(ADA injected)", ha="center", fontsize=8.2, color=GREY)
    save(fig, "bio_ch10_fig05_gene_therapy_ada.png")


if __name__ == "__main__":
    fig01_tissue_culture()
    fig02_bt_toxin()
    fig03_rnai()
    fig04_insulin()
    fig05_gene_therapy()
