# Создать наследуемые классы для категорий машин, такие как - 

# транспорт, 
# автотранспорт, 
# машины, 
# грузовики, 

# с нужными атрибутами.

# Добавь публичные и внутренние методы связянные с этими классами
# Залить код на гитхаб, и создать Pull-Request
SIMPLE_CONSTANT = 0
CORRECT_NAMES = ['Dima', "Kolya", 'Ivan', 'Anya']
class Animal:
    name = ''
    age = 0
    sex = 'MAN'
    def __init__(self, name, age=0, sex='MAN'):
        super().__init__()
        self.name = name
        if not self._check_current_age():
            age = 0
        self.age = age
        self.sex = sex
    def _check_current_age(self):
        return self.age >= 0
    def __set_name(self, name):
        self.name = name
    def set_name(self, name):
        if name in CORRECT_NAMES:
            self.__set_name(name)
    def get_name(self):
        print(self.name)    
class Human(Animal):
    def get_name(self):
        print(self.name)
class Dog(Animal):
    age = 1
    breed = ''
    def __init__(self, name, age=0, sex='MAN', breed=None):
        super().__init__(name, age, sex)
        self.breed = breed
    def get_name(self):
        print('Wooof')
def main():
    dima = Human('Dima Lyapun', 27, 'MAN')
    dog = Dog('Jeck', 10, 'MAN', 'Terier')
    dima.set_name('Dima')
    print(dima.name)
if __name__ == '__main__':
    main()
