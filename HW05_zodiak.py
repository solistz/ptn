
# Написать функцию, в которой передается месяц и день рождения,
# а на выходе получается знак зодиака 
# (постараться сделать без if с помощью словаря!)*

user_mounth = 5
user_days = 25


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
    {'kozerog':[357,365]}
]
mounth = [31,28,31,30,31,30,31,31,30,31,30,31]
ar = 1
for itm0 in range(len(mounth)):
    ar += mounth[itm0]
    if user_mounth == itm0:
        break 
ar += user_days
print(ar)


for itm1 in zodiak:
    for itm2_i,itm2_v in itm1.items():
        for itm3 in range(len(itm2_v)):
            if ar > itm2_v[0] and ar < itm2_v[1]:
                print('ok',itm2_i)
                break

                    