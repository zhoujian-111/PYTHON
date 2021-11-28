#encoding:utf-8
"""
@time:2021/11/17
@author:Byte Xiaochai
@software:PyCharm
@contact:2732472354@qq.com
@file:Join
"""
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="zjdatabase"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE users(id VARCHAR (255),name VARCHAR (255),fav VARCHAR (255))")
sql = "INSERT INTO users(id,name,fav) VALUES(%s,%s,%s)"
val =[
  ('1','John','154'),
  ('2','Peter','154'),
  ('3','Amy','155'),
  ('4','Hannah',' '),
  ('5','Michael',' ')
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")
#mycursor.execute("CREATE TABLE products(id VARCHAR (255),name VARCHAR (255))")
sql = "INSERT INTO users(id,name) VALUES(%s,%s)"
val =[
  ('154','Chocolate Heaven'),
  ('155','Tasty Lemons'),
  ('156','Vanilla Dreams')

]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")
