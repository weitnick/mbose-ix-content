"""Figures for Class X Computer Science, Ch03: Number Systems."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import flow, table_fig


def fig_systems():
    table_fig(["Number system", "Base (radix)", "Digits used", "Example"],
              [["Binary", "2", "0, 1", "(1011)₂"],
               ["Octal", "8", "0 to 7", "(257)₈"],
               ["Decimal", "10", "0 to 9", "(345)₁₀"],
               ["Hexadecimal", "16", "0 to 9 and A to F (A = 10 … F = 15)", "(2F)₁₆"]],
              "cs_ch03_fig01_systems.png", col_w=[2.8, 2.2, 5.0, 2.4],
              title="The four standard number systems", size=8.6)


def fig_division():
    table_fig(["Divide by 2", "Quotient", "Remainder"],
              [["124 ÷ 2", "62", "0  ← least significant bit (read last)"],
               ["62 ÷ 2", "31", "0"],
               ["31 ÷ 2", "15", "1"],
               ["15 ÷ 2", "7", "1"],
               ["7 ÷ 2", "3", "1"],
               ["3 ÷ 2", "1", "1"],
               ["1 ÷ 2", "0", "1  ← most significant bit (read first)"]],
              "cs_ch03_fig02_division.png", col_w=[3.0, 2.4, 6.0],
              title="Decimal to binary: (124)₁₀ = (1111100)₂ — read the remainders from bottom to top", size=8.6)


def fig_units():
    flow(["bit\n(0 or 1)", "nibble\n= 4 bits", "byte\n= 8 bits", "1 KB\n= 1024 bytes", "1 MB\n= 1024 KB",
          "1 GB\n= 1024 MB", "1 TB\n= 1024 GB"],
         "cs_ch03_fig03_units.png", width=11.5, w=1.45, h=1.0, size=8.4,
         title="Units of memory")


if __name__ == "__main__":
    fig_systems()
    fig_division()
    fig_units()
