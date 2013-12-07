__author__ = 'piammoradi'
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from priceAggregator.items import WalMartItem
from priceAggregator.spiders.starturls import StartUrls

class WalmartSpider(CrawlSpider):
    name = "walmart"
    allowed_domains = ["walmart.com"]
    rules = (
        Rule (SgmlLinkExtractor(allow=("ic=16_[1-128]\&*", ), restrict_xpaths=('//div/div[@id="bottomPagination"]/ul/li',))
    , callback="parse_items", follow= True),
    )

    def __init__(self, *a, **kw):
        super(WalmartSpider, self).__init__(*a, **kw)
        self.start_urls = [kw.get('start_url')]

    def parse_items(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[starts-with(@id,"i_")]')
        items = []
        for site in sites:
           item = WalMartItem()
           item['title'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/a[@class="prodLink GridItemLink"]/@title').extract()
           #item['link'] = "http://www.walmart.com" + site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/a[@class="prodLink GridItemLink"]/@href').extract()[0]
           item['link'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/a[@class="prodLink GridItemLink"]/@href').extract()
           item['price'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/div[@class="OnlinePriceAvail"]/div[@class="PriceContent"]/div[@class="PriceDisplay"]/div[@class="camelPrice"]/span[@class="bigPriceText2"]/text()').extract()
           item['price2'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/div[@class="OnlinePriceAvail"]/div[@class="PriceContent"]/div[@class="PriceDisplay"]/div[@class="PriceCompare"]/div[@class="camelPrice"]/span[@class="bigPriceText2"]/text()').extract()
           if item['price'] or item['price2']:
               items.append(item)
        return items