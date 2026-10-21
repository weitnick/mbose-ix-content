"""Figures for Class XII Chemistry Chapter 5, Coordination Compounds.
Run: python xii_chem_ch05_coordination.py
"""
from xii_chem_common import *
from matplotlib.patches import Arc

# perspective positions of the six octahedral sites around the centre (unit scale)
OCT = {"top": (0, 1.25), "bot": (0, -1.25), "fl": (-0.95, -0.35), "br": (0.95, 0.35), "fr": (0.75, -0.55),
       "bl": (-0.75, 0.55)}


def octa(ax, cx, cy, centre, lig, s=1.0, fs=10, chel=()):
    """lig: dict site -> label. chel: list of (site1, site2, label) drawn as a curved chelate between two cis sites."""
    pts = {k: (cx + v[0] * s, cy + v[1] * s) for k, v in OCT.items()}
    # faint octahedron edges (equatorial square)
    sq = ["fl", "fr", "br", "bl", "fl"]
    for a, b in zip(sq, sq[1:]):
        ax.plot([pts[a][0], pts[b][0]], [pts[a][1], pts[b][1]], color=GREY, lw=0.7, ls=":")
    atoms = {"M": (cx, cy, centre)}
    bonds = []
    for k, lab in lig.items():
        atoms[k] = (pts[k][0], pts[k][1], lab)
        bonds.append(("M", k, 1))
    draw(ax, atoms, bonds, fs=fs, pad=0.26)
    for a, b, lab in chel:
        pa, pb = np.array(pts[a]), np.array(pts[b])
        mid = (pa + pb) / 2
        out = mid - np.array([cx, cy])
        out = out / (np.linalg.norm(out) or 1)
        ctrl = mid + out * 0.55 * s
        t = np.linspace(0, 1, 30)[:, None]
        curve = (1 - t) ** 2 * pa + 2 * (1 - t) * t * ctrl + t ** 2 * pb
        ax.plot(curve[:, 0], curve[:, 1], color=BLUE, lw=1.6)
        if lab:
            ax.text(ctrl[0] + out[0] * 0.18, ctrl[1] + out[1] * 0.18, lab, color=BLUE, fontsize=fs - 1,
                    ha="center", va="center")


def square(ax, cx, cy, centre, lig, s=1.0, fs=11):
    pos = {"n": (cx, cy + s), "e": (cx + s, cy), "s": (cx, cy - s), "w": (cx - s, cy)}
    atoms = {"M": (cx, cy, centre)}
    bonds = []
    for k, lab in lig.items():
        atoms[k] = (pos[k][0], pos[k][1], lab)
        bonds.append(("M", k, 1))
    draw(ax, atoms, bonds, fs=fs)


def levels(ax, x0, ys, labels, w=0.9, color=INK):
    for y, lab in zip(ys, labels):
        pass


def fig01_splitting():
    fig, axs = plt.subplots(1, 2, figsize=(10.0, 4.2))
    for ax in axs:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis("off")
    # octahedral
    ax = axs[0]
    ax.set_title("Octahedral field")
    for i in range(5):
        ax.plot([0.4 + i * 0.55, 0.85 + i * 0.55], [4, 4], color=INK, lw=2)
    ax.text(1.7, 3.4, "free ion\n(degenerate d)", ha="center", fontsize=8.5)
    ax.plot([0.4, 3.3], [4.7, 4.7], color=GREY, ls="--", lw=0.8)
    ax.text(1.85, 5.0, "barycentre (spherical field)", ha="center", fontsize=7.5, color=GREY)
    for i in range(2):
        ax.plot([5.6 + i * 0.75, 6.2 + i * 0.75], [6.4, 6.4], color=RED, lw=2)
    ax.text(7.6, 6.4, "e_g  (d_x²−y², d_z²)", va="center", fontsize=9, color=RED)
    for i in range(3):
        ax.plot([5.2 + i * 0.75, 5.8 + i * 0.75], [3.3, 3.3], color=BLUE, lw=2)
    ax.text(7.6, 3.3, "t₂g  (d_xy, d_yz, d_xz)", va="center", fontsize=9, color=BLUE)
    ax.plot([3.4, 5.0], [4.7, 4.7], color=GREY, ls=":", lw=0.8)
    ax.add_patch(FancyArrowPatch((5.0, 3.3), (5.0, 6.4), arrowstyle="<|-|>", mutation_scale=10, color=INK))
    ax.text(4.35, 5.0, "Δo", fontsize=11, weight="bold")
    ax.text(8.0, 5.5, "+0.6 Δo", fontsize=8.5, color=RED)
    ax.text(8.0, 2.6, "−0.4 Δo", fontsize=8.5, color=BLUE)
    # tetrahedral
    ax = axs[1]
    ax.set_title("Tetrahedral field (Δt = 4/9 Δo)")
    for i in range(5):
        ax.plot([0.4 + i * 0.55, 0.85 + i * 0.55], [4, 4], color=INK, lw=2)
    ax.text(1.7, 3.4, "free ion", ha="center", fontsize=8.5)
    for i in range(3):
        ax.plot([5.2 + i * 0.75, 5.8 + i * 0.75], [5.6, 5.6], color=RED, lw=2)
    ax.text(7.6, 5.6, "t₂  (d_xy, d_yz, d_xz)", va="center", fontsize=9, color=RED)
    for i in range(2):
        ax.plot([5.6 + i * 0.75, 6.2 + i * 0.75], [3.8, 3.8], color=BLUE, lw=2)
    ax.text(7.6, 3.8, "e  (d_x²−y², d_z²)", va="center", fontsize=9, color=BLUE)
    ax.add_patch(FancyArrowPatch((5.0, 3.8), (5.0, 5.6), arrowstyle="<|-|>", mutation_scale=10, color=INK))
    ax.text(4.4, 4.5, "Δt", fontsize=11, weight="bold")
    ax.text(5.0, 1.6, "Splitting is inverted and smaller;\ntetrahedral complexes are high spin.", ha="center", fontsize=8.5)
    save(fig, "chem_ch05_fig01_splitting.png")


def fig02_cis_trans():
    fig, ax = canvas(11.0, 4.6, (0, 22), (0, 9.2))
    square(ax, 2.8, 5.6, "Pt", {"n": "Cl", "e": "NH₃", "s": "NH₃", "w": "Cl"}, s=1.5)
    ax.text(2.8, 3.2, "cis-[Pt(NH₃)₂Cl₂]", ha="center", fontsize=9)
    square(ax, 8.0, 5.6, "Pt", {"n": "Cl", "e": "NH₃", "s": "Cl", "w": "NH₃"}, s=1.5)
    ax.text(8.0, 3.2, "trans-[Pt(NH₃)₂Cl₂]", ha="center", fontsize=9)
    octa(ax, 13.6, 5.2, "Co", {"top": "Cl", "bot": "NH₃", "fl": "NH₃", "br": "NH₃", "fr": "Cl", "bl": "NH₃"}, s=1.55)
    ax.text(13.6, 2.3, "cis-[Co(NH₃)₄Cl₂]⁺ (violet)", ha="center", fontsize=9)
    octa(ax, 19.0, 5.2, "Co", {"top": "Cl", "bot": "Cl", "fl": "NH₃", "br": "NH₃", "fr": "NH₃", "bl": "NH₃"}, s=1.55)
    ax.text(19.0, 2.3, "trans-[Co(NH₃)₄Cl₂]⁺ (green)", ha="center", fontsize=9)
    ax.text(11.0, 0.6, "cis: identical ligands on adjacent positions (90°); trans: on opposite positions (180°)",
            ha="center", fontsize=9, color=GREY)
    save(fig, "chem_ch05_fig02_cis_trans.png")


def fig03_fac_mer():
    fig, ax = canvas(8.0, 4.4, (0, 16), (0, 8.8))
    octa(ax, 4.0, 5.0, "Co", {"top": "Cl", "bot": "NH₃", "fl": "NH₃", "br": "Cl", "fr": "Cl", "bl": "NH₃"}, s=1.6)
    ax.text(4.0, 2.0, "fac-[Co(NH₃)₃Cl₃]\n(three Cl on one face)", ha="center", fontsize=9)
    octa(ax, 12.0, 5.0, "Co", {"top": "Cl", "bot": "Cl", "fl": "NH₃", "br": "NH₃", "fr": "Cl", "bl": "NH₃"}, s=1.6)
    ax.text(12.0, 2.0, "mer-[Co(NH₃)₃Cl₃]\n(three Cl around a meridian)", ha="center", fontsize=9)
    ax.text(8.0, 0.4, "The same two forms occur for every [MA₃B₃], e.g. [Co(NO₂)₃(NH₃)₃]", ha="center", fontsize=8.5,
            color=GREY)
    save(fig, "chem_ch05_fig03_fac_mer.png")


def fig04_optical():
    fig, ax = canvas(10.0, 4.4, (0, 20), (0, 8.8))
    octa(ax, 4.5, 5.0, "Co", {"top": "", "bot": "", "fl": "", "br": "Cl", "fr": "", "bl": "Cl"}, s=1.6,
         chel=[("top", "fl", "en"), ("bot", "fr", "en")])
    ax.text(4.5, 1.6, "cis-[CoCl₂(en)₂]⁺  (d)", ha="center", fontsize=9)
    ax.plot([10, 10], [1.5, 8.2], color=GREY, lw=1.2, ls="--")
    ax.text(10, 8.4, "mirror", ha="center", fontsize=8.5, color=GREY)
    # mirror image: swap left/right sites
    octa(ax, 15.5, 5.0, "Co", {"top": "", "bot": "", "fr": "", "bl": "Cl", "br": "Cl", "fl": ""}, s=1.6,
         chel=[("top", "br", "en"), ("bot", "fl", "en")])
    ax.text(15.5, 1.6, "cis-[CoCl₂(en)₂]⁺  (l)", ha="center", fontsize=9)
    ax.text(10, 0.4, "Non-superimposable mirror images (enantiomers); the trans isomer is optically inactive",
            ha="center", fontsize=8.5, color=GREY)
    save(fig, "chem_ch05_fig04_optical.png")


def fig05_mabcn():
    fig, ax = canvas(8.0, 4.4, (0, 16), (0, 8.8))
    octa(ax, 4.0, 5.0, "Fe", {"top": "NH₃", "bot": "CN", "fl": "CN", "br": "CN", "fr": "NH₃", "bl": "CN"}, s=1.6)
    ax.text(4.0, 2.0, "cis-[Fe(NH₃)₂(CN)₄]⁻", ha="center", fontsize=9)
    octa(ax, 12.0, 5.0, "Fe", {"top": "NH₃", "bot": "NH₃", "fl": "CN", "br": "CN", "fr": "CN", "bl": "CN"}, s=1.6)
    ax.text(12.0, 2.0, "trans-[Fe(NH₃)₂(CN)₄]⁻", ha="center", fontsize=9)
    save(fig, "chem_ch05_fig05_fe_nh3_cn.png")


def fig06_ox():
    fig, ax = canvas(12.0, 4.4, (0, 24), (0, 8.8))
    octa(ax, 4.0, 5.0, "Cr", {"top": "Cl", "bot": "Cl", "fl": "", "br": "", "fr": "", "bl": ""}, s=1.6,
         chel=[("fl", "fr", "ox"), ("br", "bl", "ox")])
    ax.text(4.0, 1.8, "trans-[CrCl₂(ox)₂]³⁻\n(has a mirror plane: optically inactive)", ha="center", fontsize=8.5)
    octa(ax, 12.0, 5.0, "Cr", {"top": "", "bot": "", "fl": "", "br": "Cl", "fr": "", "bl": "Cl"}, s=1.6,
         chel=[("top", "fl", "ox"), ("bot", "fr", "ox")])
    ax.text(12.0, 1.8, "cis (d)", ha="center", fontsize=9)
    octa(ax, 20.0, 5.0, "Cr", {"top": "", "bot": "", "fr": "", "bl": "Cl", "br": "Cl", "fl": ""}, s=1.6,
         chel=[("top", "br", "ox"), ("bot", "fl", "ox")])
    ax.text(20.0, 1.8, "cis (l)", ha="center", fontsize=9)
    ax.text(16.0, 0.4, "cis-[CrCl₂(ox)₂]³⁻ has no plane of symmetry: optically active (d and l forms)", ha="center",
            fontsize=8.5, color=GREY)
    save(fig, "chem_ch05_fig06_cr_ox.png")


if __name__ == "__main__":
    fig01_splitting()
    fig02_cis_trans()
    fig03_fac_mer()
    fig04_optical()
    fig05_mabcn()
    fig06_ox()
