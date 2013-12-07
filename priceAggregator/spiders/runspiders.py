import os
from priceAggregator.spiders.starturls import StartUrls

if __name__ == "__main__":
    input = raw_input("Please enter a search term. ")
    url = StartUrls(input)
    print "Running amazon spider..."
    os.system('scrapy crawl amzn -a start_url="' + url.amazonurl + '" -o amazonscrape.csv -t csv --nolog')
    print "Running ebay spider..."
    os.system('scrapy crawl ebay -a start_url="' + url.ebayurl + '" -o ebayscrape.csv -t csv --nolog')
    print "Running walmart spider..."
    os.system('scrapy crawl walmart -a start_url="' + url.walmarturl + '" -o walmartscrape.csv -t csv --nolog')