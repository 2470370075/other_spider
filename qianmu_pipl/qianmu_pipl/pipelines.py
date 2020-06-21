# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QianmuPiplPipeline(object):

    def open_spider(self,spider):
        pass

    def close_spider(self,spider):
        pass

    def process_item(self, item, spider):
        with open('info.txt','a',encoding='utf-8') as f:
            f.write(str(item)+'\n')

        return item
