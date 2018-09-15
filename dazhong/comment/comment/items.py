# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class CommentItem(scrapy.Item):
    comment_id = Field()
    user_id = Field()
    star = Field()
    content = Field()
    support_num = Field()
    time = Field()
    shop_id = Field()
    shop_name = Field()
    shop_kind = Field()
    shop_url = Field()
    pass
