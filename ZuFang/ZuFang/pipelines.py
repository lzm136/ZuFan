# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from ZuFang.items import ZufangItem
from scrapy.conf import settings
from pymongo import MongoClient


class ZufangPipeline(object):


    def __init__(self):
        self.file = open('danke.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, ZufangItem):
            str_data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.file.write(str_data)

        return item

    def __del__(self):
        self.file.close()


class ZuFangMongoPipeline(object):
    # 储存到mongodb

    def open_spider(self, spider):
        # 读取信息
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        dbname = settings['MONGO_DBNAME']
        colname = settings['MONGO_COLNAME']

        # 创建数据库连接
        self.client = MongoClient(host, port)

        # 选择数据库
        self.db = self.client[dbname]
        # 选择集合
        self.col = self.db[colname]


    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert(data)
        return item


    def close_spider(self, spider):
        # 关闭数据库
        self.client.close()
