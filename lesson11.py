
#  для  того чтоб подключить ткинтер
import tkinter as tk
# regex - регулярные выражения
import re
# нужен чтоб добавить всплывающее окно
from tkinter import messagebox

def validate_login():
    email = email_entry.get()
    password = password_entry.get()

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    password_pattern = r'^(?=.*\d).{6,}$'

    if not re.match(email_pattern, email):
        messagebox.showerror("Error", "email is not correct")

    elif not re.match(password_pattern, password):
        messagebox.showerror("Error", "email is not correct")

    else: messagebox.showinfo("?????", "?????? !!!")


# чтоб начать использовать
root = tk.Tk()
# название проекта
root.title("STEP IT")
# размер проекта
root.geometry("300x180")

# какой текст хотим добавить
tk.Label(root, text="Email:").pack(pady=5)
# поля для ввода
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root)
password_entry.pack()

# для реализации кнопки
# в command добавляем функцию
tk.Button(root, text="Login", command=validate_login).pack(pady=15)

root.mainloop()
