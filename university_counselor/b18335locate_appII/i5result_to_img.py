import numpy as np
import matplotlib.pyplot as plt


names = ['gps', 'wifi', 'knn-combine-lg']
values = [89, 91, 95]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('accuracy compare')
plt.show()