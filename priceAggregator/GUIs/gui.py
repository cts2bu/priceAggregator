from Tkinter import *
import webbrowser
import csv
import sqlite3
from priceAggregator.parsers.AmazonCSVParser import AmazonCSVParser
from priceAggregator.parsers.eBayCSVParser import eBayCSVParser
from priceAggregator.parsers.WalmartCSVParser import WalmartCSVParser


class GUI(Frame):
    def __init__(self, root, name):
        self.name = name
        self.con = sqlite3.connect(":memory:")
        self.c = self.con.cursor()
        self.con.text_factory = str
        self.c.execute("create table if not exists " + name + " (col1, col2, col3, col4)")

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.OnFrameConfigure)

        self.populate()

    def do_url(self, url):
        webbrowser.open(url)

    def populate(self):
        csvfile = open("../main/" + self.name + "scrape.csv", 'rb')
        creader = csv.reader(csvfile)
        creader.next()
        for t in creader:
            self.c.execute("insert into " + self.name + " values (?, ?, ?, ?)", t)

        i = 0

        parser = None

        if self.name == 'amazon':
            parser = AmazonCSVParser()
        elif self.name == 'ebay':
            parser = eBayCSVParser()
        else:
            parser = WalmartCSVParser()

        for row in self.c.execute("select * from " + self.name):
            url = parser.getLink(row)
            label = Label(self.frame, text = parser.printCSV(row), relief = "solid")
            label.bind("<Button-1>", lambda e, url=url:self.do_url(url))
            label.configure(foreground="blue", underline=True)
            label.grid(row=i, column=1)
            i = i + 1


    def OnFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))