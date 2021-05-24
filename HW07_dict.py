# 1. Создать новую ветку от мастера (main) с названием feature/create_class
# 2. Переписать работу со словарем через класс
# 3. Сделать коммит и запушить ветку
# 4. Создать Pull Request
# 5. Кинуть ссылку на PR Диме, чтобы он проверил и заапрувил.
# 6. После аппрува - смерджить ветку в мастер (main)

class Zodiak_class:
    def __init__(self,_days,_mounth):
        self._days = _days
        self._mounth = _mounth

    def met_zodiak(self):
        zodiak = [
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

    def mounth_method(self):
        mounth = [31,28,31,30,31,30,31,31,30,31,30,31]

    def met_print(self):
        print(self._days)
        print(self._mounth)

    def met_print_zodiak(self):
        # for item_zodiak in self.
        pass


def main():
    obj_zodiak = Zodiak_class(25,7)
    # obj_zodiak.met_print()



if __name__ == '__main__':
    main()
