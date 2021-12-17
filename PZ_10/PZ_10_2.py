# Из предложенного текстового файла (text18-1.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме, предварительно поставив последнюю строку между первой и второй.
# <<Скажи-ка, дядя, ведь не даром
# Москва, спаленная пожаром,
# Французу отдана?
# Ведь были ж схватки боевые,
# Да, говорят, еще какие!
# Недаром помнит вся Россия
# Про день Бородина!>>

# Считываем посимвольно исходный файл и проверяем каждый из элементов на заглавную букву.

flList = []
with open("text18-1.txt", "r", encoding="utf-8") as my_file:
    text = "".join(my_file.read())
    print(text)
    upper_case = 0
    for i in text.strip():
        if i.isupper():
            upper_case += 1

print(f"\n\nКолличество заглавных букв: {upper_case}\n\n")

with open('text18-1.txt', 'r+', encoding='utf-8') as main:   # В новый список помещаем построчно текст.
    text_list = main.readlines()

for i in range(len(text_list)):   # Делаем обход списка,убирая служебные знаки.
    if text_list[i] == text_list[-1]:
        flList.append(text_list[i])
    else:
        flList.append(text_list[i][0:-1])
print(flList)

flList.insert(1, flList.__getitem__(-1))   # P.s. Pycharm порекомендовал использовать этот метод.
flList.pop()   # Перемещаем последнюю строку между первой и второй.
print(flList)

with open('pz file.txt', 'w+', encoding='utf-8') as new_file:   # Вывод полученного текста.
    for line in flList:
        new_file.writelines(f"{line}\n")