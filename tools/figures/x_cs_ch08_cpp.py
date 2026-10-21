"""Figures for Class X Computer Science, Ch08: OOP and Introduction to C++."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import INK, FILLS, plt, save, flow, tree  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

MONO = "DejaVu Sans Mono"
NOTE = "#7A2E1B"


def _class_box(ax, x, y, w, title, attrs, methods, fc):
    lh = 0.36
    h_t, h_a, h_m = 0.5, lh * len(attrs) + 0.2, lh * len(methods) + 0.2
    top = y
    ax.add_patch(Rectangle((x, top - h_t), w, h_t, fc=fc, ec=INK, lw=1.1))
    ax.text(x + w / 2, top - h_t / 2, title, ha="center", va="center", fontsize=10.5, fontweight="bold")
    ax.add_patch(Rectangle((x, top - h_t - h_a), w, h_a, fc="white", ec=INK, lw=1.1))
    for i, a in enumerate(attrs):
        ax.text(x + 0.15, top - h_t - 0.28 - i * lh, a, ha="left", va="center", fontsize=9.2, family=MONO)
    ax.add_patch(Rectangle((x, top - h_t - h_a - h_m), w, h_m, fc="white", ec=INK, lw=1.1))
    for i, m in enumerate(methods):
        ax.text(x + 0.15, top - h_t - h_a - 0.28 - i * lh, m, ha="left", va="center", fontsize=9.2, family=MONO)
    return top - h_t - h_a - h_m, top - h_t - h_a / 2, top - h_t - h_a - h_m / 2


def fig_class():
    fig, ax = plt.subplots(figsize=(10.5, 4.0))
    bottom, ya, ym = _class_box(ax, 0.2, 3.6, 3.0, "class Student", ["roll", "name", "marks"],
                                ["readData()", "display()"], FILLS[0])
    ax.text(3.35, ya, "data members\n(attributes / state)", ha="left", va="center", fontsize=8.6, style="italic", color=NOTE)
    ax.text(3.35, ym, "member functions\n(methods / behaviour)", ha="left", va="center", fontsize=8.6, style="italic",
            color=NOTE)
    _class_box(ax, 6.2, 3.6, 2.0, "object s1", ["1", "Bari", "86"], ["readData()", "display()"], FILLS[2])
    _class_box(ax, 8.5, 3.6, 2.0, "object s2", ["2", "Iba", "91"], ["readData()", "display()"], FILLS[2])
    for x in (6.2, 8.5):
        ax.annotate("", xy=(x + 1.0, 3.62), xytext=(1.7, 3.62),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0, connectionstyle="arc3,rad=-0.25"))
    ax.set_xlim(0, 10.7)
    ax.set_ylim(bottom - 0.3, 4.6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("A class is a blueprint; objects are created from it", fontsize=11, fontweight="bold", color=INK, pad=14)
    save(fig, "cs_ch08_fig01_class.png")


def fig_inherit():
    tree("Vehicle\n(base / parent class)", ["Car\n(derived / child class)", "Bus\n(derived / child class)"],
         "cs_ch08_fig02_inherit.png",
         grand={0: ["inherits wheels, speed", "adds: seats = 5"], 1: ["inherits wheels, speed", "adds: route number"]},
         width=8.5, child_w=3.2, size=9.0, title="Inheritance: a derived (child) class reuses its base (parent) class")


def fig_structure():
    lines = [("// Program to add two numbers", "comment: ignored by the compiler"),
             ("#include <iostream>", "header file (preprocessor directive)"),
             ("using namespace std;", "lets us write cout instead of std::cout"),
             ("int main()", "main function: execution starts here"),
             ("{", "opening brace: start of the body"),
             ("    int a, b, sum;", "variable declaration"),
             ("    cin >> a >> b;", "input with cin and >>"),
             ("    sum = a + b;", "every statement ends with ;"),
             ('    cout << "Sum = " << sum << endl;', "output with cout and <<; endl = new line"),
             ("    return 0;", "returns 0 to the system: program ended normally"),
             ("}", "closing brace: end of the program")]
    n = len(lines)
    fig, ax = plt.subplots(figsize=(11, 0.42 * n + 0.7))
    ax.add_patch(Rectangle((0, -0.3), 5.6, n + 0.1, fc="#F3F5F8", ec="#B8C2CC", lw=0.8))
    for i, (code, note) in enumerate(lines):
        y = n - 1 - i
        ax.text(0.15, y, code, ha="left", va="center", fontsize=9.6, family=MONO, color=INK)
        ax.annotate(note, xy=(5.65, y), xytext=(6.1, y), ha="left", va="center", fontsize=9.0, color=NOTE,
                    arrowprops=dict(arrowstyle="-", color=NOTE, lw=0.7))
    ax.set_xlim(0, 11.6)
    ax.set_ylim(-0.5, n)
    ax.axis("off")
    ax.set_title("The structure of a C++ program", fontsize=11, fontweight="bold", color=INK)
    save(fig, "cs_ch08_fig03_structure.png")


def fig_compile():
    flow(["Source code\n(add.cpp)\nwritten by you", "Compiler\nchecks syntax,\ntranslates", "Object code\n(add.obj)",
          "Linker\njoins library\ncode", "Executable\n(add.exe)", "Run:\noutput on\nthe screen"],
         "cs_ch08_fig04_compile.png", width=11.0, w=1.6, h=1.15, size=8.4,
         title="From a C++ program to its output")


if __name__ == "__main__":
    fig_class()
    fig_inherit()
    fig_structure()
    fig_compile()
