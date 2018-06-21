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

def BookInfoByIsbn(ISBN,t_proxies=proxies,apiBaseUrl="https://api.douban.com/v2/book/isbn/"):
    '''
    从豆瓣的接口下载图书信息
    Input:
        ISBN: 书籍的ISBN **字符串**
        *apiBaseUrl: 豆瓣图书api的基地址
        *t_proxies: 代理服务器有关信息
    Output:
        Json file Str
        False
    '''
    reqobj=requests.get(apiBaseUrl+ISBN,proxies=t_proxies)
    if reqobj.status_code != 200:
        Data_logger.warning("远程接口错误")
        return dict({})
    content=reqobj.text

    try:
        return json.loads(content)

    except json.decoder.JSONDecodeError:
        Data_logger.error("json解析错误")
        return  {}

#info=get_BookInfoPage(isbn)
#t_formatjson=json.dumps(json.loads(info),indent=4,sort_keys=False,ensure_ascii=False)
#print unicode(t_formatjson)
    




