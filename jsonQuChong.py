#coding=utf-8
import json
import codecs
def jsonQuChong(inFile, outFile):
    file_in = codecs.open(inFile, 'r', encoding='utf-8') 
    file_out = codecs.open(outFile, 'w+', encoding='utf-8')
    num = .0
    dupnum = .0
    filter = set()
    for line in file_in.readlines():
        dicline = json.loads(line)
        if dicline['title'] in filter:
            print 'duplicate'
            dupnum += 1
            num += 1
        else:
            #print dicline['title']
            filter.add(dicline['title'])
            data = json.dumps(dicline) + "\n" 
            file_out.write(data.decode('unicode_escape'))
            num += 1
    proportion = dupnum*100/num
    print "dupnum is " + str(dupnum)
    print "data is " + str(num-dupnum)
    print "num is " + str(num)
    print "proportion of dupObj is " + str(proportion) + "%"
    file_in.close()
    file_out.close()

if __name__=='__main__':
    jsonQuChong('test.json','output.json')
