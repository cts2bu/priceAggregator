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
       "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=bath+bedding&rh=i%3Aaps%2Ck%3Abath+bedding"
   ]

   rules = (
        Rule (SgmlLinkExtractor(allow=("ref=sr_pg_*", ), restrict_xpaths=('//span[@class="pagnRA"]',))
    , callback="parse_items", follow= True),
    )

   def parse_items(self, response):
       sel = Selector(response)
       sites = sel.xpath('//ul/li[@class="newp"]')
       sites2 = sel.xpath('//h3')
       #print sites2
       items = []
       print sites2.xpath('a/span[@class="lrg bold"]/text()').extract()
       for site in sites:
           item = AmazonItem()
           item['link'] = site.xpath('a/@href').extract()
           item['price'] = site.xpath('a/span/text()').extract()
           items.append(item)
       return items


if __name__ == "__main__":
    #os.system('scrapy crawl amzn -o amazonscrape.json -t json')
    os.system('scrapy crawl amzn -o amazonscrape.json -t json --nolog')

