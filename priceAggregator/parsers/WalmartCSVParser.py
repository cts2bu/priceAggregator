__author__ = 'Christopher'

from CSVParser import CSVParser
import csv

class WalmartCSVParser(CSVParser):

    def printCSV(self, row):
        mainPrice = ''
        mainPrice = row[0][:len(row[0]) - 1]
        if mainPrice == '':
            mainPrice = row[1][:len(row[1]) - 1]
        title = row[3]
        return title + ' ' + mainPrice
