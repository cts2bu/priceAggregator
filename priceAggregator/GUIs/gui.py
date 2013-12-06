__author__ = 'piammoradi'
from Tkinter import *
import csv, sqlite3
from abc import ABCMeta
from abc import abstractmethod

class GUI():
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def insert_into_table(self):
        pass
    @abstractmethod
    def display_GUI(self):
        pass







# if __name__ == '__main__':
#     ebay = ebay_gui()
#     ebay.insert_into_table()
#     ebay.display_GUI()