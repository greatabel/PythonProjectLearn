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
命令行底下运行: python3 i6wsgi.py


# ------------ ------------ ------------ ------------ 

6.
（********可选********）

可视化配置部分部分在：
i5data.py

7.
（********可选********）
获得更多数据
在mac系统：
下载直接在命令行运行：

抓取百度党史新闻，然后进行筛选
python3  i1scrapy_localnews.py

可以抓取环球网相关新闻，然后进行筛选
python3  i0scrapy_huanqiu.py
