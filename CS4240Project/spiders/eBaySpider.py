from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import os
from CS4240Project.items import eBayItem

class eBaySpider(CrawlSpider):
   name = "ebay"
   allowed_domains = ["ebay.com"]
   start_urls = [
       "http://www.ebay.com/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0.Xheritage+door+handle&_nkw=heritage+door+handle&_sacat=0&_from=R40"
   ]

   rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//td[@class="pages"]',))
    , callback="parse_items", follow= True),
    )

   def parse_items(self, response):
       sel = Selector(response)
       sites = sel.xpath('//tr[@itemprop="offers"]')
       items = []
       for site in sites:
           item = eBayItem()
           item['price'] = site.xpath('td[@class="prc"]/div/div[@class="g-b"]/text()').extract()
           item['price2'] = site.xpath('td[@class="prc"]/div[@class="g-b"]/text()').extract()
           item['link'] = site.xpath('td/div/h4/a/@href').extract()
           item['title'] = site.xpath('td/div/div/div/a/img/@alt').extract()
           items.append(item)
       return items

if __name__ == "__main__":
    os.system('scrapy crawl ebay -o ebay31.json -t json')
