1.
安装python3.6 以上版本

2. 
安装pip3 

<!-- 3.
可选（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt
 -->

3-4.
我帮你创建好了虚拟环境movie-env, 现在只需要
terminal 里面cd 到 new_version文件夹

then enter virtual environment:
Windows run:
movie-env\Scripts\activate.bat

Unix/MacOS run:
source movie-env/bin/activate

5.
terminal底下运行：
python3 main.py --type=image --folder=input_images
如果是原来的图片文件夹，可以打开调试参数：
python3 main.py --type=image --folder=input_images --debug=True