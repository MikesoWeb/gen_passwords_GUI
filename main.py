import string
from tkinter import *

chars = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

root = Tk()
root.title('Генератор пароля')
root.geometry('550x170')


def gen_pass():
    import random
    password = ''
    entry2.delete(0, END)

    for j in range(int(get_number())):
        password += random.choice(chars)
    print(password)
    return password


def insert_data():
    entry2.delete(0, END)
    entry2.insert(0, gen_pass())

    return entry2


def get_number():
    ent = entry.get()
    if not ent:
        ent = 24
        entry.insert(INSERT, ent)
    return ent


name_label = Label(text='Длина', font="Courier 12 italic")
name_label.grid(row=0, column=0, padx=10, pady=20, ipadx=10, sticky="w")

name_label2 = Label(text='Пароль', font="Courier 12 italic")
name_label2.grid(row=1, column=0, padx=10, pady=20, ipadx=10, sticky="w")

entry = Entry()
entry.grid(row=1, column=1, padx=5, pady=5)
entry.place(x=500, y=30, height=20, width=400, anchor="e")

entry2 = Entry()
entry2.grid(row=1, column=1, padx=10, pady=10)
entry2.place(x=500, y=100, height=20, width=400, anchor="e")

button = Button(text='Отправить', command=insert_data, font="Courier 12 italic")

button.grid()
button.place(x=400, y=120)
root.mainloop()
