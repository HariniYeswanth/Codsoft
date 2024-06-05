import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid positive integer for the password length.")
        return
    
    characters = ""
    
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if digits_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation
    
    if not characters:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Generated Password: {password}")

# Function to reset the inputs and result label
def reset():
    length_entry.delete(0, tk.END)
    uppercase_var.set(False)
    lowercase_var.set(False)
    digits_var.set(False)
    special_var.set(False)
    password_label.config(text="Generated Password: ")

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg='#e1f5fe')

# Entry widget for the password length
length_label = tk.Label(root, text="Password Length:", bg='#e1f5fe', font=("Arial", 12))
length_label.pack(pady=10)
length_entry = tk.Entry(root, width=30)
length_entry.pack(pady=5)

# Checkboxes for character types
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

uppercase_check = ttk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack(pady=5)

lowercase_check = ttk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack(pady=5)

digits_check = ttk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack(pady=5)

special_check = ttk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack(pady=5)

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='#29b6f6', fg='white', font=("Arial", 12))
generate_button.pack(pady=20)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset, bg='#9e9e9e', fg='white', font=("Arial", 12))
reset_button.pack(pady=10)

# Label to display the generated password
password_label = tk.Label(root, text="Generated Password: ", bg='#e1f5fe', font=("Arial", 14))
password_label.pack(pady=20)

# Run the application
root.mainloop()
