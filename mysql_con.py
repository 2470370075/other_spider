# 连接ubuntu上docker的mysql，传一个图片
import MySQLdb as mdb
import pymysql

conn=pymysql.connect(host='192.168.241.135',user='root',passwd='saber2014',db='test2')
cur = conn.cursor()

fin = open("./3.jpg",'rb')
img = fin.read()
fin.close()

cur.execute("INSERT INTO img1 (img) VALUES  (%s);", (img))

conn.commit()
cur.close()
conn.close()
