import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = np.linspace(-3*np.pi,3*np.pi,50)
print('len=',len(x))
a = np.random.random_sample((len(x),)) * 5
print(a)
# y1,y2 = np.sin(x),np.cos(x)
y1 = np.sin(x) + np.cos(x) + a
y2 = np.tan(x) / 3 - a

plt.plot(x,y1,color='red',label='Sensitivity')
plt.plot(x,y2,color='blue',label='Accurary')
plt.xlabel(u'distance')
# plt.ylabel(u'')
# plt.plot(x,y2,color='blue',label='cos(x)')

plt.legend()
plt.show()