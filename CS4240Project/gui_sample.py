__author__ = 'piammoradi'
from Tkinter import *
import sqlite3

con = sqlite3.connect("prices.db")
c = con.cursor()
c.execute("create table if not exists prices (item, price)")
pass
def insert_into_table():
    response = raw_input("Would you like to input items? ")
    while response == 'yes' or raw_input == 'Yes':
        input_item = raw_input("Enter item name: ")
        input_price = raw_input("Enter item price: ")
        c.execute("insert into prices values (?, ?)", (input_item, input_price))
        response = raw_input("Would you like to input items? ")
def display_GUI(value_text, price_text):
    root = Tk()
    root.wm_title("Table")
    l = Label(root, text = "Item, Price")
    l.pack()
    i = 0
    while i < len(value_text):
        a = Label(root, text = str(value_text[i]) + str(price_text[i]))
        a.pack()
        i += 1
    root.mainloop()
    #print value_text[1]

insert_into_table()
c.execute("select item from prices")
values = c.fetchall()
c.execute("select price from prices")
prices = c.fetchall()
#print str(values[0]) + str(values[1])
#
display_GUI(values, prices)


