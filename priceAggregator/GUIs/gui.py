__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3
from priceAggregator import HyperlinkManager
import webbrowser
from priceAggregator.parsers.AmazonCSVParser import AmazonCSVParser
from priceAggregator.parsers.eBayCSVParser import eBayCSVParser
from priceAggregator.parsers.WalmartCSVParser import WalmartCSVParser

class GUI(object):
    def __init__(self, name):
        self.name = name
        self.con = sqlite3.connect(":memory:")
        self.c = self.con.cursor()
        self.con.text_factory = str
        self.c.execute("create table if not exists " + name + " (col1, col2, col3, col4)")

    def insert_into_table(self):
        csvfile = open("../spiders/" + self.name + "scrape.csv", 'rb')
        creader = csv.reader(csvfile)
        creader.next()
        for t in creader:
            self.c.execute("insert into " + self.name + " values (?, ?, ?, ?)", t)

    def do_url(self, url):
        webbrowser.open(url)

    def display_GUI(self):
        root = Tk()
        root.wm_title("Table")

        for row in self.c.execute("select * from " + self.name):
            if self.name == 'amazon':
                url = AmazonCSVParser().getLink(row)
                label = Label(root, text=AmazonCSVParser().printCSV(row))
                label.configure(foreground="blue")
                label.bind("<Button-1>",lambda e,url=url:self.do_url(url))
                label.pack()

            elif self.name == 'ebay':
                url = eBayCSVParser().getLink(row)
                label = Label(root, text=eBayCSVParser().printCSV(row))
                label.configure(foreground="blue")
                label.bind("<Button-1>",lambda e,url=url:self.do_url(url))
                label.pack()

            else:
                url = "http://www.walmart.com" + WalmartCSVParser().getLink(row)
                label = Label(root, text=WalmartCSVParser().printCSV(row))
                label.configure(foreground="blue")
                label.bind("<Button-1>",lambda e,url=url:self.do_url(url))
                label.pack()

        root.mainloop()