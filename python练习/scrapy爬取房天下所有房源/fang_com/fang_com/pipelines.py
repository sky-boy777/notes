# -*- coding: utf-8 -*-
from pymongo import MongoClient

# 链接数据库
client = MongoClient(host='127.0.0.1', port=27017)
db = client["fang"]

class FangComPipeline:
    def process_item(self, item, spider):
        '''这里保存数据,我是保存到MongoDB里'''
        db.fang_date.insert_one(dict(item))
        print(item)
        return item
