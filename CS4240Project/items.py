__author__ = 'Chris'

from scrapy.item import Item, Field

class TorrentItem(Item):
    url = Field()
    #name = Field()
    #description = Field()
    size = Field()

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class eBayItem(Item):
    title = Field()

class MacysItem(Item):
    title = Field()

class CraigslistSampleItem:
    title = Field()
    link = Field()
