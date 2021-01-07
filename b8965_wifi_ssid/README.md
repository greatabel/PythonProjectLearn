正规流程
1. 
whole project based on python3
(project should work at all versons above python3.5 [include python3.5] )




create virtual environment:
python3 -m venv  movie-env


then enter virtual environment:
Windows run:
movie-env\Scripts\activate.bat

Unix/MacOS run:
source movie-env/bin/activate


2. 
pip3 install -r requirements.txt



目前流程：
如果是osx/linux的话，可以更简单。我给你打包了movie-env 虚拟环境，你可以跳过这些安装虚拟环境和依赖库的正规流程。
只需要运行：
1. 装好python3后
2. 命令行来到目录（a7990_OrganizationChart）下面，然后进入虚拟环境:
Windows run:
movie-env\Scripts\activate.bat

Unix/MacOS run:
source movie-env/bin/activate


3.
然后进入 文件夹，运行：
export FLASK_APP=i1flask_api.py
export FLASK_ENV=development
python3 -m flask run

在浏览器中通过访问：http://127.0.0.1:5000/ 查看效果

