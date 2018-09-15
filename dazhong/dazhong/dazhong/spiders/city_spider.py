# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from dazhong.items import DazhongItem


class DmozSpider(scrapy.Spider):
    name = "city"
    redis_key = 'city:start_urls'
    start_urls = ["http://dpindex.dianping.com/dpindex?category=&region=&type=rank&city=1"]
    url = "http://dpindex.dianping.com/dpindex?category=&region=&type=rank&city="
    id = 1

    def parse(self, response):
        item = DazhongItem()
        selector = Selector(response)
        city = selector.xpath('//label[@class="side-search-label"]/text()').extract()

        # id = selector.xpath('//div[@class ="side-input side-search-city"]/label/@data-id').extract()
        #  item['id'] = id

        item['id'] = self.id
        item['city'] = city
        item['url'] = response.url

        if city:
            yield item
        if self.id <= 3630:
            self.id += 1
            yield Request(self.url + str(self.id), callback=self.parse)
