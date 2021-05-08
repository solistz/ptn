def zodiaks(day,mounth_user): #функція
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
    mounth = [31,28,31,30,31,30,31,31,30,31,30,31]

    for mounth_iteration in range(len(mounth) - (len(mounth) - mounth_user)):
        day += mounth[mounth_iteration]

    for zodiak_iteration in zodiak:
        for zodiak_iteration_dict_index,zodiak_iteration_dict_value in zodiak_iteration.items():
            # print(zodiak_iteration_dict_index, zodiak_iteration_dict_value)
            for zodiak_iteration_list in range(len(zodiak_iteration_dict_value)):
                if day > zodiak_iteration_dict_value[0] and day < zodiak_iteration_dict_value[1]:
                        print(zodiak_iteration_dict_index)
                        break


zodiaks(int(input('Day : ')),int(input('Mounth : ')) - 1)
