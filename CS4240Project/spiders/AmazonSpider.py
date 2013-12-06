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
       "http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=bath%20bedding&sprefix=bath+%2Caps&rh=i%3Aaps%2Ck%3Abath%20bedding"
   ]

   rules = (
        Rule (SgmlLinkExtractor(allow=("ref=sr_pg_*", ), restrict_xpaths=('//span[@class="pagnRA"]',))
    , callback="parse_items", follow= True),
    )

   def parse_items(self, response):

       sel = Selector(response)
       sites = sel.xpath('//div[starts-with(@id,"result")]')
       items = []
       for site in sites:
           item = AmazonItem()
           item['link'] = site.xpath('h3/a/@href').extract()
           item['price'] = site.xpath('ul/li[@class="med grey mkp2"]/a/span[@class="price bld"]/text()').extract()
           item['price2'] = site.xpath('ul/li[@class="newp"]/a/span[@class="bld lrg red"]/text()').extract()
           item['title'] = site.xpath('h3/a/span[@class="lrg bold"]/text()').extract()
           items.append(item)
       return items


if __name__ == "__main__":
    os.system('scrapy crawl amzn -o amazonscrape24.json -t json')


