import pymysql
from twisted.enterprise import adbapi
from twisted.internet import reactor
 
 
def go_insert(cursor, sql):
    # 对数据库进行插入操作，并不需要commit，twisted会自动帮我commit
    try:
        for i in range(10):
            data = ('person%s' % i, 215, 'M')
            cursor.execute(sql, data)
    except Exception as e:
        print(e)
 
 
def handle_error(failure):
    # 打印错误
    if failure:
        print(failure)
 
 
if __name__ == '__main__':
    # 数据库基本配置
    db_settings = {
        'host': 'localhost',
        'db': 'scrapy_db',
        'user': 'test',
        'password': 'test1024',
        'charset': 'utf8',
        'use_unicode': True
    }
    # sql语句模版
    insert_sql = 'insert into person values (%s, %s, %s)'
     
    # 普通方法插入数据
    # conn = pymysql.connect(**db_settings)
    # cursor = conn.cursor()
    # cursor.execute(insert_sql, '1')
    # conn.commit()
     
    try:
        # 生成连接池
        db_conn = adbapi.ConnectionPool('pymysql', **db_settings)
        # 通过连接池执行具体的sql操作，返回一个对象
        query = db_conn.runInteraction(go_insert, insert_sql)
        # 对错误信息进行提示处理
        query.addCallbacks(handle_error)
    except Exception as e:
        print(e)
     
    # 定时，给4秒时间让twisted异步框架完成数据库插入异步操作，没有定时什么都不会做
    reactor.callLater(4, reactor.stop)
    reactor.run()