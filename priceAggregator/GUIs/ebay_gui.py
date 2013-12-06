__author__ = 'piammoradi'

from gui import GUI

class ebay_gui(GUI):
    def __init__(self):
        GUI.__init__(self, "ebay")

if __name__ == "__main__":
    gui = ebay_gui()
    gui.insert_into_table()
    gui.display_GUI()