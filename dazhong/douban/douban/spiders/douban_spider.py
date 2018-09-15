# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from douban.items import DoubanItem
class DmozSpider(scrapy.Spider):
    name = "douban"
    redis_key = 'douban:start_urls'
    start_urls = ["http://movie.douban.com/top250"]
    url = "http://movie.douban.com/top250"
    def parse(self, response):
        item = DoubanItem()
        selector = Selector(response)
        movies = selector.xpath('//div[@class="info"]')
        for each in movies:

            title = each.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for eachTitle in title:
                fullTitle +=eachTitle
            # print fullTitle

            movieInfo = each.xpath('div[@class="bd"]/p/text()').extract()
            # print movieInfo

            star = each.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            # print star

            quote = each.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''
            # print quote

            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield Request(self.url+nextLink, callback=self.parse)

