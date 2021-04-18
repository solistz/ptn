# Написать базу данных, где записи это массив словарей


#while True:
def controller():
    a = ('\n'
    '| 1 - Create '
    '| 2 - Modify '
    '| 3 - Remove '
    '| 4 - View Dictionary |'
    '\n'
    )
    print(a)

def input_dictionary_element():
    print('ВВедіть число 1 - 4 : ')
    number = int(input())
    return number


def create_dictionary_element():
    print('CREATE')

def modify_dictionary_element():
    print('MODIFY')
    
def remove_dictionary_element():
    pass

def view_dictionary_element():
    print('hellow')

def all_function_controller():
    pass





def main():
    #dictionary_master = {}
    controller()
    number_function = input_dictionary_element()
    print(number_function, type(number_function))
if __name__ == "__main__":
    main()

