# Создать словарь содержащий подробную информацию о себе, где характеристики - это ключи, а данные - значения
dictionary_portfolio = {
    'Name' : 'Andrew',
    'First' : 'Zhydan',
    'Age' : 33,
    'Year' : 1987,
    'Month' : 7,
    'Days' : 25,
    'Height' : 164
}
# С помощью цикла for, создать словарь, где ключом будет индекс, а value - значение элемента массива
dictionary_for = {}
for index in range(int(input('Введіть кількість'))):
    dictionary_for[index] = index**index
print(dictionary_for)

# Создать словарь который будет наполнять пользователь с помощью метода input
dictionary_for = {}
while index != '':
    index = input('Введіть індекс')
    dictionary_for[index] = input('Введіть значення: ')
    print(dictionary_for)

# Создать словарь с данными, после чего пользователь вводит ключ с помощью input, 
# если ключ есть, удалить значение
dictionary_data_del_key = {1:1,2:2,3:3,4:4,5:5}
print(dictionary_data_del_key)
index_user_input = int(input('Введіть індекс'))
for index_element in dictionary_data_del_key.keys():
    if index_element == index_user_input :
        dictionary_data_del_key[index_element] = None
print(dictionary_data_del_key)



# Создать массив с 5 элементами, попытаться взять 6 элемент, 
# обработать это исключение
array_try_except = [1,2,3,4,5]
try:
    array_try_except[22]
except IndexError:
    print('is not found')

# Создать словарь, и попытаться взять значение, если значения нет, 
# вызвать исключение в котором записать ошибку в словарь

# Написать полную конструкцию тру ексепт

dictionary_data_try_except = {1:1,2:2,3:3,4:4,5:5}
try:
    index_try_except = int(input('Значення словника: '))
    dictionary_data_try_except[index_try_except]
    print('ok')
except KeyError:
    dictionary_data_try_except[index_try_except] = KeyError
    print(dictionary_data_try_except)
except ValueError:
    dictionary_data_try_except[index_try_except] = ValueError
    print(dictionary_data_try_except)
except NameError:
    dictionary_data_try_except[index_try_except] = NameError
    print(dictionary_data_try_except)
else:
    index_try_except>5
    print('WorkS')
finally:
    print('THE END')

