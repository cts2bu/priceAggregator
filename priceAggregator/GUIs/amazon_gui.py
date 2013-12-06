__author__ = 'piammoradi'

from gui import GUI

class amazon_gui(GUI):
    def __init__(self):
        GUI.__init__(self, "amazon")

if __name__ == "__main__":
    gui = amazon_gui()
    gui.insert_into_table()
    gui.display_GUI()