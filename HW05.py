import math
# Написать математические функции - 
# получение периметра круга, где аргумент это радиус,P=2πr или P=πd
def perimetr(r):
    return(2*math.pi*r)

radius = 10
perimetr = perimetr(radius)
print(perimetr)

# # площадь круга, где элемент это радиус. 
def square(r):
    return(math.pi*r**2)

square(radius)
square = square(radius)
print(square)

# Вычисление радиуса, зная его периметр, r = P/2*pi
def radius_perimetr(perimetr):
    return(perimetr/(2*math.pi))

radius_perimetr = radius_perimetr(perimetr)
print(radius_perimetr)
# вычисление радиуса зная его площадь. r = sqrt(S/pi)
def radius_square(radius):
    return(math.sqrt(square/math.pi))

radius_square = radius_square(square)
print(radius_square)

# Написать функцию - которая печатает сообщение и закрывает программу

# Написать функцию, в которой передается месяц и день рождения, а на выходе получается знак зодиака 
# (постараться сделать без if с помощью словаря!)*

# Написать функцию, в которую передается массив, а на выходе получать перевернутый массив 
# (написать свой reverse)

# Переписать прошлое задание, используя функции
