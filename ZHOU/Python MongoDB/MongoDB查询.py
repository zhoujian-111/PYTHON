#在集合中查找文档时，能够使用query对象过滤结果 find（）方法第一个参数是query对象，用于限定搜索
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = {"address":"Park Lane 38"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
#高级查询，可以使用修饰符作为查询对象中的值
#例如要查找“address”字段以字母S或者更高开头的文档 请使用大于修饰符{“$gt”:"S"}:
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = {"address":{"$gt":"S"}}
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
#用正则表达式来筛选
#正则表达式只能用于查询字符串
#如果只查找address字段以字母S开头的文档，使用正则表达式{"#regex":"^S"}
myquery = {"address":{"$regex":"^S"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)