__author__ = 'piammoradi'

from gui import GUI

class walmart_gui(GUI):
    def __init__(self):
        GUI.__init__(self, "walmart")

if __name__ == "__main__":
    gui = walmart_gui()
    gui.insert_into_table()
    gui.display_GUI()