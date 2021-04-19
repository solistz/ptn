db_array = [{1:1},{2:2},{3:3},{4:4},{5:5},{6:6},{7:7}]
dictionary_key = int(input())
for index in db_array:
    for f,d in index.items():
        if f == dictionary_key:
            print(db_array[f-1])
            db_array[f-1][dictionary_key] = dictionary_value
            print(db_array[f-1][dictionary_key])
print(db_array)
        
