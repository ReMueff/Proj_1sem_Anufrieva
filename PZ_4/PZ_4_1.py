# Даны два целых числа A и B (A < B)
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B), а также количество N этих чисел

a, b = input('Введите первое число:'), input('Введите второе число:')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Введите число заново!')
        a = input('Введите первое число:')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Введите число заново!')
        b = input('Введите второе число:')
k = 0
while a <= b:
    print(a)
    a = a + 1
    k = k + 1
print('Количество чисел:', k)