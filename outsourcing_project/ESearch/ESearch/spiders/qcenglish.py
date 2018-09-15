# -*- coding: utf-8 -*-
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ESearch.items import QcenglishItemLoader,QcenglishItem
from ESearch.utils.common import get_md5
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class QcenglishSpider(CrawlSpider):
    name = 'qcenglish'
    allowed_domains = ['qcenglish.com']
    start_urls = ['http://qcenglish.com/']

    rules = (
        Rule(LinkExtractor(allow=("/ebook/list.*.html")),follow=True),
        Rule(LinkExtractor(allow=("/ebook/\d+.html")),callback='parse_detail',follow=True),
    )

    def parse_detail(self, response):
        item_loader = QcenglishItemLoader(item=QcenglishItem(), response=response)
        item_loader.add_css("book_name","#articleTitle::text")
        item_loader.add_xpath("book_chinese","//*[@id='details']/dl[1]/dd/text()")
        item_loader.add_xpath("book_author","//*[@id='details']/dl[2]/dd/a/text()")

        if len(response.xpath("//*[@id='details']/dl[3]/dd/a/text()").extract()) != 0:
            item_loader.add_xpath("book_type", "//*[@id='details']/dl[3]/dd/a/text()")
        else:
            item_loader.add_value("book_type", " ")
        if len(response.xpath("*[@class='last']/dd/p/text()").extract()) !=0:
            item_loader.add_xpath("book_intro","//*[@class='last']/dd/p/text()")
        else:
            item_loader.add_value("book_intro","  ")
        if len(response.xpath("//*[@id='details']/dl[4]/dd/text()")) !=0:
            item_loader.add_xpath("book_format","//*[@id='details']/dl[4]/dd/text()")
        else:
            item_loader.add_value("book_format"," ")
        item_loader.add_value("book_zip_pwd","http://www.qcenglish.com")
        item_loader.add_value("book_source","http://www.qcenglish.com")
        item_loader.add_value("book_url",response.url)
        item_loader.add_value("book_id",get_md5(response.url))
        if len(response.xpath("//*[@id='download']/li/a[1]/@href").extract())==0:
            item_loader.add_value("book_downl_url", " ")
        else:
            item_loader.add_value("book_downl_url","http://www.qcenglish.com"+response.xpath("//*[@id='download']/li/a[1]/@href").extract()[0])


        detail = item_loader.load_item()
        return detail