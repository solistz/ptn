# Создать наследуемые классы для категорий машин, такие как - 

# транспорт, 
# автотранспорт, 
# машины, 
# грузовики, 

# с нужными атрибутами.

# Добавь публичные и внутренние методы связянные с этими классами
# Залить код на гитхаб, и создать Pull-Request

class Cars:
    sm_cub = 1
    n_cil = 4
    horse_power = 100
    fuel = 'aaa'
    def engine(self,sm_cub,n_cil,horse_power,fuel=''):
        self.sm_cub = sm_cub
        self.n_cil = n_cil
        self.horse_power = horse_power
        self.fuel = fuel
    def wheel(self,weight_wheel,hight_wheel,radius_wheel):
        self.weight_wheel = weight_wheel
        self.hight_wheel = hight_wheel
        self.radius_wheel = radius_wheel
    def weight(self,kilogram):
        self.kilogram = kilogram

class Transport(Cars):
    def motorcycle():
        pass
    def car():
        pass

class Truck(Cars):
    pass


def main():
    suzuki = Transport()
    suzuki.engine(1,2,3,4)
    print(suzuki.fuel)
if __name__ == '__main__':
    main()