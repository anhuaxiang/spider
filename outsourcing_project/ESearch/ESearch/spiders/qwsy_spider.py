# -*- coding:utf-8 -*-
import scrapy
import re
import sys
from scrapy.selector import Selector
from scrapy.http import Request
from ESearch.items import XiangmuItem
from ESearch.utils.common import get_md5

reload(sys)
sys.setdefaultencoding("utf-8")


class DmozSpider(scrapy.Spider):
    name = "qwsy"
    start_urls = []
    main_url = "http://www.qwsy.com"

    def start_requests(self):
        for i in range(315):
            url = "http://www.qwsy.com/shuku.aspx?&page=" + str(i+1)
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
        lists = selector.xpath('//tbody[@id="tbody_list"]/tr')
        books = []
        for i in range(len(lists)):
            if i % 2 == 0:
                books.append(lists[i])
        for each in books:
            type = each.xpath('td[@class="roomkindwidth tc"]/text()').extract()
            item["book_type"] = ''.join(type).replace('[', '').replace(']', '')
            item["book_name"] = each.xpath('td/div[@class="td26hide"]/a[@rel="external"]/text()').extract()
            item["book_intro"] = each.xpath('td/div[@class="td26hide"]/a[@rel="external"]/@title').extract()
            item["book_content"] = each.xpath('td/div[@class="td26hide"]/a[@class="grey room_pl"]/text()').extract()
            book_url = self.main_url + "".join(each.xpath('td/div[@class="td26hide"]/a[@rel="external"]/@href').extract())
            item["book_url"] = book_url
            item["book_id"] = get_md5(book_url)
            item["book_size"] = ''.join(each.xpath('td[@class="roomwl"]/text()').extract()) + '字'
            item["book_author"] = each.xpath('td[@class="roomwrither"]/a/text()').extract()
            item["book_time"] = ''.join(each.xpath('td[@class="roomnewtime"]/text()').extract()).replace('<', '').replace('>', '')
            id = book_url.split('/')[-1].split('.')[0]
            item["book_downl_url"] = "http://www.qwsy.com/download/" + id + ".html"
            item["book_format"] = "TXT/CHM/UMD/PDF"
            yield item





