__author__ = 'piammoradi'
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors.sgml import Selector
from CS4240Project.items import TorrentItem
import sqlite3

con = sqlite3.connect("test_table.db")
c = con.cursor()
c.execute("create table if not exists torrents (url)")

class MininovaSpider(CrawlSpider):
    name = 'derp'
    allowed_domains = ['mininova.org']
    start_urls = ['http://www.mininova.org/today']
    rules = [Rule(SgmlLinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse_torrent(self, response):
        sel = Selector(response)
        torrent = TorrentItem()
        torrent['url'] = response.url
        torrent['name'] = sel.xpath("//h1/text()").extract()
        torrent['description'] = sel.xpath("//div[@id='description']").extract()
        torrent['size'] = sel.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
        # c.execute("insert into torrents values (?, ?, ?, ?)", (torrent['url'], torrent['name'], torrent['description'], torrent['size']))
        # con.commit()
        return torrent

