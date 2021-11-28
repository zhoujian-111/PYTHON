import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="zjdatabase"
)
#创建customers表
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")
mycursor.execute("SHOW TABLES")   #show tables来检查表是否存在
for x in mycursor:
  print(x)
#主键：为每一条记录创建一个具有唯一键的列
#通过PRIMARY KEY来完成
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR (255),address VARCHAR (255))")
#如果表存在，使用ALTER TABLE
mycursor = mydb.cursor()
mycursor.execute("LATER TABLE customers ADD COLUMN id INT UTO_INSREMENT PRIMARY KEY")
