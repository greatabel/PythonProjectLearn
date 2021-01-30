import xlwings as xw
import pandas as pd
import os

path = os.getcwd()
saveto = path + '/folder_test/'

app = xw.App(visible=True, add_book=False)
for i in range(3):
	workbook = app.books.add()
	workbook.save(saveto + "test"+str(i)+".xlsx")