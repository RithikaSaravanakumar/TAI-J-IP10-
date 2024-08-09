import tkinter as tk
from tkinter import messagebox
import random

# Question bank directly in the code
question_bank = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "Jane Austen", "Mark Twain", "J.K. Rowling"], "answer": "Harper Lee"},
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "H2", "HO2"], "answer": "H2O"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"}
]

# Global variables
score = 0
question_index = 0
time_left = 10  # 10 seconds per question
timer_running = False

# Functions
def start_quiz():
    global question_index, score, time_left, timer_running
    question_index = 0
    score = 0
    time_left = 10
    timer_running = True
    random.shuffle(question_bank)
    start_button.config(state="disabled")
    pause_button.config(state="normal")
    resume_button.config(state="disabled")
    load_question()
    countdown()

def load_question():
    global question_index
    if question_index < len(question_bank):
        question_label.config(text=question_bank[question_index]["question"])
        for i, option in enumerate(options):
            option.config(text=question_bank[question_index]["options"][i])
            option.config(command=lambda opt=option: check_answer(opt))
    else:
        end_quiz()

def check_answer(selected_option):
    global score, question_index, time_left
    if selected_option.cget("text") == question_bank[question_index]["answer"]:
        score += 1
    question_index += 1
    time_left = 10
    load_question()

def countdown():
    global time_left, timer_running
    if time_left > 0 and timer_running:
        time_left -= 1
        timer_label.config(text=f"Time left: {time_left}s")
        root.after(1000, countdown)
    elif timer_running:
        check_answer(tk.Label(root, text=""))

def end_quiz():
    global timer_running
    timer_running = False
    messagebox.showinfo("Quiz Finished", f"Your score is {score} out of {len(question_bank)}")
    start_button.config(state="normal")
    pause_button.config(state="disabled")
    resume_button.config(state="disabled")

def pause_quiz():
    global timer_running
    timer_running = False
    pause_button.config(state="disabled")
    resume_button.config(state="normal")

def resume_quiz():
    global timer_running
    timer_running = True
    resume_button.config(state="disabled")
    pause_button.config(state="normal")
    countdown()

# UI setup
root = tk.Tk()
root.title("Quiz Application")

question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack(pady=20)

options = [tk.Button(root, text="", font=("Arial", 14)) for _ in range(4)]
for option in options:
    option.pack(pady=5)

timer_label = tk.Label(root, text=f"Time left: {time_left}s", font=("Arial", 14))
timer_label.pack(pady=20)

start_button = tk.Button(root, text="Start Quiz", font=("Arial", 14), command=start_quiz)
start_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause Quiz", font=("Arial", 14), command=pause_quiz)
pause_button.pack(pady=10)
pause_button.config(state="disabled")

resume_button = tk.Button(root, text="Resume Quiz", font=("Arial", 14), command=resume_quiz)
resume_button.pack(pady=10)
resume_button.config(state="disabled")

# Run the application
root.mainloop()