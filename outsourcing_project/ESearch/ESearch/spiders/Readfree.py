# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ESearch.items import ReadmefreeItemLoader,ReadmefreeItem
from ESearch.utils.common import get_md5

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ReadfreeSpider(CrawlSpider):
    name = 'Readfree'
    allowed_domains = ['readfree.me']
    start_urls = ['http://readfree.me/']
    rules = (

        Rule(LinkExtractor(allow=(".page=\d+")),follow=True),
        Rule(LinkExtractor(allow=("book/\d+/")), callback='parse_detail', follow=True),

    )

    def parse_detail(self, response):
        item_loader = ReadmefreeItemLoader(item=ReadmefreeItem(), response=response)
        item_loader.add_xpath("kindle_name","//*[@class='link-search']/text()")
        item_loader.add_xpath("kindle_author", "//*[@class='z-link-search']/strong/text()")
        item_loader.add_css("kindle_score", ".badge-success::text")
        item_loader.add_xpath("kindle_intro", "//*[@class='tab-content']/div[1]/pre/text()")
        item_loader.add_value("kindle_url", response.url)
        item_loader.add_xpath("kindle_type", "//*[@id='book-tags']/li/descendant-or-self::text()")
        item_loader.add_value("kindle_id",get_md5(response.url))


        detail = item_loader.load_item()

        return detail

