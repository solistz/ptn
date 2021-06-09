class Auto:

    def __init__(self,brand,model,year,odometr):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometr = odometr

    def power(self,cylinder,square,kvt):
        self.cylinder = cylinder
        self.square = square
        self.kvt = self.cylinder * self.square

    def __pass_doc(self,tehpass,vincod):
        self.tehpass = tehpass
        self.vincod = vincod

    def user_data(self):
        self.__pass_doc(input('teh'),input('vin'))
        print(self.tehpass,self.vincod)



    def info(self):
        print('||' + self.brand + ' - ' + self.model + '||' + str(self.year) + '||' + str(self.odometr) + '||')



class Car(Auto):
    
    def __init__(self,brand,model,year,odometr):
        super().__init__(brand,model,year,odometr)

    
        
    


class Bus(Auto):
    pass

class Track(Auto):
    pass

class Electro(Car):
    
    pass



suzuki = Car('Suzuki','SX-4',2019,13500)
suzuki.info()
suzuki.user_data()

fiat = Car('Fiat','Tipo',2019,11000)
fiat.info()