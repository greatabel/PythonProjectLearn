import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# x = np.linspace(0,3*np.pi,50)
# x = np.linspace(-3*np.pi,3*np.pi,50)
# print('len=',len(x))
# a = np.random.random_sample((len(x),)) * 5
# print(a)
# y1,y2 = np.sin(x),np.cos(x)
# y1 = np.sin(x) + np.cos(x) +2+ a
# y2 = np.cos(x) / 3 + 2 + a
x = np.random.uniform(low=0.1, high=0.99, size=(50,))

y = x * 0.8 + np.random.uniform(low=0.1, high=0.2, size=(50,))
# x = [0.1, 0.2, 0.3, 0.8]
# y = (x - 3)**3 - 3*x + r
plt.plot(x, y, color='blue',label='Correlation')

# plt.scatter(x, y,color='blue',label='Correlation')

# plt.show()
# plt.plot(x,y2,color='blue',label='Accurary')
plt.xlabel(u'Sensitivity')
plt.ylabel(u'Accuracy')
# plt.plot(x,y2,color='blue',label='cos(x)')

plt.legend()
plt.show()