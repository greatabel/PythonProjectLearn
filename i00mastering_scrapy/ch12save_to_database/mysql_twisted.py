from twisted.internet import reactor, defer
from twisted.enterprise import adbapi
import threading
import pymysql
from random import randint


dbpool = adbapi.ConnectionPool('pymysql', host='localhost', database='scrapy_db',
                      user='test', password='test1024', charset='utf8')


def insert_db(cursor, sql):
    for i in range(10):
        print('i=', i)
        item = ('person%s' % i, randint(0, 100-1), 'M')
        print('In Thread:', threading.get_ident())
        
        cursor.execute(sql, item)



if __name__ == '__main__':
    sql = 'insert into person values (%s, %s, %s)'
    dbpool.runInteraction(insert_db, sql)

    # 定时，给4秒时间让twisted异步框架完成数据库插入异步操作，没有定时什么都不会做
    reactor.callLater(4, reactor.stop)
    reactor.run()