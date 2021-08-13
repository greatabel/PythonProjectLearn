import xlwings as xw
import pandas as pd
import os


app = xw.App(visible = False, add_book = False)  # 启动Excel程序
path = os.getcwd()
workbook = app.books.open(path + '/example1.xlsx')  # 打开工作簿
worksheets = workbook.sheets  # 获取工作簿中的所有工作表
for i in range(len(worksheets))[:3]:  # 遍历获取到的工作表
     worksheets[i].name = worksheets[i].name.replace('Sheet', 'SheetNew')  # 重命名工作表
workbook.save(path + '/example1.xlsx')  # 另存重命名工作表后的工作簿
app.quit()  # 退出Excel程序”
