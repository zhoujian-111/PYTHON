#encoding:utf-8
"""
@time:2021/11/17
@author:Byte Xiaochai
@software:PyCharm
@contact:2732472354@qq.com
@file:limit 限制查询返回记录数
"""
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")
#mycursor.execute("SHOW TABLES")   #show tables来检查表是否存在
#for x in mycursor:
 # print(x)
sql = "INSERT INTO customers (name ,address) VALUE (%s,%s)"   #插入表
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted.")
#
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#从位置3开始返回5条记录
#mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")