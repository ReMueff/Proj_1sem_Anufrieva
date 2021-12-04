# Дана строка, содержащая латинские буквы и скобки трех видов: «()», «[]», «{}». Если
# скобки расставлены правильно (то есть каждой открывающей соответствует
# закрывающая скобка того же вида), то вывести число 0. В противном случае вывести
# или номер позиции, в которой расположена первая ошибочная скобка, или, если
# закрывающих скобок не хватает, число —1.

my_list = list(input(f"Введите строку: "))
count_circle, count_square, count_figure = 0, 0, 0   # добавляем счётчики скобок
k = 0

# при обходе списка, если встречается открывающаяся скобка, к счётчику прибавляется единица
# в случае с закрывающейся - отнимается. Тут же проверяется
# встреча закрывающейся скобки первее.

for i in my_list:
    if i == '(':
        count_circle += 1
    elif i == ')' and count_circle > 0:
        count_circle -= 1
    elif i == ')' and count_circle <= 0:
        print(f"{my_list.index(i)}-й элемент массива: {i} нарушает порядок ")
        k +=1
        break
    elif i == '[':
        count_square += 1
    elif i == ']' and count_square > 0:
        count_square -= 1
    elif i == ']' and count_square <= 0:
        print(f"{my_list.index(i)}-й элемент массива: {i} нарушает порядок ")
        k +=1
        break
    elif i == '{':
        count_figure += 1
    elif i == '}' and count_figure > 0:
        count_figure -= 1
    elif i == '}' and count_figure <= 0:
        print(f"{my_list.index(i)}-й элемент массива: {i} нарушает порядок ")
        k +=1
        break

# в случае если всё верно - выводится первый if, если же
# не хватает закрывающейся скобки, выводится одна из последующих проверок.

if count_figure == 0 and count_square == 0 and count_circle == 0 and k ==0:
    print(f"Список не нарушает порядка")
elif count_circle > 0:
    print(f"Не хватает ')'")
elif count_square > 0:
    print(f"Не хватает ']'")
elif count_figure > 0:
    print("Не хватает '}'")