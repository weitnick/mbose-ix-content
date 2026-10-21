"""Figures for Class X Computer Science, Ch09: C++ Operators and Expressions."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import flow, table_fig  # noqa: E402


def fig_kinds():
    table_fig(["Kind", "Operators", "Example (a = 7, b = 2)", "Result"],
              [["Arithmetic", "+   -   *   /   %", "a / b   and   a % b", "3   and   1"],
               ["Relational", "<   >   <=   >=   ==   !=", "a > b", "1 (true)"],
               ["Logical", "&&   ||   !", "(a > 5) && (b > 5)", "0 (false)"],
               ["Assignment", "=   +=   -=   *=   /=   %=", "a += b", "a becomes 9"],
               ["Increment, decrement", "++   --", "++a", "a becomes 8"],
               ["Conditional (ternary)", "? :", "(a > b) ? a : b", "7"],
               ["Comma", ",", "x = (a++, a + b)", "x = 10"]],
              "cs_ch09_fig01_kinds.png", col_w=[3.2, 4.0, 4.0, 2.4], title="Kinds of operators in C++", size=8.8)


def fig_precedence():
    table_fig(["Level", "Operators", "Name", "Associativity"],
              [["1 (highest)", "( )", "parentheses", "left to right"],
               ["2", "!   ++   --   unary -", "unary", "right to left"],
               ["3", "*   /   %", "multiplicative", "left to right"],
               ["4", "+   -", "additive", "left to right"],
               ["5", "<   <=   >   >=", "relational", "left to right"],
               ["6", "==   !=", "equality", "left to right"],
               ["7", "&&", "logical AND", "left to right"],
               ["8", "||", "logical OR", "left to right"],
               ["9", "? :", "conditional", "right to left"],
               ["10", "=   +=   -=   *=   /=   %=", "assignment", "right to left"],
               ["11 (lowest)", ",", "comma", "left to right"]],
              "cs_ch09_fig02_precedence.png", col_w=[2.2, 4.2, 3.0, 2.6],
              title="Precedence of C++ operators (highest first)", size=8.8)


def fig_eval():
    flow(["w = x + y % 2 - (x + y)", "w = 5 + 7 % 2 - (12)\n\nbrackets first", "w = 5 + 1 - 12\n\n% before + and -",
          "w = 6 - 12\n\nleft to right", "w = -6"],
         "cs_ch09_fig03_eval.png", width=11.5, w=2.15, h=1.15, size=8.4,
         title="Evaluating w = x + y % 2 - (x + y) with x = 5, y = 7")


def fig_prefix():
    table_fig(["Statement (a = 5 before each)", "What happens", "a", "b"],
              [["b = ++a;", "prefix: a is increased first, then used", "6", "6"],
               ["b = a++;", "postfix: a is used first, then increased", "6", "5"],
               ["b = --a;", "prefix: a is decreased first, then used", "4", "4"],
               ["b = a--;", "postfix: a is used first, then decreased", "4", "5"]],
              "cs_ch09_fig04_prefix.png", col_w=[4.6, 5.6, 0.9, 0.9],
              title="Prefix and postfix increment and decrement", size=9.0)


if __name__ == "__main__":
    fig_kinds()
    fig_precedence()
    fig_eval()
    fig_prefix()
