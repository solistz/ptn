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

    def modyfi_data_base(self):
        print('modify')

    def remove_data_base(self):
        print('delete')

    def view_data_base(self):
        print('view')
    
    def exit_data_base(self):
        print('view')
        return 0



def main():
    item = 1
    while item ==1:
        test = user_number()
        print('ви ввели', test)

        db = Data_Base()

        if test == 1 :
            db.create_data_base()
        elif test == 2:
            db.modyfi_data_base()
        elif test == 3:
            db.remove_data_base()
        elif test == 4:
            db.view_data_base()
        elif test == 5:
            ttt = db.exit_data_base()
            print(ttt)
            item = ttt
    
if __name__ == '__main__':
    main()