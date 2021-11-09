# Даны положительные числа A, B, C. На прямоугольнике размера A х B размещено максимально
# возможное количество квадратов со стороной C (без наложений). Найти количество квадратов,
# размещенных на прямоугольнике. Операции умножения и деления не использовать
a, b, c = input('Введите значение A:'), input('Введите значение B:'), input("Введите значение C:")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Введите значение заново!')
        a = input('Введите значение A:')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Введите значение заново!')
        b = input('Введите значение B:')
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Введите значение заново!')
        c = input('Введите значение C:')
t = c
p = c
i = 0
while t <= a:
    while p <= b:
        p += c
        i += 1
    p = c
    t += c
print(i)

