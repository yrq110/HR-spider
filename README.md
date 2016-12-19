# house-spider
crawl data from Internet for [HouseRadar](https://github.com/yrq110/HouseRadar).

## Ability
crawl data of rental room from [58](http://bj.58.com/chuzu/) and [Ganji](http://bj.ganji.com/fang1/).

## Requirements
* python 2.7
* scrapy 1.0.1
* celery 3.1.18
* beautifulsoup4
* pymongo 3.0
* mongoDB 3.0
* redis 2.4.5

## Bonus
* `test.json`and`test_detail.json` - sample data of crawling.
* `json2txt.py` - convert json to text.
* `jsonQuChong.py` - filter duplicate data in json file according to value of `title`.

## Run
1.Set your own mongo server in `house_pipe.py`and`settings.py`.

> Note:It's very importment, or you can store data locally.

2.Run spider:
```
scrapy crawl spider_name
```

## Optional
1.Run redis:
```
redis-server.exe redis.conf
```
2.Run celery task queue：
```
1.run redis
2.run a worker:
  celery -A tasks worker
3.run a beat:
  celery -A tasks beat
```
In linux you can use `celery -A proj worker -B `.
