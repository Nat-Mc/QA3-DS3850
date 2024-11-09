import sqlite3

# Function to create a new table for questions
def create_table(table_name):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Table '{table_name}' created successfully.")

# Function to insert questions into a specified table
def insert_questions(table_name, questions):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    
    # Insert questions into the specified table
    for question, option_a, option_b, option_c, option_d, answer in questions:
        cursor.execute(f'''
            INSERT INTO {table_name} (question, option_a, option_b, option_c, option_d, answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, option_a, option_b, option_c, option_d, answer))
    
    conn.commit()
    conn.close()
    print(f"Questions inserted into table '{table_name}' successfully.")

# List of questions and answers
questions = [
    ("What is the correct way to assign the integer 5 to a variable named x?", "x = 5", "5 = x", "int x = 5", "x == 5", "A"),
    ("Which of the following data types represents a sequence of characters?", "int", "str", "float", "bool", "B"),
    ("What will be the output of the following code: print(10 % 3)?", "0", "1", "2", "3", "B"),
    ("What is the correct syntax to define a function in Python?", "function myFunction():", "def myFunction():", "myFunction def():", "myFunction():", "B"),
    ("Which of the following is the correct way to access the third item in a list named myList?", "myList[3]", "myList[2]", "myList[1]", "myList(3)", "B"),
    ("What is the output of the following code?\n\nnumbers = [1, 2, 3, 4]\nnumbers.append(5)\nprint(numbers)", "[1, 2, 3, 4]", "[1, 2, 3, 4, 5]", "[1, 2, 3, 5]", "[1, 2, 3, 4, 0]", "B"),
    ("How do you access the value associated with the key name in a dictionary named person?", "person.name", "person['name']", "person(name)", "person{name}", "B"),
    ("What will be the result of bool('False') in Python?", "True", "False", "Error", "None", "A"),
    ("What does the len() function return?", "The number of characters in a string or elements in a list", "The sum of all elements in a list", "The last element of a list", "The index of the first item in a list", "A"),
    ("Given the dictionary my_dict = {'a': 1, 'b': 2, 'c': 3}, what will my_dict['b'] return?", "1", "2", "3", "None", "B")
]

# Example Usage
table_name = "DS3850"  # Specify your table name
create_table(table_name)  # Create the table if it does not exist
insert_questions(table_name, questions)  # Insert questions into the table
