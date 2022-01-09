1. 
whole project based on python3
(project should work at all versons above python3.5 [include python3.5] )

2. 
创建虚拟环境：（具体可以看： https://docs.python.org/zh-cn/3/library/venv.html）
create virtual environment 
at Unix/MacOS run 进入终端环境然后执行：
python3 -m venv  mlsystem-env

at windows run:
python -m venv  mlsystem-env

then enter virtual environment:
Windows run:
mlsystem-env\Scripts\activate.bat

Unix/MacOS run:
source mlsystem-env/bin/activate


3. 
来到工程目录requirements.txt所在目录，在命令行下执行：
pip3 install -r requirements.txt

4.
运行本地mac程序

新开一个窗口，同样进入虚拟环境然后,
运行 python3 i0pedestrian_detection.py --video=test1.mp4

或者使用自带摄像头/其他网络摄像头：python3 i0pedestrian_detection.py --camera=true


(注意事项：
macbook上面，因为没有支持macbook的GPU，所以使用CPU版本，考虑到CPU的运行神经网络性能，
我采取了各种措施提高处理效率：
python3 i0pedestrian_detection.py  --network=yolo3_mobilenet0.25_voc

如果是带英伟达GPU的笔记本(RTX1080/RTX1080Ti/RTX2080/RTX2080Ti...)，
可以开更强的模型，开GPU版本：
python3 i0pedestrian_detection.py  --network=yolo3_darknet53_voc --gpu=True
可以修改第48行，把“if count % 15 == 0” 中的15修改为1， 这样处理起来帧数更高，更流畅)



5.
配置视频来源


将来如果需要接入真实的枪机摄像头，功能也准备好了，就注视掉以上部分，打开49-54，就可以
支持所有的海康/大华主流摄像头



