#coding:utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
#Happy Coding
import json,sqlite3
def atomexec(json_file,sqlite_conn):
    '''
    写入数据库文件,写入的字段是固定的
    包括: isbn13,isbn10,images_url,title,pubdate,pages,publisher,Author
    json_file : instance that can be decode by json.loads
    sqlite_conn : instance which return by sqlite3.connect() method
    '''
    try:
        a=json.loads(json_file)
        try :
            AU1=a['author'][0]
        except: # if json file do not contain author name ,set it empty
            AU1=''
        try:
            sqlite_conn.execute('''
                    INSERT INTO main.book(ISBN,ISBN10,CoverURL,Title,pubDate,pages,publisher,Au1)\
        VALUES('%s','%s','%s','%s','%s','%s','%s','%s');'''%(a['isbn13'],a['isbn10'],a['images']['large'],a['title'],a['pubdate'],a['pages'],a['publisher'],AU1))
        except sqlite3.IntegrityError: #if have storged a duplicate in the database 
            return False
    except IOError: #Json decode Failed
        return False

conn=sqlite3.connect('./book.db')
