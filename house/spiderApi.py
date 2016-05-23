from house.spiders.test_spider import Tongcheng_Spider, Ganji_Spider
#, Baixing_Spider
#, Page_Spider

class customSpider_1(Tongcheng_Spider):
    name = "58spider"
    allowed_domains = ["bj.58.com"]
    start_urls = [
        "http://bj.58.com/chuzu/"
    ]

class customSpider_2(Ganji_Spider):
    name = "ganjispider"
    allowed_domains = ["bj.ganji.com"]
    start_urls = [
        "http://bj.ganji.com/fang1/"
    ]
    
#class customSpider_3(Baixing_Spider):
#    name = "baixingspider"
#    allowed_domains = ["beijing.baixing.com"]
#    start_urls = [
#        "http://beijing.baixing.com/zhengzu/"
#    ]
    
#class custom_Page_Spider(Page_Spider):
#    name = "page"
#    start_urls = [
#        "http://beijing.baixing.com/zhengzu/"
#    ]