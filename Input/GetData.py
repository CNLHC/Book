#coding:u8
import requests
import json 
import sys
import os
import logging
Data_logger=logging.getLogger("GetData")
formatter=logging.Formatter(fmt="%(levelname)s-%(filename)s-%(funcName)s:%(message)s")
ch=logging.StreamHandler()
ch.setFormatter(formatter)
Data_logger.addHandler(ch)

proxies={ "https":"http://182.92.177.164:2333"}
def get_BookInfoPage(ISBN,t_proxies={}):
    '''
    从豆瓣的接口下载图书信息
    Input:
        ISBN:ISBN string of book
        *t_proxies:Dict contain proxies info that can be read by requests.get
    Output:
        Json file Str
        False
    '''
    page=requests.get("https://api.douban.com/v2/book/isbn/"+ISBN,proxies=t_proxies).text
    if page.find("rate_limit_exceeded2")>=0:
        Data_logger.warning("豆瓣接口调用次数已达到最大值")
        return False
    elif page.find("book_not_found")>=0:
        Data_logger.warning("豆瓣上未找到该书信息")
        return False
    else:
        return page

#info=get_BookInfoPage(isbn)
#t_formatjson=json.dumps(json.loads(info),indent=4,sort_keys=False,ensure_ascii=False)
#print unicode(t_formatjson)
    




