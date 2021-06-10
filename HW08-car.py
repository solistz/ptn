# 1. Создать наследуемые классы для 
# категорий машин, такие как - 
# 
# транспорт, 
# автотранспорт, 
# машины, грузовики, 
# 
# с нужными атрибутами.
# 2. Добавь публичные и внутренние методы связянные с этими классами
# 3. Залить код на гитхаб, и создать Pull-Request

from auto import *



suzuki = Car('Suzuki','SX-4',2019,13500)
suzuki.info()
print(suzuki.zapravka)
# suzuki.user_data()
suzuki.name = 'zap'
print(suzuki.name)
suzuki.lname = 'zh'
print(suzuki.lname)


fiat = Car('Fiat','Tipo',2019,11000)
fiat.info()
print(fiat.zapravka)
# fiat.user_data()

tesla = Electro('Tesla','M3',2018,150000)
tesla.info()
print(tesla.zapravka)




