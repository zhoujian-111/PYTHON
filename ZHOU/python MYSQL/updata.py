#encoding:utf-8
"""
@time:2021/11/17
@author:Byte Xiaochai
@software:PyCharm
@contact:2732472354@qq.com
@file:update 更新数据库
"""
#更新表update
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="zjdatabase"
)
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
#注释一下    我上一个drop table 把mydatabase表中内容删除了
#我更换一个新的名为zjdatabase的表
