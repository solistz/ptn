# Написать функцию, в которую передается массив, а на выходе получать перевернутый массив 
# (написать свой reverse)
array = [1,2,3,4,5,6,7,8,9,10]
print(array)

def array_revers(arr):
    # temp = arr.pop(1)
    # arr[10] = 
    # print(temp)
    # print(arr[-1])
    number = len(arr) - 1
    temp_array = []
    for iterators in range(number,-1,-1):
    #    print(iterators, arr[iterators])
        temp_array.append(arr[iterators])
    arr = temp_array
    print(arr)


array_revers(array)
