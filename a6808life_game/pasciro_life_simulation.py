#
# Author : 
# ID : 
#
# pasciroExample.py - Basic simulation of PaSciRo lifeforms for assignment, S2 2020. 
#
# Revisions: 
#
# 22/9/2019 – Base version for assignment
#

import random
import matplotlib.pyplot as plt
import numpy as np
import time

from PaSciRoAnimal import PaSciRoTiger, PaSciRoSheep, PaSciRoBird

def stepChange(lifeform):
    if lifeform[2] == 1:
        lifeform[0] = lifeform[0] + random.randint(-3, 3)
        lifeform[1] = lifeform[1] + random.randint(-3, 3)


XMAX  = 200
YMAX  = 100
POP   = 20
STEPS = 10
STEPS = 5
    
def main():
    # init 3 Alien Species: PaSciRoTiger PaSciRoSheep PaSciRoBird
    tiger = PaSciRoTiger(5, 'yellow', 120)
    tiger.printit()
    sheep = PaSciRoSheep(2, 'blue', 60)
    sheep.printit()
    bird = PaSciRoBird(8, 'red',30)
    bird.printit()
    alien_species = {0: tiger, 1: sheep, 2: bird}
    # inital population of anmial:
    # size is bigger, the num of species should be smaller
    # so we initally with less tiger, more sheep, even more birds
    pops = [POP//8, POP//4, POP*5 //8]
    for key, animal_obj in alien_species.items():

        x = np.random.randint(XMAX, size=pops[key])
        y = np.random.randint(YMAX, size=pops[key])
        plt.scatter(x, y, c =animal_obj.colour,  
            linewidths = 1,  
            marker = animal_obj.shape_on_plot,  
            edgecolor ="green",  
            s = animal_obj.size)

      
    plt.xlabel("X-axis") 
    plt.ylabel("Y-axis") 
    plt.show() 
    # lifeforms = np.zeros((POP, 3), dtype=int)
    # print('0 lifeforms=', lifeforms)
    # for i in range(POP):
    #     randX = random.randint(0,XMAX)
    #     randY = random.randint(0,YMAX)
    #     randTYPE = random.randint(0,2)
    #     lifeforms[i,0] = randX
    #     lifeforms[i,1] = randY
    #     lifeforms[i,2] = randTYPE
    #     print(lifeforms[i])
    # print('1 lifeforms=', lifeforms)
    # for i in range(STEPS):
    #     print("\n ### TIMESTEP ",i, "###")
    #     xvalues = []
    #     yvalues = []
    #     colours = []
    #     for l in lifeforms:
    #         print('l=', l)
    #         print('l[2]=', l[2])
    #         stepChange(l)
    #         #print(l)
    #         xvalues.append(l[0])
    #         yvalues.append(l[1])
    #         colours.append(l[2])
    #     print('colours=', colours)
    #     plt.scatter(xvalues, yvalues, c=colours)   # Note plt origin is bottom left 
    #     plt.xlim(0,XMAX)
    #     plt.ylim(0,YMAX)

    #     plt.show(block=False)
    #     # time.sleep(1)
    #     plt.pause(1)
    #     plt.close()
    # print('2 lifeforms=', lifeforms)


if __name__ == "__main__":
    main()

