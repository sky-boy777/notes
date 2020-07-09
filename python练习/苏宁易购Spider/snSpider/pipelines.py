# -*- coding: utf-8 -*-


from pymongo import MongoClient

class SnspiderPipeline:
    def process_item(self, item, spider):
        client = MongoClient(host="127.0.0.1", port=27017)
        db = client["suning"]
        #db.book_data.insert_one(dict(item))  #将数据插入数据库
        print(item)
        return item
