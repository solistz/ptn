# 1. Создать новую ветку от мастера (main) с названием feature/create_class
# 2. Переписать работу со словарем через класс
# 3. Сделать коммит и запушить ветку
# 4. Создать Pull Request
# 5. Кинуть ссылку на PR Диме, чтобы он проверил и заапрувил.
# 6. После аппрува - смерджить ветку в мастер (main)

class Class_zodiak:
    atr_zodiak = [
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
    atr_mounth = [31,28,31,30,31,30,31,31,30,31,30,31]
    summa_days = 0

    def __init__(self,_days,_mounth):
        self._days = _days
        self._mounth = _mounth -1
    
    def summa(self):
        for iteration_atr_mounth in range(len(self.atr_mounth)):
            if iteration_atr_mounth < self._mounth:
                self.summa_days += self.atr_mounth[iteration_atr_mounth]
            else:
                self.summa_days += self._days
                break
        return self.summa_days

    def output_zodiak(self):
        for iteration_atr_zodiak in self.atr_zodiak:
            for index_it_atr_zodiak,value_it_atr_zodiak in iteration_atr_zodiak.items():
                for iteration_value_it_atr_zodiak in range(len(value_it_atr_zodiak)):
                    if self.summa_days > value_it_atr_zodiak[0] and self.summa_days < value_it_atr_zodiak[1]:
                        print(index_it_atr_zodiak)
                        return



def main():
    obj_zod = Class_zodiak(int(input('Days : ')),int(input('Mounth : ')))
    # print(obj_zod._days)
    # print(obj_zod._mounth)
    # obj_zod.summa()
    print(obj_zod.summa())
    obj_zod.output_zodiak()



if __name__ == '__main__':
    main()
