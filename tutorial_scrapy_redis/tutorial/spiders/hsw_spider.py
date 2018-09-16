# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from tutorial.items import TutorialItem


# class HswSpiderSpider(scrapy.Spider):
class HswSpiderSpider(RedisSpider):
    name = 'hsw_spider'
    allowed_domains = ['hsw.cn']
    # start_urls = ["http://finance.hsw.cn/hyxw/index.shtml"]
    redis_key = 'myspider:start_urls'

    def parse(self, response):
        list_url = response.xpath('//div[@class="listleft"]/ul/li/h3/a/@href').extract()
        for url in list_url:
            yield scrapy.Request(url, callback=self.parse_item)

        next_url = response.xpath('//div[@class="page"]/a[@class="a1"]/@href').extract()
        if len(next_url) > 1:
            yield scrapy.Request(next_url[1], callback=self.parse)

    def parse_item(self, response):
        item = TutorialItem()
        item['title'] = response.xpath('//div[@class="hd"]/h1/text()').extract_first()
        item['content'] = response.xpath('//div[@class="photoarea"]//p/text()|//div[@class="contentBox cf"]//p/text()').extract_first()
        item['get_time'] = response.xpath('//span[@class="article-time"]/text()').extract_first()
        yield item
