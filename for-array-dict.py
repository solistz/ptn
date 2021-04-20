db_array = [{1:11},{3:3},{4:4},{5:5},{6:6},{7:7}]
print(db_array)
while True:
    try:
        dictionary_key = input('Key')
        if dictionary_key != '':
            break
    except ValueError:
        print('Ви ввели : ', dictionary_key,' спробуйте ще раз')
while True:
    dictionary_value = input('Value')
    if int(dictionary_value) == int(dictionary_value):
        dictionary_value = int(dictionary_value)
        break
iteration = 0
for index in db_array:
    for f,d in index.items():
        if f == dictionary_key:
            print(db_array[iteration])
            db_array[iteration][dictionary_key] = dictionary_value
            print(db_array[iteration][dictionary_key])
            dictionary_key = 0
    iteration += 1
print(db_array)
print(dictionary_key)
