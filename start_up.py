from threading import Thread  
import subprocess  
from Queue import Queue  


celery_worker = subprocess.Popen('celery -A tasks worker',shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
celery_beat = subprocess.Popen('celery -A tasks beat',shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
returncode = celery_worker.poll()
#while returncode is None:
        # line = celery_worker.stdout.readline()
        # returncode = celery_worker.poll()
        # line = line.strip()
        # print line
print returncode
# celery_worker.communicate()
# for line in celery_worker.stdout.readlines():
   # print line
   
   
# num_threads = 2
# spiders= ["58spider"]
# q = Queue()

# def crawl(i,queue):
    # while True:
        # spider = queue.get()
        # ret=subprocess.call('scrapy crawl %s' % spider,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        # queue.task_done()  
  
# start num_threads threads  
# for i in range(num_threads):  
    # t=Thread(target=crawl,args=(i,q))  
    # t.setDaemon(True)  
    # t.start()  
  
# for spider in spiders:  
    # q.put(spider)  
    
# print 'main thread waiting...'  
# q.join();
# print 'Done'  
# child = subprocess.Popen(["scrapy","crawl","58spider"],shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# for line in child.stdout.readlines():
   # print line
# spiders = ['58spider','ganjispider']
# for spider in spiders:
    # child = subprocess.Popen('scrapy crawl %s' % spider)
    # child.wait()
    # print('--------------------------------------------------------------------')
    # print('--------------------------%s Done--------------------------' % spider)
    # print('--------------------------------------------------------------------')
# print('--------------------------------------------------------------------')
# print("----------------------------Finished--------------------------------")
# print('--------------------------------------------------------------------')