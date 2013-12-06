__author__ = 'piammoradi'
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import os
from CS4240Project.items import WalMartItem

class WalmartSpider(CrawlSpider):
    name = "walmart"
    allowed_domains = ["walmart.com"]
    start_urls = ["http://www.walmart.com/search/search-ng.do?ic=16_0&Find=Find&search_query=jvc+camcorder&Find=Find&search_constraint=0"]
    rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//div/div[@id="bottomPagination"]/ul/li',))
    , callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[starts-with(@id,"i_")]')
        items = []
        for site in sites:
           item = WalMartItem()
           item['title'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/a[@class="prodLink ListItemLink"]/text()').extract()
           item['price'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/div[@class="OnlinePriceAvail"]/div[@class="PriceContent"]/div[@class="PriceDisplay"]/div[@class="camelPrice"]/span[@class="bigPriceText2"]/text()').extract()
           item['price2'] = site.xpath('div[@class="prodInfo"]/div[@class="prodInfoBox"]/div[@class="OnlinePriceAvail"]/div[@class="PriceContent"]/div[@class="PriceDisplay"]/div[@class="PriceCompare"]/div[@class="camelPrice"]/span[@class="bigPriceText2"]/text()').extract()
           items.append(item)
        return items
        pass
        # sites2 = sel.xpath('//div[@class="PriceDisplay"]/div[@class="PriceCompare"]/div[@class="camelPrice"]')
        # for site2 in sites2:
        #     item = WalMartItem()
        #     item['price'] = site2.xpath('a[@class="bigPriceText2"]/text()').extract()
        #     items.append(item)
        # return items
        # item = WalMartItem()
        # item['title'] = sel.xpath('//div[@class="prodInfo"]/div[@class="prodInfoBox"]/a[@class="prodLink ListItemLink"]/text()').extract()
        # item['price'] = sel.xpath('//div[@class="camelPrice"]/span/text()').extract()
        # return item


if __name__ == "__main__":
    os.system('scrapy crawl walmart -o walmart8.json -t json')