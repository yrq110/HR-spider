import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor
from house.items.house_items import HouseItem, HouseLoader, HouseDetailItem, TestItem
from bs4 import BeautifulSoup
from hashlib import md5
#md5(item['link']).hexdigest()

#class Page_Spider(scrapy.spiders):
    
#    def parse(self, response):
#        item = HouseDetailItem()
#        item['title_detail'] = response.body
#        yield item    


class Baixing_Spider(Spider):
    name = 'baixingspider'
    start_urls = [
        'http://beijing.baixing.com/zhengzu/'
        ]
        
    def parse(self, response): 
        soup = BeautifulSoup(response.body)
        [script.extract() for script in soup.findAll('script')]
        [style.extract() for style in soup.findAll('style')]
        soup.prettify()
        reg1 = re.compile("<[^>]*>")
        content = reg1.sub('',soup.prettify())
        item = TestItem()
        item['url'] = response.url
        item['headers'] = response.headers
        item['status'] = response.status
        item['meta'] = response.meta
        item['body'] = response.body
        yield item


class Ganji_Spider(CrawlSpider):

#    name = "ganjispider"
    allowed_domains = ["bj.ganji.com"]
    start_urls = [
        "http://bj.ganji.com/fang1/"
    ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="pageBox"]/ul[@class]')), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="info-title"]/a[@href]')), callback='parse_detail_item', follow=True),
    )
    
    def parse_item(self, response):
        for block in response.xpath('//li[@class="list-img clearfix"]'):
            el = HouseLoader(selector=block)
            #title = BeautifulSoup(block).find("div",class_="info-title").get_text()
            #el.add_value('title',title)
            el.add_xpath('title', 'div[@class="list-mod4"]/div[@class="info-title"]/a[@class]/text()')
            el.add_xpath('address','div[@class="list-mod4"]/div[@class="list-mod2"]/div[@class="list-word"]/span[@class]/a[@class="adds"]/text()')
            #el.add_xpath('lbl', 'div[@class="list-mod4"]/div[@class="list-mod2"]/div[@class="lbl-box clearfix"]/span[@class]/text()')
            el.add_xpath('price','div[@class="list-mod4"]/div[@class="list-mod3 clearfix"]/p[@class]/em[@class="sale-price"]/text()')
            el.add_xpath('room','div[@class="list-mod4"]/div[@class="list-mod2"]/p[@class="list-word"]/span[@class="js-huxing"]/text()')
            el.add_value('city','Beijing')
            pic_url = block.xpath('//div[@class="list-mod1"]/a[@class="img-box"]').re('src="(.*?)"')
            el.add_value('pic_url',pic_url)
            yield el.load_item()
            
    def parse_detail_item(self, response):
        item = HouseDetailItem()
        item['title_detail'] = response.xpath('//div[@class]/h1[@class]/text()').extract()
        item['price_detail'] = response.xpath('//b[@class="basic-info-price fl"]/text()').extract()
        item['house_type'] = response.xpath('//div[@class="basic-info"]/ul[@class]/li[2]/text()').extract()[0].replace('\t','').replace('\n','').replace(' ','').replace('\r','')  
        item['xiaoqu'] = response.xpath('//div[@class="spc-cont"]/a[@href]/text()').extract()[0].replace('\t','').replace('\n','').replace(' ','').replace('\r','')
        item['address'] = response.xpath('//span[@class="addr-area"]/text()').extract()
        item['config'] = response.xpath('//li[@class="peizhi"]/p/text()').extract()[0].replace('\t','').replace('\n','').replace(' ','').replace('\r','')
        item['broker_tel'] = response.xpath('//span[@class="contact-col"]/em[@class="contact-mobile"]/text()').extract()
        item['broker_name'] = response.xpath('//span[@class="contact-col"]/i[@class="fc-gray9"]/text()').extract()
        item['description'] = BeautifulSoup(response.body,"lxml").find("div",class_="summary-cont").get_text().replace('\t','').replace('\n','').replace(' ','').replace('\r','')
        item['publish_time'] = response.xpath('//ul[@class]/li/i[@class="f10 pr-5"]/text()').extract()
        item['pic_urls'] = response.xpath('//div[@class="cont-box pics"]').re('src="(.*?)"')
        #item['url'] = response.url
        #item['pay_method'] = response.xpath('//span[@class="f1"]/text()').extract()[0].replace('\t','').replace('\n','').replace(' ','').replace('\r','')
        yield item 





class Tongcheng_Spider(CrawlSpider):

#    name = "58spider"
    allowed_domains = ["bj.58.com"]
    start_urls = [
        "http://bj.58.com/chuzu/"
    ]
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="pager"]')), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//td[@class="t qj-rentd"]/a[@href]')), callback='parse_detail_item', follow=True),
    )
    
    def parse_item(self, response):
        for block in response.xpath('//tr[@logr]'):
            el = HouseLoader(selector=block)
            el.add_xpath('title', 'td[@class="t qj-rentd"]/a[@href]/text()')
            room = block.re('<span class="showroom">(.*?)</span>')
            el.add_value('room',room)
            el.add_xpath('price','td/b[@class="pri"]/text()')
            address = block.re('class="a_xq1">(.*?)</a>(.*?)')[0]
            el.add_value('address',address)
            el.add_value('city','Beijing')
            yield el.load_item()
            
    def parse_detail_item(self, response):
        item = HouseDetailItem()
        item['title_detail'] = response.xpath('//title/text()').extract()[0].replace('\t','').replace('\n','').replace(' ','')
        item['price_detail'] = response.xpath('//em[@class="house-price"]/text()').extract()
        item['pay_method'] = response.xpath('//span[@class="pay-method f16 c70"]/text()').extract()
        item['house_type'] = response.xpath('//div[@class="fl house-type c70"]/text()').extract()[0].replace('\t','').replace('\n','').replace(' ','').replace('\r','')
        item['xiaoqu'] = response.xpath('//div[@class="fl xiaoqu c70"]/a[@href]/text()').extract()
        item['address'] = response.xpath('//li[@class="house-primary-content-li clearfix"]/div[@class="fl c70"]/text()').extract()[0].replace('\t','').replace('\n','').replace(' ','').replace('\r','')
        item['config'] = response.xpath('//li[@class="house-primary-content-li clearfix broker-config"]/div[@class="fl c70"]/span[@class]/text()').extract()
        item['broker_tel'] = response.xpath('//div[@class="fl tel cfff"]/span[@class="tel-num pl30 f30"]/text()').extract()
        item['broker_name'] = response.xpath('//div[@class="fl tel cfff"]/span[@class="f18 pl20"]/text()').extract()
        item['description'] = BeautifulSoup(response.body,"lxml").find("div",class_="description-content").get_text().replace('\t','').replace('\n','').replace(' ','').replace('\r','')
        #item['url'] = response.url
        yield item