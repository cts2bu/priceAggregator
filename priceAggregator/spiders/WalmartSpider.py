from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from priceAggregator.items import WalmartItem

class WalmartSpider(CrawlSpider):
   name = "walmart"
   allowed_domains = ["walmart.com"]
   rules = (
        Rule (SgmlLinkExtractor(allow=("ic=16_[0-128]\&*", ), restrict_xpaths=('//div/div[@id="bottomPagination"]/ul/li',))
    , callback="parse_start_url", follow= True),
    )

   def __init__(self, *a, **kw):
        super(WalmartSpider, self).__init__(*a, **kw)
        self.start_urls = [kw.get('start_url')]

   def parse_start_url(self, response):
        return self.parse_items(response)

   def parse_items(self, response):
       sel = Selector(response)
       sites = sel.xpath('//div[starts-with(@id,"i_")]')
       items = []
       for site in sites:
           item = WalmartItem()
           item['price'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/div[@class="OnlinePriceAvail"]/div[@class="PriceContent"]/div[@class="PriceDisplay"]/div[@class="camelPrice"]/span[@class="bigPriceText2"]/text()').extract()
           item['link'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/a[@class="prodLink GridItemLink"]/@href').extract()
           item['title'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/a[@class="prodLink GridItemLink"]/@title').extract()
           if item['price'] and item['title']:
               if(item['link']):
                   item['link'][0] = "www.walmart.com" + item['link'][0]
                   items.append(item)
           else:
               item['price'] = site.xpath('div/div/div/div/div/div/span[@class="bigPriceText2"]/text()').extract()
               item['link'] = site.xpath('div/div[@class="prodInfo"]/div[@class="prodInfoBox"]/a[@class="prodLink GridItemLink"]/@href').extract()
               item['title'] = site.xpath('div/div[@class="prodInfo"]/div[@class="prodInfoBox"]/a[@class="prodLink GridItemLink"]/@title').extract()
               if item['price'] and item['title']:
                   if(item['link']):
                       item['link'][0] = "www.walmart.com" + item['link'][0]
                       items.append(item)
       return items
