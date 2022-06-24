# Вычислить сумму элементов набора чисел
my_list = [i for i in range(15)]
print(my_list)


def sum_array(arr, size):
    if size == 0:
        return 0
    else:
        return arr[size - 1] + sum_array(arr, size - 1)


print(sum_array(my_list, len(my_list)))
print(sum(my_list))