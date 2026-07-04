from tkinter import *
from tkinter import messagebox
import random
import string

root = Tk()
root.title("Password Generator")
root.geometry("450x250")
root.configure(bg="lightblue")

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Enter a valid length")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for i in range(length))

        password_entry.delete(0, END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a number")

Label(root, text="Password Generator",
      font=("Arial", 18, "bold"),
      bg="lightblue").pack(pady=10)

Label(root, text="Enter Password Length:",
      bg="lightblue",
      font=("Arial", 12)).pack()

length_entry = Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

Button(root,
       text="Generate Password",
       command=generate_password,
       bg="green",
       fg="white",
       font=("Arial", 12)).pack(pady=10)

password_entry = Entry(root,
                       width=35,
                       font=("Arial", 12))
password_entry.pack(pady=5)

root.mainloop()