# -*- coding:utf-8 -*-
import scrapy

from scrapy import Request
from scrapy import Selector
from aiqiyi.items import AiqiyiItem


class DmozSpider(scrapy.Spider):
    name = "aiqiyi"
    start_urls = ["http://list.iqiyi.com/www/1/-------------4-1-1-iqiyi--.html"]
    main_url = "http://www.iqiyi.com"

    def parse(self, response):
        item = AiqiyiItem()
        selector = Selector(response)
        is_list_page = selector.xpath('//div[@class="wrapper-cols"]')
        if is_list_page:
            movie_lists_url = is_list_page.xpath('div/ul/li/div[@class="site-piclist_pic"]/a/@href').extract()
            for each in movie_lists_url:
                yield Request(each, callback=self.parse)

            next_href = selector.xpath('//a[@data-key="down"]/@href').extract()
            if next_href:
                yield Request("http://list.iqiyi.com/" + next_href[0], callback=self.parse)

        # 系列
        is_info_page_1 = selector.xpath('//div[@class="result_detail-minH"]')
        if is_info_page_1:
            item["url"] = response.url
            item["name"] = is_info_page_1.xpath('h1/a/text()').extract()
            info_lists = selector.xpath('//div[@class="topic_item clearfix"]')
            if info_lists:
                del info_lists[-1]
                type = ""
                for each in info_lists:
                    t = '/'.join(each.xpath('div/em/a/text()').extract())
                    type = type + "/" + t
                item["type"] = type
            item["introduction"] = selector.xpath('//span[@data-moreorless="lessinfo"]/span/text()').extract()
            item["id"] = selector.xpath('//span[@title="播放"]/@data-pc-albumid'.decode('utf-8')).extract()[0]
            yield item

        is_info_page_2 = selector.xpath('//div[@class="mod-breadcrumb"]')
        if is_info_page_2:
            item["name"] = selector.xpath('//h1[@class="mod-play-tit"]/span[@id="widget-videotitle"]/text()').extract()
            item["id"] = selector.xpath('//h1[@class="mod-play-tit"]/span[@class="score"]/@data-score-tvid').extract()
            item["url"] = response.url
            type = selector.xpath('//span[@id="datainfo-taglist"]/a/text()').extract()
            item["type"] = '/'.join(type)
            performer = selector.xpath('//p[@class="rl-pic"]/a/@title').extract()
            item["performer"] = '/'.join(performer)
            item["director"] = selector.xpath('//a[@rseat="director_1"]/text()').extract()
            item["introduction"] = ''.join(selector.xpath('//span[@id="data-videoInfoDes"]/text()').extract()).replace(" ", "").replace("\n", "")
            yield item
