# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class AiqiyiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    url = Field()
    id = Field()
    type = Field()
    introduction = Field()

    performer = Field()
    director = Field()
    pass


class CommentItem(scrapy.Item):
    comment_id = Field()
    user_id = Field()
    user_name = Field()
    tv_id = Field()
    content = Field()
