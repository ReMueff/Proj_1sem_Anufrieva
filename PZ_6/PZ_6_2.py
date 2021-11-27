# Дан список размера N. Найти номера тех элементов списка, которые больше своего
# правого соседа, и количество таких элементов. Найденные номера выводить в порядке
# их возрастания.
from random import randint


# def row(n):
#     counter_list = []
#     counter = []
#     my_list = [randint(1, 100) for i in range(n)]
#     dictionary = {}
#     print(my_list)
#     for i in range(1, n):
#         # my_list.append(randint(1, 100))
#         if my_list[i - 1] > my_list[i]:
#             print(i - 1)
#     # print(my_list)
#     # for i in my_list:
#     #     if i > i+1:
#     #         print(i)
#     #         # dictionary.update({'my_list[i]' : i})
#     #     # else:
#     #     #     continue
#     # #  dictionary = dict(zip(counter_list, counter))
#     # return dictionary
#
#
# row(int(input(f"Введите предел числового ряда")))


def row(n):
    my_list = []
    inn = 1
    counter = []
    counter_list = []
    count = 0
    for i in range(n):
        my_list.append(randint(1, 100))
    print(my_list)
    for i in range(int(len(my_list)) - 1):
        if my_list[i] > my_list[inn]:
            counter.append(inn - 1)
            counter_list.append(my_list[i])
            count += 1
        inn += 1
    dictionary = dict(zip(counter, counter_list))
    return dictionary, count

final_dict, final_count = (row(int(input(f'Введите предел числового ряда:  '))))

print(f'\nКоличество: {final_count}. \n\nПоследовательность: {final_dict}')

