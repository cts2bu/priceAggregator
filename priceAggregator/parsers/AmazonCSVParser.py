__author__ = 'Christopher'

import csv

def printCSV():
        csvfile = open('../spiders/amazonscrape.csv', "rb")
        reader = csv.reader(csvfile)
        reader.next() #skip the first title line
        for row in reader:
            mainPrice = ''
            mainPrice = row[1].split(',')[0]
            if mainPrice == '':
                mainPrice = row[0][1:]
            link = row[2]
            title = row[3]
            print title + ' ' + mainPrice + ' ' + link


if __name__ == "__main__":
    printCSV()

