# Описать функцию PowerA234(параметры), вычисляющую вторую, третью и четвертую
# степень числа A и возвращающую эти степени соответственно в переменные B, C и D. С
# помощью этой функции найти вторую, третью и четвертую степень пяти данных чисел.


def PowerA234(num):   #
    step2 = 0
    step3 = 0
    step4 = 0
    step2 = num ** 2
    step3 = num ** 3
    step4 = num ** 4
    print(f"\n\033[3m\033[33m Число = {num} : вторая степень = {step2}, третья степень = {step3}, четвёртая степень = {step4}")


a = 'fill'   #
List = []
while a != '':
    a = input(f"\033[36mВведите число:\033[0m ")
    List.append(a)
    if List[-1] == '':
        List.pop()
    print(List)

counter = 0   #
while counter != len(List):
    PowerA234(int(List[counter]))
    counter += 1
