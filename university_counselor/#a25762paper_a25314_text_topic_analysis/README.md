1.
安装python3.6 以上版本

2. 
安装pip3 
（如果网速慢 可以pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  把some-package替换成自己的慢的包 )

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
模拟运行在:
python3 i1wsgi.py



6.
浏览器访问：

http://localhost:5000/home

已经注册好的管理员账号 可以直接登录：
管理员1
username: greatabel1@126.com
password: abel
你也可以自己注册和登录

管理员2
username: admin@126.com
password: admin

-------------------
一般用户测试账号:(geust_test)
username:test@126.com
password: test

7.
个人主页： http://localhost:5000/profile



8.
（可选，不是必须做的）
自己训练文本主题和文本主题关系可以单组在cmd运行：
python3 i3topic_analysis.py






# ------ 总需求 ------

做twitter的文本主题分析吗，可以按月份来做主题；

然后可视化会用matplot/d3 弄到网站上（网站本身python3/flask/d3/vue)
；如果觉得不够，我觉得还可以加上对主题的做知识图谱可视化。

然后主题之间可以做一个推荐引擎（协同过滤推荐，根据不同用户的喜好，进行协同推荐）



# ------ 附加 ------
周报1：
在上周的开发中，我们完成了 Flask 应用程序的基本架构和路由配置。
我们创建了一个简单的页面来展示所有主题，并为每个主题创建了一个详细信息页面。

1. 我们正在编写代码来分析主题内容中的情感词汇，并生成对主题情感的可视化。我们希望这些图表可以让用户更直观地了解每个主题的情感倾向。

2.
我们还在本周的开发中添加了 Vue。我们正在使用 Vue 来创建一些动态元素，例如用于交互的复选框和滑块。这些元素将与 Flask 后端进行通信，并且允许用户按照特定条件来过滤主题列表。

3. 前端在本周的开发中我们也引入了 Bootstrap。我们正在使用 Bootstrap 来提高应用程序的外观和易用性。
我们正在使用一些内置的 Bootstrap 样式来美化主题列表和详情页面，并且正在创建一些自定义的样式来使我们的应用程序与众不同。

4.
知识图谱基于d3+jquery

这就是大体目前更新，我们正在积极开发这个文本主题系统，希望27日展示一个有用和易于使用的应用程序
