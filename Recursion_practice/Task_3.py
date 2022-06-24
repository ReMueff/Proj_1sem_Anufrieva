# Вычисление суммы чисел с поддержкой вложенных списков.


from random import randint


def my_sum(array_):
    summa = 0
    for k in array_:
        if not isinstance(k, list):
            summa = summa + k
        else:
            summa = summa + my_sum(k)
    return summa


my_list = [[randint(-20, 20) for i in range(7)] for j in range(5)]
for i in my_list:
    print(i)


print(my_sum(my_list))