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
import math

from PaSciRoAnimal import PaSciRoTiger, PaSciRoSheep, PaSciRoBird


# def stepChange(lifeform):
#     if lifeform[2] == 1:
#         lifeform[0] = lifeform[0] + random.randint(-3, 3)
#         lifeform[1] = lifeform[1] + random.randint(-3, 3)
last_x_step = None
last_y_step = None


def stepChange(animal_obj, key, positions, step_index):

    position = positions[key]
    # animal move is different accordign to speces
    x, y = position[0], position[1]
    step = animal_obj.normal_speed
    x_step = np.random.randint(-step, step, size=len(x))
    y_step = np.random.randint(-step, step, size=len(y))
    if animal_obj.myclass in ("PaSciRoSheep", "PaSciRoBird"):
        index = 0
        for x1, y1 in zip(x, y):

            # print(x1, y1, '#'*5)
            # because we kunow tiger 's position is at index = 0 at postions
            for x2, y2 in zip(positions[0][0], positions[0][1]):
                # print(x2, y2, '@'*3)
                dist = math.hypot(x2 - x1, y2 - y1)
                # print('dist=',dist, animal_obj.myclass)
                if dist < 20:
                    # run much fast , when found danger
                    print(
                        "run faster, in dangerous in distance:",
                        dist,
                        x1,
                        y1,
                        " in ",
                        x,
                        y,
                    )
                    x_step += [animal_obj.accelerated_speed] * len(x)
                    y_step += [animal_obj.accelerated_speed] * len(y)
                if dist < 3:
                    print("Collision", "#" * 20)
                    # x = np.delete(x, index)
                    # y = np.delete(y, index)
                    # sheep meet tiger, we remove it from map, it means sheep dead
                    x[index] = 500
                    y[index] = 500

                    print("removed out of map, death!")
            index += 1

    # in self species, for pregnant populations
    for x1, y1 in zip(x, y):
        for x2, y2 in zip(x, y):
            dist = math.hypot(x2 - x1, y2 - y1)
            if dist < 3:
                # print('same species, prepare for reproduction! ',animal_obj.myclass, '@'*20)
                animal_obj.set_pregnancy(True)

    tempx = x + x_step
    tempy = y + y_step
    # if this move is run , the next postion is out of boundary
    # means we don't make this move, we skip this turn's movement, next rurn to see whether run

    if np.any((tempx < 1) | (tempx > XMAX) | (tempy < 1) | (tempy > YMAX)):
        print("boundary warning!", animal_obj.myclass, tempx, tempy)
        a0 = np.nonzero(tempx < 1)
        a1 = np.nonzero(tempx > XMAX)
        a2 = np.nonzero(tempy < 1)
        a3 = np.nonzero(tempy > YMAX)
        print(a0, a1, a2, a3)

        for i in a0:
            x_step[i] = 0
        for i in a1:
            x_step[i] = 0
        for i in a2:
            y_step[i] = 0
        for i in a3:
            y_step[i] = 0

        print("x_step, y_step", x_step, y_step)

    x += x_step
    y += y_step


XMAX = 200
YMAX = 100
POP = 20
STEPS = 10


def main():
    # init 3 Alien Species: PaSciRoTiger PaSciRoSheep PaSciRoBird
    tiger = PaSciRoTiger(8, 16, "yellow", 120)
    tiger.printit()
    sheep = PaSciRoSheep(3, 6, "skyblue", 60)
    sheep.printit()
    bird = PaSciRoBird(1, 2, "red", 30)
    bird.printit()
    alien_species = {0: tiger, 1: sheep, 2: bird}

    # inital population of anmial:
    # size is bigger, the num of species should be smaller
    # Genesis time ， so we initally with less tiger, more sheep, even more birds
    pops = [POP * 3 // 20, POP * 7 // 20, POP // 2]

    positions = []
    for key, animal_obj in alien_species.items():

        x = np.random.randint(10, XMAX - 10, size=pops[key])
        y = np.random.randint(10, YMAX - 10, size=pops[key])
        print(x, y)
        positions.append([x, y])

    # simulate life after inital
    for i in range(STEPS):
        for key, animal_obj in alien_species.items():
            print("-" * 10, "turn", i, "-" * 10)
            stepChange(animal_obj, key, positions, i)
            plt.scatter(
                positions[key][0],
                positions[key][1],
                c=animal_obj.colour,
                linewidths=1,
                marker=animal_obj.shape_on_plot,
                edgecolor="green",
                s=animal_obj.size,
            )

            if animal_obj.is_pregnancy == True:
                print("reproduction", "->" * 10)
                child_x = np.random.randint(10, XMAX - 10, size=pops[key] // 4)
                child_y = np.random.randint(10, YMAX - 10, size=pops[key] // 4)
                plt.scatter(
                    child_x,
                    child_y,
                    c=animal_obj.colour,
                    linewidths=1,
                    marker=animal_obj.shape_on_plot,
                    edgecolor="yellow",
                    s=animal_obj.size // 2,
                )
        plt.xlim(0, XMAX)
        plt.ylim(0, YMAX)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show(block=False)
        plt.savefig("save_png/" + str(i) + ".png")
        # time.sleep(1)
        plt.pause(2)
        plt.close()


if __name__ == "__main__":
    main()
