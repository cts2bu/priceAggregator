__author__ = 'Christopher'

from AmazonCSVParser import AmazonCSVParser
from eBayCSVParser import eBayCSVParser

if __name__ == "__main__":
    AmazonCSVParser().printCSV()
    eBayCSVParser().printCSV()