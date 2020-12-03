"""App entry point."""

import flask_login
from flask import request
from flask import url_for
from flask import redirect
from flask import Blueprint, render_template

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from movie import create_app


app = create_app()
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ecology_readonly:Nthd1234@rm-bp1sf93ozy51616a65o.mysql.rds.aliyuncs.com:3306/ecology'
db = SQLAlchemy(app)





def get_db_data(table_number):
    if table_number == 1:
        result = db.session.execute('SELECT mc, zgbl, xjmc, xjzgbl FROM uf_gdcy' )
    elif table_number == 2:
        result = db.session.execute('SELECT gsmc, zgbl, xjgs, xjzg FROM uf_tzgs' )
    elif table_number == 3:
        result = db.session.execute('SELECT labelid, sType FROM accountmoremenuinfo' )
    for r in result:
        # print(r[0], '#' , r[1]) # Access by positional index
        # print(r['sType']) # Access by column name as a string
        r_dict = dict(r.items())
        print(r_dict)



@app.route("/org_chart", methods=["GET", "POST"])
def org_chart():
    print('-'*10, 'start')
    get_db_data(3)
    print('-'*10, 'end')
    
    charts = []
    return render_template(
        'org_chart.html',
        charts=charts,
        
    )


if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=False)

