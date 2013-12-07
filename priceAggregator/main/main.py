__author__ = 'piammoradi'
from priceAggregator.spiders.starturls import StartUrls
import os
#from priceAggregator.GUIs import run_guis

input_search = raw_input("Search for items: ")
urls = StartUrls(input_search)

print "Running amazon spider..."
os.system('scrapy crawl amzn -a start_url="' + urls.amazonurl + '" -o amazonscrape.csv -t csv --nolog')
print "Running ebay spider..."
os.system('scrapy crawl ebay -a start_url="' + urls.ebayurl + '" -o ebay.csv -t csv --nolog')
print "Running walmart spider..."
os.system('scrapy crawl walmart -a start_url="' + urls.walmarturl + '" -o walmart.csv -t csv --nolog')

#run_guis.run_GUI().show_menu()



