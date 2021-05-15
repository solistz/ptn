# Написать базу данных, где записи это массив словарей
def controller():
        a = ('\n'
        '| 1 - Create '
        '| 2 - Modify Value'
        '| 3 - Remove '
        '|  4 - View  '
        '|  5 - EXIT  |'
        '\n'
        )
        print(a)

def input_in_user():
    while True:
        try:
            user_number_input = int(input('Введіть число від 1 до 5: '))
        except TypeError:
            print('Ви ввели щось не коректно : T', user_number_input)
            print('Спробуйте ще раз :')
        except KeyError:
            print('Ви ввели щось не коректно : K', user_number_input)
            print('Спробуйте ще раз :')
        except ValueError:
            print('Ви ввели щось не коректно : V', user_number_input)
            print('Спробуйте ще раз :')
        except UnboundLocalError:
            print('Ви ввели щось не коректно : U', user_number_input)
            print('Спробуйте ще раз :')
        finally:
            print('COOOOL')
    # return int(user_number_input)




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
    controller()
    input_in_user()
    print('Finish')
if __name__ == "__main__":
    main()




