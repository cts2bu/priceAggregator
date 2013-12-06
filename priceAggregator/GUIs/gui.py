__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3
from abc import ABCMeta
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

    def display_GUI(self):
        root = Tk()
        root.wm_title("Table")
        l = Label(root, text = "title, price, link")
        l.pack()

        frame = Frame(root, bd=2, relief=SUNKEN)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(frame, bd=0, yscrollcommand=scrollbar.set)
        listbox.config(width = 225, height = 200)
        listbox.pack()

        scrollbar.config(command=listbox.yview)
        frame.pack()

        text = Text(root)
        text.pack()


        #hyperlink = HyperlinkManager(listbox)

        for row in self.c.execute("select * from " + self.name):
            if self.name == 'amazon':
                listbox.insert(END, AmazonCSVParser().printCSV(row))

            elif self.name == 'ebay':
                a = Label(root, text=eBayCSVParser().printCSV(row))
                a.pack()
                separator = Frame(height=2, bd=1, relief=SUNKEN)
                separator.pack(fill=X, padx=5, pady=5)

            else:
                a = Label(root, text=WalmartCSVParser().printCSV(row))
                a.pack()
        root.mainloop()


# if __name__ == '__main__':
#     ebay = ebay_gui()
#     ebay.insert_into_table()
#     ebay.display_GUI()