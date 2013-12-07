__author__ = 'piammoradi'
from priceAggregator.spiders.starturls import StartUrls
import os
from Tkinter import *
#from priceAggregator.GUIs import run_guis

class Main():
    def __init__(self):
        self.urls = StartUrls("")
    def display(self):
        root = Tk()
        root.wm_title("Search")
        e = Entry(root)
        e.pack()
        e.focus_set()
        b = Button(root, text = "Search", command =lambda: self.run_spiders())
        b.pack()
        root.mainloop()
        self.urls = StartUrls(e.get())
    def run_spiders(self):
        print "Running amazon spider..."
        os.system('scrapy crawl amzn -a start_url="' + self.urls.amazonurl + '" -o amazonscrape.csv -t csv --nolog')
        print "Running ebay spider..."
        os.system('scrapy crawl ebay -a start_url="' + self.urls.ebayurl + '" -o ebay.csv -t csv --nolog')
        print "Running walmart spider..."
        os.system('scrapy crawl walmart -a start_url="' + self.urls.walmarturl + '" -o walmart.csv -t csv --nolog')
new_main = Main()
new_main.display()




#run_guis.run_GUI().show_menu()



