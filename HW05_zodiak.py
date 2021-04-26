
# Написать функцию, в которой передается месяц и день рождения,
# а на выходе получается знак зодиака 
# (постараться сделать без if с помощью словаря!)*

mounth = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# mounth = [31,28,31,30,31,30,31,31,30,31,30,31]

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

zodiak = [
    {'vodolei':[{1:21},{2:18}]},
    {'fish':[{2:19},{3:20}]},
    {'oven':[{3:21},{4:20}]},
    {'telez':[{4:21},{5:20}]},
    {'bliznez':[{5:21},{6:20}]},
    {'rak':[{6:21},{7:22}]},
    {'lev':[{7:23},{8:22}]},
    {'diva':[{8:23},{9:23}]},
    {'vagi':[{9:24},{10:23}]},
    {'skorpion':[{10:24},{11:21}]},
    {'strilez':[{11:22},{12:21}]},
    {'kozerog':[{12:22},{1:19}]}

]

user_mounth = 7
user_days = 25
# b = 0
# for a in mounth:
#     # print(a)
#     if a == user_mounth:
#         print(b)
#         break

for zodiak_elem_dict in zodiak:
    # print(item)
    for zodiak_index,zodiak_value in zodiak_elem_dict.items():
        # print(bb)
        for zodiak_value_array in zodiak_value:
            # print(zodiak_value[0])
            for zodiak_value_array_index,zodiak_value_array_value in zodiak_value_array.items():
                if zodiak_value_array_index==user_mounth:
                    print(zodiak_index, zodiak_value_array)



