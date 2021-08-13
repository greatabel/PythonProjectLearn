import os
import xlwings as xw

path = os.getcwd()
# print('path=', path)

#创建工作簿 
app = xw.App(visible=True, add_book=False)
workbook = app.books.add()

saveto = path + '/example.xlsx'
print(saveto)
#保存工作簿
workbook.save(saveto)
workbook.close()
app.quit()