db_array = [{1:11},{3:3},{4:4},{5:5},{6:6},{7:7}]
print(db_array)
dictionary_key = int(input('Key'))
dictionary_value = int(input('Value'))
iteration = 0
for index in db_array:
    for f,d in index.items():
        if f == dictionary_key:
            print(db_array[iteration])
            db_array[iteration][dictionary_key] = dictionary_value
            print(db_array[iteration][dictionary_key])
    iteration += 1
print(iteration)
print(db_array)
