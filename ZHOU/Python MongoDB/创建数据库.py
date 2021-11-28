#首先安装MongoDB
import pymongo  #导入pymongo 测试是否完成
#要在MongoDB中创建数据库，首先创建MongoClient对象，然后用正确的ip地址和要创建的数据库的名称指定连接URL
#如果数据库不存在，则MongoDB将创建数据库并建立连接
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
#检查数据库是否存在
print(myclient.list_database_names())
#检查mydatabase是否存在
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")