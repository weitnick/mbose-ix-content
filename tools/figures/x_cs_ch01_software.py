"""Figures for Class X Computer Science, Ch01: Software and Operating Systems."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import table_fig, tree


def fig_software():
    tree("Software",
         ["System software", "Application software"],
         "cs_ch01_fig01_software.png",
         grand={0: ["operating system", "language translators", "utility programs", "device drivers"],
                1: ["general purpose: word processor, spreadsheet", "presentation, database, DTP, multimedia",
                    "specific purpose: payroll, billing", "attendance, reservation, HR management"]},
         width=10.0, child_w=3.8, size=8.6)


def fig_os_functions():
    tree("Functions of an operating system",
         ["Process\nmanagement", "Memory\nmanagement", "File\nmanagement", "Device\nmanagement", "Security", "User\ninterface"],
         "cs_ch01_fig02_os_functions.png",
         grand={0: ["schedules programs"],
                1: ["allocates memory"],
                2: ["organises files"],
                3: ["controls I/O devices"],
                4: ["passwords, rights"],
                5: ["CUI or GUI"]},
         width=11.5, child_w=1.75, size=7.9)


def fig_os_types():
    table_fig(["Type of operating system", "What it does", "Example"],
              [["Batch processing", "runs jobs in batches without user interaction; uses spooling", "early mainframe systems"],
               ["Multi-user", "many users share one computer at the same time", "UNIX"],
               ["Multitasking / time-sharing", "runs several programs at once by sharing CPU time", "Windows, Linux"],
               ["Real-time", "dedicated system that processes tasks immediately", "air-traffic control, ABS brakes"],
               ["Network", "manages files, printers and users on a network", "Windows Server, Novell NetWare"],
               ["Single-user, single-task", "one user, one program at a time", "MS-DOS"]],
              "cs_ch01_fig03_os_types.png", col_w=[3.2, 6.0, 3.4],
              title="Types of operating systems", size=8.0)


if __name__ == "__main__":
    fig_software()
    fig_os_functions()
    fig_os_types()
