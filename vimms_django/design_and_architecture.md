本工程主要通过修改Vimms工程一些代码，使之可以在web环境下直接通过django
后台代码调用，使之可以实现之前vimms的ipynb本地才能实现的数据处理、分析：

具体做了以下工作：
    # 修复了一些Vimms库没有考虑在web交互场景使用的问题：
      ·修改文件包在线解压缩xml，和处理巨大xml（超过4G+）的网络延迟处理
      ·修改原生包处理一些训练时候处理上一次遗留数据的bug
      ·修复ScanParameters相关的一些初始化bug
      ····
    # 修改原来jupter的代码，修改为可以在web的安全线程内运行
      · 修改matplot在后台静默处理，并提供接口将处理后的mZml文件和png图表等文件提供下载功能
      · 将原来一些巨大的单体jupter的代码根据DRY原则进行的重构和拆分，减少冗余度

    # 使用django和相关库处理实现了：
      · django网站架构本身, 前端采用bootstrap和jquery实现了自适应UI，适应pc站和移动站访问
      · 实现了防止跨站脚本攻击安全性
      · 实现了压缩包的自动上传、解压缩，处理，处理后的下载的pipeline功能
      ···


整体处理流程如下：
    应用程序则负责具体的逻辑处理。为了方便应用程序的开发.
    开发出的应用程序都要和服务器程序配合，才能为用户提供服务。
    为了统一规范，设立了一个标准，服务器和框架都支持这个标准。这样不同的服务器就能适应不同的开发框架，
    不同的开发框架也就能适应不同的服务器。
    WSGI（Web Server Gateway Interface）就是一种规范，
    它定义了使用Python编写的web应用程序与web服务器程序之间的接口格式，
    实现web应用程序与web服务器程序间的解耦。

    用户通过Django的view层的html 页面（即用户看到的网站UI）进行操作：

    Simple_ms1页上传需要处理的example_data.zip之类的压缩包，然后进行Simple_ms1的处理，
    然后去dia页，topn页选择不同的按钮，查看不同的处理流程的结果，下载对应的处理文件。

    user input ->  view -> controller --> model
    MVC 即 model(M)、view(V)、control(C)。model即数据库模型，对数据库表结构的定义；
    view即视图逻辑程序；control即控制器，根据用户的输入的URL来指定将调用的视图。
    由于control的部分由框架自行处理，因此也会被认为是MTV模式。
    MTV 即 model(M)、template(T)、view(V)。

工程整体结构介绍：
__init__.py           # 让python把它该目录当做一个开发包所需要的文件，即当做一组模块
settings.py          # 项目的配置文件，其中有一些项目的基本设置
urls.py                 # URL和视图函数的映射文件
wsgi.py                # web服务器网关接口配置文件
forms.py              # 手动创建的，利用Django.forms，创建HTML表单模型，由Django系统检查错误，便于简化视图函数和HTML代码的简化
admin.py              # 启用该文件，将表模型导入，可以使用Django自带的admin页面操作这些表
apps.py                # 存放app信息
models.py            # 定义表的模型（和表的数据结构相似），即我们管理压缩包上传的模型
file_procesor.py     # 解压缩文件，把解压缩之后的文件传递给pre_proces.py进行处理
pre_prcosss.py       # 为处理我们下载然后调用相关extract方法，proces方法的地方
processor_*.py       #  为具体不同的处理方法（dia, simple_sm1, topn, vary in topn ...)

    从页面获取URL: 比如localhost:8000
从settings.py中找到的urls.py的位置；
从urls.py中搜索到对应的view
执行该视图simple_ms1的request对象；
在视图中如需数据库里的数据，根据models.py，从数据库里获取数据，然后将数据返回给视图；
经过视图函数Document的一系列操作，会将 要显示的数据返回给模板templates中的HTML文件；
最后，用户会看到返回的页面，页面中包含了用户需要的数据。

整个网站由：python3.7语言
使用到具体软件包：
    Django==3.1.1
    flake8==3.7.9
    loguru==0.5.2
    pymzml==2.4.7
还有原vimms工程本身

同时用到R3.6.1
使用到具体软件包：
    xcms极其依赖


