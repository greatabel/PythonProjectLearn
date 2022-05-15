

1.
安装python3.6 以上版本

2. 
安装pip3 
（如果网速慢 可以pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  把some-package替换成自己的慢的包 )

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
模拟运行在:
python3 wsgi.py





6.
浏览器访问：

http://localhost:5000/home

已经注册好的管理员账号 可以直接登录：
管理员1
username: greatabel1@126.com 
password: abel
你也可以自己注册和登录

管理员2
username: admin@126.com
password: admin

-------------------
一般用户测试账号:
username:test@126.com   
password: test
7.
个人主页： http://localhost:5000/profile


# ---- 架构说明 -----


ComplexEventExtraction代码还可以用，我找到啦原作者的开源代码：
https://github.com/liuhuanyong/ComplexEventExtraction， 后续封装成库啦，在i2wsgi.py中调用


第2个时间抽取库就用简单的机遇摘要的：https://blog.csdn.net/kobeyu652453/article/details/106985033 这个没现成的，我们自己缝制，
我们的代码基本就是用这个文章的，nlp的基于概率的摘要，在i1extract_method2.py里面
真正整个软件平台肯定只用1种（用ComplexEventExtraction）
 
我们支持json格式的三元组的知识图谱的上传和下载，还有构建（构建就是上一步的ComplexEventExtraction 分析用户在点击了：extract—event按键
进入对应页面上传数据后分析得到。我们主要选用了pre_event 和 post—event，概率统计用来计算频度

支持把生成的知识图谱导出，因为生成之后我们保存为了json（方便可视化）也是先json吧

我们会给予flask+echart+vue+d3实现知识图谱的可视化，也会设计用户系统（注册 登录，首页，上传json三元组的功能）
d3比较合适的图谱布局：
能更好地表达出数据的含义，通过视觉降噪可以进一步让图谱传递出更多的有效信息。但是用户依然需要通过交互找到自己关心的信息，一个图谱可视化工具是否好用，交互功能会起到非常重要的作用。目前，我们实现了下面的基本交互功能：画布操作：拖动、缩放、动态延展、布局变换、多节点圈选。
元素（节点和边）操作：样式配置、悬浮高亮、元素锁定、单击、双击、右键菜单、折叠/展开、节点拖动。
echart也可以让图谱在初始化时都会有一段时间的位置调整动画，这是力引导布局的共性，差别在于如何更快的让节点趋于稳定。
（节点很少的时候，基本看不出来差别）节点单击展示节点属性表格，表格内容动态切换节点第一次双击拓展，第二次双击折叠，类似于按钮 toggle过程。节点右键可出现操作菜单，如删除节点，添加关注点等。放大缩小清空图谱

我们知识图谱的可视化是基于d3+echart,但是d3 好像实现不了箭头和方向，就是事件和事件的关联是可以可视化的，并且可以拉升/放大/缩小/节点有弹性





