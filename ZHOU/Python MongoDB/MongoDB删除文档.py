#删除文档使用delete_one()
#delete_one（）方法的第一个参数是query对象，用于定义删除的文档
#删除地址为“Mountain 21”的文档
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = {"address":"Mountain 21"}
mycol.delete_one(myquery)
for x in mycol.find():
    print(x)
#删除多个文档 delete_many()
#删除地址以字母S开头的所有文档
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = {"address":{"$regex":"^S"}}
x = mycol.delete_many(myquery)
print(x.deleted_count,"documents deleted.")
#删除所有文档
x = mycol.delete_many({})
print(x.deleted_count,"documents deleted.")