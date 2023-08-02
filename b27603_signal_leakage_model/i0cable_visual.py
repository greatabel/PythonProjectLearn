import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')


z = np.linspace(0, 1, 100)
theta = np.linspace(0, 2.*np.pi, 100)
r_outer = 0.1  
r_inner = 0.02  
x_outer = r_outer * np.sin(theta)
y_outer = r_outer * np.cos(theta)
x_inner = r_inner * np.sin(theta)
y_inner = r_inner * np.cos(theta)

# draw the outer cylinder
ax.plot(x_outer, y_outer, zs=0, zdir='z', color='b', linewidth=2)
ax.plot(x_outer, y_outer, zs=1, zdir='z', color='b', linewidth=2)

# draw the inner wire (central line)
ax.plot(x_inner, y_inner, zs=0, zdir='z', color='r', linewidth=5)
ax.plot(x_inner, y_inner, zs=1, zdir='z', color='r', linewidth=5)


for angle in range(0, 360, 45):
    angle_rad = np.deg2rad(angle)
    ax.plot([0, r_outer*np.sin(angle_rad)], [0, r_outer*np.cos(angle_rad)], [0, 1], color='r', linewidth=1)


for i in range(len(x_outer)-1):
    ax.plot([x_outer[i], x_outer[i+1]], [y_outer[i], y_outer[i+1]], [0, 0], color='b')
    ax.plot([x_outer[i], x_outer[i+1]], [y_outer[i], y_outer[i+1]], [1, 1], color='b')


ax.grid(False)
ax.axis('off')

# set the view angle
ax.view_init(elev=90., azim=0)

plt.show()
