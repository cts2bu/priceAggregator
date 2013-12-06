__author__ = 'piammoradi'
from Tkinter import *
from amazon_gui import amazon_gui
from ebay_gui import ebay_gui
from walmart_gui import walmart_gui
class run_GUI():
    def show_menu(self):
        root = Tk()
        root.wm_title("Menu")
        root.minsize(200, 75)
        a = Button(root, text = "Amazon", command = lambda: self.show_amazon())
        a.pack()
        b = Button(root, text = "eBay", command = lambda: self.show_ebay())
        b.pack()
        c = Button(root, text = "WalMart", command = lambda: self.show_walmart())
        c.pack()
        root.mainloop()
    def show_amazon(self):
        amazon = amazon_gui()
        amazon.insert_into_table()
        amazon.display_GUI()
    def show_ebay(self):
        ebay = ebay_gui()
        ebay.insert_into_table()
        ebay.display_GUI()
    def show_walmart(self):
        walmart = walmart_gui()
        walmart.insert_into_table()
        walmart.display_GUI()
run_GUI().show_menu()