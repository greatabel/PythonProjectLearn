"""App entry point."""

import os
from flask import request
from flask import url_for
from flask import redirect
from flask import Blueprint, render_template

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import json
from flask import jsonify

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
    return result
    # for r in result:
    #     # print(r[0], '#' , r[1]) # Access by positional index
    #     # print(r['sType']) # Access by column name as a string
    #     r_dict = dict(r.items())
    #     print(r_dict)



@app.route("/relationship", methods=['GET'])
def relationship():

    # static/data/test_data.json
    filename = os.path.join(app.static_folder, 'data.json')

    with open(filename) as test_file:
        d = json.load(test_file)

    # d = {
    # "downward": {
    #     "direction": "downward",
    #     "name": "origin",
    #     "children": [
    #         {
    #             "name": "珠海市华裕发展集团有限公司",
    #             "amount": "100",
    #             "ratio": "100%",
    #             "hasHumanholding":"true",
    #             "hasChildren":"true",
    #             "isExpand": "false",
    #             "children": [
    #                 {
    #                     "name": "珠海市睿诚商务信息咨询有限公司",
    #                     "hasHumanholding":"false",
    #                     "hasChildren":"true",
    #                     "amount": "100",
    #                     "ratio": "100%",
    #                     "children": []
    #                 },
    #                 {
    #                     "name": "珠海市裕恒商贸有限公司",
    #                     "hasHumanholding":"false",
    #                     "hasChildren":"true",
    #                     "amount": "100",
    #                     "ratio": "55%",
    #                     "children": []
    #                 },
    #                 {
    #                     "name": "珠海经济特区腾辉发展有限公司",
    #                     "hasHumanholding":"false",
    #                     "hasChildren":"true",
    #                     "amount": "100",
    #                     "ratio": "91%",
    #                     "children": []
    #                 }
    #             ]
    #         },
    #         {
    #             "name": "Abel测试公司1",
    #             "amount": "100",
    #             "ratio": "55%",
    #             "hasHumanholding":"true",
    #             "hasChildren":"true",
    #             "isExpand": "false",
    #             "children": [
    #                 {
    #                     "name": "公司名字",
    #                     "hasHumanholding":"false",
    #                     "hasChildren":"true",
    #                     "amount": "100",
    #                     "ratio": "55%",
    #                     "children": []
    #                 },
    #                 {
    #                     "name": "公司名字",
    #                     "hasHumanholding":"false",
    #                     "hasChildren":"true",
    #                     "amount": "100",
    #                     "ratio": "55%",
    #                     "children": []
    #                 }
    #             ]
    #         },
    #         {
    #             "name": "Abel测试公司2",
    #             "amount": "100",
    #             "ratio": "55%",
    #             "hasHumanholding":"true",
    #             "hasChildren":"true",
    #             "isExpand": "false",
    #             "children": [
    #                 {
    #                     "name": "公司名字",
    #                     "hasHumanholding":"false",
    #                     "hasChildren":"true",
    #                     "amount": "100",
    #                     "ratio": "55%",
    #                     "children": []
    #                 },
    #                 {
    #                     "name": "公司名字",
    #                     "hasHumanholding":"false",
    #                     "hasChildren":"true",
    #                     "amount": "100",
    #                     "ratio": "55%",
    #                     "children": []
    #                 }
    #             ]
    #         },
    #         {
    #             "name": "Abel测试公司3",
    #             "hasHumanholding":"false",
    #             "hasChildren":"true",
    #             "amount": "100",
    #             "ratio": "55%",
    #             "children": []
    #         },
    #         {
    #             "name": "Abel测试公司4",
    #             "hasHumanholding":"false",
    #             "hasChildren":"true",
    #             "isExpand": "false",
    #             "amount": "100",
    #             "ratio": "55%",
    #             "children": [
    #                 {
    #                     "name": "公司或股东名字",
    #                     "hasHumanholding":"false",
    #                     "amount": "100",
    #                     "ratio": "55%",
    #                     "children": []
    #                 },
    #                 {
    #                     "name": "公司或股东名字",
    #                     "hasHumanholding":"false",
    #                     "amount": "100",
    #                     "ratio": "55%",
    #                     "children": []
    #                 },
    #                 {
    #                     "name": "公司或股东名字",
    #                     "hasHumanholding":"false",
    #                     "amount": "100",
    #                     "ratio": "55%",
    #                     "children": []
    #                 },
    #                 {
    #                     "name": "公司或股东名字",
    #                     "hasHumanholding":"false",
    #                     "amount": "100",
    #                     "ratio": "55%",
    #                     "children": []
    #                 }
    #             ]
    #         }
    #     ]
    # },
    # "upward": {
    #     "direction": "upward",
    #     "name": "origin",
    #     "children": [
                    
    #                 {
    #                     "name": "达海控股集团有限公司",
    #                     "hasHumanholding":"false",
    #                     "isExpand": "false",
    #                     "amount": "100",
    #                     "ratio": "2.45416%",
    #                     "children": [
    #                         {
    #                             "name": "张昕",
    #                             "hasHumanholding":"false",
    #                             "amount": "100",
    #                             "ratio": "1.14749%",
    #                             "children": []
    #                         },
    #                         {
    #                             "name": "陈卫新",
    #                             "hasHumanholding":"false",
    #                             "amount": "100",
    #                             "ratio": "1.14749%",
    #                             "children": []
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "name": "耿裕华",
    #                     "hasHumanholding":"false",
    #                     "amount": "100",
    #                     "ratio": "2.9499%",
    #                     "children": []
    #                 },
    #                 {
    #                     "name": "姚富新",
    #                     "hasHumanholding":"false",
    #                     "amount": "100",
    #                     "ratio": "1.8437%",
    #                     "children": []
    #                 },
    #                 {
    #                     "name": "张建忠",
    #                     "hasHumanholding":"false",
    #                     "amount": "100",
    #                     "ratio": "1.4749%",
    #                     "children": []
    #                 }
    #             ]
    #     }
    # }
    print(type(d), '#'*10)
    return d


@app.route("/org_chart", methods=["GET", "POST"])
def org_chart():


    charts = []
    return render_template(
        'org_chart.html',
        charts=charts,
        
    )


if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=False)

