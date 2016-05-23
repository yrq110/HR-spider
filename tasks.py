# tasks.py
import time
from celery import Celery
import os
from datetime import timedelta
from celery.schedules import crontab
import subprocess
celery = Celery('tasks', broker='redis://127.0.0.1:6379/0')

@celery.task
def runSpider(command):
    line = subprocess.Popen(command)
    # line=os.popen(command)
    #print "%s" % command
    #return line
    print 'spider crawling'

# @celery.task    
# def fab(max):
    # print 'fab excuted'

celery.conf.update(
    CELERYBEAT_SCHEDULE = {
        'periodic 58spider': {
            'task': 'tasks.runSpider',
            'schedule': timedelta(seconds=10),
            'args': ('scrapy crawl 58spider',)
            },
        'periodic ganjispider': {
            'task': 'tasks.runSpider',
            'schedule': timedelta(seconds=10),
            'args': ('scrapy crawl ganjispider',)
            },
        # '10_second_tag': {
            # 'task': 'tasks.fab',
            # 'schedule': timedelta(seconds=10),
            # 'args': (10,)
            # },
        #'spider test':{
        #    'task':'tasks.excute'
        #    'schedule': crontab(),
        #    'args': (20,)
            }
        
    )
#if __name__ == '__main__':
#    celery.start()