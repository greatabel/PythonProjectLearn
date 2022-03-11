学习材料：

https://dormousehole.readthedocs.io/en/latest/
flask 框架
https://www.numpy.org.cn/
NumPy官方的中文文档
http://www.pypandas.cn/
pandas中文文档


--------------------------------------------------------
部署流程：

ubuntu(我是在ubuntu 18.04）或者其他linux，或者osx等类unix系统
其他系统没有经过充分测试

1.
安装python3.6 以上版本

2. 
安装pip3 

3.
（可选，非必须）（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html


4.
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt


5.
进入虚拟环境，开2个terminl窗口

运行已经训练好的结果看, 在terminal输入：
python3 i0detect_arrow.py

另一个窗口开贪食蛇
python3 i1snake.py

6.
(可选项)
不使用演示视频的话，修改成摄像头，只需要修改：
取消掉 i0detect_arrow.py 第26行的注释，程序会忽略视频读取，变成从实时摄像头
