1.
你先打开
http://127.0.0.1:15672/

可以翻看各个tab，介绍下rabbitmq的各个主要概念：

Publisher
消息的生产者。也是一个向交换器Exchange发送消息的客户端应用程序。

Consumer
消息的消费者。表示一个从消息队列中取得消息的客户端应用程序。

Server/Broker
Broker，接受客户端的连接，实现AMQP实体服务

主要翻到queue的tab 讲一讲：我们使用的hello queue
Message Queue（消费者创建），消息队列，保存消息并将它们转发给消费者。它是消息的容器，也是消息的终点。
一个消息可以投入一个或多个队列。消息一直在队列里面，等待消费者连接到这个队列上将其取走
我们是Number Int类型，max-length=5 之类

还可以将一讲 我们的命令行程序，还有GUI程序都算作Consumer，订阅啦这个hello queue


2.

你新开命令行，模拟运行在:
python3 wsgi.py

这部分你主要讲解flask和UI部分（jinjia template/vue/boostrap），承载我们可视化操作，控制命令行客户端和GUI客户端的用户server操作端。

我们是flask 提供网站的后端，并且还有api端 和 前端jinjia template打交道，把用户的操作传到 api，然后api传递到rabbimq的hello channenl，变成移步缓存的队列。

Flask本身是一个基于Python开发并且依赖jinja2模板和Werkzeug WSGI服务的一个微型框架，对于Werkzeug本质是Socket服务端，
其用于接收http请求并对请求进行预处理，然后触发Flask框架。开发人员基于Flask框架提供的功能对请求进行相应的处理，
并返回给用户，如果要返回给用户复杂的内容时，
需要借助jinja2模板来实现对模板的处理，即：将模板和数据进行渲染，将渲染后的字符串返回给用户浏览器

而我们之所以选择flask是由于灵活：
1)Flask自由、灵活，可扩展性强，第三方库的选择面广，开发时可以结合自己最喜欢用的轮子，也能结合最流行最强大的Python库;

2)入门简单，即便没有多少web开发经验，也能很快做出网站;

3)非常适用于小型网站;

4)非常适用于开发Web服务的API


3.
再开2个命令行分别进入虚拟环境，运行：

python3 i14simulate_iot.py

python3 i6more_attractive_gui.py

这2个客户端程序一个是命令行的，一个是GUi，但是他们都是rabbimq中的消费者。
一个生产者，一个消费者；就是简单的队列方式。 生产者是flask端。

i14simulate_iot.py是我们开始版本的客户端程序，所有比较直观，是命令行的
i6more_attractive_gui.py是GUI的，tkinter是Python 的标准 GUI库。
Python 使用 Tkinter 可以快速的创建 GUI 应用程序。
由于 Tkinter 是内置到 python 的安装包中、只要安装好 Python 之后就能 import Tkinter 库、
而且 IDLE 也是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如





