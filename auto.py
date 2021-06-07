class Auto:
    wheel = 4
    place = 5
    color = None
    door = 4

    def __init__(self,brand,model,year,odometr):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometr = odometr

    def power(self,cylinder,square,kvt):
        self.cylinder = cylinder
        self.square = square
        self.kvt = self.cylinder * self.square

    def info(self):
        print('||' + self.brand + ' - ' + self.model + '||' + str(self.year) + '||' + str(self.odometr) + '||')



class Car(Auto):
    
    def __init__(self,brand,model,year,odometr):
        super().__init__(brand,model,year,odometr)


class Bus(Auto):
    pass

class Track(Auto):
    pass

class Electro(Auto):
    pass

