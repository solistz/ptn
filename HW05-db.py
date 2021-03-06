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


def create_db_element(db_create):
    add_dictionary_input = {}
    dictionaty_key = input('Введіть KEY : ')
    add_dictionary_input[dictionaty_key] = input('Ведіть Value : ')
    db_create.append(add_dictionary_input)
    print(db_create)


def modify_db(db_modify):
    print(db_modify)
    dictionary_key = input('Key')
    dictionary_value = input('Value')
    iteration = 0
    for index in db_modify:
        for f,d in index.items():
            if f == dictionary_key:
                print(db_modify[iteration])
                db_modify[iteration][dictionary_key] = dictionary_value
                print(db_modify[iteration][dictionary_key])
                dictionary_key = None
        iteration += 1
    if dictionary_key != None:
        print('Key is not defined')
    print(db_modify)
    

def remove_db(db_remove):
    print(db_remove)
    dictionary_key = input('Key')
    iteration = 0
    for index in db_remove:
        for f,d in index.items():
            if f == dictionary_key:
                print(db_remove[iteration])
                db_remove.pop(iteration)
                dictionary_key = None
        iteration += 1
    if dictionary_key != None:
        print('Key is not defined')
    print(db_remove)


def view_db(db_view):
    print(db_view)


def exit_db():
    print('THE END')


def main():
    db_array = []
    while True:
        user_number_input = '999'
        user_number_input = controller()
        if user_number_input == 1:
            create_db_element(db_array)
        elif user_number_input == 2:
            modify_db(db_array)
        elif user_number_input == 3:
            remove_db(db_array)
        elif user_number_input == 4:
            view_db(db_array)
        elif user_number_input == 5:
            exit_db()

    print('Finish')
if __name__ == "__main__":
    main()




