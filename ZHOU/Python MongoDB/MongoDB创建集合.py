#创建集合，请使用数据库对象并指定创建的集合的名称
#例题：创建一个名为customers的集合
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
#在MongoDB中，集合会获得内容之前不会被创建，所以这一步在MongoDB中不会显示customers的集合
#print(mydb.list_collection_names())  查看是否存在
#collist = mydb.list_collection_names()
#if "customers"in collist:
#    print("The collection exists.")
mydict = {"name":"Bill","address":"Highway 37"}
x = mycol.insert_one(mydict)   #这里添加了一个文档，这里没有显示，但是在MongoDB中可以看到
print(x.inserted_id)   #查看插入文档的 _id字段
#插入多个文档用insert_many()方法
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)