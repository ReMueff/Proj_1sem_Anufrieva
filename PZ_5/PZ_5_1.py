# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
# результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится
# нуль?
a = input('Введите ваше число: ')
while type(a) != int:   # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Введите число заново!')
        a = input('Введите ваше число:')


def vichty(num):   # объявление функции
    count = 0
    while num > 0:
        p = num % 10
        count += p
        num //= 10
    return count


k = 0
while a > 0:   # проведение расчётов
    cont = vichty(a)
    a -= cont
    k += 1
    print(cont)
print('Результат: ', k)
