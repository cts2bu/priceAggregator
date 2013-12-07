__author__ = 'piammoradi'
from priceAggregator.spiders.starturls import StartUrls

input_search = raw_input("Search for items: ")
urls = StartUrls(input_search)