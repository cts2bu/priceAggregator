from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import os
from CS4240Project.items import MacysItem

class MacysSpider(CrawlSpider):
   name = "sstuff"
   allowed_domains = ["macys.com"]
   start_urls = [
       "http://www1.macys.com/shop/search?keyword=bedding+collections"
   ]

   rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//div[@id="paginateBottom"]',))
    , callback="parse_items", follow= True),
    )

   def parse_items(self, response):
       sel = Selector(response)
       sites = sel.xpath('//div')
       items = []
       for site in sites:
           item = MacysItem()
           item['title'] = site.xpath('span/text()').extract()
           items.append(item)
       return items

if __name__ == "__main__":
    os.system('scrapy crawl sstuff -o macyscrape15.json -t json')

