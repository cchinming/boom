#-*- coding:utf-8 -*-
#---------------------------------
#FILENAME:UserAgent.py
#目的：爬取旅游数据
#环境：Ubuntu14 python3.x/python2.x
#FILE:UserAgent.py
#TIME:20170923
#---------------------------------
import random

User_Agent=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36",
              ]  
  
HEADERS = {  
    'User-Agent':  User_Agent[random.randint(0,len(User_Agent)-1)],  
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',  
    'Accept-Encoding': 'gzip, deflate, br',  
    'Cookie': '',  
    'Connection': 'keep-alive',  
    'Pragma': 'no-cache',  
    'Cache-Control': 'no-cache'  
} 
