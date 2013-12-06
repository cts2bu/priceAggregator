__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3
from gui import GUI

class walmart_gui(GUI):
    def __init__(self):
        self.con = sqlite3.connect("csv.db")
        self.c = self.con.cursor()
        self.con.text_factory = str
        self.c.execute("create table if not exists walmart (col1, col2, col3, col4)")
    def insert_into_table(self):
        csvfile = open("walmart.csv", 'rb')
        creader = csv.reader(csvfile)
        creader.next()
        for t in creader:
            self.c.execute("insert into walmart values (?, ?, ?, ?)", t)
    def display_GUI(self):
        root = Tk()
        root.wm_title("Table")
        l = Label(root, text = "price2, price, link, title")
        l.pack()
        self.c.execute("select col1 from walmart")
        col1_text = self.c.fetchall()
        self.c.execute("select col2 from walmart")
        col2_text = self.c.fetchall()
        self.c.execute("select col3 from walmart")
        col3_text = self.c.fetchall()
        self.c.execute("select col4 from walmart")
        col4_text = self.c.fetchall()
        i = 0
        while i < len(col1_text):
            a = Label(root, text = str(col1_text[i]) + str(col2_text[i]) + str(col3_text[i]) + str(col4_text[i]))
            a.pack()
            i += 1
        root.mainloop()