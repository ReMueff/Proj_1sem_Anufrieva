# Используя словарь посчитать количество уникальных слов в заданном
# предложении «Изучаем язык Питон». Вывести на экран каждую пару
# «ключ:значение»
equal_words = []
dictionary = {}
my_list = list(input(f'Введите строку:   ').split(' '))   # делим список на отдельные слова
print(my_list)

# при обходе списка идёт проверка на уникальность слова, в негативном исходе к счётчику прибавляется 1

for i in my_list:
    if i not in equal_words:
        equal_words.append(i)
        dictionary[i] = 1
    elif i in equal_words:
        dictionary.update({f'{i}' : dictionary[i]+1})

print(dictionary)   # вывод словаря