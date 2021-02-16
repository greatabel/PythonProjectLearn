import imaplib, email, os
import shutil
import pandas as pd
# import numpy as np
from datetime import datetime

def copy_template_file():
	template_excel = os.getcwd() + '/template/恒昌防疫防控数据统计.xlsx'
	today = (datetime.today()).strftime("%Y-%m-%d")
	result_excel = os.getcwd() + '/result/恒昌防疫防控数据统计_' + today + '.xlsx'
	shutil.copy(template_excel, result_excel)
	return result_excel


def read_template(target_excel):
	# 其实表格有5个表，我们需要处理的是3， 4
	# ['职能端异常跟踪', '业务端异常跟踪 ', '职能端', '业务端', 'Sheet1']
	df = pd.read_excel(target_excel, sheet_name=2, skiprows=[0,1,2],
						usecols="A:P", header=None)

	# table1 = pd.read_excel(template_excel, sheet_name=1, skiprows=[0,1])
	print(df)


def process_excel(target_excel):
    data = pd.read_excel(target_excel, sheet_name=0)


def loop_folder_excels():
    path = os.getcwd()
    directory = (datetime.today()).strftime("%Y-%m-%d")
    path = path + "/" + directory + "/"
    for filename in os.listdir(path):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            print(path + filename)
            # process_excel(path + filename)

if __name__ == "__main__":
	target_excel = copy_template_file()
	read_template(target_excel)
	# loop_folder_excels()
