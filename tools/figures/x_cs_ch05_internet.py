"""Figures for Class X Computer Science, Ch05: Internet Basics."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from x_cs_common import flow, table_fig, tree


def fig_connect():
    flow(["Your computer\nwith a web\nbrowser", "Modem\n(digital ↔\nanalogue)", "ISP\n(account with\nuser ID, password)",
          "Internet\n(network of\nnetworks)", "Web server\n(stores and sends\nweb pages)"],
         "cs_ch05_fig01_connect.png", width=10.5, w=1.95, h=1.25, size=8.4,
         title="How a computer connects to the Internet")


def fig_url():
    table_fig(["Part of the URL", "Example", "Meaning"],
              [["Protocol", "https://", "the rules used to fetch the page"],
               ["Domain name (host)", "www.mbose.in", "the web server's name; .in = India"],
               ["Path", "/notice/", "the folder on the server"],
               ["File name", "result.html", "the page (resource) itself"]],
              "cs_ch05_fig02_url.png", col_w=[3.0, 4.6, 4.6],
              title="The parts of the URL  https://www.mbose.in/notice/result.html", size=8.4)


def fig_connections():
    tree("Types of Internet connection",
         ["Wired", "Wireless"],
         "cs_ch05_fig03_connections.png",
         grand={0: ["dial-up (telephone line)", "DSL / broadband", "cable", "leased line", "optical fibre"],
                1: ["Wi-Fi", "mobile data (4G, 5G)", "satellite", "microwave", "radio frequency (Wi-Max)"]},
         width=9.0, child_w=3.4, size=8.8)


if __name__ == "__main__":
    fig_connect()
    fig_url()
    fig_connections()
