# Написать базу данных, где записи это массив словарей
def controller():
    while True:
        a = ('\n'
        '| 1 - Create '
        '| 2 - Modify Value'
        '| 3 - Remove '
        '|  4 - View  '
        '|  5 - EXIT  |'
        '\n'
        )
        print(a)
        user_number_input = input('Введіть число від 1 до 5: ')
        if user_number_input.isdigit() and (int(user_number_input)>=1 and int(user_number_input)<=5):
            user_number_input = int(user_number_input)
            return user_number_input
        else:
            print('Ви ввели щось не коректно :', user_number_input)
            print('Спробуйте ще раз :')


def create_db_element(db_temp):
    add_dictionary_input = {}
    dictionaty_key = input('Введіть KEY : ')
    add_dictionary_input[dictionaty_key] = input('Ведіть Value : ')
    db_array.append(add_dictionary_input)
    print(db_array)


def modify_db():
    print(db_array)
    dictionary_key = input('Key')
    dictionary_value = input('Value')
    iteration = 0
    for index in db_array:
        for f,d in index.items():
            if f == dictionary_key:
                print(db_array[iteration])
                db_array[iteration][dictionary_key] = dictionary_value
                print(db_array[iteration][dictionary_key])
                dictionary_key = None
        iteration += 1
    if dictionary_key != None:
        print('Key is not defined')
    print(db_array)
    

def remove_db():
    print(db_array)
    dictionary_key = input('Key')
    iteration = 0
    for index in db_array:
        for f,d in index.items():
            if f == dictionary_key:
                print(db_array[iteration])
                db_array.pop(iteration)
                dictionary_key = None
        iteration += 1
    if dictionary_key != None:
        print('Key is not defined')
    print(db_array)


def main():
    db_array = []
    while True:
        user_number_input = '999'
        user_number_input = controller()
        if user_number_input == 1:
            create_db_element(db_array)
        elif user_number_input == 2:
            modify_db()
        elif user_number_input == 3:
            remove_db()
        elif user_number_input == 4:
            print(db_array)
        elif user_number_input == 5:
            print('THE END')
            break
    print('Finish')
if __name__ == "__main__":
    main()




