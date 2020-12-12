import numpy as np
import matplotlib.pyplot as plt


# dy/dx = f(x,y)
# Euler formula
f = lambda x,y: y + x**2
F = lambda x: (4 * np.exp(x-1) - x**2 - 2*x - 2)
x = 1
y = -1
h = 0.1

losses = []

end = 11 
while x <= end:
    loss = F(x) - y
    # print(x, '|', F(x), '|', y, '|', loss)
    losses.append(loss)

    y = y + h * f(x, y)
    
    if  end - x < 0.0001:
        print('loss', loss, '0.01 * F(x)=', 0.01 * F(x))
        if loss < 0.01 * F(x):
            print('filed c requirement')

    x += h


plt.title('dt='+str(h))

plt.plot(np.arange(1, end+h, h), losses)
plt.plot(np.arange(1, end+h, h), losses, 'r*')
plt.show()