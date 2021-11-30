# Дан список A размера N и целые числа K и L (1 < K< L < N). Переставить в обратном
# порядке элементы списка, расположенные между элементами AK и AL, не включая эти
# элементы

from random import randint


def row(n, k, l):   # Функция, разворачивающая определённую область списка.
    my_list = []
    for i in range(n):
        my_list.append(randint(1, 100))
    print(my_list)
    res_list = my_list[k:l-1]   # Находим нужный предел, используя срез списка.
    print(res_list)
    res_list.reverse()   # Разворачиваем данный предел.
    print(res_list)
    my_list[k:l-1] = res_list   # Заменяем элементы среза на необходимые.
    print(my_list)

end = int(input('Предел числового ряда:   '))
first_el = int(input('Первая граница:   '))
last_el = int(input('Вторая граница:   '))
row(end, first_el, last_el)   # Вывод полученного списка.
