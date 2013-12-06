__author__ = 'Chris'

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from priceAggregator.items import AmazonItem
from priceAggregator.starturls import StartUrls

class AmazonSpider(CrawlSpider):
   name = "amzn"
   allowed_domains = ["amazon.com"]
   start_urls = StartUrls.amazonurls

   rules = (
        Rule (SgmlLinkExtractor(allow=("ref=sr_pg_[2-7]\?*", ), restrict_xpaths=('//span[@class="pagnRA"]',))
    , callback="parse_start_url", follow= True),
    )

   def parse_start_url(self, response):
        return self.parse_items(response)

   def parse_items(self, response):
       sel = Selector(response)
       sites = sel.xpath('//div[starts-with(@id,"result_")]')
       items = []
       for site in sites:
           item = AmazonItem()
           item['link'] = site.xpath('h3/a/@href').extract()
           item['price'] = site.xpath('ul/li[@class="med grey mkp2"]/a/span[@class="price bld"]/text()').extract()
           item['price2'] = site.xpath('ul/li[@class="newp"]/a/span[@class="bld lrg red"]/text()').extract()
           item['title'] = site.xpath('h3/a/span[@class="lrg bold"]/text()').extract()
           if item['price'] or item['price2']: #pre-filter items with no prices
                items.append(item)
       return items



