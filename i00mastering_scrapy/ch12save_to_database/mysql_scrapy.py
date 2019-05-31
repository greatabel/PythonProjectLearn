import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='test',
                             password='test1024',
                             db='scrapy_db',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE TABLE person (name VARCHAR(32), age INT, sex char(1)) \
         ENGINE=InnoDB DEFAULT CHARSET=utf8')

        # Create a new record
        sql = "INSERT INTO person VALUES (%s,%s,%s)"
        cursor.execute(sql, ('刘硕', 34, 'M'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `name`, `age` FROM `person` WHERE `name`=%s"
        cursor.execute(sql, ('刘硕',))
        result = cursor.fetchone()
        print('r=', result)
finally:
    connection.close()