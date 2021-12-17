# import camelot
# brew install ghostscript tcl-tk
# brew install libmagic

# tables = camelot.read_pdf('data/100024.pdf')
# print(tables)
from pdfreader import PDFDocument, SimplePDFViewer
import re

name = "16.QSY1002.1-2013健康、安全与环境管理体系第1部分：规范"


name = "QSY1142-2008 井下作业设计规范"
name = "QSYXJ0059-2009(2014)采气井口及集气站操作规范"

file_name = "data/" + name + ".pdf"


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
fd = open(file_name, "rb")
viewer = SimplePDFViewer(fd)
results_txt = ""
for canvas in viewer:
    page_images = canvas.images
    page_forms = canvas.forms
    page_text = canvas.text_content
    page_inline_images = canvas.inline_images
    page_strings = canvas.strings
    print("#" * 20)
    # chinese_txt = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", page_text)
    t = translate(page_text).strip()
    print(t)
    results_txt += t

textfile = open("processed_data/" + name + ".txt", "w")
textfile.write(results_txt)
textfile.close()
