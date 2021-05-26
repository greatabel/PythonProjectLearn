from pylab import *

# The following import line is used to use some 
# special settings in the function graph_ellipse.
# You do not need to adjust anything to use graph_ellipse
import matplotlib.pyplot as plt


######################  functions are defined here ###########################  
# You need to rewrite the body of each of the functions below to achieve its purpose
# You may choose to write more functions here as well.


# Do not edit the function graph_ellipse
# This function is only needed for the Advanced Section
def graph_ellipse(a,b):
    # Prints a graph of the shape of an ellipse
    # with minor axis length a and major axis b
    t = arange(0, 2*pi, 0.01)
    xvalues = zeros(size(t))
    yvalues = zeros(size(t))
    i = 0
    while i < size(t):
        xvalues = (b/2)*sin(t)
        yvalues = (a/2)*cos(t)
        i = i+1
    plt.plot(xvalues, yvalues, 'b-')
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

def average_winter_temp(day):
    return 1

def winter_temp(t):
    return 1
      
def wind_chill(T, v):
    return 1
    
######################  main body of the code  ###########################

# Write the rest of your code here.  
# You may call on any of the functions above
def main():
    ''

if __name__ == "__main__":
    main()

######################  Bibliography (Optional)  ###########################
# If you used sources other than those in the task sheet, 
# then include references as comments