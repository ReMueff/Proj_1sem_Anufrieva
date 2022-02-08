# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
# «произведение».


import re

with open('writer.txt', 'r+', encoding='utf-8') as file:  # Считываем нужный файл.
    text = file.read()

print(text)

p = re.compile(f"(^[А-Я]\w+|^[А-Я]\S+)\s[А-Я]\W[А-Я]\W", re.M)  # Шаблон для фамилий без инициалов.
writers = p.findall(text)  # Находим все фамилии по шаблону.

print(writers, end='\n')  # Вывод результата
print(f'Количество писателей: {len(writers)}\n\n')

text = re.sub(r'([Рр]оманов)(\s|\W)', r'произведений\2', text)  # Замена по шаблону с учётом окончаний.
text = re.sub(r'([Рр]оман)(\s|\W)', r'произведение\2', text)
text = re.sub(r'([Рр]омана)(\s|\W)', r'произведения\2', text)
text = re.sub(r'([Рр]оманы)(\s|\W)', r'произведения\2', text)

with open('new-writers-list.txt', 'w+', encoding='utf-8') as new_file:
    new_file.write(f"{text}")  # Запись результата в новый файл.
