#coding:utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
#Happy Coding
import sqlite3
conn=sqlite3.connect('./book.db')
cursor = conn.execute("SELECT CoverURL,Title,Au1,publisher,ISBN  from main.book")

fp=open("DEMOD.html","w")

def Genhtml(k):
    base=''' 
			<li>
				<div class="bookimg">
					<img src='%s' height=150px>
				</div>
				<div class="bookinfo">
					<p>书名:%s</p>
					<p>作者:%s</p>
					<p>出版社:%s</p>
					<p>ISBN:%s</p>
				</div>
			</li>
			<hr>
        '''%(k[0],k[1],k[2],k[3],k[4])
    fp.write(base)

for i in cursor:
    LE=[]
    for k in i:
        LE.append(k)
    Genhtml(LE)


