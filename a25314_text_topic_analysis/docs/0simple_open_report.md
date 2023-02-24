# 开题简洁版


原始用户需求（就是来自学校）：
（1）上传各种格式的学习材料(例如PDF幻灯片、练习题、阅读材料、过去的试卷等)；
（2）一组访问、阅读和直接在共享材料上留下评论和问题的功能。
（3）您还将实施同行评估功能（peer assessment function），学生回答过去的考试问题，并由其他学生进行评论和评分。
（4）在学生没有自己尝试回答问题之前，不能看到其他人的答案。
（5）学生能够输入一个问题，系统自动选择已经被上传过的相关学习材料，并且强调其他学生的相关评论和注释。
 (6)为软件设计并制作合适的UI


根据软件工程进行实体拆分后，然后归纳feature和功能模块划分：
 主要功能：
 1. 用户注册/登录/
 	用户可以根据email/phone/username之类注册，可以有昵称，密码
 2. 个人主页
 	用户可以拥有自己的个人profile，profile可以修改各种第一步的信息
 3. 权限划分（管理员/普通使用者）
 	管理员可以看到材料列表，管理材料
 4. 学习材料的介绍页（title，content）
 5. 学习材料的相关培训视频上传功能，视频下载功能
 6. 网站的home页展示课程，前往注册，登录，个人主页，搜索和推荐页
 7. 学习材料detail页的学习材料展示功能
 8. 学习材料上发布问题/评论功能
 9. 学生在学习材料上回答问题的功能
10. 学生在学习材料上评论和问题的回答的同行评审/打分功能
11. 学习材料（pdf/docx/ppt）上传功能，下载功能


我们的前后端主要基于：flask+sqlchemy+flask cros + numpy+ html5+vue+jquery技术栈

数据库DB entity 识别表实体：
User: userrole(amdin/studdent, suername, email/phone, password ..etc)
Meterial_Blog( tiltle, detail, file_path)
File (FileObject and related Material_Blog)
Comments(question, comments related, ratings)
Question(title, content)
Answers(question related, answer content)


整体上主要是从前端Jinja的template + bootstrap + css3 页面触发事件，然后通过Flask CROS 传递到Flask的API 
Flask 是一个基于 Python 的轻量级 Web 框架，WSGI 工具箱采用 Werkzeug，模板引擎使用 Jinja2。由于其不依赖于特殊的工具或库，并且没有数据抽象层、表单验证或是其他任何已有多种库可以胜任的功能，从而保持核心简单、易于扩展，而被定义为"微"框架。但是，Flask 可以通过扩展来添加应用功能。并且 Flask 具有自带开发用服务器和 debugger、集成单元测试和 RESTful 请求调度 (request dispatching)、支持 secure cookie 的特点。我们就主要使用Flask的网站部分和wsgi写API部分

