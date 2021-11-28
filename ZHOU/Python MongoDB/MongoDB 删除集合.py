#使用drop（）方法删除在MongoDB中调用的表或者集合
#删除customers集合
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mycol.drop()