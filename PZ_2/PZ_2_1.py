# Известно, что X кг конфет стоит A рублей
# Определить, сколько стоит 1 кг и Y кг этих же конфет
x, a = input('Введите вес конфет(кг):'), input('Ваша покупка стоила(руб):')
while type(x) != float and type(a) != float:  # обработка исключений по типу данных
    try:
        x = float(x)
        a = float(a)
    except ValueError:
        print(f'Вы ввели неправильные данные! Введите ТОЛЬКО числа')
        x, a = input('Вес конфет(кг):'), input('Ваша покупка стоила(руб):')
t = a / x  # расчёт цены за кг продукта
c = int(a // x)
b = int(100 * (t - c))
print('Цена конфет за килограмм = %d рублей %d копеек' % (c, b))  # вывод цены за кг
y = input('Сколько хотите взять ещё(кг)?')  # выполнение 2-й части задания
while type(y) != float:  # обработка исключений по типу данных
    try:
        y = float(y)
    except ValueError:
        print(f'Вы ввели неправильные данные! Введите ТОЛЬКО числа')
        y = input('Сколько хотите взять ещё(кг)? ')
k = t * y  # расчёт цены за y кг продукта
g = int(k // 1)
p = int(100 * (k - g))
print('Вы должны заплатить ещё %d рублей %d копеек' % (g, p))  # вывод цены за y кг