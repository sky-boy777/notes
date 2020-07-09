# -*- coding: utf-8 -*-
from pymongo import MongoClient


#链接数据库
client = MongoClient(host="127.0.0.1", port=27017)
#创建数据库
db = client.BSLN_tieba

class TbPipeline:
    def process_item(self, item, spider):
        """保存数据到mongo"""
        #插入数据
        db.data.insert_one(dict(item))
        print(item)
