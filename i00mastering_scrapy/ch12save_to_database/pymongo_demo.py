from pymongo import MongoClient


# 连接 mongodb，得到一个客户端
client = MongoClient('mongodb://localhost:27017')

# 获取名为 scrapy_db 数据库对象
db = client.scrapy_db

# 获取名为 person的集合对象
collection = db.person的集合对象

doc = {
    'name': 'tester',
    'age': 33,
    'sex': 'M',
}

collection.insert_one(doc)

client.close()