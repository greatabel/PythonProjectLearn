from flask import Flask, request
from flask import render_template
from flask import make_response

import sqlite3
from flask import g


app = Flask(__name__)
app.debug = True

# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
DATABASE = 'campus_data.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/scp2/')
@app.route('/scp2/<index_id>')
def scp2(index_id=""):
    # input :http://www.baidu.com
    query_value = request.args.get('query')
    index =  " is here"
    teacher_works = []
    for t in query_db('select * from teacher_work'):
        print(t[0],'#'*10, t[1])
        teacher_works.append(t)
    r = make_response(
        render_template('scp2.html', query_value=query_value,index=index, teacher_works=teacher_works)
        )
    # r.headers.set('Content-Security-Policy', "default-src 'unsafe-inline' 'unsafe-eval' 'self'  ")
    return r


@app.route('/scp3/')
@app.route('/scp3/<index_id>')
def scp3(index_id=""):
    # input :http://www.baidu.com
    query_value = request.args.get('query')
    index =  " is here"

    teacher_works = []
    for t in query_db('select * from teacher_work'):
        print(t[0],'#'*10, t[1])
        teacher_works.append(t)

    r = make_response(
        render_template('scp3.html', query_value=query_value,index=index,teacher_works=teacher_works)
        )
    r.headers.set('Content-Security-Policy', "default-src * 'unsafe-inline'; connect-src 'self' 'nonce-987654321' ")
    return r

if __name__ == '__main__':
    # app.run()
    print('#'*30, 'target website is working')
    app.run(host="localhost", port=8000, threaded=False)