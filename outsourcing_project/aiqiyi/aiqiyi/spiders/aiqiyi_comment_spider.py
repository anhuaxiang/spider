# -*- coding:utf-8 -*-
import scrapy
import json

from aiqiyi.items import CommentItem

class DmozSpider(scrapy.Spider):
    name = "comment"
    start_urls = ["http://api.t.iqiyi.com/qx_api/comment/get_video_comments?page=1&page_size=10&sort=hot&tvid=676191100"]

    def start_requests(self):
        file_object = open(r'aiqiyi_movie_info.csv', 'r')
        try:
            for line in file_object:
                x = line.strip()
                movie_id = x.split(',')[-1]
                for i in range(100):
                    url = "http://api.t.iqiyi.com/qx_api/comment/get_video_comments?page="+str(i+1)+"&page_size=10&sort=hot&tvid="+movie_id
                    self.start_urls.append(url)
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        finally:
            file_object.close()

    def parse(self, response):
        item = CommentItem()
        sites = json.loads(response.body)
        data = sites["data"]
        comments = data["comments"]
        if comments:
            for each in comments:
                item["comment_id"] = each["contentId"]
                item["tv_id"] = each["resourceInfo"]["tvId"]
                item["user_id"] = each["userInfo"]["uid"]
                item["user_name"] = each["userInfo"]["uname"]
                item["content"] = each["content"]
                yield item

