

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
python3 wsgi.py



6.
浏览器访问：

http://localhost:5000/home

已经注册好的账号 可以直接登录：
username: greatabel1@126.com 
password: abel
你也可以自己注册和登录

学生测试账号:
username:test@126.com   
password: test
7.
个人主页： http://localhost:5000/profile


知识图谱访问: http://localhost:5000/index_a/


---------- ---------- 可选项 ---------- ---------- 
从步骤8开始都是可选项，不是必须

i0ocr.py 是从pdf里面ocr出问题的功能，也许图片的题库可以提取出来，暂时可以不使用这块功能
downloader/i0scrapy_huanqiu.py  是从论文和网络上抓取的功能，作为素材,暂时可以不使用这块功能

