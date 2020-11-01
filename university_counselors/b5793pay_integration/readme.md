1. 本地安装python3 然后terminal执行：
（如果pip没有安装，请先安装pip工具：https://www.runoob.com/w3cnote/python-pip-install-usage.html ）
pip3 install --upgrade -r requirements.txt


2.
在命令行中来到工程文件夹，到达app.py平级，然后执行下面领域运行网站：

export FLASK_APP=app.py
export FLASK_ENV=development

python3 -m flask run
然后访问：http://localhost:5000/




3. 
paypal选项 选择支付页面的paypal按钮（黄色）， 
所有的信用卡（visa, mastercard ,americaexprss)都使用paypal按钮下面的 借记卡或信用卡 按钮（黑色）


相关支付测试账号：
https://www.sandbox.paypal.com/
myreceiver2for2github@gmail.com Test1024

测试用zipcode：
99501

测试填写电话：
202-555-0156

mastercard测试账号：5217 2918 4234 0252
                    11/20  ,  045
                    lie  xu


visa测试账号0: 4929 5183 4671 0172
              Expires :10-2022 (MM-YYYY)CVV2 :347
visa测试账号1：4012888888881881

美国运通测试账号：American Express :345390028685591    
        Expires :10-2022 (MM-YYYY)    CVV2 :181 （不够前面补0： 0181）


4. Q2_c 测试页面 url 所在 和输入的私钥 公钥 数据：
http://localhost:5000/q2_c_home/alice 私钥使用50621_27221_3821_20981中的50621
http://localhost:5000/q2_c_home/bob   私钥使用50621_27221_3821_20981中的27221
http://localhost:5000/q2_c_home/karen 私钥使用50621_27221_3821_20981中3821
http://localhost:5000/q2_c_home/bank  公钥使用50621_27221_3821_20981中的20981


5. 
研究工程发现暂时不需要持久化，所以backend存储暂时使用json文件和缓存，
也可以很方便的修改为使用mysql：只需要自己修改下app.py的get_products方法读取mysql的products table即可
启动mysql，配置好本地mysql，执行ecommercedb.sql

