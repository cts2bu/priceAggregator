__author__ = 'piammoradi'
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import os
from CS4240Project.items import WalMartItem

class WalmartSpider(CrawlSpider):
    name = "walmart"
    allowed_domains = ["walmart.com"]
    start_urls = ["http://www.walmart.com/search/search-ng.do?Find=Find&_be_switches=rmfield_product_badges_rmvalue_top_rated%3Aoff&_refineresult=true&ic=16_0&search_constraint=0&search_query=jvc+camcorder&facet=brand%3AJVC&_be_switches=rmfield_product_badges_rmvalue_top_rated:off"]
    rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//div/div[@id="bottomPagination"]/ul/li',))
    , callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="prodInfo"]//div[@class="prodInfoBox"]')
        items = []
        for site in sites:
           item = WalMartItem()
           item['title'] = site.xpath('a[@class="prodLink ListItemLink"]/text()').extract()
           item['price'] = site.xpath('div[@class="OnlinePriceAvail"]/div[@class="PriceContent"]/div[@class="PriceDisplay"]/div[@class="PriceCompare"]/div[@class="camelPrice"]/span[@class="bigPriceText2"]/text()').extract()
           items.append(item)
        return items
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