# Сформировать и вывести целочисленный список размера 10, содержащий 10 первых
# положительных нечетных чисел: 1,3,5, ... .


def count():
    my_list = []
    a = 1
    for i in range(10):
        my_list.append(a)
        a += 2
    return my_list


print(count())