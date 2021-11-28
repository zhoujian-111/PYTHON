#encoding:utf-8
"""
@time:2021/11/17
@author:Byte Xiaochai
@software:PyCharm
@contact:2732472354@qq.com
@file:删除表
"""
#删除表
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)
#只在表存在的时候删除  可以使用IF EXISTS关键字
##mysql = "DROP TABLE IF EXISTS customers"
