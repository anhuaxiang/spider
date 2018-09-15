# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from ESearch.items import SinaItem,SinaItemLoader
from ESearch.utils.common import get_md5
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class SinaSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['ishare.iask.sina.com.cn']
    start_urls = ['http://ishare.iask.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=("/c/\d.*.html")),follow=True),
        Rule(LinkExtractor(allow=("/f/[A-Za-z0-0].*.html")),callback='parse_detail',follow=True)
    )
    def parse_detail(self, response):
        item_loader = SinaItemLoader(item=SinaItem(), response=response)
        item_loader.add_value("book_id",get_md5(response.url))
        item_loader.add_xpath("book_name","//*[@class='detail-box']/h2/@title")

        if len(response.xpath("//*[@class='detail-box']/h2/@title").extract()) != 0:
            item_loader.add_xpath("book_type", "//*[@class='detail-box']/h2/@title")
        else:
            item_loader.add_value("book_type"," ")

        if len(response.xpath("//*[class='crumbs-item']/a[1]/text()").extract()) != 0:
            item_loader.add_xpath("book_format", "//*[class='crumbs-item']/a[1]/text()")
        else:
            item_loader.add_value("book_format", " ")

        if len(response.xpath("//*[@class='detail-user-con']/div[1]/span[3]/text()").extract()) != 0:
            item_loader.add_xpath("book_time","//*[@class='detail-user-con']/div[1]/span[3]/text()" )
        else:
            item_loader.add_value("book_time"," " )

        item_loader.add_value("book_url",response.url )

        if len(response.xpath("//*[@class='detail-user-con']/div[1]/a/text()").extract()) != 0:
            item_loader.add_xpath("book_source", "//*[@class='detail-user-con']/div[1]/a/text()")
        else:
            item_loader.add_value("book_source", " ")

        if len(response.xpath("//*[@class='synopsis-detail']/p/text()").extract()) != 0:
            item_loader.add_xpath("book_intro", "//*[@class='synopsis-detail']/p/text()")
        else:
            item_loader.add_value("book_intro", " ")

        if len(response.xpath("//*[@class='detail-inner']/g/g/descendant-or-self::text()").extract()) != 0:
            item_loader.add_xpath("book_content","//*[@class='detail-inner']/g/g/descendant-or-self::text()" )
        else:
            item_loader.add_value("book_content", " ")
        detail = item_loader.load_item()
        return detail


