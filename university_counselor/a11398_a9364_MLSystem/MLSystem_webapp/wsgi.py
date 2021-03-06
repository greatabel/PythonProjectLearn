"""App entry point."""
import os
import random
import datetime
import time
import json

import flask_login
from flask import request
from flask import url_for
from flask import redirect
from flask import Blueprint, render_template as rt

from flask import Flask, Response, session
from flask import Blueprint,  jsonify
from flask_sqlalchemy import SQLAlchemy

from movie import create_app
from movie.domain.model import Director, User, Review, Movie

from sqlitedict import SqliteDict
from flask_docs import ApiDoc

app = create_app()
app.secret_key = "ABCabc123"
app.debug = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

# 本地加载
# app.config['API_DOC_CDN'] = False

# 禁用文档页面
# app.config['API_DOC_ENABLE'] = False

# 需要显示文档的 Api
app.config["API_DOC_MEMBER"] = ["api", "platform"]

ApiDoc(app, title="Sample App", version="1.0.0")

api = Blueprint("api", __name__)
platform = Blueprint("platform", __name__)

#--结束文档设置 --

db = SQLAlchemy(app)

stored_user = None


login_manager = flask_login.LoginManager(app)
# user_pass = {}

# https://pypi.org/project/sqlitedict/
user_pass = SqliteDict('my_db.sqlite', autocommit=True)



"""
为将来做数据统计和可视化做准备的代码，暂时没有用到，暂时可以忽略
"""


@api.route("/statistics", methods=["GET"])
def relationship():
    """Add some data
    @@@
    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    | title |  false   |    body      | str  | blog title    |
    | name  |  false   |    body      | str  | person's name |
    ### request
    ```json
    {"title": "xxx", "name": "xxx"}
    ```
    ### return
    ```json
    {"code": xxxx, "msg": "xxx", "data": null}
    ```
    """

    filename = os.path.join(app.static_folder, "data.json")
    with open(filename) as test_file:
        d = json.load(test_file)
    print(type(d), "#" * 10, d)
    return d


"""
使用 https://flask-login.readthedocs.io/en/0.3.1/ 
库进行用户登录凭证的验证
"""


@login_manager.user_loader
def load_user(email):
    return user_pass.get(email, None)


"""
登录相关后端接口，验证凭证，根据是否通过进行跳转和提示
"""


@api.route("/login", methods=["POST", "GET"])
def login():
    """login function

    login function 

    Args:
        email, password

    Returns:
        edirect "home_bp.home"
    """
    global stored_user
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = user_pass.get(email, None)
    if stored_user and password == stored_user.password:

        flask_login.login_user(stored_user)
        session['username'] =stored_user.user_name
        print(stored_user.is_active, "login")
        return redirect(url_for("review"))
    else:
        print("login fail")
    return redirect(url_for("home_bp.home", pagenum=1))


"""
登录相关后端接口，验证凭证，根据是否通过进行跳转和提示
"""


@api.route("/register", methods=["POST"])
def register():
    """register function

    @@@
    #### args

    | args | nullable | type | remark |
    |--------|--------|--------|--------|
    |    email    |    password    |    password2   
   
    #### return
    - ##### json
    > redirect(url_for("home_bp.home", pagenum=1))
    @@@
    """
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        session['username'] = email
        return redirect(url_for("home_bp.home", pagenum=1))
    # if DB.get_user(email):
    if email in user_pass:
        print("already existed user")
        return redirect(url_for("home_bp.home", pagenum=1))
    # salt = PH.get_salt()
    # hashed = PH.get_hash(pw1 + salt)
    print("register", email, pw1)
    user = User(email, pw1)
    user_pass[email] = user
    print("register", user_pass, "#" * 5)
    return redirect(url_for("home_bp.home", pagenum=1))


"""
登出网站相关后端接口，根据是否通过进行跳转和提示
"""


@api.route("/logout")
def logout():
    """logout function

    @@@
    #### args


   
    #### return
    - ##### json
    > redirect(url_for("home_bp.home", pagenum=1))
    @@@
    """
    flask_login.logout_user()
    return redirect(url_for("home_bp.home", pagenum=1))


reviews = []
data_visual_list = None
model_name_list = None
"""
另外一个机器学习项目示例的数据展示准备，这次没有启用，暂时可以忽略
"""


# https://stackoverflow.com/questions/40566757/how-to-get-multiple-selected-items-from-form-in-flask
@app.route("/review", methods=["GET", "POST"])
@flask_login.login_required
def review():
    global data_visual_list, model_name_list
    if request.method == "POST":
        data_visual_list = request.form.getlist('data_visual')
        model_name_list = request.form.getlist('model_name')
        print(data_visual_list, '#'*5, model_name_list)
        # model_name = request.form["model_name"]
        # data_visual = request.form["data_visual"]
        # print('#'*10, data_visual, model_name)

        # 由于我们模型以及训练成功，模拟模拟训练不同的时间
        time.sleep(random.randint(1, 3))
        return redirect(url_for("result"))
    return rt(
        "review.html",
        reviews=reviews,
    )


@app.route("/result", methods=["GET"])
@flask_login.login_required
def result():
    global data_visual_list, model_name_list
    # if request.method == "POST":

    # images = ['0_distplot_saleprice', '1Contrast heat map', '2price_lotarea', '3importance']
    rand = random.uniform(0, 0.1)
    results_dict = {
    'LR模型': [ 0.138401+rand, 0.0112],
    'Ridge模型': [ 0.129672, 0.0126+rand],
    'Lasso模型': [ 0.137959+rand, 0.0096],

    }
    results = []
    for item in model_name_list:
        results.append((item, results_dict[item] ))

    historys = user_pass.get('train_history', None)
    print('historys=', historys, '#'*10)
    from time import gmtime, strftime
    nowdt = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    record = (session['username'], nowdt, data_visual_list, results)

    if historys is None:
        historys = []
        print('historys is emppty' )        
        user_pass['train_history'] = [record]
    else:
        import copy
        new_historys = copy.deepcopy(historys)
        # new_historys.append(record)
        new_historys.insert(0,record)
        user_pass['train_history'] = new_historys

    return rt(
        "result.html",
        images=data_visual_list,
        results=results,
        historys=historys
    )



@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized"


# --------------------------


"""
上传后数据相关页面的后台支持接口
"""


@app.route("/", methods=["GET"])
def index():
    return rt("./index.html")


"""
上传后数据上传的真正接受接口
"""


@app.route("/file/upload", methods=["POST"])
def upload_part():  # 接收前端上传的一个分片
    task = request.form.get("task_id")  # 获取文件的唯一标识符
    chunk = request.form.get("chunk", 0)  # 获取该分片在所有分片中的序号
    filename = "%s%s" % (task, chunk)  # 构造该分片的唯一标识符

    upload_file = request.files["file"]
    upload_file.save("./upload/%s" % filename)  # 保存分片到本地
    return rt("./index.html")


"""
上传后数据上传分片的合并功能真正接受接口
"""


@app.route("/file/merge", methods=["GET"])
def upload_success():  # 按序读出分片内容，并写入新文件
    target_filename = request.args.get("filename")  # 获取上传文件的文件名
    task = request.args.get("task_id")  # 获取文件的唯一标识符
    chunk = 0  # 分片序号
    with open("./upload/%s" % target_filename, "wb") as target_file:  # 创建新文件
        while True:
            try:
                filename = "./upload/%s%d" % (task, chunk)
                source_file = open(filename, "rb")  # 按序打开每个分片
                target_file.write(source_file.read())  # 读取分片内容写入新文件
                source_file.close()
            except IOError as msg:
                break

            chunk += 1
            os.remove(filename)  # 删除该分片，节约空间

    return rt("./index.html")


"""
上传后数据展示页面的后台支持接口
"""


@app.route("/file/list", methods=["GET"])
def file_list():
    files = os.listdir("./upload/")  # 获取文件目录
    # print(type(files))
    files.remove(".DS_Store")
    # files = map(lambda x: x if isinstance(x, unicode) else x.decode('utf-8'), files)  # 注意编码
    return rt("./list.html", files=files)


"""
上传后数据下载功能 的后台支持接口
"""


@app.route("/file/download/<filename>", methods=["GET"])
def file_download(filename):
    def send_chunk():  # 流式读取
        store_path = "./upload/%s" % filename
        with open(store_path, "rb") as target_file:
            while True:
                chunk = target_file.read(20 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk

    return Response(send_chunk(), content_type="application/octet-stream")


# --------------------------
"""
启动主程序功能
"""
app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(platform, url_prefix="/platform")

if __name__ == "__main__":
    app.run(host="localhost", port=5000, threaded=False)
