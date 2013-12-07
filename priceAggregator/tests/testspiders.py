import unittest
import os
import csv
from priceAggregator.spiders.starturls import StartUrls


#This tests spider crawling methods, particularly in relation to start-url activity generation.
class TestSpiders(unittest.TestCase):
    #Cleanup -> get rid of old test csv file per test pass
    def setUp(self):
        try:
            os.remove("testscrape.csv")
        except OSError:
            pass

    #Make sure the spider (Let's say amazon) fails on a bad url
    def test_spider_badurl(self):
        self.assertEquals(os.system('scrapy crawl amzn -a start_url="blah" --nolog'), 0)

    #Make sure you can get an element from a .csv file on a scrape from a given search term (Amazon)
    def test_create_amazoncsv(self):
        searchterm = "Tristram Shandy"
        os.system(
            'scrapy crawl amzn -a start_url="' + StartUrls(searchterm).amazonurl + '" -o testscrape.csv -t csv --nolog')
        reader = csv.reader("testscrape.csv")
        for row in reader:
            self.assertIsInstance(row[0], str)

    #Make sure you can get an element from a .csv file on a scrape from a given search term (eBay)
    def test_create_eBaycsv(self):
        searchterm = "In Memoriam A.H.H."
        os.system(
            'scrapy crawl ebay -a start_url="' + StartUrls(searchterm).ebayurl + '" -o testscrape.csv -t csv --nolog')
        reader = csv.reader("testscrape.csv")
        for row in reader:
            self.assertIsInstance(row[0], str)

    #Make sure you can get an element from a .csv file on a scrape from a given search term
    def test_create_walmartcsv(self):
        searchterm = "Eugene Onegin"
        os.system('scrapy crawl walmart -a start_url="' + StartUrls(
            searchterm).walmarturl + '" -o testscrape.csv -t csv --nolog')
        reader = csv.reader("testscrape.csv")
        for row in reader:
            self.assertIsInstance(row[0], str)


if __name__ == '__main__':
    unittest.main()