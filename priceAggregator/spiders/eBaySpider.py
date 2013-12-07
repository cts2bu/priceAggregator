from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from priceAggregator.items import eBayItem
from priceAggregator.spiders.starturls import StartUrls

class eBaySpider(CrawlSpider):
   name = "ebay"
   allowed_domains = ["ebay.com"]
   rules = (
        Rule (SgmlLinkExtractor(allow=("_pgn=[2-2]\&*", ), restrict_xpaths=('//td[@class="pages"]',))
    , callback="parse_start_url", follow= True),
    )

   def __init__(self, *a, **kw):
        super(eBaySpider, self).__init__(*a, **kw)
        self.start_urls = [kw.get('start_url')]

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
           if item['price'] or item['price2']: #pre-filter items with no prices
                items.append(item)
       return items
