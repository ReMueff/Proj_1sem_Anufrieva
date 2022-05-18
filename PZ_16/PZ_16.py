# Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения
# товаров на оптовой базе. Таблица Товары должна содержать следующие данные: Код
# товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
# товара на складе, Единицы измерения, Оптовая цена.
# БД должна обеспечивать получение информации о товаре его наименованию.

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
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
                                         compound=tk.TOP)  # , image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        # self.update_img = tk.PhotoImage(file="BD/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP)  # , image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        # self.delete_img = tk.PhotoImage(file="BD/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                               bd=0, compound=tk.TOP)  # , image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        # self.search_img = tk.PhotoImage(file="BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP)  # , image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        # self.refresh_img = tk.PhotoImage(file="BD/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP)  # , image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=(
        'goods_id', 'goods_name', 'shop_name', 'shop_bid', 'amount', 'value', 'opt_price'), height=15, show='headings')

        self.tree.column('goods_id', width=30, anchor=tk.CENTER)
        self.tree.column('goods_name', width=130, anchor=tk.CENTER)
        self.tree.column('shop_name', width=200, anchor=tk.CENTER)
        self.tree.column('shop_bid', width=100, anchor=tk.CENTER)
        self.tree.column('amount', width=170, anchor=tk.CENTER)
        self.tree.column('value', width=120, anchor=tk.CENTER)
        self.tree.column('opt_price', width=100, anchor=tk.CENTER)

        self.tree.heading('goods_id', text='Код')
        self.tree.heading('goods_name', text='Наименование товара')
        self.tree.heading('shop_name', text='Наименование магазина')
        self.tree.heading('shop_bid', text='Заявки магазина')
        self.tree.heading('amount', text='Количество товара на складе')
        self.tree.heading('value', text='Единицы измерения')
        self.tree.heading('opt_price', text='Оптовая цена')

        self.tree.pack(side=tk.BOTTOM)

    def records(self, goods_id, goods_name, shop_name, shop_bid, amount, value, opt_price):
        self.db.insert_data(goods_id, goods_name, shop_name, shop_bid, amount, value, opt_price)
        self.view_records()

    def update_record(self, goods_id, goods_name, shop_name, shop_bid, amount, value, opt_price):
        self.db.cur.execute("""UPDATE goods SET goods_id=?, goods_name=?, shop_name=?, shop_bid=?, amount=?, value=?, 
        opt_price=? WHERE goods_name=?""", (goods_id, goods_name.lower(), shop_name, shop_bid, amount, value, opt_price,
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



    def search_records(self, good_name):
        score = (good_name,)
        self.db.cur.execute(f"""SELECT * FROM goods WHERE goods_name LIKE '%{good_name.lower()}%'""")
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
        self.geometry('400x270+400+300')
        self.resizable(False, False)

        label_id = tk.Label(self, text='Код товара')
        label_id.place(x=50, y=25)
        self.entry_id = ttk.Entry(self)
        self.entry_id.place(x=250, y=25)

        label_name_good = tk.Label(self, text='Наименование товара')
        label_name_good.place(x=50, y=50)
        self.entry_name_good = ttk.Entry(self)
        self.entry_name_good.place(x=250, y=50)

        label_name_shop = tk.Label(self, text='Наименование магазина')
        label_name_shop.place(x=50, y=75)
        self.entry_name_shop = ttk.Entry(self)
        self.entry_name_shop.place(x=250, y=75)

        label_bid = tk.Label(self, text='Заявки магазина')
        label_bid.place(x=50, y=100)
        self.entry_bid = ttk.Scale(self, from_=0, to=100, command=self.onScale)

        self.entry_bid.place(x=250, y=100)
        self.var = tk.IntVar()

        self.label_bid = Label(self, text=0, textvariable=self.var)
        self.label_bid.place(x=360, y=100)

        label_amount = tk.Label(self, text='Количество товара на складе')
        label_amount.place(x=50, y=125)
        self.entry_amount = ttk.Entry(self)
        self.entry_amount.place(x=250, y=125)

        label_value = tk.Label(self, text='Единицы измерения')
        label_value.place(x=50, y=150)
        self.entry_value = ttk.Combobox(self, values=[u'килограмм', u'штука', u'литр', u'грамм', u'миллиграмм',
                                                      u'миллилитр', u'баррель', u'тонна', u'центнер', u'метр',
                                                      u'упаковка', u'коробка'])
        self.entry_value.place(x=250, y=150)

        label_opt_price = tk.Label(self, text='Оптовая цена')
        label_opt_price.place(x=50, y=175)
        self.entry_opt_price = ttk.Entry(self)
        self.entry_opt_price.place(x=250, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=220)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=220)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_id.get(),
                                                                       self.entry_name_good.get(),
                                                                       self.entry_name_shop.get(),
                                                                       self.label_bid['text'],
                                                                       self.entry_amount.get(),
                                                                       self.entry_value.get(),
                                                                       self.entry_opt_price.get()))
        self.grab_set()
        self.focus_set()

    def onScale(self, val):
        v = int(float(val))
        self.var.set(v)


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=220)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_id.get(),
                                                                          self.entry_name_good.get(),
                                                                          self.entry_name_shop.get(),
                                                                          self.label_bid['text'],
                                                                          self.entry_amount.get(),
                                                                          self.entry_value.get(),
                                                                          self.entry_opt_price.get()))
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
            self.cur.execute("""CREATE TABLE IF NOT EXISTS goods (
                goods_id INTEGER PRIMARY KEY AUTOINCREMENT,
                goods_name TEXT NOT NULL,
                shop_name TEXT NOT NULL,
                shop_bid INTEGER,
                amount INTEGER,
                value TEXT NOT NULL,
                opt_price INTEGER
                )""")

    def insert_data(self, goods_id, goods_name, shop_name, shop_bid, amount, value, opt_price):
        self.cur.execute(
            """INSERT INTO goods (goods_id, goods_name, shop_name, shop_bid, amount, value, opt_price) VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (goods_id, goods_name.lower(), shop_name, shop_bid, amount, value, opt_price))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных Сапер")
    root.geometry("1000x450+300+200")
    root.resizable(False, False)
    root.mainloop()
