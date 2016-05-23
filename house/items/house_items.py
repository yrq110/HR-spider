# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item 
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class TestItem(Item):
    url = Field()
    body = Field()
    headers = Field()
    status = Field()
    meta = Field()
    
class HouseItem(Item):
    title = Field()
    address = Field()
    price = Field()
    room = Field()
    city = Field()
    pic_url = Field()
    #spider = Field()
    #lbl = Field()

class HouseLoader(ItemLoader):
    default_item_class = HouseItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
    
class HouseDetailItem(Item):
    title_detail = Field()
    price_detail = Field()
    pay_method = Field()
    house_type = Field()
    xiaoqu = Field()
    address = Field()
    config = Field()
    broker_tel = Field()
    broker_name = Field()
    description = Field()
    publish_time = Field()
    pic_urls = Field()