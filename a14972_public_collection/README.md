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
python3 main.py

6.
（可选）
获得更多数据
在mac系统：
下载直接在命令行运行：
python3 i0scrapy_huanqiu.py
（现在selenium的chrome扩展，是用在mac上面；
如果系统不是macosx 需要修改下配置：修改i0scrapy_huanqiu.py的头10行）

抓取本地天津新闻
python3  i1scrapy_localnews.py

（没有外网爬虫代理前，可以不做。假设有了外网爬虫，可以抓取twitter上中文圈舆情:)
进入i2Scrapy/twitter_scrapy 工程 在命令行下: python3 i0my_tw_downloader.py

7.
