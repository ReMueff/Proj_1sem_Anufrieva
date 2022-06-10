# Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
# последних строках и столбцах матрицы Matr2 произвольного размера.

from random import randint

# Генерация матрицы.

col_nums = randint(4, 6)
matr1 = []

matr2 = [[randint(-10, 10) for _ in range(col_nums)] for i in range(randint(4, 6))]


# В цикл for помещаем исходную матрицу без первой и последней строки.
# На каждой итеррации помещаем в новую матрицу построчно элементы.

for i in matr2[1:-1]:
    matr1.append(i[1:-1])

# Вывод результата.

for i in matr2:
    print(*i, sep='|')

print('_________________________')

for i in matr1:
    print(*i, sep='|')