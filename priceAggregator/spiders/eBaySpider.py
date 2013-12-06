from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import os
from priceAggregator.items import eBayItem
from priceAggregator.starturls import StartUrls

class eBaySpider(CrawlSpider):
   name = "ebay"
   allowed_domains = ["ebay.com"]
   start_urls = StartUrls.ebayurls

   rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//td[@class="pages"]',))
    , callback="parse_start_url", follow= True),
    )

   def parse_start_url(self, response):
        return self.parse_items(response)

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
    os.system('scrapy crawl ebay -o ebay39.json -t json --nolog')
