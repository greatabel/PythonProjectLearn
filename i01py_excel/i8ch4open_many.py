import os  # 导入os模块
import xlwings as xw  # 导入xlwings模块

path = os.getcwd()
file_path = path + '/folder_test/'


file_list = os.listdir(file_path)  # 列出路径下所有文件和子文件夹的名称
app = xw.App(visible = True, add_book = False)  # 启动Excel程序
for i in file_list:
     if os.path.splitext(i)[1] == '.xlsx':  # 判断文件夹下文件的扩展名是否为“.xlsx”
        app.books.open(file_path + '\\' + i)  # 打开工作簿”

