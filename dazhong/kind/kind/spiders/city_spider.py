# -*- coding:utf-8 -*-
import scrapy
import re
import time
from scrapy.selector import Selector
from kind.items import KindItem
import urllib2


class DmozSpider(scrapy.Spider):
    name = "kind"
    redis_key = 'city:start_urls'
    start_urls = ["http://www.anhuaxiang.cn/xiaoyan/1.html"]

    def parse(self, response):
        item = KindItem()
        selector = Selector(response)
        div = selector.xpath('//div[@class="select-stration"]')
        div = div[1]
        list = div.xpath('div/a')
        for a in list:
            id = a.xpath('@desc-id').extract()
            kind = a.xpath('text()').extract()
            if id and kind:
                item['id'] = id
                item['kind'] = kind
                yield item


