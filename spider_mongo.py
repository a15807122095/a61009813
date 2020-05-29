# -*-coding:utf-8-*-

import pymongo

# 创建mongo连接对象
client = pymongo.MongoClient('127.0.0.1', 27017)

collection = client['eastmoney']['status']
