# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ZhangshangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = Field()
    book_author = Field()
    book_type = Field()
    book_format = Field()
    book_time = Field()
    book_url = Field()
    book_size = Field()
    book_download_url = Field()
    book_source = Field()
    book_intro = Field()
    book_content = Field()
    book_zip_pswd = Field()
    book_chinese = Field()
    book_id = Field()
    pass
