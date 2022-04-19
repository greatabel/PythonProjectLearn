"""App entry point."""
import os
import sys
import json

import flask_login
from flask_cors import CORS

from flask import send_from_directory
from flask import request
from flask import url_for
from flask import redirect, session
from flask import Blueprint, render_template as rt
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, Response
from flask import jsonify
from flask_cors import CORS
from movie import create_app

# import es_search
import jellyfish
import random
# from movie.domain.model import Director, Review, Movie

# from html_similarity import style_similarity, structural_similarity, similarity
# from common import set_js_file

app = create_app()
app.secret_key = "ABCabc123"
app.debug = True
CORS(app)
# --- total requirement ----


# ---start  数据库 ---

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campus_data.db"
db = SQLAlchemy(app)

# --- end   数据库 ---
admin_list = ["admin@126.com"]


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
    试卷数据模型
    """

    # 主键ID
    id = db.Column(db.Integer, primary_key=True)
    # 试卷标题
    title = db.Column(db.String(100))
    # 试卷正文
    text = db.Column(db.Text)

    right_answer = db.Column(db.Text)
    student_answer = db.Column(db.Text)

    def __init__(self, title, text, right_answer, student_answer):
        """
        初始化方法
        """
        self.title = title
        self.text = text
        self.right_answer = right_answer
        self.student_answer = student_answer


# # 老师当前布置作业的表
# class TeacherWork(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), unique=True)
#     detail = db.Column(db.String(500))
#     answer = db.Column(db.String(5000))
#     course_id = db.Column(db.Integer)

#     def __init__(self, title, detail, answer, course_id):
#         self.title = title
#         self.detail = detail
#         self.answer = answer
#         self.course_id = course_id


# class StudentWork(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     userid = db.Column(db.Integer)
#     answer = db.Column(db.String(5000))
#     score = db.Column(db.DECIMAL(10, 2))
#     course_id = db.Column(db.Integer)

#     def __init__(self, userid, answer, score, course_id):
#         self.userid = userid
#         self.answer = answer
#         self.score = score
#         self.course_id = course_id


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
        self.totalpage = len(data) // number + 1
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
    blogs = Blog.query.all()
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

            if len(search_list) == 0 and keyword in ['天气', '心情']:
                es_content = es_search.mysearch(keyword)
                search_list.append(es_content)
            # for movie in notice_list:
            #     if movie.director.director_full_name == keyword:
            #         search_list.append(movie)

            #     for actor in movie.actors:
            #         if actor.actor_full_name == keyword:
            #             search_list.append(movie)
            #             break

            #     for gene in movie.genres:
            #         if gene.genre_name == keyword:
            #             search_list.append(movie)
            #             break
        print("search_list=", search_list, "=>" * 5)
        return rt("home.html", listing=PageResult(search_list, pagenum, 10), user=user, keyword=keyword)
        # return rt("home.html", listing=PageResult(search_list, pagenum, 2), user=user)

    return rt("home.html", listing=PageResult(blogs, pagenum), user=user)


single_choice_title = ["在计算机中,正在运行的程序存放在哪儿?","在下列存储器中,访问速度最快的是什么?",
 "下列不属于系统软件的是?"]
single_choice_text = ["A. 内存 B. 软盘 C. 光盘", "A.硬盘 B.随机存储器", 
    "A. 汇编程序 B. 电子表格处理软件"]
single_choice_right_answer = ['A', 'B', "B"]

design_title = ["论述计算机网络安全",
 "自己组装一个台式微型计算机"]
desing_text = ["论述计算机网络安全的主要因素有哪些", "自己组装一个台式微型计算机，必须选购的电脑组件,试着说明"]
desing_right_answer = ["(1)网络内部人员操作失误;(2)来自网络外部的恶意攻击;(3)网络软件的漏洞和“后门” ", 
     "(1)CPU(或者中央处理器或者CPU和CPU风扇)(2)内存(3)硬盘(或者外存储器)(4)显示器(显示器和显卡)(5)鼠标和键盘(或者其他输入设备)(6)机箱"
    ]

@app.route("/self_generate_blogs", methods=["GET", "POST"])
def self_generate_blogs():
    """
    创建试卷文章
    """
    generate_length = 2

    hard_rate = 0.9

    choosed_list = []
    for i in range(generate_length):
        choosed = random.randint(0, len(single_choice_title))
        if choosed not in choosed_list:
            title = "(单选题)" + single_choice_title[choosed]
            text= single_choice_text[choosed]
            right_answer = single_choice_right_answer[choosed]
            choosed_list.append(choosed)

            blog = Blog(title=title, text=text, right_answer=right_answer, student_answer='')
            print(blog.title, blog.text, ' #-# '*5, ' In self_generate_blogs')
            db.session.add(blog)
            # 必须提交才能生效
            db.session.commit()

    design_num = int(generate_length*hard_rate//3)
    if design_num == 0:
        design_num = 1
    print(design_num, '-'*20)
    for i in range(design_num):
        choosed = random.randint(0, design_num)
        if choosed not in choosed_list:
            title = "(设计题)" + design_title[choosed]
            text= desing_text[choosed]
            right_answer = desing_right_answer[choosed]
            choosed_list.append(choosed)

            blog = Blog(title=title, text=text, right_answer=right_answer, student_answer='')
            print(blog.title, blog.text, ' ## '*5, ' In self_generate_blogs')
            db.session.add(blog)
            # 必须提交才能生效
            db.session.commit()
    return redirect("/blogs")

@app.route("/blogs/create", methods=["GET", "POST"])
def create_blog():
    """
    创建试卷文章
    """
    if request.method == "GET":
        # 如果是GET请求，则渲染创建页面
        return rt("create_blog.html")
    else:
        # 从表单请求体中获取请求数据
        title = request.form["title"]
        text = request.form["text"]

        right_answer = request.form["right_answer"]
        # student_answer = request.form["student_answer"]


        # 创建一个试卷对象
        blog = Blog(title=title, text=text, right_answer=right_answer, student_answer='')
        db.session.add(blog)
        # 必须提交才能生效
        db.session.commit()
        # 创建完成之后重定向到试卷列表页面
        return redirect("/blogs")


# 自动打分系统
@app.route("/scores", methods=["GET"])
def circulate_scores():
    """
    查询试卷列表
    """
    blogs = Blog.query.all()
    scores = []

    for b in blogs:
        title = b.title
        right_answer = b.right_answer
        student_answer = b.student_answer


        s = 5
        if '单选题' in title:
            s = 10
        elif '多选题' in title:
            s = 15
        elif '计算题' in title:
            s = 20
        elif '设计题' in title:
            s = 25
        c0 = jellyfish.levenshtein_distance(right_answer, student_answer)
        c1 = jellyfish.jaro_distance(right_answer, student_answer)

        print('title=', title)
        print(right_answer, 'V'*10, student_answer, 'similarity=', c1, c0)
        scores.append(s*c1)
    total = sum(scores)
    # 渲染试卷列表页面目标文件，传入blogs参数
    print(scores)
    return rt("circulate_scores.html", blogs=blogs, scores=scores, total=total)

@app.route("/blogs", methods=["GET"])
def list_notes():
    """
    查询试卷列表
    """
    blogs = Blog.query.all()
    # 渲染试卷列表页面目标文件，传入blogs参数
    return rt("list_blogs.html", blogs=blogs)


@app.route("/blogs/update/<id>", methods=["GET", "POST"])
def update_note(id):
    """
    更新试卷
    """
    if request.method == "GET":
        # 根据ID查询试卷详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_blog.html", blog=blog)
    else:
        # 获取请求的试卷标题和正文
        title = request.form["title"]
        text = request.form["text"]

        # 更新试卷
        blog = Blog.query.filter_by(id=id).update({"title": title, "text": text})
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到试卷详情页面
        return redirect("/blogs/{id}".format(id=id))



@app.route("/blogs/answer/<id>", methods=["GET", "POST"])
def answer_note(id):
    """
    更新试卷
    """
    if request.method == "GET":
        # 根据ID查询试卷详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("answer_blog.html", blog=blog)
    else:
        # 获取请求的试卷标题和正文
        student_answer = request.form["student_answer"]



        # 更新试卷
        blog = Blog.query.filter_by(id=id).update({"student_answer": student_answer})
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到试卷详情页面
        # return redirect("/blogs/{id}".format(id=id))
        return redirect("/home")


@app.route("/blogs/<id>", methods=["GET", "DELETE"])
def query_note(id):
    """
    查询试卷详情、删除试卷
    """
    if request.method == "GET":
        # 到数据库查询试卷详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        print(id, blog, "in query_blog", "@" * 20)
        # 渲染试卷详情页面
        return rt("query_blog.html", blog=blog)
    else:
        # 删除试卷
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
    查询试卷详情、删除试卷
    """

    id = session["userid"]

    if request.method == "GET":

        # 到数据库查询试卷详情
        user = User.query.filter_by(id=id).first_or_404()
        print(user.username, user.password, "#" * 5)
        # 渲染试卷详情页面
        return rt("profile.html", user=user)
    else:
        # 删除试卷
        user = User.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return "", 204


@app.route("/profiles/update/<id>", methods=["GET", "POST"])
def update_profile(id):
    """
    更新试卷
    """
    if request.method == "GET":
        # 根据ID查询试卷详情
        user = User.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_profile.html", user=user)
    else:
        # 获取请求的试卷标题和正文
        password = request.form["password"]
        nickname = request.form["nickname"]
        school_class = request.form["school_class"]
        school_grade = request.form["school_grade"]

        # 更新试卷
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
        # 修改完成之后重定向到试卷详情页面
        return redirect("/profile")


### -------------end of profile


@app.route("/course/<id>", methods=["GET"])
def course_home(id):
    """
    查询试卷详情、删除试卷
    """
    if request.method == "GET":
        # 到数据库查询试卷详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        teacherWork = TeacherWork.query.filter_by(course_id=id).first()
        print(id, blog, "in query_blog", "@" * 20)
        # 渲染试卷详情页面
        return rt("course.html", blog=blog, teacherWork=teacherWork)
    else:
        return "", 204


login_manager = flask_login.LoginManager(app)
user_pass = {}


# @app.route("/call_bash", methods=["GET"])
# def call_bash():
#     i0bash_caller.open_client("")
#     return {}, 200


@app.route("/statistics", methods=["GET"])
def relationship():
    # static/data/test_data.json
    filename = os.path.join(app.static_folder, "data.json")
    with open(filename) as test_file:
        d = json.load(test_file)
    print(type(d), "#" * 10, d)
    return jsonify(d)

@app.route('/index_a/')
def index():
    return rt('index-A.html')
       

@app.route('/index_b/')
def index_b():
    return rt('index-B.html')
        


@login_manager.user_loader
def load_user(email):
    print("$" * 30)
    return user_pass.get(email, None)


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    print('login=>', email, password)
    try:
        data = User.query.filter_by(username=email, password=password).first()
        print(data, "@" * 10)
        if data is not None:
            print("test login")
            session["logged_in"] = True

            if email in admin_list:
                session["isadmin"] = True
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
    if email in user_pass:
        print("already existed user")
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
# @app.route("/assignwork", methods=["GET"])
# def assignwork():
#     return rt("index.html")


# @app.route("/teacher_work", methods=["POST"])
# def teacher_work():

#     detail = request.form.get("detail")
#     print("#" * 20, detail, "@" * 20)
#     with open("movie/static/data.js", "w") as file:
#         file.write(detail)

#     return redirect(url_for("assignwork"))


# @app.route("/student_work", methods=["POST"])
# def student_work():
#     return redirect(url_for("student_index"))


# @app.route("/student_index", methods=["GET"])
# def student_index():
#     return rt("student_index.html")


# @app.route("/", methods=["GET"])
# def index():
#     return rt("index.html")


@app.route("/file/upload", methods=["POST"])
def upload_part():  # 接收前端上传的一个分片
    task = request.form.get("task_id")  # 获取文件的唯一标识符
    chunk = request.form.get("chunk", 0)  # 获取该分片在所有分片中的序号
    filename = "%s%s" % (task, chunk)  # 构造该分片的唯一标识符
    print("filename=", filename)
    upload_file = request.files["file"]
    upload_file.save("./upload/%s" % filename)  # 保存分片到本地
    return rt("index.html")


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

    return rt("index.html")


@app.route("/file/list", methods=["GET"])
def file_list():
    files = os.listdir("./upload/")  # 获取文件目录
    # print(type(files))
    files.remove(".DS_Store")
    # files = map(lambda x: x if isinstance(x, unicode) else x.decode('utf-8'), files)  # 注意编码
    return rt("list.html", files=files)


@app.route("/file/download/<filename>", methods=["GET"])
def file_download(filename):
    def send_chunk():  # 流式读取
        store_path = "./upload/%s" % filename
        print("store_path=", store_path)
        with open(store_path, "rb") as target_file:
            while True:
                chunk = target_file.read(20 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk

    return Response(send_chunk(), content_type="application/octet-stream")


# Custom static data
@app.route("/cdn/<path:filename>")
def custom_static(filename):
    print("#" * 20, filename, " in custom_static", app.root_path)
    return send_from_directory(
        "/Users/abel/Downloads/AbelProject/FlaskRepository/b13596campus_navigation/upload/",
        filename,
    )


# --------------------------


if __name__ == "__main__":
    db.create_all()

    app.run(host="localhost", port=5000, threaded=False)
