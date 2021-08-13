from pylab import *

# The following import line is used to use some
# special settings in the function graph_ellipse.
# You do not need to adjust anything to use graph_ellipse
import matplotlib.pyplot as plt
import math
import random
# import numpy as np
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
    # x = np.array(range(0, 30))
    x = list(range(0, 30))
    y = mylist
    # print('-'*10, x, '@'*10, y, '#'*10)
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


def winter_temp(month, day, hour=0):
    t = average_winter_temp(month, day)
    # print('t=', t)
    while True:
        rand_t = t + random.randint(mean_dict[month][2],mean_dict[month][1])/20
        # rand_t = t
        ran_h = randint(0, 2) * hour/ 24
        rand_t = rand_t + ran_h
        if abs(rand_t - t) < 10:
            break
    return rand_t


def generate_days_temp(month):
    mylist = []
    for i in range(30):
        t = winter_temp(month, i)
        mylist.append(t)
    return mylist

def wind_chill(T, v):
    a = 13.112 + 0.6215*T - 11.37*math.pow(v, 0.16) + 0.3965*math.pow(v, 0.16)
    return a


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
0. Science Rookie
1. Science Enthusiast
"""
    patron_type = 0
    patron_type = input(
        welcome_str + "Dear patrons, you can choose your type (0 or 1):"
    )
    patron_type = int(patron_type)
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
    if patron_type == 0:
        print('let us continue')
    else:
        mylist = generate_days_temp('5m')
        draw_temp(mylist)

    day = 0
    day = input(
        "Dear patrons, you can input a day of your choosed month (1~30):"
    )
    hour = 0
    hour = input(
        "Dear patrons, you can input an hour of your choosed day (1~24):"
    )
    temperature = winter_temp(month, int(day), int(hour))
    print('temperature we predict is: ', temperature)
    speed = 0
    speed = input(
        "Dear patrons, you can input speed of weed (unit is km/h):"
    )
    at = wind_chill(temperature, int(speed))
    print('The wind chill we predict is: ', at)



def main():
    while True:
        greeting()
        user_input = input("Would you like to continue to choose month(y/n):")
        if user_input == "n":
            print('*'*20)
            print('Thank you for using our platform, see you next time')
            print('*'*20)
            break


if __name__ == "__main__":
    main()

######################  Bibliography (Optional)  ###########################
# If you used sources other than those in the task sheet,
# then include references as comments
