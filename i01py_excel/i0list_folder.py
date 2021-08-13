import os

path = os.getcwd()
print('path=', path)


file_list = os.listdir(path)
print(file_list)


print('分离文件主名和扩展名')
for f in file_list:
    seperate = os.path.splitext(f)
    print(seperate)


print('重命名文件和文件夹')
oldname = path + '/folder_test/test0.txt'
newname = path + '/folder_test/changed0.txt'
os.rename(oldname, newname)