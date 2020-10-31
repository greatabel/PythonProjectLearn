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


# def stepChange(lifeform):
#     if lifeform[2] == 1:
#         lifeform[0] = lifeform[0] + random.randint(-3, 3)
#         lifeform[1] = lifeform[1] + random.randint(-3, 3)
def stepChange(animal_obj, position):
    # animal move is different accordign to speces
    x, y = position[0], position[1]
    x_step = np.random.randint(-animal_obj.normal_speed, animal_obj.normal_speed, size=len(x))
    y_step = np.random.randint(-animal_obj.normal_speed, animal_obj.normal_speed, size=len(y))
    x += x_step
    y += y_step
    # if this move is run , the next postion is out of boundary 
    # means we don't make this move, we skip this turn's movement, next rurn to see whether run

    if np.any((x < 1)|(x > XMAX )|(y < 1 )|(y > YMAX )):
        print('boundary warning!', x)
        x -= x_step
        y -= y_step

XMAX  = 200
YMAX  = 100
POP   = 20
STEPS = 10
# STEPS = 5
    
def main():
    # init 3 Alien Species: PaSciRoTiger PaSciRoSheep PaSciRoBird
    tiger = PaSciRoTiger(8, 'yellow', 120)
    tiger.printit()
    sheep = PaSciRoSheep(2, 'skyblue', 60)
    sheep.printit()
    bird = PaSciRoBird(1, 'red',30)
    bird.printit()
    alien_species = {0: tiger, 1: sheep, 2: bird}

    # inital population of anmial:
    # size is bigger, the num of species should be smaller
    # Genesis time ， so we initally with less tiger, more sheep, even more birds
    pops = [POP//6, POP//3, POP//2]

    positions = []
    for key, animal_obj in alien_species.items():

        x = np.random.randint(XMAX, size=pops[key])
        y = np.random.randint(YMAX, size=pops[key])
        print(x, y)
        positions.append([x, y])

    # simulate life after inital 
    for i in range(STEPS):
        for key, animal_obj in alien_species.items():    
            stepChange(animal_obj,positions[key])
            plt.scatter(positions[key][0], positions[key][1], c =animal_obj.colour,  
                linewidths = 1,  
                marker = animal_obj.shape_on_plot,  
                edgecolor ="green",  
                s = animal_obj.size)

        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        plt.xlabel("X-axis") 
        plt.ylabel("Y-axis") 
        plt.show(block=False)
        plt.savefig('save_png/' + str(i) + '.png')
        # time.sleep(1)
        plt.pause(2)
        plt.close()

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

