class PaSciRoAnimal():
    myclass = "Animal"

    def __init__(self, mytype, colour): 
        self.mytype = mytype
        self.colour = colour


    def __str__(self):
        return (self.mytype + '|' + self.colour)

    def printit(self):
        spacing = 5 - len(self.myclass)
        print(self.myclass.upper(), spacing*' ' +
              ': ', self.type,'\tColour: ', self.colour)


class PaSciRoTiger(PaSciRoAnimal):
    myclass = "PaSciRoTiger"


class PaSciRoSheep(PaSciRoAnimal):
    myclass = "PaSciRoSheep"


class PaSciRoBird(PaSciRoAnimal):
    myclass = "PaSciRoSheepBird"