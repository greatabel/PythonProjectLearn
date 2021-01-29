import xlwings as xw
import pandas as pd
import os

path = os.getcwd()
saveto = path + '/example1.xlsx'

app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add('新工作表')
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
worksheet.range('A1').value = df
workbook.save(saveto)
workbook.close()
app.quit()