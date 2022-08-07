
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
需要处理的pdf都放在data文件夹即可，默认处理pdf

模拟运行在:
python3 i0ocr.py

6.
（可选项）
遇到没有遇到的关键词或者pdf搜索的检索情况
修改地i0ocr.py 99行的extract，添加更多case 情况，会越多越全

