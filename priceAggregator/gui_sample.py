__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3, json
from abc import ABCMeta

con = sqlite3.connect("csv.db")
c = con.cursor()
#con.text_factory = str
c.execute("create table if not exists ebay (col1, col2)")

class GUI():
    __metaclass__ = ABCMeta
    def __init__(self):
        self.con = sqlite3.connect("csv.db")
        self.c = self.con.cursor()
        self.c.execute("create table if not exists ebay(col1, col2)")
    def insert_into_table(self):
        csvfile = open("ebay.csv", 'rb')
        creader = csv.reader(csvfile)
        creader.next()
        for t in creader:
            self.c.execute("insert into ebay values (?, ?)", t)
    def display_GUI(self):
        root = Tk()
        root.wm_title("Table")
        l = Label(root, text = "price, title")
        l.pack()
        self.c.execute("select col1 from ebay")
        col1_text = self.c.fetchall()
        self.c.execute("select col2 from ebay")
        col2_text = self.c.fetchall()
        i = 0
        while i < len(col1_text):
            a = Label(root, text = str(col1_text[i]) + str(col2_text[i]))
            a.pack()
            i += 1
        root.mainloop()


def insert_into_table():
    csvfile = open('ebay.csv', 'rb')
    creader = csv.reader(csvfile)
    creader.next()
    for t in creader:
        c.execute("insert into ebay values (?, ?)", t)

    # new_data = []
    # with open("macys_crawl.json") as f:
    #     for line in f:
    #         new_data.append(json.loads(line))

def display_GUI(col1_text, col2_text):
    root = Tk()
    root.wm_title("Table")
    l = Label(root, text = "price, title")
    l.pack()
    i = 0
    while i < len(col1_text):
        a = Label(root, text = str(col1_text[i]) + str(col2_text[i]))
        a.pack()
        i += 1
    root.mainloop()

insert_into_table()
c.execute("select col1 from ebay")
col1 = c.fetchall()
c.execute("select col2 from ebay")
col2 = c.fetchall()
# c.execute("select col3 from e")
# col3 = c.fetchall()
display_GUI(col1, col2)


