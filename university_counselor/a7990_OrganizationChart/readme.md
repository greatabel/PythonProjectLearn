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

然后运行：
python3 wsgi.py

在浏览器中通过访问：http://127.0.0.1:5000/org_chart 查看效果

将来自己修改的数据关系data.json位置在： a7990_OrganizationChart/movie/static/data.json 
直接编辑data.json就实时起作用