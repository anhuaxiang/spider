# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ShopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shop_id = Field()
    name = Field()
    kind = Field()
    star = Field()
    comment_num = Field()
    city = Field()
    address = Field()
    url = Field()
    pass
