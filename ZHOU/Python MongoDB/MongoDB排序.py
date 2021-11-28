#使用sort（）进行排序
#sort（）方法为“fieldname”（字段名称）提供一个参数，为“direction”（方向）提供一个参数默认方向是升序
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydoc = mycol.find().sort("name")
for x in mydoc:
    print(x)
#降序
mydoc = mycol.find().sort("name",-1)
for x in mydoc:
    print(x)