__author__ = 'Christopher'

from CSVParser import CSVParser
import csv

class eBayCSVParser(CSVParser):

    def printCSV(self):
        csvfile = open('../spiders/ebayscrape.csv', "rb")
        reader = csv.reader(csvfile)
        reader.next() #skip the first title line
        for row in reader:
            mainPrice = ''
            mainPrice = row[0]
            if mainPrice == '':
                mainPrice = row[1].strip()
            link = row[2]
            title = row[3]
            print title + ' ' + mainPrice + ' ' + link