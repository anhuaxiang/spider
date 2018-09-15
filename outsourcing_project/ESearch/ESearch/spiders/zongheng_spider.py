# -*- coding:utf-8 -*-
import scrapy
import re
import sys
import urllib2
from scrapy.selector import Selector
from scrapy.http import Request
from ESearch.items import XiangmuItem
from ESearch.utils.common import get_md5

reload(sys)
sys.setdefaultencoding("utf-8")


class DmozSpider(scrapy.Spider):
    name = "zongheng"
    start_urls = []
    main_url = "http://www.zongheng.com"

    def start_requests(self):
        for i in range(999):
            url = "http://book.zongheng.com/store/c0/c0/b0/u0/p" + str(i+1) +"/v9/s9/t0/ALL.html"
            self.start_urls.append(url)
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        item = XiangmuItem()
        item["book_name"] = ''
        item["book_author"] = ''
        item["book_type"] = ''
        item["book_format"] = ''
        item["book_time"] = ''
        item["book_url"] = ''
        item["book_size"] = ''
        item["book_downl_url"] = ''
        item["book_source"] = ''
        item["book_intro"] = ''
        item["book_content"] = ''
        item["book_zip_pswd"] = ''
        item["book_chinese"] = ''
        item["book_id"] = ''

        selector = Selector(response)
        lists = selector.xpath('//ul[@class="main_con"]/li')
        for each in lists:
            kind = each.xpath('span[@class="kind"]')
            if kind:
                item["book_type"] = each.xpath('span[@class="kind"]/a/text()').extract()
                item["book_name"] = each.xpath('span[@class="chap"]/a')[0].xpath('text()').extract()
                url = each.xpath('span[@class="chap"]/a')[0].xpath('@href').extract()
                item["book_url"] = url
                item["book_id"] = get_md5(''.join(url))
                item["book_downl_url"] = url
                item["book_content"] = ''.join(each.xpath('span[@class="chap"]/a')[1].xpath('text()').extract()).replace('\n', '')
                item["book_size"] = ''.join(each.xpath('span[@class="number"]/text()').extract()).replace('\n', '').replace('\t', '')+"字"
                item["book_author"] = each.xpath('span[@class="author"]/a/text()').extract()
                item["book_time"] = ''.join(each.xpath('span[@class="time"]/text()').extract()).replace('\n', '').replace('\t', '')

                data = urllib2.urlopen(''.join(url)).read().decode('utf-8')
                reg = r'<div class="info_con">(.*?)</div>'
                gre = re.compile(reg, re.S)
                intro = re.findall(gre, data)
                intro = ''.join(intro).replace('\r', '').replace('\n', '').replace('\t', '')

                reg = r'<p>(.*?)</p>'
                gre = re.compile(reg, re.S)
                book_intro = re.findall(gre, intro)
                item["book_intro"] = book_intro
                yield item



