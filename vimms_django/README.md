# vimms_django
SG=StarGate，SGScrapy工程主要是后端抓取、入库功能

original requirements：
需求详细描述：已经有源码的python软件（Vimms 一个质谱模拟器）将其变成一个web应用程序（django），
可以上传数据（file）然后运行它以观察从不同数据采集参数获得的输出。
注意事项及程序环境：ViMMS是Python软件包，可以从Python脚本和交互式环境（如Jupyter Notebook）中访问，
用户可以在其中指向自己的光谱文件或化合物列表，以开始对自己的数据使用ViMMS。 
输出有几种不同数据的采集参数选择


************** attention please **************
vimms库还非常不成熟，因此移植时候需要修复移植库的bug：
1. exmaple在最新的代码上运行不起来，不要使用pip安装，也不要使用github上master分支1.0.0, 1.1.0，
  而要去你发给我的文件夹下本地安装：
（比如我的在你传给我的文件解压下 vimms-master 有setup.py的目录下执行：）
先执行 python3 setup.py build
然后执行 python3 setup.py install

2. 打开本地安装的mass_spec_utils的gnps.py文件：
比如我的在： /usr/local/lib/python3.7/site-packages/mass_spec_utils/library_matching/gnps.py
的代码有bug：from .spectrum import SpectralRecord 改为from spectrum import SpectralRecord


