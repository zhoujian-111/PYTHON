#encoding:utf-8
"""
@time:2021/11/17
@author:Byte Xiaochai
@software:PyCharm
@contact:2732472354@qq.com
@file：where 和order by排序
"""
#筛选结果用where进行筛选
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql="SELECT * FROM customers WHERE address = 'Park Lane 38'"
mycursor.execute(sql)
myresult= mycursor.fetchall()
for x in myresult:
    print(x)
#   %通配符  比如%way 表示以way结尾的词，way%表示以wey开头的词
#防止SQL注入mysql.connector模块具有转义查询值的方法
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql,adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
#ORDER BY语句按升序或者降序对结果进行排序
#ORDER BY 默认升序，DESC降序
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='root',
    database='mydatabase'
)
mycursor = mydb.cursor()
sql = "SELECT *FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
#降序
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='root',
    database='mydatabase'
)
mycursor = mydb.cursor()
sql = "SELECT *FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
#删除记录  DELETE FROM删除记录
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#防止SQL注入，在mysql.connector模块使用占位符%s来转义delete语句中的值
#sql = "SELECT * FROM customers WHERE address = %s"
