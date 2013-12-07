import os
from priceAggregator.spiders.starturls import StartUrls

class RunSpiders():
    def __init__(self, url):
        self.urls = StartUrls(url)

    def run_spiders(self):
        try:
            os.remove("amazonscrape.csv")
            os.remove("ebayscrape.csv")
            os.remove("walmartscrape.csv")
        except OSError:
            pass

        print "Running amazon spider..."
        os.system('scrapy crawl amzn -a start_url="' + self.urls.amazonurl + '" -o amazonscrape.csv -t csv --nolog')
        print "Running ebay spider..."
        os.system('scrapy crawl ebay -a start_url="' + self.urls.ebayurl + '" -o ebayscrape.csv -t csv --nolog')
        print "Running walmart spider..."
        os.system('scrapy crawl walmart -a start_url="' + self.urls.walmarturl + '" -o walmartscrape.csv -t csv --nolog')