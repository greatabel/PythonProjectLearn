from pylab import *

# The following import line is used to use some
# special settings in the function graph_ellipse.
# You do not need to adjust anything to use graph_ellipse
import matplotlib.pyplot as plt
import math
import random
import numpy as np
import matplotlib.pyplot as plt
######################  functions are defined here ###########################
# You need to rewrite the body of each of the functions below to achieve its purpose
# You may choose to write more functions here as well.


# Do not edit the function graph_ellipse
# This function is only needed for the Advanced Section
def graph_ellipse(a, b):
    # Prints a graph of the shape of an ellipse
    # with minor axis length a and major axis b
    t = arange(0, 2 * pi, 0.01)
    xvalues = zeros(size(t))
    yvalues = zeros(size(t))
    i = 0
    while i < size(t):
        xvalues = (b / 2) * sin(t)
        yvalues = (a / 2) * cos(t)
        i = i + 1
    plt.plot(xvalues, yvalues, "b-")
    ellipse = plt.gca()
    ellipse.set_xlim(-80, 80)
    ellipse.set_ylim(-80, 80)
    ellipse.axes.xaxis.set_visible(False)
    ellipse.axes.yaxis.set_visible(False)
    print("")
    print("Huddle shape with wind direction approaching from the left")
    show()


# You need to edit each of the functions below, so they acheive their purpose
# (at the moment they clearly do not achieve their purpose!)
# You may change variable names as you see fit

mean_dict = {
'5m': [-21, -2, -45],
'6m': [-22, -5, -45],
'7m': [-24, -4, -46],
'8m': [-23, -4, -44],
'9m': [-23, -3, -46]
}

def draw_temp(mylist):
# Dataset
    x = np.array(range(0, 30))
    y = mylist
    print('-'*10, x, '@'*10, y, '#'*10)
    # Plotting the Graph
    plt.plot(x, y)
    plt.title("Curve plotted using the given points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    plt.show()

def average_winter_temp(month,day):
    addtional_t = 0
    if day > 0 and day < 15:
        addtional_t = math.sin(math.pi * day/15)
    elif day > 15 and day <= 31:
        addtional_t = -1 * math.sin(math.pi * day/31)
    t = mean_dict[month][0] + addtional_t
    return t


def winter_temp(month, day):
    t = average_winter_temp(month, day)
    while True:
        rand_t = random.randint(mean_dict[month][2],mean_dict[month][1])
        if abs(rand_t - t) < 10:
            break
    return rand_t


def generate_days_temp(month):
    mylist = []
    for i in range(30):
        t = winter_temp(month, 1)
        mylist.append(t)
    return mylist

def wind_chill(T, v):
    return 1


######################  main body of the code  ###########################

# Write the rest of your code here.
# You may call on any of the functions above


def greeting():
    welcome_str = """ 
        Welcome to 'Mother Nature, the Mother of Invention' exhibition. \n
With this exhibition we aim to instil in our patrons a sense of wonder 
at the abilities displayed by animals to withstand harsh environments. 
--------
We support two browsing modes:
1. Science Rookie
2. Science Enthusiast
"""
    patron_type = 1
    patron_type = input(
        welcome_str + "Dear patrons, you can choose your type (1 or 2):"
    )
    introd = """
Penguins are flightless birds, with flippers instead of wings, adapted to living in a marine environment. 
The emperor penguin is the only bird that breeds during the Antarctic winter. 
They breed on sea ice which is well away from the ocean where these penguins feed. 
"""
    introd_temperatures = """
winter starts in May and lasts until Sept in Antarctic.
Please choose a month to see temperatures(for example:  5m, 6m, 7m, 8m, 9m):?
"""
    print(
        "You choosed ",
        patron_type,
        "\n------------------------------------------------",
        introd,
        "\n------------------------------------------------"

    )
    month = 'May'
    month = input(
         introd_temperatures
    )
    if patron_type == 1:
        print('just 1')
    else:
        mylist = generate_days_temp('5m')
        draw_temp(mylist)



def main():
    greeting()


if __name__ == "__main__":
    main()

######################  Bibliography (Optional)  ###########################
# If you used sources other than those in the task sheet,
# then include references as comments
