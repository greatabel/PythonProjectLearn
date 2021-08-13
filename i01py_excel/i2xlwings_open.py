import os
import xlwings as xw

path = os.getcwd()



app = xw.App(visible=True, add_book=False)
openfilepath = path + '/example.xlsx'
print(openfilepath)
workbook = app.books.open(openfilepath)

#“操控工作表和单元格”
worksheet = workbook.sheets['Sheet1']
worksheet.range('A1').value='编号'



#保存工作簿
workbook.save(openfilepath)
workbook.close()
app.quit()