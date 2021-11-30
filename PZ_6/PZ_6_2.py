# Дан список размера N. Найти номера тех элементов списка, которые больше своего
# правого соседа, и количество таких элементов. Найденные номера выводить в порядке
# их возрастания.

# В ходе решения данной задачи был сделан упор на универсальность и практичность
# вывода результата путём соединения идентификатора числа и самого числа в 
# словарь. (Хотела показать нестандартное решение)

from random import randint


def row(n):   # Функция, находящая необходимые элементы и их идентификаторы.
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
# Соединение двух списков в словарь.
    dictionary = dict(zip(counter, counter_list))
    return dictionary, count

final_dict, final_count = (row(int(input(f'Введите предел числового ряда:  '))))

print(f'\nКоличество: {final_count}. \n\nПоследовательность: {final_dict}')

