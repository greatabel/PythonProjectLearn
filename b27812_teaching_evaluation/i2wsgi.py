"""App entry point."""
import os
import sys
import json
import random
import flask_login
from flask_cors import CORS

from flask import send_from_directory
from flask import request
from flask import url_for
from flask import redirect, session
from flask import Blueprint, render_template as rt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer


from flask import Flask, Response
from flask import jsonify
from flask_cors import CORS
from flask import make_response

# from flask_wtf.csrf import CSRFProtect
from flask import flash

from movie import create_app

# import es_search
import logging
import numpy as np
from scipy.integrate import odeint
import pandas as pd
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objs as go
from collections import defaultdict
from collections import Counter

from flask import render_template_string

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# key = get_random_bytes(16)  # 生成一个随机AES密钥，长度为16字节
key= b'7\xf4\xae\xb6\xee$\x9cdw\xf7%\xde\x88\x01$<'
print('key=', key)

app = create_app()
app.secret_key = "ABCabc123"
app.debug = True


handler = logging.FileHandler("flask.log", encoding="UTF-8")
handler.setLevel(
    logging.DEBUG
)  # 设置日志记录最低级别为DEBUG，低于DEBUG级别的日志记录会被忽略，不设置setLevel()则默认为NOTSET级别。
logging_format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s"
)
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


CORS(app)

# 防御点3: CSRF攻击模拟 防御
# CSRFProtect(app)

# --- total requirement ----


# ---start  数据库 ---

print("#" * 20, os.path.abspath("movie/campus_data.db"), "#" * 20)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(
    "movie/campus_data.db"
)
# 防御点1: 防止入sql-inject ，不实用sql注入，sqlchemy让代码ORM化，安全执行
db = SQLAlchemy(app)

last_upload_filename = None
# --- end   database  ---
admin_list = ["admin@126.com", "greatabel1@126.com"]


class User(db.Model):
    """Create user table"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    nickname = db.Column(db.String(80))
    school_class = db.Column(db.String(80))
    school_grade = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Blog(db.Model):
    """
    ppt entity
    """

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))

    text = db.Column(db.Text)

    def __init__(self, title, text):
        """
        初始化方法
        """
        self.title = title
        self.text = text


class Comment(db.Model):
    """
    Comment entity
    """
    id = db.Column(db.Integer, primary_key=True)

    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))  
    # the corresponding blog id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  
    # the corresponding user id, nullable=True for anonymous comments
    rating = Column(Integer)  # 新增字段

    raw_text = db.Column(db.Text)  # original comment text
    cipher_text = db.Column(db.Text)  # encrypted comment text

    def __init__(self, raw_text, blog_id, rating,user_id=None):
        """
        Initialization method
        """
        self.raw_text = raw_text
        self.blog_id = blog_id
        self.user_id = user_id
        self.rating = rating

        cipher = AES.new(key, AES.MODE_ECB)
        self.cipher_text = base64.b64encode(cipher.encrypt(pad(self.raw_text.encode('utf-8'), 
                            AES.block_size))).decode('utf-8')  # encrypt comment and store

### -------------start of home
def replace_html_tag(text, word):
    new_word = '<font color="red">' + word + "</font>"
    len_w = len(word)
    len_t = len(text)
    for i in range(len_t - len_w, -1, -1):
        if text[i : i + len_w] == word:
            text = text[:i] + new_word + text[i + len_w :]
    return text


class PageResult:
    def __init__(self, data, page=1, number=4):
        self.__dict__ = dict(zip(["data", "page", "number"], [data, page, number]))
        self.full_listing = [
            self.data[i : i + number] for i in range(0, len(self.data), number)
        ]
        self.totalpage = len(data) // number
        print("totalpage=", self.totalpage)

    def __iter__(self):
        if self.page - 1 < len(self.full_listing):
            for i in self.full_listing[self.page - 1]:
                yield i
        else:
            return None

    def __repr__(self):  # used for page linking
        return "/home/{}".format(self.page + 1)  # view the next page





@app.route("/home/<int:pagenum>", methods=["GET"])
@app.route("/home", methods=["GET", "POST"])
def home(pagenum=1):
    print("home " * 10)
    app.logger.info("home info log")

    blogs = Blog.query.all()
    blogs = list(reversed(blogs))
    user = None
    if "userid" in session:
        user = User.query.filter_by(id=session["userid"]).first()
    else:
        print("userid not in session")
    print("in home", user, "blogs=", len(blogs), "*" * 20)
    if request.method == "POST":
        search_list = []
        keyword = request.form["keyword"]
        print("keyword=", keyword, "-" * 10)
        if keyword is not None:
            for blog in blogs:
                if keyword in blog.title or keyword in blog.text:
                    blog.title = replace_html_tag(blog.title, keyword)
                    print(blog.title)
                    blog.text = replace_html_tag(blog.text, keyword)

                    search_list.append(blog)


        print("search_list=", search_list, "=>" * 5)
        return rt(
            "home.html",
            listing=PageResult(search_list, pagenum, 10),
            user=user,
            keyword=keyword,
        )
        # return rt("home.html", listing=PageResult(search_list, pagenum, 2), user=user)

    return rt("home.html", listing=PageResult(blogs, pagenum), user=user)


@app.route('/comments/create', methods=['POST'])
def create_comment():
    comment_text = request.form.get('comment_text')
    rating = int(request.form.get('rating', 0))  # 获取评分
    blog_id = request.form.get('blog_id')
    user_id = session['user_id'] if 'user_id' in session else None  # 当前登录的用户ID，如果有的话

    if not comment_text:
        # 如果没有评论内容，返回错误信息
        flash('评论内容不能为空')
        return redirect(request.referrer)

    if not 1 <= rating <= 5:
        # 如果评分不在1到5的范围内，返回错误信息
        flash('评分必须在1到5之间')
        return redirect(request.referrer)
    print('comment_text=',comment_text)
    comment = Comment(raw_text=comment_text, rating=rating, blog_id=blog_id, user_id=user_id)
    db.session.add(comment)
    db.session.commit()

    flash('评论添加成功')
    return redirect(request.referrer)




from plotly.offline import plot
import plotly.graph_objs as go
from collections import defaultdict

@app.route("/statistics", methods=["GET"])
def statistics():
    blogs = Blog.query.all()  # get all blogs
    blog_titles = {blog.id: blog.title for blog in blogs}  # map blog ids to titles

    # Prepare a dictionary to store scores for each blog
    scores_by_blog = defaultdict(list)

    # Get all comments
    comments = Comment.query.all()

    # Go through each comment and add its score to the corresponding blog
    for comment in comments:
        blog_title = blog_titles.get(comment.blog_id)
        if blog_title is not None:
            scores_by_blog[blog_title].append(comment.rating)

    # Now create a separate bar chart for each blog
    fig = go.Figure()
    for blog_title, scores in scores_by_blog.items():
        score_counts = Counter(scores)
        fig.add_trace(go.Bar(x=list(score_counts.keys()), y=list(score_counts.values()), name=blog_title))

    # Update layout
    fig.update_layout(barmode='stack', xaxis_title='Rating', yaxis_title='Count', title="Rating distribution by blog")

    div = plot(fig, output_type='div')

    return rt("statistics.html", plot_div=div)


@app.route("/blogs/create", methods=["GET", "POST"])
def create_blog():
    """
    创建ppt文章
    """
    if request.method == "GET":
        # 如果是GET请求，则渲染创建页面
        return rt("create_blog.html")
    else:
        # 从表单请求体中获取请求数据
        title = request.form["title"]
        text = request.form["text"]

        # 创建一个ppt对象
        blog = Blog(title=title, text=text)
        db.session.add(blog)
        # 必须提交才能生效
        db.session.commit()
        # 创建完成之后重定向到ppt列表页面
        return redirect("/blogs")


@app.route("/blogs", methods=["GET"])
def list_notes():
    """
    查询ppt列表
    """
    blogs = Blog.query.all()

    # 渲染ppt列表页面目标文件，传入blogs参数
    return rt("list_blogs.html", blogs=blogs)


@app.route("/blogs/update/<id>", methods=["GET", "POST"])
def update_note(id):
    """
    更新Predict_Category
    """
    if request.method == "GET":
        # 根据ID查询ppt详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_blog.html", blog=blog)
    else:
        # 获取请求的ppt标题和正文
        title = request.form["title"]
        text = request.form["text"]

        # 更新ppt
        blog = Blog.query.filter_by(id=id).update({"title": title, "text": text})
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到ppt详情页面
        return redirect("/blogs/{id}".format(id=id))


@app.route("/blogs/<id>", methods=["GET", "DELETE"])
def query_note(id):
    """
    查询Predict_Category详情、删除Predict_Category
    """
    if request.method == "GET":
        # 到数据库查询ppt详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        print(id, blog, "in query_blog", "@" * 20)
        comments = Comment.query.filter_by(blog_id=blog.id).all()

        # 渲染ppt详情页面
        return rt("query_blog.html", blog=blog, comments=comments)
    else:
        # 删除ppt
        blog = Blog.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return "", 204


### -------------end of home


### -------------start of profile


@app.route("/profile", methods=["GET", "DELETE"])
def query_profile():
    """
    查询Predict_Category详情、删除ppt
    """

    id = session["userid"]

    if request.method == "GET":

        # 到数据库查询ppt详情
        user = User.query.filter_by(id=id).first_or_404()
        print(user.username, user.password, "#" * 5)
        # 渲染ppt详情页面
        r = make_response(rt("profile.html", user=user))
        # 防御点2：xss攻击，实用csp方式： https://content-security-policy.com/
        r.headers.set(
            "Content-Security-Policy",
            "default-src * 'unsafe-inline'; connect-src 'self' 'nonce-987654321' ",
        )
        return r
    else:
        # 删除ppt
        user = User.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return "", 204


@app.route("/profiles/update/<id>", methods=["GET", "POST"])
def update_profile(id):
    """
    更新ppt
    """
    if request.method == "GET":
        # 根据ID查询ppt详情
        user = User.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_profile.html", user=user)
    else:
        # 获取请求的ppt标题和正文
        password = request.form["password"]
        nickname = request.form["nickname"]
        school_class = request.form["school_class"]
        school_grade = request.form["school_grade"]

        # 更新ppt
        user = User.query.filter_by(id=id).update(
            {
                "password": password,
                "nickname": nickname,
                "school_class": school_class,
                "school_grade": school_grade,
            }
        )
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到ppt详情页面
        return redirect("/profile")


### -------------end of profile


login_manager = flask_login.LoginManager(app)
user_pass = {}





@login_manager.user_loader
def load_user(email):
    print("$" * 30)
    return user_pass.get(email, None)


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        data = User.query.filter_by(username=email, password=password).first()
        print(data, "@" * 10)
        if data is not None:
            print("test login")
            session["logged_in"] = True

            if email in admin_list:
                session["isadmin"] = True
                print("@" * 20, "setting isadmin")
            session["userid"] = data.id

            print("login sucess", "#" * 20, session["logged_in"])

            # w = TeacherWork.query.get(1)
            # print('w=', w, w.answer, w.title)
            # if w is not None:
            #     session['title'] = w.title
            #     session['detail'] = w.detail
            #     session['answer'] = w.answer

            return redirect(url_for("home", pagenum=1))
        else:
            return "Not Login"
    except Exception as e:
        print(e)
        return "Not Login"
    return redirect(url_for("home", pagenum=1))


@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        return redirect(url_for("home", pagenum=1))
    # if DB.get_user(email):
    data = User.query.filter_by(username=email).first()
    # if email in user_pass:
    if data is not None:
        print("already existed user")
        flash("already existed user")
        return redirect(url_for("home", pagenum=1))
    # salt = PH.get_salt()
    # hashed = PH.get_hash(pw1 + salt)
    print("register", email, pw1)
    new_user = User(username=email, password=pw1)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("home", pagenum=1))


@app.route("/logout")
def logout():
    session["logged_in"] = False
    return redirect(url_for("home", pagenum=1))


reviews = []


@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized"


# --------------------------


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        app.run(host="localhost", port=5000, threaded=False)
