import os
import pandas as pd
import numpy as np

# data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 
# 'r2', 'r3'], columns=['c1', 'c2', 'c3'])

data = pd.DataFrame(np.arange(1, 10).reshape(3, 3), index=['r1', 
'r2', 'r3'], columns=['c1', 'c2', 'c3'])
print(data)

print('数据的选取、筛选、排序、运算与删除等')

a = data['c1']
print('按列选取数据:\n', a, " data['c1']选取一列时返回的是一个一维的Series类型的数据 ")

b = data[['c1']]
print("返回一个二维的表格数据:\n", b)

c = data[ ['c1', 'c3'] ]
print('选取多列：\n', c)

print('-----按行选取------')
d = data[1:3]
print('选取第2～3行的数据，注意序号从0开始，左闭右开=>\n', d)

d1 = data.iloc[1:3]
print("data.iloc[1:3]=", d1)

print('区块选择')
e = data[ ['c1', 'c3'] ][0:2]
e1 = data[ ['c1', 'c3'] ].iloc[0:2]
print(e, '\n', e1)

print('数据筛选')
f = data[data['c1'] > 1]
print(f)

print('\n数据排序')
g = data.sort_values(by='c2', ascending=False)
print(g)

print('---数据运算---')
data['c4'] = data['c3'] - data['c1']
print(data)

print('--数据删除--')
a1 = data.drop(columns='c1')
print(a1)
b1 = data.drop(index=['r1', 'r3'])
print(b1)

