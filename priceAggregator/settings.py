# Scrapy settings for priceAggregator project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'priceAggregator'

SPIDER_MODULES = ['priceAggregator.spiders']
NEWSPIDER_MODULE = 'priceAggregator.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'priceAggregator (+http://www.yourdomain.com)'
