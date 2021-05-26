# 1. Создать новую ветку от мастера (main) с названием feature/create_class
# 2. Переписать работу со словарем через класс
# 3. Сделать коммит и запушить ветку
# 4. Создать Pull Request
# 5. Кинуть ссылку на PR Диме, чтобы он проверил и заапрувил.
# 6. После аппрува - смерджить ветку в мастер (main)
def user_number():
    while True:
        try:
            user_number_input = int(input('Введіть число від 1 до 5: '))
            break
        except TypeError:
            print('Ви ввели щось не коректно : T')
            print('Спробуйте ще раз :')
        except KeyError:
            print('Ви ввели щось не коректно : K')
            print('Спробуйте ще раз :')
        except ValueError as e:
            print('Ви ввели щось не коректно : V',e)
            print('Спробуйте ще раз :')
        except UnboundLocalError:
            print('Ви ввели щось не коректно : U')
            print('Спробуйте ще раз :')
        except NameError as e:
            print('Ви ввели щось не коректно : U',e)
            print('Спробуйте ще раз :')
    return(user_number_input)


class Data_Base:
    db_key = None
    db_value = None
    db_array = []
    db_dictionary = {}
    iteration = 0
    def __init__(self):
        number = ('\n'
        '| 1 - Create '
        '| 2 - Modify Value'
        '| 3 - Remove '
        '|  4 - View  '
        '|  5 - EXIT  |'
        '\n'
        )
        print(number)


    def create_data_base(self):
        print('create')
        add_dictionary_input = {}
        dictionaty_key = input('Введіть KEY : ')
        add_dictionary_input[dictionaty_key] = input('Ведіть Value : ')
        self.db_array.append(add_dictionary_input)
        print(self.db_array)

    def modyfi_data_base(self):
        print('modify')
        dictionary_key = input('Key')
        dictionary_value = input('Value')
        iteration = 0
        for index in self.db_array:
            for f,d in index.items():
                if f == dictionary_key:
                    print(self.db_array[iteration])
                    self.db_array[iteration][dictionary_key] = dictionary_value
                    print(self.db_array[iteration][dictionary_key])
                    dictionary_key = None
            iteration += 1
        if dictionary_key != None:
            print('Key is not defined')
        print(self.db_array)


    def remove_data_base(self):
        print('delete')
        dictionary_key = input('Key')
        iteration = 0
        for index in self.db_array:
            for f,d in index.items():
                if f == dictionary_key:
                    print(self.db_array[iteration])
                    self.db_array.pop(iteration)
                    dictionary_key = None
            iteration += 1
        if dictionary_key != None:
            print('Key is not defined')
        print(self.db_array)


    def view_data_base(self):
        print(self.db_array)
    
    def exit_data_base(self):
        return 0



def main():
    item = 1
    db = Data_Base()
    while item ==1:
        number = user_number()
        print('ви ввели', number)
        if number == 1 :
            db.create_data_base()
        elif number == 2:
            db.modyfi_data_base()
        elif number == 3:
            db.remove_data_base()
        elif number == 4:
            db.view_data_base()
        elif number == 5:
            item_db_exit = db.exit_data_base()
            item = item_db_exit
    
if __name__ == '__main__':
    main()