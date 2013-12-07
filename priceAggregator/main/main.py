__author__ = 'piammoradi'
from priceAggregator.spiders.starturls import StartUrls
from priceAggregator.spiders.AmazonSpider import AmazonSpider
from scrapy.crawler import Crawler
from priceAggregator import settings
from twisted.internet import reactor
from scrapy import signals
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

input_search = raw_input("Search for items: ")
urls = StartUrls(input_search)

spider = AmazonSpider(urls)

crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start
reactor.run()



