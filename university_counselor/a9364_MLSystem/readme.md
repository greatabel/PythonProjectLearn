1. 
whole project based on python3
(project should work at all versons above python3.5 [include python3.5] )

create virtual environment
at Unix/MacOS run:
python3 -m venv  mlsystem-env

at windows run:
python -m venv  mlsystem-env

then enter virtual environment:
Windows run:
mlsystem-env\Scripts\activate.bat

Unix/MacOS run:
source mlsystem-env/bin/activate


2. 
在windows系统，在命令行中找到工程目录（你可以直接把工程文件夹拖到命令行，就显示了工程所在路径）
然后执行: cd  工程所在路径
pip3 install -r requirements.txt


3.
新开一个窗口，同样进入虚拟环境然后
python3 wsgi.py

4.
命令行下进入a9364_MLSystem/ipynb_backup的目录，执行：
jupyter notebook pricepredict.ipynb 


5. 
浏览器访问首页: http://127.0.0.1:5000/home