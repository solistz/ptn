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
class Zodiak_class:

    def zodiak_method(self):
        zodiak = [ # масив - словник - масив
            {'vodolei':[21,49]},
            {'fish':[50,80]},
            {'oven':[81,111]},
            {'telez':[112,141]},
            {'bliznez':[142,172]},
            {'rak':[173,204]},
            {'lev':[205,235]},
            {'diva':[236,267]},
            {'vagi':[268,297]},
            {'skorpion':[298,326]},
            {'strilez':[327,356]},
            {'kozerog':[357,365]},
            {'kozerog':[1,20]}
        ]
        print(zodiak)
    

    def mounth_method(self):
        mounth = [31,28,31,30,31,30,31,31,30,31,30,31]
        print(mounth)





def main():
    zodiak_object = 
if __name__ == '__main__':
    main()