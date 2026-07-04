from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List")
root.geometry("500x500")
root.configure(bg="lightblue")

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except:
        messagebox.showwarning("Warning", "Select a task!")

Label(root, text="TO-DO LIST", font=("Arial", 20, "bold"),
      bg="lightblue").pack(pady=10)

entry = Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

Button(root, text="Add Task", bg="green", fg="white",
       width=15, command=add_task).pack(pady=5)

listbox = Listbox(root, width=30, height=10, font=("Arial", 14))
listbox.pack(pady=10)

Button(root, text="Delete Task", bg="red", fg="white",
       width=15, command=delete_task).pack(pady=5)

root.mainloop()