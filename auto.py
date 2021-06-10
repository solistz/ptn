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
        self.lname = lname
        self.tehpass = tehpass
        self.vincod = vincod

    def user_data(self):
        self.name = name
        self.__pass_doc(input('teh'),input('vin'))
        print(self.tehpass,self.vincod)



    def info(self):
        print('||' + self.brand + ' - ' + self.model + '||' + str(self.year) + '||' + str(self.odometr) + '||')



class Car(Auto):
    zapravka = "benzin"
    
    def __init__(self,brand,model,year,odometr):
        super().__init__(brand,model,year,odometr)

        
    


class Bus(Auto):
    pass

class Track(Auto):
    pass

class Electro(Car):
    zapravka = 'energy'
    # self.zapravka = 'energy'
    def __init__(self,brand,model,year,odometr):
        super().__init__(brand,model,year,odometr)


