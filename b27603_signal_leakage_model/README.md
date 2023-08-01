1.
安装python3.6 以上版本

2. 
安装pip3 
（如果网速慢 可以pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  把some-package替换成自己的慢的包 )

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.

terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
terminal底执行；
jupyter notebook i3predict_model.ipynb     

另开一个terminal：
python3 i2wsgi.py

访问：
http://localhost:5000/home

6.
已经注册好的管理员账号 可以直接登录：
管理员1
username: greatabel1@126.com
password: abel


你也可以自己注册和登录




-------------------
一般用户测试账号:(geust_test)
username:test@126.com
password: test


# -----start requirement ------

简化方案：
1.  一个课程管理系统（增删改查 课程变成学科教学）
2. 用户系统（注册，登陆）
3. 用户的增删改查
4. 评价功能 我们就往多方安全计算靠下（用AES对用户评价进行加密，同时，匿名评价我们采用不保存用户ID或者通过其他方式保持用户的匿名性）
5. Blog这个数据模型中增加一个字段来存储加密后的评价
6.  可视化页面和统计解密评价，统计分析，比如得分平均值，标准差等

# -----end   requirement ------