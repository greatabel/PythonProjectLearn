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
根据自己机器的ip和操作系统情况，修改下面的ip
i0start_ui.py 中的
cmd = "python3 main.py --ip 192.168.2.102 --encryption yes"


6.
命令的2边同步：
一台机器执行 python3 i2server.py
另一台机器执行: python3 i3ui_with_list.py
（2个脚本中的ip需要换成对方机器的ip）


# ----------------------------------------  需求方案 ----------------------------------------

我们反正默认就是对ubuntu18.04进行上传下载之类的
还有ubuntu上面放一个脚本 可以吧
作为一个client接受
主控端mac那边可以点个简单图形化