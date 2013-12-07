__author__ = 'piammoradi'

from gui import GUI
from Tkinter import Tk

class WalmartGUI(GUI):
    def __init__(self, root):
        root.wm_title("Walmart Table")
        sizex = 800
        sizey = 600
        posx  = 100
        posy  = 100
        root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
        GUI.__init__(self, root, "walmart")

if __name__ == "__main__":
    root = Tk()
    gui = WalmartGUI(root)
    gui.pack(side="top", fill="both", expand=True)
    root.mainloop()