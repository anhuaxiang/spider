# -*- coding:utf-8 -*-
import scrapy
import urllib2
import sys
import re
import json
from ESearch.items import XiangmuItem
from ESearch.utils.common import get_md5

reload(sys)
sys.setdefaultencoding("utf-8")


class DmozSpider(scrapy.Spider):
    name = "ruochu"
    start_urls = []

    def start_requests(self):
        for i in range(28):
            url = "http://a.ruochu.com/jsonp/book/all?&pageNo=" + str(i+1)
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

        sites = json.loads(response.body)
        books = sites["date"]["items"]
        for each_book in books:
            item["book_time"] = each_book["updateTime"]
            item["book_name"] = each_book["name"]
            item["book_author"] = each_book["userName"]
            item["book_size"] = str(each_book["words"]) + '字'
            item["book_content"] = each_book["subName"]
            item["book_id"] = get_md5("http://www.ruochu.com/book/" + str(each_book["objectId"]))
            item["book_url"] = "http://www.ruochu.com/book/" + str(each_book["objectId"])
            item["book_downl_url"] = "http://www.ruochu.com/book/" + str(each_book["objectId"])

            book_url = "http://www.ruochu.com/book/" + str(each_book["objectId"])
            data = urllib2.urlopen(book_url).read().decode('utf-8')
            reg = r'<span class="cate"><a>(.*?)</a></span>'
            gre = re.compile(reg, re.S)
            type = re.findall(gre, data)
            item["book_type"] = type

            yield item


















