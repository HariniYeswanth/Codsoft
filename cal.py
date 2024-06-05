import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")
root.configure(bg='#e1f5fe')

# Entry widget for the first number
first_number_label = tk.Label(root, text="First Number:", bg='#e1f5fe', font=("Arial", 12))
first_number_label.pack(pady=10)
first_number_entry = tk.Entry(root, width=30)
first_number_entry.pack(pady=5)

# Entry widget for the second number
second_number_label = tk.Label(root, text="Second Number:", bg='#e1f5fe', font=("Arial", 12))
second_number_label.pack(pady=10)
second_number_entry = tk.Entry(root, width=30)
second_number_entry.pack(pady=5)

# Function to perform the arithmetic operations
def calculate(operation):
    try:
        num1 = float(first_number_entry.get())
        num2 = float(second_number_entry.get())
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                messagebox.showwarning("Warning", "Division by zero is not allowed.")
                return
            result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showwarning("Warning", "Please enter valid numbers.")

# Function to reset the entries and result label
def reset():
    first_number_entry.delete(0, tk.END)
    second_number_entry.delete(0, tk.END)
    result_label.config(text="Result: ")

# Buttons for the arithmetic operations
button_frame = tk.Frame(root, bg='#e1f5fe')
button_frame.pack(pady=20)

add_button = tk.Button(button_frame, text="Add", command=lambda: calculate('add'), bg='#29b6f6', fg='white', font=("Arial", 12))
add_button.pack(side=tk.LEFT, padx=10)

subtract_button = tk.Button(button_frame, text="Subtract", command=lambda: calculate('subtract'), bg='#ef5350', fg='white', font=("Arial", 12))
subtract_button.pack(side=tk.LEFT, padx=10)

multiply_button = tk.Button(button_frame, text="Multiply", command=lambda: calculate('multiply'), bg='#66bb6a', fg='white', font=("Arial", 12))
multiply_button.pack(side=tk.LEFT, padx=10)

divide_button = tk.Button(button_frame, text="Divide", command=lambda: calculate('divide'), bg='#ffca28', fg='white', font=("Arial", 12))
divide_button.pack(side=tk.LEFT, padx=10)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset, bg='#9e9e9e', fg='white', font=("Arial", 12))
reset_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(root, text="Result: ", bg='#e1f5fe', font=("Arial", 14))
result_label.pack(pady=20)

# Run the application
root.mainloop()
