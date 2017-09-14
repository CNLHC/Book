#coding:utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
#Happy Coding
import json,sqlite3,os
import logging
####################logger setting####################
logger_Datatool=logging.getLogger("Databasetool")
formatter=logging.Formatter(fmt="%(levelname)s-%(filename)s-%(funcName)s:%(message)s")
ch=logging.StreamHandler()
ch.setFormatter(formatter)
logger_Datatool.addHandler(ch)

def HasDuplicate(sqlite_conn,ISBN):
    ''' 检查isbn是否已经在数据库中有记录
    Input:
        sqlite_conn: instance created from sqlite3.connect
        ISBN:   ISBN num (str)
    Output:
        True: has a duplicate
        False: do not have a duplicate
    '''
    cursor=sqlite_conn.cursor()
    cursor.execute("SELECT * FROM book WHERE ISBN = '%s'"%ISBN)
    index=0
    for row in cursor:
        index+=1
    if index==0:
        return False
    else:
        logger_Datatool.debug('Has Duplicate')
        return True
def atomexec(json_str,sqlite_conn):
    ''' 写入数据库文件,写入的字段是固定的.本函数不检查数据库中是否存在重复项
    写入的字段包括: isbn13,isbn10,images_url,title,pubdate,pages,publisher,Author
    Input:
        json_str : instance that can be decode by json.loads
        sqlite_conn : instance which return by sqlite3.connect() method
    Output:
        Nonsense
    '''
    a=json.loads(json_str)
    try:
        a=json.loads(json_str)
        try :
            AU1=a['author'][0]
        except: # if json file do not contain author name ,set it empty
            AU1=''
        try:
            sqlite_conn.execute('''
                    INSERT INTO main.book(ISBN,ISBN10,CoverURL,Title,pubDate,pages,publisher,Au1)\
        VALUES('%s','%s','%s','%s','%s','%s','%s','%s');'''%(a['isbn13'],a['isbn10'],a['images']['large'],a['title'],a['pubdate'],a['pages'],a['publisher'],AU1))
            logger_Datatool.info('书籍信息已添加')
        except sqlite3.IntegrityError: #if have storged a duplicate in the database 
            logger_Datatool.error('sqlite Integerity Error,may try to override an item')
    except : #Json decode Failed
        logger_Datatool.error('Json Load Error')
