import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the SQLite database
def connect_db():
    conn = sqlite3.connect('questions.db')
    return conn

# Function to fetch questions from a specific table
def fetch_questions(table_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT question, answer FROM {table_name}")
    questions = cursor.fetchall()
    conn.close()
    return questions

# Function to display a question and allow the user to answer
def show_question(table_name):
    questions = fetch_questions(table_name)
    
    # Function to check the user's answer
    def check_answer():
        user_answer = answer_entry.get()
        correct_answer = questions[question_index][1]
        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"The correct answer is: {correct_answer}")

    # Setup the window
    window = tk.Tk()
    window.title(f"Trivia - {table_name}")
    
    # Initialize the question index
    question_index = 0
    
    # Display the current question
    question_label = tk.Label(window, text=questions[question_index][0], font=('Arial', 14))
    question_label.pack(pady=20)
    
    # Entry widget for the user's answer
    answer_entry = tk.Entry(window, font=('Arial', 12))
    answer_entry.pack(pady=10)
    
    # Button to check the answer
    check_button = tk.Button(window, text="Check Answer", font=('Arial', 12), command=check_answer)
    check_button.pack(pady=10)

    # Button to move to the next question
    def next_question():
        nonlocal question_index
        question_index += 1
        if question_index < len(questions):
            question_label.config(text=questions[question_index][0])
            answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("End of Questions", "You've reached the end of the questions!")
            window.quit()

    next_button = tk.Button(window, text="Next Question", font=('Arial', 12), command=next_question)
    next_button.pack(pady=10)
    
    # Start the Tkinter loop
    window.mainloop()

# Example to start the trivia game with a specific table
if __name__ == "__main__":
    # Change the table name to whatever you want to start with
    show_question("world_history")
