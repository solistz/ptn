# Написать базу данных, где записи это массив словарей


#while True:
def Controller():
    a = ('\n'
    '| 1 - Create '
    '| 2 - Modify '
    '| 3 - Remove '
    '| 4 - View Dictionary |'
    '\n'
    )
    print(a)



def Create_dict_el():
    print('CREATE')

def Modify_dict_el():
    print('MODIFY')
    
def Remove_dict_el():
    pass
def View_dict_el():
    print('hellow')

def input_dict_el():
    print('ВВедіть число 1 - 4 : ')
    number = int(input())

# test commit


def main():
    print('test commit')
    dictionary_master = {}
    all_function = {Create_dict_el(), Modify_dict_el(), Remove_dict_el(), View_dict_el()}

    Controller()
    View_dict_el()
if __name__ == "__main__":
    main()