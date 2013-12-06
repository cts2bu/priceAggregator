__author__ = 'Chris'

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import os
from CS4240Project.items import AmazonItem

class AmazonSpider(CrawlSpider):
   name = "amzn"
   allowed_domains = ["amazon.com"]
   start_urls = [
       "http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=bath%20bedding&sprefix=bath+bedd%2Caps&rh=i%3Aaps%2Ck%3Abath%20bedding"
   ]

   rules = (
        Rule (SgmlLinkExtractor(allow=("ref=sr_pg_*", ), restrict_xpaths=('//span[@class="pagnRA"]',))
    , callback="parse_items", follow= True),
    )

   def parse_items(self, response):
       sel = Selector(response)
       #sites = sel.xpath('//div[@class="btfResults"]')
       items = []
       #for site in sites:
       item = AmazonItem()
           #item['title'] = site.xpath('div[@class="shortDescription"]/a/text()').extract()
       item['title'] = sel.xpath('//*[@class="result_0"]/h3/a/span/text()').extract()
           #item['link'] = site.xpath('a/@href').extract()
           #item['saleprice'] = site.xpath('div[@class="prices"]/span[@class="priceSale"]/text()').extract()
           #item['origprice'] = site.xpath('div[@class="prices"]/span[not(contains(@class, "priceSale"))]/text()').extract()
       items.append(item)
       return items

if __name__ == "__main__":
    os.system('scrapy crawl amzn -o amazonscrape.json -t json')

