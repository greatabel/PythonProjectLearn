
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
运行目标靶场
打开一个命令行窗口，cd进入i1target_website/final_target 文件夹
然后执行: python3 app.py 

新开另一个命令行窗口，在a20001sql_injection_platform目录下执行:
python3 i4wsgi.py



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
一般用户测试账号:
username:test@126.com   
password: test

7.
个人主页： http://localhost:5000/profile

8.
(可选)
sqlmap安装(macbook): 
https://codeantenna.com/a/DTCXKTs1fW

9.
(可选)
运行final_target以外的其他目标靶场：
cd到 i1target_website下，重复第四步的代码，
安装好目标靶场相关的requirements.txt
分别进入L1-L6运行不同
python3 L1.py 
python3 L2.py 
...
python3 L6.py 
等目标站点

10.




