# Реверсирование числа.


def reverse(n):
    n = str(n)
    return '' if n == '' else n[-1] + reverse(n[:-1])


print(reverse(12345))