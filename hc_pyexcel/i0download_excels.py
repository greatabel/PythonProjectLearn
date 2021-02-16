from os import environ

import imaplib, email, os
# import pandas as pd
# import numpy as np
from datetime import datetime
from email.header import decode_header

# 抓取分析多少封邮件
N = 5

# https://zhuanlan.zhihu.com/p/94943212
def fetch_attachment(inputmail):
    #提取了指定编号（最新一封）的邮件
    resp, data = conn.fetch (inputmail.split()[len(inputmail.split())-1],'(RFC822)')
    emailbody = data[0][1]
    mail = email.message_from_bytes(emailbody)

    fileName = '没有找到任何附件！' 
    #获取邮件附件名称
    for part in mail.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename() 

    #如果文件名为纯数字、字母时不需要解码，否则需要解码
        try:
            fileName = decode_header(fileName)[0][0].decode(decode_header(fileName)[0][1])
            # print(fileName, '#'*10)
        except:
            pass
    #如果获取到了文件，则将文件保存在制定的目录下
        if fileName != '没有找到任何附件！':
            # filePath = os.path.join("C:\\文件夹名称", fileName)
            filePath = path + fileName

            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                print("附件已经下载，文件名为：" + fileName)
            else:
                print("附件已经存在，文件名为：" + fileName)


if __name__ == "__main__":
    path = os.getcwd()
    directory = (datetime.today()).strftime('%Y-%m-%d')   
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    path = path + '/' + directory + '/'
    #连接到qq企业邮箱，其他邮箱调整括号里的参数
    conn = imaplib.IMAP4_SSL("imap.exmail.qq.com", 993)

    hengchang_qyweixin_username = environ.get('hengchang_qyweixin_username', 'username')
    hengchang_qyweixin_password = environ.get('hengchang_qyweixin_password', 'password')
    # print(hengchang_qyweixin_username, hengchang_qyweixin_password)

    #用户名、密码，登陆
    conn.login(hengchang_qyweixin_username, hengchang_qyweixin_password)
    # conn.login("username","password")

    #选定一个邮件文件夹
    #可以用conn.list()查看都有哪些文件夹。中文的文件夹名称可能是乱码，没关系，直接拷贝过来就行了。
    # print(conn.list())

    resp, mails = conn.select("INBOX")
    print(resp, mails)
    # https://stackoverflow.com/questions/52054196/python-imaplib-search-email-with-date-and-time
    
    # total number of emails
    num_of_total_email = int(mails[0])

    #提取了文件夹中所有邮件的编号，search功能在本邮箱中没有实现……
    # resp, mails = conn.search(None,'ALL')
    counter = 0
    for i in range(num_of_total_email, num_of_total_email-N, -1):
        print('处理第', counter, '封邮件')
        counter += 1

        fetch_attachment(str(i))

    conn.close()
    conn.logout()


    #再用Pandas把数据读出来进行处理：
    # Data = pd.read_excel("C:\\文件夹名称\\" + fileName)
    #此处省略一大堆的处理
    #最后用df.to_excel()函数，把新的df保存就可以了。