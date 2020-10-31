class PaSciRoAnimal():
    myclass = "Animal"
    shape_on_plot = None

    def __init__(self, normal_speed, colour='yellow', size=2): 
        self.normal_speed = normal_speed
        self.colour = colour
        # size of the body
        self.size = size


    def __str__(self):
        return (self.normal_speed + '|' + self.colour)

    def printit(self):
        spacing = 20 - len(self.myclass)
        print(self.myclass.upper(), spacing*' ' +
              ': normal_speed', self.normal_speed,'\tColour: ', self.colour,
              '\size: ',self.size)


class PaSciRoTiger(PaSciRoAnimal):
    myclass = "PaSciRoTiger"
    shape_on_plot = "H"


class PaSciRoSheep(PaSciRoAnimal):
    myclass = "PaSciRoSheep"
    shape_on_plot = "P"


class PaSciRoBird(PaSciRoAnimal):
    myclass = "PaSciRoSheepBird"
    shape_on_plot = "^"