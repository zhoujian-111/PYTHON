#插入单行用mydb.commit()
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
#插入多行用mycursor.executemany（)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name ,address) VALUE (%s,%s)"
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

#获取已经插入的id
#插入一行，并返回id
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="zjdatabase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

#从表中选择结果
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT *FROM customers")
myresult = mycursor.fetchall()  #fetchall 返回多个元组   fetchone（）返回单个元组
for x in myresult:
  print(x)