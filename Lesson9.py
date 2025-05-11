import tkinter as tk
import re
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

    else: messagebox.showinfo("Успех", "Прошло !!!")

root = tk.Tk()
root.title("STEP IT")
root.geometry("300x180")

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root)
password_entry.pack()

tk.Button(root, text="Login", command=validate_login).pack(pady=15)

root.mainloop()

