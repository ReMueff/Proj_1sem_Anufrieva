# Возведение числа x в степень y.


def pow_(x, y):
    return 1 if y == 0 else x * pow(x, y-1)


print(pow_(2, 4))