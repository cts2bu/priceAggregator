__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3

con = sqlite3.connect("csv.db")
c = con.cursor()
con.text_factory = str
c.execute("create table if not exists t (col1, col2, col3, col4)")
def insert_into_table():
    # response = raw_input("Would you like to input items? ")
    # while response == 'yes' or raw_input == 'Yes':
    #     input_item = raw_input("Enter item name: ")
    #     input_price = raw_input("Enter item price: ")
    #     c.execute("insert into prices values (?, ?)", (input_item, input_price))
    #     response = raw_input("Would you like to input items? ")
    #     con.commit()
    csvfile = open('spiders/amazonscrape.csv', 'rb')
    creader = csv.reader(csvfile, delimiter=',')
    headers = creader.next()
    for t in creader:
        c.execute("insert into t values (?, ?, ?, ?)", t)

def display_GUI(col1_text, col2_text, col3_text, col4_text):
    root = Tk()
    root.wm_title("Table")
    l = Label(root, text = "Col1, Col2, Col3, Col4")
    l.pack()
    i = 0
    while i < len(col1_text):
        a = Label(root, text = str(col1_text[i]) + str(col2_text[i]) + str(col3_text[i]) + str(col4_text[i]))
        a.pack()
        i += 1
    root.mainloop()
    #print value_text[1]

insert_into_table()
c.execute("select col1 from t")
col1 = c.fetchall()
c.execute("select col2 from t")
col2 = c.fetchall()
c.execute("select col3 from t")
col3 = c.fetchall()
c.execute("select col4 from t")
col4 = c.fetchall()
display_GUI(col1, col2, col3, col4)


