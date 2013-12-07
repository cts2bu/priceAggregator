__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3
from abc import ABCMeta
from priceAggregator.parsers.AmazonCSVParser import AmazonCSVParser
from priceAggregator.parsers.eBayCSVParser import eBayCSVParser
from priceAggregator.parsers.WalmartCSVParser import WalmartCSVParser
import tkHyperlinkManager
import webbrowser

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

    def display_GUI(self):
        root = Tk()
        root.title("hyperlink-1")

        text = Text(root)
        text.pack()

        hyperlink = tkHyperlinkManager.HyperlinkManager(text)

        getrow = []

        i = 0
        links = []

        for row in self.c.execute("select * from " + self.name):

            getrow = AmazonCSVParser().printCSV(row)
            links.append(getrow[2])

            def click1(j):
                webbrowser.open_new(links[j])

            if self.name == 'amazon':
                text.insert(INSERT, getrow[0], hyperlink.add(click1(i)))
                text.insert(INSERT, "\t\t")
                text.insert(INSERT, getrow[1])
                text.insert(INSERT, "\n\n")

            i = i + 1

        mainloop()