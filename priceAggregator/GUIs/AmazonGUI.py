__author__ = 'piammoradi'

from gui import GUI
from Tkinter import Tk

class AmazonGUI(GUI):
    def __init__(self, root):
        root.wm_title("Amazon Table")
        sizex = 800
        sizey = 600
        posx  = 100
        posy  = 100
        root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
        GUI.__init__(self, root, "amazon")

if __name__ == "__main__":
    root = Tk()
    gui = AmazonGUI(root)
    gui.pack(side="top", fill="both", expand=True)
    root.mainloop()