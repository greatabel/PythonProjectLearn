import sqlite3

#连接数据库，得到Connection 对象
conn = sqlite3.connect('example.db')
#创建Curosr 对象，用来执行SQL语句
cur = conn.cursor()
#创建数据表
cur.execute('CREATE TABLE person (name VARCHAR(32), age INT, sex char(1))')
#插入一条数据
cur.execute('INSERT INTO person VALUES (?,?,?)', ('刘硕', 34, 'M'))
#保存变更, commit 后数据才被实际写入数据库
conn.commit()
#关闭连接
conn.close()
