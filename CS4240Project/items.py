__author__ = 'Chris'

from scrapy.item import Item, Field

class TorrentItem(Item):
    url = Field()
    name = Field()
    description = Field()
    size = Field()

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class eBayItem(Item):
    title = Field()
    price = Field()
    price2 = Field()
    link = Field()

class MacysItem(Item):
    title = Field()
    origprice = Field()
    saleprice = Field()

class CraigslistSampleItem(Item):
    title = Field()
    link = Field()

class AmazonItem(Item):
    title = Field()
    link = Field()
    price = Field()
    price2 = Field()

class AmazeItem(Item):
    title = Field()
    link = Field()

class WalMartItem(Item):
    title = Field()
    price = Field()
    price2 = Field()
    link = Field()
