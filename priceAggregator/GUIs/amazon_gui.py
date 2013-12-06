__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3
from gui import GUI
from priceAggregator.parsers.AmazonCSVParser import AmazonCSVParser

class amazon_gui(GUI):
    def __init__(self):
        self.con = sqlite3.connect("csv.db")
        self.c = self.con.cursor()
        self.con.text_factory = str
        self.c.execute("create table if not exists amazon (col1, col2, col3, col4)")
    def insert_into_table(self):
        csvfile = open("../spiders/amazonscrape.csv", 'rb')
        creader = csv.reader(csvfile)
        creader.next()
        for t in creader:
            self.c.execute("insert into amazon values (?, ?, ?, ?)", t)
    def display_GUI(self):
        root = Tk()
        root.wm_title("Table")
        l = Label(root, text = "title, price, link")
        l.pack()
        for row in self.c.execute('select * from amazon'):
            a = Label(root, text = AmazonCSVParser().printCSV(row))
            a.pack()
        root.mainloop()

if __name__ == "__main__":
    gui = amazon_gui()
    gui.insert_into_table()
    gui.display_GUI()