0.
在mac系统：
brew install ghostscript tcl-tk
brew install libmagic

1.
安装python3.6 以上版本

2. 
安装pip3 

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

7.
个人主页： http://localhost:5000/profile

修改编辑地点的后台管理页：
http://localhost:5000/blogs
可以点击 add doc连接，自己从pdf上copy文字输入到列表中；
或者命令行下：python3 i0ocr.py (记得修改14行的文件名，获得processeddata的text，目前60-70%准确度)然后再复制黏贴