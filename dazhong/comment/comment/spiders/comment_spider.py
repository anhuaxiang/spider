# -*- coding:utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from comment.items import CommentItem
from scrapy.http import Request


class DmozSpider(scrapy.Spider):
    name = "comment"
    redis_key = 'comment:start_urls'
    x = input("输入要爬信息:")
    y = input("输入要爬城市id:")
    url = "http://www.dianping.com"
    s_u = url+'/search/keyword/'+str(y)+'/0_' + x
    start_urls = [s_u]

    def parse(self, response):
        item = CommentItem()
        selector = Selector(response)
        shop_list = selector.xpath('//div[@id="shop-all-list"]')
        shop_comment_1 = selector.xpath('//div[@class="main"]')
        shop_comment_2 = selector.xpath('//div[@class="main page-sa Fix"]')

        if shop_list:
            url = shop_list.xpath('//div[@class="tit"]/a[@data-hippo-type="shop"]/@href').extract()
            for each in url:
                next = "http://www.dianping.com"+each+"/review_more"
                yield Request(next, callback=self.parse)
            nextLink = selector.xpath('//div[@class="page"]/a[@class="next"]/@href').extract()
            if nextLink:
                yield Request(self.url+nextLink[0], callback=self.parse)

        if shop_comment_2:
            shop_kind = selector.xpath('//span[@itemprop="title"]/text()').extract()
            if shop_kind:
                item['shop_kind'] = shop_kind[-1]
            lis = selector.xpath('//li[@class="comment-list-item"]')
            for each in lis:
                comment_id = each.xpath('@data-id').extract()
                item['comment_id'] = comment_id

                user_id = each.xpath('a[@rel="nofollow"]/@user-id').extract()
                item['user_id'] = user_id

                reg_1 = r'irr-star(.*?)" title'
                gre_1 = re.compile(reg_1, re.S)
                star = re.findall(gre_1, each.extract())
                item['star'] = star

                content = each.xpath('div[@class="content"]/div[@class="comment-entry"]/div/text()').extract()
                item['content'] = item['content'] = ''.join(content).replace('\n', '').replace(' ', '')

                item['support_num'] = 0

                time = each.xpath('div[@class="content"]/div[@class="misc"]/span/text()').extract()
                item['time'] = time[0]

                shop_name = each.xpath('div[@class="content"]/div[@class="misc"]/h2/text()').extract()
                item['shop_name'] = "".join(shop_name).replace('\n', '').replace(' ', '')

                self_url = str(response.url)
                reg_1 = r'shop/(.*?)/revie'
                gre_1 = re.compile(reg_1, re.S)
                shop_id = re.findall(gre_1, self_url)
                item['shop_url'] = self.url+'/shop/'+str(shop_id[0])
                item['shop_id'] = shop_id
                yield item
            nextPage = selector.xpath('//a[@class="NextPage"]/@href').extract()
            if nextPage:
                self_url = str(response.url)
                reg_0 = r'shop/(.*?)/revie'
                gre_0 = re.compile(reg_0, re.S)
                shop_id = re.findall(gre_0, self_url)
                shop_url_self = self.url + '/shop/' + str(shop_id[0])
                yield Request(shop_url_self+'/review_all'+nextPage[0], callback=self.parse)

        if shop_comment_1:
            lis = selector.xpath('//div[@class="comment-list"]/ul/li')
            shop_kind = selector.xpath('//span[@itemprop="title"]/text()').extract()
            if shop_kind:
                item['shop_kind'] = shop_kind[-1]
            for each in lis:
                comment_id = each.xpath('@data-id').extract()
                item['comment_id'] = comment_id

                user_id = each.xpath('div[@class="pic"]/a[@rel="nofollow"]/@user-id').extract()
                item['user_id'] = user_id

                reg_1 = r'irr-star(.*?)">'
                gre_1 = re.compile(reg_1, re.S)
                star = re.findall(gre_1, each.extract())
                item['star'] = star

                content = each.xpath('div[@class="content"]/div[@class="comment-txt"]/div/text()').extract()
                item['content'] = ''.join(content).replace('\n', '').replace(' ', '')

                support_num = each.xpath('div[@class="content"]/div[@class="misc-info"]/span[@class="col-right"]/span[@class="countWrapper"]/a/span[@class="heart-num"]/text()').extract()
                if support_num:
                    item['support_num'] = support_num
                else:
                    item['support_num'] = "(0)"

                time = each.xpath('div[@class="content"]/div[@class="misc-info"]/span/text()').extract()
                item['time'] = time[0]

                shop_name = each.xpath('div[@class="content"]/div[@class="misc-info"]/h2/text()').extract()
                item['shop_name'] = "".join(shop_name).replace('\n', '').replace(' ', '')

                self_url = str(response.url)
                reg_1 = r'shop/(.*?)/revie'
                gre_1 = re.compile(reg_1, re.S)
                shop_id = re.findall(gre_1, self_url)
                item['shop_url'] = self.url + '/shop/' + str(shop_id[0])
                item['shop_id'] = shop_id
                yield item
            nextPage = selector.xpath('//a[@class="NextPage"]/@href').extract()
            if nextPage:
                self_url = str(response.url)
                reg_0 = r'shop/(.*?)/revie'
                gre_0 = re.compile(reg_0, re.S)
                shop_id = re.findall(gre_0, self_url)
                shop_url_self = self.url + '/shop/' + str(shop_id[0])
                yield Request(shop_url_self + '/review_all' + nextPage[0], callback=self.parse)



