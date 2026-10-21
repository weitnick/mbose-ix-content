"""Figures for Class X Computer Science, Ch11: Introduction to Java."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import INK, FILLS, plt, save, box, arrow, table_fig  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

MONO = "DejaVu Sans Mono"
NOTE = "#7A2E1B"


def fig_wora():
    fig, ax = plt.subplots(figsize=(11, 4.2))
    box(ax, (1.1, 2.0), "Source code\nHello.java\n(written by you)", fc=FILLS[0], w=1.9, h=1.1, size=9)
    box(ax, (3.5, 2.0), "javac\n(Java compiler)", fc=FILLS[1], w=1.7, h=0.9, size=9, bold=True)
    box(ax, (5.9, 2.0), "Bytecode\nHello.class\n(platform-independent)", fc=FILLS[2], w=2.2, h=1.1, size=9)
    arrow(ax, (2.05, 2.0), (2.65, 2.0))
    arrow(ax, (4.35, 2.0), (4.8, 2.0))
    ys = [3.4, 2.0, 0.6]
    labels = ["JVM on Windows", "JVM on Linux", "JVM on macOS / Android"]
    for y, lab in zip(ys, labels):
        box(ax, (8.6, y), lab, fc=FILLS[3], w=2.2, h=0.7, size=9)
        arrow(ax, (7.0, 2.0), (7.5, y))
        arrow(ax, (9.7, y), (10.15, 2.0))
    box(ax, (10.9, 2.0), "same\noutput", fc=FILLS[5], w=1.1, h=0.8, size=9, bold=True)
    ax.text(5.9, 0.9, "the  java  command runs the\nbytecode on the JVM", ha="center", va="center", fontsize=8.6,
            style="italic", color=NOTE)
    ax.set_xlim(0, 11.6)
    ax.set_ylim(0.0, 4.1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Write once, run anywhere: how a Java program runs", fontsize=11, fontweight="bold", color=INK)
    save(fig, "cs_ch11_fig01_wora.png")


def fig_structure():
    lines = [("// My first Java program", "comment"),
             ("public class Hello", "class name = file name (Hello.java)"),
             ("{", "start of the class"),
             ("    public static void main(String[] args)", "main method: execution starts here"),
             ("    {", "start of the body of main"),
             ('        System.out.println("Hello, Meghalaya!");', "prints the text, then moves to a new line"),
             ("    }", "end of main"),
             ("}", "end of the class")]
    n = len(lines)
    fig, ax = plt.subplots(figsize=(11.5, 0.46 * n + 0.7))
    ax.add_patch(Rectangle((0, -0.35), 6.3, n + 0.15, fc="#F3F5F8", ec="#B8C2CC", lw=0.8))
    for i, (code, note) in enumerate(lines):
        y = n - 1 - i
        ax.text(0.15, y, code, ha="left", va="center", fontsize=9.6, family=MONO, color=INK)
        ax.annotate(note, xy=(6.35, y), xytext=(6.75, y), ha="left", va="center", fontsize=9.0, color=NOTE,
                    arrowprops=dict(arrowstyle="-", color=NOTE, lw=0.7))
    ax.set_xlim(0, 12.2)
    ax.set_ylim(-0.55, n)
    ax.axis("off")
    ax.set_title("The structure of a Java program", fontsize=11, fontweight="bold", color=INK)
    save(fig, "cs_ch11_fig02_structure.png")


def fig_features():
    table_fig(["Feature", "Meaning"],
              [["Simple", "easy to learn; no pointers; syntax like C++"],
               ["Object-oriented", "everything is written inside classes and objects"],
               ["Platform independent", "bytecode runs on any computer that has a JVM"],
               ["Portable (architecture-neutral)", "the same program runs unchanged on different machines"],
               ["Secure", "runs inside the JVM; no direct memory access"],
               ["Robust", "strong type checking, exception handling, automatic memory management"],
               ["Multithreaded", "can do several tasks at the same time"],
               ["Distributed", "programs can work across networks and the Internet"],
               ["Compiled and interpreted", "compiled to bytecode, then run by the JVM"]],
              "cs_ch11_fig03_features.png", col_w=[3.8, 8.2], title="Features of Java", size=9.0)


def fig_family():
    table_fig(["Name", "What it is"],
              [["Java application", "a stand-alone program run with the java command"],
               ["Applet", "a small Java program that ran inside a web page (now obsolete)"],
               ["J2SE / J2EE / J2ME", "Standard, Enterprise (web and business) and Micro (small devices) editions"],
               ["Servlet", "Java program on a web server that handles requests and builds replies"],
               ["JSP (Java Server Pages)", "used to create dynamic web pages"],
               ["JavaBean", "a reusable software component used to build bigger applications"],
               ["JDBC", "methods for querying and updating data in a database"],
               ["IDE", "editor + compiler + debugger in one: BlueJ, NetBeans, Eclipse, JCreator"]],
              "cs_ch11_fig04_family.png", col_w=[3.8, 8.6], title="Java programs, editions and technologies", size=9.0)


if __name__ == "__main__":
    fig_wora()
    fig_structure()
    fig_features()
    fig_family()
