import redis


# 连接数据库
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('s', "hello world")
print(r.get('s'))