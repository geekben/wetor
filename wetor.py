# coding:utf-8
'''
Created on 2013-12-20
@author: bn
'''

import time
import re
import os
import sys
import threading
from multiprocessing import Process
from string import capitalize

try: 
    input = raw_input
except NameError:
    pass

try:
    import urllib.request
    #import urllib.parse
except ImportError:
    import urllib
    urllib.request = __import__('urllib2')
    urllib.parse = __import__('urlparse')
 
urlopen = urllib.request.urlopen
request = urllib.request.Request

def get_content_from_url(url):
    attempts = 0
    content = ''

    while attempts < 5:
        #url_lock.acquire()
        try:
            content = urlopen(url).read().decode('utf-8', 'ignore')
            time.sleep(2)
            #url_lock.release()
            break
        except Exception as e:
            attempts += 1
            time.sleep(2)
            #url_lock.release()
            print(e)

    return content

def notify(url, target):
    html = get_content_from_url(url)
    retlist = re.findall('switch switch_on',html)
    if len(retlist) == 1:
        print "%s, you have got a message." % target
    global timer
    timer = threading.Timer(60, notify, [url, target])
    timer.start()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "ONE argument, the url needed"
        sys.exit(-1)
    #for ret in retlist:
    #    print ret
    timer = threading.Timer(1, notify, [sys.argv[1],"Luoben's phone"])
