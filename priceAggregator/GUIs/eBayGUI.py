__author__ = 'piammoradi'

from gui import GUI
from Tkinter import Tk

class eBayGUI(GUI):
    def __init__(self, root):
        root.wm_title("eBay Table")
        sizex = 800
        sizey = 600
        posx  = 100
        posy  = 100
        root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
        GUI.__init__(self, root, "ebay")

if __name__ == "__main__":
    root = Tk()
    gui = eBayGUI(root)
    gui.pack(side="top", fill="both", expand=True)
    root.mainloop()