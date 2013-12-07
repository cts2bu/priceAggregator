__author__ = 'piammoradi'
from Tkinter import *
from priceAggregator.GUIs.AmazonGUI import AmazonGUI
from priceAggregator.GUIs.eBayGUI import eBayGUI
from priceAggregator.GUIs.WalmartGUI import WalmartGUI
from priceAggregator.spiders.runspiders import RunSpiders

class MainMenu():
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
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)
        e = Entry(root)
        e.pack()
        e.focus_set()
        b = Button(root, text = "Search", command =lambda: RunSpiders(e.get()).run_spiders())
        b.pack()
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

if __name__ == "__main__":
    MainMenu().show_menu()