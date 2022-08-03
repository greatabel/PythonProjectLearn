# deploy steps


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
pip 3install --upgrade -r requirements.txt

5.
一个terminal窗口执行监测的service端：
python3 i0simulate_camera_detect.py

另一个terminal窗口执行模拟接受的client：
python3 i1ros_read_from_detection.py


## 代码解释
 
