class PaSciRoAnimal():
    myclass = "Animal"

    def __init__(self, normal_speed, colour): 
        self.normal_speed = normal_speed
        self.colour = colour


    def __str__(self):
        return (self.normal_speed + '|' + self.colour)

    def printit(self):
        spacing = 20 - len(self.myclass)
        print(self.myclass.upper(), spacing*' ' +
              ': normal_speed', self.normal_speed,'\tColour: ', self.colour)


class PaSciRoTiger(PaSciRoAnimal):
    myclass = "PaSciRoTiger"


class PaSciRoSheep(PaSciRoAnimal):
    myclass = "PaSciRoSheep"


class PaSciRoBird(PaSciRoAnimal):
    myclass = "PaSciRoSheepBird"