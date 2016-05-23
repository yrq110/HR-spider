# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from house.items.house_items import HouseItem, HouseLoader, HouseDetailItem
from scrapy.exceptions import DropItem
from pymongo.mongo_client import MongoClient

class HousePipeline(object):

    MONGODB_SERVER = "your_server"
    MONGODB_PORT = "your_port"
    MONGODB_DB = "house_fs"
    MONGODB_USER = "your_user"
    MONGODB_PASSWORD = "your_password"
    
    #MONGODB_SERVER = "localhost" 
    #MONGODB_PORT = 27017
    #MONGODB_DB = "house_fs"

    def __init__(self): 
        self.item_title = set()
        self.file_test = codecs.open('test.json', 'w+', encoding='utf-8') 
        self.file_test_detail = codecs.open('test_detail.json', 'w+', encoding='utf-8') 
        try:
            #client = MongoClient(self.MONGODB_SERVER,self.MONGODB_PORT) 
            #client = MongoClient(self.MONGODB_USER+self.MONGODB_PASSWORD+"@"+self.MONGODB_SERVER+":"+self.MONGODB_PORT) 
            client = MongoClient('your_client') 
            self.db = client[self.MONGODB_DB]
        except Exception as e:
            #print self.MONGODB_USER+self.MONGODB_PASSWORD+"@"+self.MONGODB_SERVER+self.MONGODB_PORT
            #traceback.print_exc()
            print "sad"
     
    @classmethod
    def from_crawler(cls, crawler):
        #cls.MONGODB_SERVER = crawler.settings.get('SingleMONGODB_SERVER', 'localhost')
        #cls.MONGODB_PORT = crawler.settings.getint('SingleMONGODB_PORT', 27017)
        cls.MONGODB_SERVER = crawler.settings.get('SingleMONGODB_SERVER', 'your_server')
        cls.MONGODB_PORT = crawler.settings.getint('SingleMONGODB_PORT', "your_port")
        cls.MONGODB_DB = crawler.settings.get('SingleMONGODB_DB', 'house_fs')
        cls.MONGODB_USER = crawler.settings.get('SingleMONGODB_USER', 'your_user')
        cls.MONGODB_PASSWORD = crawler.settings.get('SingleMONGODB_PASSWORD', 'your_password')
        pipe = cls()
        pipe.crawler = crawler
        return pipe

    def process_item(self, item, spider):
        #if spider.name not in ['zufang']: 
        if spider.name not in ['58spider','ganjispider','baixingspider']:
            return item
        else: 
            if isinstance(item,HouseDetailItem):
                line = json.dumps(dict(item)) + "\n" 
                self.file_test_detail.write(line.decode('unicode_escape'))
                
                house_detail = {
                'title_detail':item.get('title_detail'),
                'price_detail':item.get('price_detail'),
                'pay_method':item.get('pay_method'),
                'house_type':item.get('house_type'),
                'xiaoqu':item.get('xiaoqu'),
                'address':item.get('address'),
                'config':item.get('config'),
                'broker_tel':item.get('broker_tel'),
                'broker_name':item.get('broker_name'),
                'description':item.get('description'),
                'publish_time':item.get('publish_time'),
                'pic_urls':item.get('pic_urls'),
                }
                self.db['house_detail'].insert(house_detail)
                
                return item                   
            else:
                line = json.dumps(dict(item)) + "\n" 
                self.file_test.write(line.decode('unicode_escape'))
                
                house_list = {
                'title':item.get('title'),
                'address':item.get('address'),
                'price':item.get('price'),
                'room':item.get('room'),
                'city':item.get('city'),
                'pic_url':item.get('pic_url'),
                }
                self.db['house_list'].insert(house_list)
                
                return item  
          
    def spider_closed(self, spider):
        self.file_test.close()
        self.file_test_detail.close()