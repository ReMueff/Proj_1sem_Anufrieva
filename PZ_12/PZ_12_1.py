from tkinter import *
from tkinter import ttk

My_list = ['First Name', 'Last Name', 'Email Address', 'User Name', 'Password', 'Verify Password']
y = 180

root = Tk()
root.title("Register")
root.geometry('500x700')

label = Label(text="Register", width=100, height=50, bg="black")
label.place(x=0, y=0)
Label(bg='#20242d', text='Register', fg='black', font='comforta 20').place(x=10, y=10,
                                                                           width=480, height=90)
Label(bg='#20242d').place(x=10, y=101,
                          width=480, height=570)

for i in My_list:
    Label(text=i, bg='#20242d', fg='white', font=('comforta', 10)).place(x=50, y=y)
    y += 70

Entry(bg='#13161b', fg='#444444', font=('comforta', 15)).place(x=50, y=130,
                                                               width=400, height=50)
Entry(bg='#13161b', fg='#444444', font=('comforta', 15)).place(x=50, y=200,
                                                               width=400, height=50)
Entry(bg='#13161b', fg='#444444', font=('comforta', 15)).place(x=50, y=270,
                                                               width=400, height=50)
Entry(bg='#13161b', fg='#444444', font=('comforta', 15)).place(x=50, y=340,
                                                               width=400, height=50)
Entry(bg='#13161b', fg='#444444', font=('comforta', 15)).place(x=50, y=410,
                                                               width=400, height=50)
Entry(bg='#13161b', fg='#444444', font=('comforta', 15)).place(x=50, y=480,
                                                               width=400, height=50)

Var1 = IntVar()
chk = ttk.Checkbutton(variable=Var1, onvalue=1, offvalue=0)
chk.place(x=50, y=570, anchor=CENTER)

# x=50, y=550, width=20, height=20


# chk = BooleanVar()
# chk.set(False)
# ok = Checkbutton(root, text="", var=chk).place(x=50, y=550, width=20, height=20)


label1 = Label(root, text="I agree to the Terms and Conditions", bg='#20242d', fg='#444444',
               font=('Arial Bold', 12)).place(x=60, y=555, width=300, height=30)

button = Button(root, text='Sign me UP-->', bg='#8FBC8F', fg='#006400', font=('Arial Bold', 13))
button.place(x=90, y=610, width=300, height=50)

root.resizable(width=False, height=False)
root.mainloop()
