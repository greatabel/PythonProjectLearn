import pandas as pd


df1 = pd.DataFrame({'公司': ['恒盛', '创锐', '快学'], '分数': [90, 95, 85]})
df2 = pd.DataFrame({'公司': ['恒盛', '创锐', '京西'], '股价': [20, 180, 30]})

df3 = df1.merge(df2)
print(df1, '\n', df2, '\n\n', df3)

print('并集')
df4 =  pd.merge(df1, df2, how='outer')
print(df4)

print('如果想保留左表（df1）的全部内容，而对右表（df2）不太在意，可以将参数how设置为left')
df5 =  pd.merge(df1, df2, how='left')
print(df5)

