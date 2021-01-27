import pandas as pd


a = pd.DataFrame([
    [1, 2],[3, 4], [5, 6]
    ])

print(a)

print('创建DataFrame时自定义列索引和行索引')
b = pd.DataFrame([
    [1, 2],[3, 4], [5, 6]
    ],
    columns=['date', 'score'],
    index=['A', 'B', 'C'])
print(b)

print('通过列表创建DataFrame还有另一种方式')
c = pd.DataFrame()
date = [1, 3, 5]
score = [2, 4, 6]
c['date'] = date
c['score'] = score
print(c)
