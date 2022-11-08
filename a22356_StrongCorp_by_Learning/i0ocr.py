# import camelot
# brew install ghostscript tcl-tk
# brew install libmagic

# tables = camelot.read_pdf('data/100024.pdf')
# print(tables)
import os

from termcolor import colored, cprint
import PyPDF2 

# from pdfreader import PDFDocument, SimplePDFViewer
import re
import csv




def translate(str):
    line = str.strip()  # 处理前进行相关的处理，包括转换成Unicode等
    pattern = re.compile("[^\u4e00-\u9fa50-9]")  # 中文的编码范围是：\u4e00到\u9fa5
    zh = " ".join(pattern.split(line)).strip()
    # zh = ",".join(zh.split())
    outStr = zh  # 经过相关处理后得到中文的文本
    return outStr


# get raw document
# fd = open(file_name, "rb")
# doc = PDFDocument(fd)

# # there is an iterator for pages
# page_one = next(doc.pages())
# all_pages = [p for p in doc.pages()]

# and even a viewer



def handle(name):
    # name = "0080_ltn20141022320"
    file_name = "data/" + name 

    # fd = open(file_name, "rb")
    # viewer = SimplePDFViewer(fd)
    # results_txt = ""
    # for canvas in viewer:
    #     page_images = canvas.images
    #     page_forms = canvas.forms
    #     page_text = canvas.text_content
    #     page_inline_images = canvas.inline_images
    #     page_strings = canvas.strings
    #     print("#" * 20)
    #     print('find text length=',len(page_text))

    #     # chinese_txt = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", page_text)
    #     # t = translate(page_text).strip()
    #     # print(t)
    #     # results_txt += t
    #     results_txt += page_text

    # creating a pdf file object 
    pdfFileObj = open(file_name, 'rb')
        
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        
    # printing number of pages in pdf file 
    print(pdfReader.numPages) 
        
    # creating a page object 
    pageObj = pdfReader.getPage(0) 
        
    # extracting text from page 
    content = pageObj.extractText()



    # print(pageObj.extractText()) 
        
    # closing the pdf file object 
    pdfFileObj.close() 

    textfile = open("processed_data/" + name + ".txt", "w")
    textfile.write(content)
    textfile.close()


# 获取所有文件
files = os.listdir("data/")  # 获取文件目录
print(files)
for name in files:
    handle(name)

flags1 = colored('#'*10, 'red', attrs=['reverse', 'blink'])
flags2 = colored('#'*10, 'blue', attrs=['reverse', 'blink'])
flags3 = colored('#'*10, 'yellow', attrs=['reverse', 'blink'])

def extract(name):
    mydate = None
    myamount = None
    # f = open("processed_data/" + name, "w")
    with open("processed_data/" + name, 'r') as file:
        data = file.read().replace('\n', '')
        # 日期部分 case code

        if 'THE PLACING' in data:
            start = data.index("THE PLACING") + 11
            end = start + 20
            mydate = data[start: end]
            print(flags1, mydate)
        elif 'Opening balance' in data:
            start = data.index("Opening balance") + 15
            end = start + 20
            mydate = data[start: end]
            print(flags1, mydate)

        # 数量部分 case code
        if 'Placing Shares' in data:
            end = data.index("Placing Shares") 
            start = end - 20
            myamount = data[start: end]
            print(myamount)
            myamount = re.findall(r'\d+', myamount)
            myamount = ''.join(map(str, myamount))
            print(flags2, myamount )        

        if (myamount is None or myamount == '') and  '000' in data:
            print('other branch')
            end = data.index("000") + 40
            start = end - 50
            myamount = data[start: end]
            print(myamount)
            myamount = re.findall(r'\d+', myamount)
            myamount = ''.join(map(str, myamount))
            print(flags3, myamount )        

    return mydate, myamount

prossed_files = os.listdir("processed_data/")  # 获取文件目录
print(prossed_files)

if '.DS_Store' in prossed_files:
    prossed_files.remove(".DS_Store")


mylist = ['date', 'share_amount', 'file_from']

with open('mydata.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    employee_writer.writerow(mylist)


    for name in prossed_files:
        print('>'*20, name)
        mydate, myamount = extract(name)

        if mydate is not None or myamount is not None:
            employee_writer.writerow([mydate, myamount, name])


