# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnproxyItem(scrapy.Item):
    # define the fields for your item here like:
    tp = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
