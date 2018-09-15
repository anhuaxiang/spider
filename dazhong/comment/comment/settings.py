# -*- coding: utf-8 -*-

# Scrapy settings for comment project

BOT_NAME = 'comment'

SPIDER_MODULES = ['comment.spiders']
NEWSPIDER_MODULE = 'comment.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


DOWNLOAD_DELAY = 2

# COOKIES_ENABLED = False
FEED_FORMAT = 'CSV'
FEED_URI = u'file:///C:/Users/yanrujing/Desktop/comment.CSV'

# FEED_EXPORTERS = {
#     'csv': 'comment.export.MyProjectItemExporter',
# }
#
# FIELDS_TO_EXPORT = [
#     'comment_id',
#     'user_id'
#     'star',
#     'content',
#     'support_num',
#     'time',
#     'shop_id',
#     'shop_name'
#     'shop_kind'
#     'shop_url'
#
# ]
