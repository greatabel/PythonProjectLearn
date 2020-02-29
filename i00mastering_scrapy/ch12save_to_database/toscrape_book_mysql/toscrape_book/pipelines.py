# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from toscrape_book import settings

class ToscrapeBookPipeline(object):
    def process_item(self, item, spider):
        return item

class BookPipeline(object):
    review_rating_map = {
       'One':     1,
       'Two':     2,
       'Three':  3,
       'Four':   4,
       'Five':   5,
    }

    def process_item(self, item, spider):
        rating = item.get('review_rating')
        if rating:
            item['review_rating'] = self.review_rating_map[rating]
        return item

class MySQLPipeline:
    review_rating_map = {
       'One':     1,
       'Two':     2,
       'Three':  3,
       'Four':   4,
       'Five':   5,
      }





    def open_spider(self, spider):
      db = spider.settings.get('MYSQL_DB_NAME', 'scrapy_db')
      host = spider.settings.get('MYSQL_HOST', 'localhost')
      port = spider.settings.get('MYSQL_PORT', 3306)
      user = spider.settings.get('MYSQL_USER', 'test')
      passwd = spider.settings.get('MYSQL_PASSWORD', 'test1024')
      print('#'*20, 'open_spider')
      self.db_conn = pymysql.connect(host=host, port=port, db=db,
                            user=user, passwd=passwd, charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

      self.db_cur = self.db_conn.cursor()


    def close_spider(self, spider):
      # self.db_conn.commit()
      self.db_cur.close()
      self.db_conn.close()


    def process_item(self, item, spider):

      rating = item.get('review_rating')
      if rating:
          item['review_rating'] = self.review_rating_map[rating]

      review_num = item.get('review_num')
      if review_num:
          print('review_num=', review_num)
          item['review_num'] = int(review_num)

      stock = item.get('stock')
      if stock:
          print('stock=', stock)
          item['stock'] = int(stock)
      
      self.insert_db(item)

      return item


    def insert_db(self, item):
      values = (
          item['upc'],
          item['name'],
          item['price'],
          item['review_rating'],
          item['review_num'],
          item['stock'],
      )
      sql = "INSERT INTO books VALUES (%s,%s,%s,%s,%s,%s)"
      with self.db_conn.cursor() as cursor:
        cursor.execute(sql, values)
      self.db_conn.commit()
      # print('1'*20)
      # print('sql=', sql, 'values=', values)
      # self.db_cur.execute(sql, values)
      # print('2'*20)
      # self.db_conn.commit()
      # self.db_cur.close()
      # print('3'*20)
