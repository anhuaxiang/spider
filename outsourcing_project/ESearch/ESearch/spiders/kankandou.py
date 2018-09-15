# -*- coding: utf-8 -*-
import scrapy
from ESearch.items import KankandouItemLoader, KankandouItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ESearch.utils.common import get_md5
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class KankandouSpider(CrawlSpider):
    name = 'kankandou'
    allowed_domains = ['kankandou.com']
    start_urls = ['https://kankandou.com/']

    rules = (
        Rule(LinkExtractor(allow=(r"book/%.*.html"),deny=(r"login.html.*.html",r"reg.html.*.html")),follow=True),
        Rule(LinkExtractor(allow=(r"book/page/\d+"),deny=(r"login.html.*.html",r"reg.html.*.html")),follow=True),
        Rule(LinkExtractor(allow=(r"book/view/\d+.html"),deny=(r"login.html.*.html",r"reg.html.*.html")),callback='parse_detail',follow=True),

    )
    def parse_detail(self, response):
        item_loader = KankandouItemLoader(item=KankandouItem() , response=response)
        item_loader.add_css("kindle_name",".object-title::text")
        item_loader.add_xpath("kindle_author", "//*[@class='object-tags']/li[1]/span/descendant-or-self::text()")
        if len(response.xpath("//*[@class='object-tags']/li[5]/a/@href")) !=0:
            item_loader.add_xpath("kindle_score", "//*[@class='object-tags']/li[5]/a/@href")
        else:
            item_loader.add_value("kindle_score", " ")
        item_loader.add_xpath("kindle_intro", "//*[@class='object-content']/text()")
        item_loader.add_value("kindle_url", response.url)
        item_loader.add_xpath("kindle_type", "//*[@class='object-tags']/li[3]/span/descendant-or-self::text()")
        item_loader.add_value("kindle_id", get_md5(response.url))

        detail = item_loader.load_item()
        return detail