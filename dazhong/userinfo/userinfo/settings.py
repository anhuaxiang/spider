# -*- coding: utf-8 -*-

BOT_NAME = 'userinfo'

SPIDER_MODULES = ['userinfo.spiders']
NEWSPIDER_MODULE = 'userinfo.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 2

COOKIES_ENABLED = False

FEED_FORMAT = 'CSV'
FEED_URI = u'file:///C:/Users/yanrujing/Desktop/user.CSV'


FEED_EXPORTERS = {
    'csv': 'userinfo.export.MyProjectItemExporter',
}

# FIELDS_TO_EXPORT = [
#     'user_id',
#     'name',
#     'sex',
#     'city',
#     'contribution',
#     'attention',
#     'fans',
#     'inter',
#     'comment',
#     'register_time',
#     'login_time',
# ]