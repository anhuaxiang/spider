# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector
from shop.items import ShopItem
import re


class DmozSpider(scrapy.Spider):
    name = "shop"
    redis_key = 'city:start_urls'
    start_urls = []

    def start_requests(self):
        file_object = open(r'C:\Users\yanrujing\Desktop\dazhong\shop_url\shop_url_1.txt', 'r')
        try:
            for line in file_object:
                x = line.strip()
                self.start_urls.append(x)
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        finally:
            file_object.close()

    def parse(self, response):
        item = ShopItem()
        selector = Selector(response)

        item['url'] = response.url

        item['shop_id'] = str(str(response.url).split('/')[-1])

        reg_1 = r'shopName: "(.*?)",.*?'
        imgre_1 = re.compile(reg_1, re.S)
        shop_name = re.findall(imgre_1, str(response.body))
        reg_3 = r'fullName: "(.*?)",.*?'
        imgre_3 = re.compile(reg_3, re.S)
        full_name = re.findall(imgre_3, str(response.body))
        if full_name:
            item['name'] = full_name[0]
        else:
            if shop_name:
                item['name'] = shop_name[0]

        reg_2 = r'cityCnName: "(.*?)",.*?'
        imgre_2 = re.compile(reg_2, re.S)
        city = re.findall(imgre_2, str(response.body))
        if city:
            item['city'] = city[0]
        else:
            city = selector.xpath('//a[@class="city J-city"]/span/text()')
            if city:
                item['city'] = city

        reg_4 = r'class="mid-rank-stars mid-str(.*?)">'
        imgre_4 = re.compile(reg_4, re.S)
        star_1 = re.findall(imgre_4, str(response.body))
        reg_7 = r'class="item-rank-rst irr-star(.*?)".*?'
        imgre_7 = re.compile(reg_7, re.S)
        star_2 = re.findall(imgre_7, str(response.body))
        if star_1:
            item['star'] = star_1[0]
        else:
            item['star'] = star_2[0]

        reg_5 = r'class="item">(.*?)条评论</span>'
        imgre_5 = re.compile(reg_5, re.S)
        num_1 = re.findall(imgre_5, str(response.body))
        num_2 = selector.xpath('//span[@itemprop="count"]/text()').extract()
        if num_1:
            item['comment_num'] = num_1
        else:
            item['comment_num'] = num_2

        address = selector.xpath('//span[@itemprop="street-address"]/@title').extract()
        if address:
            item['address'] = address
        else:
            address = selector.xpath('//span[@class="fl"]/@title').extract()
            item['address'] = address

        reg_6 = r'mainCategoryName:"(.*?)",.*?'
        imgre_6 = re.compile(reg_6, re.S)
        kind = re.findall(imgre_6, str(response.body))
        if kind:
            item['kind'] = kind
        else:
            kind = selector.xpath('//span[@class="bread-name"]/text()').extract()
            if kind:
                item['kind'] = kind[-1]
            else:
                kind = selector.xpath('//a[@itemprop="url"]/text()').extract()
                if kind:
                    item['kind'] = kind[-2]
                else:
                    kind = selector.xpath('//a[@target="_blank"]').extract()
                    if kind:
                        item['kind'] = kind[-2]
        yield item
