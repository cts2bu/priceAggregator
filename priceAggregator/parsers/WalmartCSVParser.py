__author__ = 'Christopher'

from CSVParser import CSVParser
import csv

class WalmartCSVParser(CSVParser):

    def printCSV(self):
        csvfile = open('../spiders/walmartscrape.csv', "rb")
        reader = csv.reader(csvfile)
        reader.next() #skip the first title line
        for row in reader:
            mainPrice = ''
            mainPrice = row[0][:len(row[0]) - 1]
            if mainPrice == '':
                mainPrice = row[1][:len(row[1]) - 1]
            link = row[2]
            title = row[3]
            print title + ' ' + mainPrice + ' ' + link
