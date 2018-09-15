# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class UserinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = Field()
    name = Field()
    sex = Field()
    city = Field()
    contribution = Field()
    attention = Field()
    fans = Field()
    inter = Field ()
    register_time = Field()
    user_url = Field()
    pass
