
# Написать функцию, в которой передается месяц и день рождения,
# а на выходе получается знак зодиака 
# (постараться сделать без if с помощью словаря!)*

# mounth = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

# zodiak = [
#     {'vodolei':{1:21,2:18}},
#     {'fish':{2:19,3:20}},
#     {'oven':{3:21,4:20}},
#     {'telez':{4:21,5:20}},
#     {'bliznez':{5:21,6:20}},
#     {'rak':{6:21,7:22}},
#     {'lev':{7:23,8:22}},
#     {'diva':{8:23,9:23}},
#     {'vagi':{9:24,10:23}},
#     {'skorpion':{10:24,11:21}},
#     {'strilez':{11:22,12:21}},
#     {'kozerog':{12:22,1:19}}
#     ]
mounth = [31,28,31,30,31,30,31,31,30,31,30,31]
zodiak = [
    {'vodolei':[[1,21],[2,18]]},
    {'fish':[[2,19],[3,20]]},
    {'oven':[[3,21],[4,20]]},
    {'telez':[[4,21],[5,20]]}
    # {'bliznez':{5:21,6:20}},
    # {'rak':{6:21,7:22}},
    # {'lev':{7:23,8:22}},
    # {'diva':{8:23,9:23}},
    # {'vagi':{9:24,10:23}},
    # {'skorpion':{10:24,11:21}},
    # {'strilez':{11:22,12:21}},
    # {'kozerog':{12:22,1:19}}
    ]

days_user = int(input('Введіть число'))
mounth_user = int(input('Введіть місяць'))
def operations():
    # for i in range(len(mounth)):
    #     print()
    days_in_mounth = mounth[mounth_user-1]
    print(days_in_mounth)
    for mounth_item in zodiak:
        for zodiak_element,zodiak_days in mounth_item.items():
            # print(zodiak_days)
            for zodiak_days_el in range(len(zodiak_days)):
                print(zodiak_days[zodiak_days_el])
                # for zodiak_days_el_1 in zodiak_days_el:
                #     print(zodiak_days_el[zodiak_days_el_1])


operations()