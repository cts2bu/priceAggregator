__author__ = 'Christopher'

from abc import abstractmethod, ABCMeta

class CSVParser():
    __metaclass__ = ABCMeta

    @abstractmethod
    def printCSV(self, row):
        print "This won't ever be called"

    def getLink(self, row):
        if row[2] != "link":
            return row[2]