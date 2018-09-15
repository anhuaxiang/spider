# -*- coding: utf-8 -*-

# Scrapy settings for douban project

BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

FEED_URI = u'file:///G:/python-pachong/douban/douban.csv'
FEED_FORMAT = 'CSV'

FEED_EXPORTERS = {
    'csv': 'douban.export.MyProjectItemExporter',
}

FIELDS_TO_EXPORT = [
    'title',
    'movieInfo',
    'star',
    'quote',
]
