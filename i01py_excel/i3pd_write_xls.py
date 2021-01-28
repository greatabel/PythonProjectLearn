import os
import pandas as pd


path = os.getcwd()
openfilepath = path + '/example1.xlsx'
print(openfilepath)

data = pd.DataFrame([
    [1, 2],[3, 4], [5, 6]
    ],
    columns=['date', 'score'],
    index=['A', 'B', 'C'])
data.to_excel(openfilepath, index=False)