"""Figures for Class X Computer Science, Ch14: Cyber Security and Data Protection."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import INK, FILLS, plt, save, box, arrow, table_fig  # noqa: E402

NOTE = "#7A2E1B"


def fig_encrypt():
    fig, ax = plt.subplots(figsize=(11, 3.0))
    box(ax, (1.0, 1.2), "Plaintext\nMEET AT 5", fc=FILLS[0], w=1.7, h=0.9, size=9.5, bold=True)
    box(ax, (3.2, 1.2), "Encryption\ncipher + key\n(shift each letter by 3)", fc=FILLS[1], w=2.2, h=1.1, size=8.8)
    box(ax, (5.6, 1.2), "Ciphertext\nPHHW DW 5", fc=FILLS[3], w=1.8, h=0.9, size=9.5, bold=True)
    box(ax, (8.0, 1.2), "Decryption\nsame cipher + key\n(shift back by 3)", fc=FILLS[2], w=2.2, h=1.1, size=8.8)
    box(ax, (10.2, 1.2), "Plaintext\nMEET AT 5", fc=FILLS[0], w=1.7, h=0.9, size=9.5, bold=True)
    arrow(ax, (1.85, 1.2), (2.1, 1.2))
    arrow(ax, (4.3, 1.2), (4.7, 1.2))
    arrow(ax, (6.5, 1.2), (6.9, 1.2))
    arrow(ax, (9.1, 1.2), (9.35, 1.2))
    ax.text(5.6, 0.45, "sent over the Internet: unreadable to anyone without the key", ha="center", va="center",
            fontsize=8.8, style="italic", color=NOTE)
    ax.set_xlim(0, 11.2)
    ax.set_ylim(0.15, 2.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Encryption and decryption (a simple shift cipher)", fontsize=11, fontweight="bold", color=INK)
    save(fig, "cs_ch14_fig01_encrypt.png")


def fig_firewall():
    fig, ax = plt.subplots(figsize=(11, 3.6))
    box(ax, (1.4, 1.7), "Your computer\nor school network", fc=FILLS[0], w=2.3, h=1.0, size=9.5)
    box(ax, (5.5, 1.7), "FIREWALL\nchecks traffic against\nsecurity rules", fc=FILLS[3], w=2.6, h=1.3, size=9.5,
        bold=True)
    box(ax, (9.6, 1.7), "Internet\n(external systems)", fc=FILLS[5], w=2.3, h=1.0, size=9.5)
    arrow(ax, (2.55, 1.9), (4.2, 1.9))
    arrow(ax, (4.2, 1.5), (2.55, 1.5))
    arrow(ax, (6.8, 1.9), (8.45, 1.9))
    arrow(ax, (8.45, 1.5), (6.8, 1.5))
    ax.text(7.62, 2.5, "allowed traffic passes", ha="center", fontsize=8.4, color=INK)
    ax.text(7.62, 0.8, "harmful traffic blocked", ha="center", fontsize=8.4, color=NOTE, fontweight="bold")
    ax.text(5.5, 0.2, "Modes:  packet filtering  ·  proxy (intermediary)  ·  inspection (checks every packet)",
            ha="center", fontsize=9.2, style="italic", color=INK)
    ax.set_xlim(0, 11)
    ax.set_ylim(-0.1, 2.9)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("A firewall stands between a private network and the Internet", fontsize=11, fontweight="bold",
                 color=INK)
    save(fig, "cs_ch14_fig02_firewall.png")


def fig_backup():
    table_fig(["Type of backup", "What is copied", "Good point"],
              [["Full backup", "all the selected data, every time", "simplest to restore"],
               ["Incremental backup", "only data changed since the last backup of any kind", "fastest; least space"],
               ["Differential backup", "data changed since the last full backup", "restore needs only two sets"],
               ["Online (cloud) backup", "a copy kept at a remote online location", "safe from fire, theft, damage"],
               ["Drive imaging", "an exact image of the whole drive (OS, programs, data)",
                "restores the entire system"]],
              "cs_ch14_fig03_backup.png", col_w=[3.4, 6.6, 3.6], title="Types of data backup", size=8.9)


def fig_ecommerce():
    table_fig(["E-commerce security", "It ensures that", "How"],
              [["Privacy", "information is protected from unauthorised use", "encryption, privacy policies"],
               ["Integrity", "information is not changed on the way", "encryption, checksums"],
               ["Authentication", "both sides are who they claim to be", "passwords, OTP, digital certificates"],
               ["Non-repudiation", "information is intact and there is evidence it was received",
                "digital signatures, receipts"]],
              "cs_ch14_fig04_ecommerce.png", col_w=[3.2, 6.8, 4.0], title="The four aims of e-commerce security",
              size=8.9)


if __name__ == "__main__":
    fig_encrypt()
    fig_firewall()
    fig_backup()
    fig_ecommerce()
