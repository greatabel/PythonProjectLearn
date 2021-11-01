0.
esseract安装

由于Textshot的OCR识别需要调用tesseract后端引擎，所以，首先需要安装tesseract。

Windows版安装可以直接访问下载链接[1].

Mac下可以使用Homebrew进行安装，

brew install tesseract
brew install poppler

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
