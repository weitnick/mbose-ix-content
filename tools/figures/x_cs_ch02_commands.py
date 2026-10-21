"""Figures for Class X Computer Science, Ch02: DOS and Linux Commands."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import table_fig, tree


def fig_dir_tree():
    tree("C:\\  (root directory)",
         ["SCHOOL", "GAMES", "TEMP"],
         "cs_ch02_fig01_dir_tree.png",
         grand={0: ["CLASSX (subdirectory)", "NOTES.TXT", "MARKS.XLS"],
                1: ["CHESS.EXE"],
                2: ["PHOTO1.JPG", "PHOTO2.JPG"]},
         width=9.0, child_w=2.6, size=8.8)


def fig_dos_types():
    tree("MS-DOS commands",
         ["Internal commands\n(inside COMMAND.COM;\nalways in memory)", "External commands\n(separate program files\non the disk)"],
         "cs_ch02_fig02_dos_types.png",
         grand={0: ["DIR, CD, MD, RD", "COPY, DEL, REN, TYPE", "CLS, DATE, TIME, VER"],
                1: ["FORMAT, DISKCOPY, DISKCOMP", "CHKDSK, ATTRIB, EDIT", "XCOPY, TREE, DOSKEY"]},
         width=9.5, child_w=3.6, size=8.6)


def fig_equivalents():
    table_fig(["Task", "MS-DOS command", "Linux command"],
              [["List files", "DIR", "ls"],
               ["Show current directory", "CD (alone)", "pwd"],
               ["Change directory", "CD name", "cd name"],
               ["Make a directory", "MD name", "mkdir name"],
               ["Remove an empty directory", "RD name", "rmdir name"],
               ["Copy a file", "COPY a b", "cp a b"],
               ["Move or rename a file", "MOVE / REN", "mv"],
               ["Delete a file", "DEL name", "rm name"],
               ["Show a file's contents", "TYPE name", "cat name"],
               ["Clear the screen", "CLS", "clear"],
               ["Edit a text file", "EDIT name", "nano name"],
               ["Get help on a command", "HELP cmd  or  cmd /?", "man cmd"]],
              "cs_ch02_fig03_equivalents.png", col_w=[4.2, 3.6, 3.6],
              title="The same jobs in MS-DOS and Linux", size=8.2)


if __name__ == "__main__":
    fig_dir_tree()
    fig_dos_types()
    fig_equivalents()
