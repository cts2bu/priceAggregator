__author__ = 'piammoradi'
from priceAggregator.spiders.starturls import StartUrls
import os
from Tkinter import *
from priceAggregator.GUIs.run_guis import run_GUI

class Main():
    def __init__(self):
        self.urls = StartUrls("")

    def setUp(self):
        try:
            os.remove("amazonscrape.csv")
            os.remove("ebayscrape.csv")
            os.remove("walmartscrape.csv")
        except OSError:
            pass

    def display(self):
        root = Tk()
        root.wm_title("Search")
        e = Entry(root)
        e.pack()
        e.focus_set()
        print e.get()
        b = Button(root, text = "Search", command =lambda: self.run_spiders(e.get()))
        b.pack()
        root.mainloop()

    def run_spiders(self, urlText):
        self.urls = StartUrls(urlText)
        print "Running amazon spider..."
        os.system('scrapy crawl amzn -a start_url="' + self.urls.amazonurl + '" -o amazonscrape.csv -t csv --nolog')
        print "Running ebay spider..."
        os.system('scrapy crawl ebay -a start_url="' + self.urls.ebayurl + '" -o ebayscrape.csv -t csv --nolog')
        print "Running walmart spider..."
        os.system('scrapy crawl walmart -a start_url="' + self.urls.walmarturl + '" -o walmartscrape.csv -t csv --nolog')
        run_GUI().show_menu()

if __name__ == "__main__":
    new_main = Main()
    new_main.setUp()
    new_main.display()



