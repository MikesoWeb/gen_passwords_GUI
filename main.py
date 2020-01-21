from tkinter import *
from tkinter import messagebox
 
 


def generate():
  pass  
 
root = Tk()
root.title("Генератор паролей 2020")
root.geometry("450x150+150+100")

 
name_label = Label(text="Длинна пароля:")
name_label.grid(row=0, column=0, padx=10, pady=20, ipadx=10, sticky="w")
name_label = Label(text="Ваш пароль:")
name_label.grid(row=1, column=0, padx=10, pady=0, ipadx=10,sticky="w")

 
 
name_entry = Entry()
name_entry1 = Entry()

name_entry.grid(row=0,column=1, padx=5, pady=5)
name_entry1.grid(row=1,column=1, padx=5, pady=5)
name_entry.place(x=430, y=30, height=30, width=130, anchor="e")
name_entry1.place(x=430, y=70, height=30, width=300, anchor="e")

 
# вставка начальных данных
name_entry.insert(0,"")
name_entry1.insert(0, "Здесь будет пароль")


 

gen_button = Button(text="Сгенерировать", command=generate)
 


gen_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()