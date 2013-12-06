__author__ = 'Christopher'

from AmazonCSVParser import AmazonCSVParser
from eBayCSVParser import eBayCSVParser
from WalmartCSVParser import WalmartCSVParser

if __name__ == "__main__":
    AmazonCSVParser().printCSV()
    print ""
    eBayCSVParser().printCSV()
    print ""
    WalmartCSVParser().printCSV()