# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
client = MongoClient()
db = client["lagou"]

class LagouPipeline:
    def process_item(self, item, spider):

        #保存数据的地方
        print(item)
        #db.zhaopin.insert_one(dict(item))
        return item
