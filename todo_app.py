import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=0, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1)

listbox = tk.Listbox(root, width=45)
listbox.pack(pady=10)

del_button = tk.Button(root, text="Delete Task", command=delete_task)
del_button.pack()

root.mainloop()
