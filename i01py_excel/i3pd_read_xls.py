import os
import pandas as pd


path = os.getcwd()
openfilepath = path + '/example.xlsx'
print(openfilepath)

data = pd.read_excel(openfilepath, 
					sheet_name=0)

print(data)
