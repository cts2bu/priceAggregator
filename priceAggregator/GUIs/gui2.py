__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3
import webbrowser
import tkHyperlinkManager
from priceAggregator.parsers.AmazonCSVParser import AmazonCSVParser
from priceAggregator.parsers.eBayCSVParser import eBayCSVParser
from priceAggregator.parsers.WalmartCSVParser import WalmartCSVParser


class GUI(object):
    def __init__(self, name):
        self.name = name
        self.con = sqlite3.connect(":memory:")
        self.c = self.con.cursor()
        self.con.text_factory = str
        self.c.execute("create table if not exists " + name + " (col1, col2, col3, col4)")

    def insert_into_table(self):
        csvfile = open("../spiders/" + self.name + "scrape.csv", 'rb')
        creader = csv.reader(csvfile)
        creader.next()
        for t in creader:
            self.c.execute("insert into " + self.name + " values (?, ?, ?, ?)", t)

    def do_url(self, url):
        webbrowser.open(url)

    def display_GUI(self):

        root = Tk()
        #root.wm_title("Table")
        '''
        sizex = 800
        sizey = 600
        posx  = 100
        posy  = 100
        root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

        myframe=Frame(root,relief=GROOVE,width=750,height=500,bd=1)
        myframe.place(x=10,y=10)

        canvas=Canvas(myframe, width = 750, height = 500)
        frame=Frame(canvas, width = 750, height = 500)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",canvas.configure(scrollregion=canvas.bbox("all"),width=750,height=500))
        '''

        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(root)
        listbox.config(width = 500, height = 500)
        listbox.pack()


        for row in self.c.execute("select * from " + self.name):
            if self.name == 'amazon':
                '''
                url = AmazonCSVParser().getLink(row)
                Label(frame, text=i).grid(row=i, column=0)
                l = Label(frame, text=AmazonCSVParser().printCSV(row))
                l.bind("<Button-1>", lambda e, url=url:self.do_url(url))
                l.configure(foreground="blue")
                l.grid(row=i, column=1)
                i = i + 1
                '''

                url = AmazonCSVParser().getLink(row)
                l = Label(root, text=AmazonCSVParser().printCSV(row))
                l.bind("<Button-1>", lambda e, url=url:self.do_url(url))
                l.configure(foreground="blue")
                listbox.insert(END, l)

            elif self.name == 'ebay':
                url = eBayCSVParser().getLink(row)
                label = Label(root, text=eBayCSVParser().printCSV(row))
                label.configure(foreground="blue")
                label.bind("<Button-1>",lambda e,url=url:self.do_url(url))
                #label.pack()

            else:
                url = "http://www.walmart.com" + WalmartCSVParser().getLink(row)
                label = Label(root, text=WalmartCSVParser().printCSV(row))
                label.configure(foreground="blue")
                label.bind("<Button-1>",lambda e,url=url:self.do_url(url))
                #label.pack()

        # attach listbox to scrollbar
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)


        root.mainloop()