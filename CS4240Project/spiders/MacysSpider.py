from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector

from CS4240Project.items import MacysItem

class MacysSpider(CrawlSpider):
   name = "macys"
   allowed_domains = ["macys.com"]
   start_urls = [
       "http://www1.macys.com/shop/bed-bath/bedding-collections?id=7502"
   ]

   def parse(self, response):
       sel = Selector(response)
       sites = sel.xpath('//div/div[@class="shortDescription"]')
       items = []
       for site in sites:
           item = MacysItem()
           item['title'] = site.xpath('a/text()').extract()
           items.append(item)
       return items