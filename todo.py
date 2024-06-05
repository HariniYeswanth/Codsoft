import tkinter as tk
from tkinter import messagebox
import os

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Entry widget to add new tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to update a task
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

# Function to save tasks to a file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for task in file:
                task_listbox.insert(tk.END, task.strip())

# Load tasks when the application starts
load_tasks()

# Save tasks when the application closes
root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), root.destroy()))

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Delete Task Button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Update Task Button
update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

# Run the application
root.mainloop()
