#在MongoDB中，我们使用find和findOne方法来查找集合中的数据
#查找一项用find_one()
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
x = mycol.find_one()
print(x)
#查找全部用find()返回选择中的所有匹配项，find（）方法没有参数提供与MYSQL中的SELECT*相同的结果
#返回customers中集合的所有文档，并打印每个文档
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
for x in mycol.find():
    print(x)
#只返回某些字段  find（）参数可选
#若只返回姓名地址
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
#for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
 # print(x)
#排出address的结果
for x in mycol.find({},{"address": 0}):
    print(x)
