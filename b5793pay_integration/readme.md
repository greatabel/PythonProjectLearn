1. 本地安装python3 然后terminal执行：

pip3 install --upgrade -r requirements.txt

在命令行中来到工程文件夹，到达app.py平级，然后执行下面领域运行网站：

export FLASK_APP=app.py
export FLASK_ENV=development

python3 -m flask run


2. 
启动mysql，配置好本地mysql，执行ecommercedb.sql


3. 相关支付测试账号：
https://www.sandbox.paypal.com/
myreceiver2for2github@gmail.com Test1024

测试用zipcode：
99501

测试填写电话：
202-555-0156

mastercard测试账号：5217 2918 4234 0252
                    11/20  ,  045
                    lie  xu

visa测试账号：4012888888881881
visa: 4929 5183 4671 0172Expires :10-2022 (MM-YYYY)CVV2 :347

美国运通测试账号：American Express :345390028685591    
        Expires :10-2022 (MM-YYYY)    CVV2 :181 （不够前面补0： 0181）