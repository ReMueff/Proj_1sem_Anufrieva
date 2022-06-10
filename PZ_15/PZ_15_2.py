# В матрице отрицательные элементы возвести в квадрат.

from random import randint

# Генерация матрицы.
new_matr = []
col_nums = randint(4, 6)

matr = [[randint(-10, 10) for _ in range(col_nums)] for i in range(randint(4, 6))]


# Циклом for проходим построчно матрицу и с применением анонимной функции возводим в квадрат отрицательные числа.
for i in matr:
    new_matr.append(list(map(lambda x: x ** 2 if x < 0 else x, i)))

for i in matr:
    print(*i, sep='|')

print('_________________________')

for i in new_matr:
    print(*i, sep='|')