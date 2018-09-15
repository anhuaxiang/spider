# -*- coding:utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from userinfo.items import UserinfoItem


class DmozSpider(scrapy.Spider):
    name = "user"
    redis_key = 'douban:start_urls'
    start_urls = []
    url = 'http://www.dianping.com/member/'

    def start_requests(self):
        file_object = open(r'C:\Users\yanrujing\Desktop\comment.csv', 'r')
        try:
            for line in file_object:
                x = line.strip()
                user_id = x.split(',')[-1]
                self.start_urls.append("http://www.dianping.com/member/" + user_id)
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        finally:
            file_object.close()

    def parse(self, response):
        item = UserinfoItem()
        selector = Selector(response)

        id = response.url.split('/')[-1]
        item['user_id'] = id

        reg_1 = r'class="name">(.*?)</h2>'
        gre_1 = re.compile(reg_1, re.S)
        name = re.findall(gre_1, str(response.body))
        item['name'] = name

        user_span = selector.xpath('//span[@class="user-groun"]')
        for x in user_span:
            sex = x.xpath('i/@class').extract()
            city = x.xpath('text()').extract()
            item['sex'] = sex
            item['city'] = city

        reg_2 = r'title="贡献值(.*?)"'
        gre_2 = re.compile(reg_2, re.S)
        contribution = re.findall(gre_2, str(response.body))
        item['contribution'] = contribution

        reg_3 = r'<strong >(.*?)</strong>'
        gre_3 = re.compile(reg_3, re.S)
        num = re.findall(gre_3, str(response.body))
        if num[0]:
            item['attention'] = num[0]
        if num[1]:
            item['fans'] = num[1]
        if num[2]:
            item['inter'] = num[2]

        reg_4 = r'</span>(.*?)</p>'
        gre_4 = re.compile(reg_4, re.S)
        time = re.findall(gre_4, str(response.body))
        item['register_time'] = time[2]
        item['user_url'] = response.url
        yield item



