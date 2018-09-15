# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EsearchPipeline(object):
    def process_item(self, item, spider):
        return item


class ElasticsearchPipeline(object):
    #将数据写入到es中

    def process_item(self, item, spider):
        #将item转换为es的数据
        item.save_to_es()

        return item