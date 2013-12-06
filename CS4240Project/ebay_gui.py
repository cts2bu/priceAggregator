__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3

con = sqlite3.connect("ebay.db")
c = con.cursor()
con.text_factory = str
c.execute("create table if not exists ebay (col1, col2, col3, col4)")

def insert_into_table():
    csvfile = open('spiders/ebay.csv', 'rb')
    creader = csv.reader(csvfile, delimiter=',')
    headers = creader.next()
    for t in creader:
        c.execute("insert into ebay values (?, ?, ?, ?)", t)

def display_GUI(col1_text, col2_text, col3_text, col4_text):
    root = Tk()
    root.wm_title("Table")
    l = Label(root, text = "price, price2, link, title")
    l.pack()
    i = 0
    while i < len(col1_text):
        a = Label(root, text = str(col1_text[i]) + str(col2_text[i]) + str(col3_text[i]) + str(col4_text[i]))
        a.pack()
        i += 1
    root.mainloop()

insert_into_table()
c.execute("select col1 from ebay")
col1 = c.fetchall()
c.execute("select col2 from ebay")
col2 = c.fetchall()
c.execute("select col3 from ebay")
col3 = c.fetchall()
c.execute("select col4 from ebay")
col4 = c.fetchall()
display_GUI(col1, col2, col3, col4)