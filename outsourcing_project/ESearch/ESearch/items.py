# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy import Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from models.es_types import CommonbookType

from elasticsearch_dsl.connections import connections

es_f = connections.create_connection(CommonbookType._doc_type.using)


def fgen_suggests(index, info_tuple):
    # 根据字符串生成搜索建议数组
    used_words = set()
    suggests = []
    for text, weight in info_tuple:
        if text:
            # 调用es的analyze接口分析字符串
            words = es_f.indices.analyze(index=index, analyzer="ik_max_word", params={'filter': ["lowercase"]},
                                         body=text)
            anylyzed_words = set([r["token"] for r in words["tokens"] if len(r["token"]) > 1])
            new_words = anylyzed_words - used_words
        else:
            new_words = set()

        if new_words:
            suggests.append({"input": list(new_words), "weight": weight})

    return suggests


def return_value(value):
    if value:
        return " "
    else:
        return value


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


class QcenglishItemLoader(ItemLoader):
    default_input_processor = TakeFirst()


class QcenglishItem(scrapy.Item):
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_type = scrapy.Field(input_processor=MapCompose(return_value))
    book_format = scrapy.Field(input_processor=MapCompose(return_value))
    book_time = scrapy.Field(input_processor=MapCompose(return_value))
    book_url = scrapy.Field()
    book_size = scrapy.Field(input_processor=MapCompose(get_nums))
    book_downl_url = scrapy.Field(input_processor=MapCompose(return_value))
    book_source = scrapy.Field(input_processor=MapCompose(return_value))
    book_intro = scrapy.Field(input_processor=MapCompose(return_value))
    book_content = scrapy.Field(input_processor=MapCompose(return_value))
    book_zip_pwd = scrapy.Field()
    book_chinese = scrapy.Field(input_processor=MapCompose(return_value))
    book_id = scrapy.Field()

    def save_to_es(self):
        article = CommonbookType()

        article.book_name = self["book_name"]
        article.book_author = self["book_author"]
        article.book_type = self["book_type"]
        article.book_format = self["book_format"]
        article.book_url = self["book_url"]
        article.book_downl_url = self["book_downl_url"]
        article.book_source = self["book_source"]
        article.book_intro = self["book_intro"]
        article.book_zip_pwd = self["book_zip_pwd"]
        article.book_chinese = self["book_chinese"]
        article.book_id = self["book_id"]
        article.suggest = fgen_suggests(CommonbookType._doc_type.index,
                                        ((article.book_name, 10), (article.book_intro, 7), (article.book_author, 5)))
        article.save()

        return


class SinaItemLoader(ItemLoader):
    default_input_processor = TakeFirst()


class SinaItem(scrapy.Item):
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_type = scrapy.Field()
    book_format = scrapy.Field()
    book_time = scrapy.Field()
    book_url = scrapy.Field()
    book_size = scrapy.Field()
    book_downl_url = scrapy.Field()
    book_source = scrapy.Field()
    book_intro = scrapy.Field()
    book_content = scrapy.Field()
    book_zip_pwd = scrapy.Field()
    book_chinese = scrapy.Field()
    book_id = scrapy.Field()

    def save_to_es(self):
        article = CommonbookType()
        article.book_name = self['book_name']
        article.book_format = self['book_format']
        article.book_type = self['book_type']
        article.book_url = self['book_url']
        article.book_content = self['book_content']
        article.book_source = self['book_source']
        article.book_intro = self['book_intro']
        article.book_id = self['book_id']
        article.book_time = self['book_time']
        article.suggest = fgen_suggests(CommonbookType._doc_type.index,
                                        ((article.book_name, 10), (article.book_intro, 7), (article.book_author, 5)))
        article.save()

        return


class ReadmefreeItemLoader(ItemLoader):
    default_input_processor = TakeFirst()


class ReadmefreeItem(scrapy.Item):
    kindle_name = scrapy.Field()
    kindle_author = scrapy.Field()
    kindle_score = scrapy.Field()
    kindle_intro = scrapy.Field()
    kindle_url = scrapy.Field()
    kindle_type = scrapy.Field()
    kindle_id = scrapy.Field()

    def save_to_es(self):
        article = CommonbookType()
        article.kindle_name = self['kindle_name']
        article.kindle_author = self['kindle_author']
        article.kindle_score = self['kindle_score']
        article.kindle_intro = self['kindle_intro']
        article.kindle_url = self['kindle_url']
        article.kindle_type = self['kindle_type']
        article.kindle_id = self['kindle_id']

        article.suggest = fgen_suggests(CommonbookType._doc_type.index, (
            (article.kindle_name, 10), (article.kindle_intro, 7), (article.kindle_type, 5)))
        article.save()

        return


class KankandouItemLoader(ItemLoader):
    default_input_processor = TakeFirst()


class KankandouItem(scrapy.Item):
    kindle_name = scrapy.Field()
    kindle_author = scrapy.Field()
    kindle_score = scrapy.Field()
    kindle_intro = scrapy.Field()
    kindle_url = scrapy.Field()
    kindle_type = scrapy.Field()
    kindle_id = scrapy.Field()

    def save_to_es(self):
        article = CommonbookType()
        article.kindle_name = self['kindle_name']
        article.kindle_author = self['kindle_author']
        article.kindle_score = self['kindle_score']
        article.kindle_intro = self['kindle_intro']
        article.kindle_url = self['kindle_url']
        article.kindle_type = self['kindle_type']
        article.kindle_id = self['kindle_id']

        article.suggest = fgen_suggests(CommonbookType._doc_type.index, (
            (article.kindle_name, 10), (article.kindle_intro, 7), (article.kindle_type, 5)))
        article.save()

        return


class XiangmuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = Field()
    book_author = Field()
    book_type = Field()
    book_format = Field()
    book_time = Field()
    book_url = Field()
    book_size = Field()
    book_downl_url = Field()
    book_source = Field()
    book_intro = Field()
    book_content = Field()
    book_zip_pswd = Field()
    book_chinese = Field()
    book_id = Field()

    def save_to_es(self):
        article = CommonbookType()
        article.book_name = self["book_name"]
        article.book_author = self["book_author"]
        article.book_type = self["book_type"]
        article.book_format = self["book_format"]
        article.book_time = self["book_time"]
        article.book_url = self["book_url"]
        article.book_size = self["book_size"]
        article.book_downl_url = self["book_downl_url"]
        article.book_source = self["book_source"]
        article.book_intro = self["book_intro"]
        article.book_content = self["book_content"]
        article.book_zip_pswd = self["book_zip_pswd"]
        article.book_chinese = self["book_chinese"]
        article.book_id = self["book_id"]

        article.suggest = fgen_suggests(CommonbookType._doc_type.index, (
            (article.book_name, 10), (article.book_intro, 7), (article.book_author, 5)))
        article.save()
