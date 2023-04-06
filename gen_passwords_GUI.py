import secrets
import string
from tkinter import *
from tkinter import messagebox, ttk


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tip_window or not self.text:
            return

        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tip_window = Toplevel(self.widget)
        self.tip_window.wm_overrideredirect(True)
        self.tip_window.wm_geometry(f"+{x}+{y}")

        label = Label(self.tip_window, text=self.text, background="#ffffe0",
                      relief=SOLID, borderwidth=1, font=("Arial", "10", "normal"))
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None


class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title('Генератор пароля')
        self.master.geometry('350x100')
        self.master.configure(bg='#F0F0F0')
        self.master.resizable(False, False)

        name_label = Label(text='Длина', font="Arial 12", bg='#F0F0F0')
        name_label.place(x=10, y=20)

        self.name_label2 = Label(text='Пароль', font="Arial 12", bg='#F0F0F0')
        self.name_label2.place(x=10, y=60)

        self.entry_var = StringVar()
        self.entry = Entry(textvariable=self.entry_var, font="Arial 10")
        self.entry.place(x=80, y=20, height=20, width=200)
        self.entry_var.trace_add("write", self.on_entry_change)

        self.entry2 = Entry(font="Arial 10")
        self.entry2.place(x=80, y=60, height=20, width=250)
        self.entry2.bind('<Button-1>', self.copy_password)

        self.tooltip = ToolTip(self.entry2, "Нажмите для копирования пароля")

        help_button = ttk.Button(self.master, text="?", width=2)
        help_button.place(x=290, y=17)
        self.tooltip2 = ToolTip(
            help_button, "Длина пароля не более 128 символов")

    def on_entry_change(self, *args):
        ent = self.entry.get()
        if ent.isdigit() and 0 < int(ent) <= 128:
            password_length = int(ent)
            password = self.generate_password(password_length)
            self.entry2.delete(0, END)
            self.entry2.insert(0, password)
            self.name_label2.configure(text='Пароль')
            self.entry2.configure(state="normal")

        else:
            self.entry2.delete(0, END)

    def generate_password(self, length):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(chars) for _ in range(length))
        return password

    def copy_password(self, event=None):
        password = self.entry2.get()
        if password:
            root.clipboard_clear()
            root.clipboard_append(password)
            self.tooltip.hide_tooltip()
            self.entry2.delete(0, END)
            self.entry2.insert(0, "Пароль скопирован")
            self.entry2.configure(
                state="readonly", disabledbackground="#D3D3D3")
            self.entry2.configure(state="disabled")

    def reset_label_text(self):
        self.entry2.configure(
            state="normal", foreground="black", background="white")
        self.entry2.delete(0, END)
        self.entry2.insert(0, "")
        self.tooltip.show_tooltip()


if __name__ == '__main__':
    root = Tk()
    PasswordGenerator(root)
    root.mainloop()
