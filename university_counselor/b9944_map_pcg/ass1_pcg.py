'''

https://mikecgreenblog.wordpress.com/2018/05/31/the-generative-design-in-minecraft-competition-gdmc/

https://medium.com/inspired-to-program-%E3%85%82-%D9%88-%CC%91%CC%91/procedural-generation-in-python-7b75127b2f74

'''
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches



def generate_noise(width, height):
    noise_map = []
    # Populate a noise map with 0s
    for y in range(height):
        new_row = []
        for x in range(width):
            new_row.append(0)
        noise_map.append(new_row)

    # Progressively apply variation to the noise map but changing values + or -
    # 5 from the previous entry in the same list, or the average of the
    # previous entry and the entry directly above
    new_value = 0
    top_of_range = 0
    bottom_of_range = 0
    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                continue
            if y == 0:  # If the current position is in the first row
                new_value = noise_map[y][x - 1] + random.randint(-1000, +1000)
            elif x == 0:  # If the current position is in the first column
                new_value = noise_map[y - 1][x] + random.randint(-1000, +1000)
            else:
                minimum = min(noise_map[y][x - 1], noise_map[y-1][x])
                maximum = max(noise_map[y][x - 1], noise_map[y-1][x])
                average_value = minimum + ((maximum-minimum)/2.0)
                new_value = average_value + random.randint(-1000, +1000)
            noise_map[y][x] = new_value
            # check whether value of current position is new top or bottom
            # of range
            if new_value < bottom_of_range:
                bottom_of_range = new_value
            elif new_value > top_of_range:
                top_of_range = new_value
    # Normalises the range, making minimum = 0 and maximum = 1
    difference = float(top_of_range - bottom_of_range)
    print('difference=', difference, 'bottom_of_range=', bottom_of_range)
    for y in range(height):
        for x in range(width):
            noise_map[y][x] = (noise_map[y][x] - bottom_of_range)/difference
            noise_map[y][x] *= 0.6
            # noise_map[y][x] = 4
    return noise_map


blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]
snow = [255, 250, 250]
mountain = [139, 137, 137]

house_positions = []
def add_color(world):

    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.05:
                color_world[i][j] = snow
            elif world[i][j] < 0.1:
                color_world[i][j] = mountain
               
            elif world[i][j] < .20:
                color_world[i][j] = green
                house_positions.append((j,i))
            elif world[i][j] < 0.35:
                color_world[i][j] = beach
            elif world[i][j] < 1.0:
                color_world[i][j] = blue
    return color_world


shape = (500, 500)
scale = 100
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = np.random.randint(0,100)
seed = 126



def hanging_line(point1, point2):
    import numpy as np

    a = (point2[1] - point1[1])/(np.cosh(point2[0]) - np.cosh(point1[0]))
    b = point1[1] - a*np.cosh(point1[0])
    x = np.linspace(point1[0], point2[0], 100)
    y = a*np.cosh(x) + b

    return (x,y)



img = generate_noise(shape[0], shape[1])
world = np.array(img)
color_world = add_color(world).astype(np.uint8)
# Image.fromarray(color_world,'RGB').show()

fig, ax = plt.subplots()

plt.imshow(color_world)

house_count = 5
real_house_positions = []
colors = ['red', 'blue', 'DarkKhaki', 'yellow', 'pink']
for i in range(house_count):
	# Create a Rectangle patch
	rect = patches.Rectangle(house_positions[len(house_positions)*i//house_count], 10, 10, linewidth=5, 
			edgecolor=colors[i], facecolor='none')
	real_house_positions.append(house_positions[len(house_positions)*i//house_count])
	# Add the patch to the Axes
	ax.add_patch(rect)
	# if i < house_count-1:
	# 	plt.plot(house_positions[len(house_positions)*i//house_count], house_positions[len(house_positions)*(i+1)//house_count])

x, y = zip(*real_house_positions)
x = np.array(list(x))
y = np.array(list(y))

# #draw lines if you want to draw smooth lines
# from scipy.interpolate import interp1d
# x_new = np.linspace(x.min(), x.max(),500)
# f = interp1d(x, y, kind='quadratic')
# y_smooth=f(x_new)
# plot.plot(x_new, y_smooth)

plt.plot(x,y)




plt.savefig('Result.png')
# print(house_positions[0], house_positions[len(house_positions)//2], len(house_positions))

