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
    name = "shuhai"
    start_urls = ["http://www.shuhai.com/shuku/0_0_0_0_0_2.html"]
    main_url = "http://www.shuhai.com"

    def start_requests(self):
        for i in range(58):
            url = "http://www.shuhai.com/shuku/0_0_0_0_0_" + str(i+1) + ".html"
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
        is_list_page = selector.xpath('//div[@class="show_li fix p5"]')
        if is_list_page:
            lists = selector.xpath('//p[@class="name"]')
            for each in lists:
                url = each.xpath('a/@href').extract()[0]
                yield Request(url, callback=self.parse)

        is_info_page = selector.xpath('//div[@class="book_top fix"]')
        if is_info_page:
            item["book_name"] = selector.xpath('//h2[@class="name"]/text()').extract()
            item["book_author"] = selector.xpath('//p[@class="author"]/a/text()').extract()
            item["book_url"] = response.url
            item["book_id"] = get_md5(response.url)
            item["book_downl_url"] = response.url
            item["book_intro"] = ''.join(selector.xpath('//p[@class="intro"]/text()').extract()).replace('\n', '').replace(' ', '')
            info = selector.xpath('//dl[@class="fix"]/dd')
            item["book_type"] = info[0].xpath('text()').extract()
            item["book_size"] = info[4].xpath('text()').extract()
            item["book_time"] = info[5].xpath('text()').extract()
            item["book_content"] = ''.join(selector.xpath('//p[@class="new_summary"]/text()').extract()).replace('\n', '').replace(' ', '')

            yield item









