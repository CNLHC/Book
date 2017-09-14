#coding:utf-8
import sys 
import Databasetool,sqlite3
import GetData
import logging
reload(sys)
sys.setdefaultencoding('utf-8')
#Happy Coding
#====================logger setting====================
CLI_logger=logging.getLogger("CLI")
CLI_logger.addHandler(logging.StreamHandler())
CLI_logger.setLevel(logging.INFO)
GetData.Data_logger.setLevel(logging.INFO)
Databasetool.logger_Datatool.setLevel(logging.INFO)
#========================================
conn=sqlite3.connect('../book.db')
ERROR_BOOK=open('./ERROR','a')
while 1:
    ISBN=raw_input("Input ISBN:")    
    if not Databasetool.HasDuplicate(conn,ISBN):
        f=GetData.get_BookInfoPage(ISBN)
        if f is not False:
            Databasetool.atomexec(json_str=f,sqlite_conn=conn)
            conn.commit()
        else :
            ERROR_BOOK.write(ISBN+'\n')
            CLI_logger.info("错误书籍数据已添加")
    else:
        CLI_logger.info("数据库中已有数据")
    print "========================"
        

        
        

