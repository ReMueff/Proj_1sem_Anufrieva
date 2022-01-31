# Даны положительные числа A, B, C. На прямоугольнике размера A х B размещено максимально
# возможное количество квадратов со стороной C (без наложений). Найти количество квадратов,
# размещенных на прямоугольнике. Операции умножения и деления не использовать.
# Создать приложение к данной задаче в Tkinter.


from tkinter import *
from tkinter import ttk


# Функция-обработчик нажатия кнопки: вывод будет происходить путём изменения скрытого текстового поля.

def square_count():
    a = side_a.get()
    # Обработка исключений
    # (невозможно остановить выполнение функции сразу при вводе неверных параметров, решение будет показано далее)
    try:
        a = float(a)
    except ValueError:
        Fin_label.configure(text='Первая сторона введена неверно!', fg='red')

    b = side_b.get()
    try:
        b = float(b)
    except ValueError:
        Fin_label.configure(text='Вторая сторона введена неверно!', fg='red')

    c = val_c.get()
    try:
        c = float(c)
    except ValueError:
        Fin_label.configure(text='Сторона квадрата введена неверно!', fg='red')

    # В случае невозможности присваивания float типа данным, происходит повторная проверка данных и обработка ошибок).

    if type(a) != float or type(b) != float or type(c) != float:
        Fin_label.configure(text='Сторона квадрата введена неверно!', fg='red')
    elif a <= 0 or b <= 0 or c <= 0:
        Fin_label.configure(text='Введён как минимум один отрицательный показатель', fg='red')
    else:
        t = c  # присваивание первоначальных значений переменным
        p = c
        i = 0
        while t <= a:  # выполнение условия задачи
            while p <= b:
                p += c
                i += 1
            p = c
            t += c
        Fin_label.configure(text=f'Количество квадратов: {i}')


# Инициализация корневого окна приложения.

root = Tk()
root.title('Счётчик квадратов')
root.geometry('450x500')

main = Label(text='Счётчик квадратов', font=('Arial', 20)).grid(columnspan=2, row=0)

side_a = Entry(master=main, width=10)   # Добавление полей для ввода информации.
side_a.grid(row=1, column=0, pady=5, padx=5)
lab_sidea = Label(text='Введите первую сторону внешней прямоугольной области', font=('Arial', 10)).grid(row=1, column=1,
                                                                                                        pady=5)
side_b = Entry(master=main, width=10)
side_b.grid(row=2, column=0, padx=5)
lab_sideb = Label(text='Введите вторую сторону внешней прямоугольной области', font=('Arial', 10)).grid(row=2, column=1,
                                                                                                        pady=5)
val_c = Entry(master=main, width=10)
val_c.grid(row=3, column=0, padx=5)
lab_valc = Label(text='Введите сторону внутренних квадратов', font=('Arial', 10)).grid(row=3, column=1, pady=5,
                                                                                       sticky=W)
# Добавление кнопки, к которой привязан обработчик.
button = Button(text='Accept', font=('Arial', 12), command=square_count)
button.grid(row=4, columnspan=2, sticky=W + E, padx=5)

Fin_label = Label(text='', font=('Arial', 12))   # Добавление изменяемого текстового поля.
Fin_label.grid(row=5, columnspan=2)

root.mainloop()
