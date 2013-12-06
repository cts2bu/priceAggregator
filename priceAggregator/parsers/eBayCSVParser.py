__author__ = 'Christopher'

from CSVParser import CSVParser
import csv

class eBayCSVParser(CSVParser):

    def printCSV(self, row):
        mainPrice = ''
        mainPrice = row[0]
        if mainPrice == '':
            mainPrice = row[1].strip()
        link = row[2]
        title = row[3]
        return title + ' ' + mainPrice + ' ' + link