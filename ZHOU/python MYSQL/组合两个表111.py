import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="zjdatabase"
)
mycursor = mydb.cursor()
sql = "SELECT \
  users.name AS user,\
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#用left join 可以显示所有的记录，因为inner join只显示匹配的记录
sql = "SELECT \
  user.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON user.fav = products.id"
#right join 返回有键值的和没有键值的
sql ="SELECT \
  user.=s.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"