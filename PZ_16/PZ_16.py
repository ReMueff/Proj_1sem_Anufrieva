# Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения
# товаров на оптовой базе. Таблица Товары должна содержать следующие данные: Код
# товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
# товара на складе, Единицы измерения, Оптовая цена.
# БД должна обеспечивать получение информации о товаре его наименованию.

import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # self.add_img = tk.PhotoImage(file="BD/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dialog, bg='#5da130', bd=0,
                                    compound=tk.TOP) #, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        # self.update_img = tk.PhotoImage(file="BD/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP) #, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        # self.delete_img = tk.PhotoImage(file="BD/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                                    bd=0, compound=tk.TOP) #, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        # self.search_img = tk.PhotoImage(file="BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP) #, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        # self.refresh_img = tk.PhotoImage(file="BD/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                               bd=0, compound=tk.TOP) #, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('goods_id', 'goods_name', 'shop_name', 'shop_bid', 'amount', 'value', 'opt_price'), height=15, show='headings')

        self.tree.column('goods_id', width=50, anchor=tk.CENTER)
        self.tree.column('goods_name', width=180, anchor=tk.CENTER)
        self.tree.column('shop_name', width=140, anchor=tk.CENTER)
        self.tree.column('shop_bid', width=70, anchor=tk.CENTER)
        self.tree.column('amount', width=50, anchor=tk.CENTER)
        self.tree.column('value', width=50, anchor=tk.CENTER)
        self.tree.column('opt_price', width=140, anchor=tk.CENTER)

        self.tree.heading('goods_id', text='Код товара')
        self.tree.heading('goods_name', text='Наименование товара')
        self.tree.heading('shop_name', text='Наименование магазина')
        self.tree.heading('shop_bid', text='Заявки магазина')
        self.tree.heading('amount', text='Количество товара на складе')
        self.tree.heading('value', text='Единицы измерения')
        self.tree.heading('opt_price', text=' Оптовая цена')

        self.tree.pack()

    def records(self, goods_id, goods_name, shop_name, shop_bid, amount, value, opt_price):
        self.db.insert_data(goods_id, goods_name, shop_name, shop_bid, amount, value, opt_price)
        self.view_records()

    def update_record(self, goods_id, goods_name, shop_name, shop_bid, amount, value, opt_price):
        self.db.cur.execute("""UPDATE goods SET goods_id=?, goods_name=?, shop_name=?, shop_bid=?, amount=? value=? 
        opt_price=? WHERE goods_name=?""",(goods_id, goods_name, shop_name, shop_bid, amount, value, opt_price,
                                           self.tree.set(self.tree.selection()[0], '#2')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM goods""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM goods WHERE goods_name=?""", (self.tree.set(selection_item, '#2'),))
        self.db.con.commit()
        self.view_records()

    # def search_records(self, user_id):
    #     user_id = ("%" + user_id + "%",)
    #     self.db.cur.execute("""SELECT * FROM users WHERE name LIKE ?""", user_id)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, score):
        score = (score,)
        self.db.cur.execute("""SELECT * FROM goods WHERE goods_name=?""", score)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить запись')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Код товара')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=110, y=25)

        label_name = tk.Label(self, text='Наименование товара')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=110, y=50)

        label_sex = tk.Label(self, text=' Наименование магазина')
        label_sex.place(x=50, y=75)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=110, y=50)
        # self.combobox = ttk.Combobox(self, values=[u'Мужской', u'Женский'])
        # self.combobox.current(0)
        # self.combobox.place(x=110, y=75)

        label_old = tk.Label(self, text='Заявки магазина')
        label_old.place(x=50, y=100)
        self.entry_old = ttk.Entry(self)
        self.entry_old.place(x=110, y=100)

        label_score = tk.Label(self, text='Количество товара на складе')
        label_score.place(x=50, y=125)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=110, y=125)

        label_score = tk.Label(self, text='Единицы измерения')
        label_score.place(x=50, y=150)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=110, y=125)

        label_score = tk.Label(self, text='Оптовая цена')
        label_score.place(x=50, y=175)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=110, y=125)



        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_score.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_old.get(),
                                                                          self.entry_score.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('optBase.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex INTEGER NOT NULL DEFAULT 1,
                old INTEGER,
                score INTEGER
                )""")

    def insert_data(self, user_id, name, sex, old, score):
        self.cur.execute("""INSERT INTO users(user_id, name, sex, old, score) VALUES (?, ?, ?, ?, ?)""",
                             (user_id, name, sex, old, score))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных Сапер")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()