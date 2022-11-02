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

6.
可视化部分在：
a14972_public_collection/movie/static/i4data_visualization

7.
（**可选**）
获得更多数据
在mac系统：
下载直接在命令行运行：
python3 i0scrapy_huanqiu.py
（现在selenium的chrome扩展，是用在mac上面；
如果系统不是macosx 需要修改下配置：修改i0scrapy_huanqiu.py的头10行）

抓取本地天津新闻
python3  i1scrapy_localnews.py

（**可选**）
（没有外网爬虫代理前，可以不做。假设有了外网爬虫，可以抓取twitter上中文圈舆情:)
进入i2Scrapy/twitter_scrapy 工程 在命令行下: python3 i0my_tw_downloader.py

（**可选**）情感分析模型训练
把新收集数据放在i3sentiment_analysis/data下，根据i3工程下的readme运行
i3deep-learning-for-sentiment-analysis.ipynb 可以进行情感模型训练


# 默认管理员账号：
greatabel1@126.com abel1024