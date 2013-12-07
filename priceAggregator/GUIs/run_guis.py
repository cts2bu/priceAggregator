__author__ = 'piammoradi'
from Tkinter import *
from AmazonGUI import AmazonGUI
from eBayGUI import eBayGUI
from WalmartGUI import WalmartGUI
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
        root = Tk()
        gui = AmazonGUI(root)
        gui.pack(side="top", fill="both", expand=True)
        root.mainloop()
    def show_ebay(self):
        root = Tk()
        gui = eBayGUI(root)
        gui.pack(side="top", fill="both", expand=True)
        root.mainloop()
    def show_walmart(self):
        root = Tk()
        gui = WalmartGUI(root)
        gui.pack(side="top", fill="both", expand=True)
        root.mainloop()
run_GUI().show_menu()