#限制MongoDB中的结果，使用limit（）方法
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[",ydatabase"]
mycol = mydb["customers"]
myresult = mycol.find().limit(5)
for x in myresult:
    print(x)
