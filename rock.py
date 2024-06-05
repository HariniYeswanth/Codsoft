import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")
root.configure(bg='#e1f5fe')

# Initialize scores
user_score = 0
computer_score = 0

# Function to play the game
def play(user_choice):
    global user_score, computer_score
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    user_choice_label.config(text=f"User's Choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score - User: {user_score} Computer: {computer_score}")

# Function to reset the game
def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="User's Choice: ")
    computer_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="Result: ")
    score_label.config(text="Score - User: 0 Computer: 0")

# Labels to display choices and result
user_choice_label = tk.Label(root, text="User's Choice: ", bg='#e1f5fe', font=("Arial", 12))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer's Choice: ", bg='#e1f5fe', font=("Arial", 12))
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="Result: ", bg='#e1f5fe', font=("Arial", 14))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - User: 0 Computer: 0", bg='#e1f5fe', font=("Arial", 14))
score_label.pack(pady=20)

# Buttons for user to choose rock, paper, or scissors
button_frame = tk.Frame(root, bg='#e1f5fe')
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play('rock'), bg='#29b6f6', fg='white', font=("Arial", 12))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play('paper'), bg='#ef5350', fg='white', font=("Arial", 12))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play('scissors'), bg='#66bb6a', fg='white', font=("Arial", 12))
scissors_button.pack(side=tk.LEFT, padx=10)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset, bg='#9e9e9e', fg='white', font=("Arial", 12))
reset_button.pack(pady=20)

# Run the application
root.mainloop()
