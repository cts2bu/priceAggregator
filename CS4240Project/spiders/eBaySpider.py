from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from CS4240Project.items import eBayItem

class eBaySpider(BaseSpider):
   name = "ebay"
   allowed_domains = ["macys.com"]
   start_urls = [
       "http://www1.macys.com/shop/product/hotel-collection-modern-trellis-bedding-collection?ID=1121718&CategoryID=7502"
   ]

   def parse(self, response):
       sel = Selector(response)
       sites = sel.xpath('//ul/li')
       items = []
       for site in sites:
           item = eBayItem()
           item['title'] = site.xpath('//h1/text()').extract()
           items.append(item)
       return items
