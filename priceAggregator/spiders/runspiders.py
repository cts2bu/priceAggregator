import os


if __name__ == "__main__":
    os.system('scrapy crawl amzn -o amazonscrape.csv -t csv')
    os.system('scrapy crawl ebay -o ebayscrape.csv -t csv')
    os.system('scrapy crawl walmart -o walmartscrape.csv -t csv')