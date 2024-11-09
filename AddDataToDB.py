import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Function to create a table with a specified name and columns
def create_table(table_name, columns):
    """
    Create a table with the given name and columns.
    :param table_name: Name of the table
    :param columns: Dictionary with column names as keys and data types as values
    """
    columns_with_types = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})")
    conn.commit()
    print(f"Table '{table_name}' created successfully.")

# Function to insert data into a specified table
def insert_data(table_name, data):
    """
    Insert data into the specified table.
    :param table_name: Name of the table
    :param data: Dictionary with column names as keys and corresponding values
    """
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?"] * len(data))
    values = tuple(data.values())
    cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values)
    conn.commit()
    print(f"Data inserted into '{table_name}' successfully.")

# Function to retrieve all data from a specified table
def get_all_data(table_name):
    """
    Retrieve all data from the specified table.
    :param table_name: Name of the table
    :return: List of tuples containing rows of data
    """
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

# Create a table for multiple-choice questions
create_table("multiple_choice_questions", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "question": "TEXT NOT NULL",
    "choice_a": "TEXT NOT NULL",
    "choice_b": "TEXT NOT NULL",
    "choice_c": "TEXT NOT NULL",
    "choice_d": "TEXT NOT NULL",
    "correct_answer": "TEXT NOT NULL"  # stores the correct choice (e.g., 'A', 'B', 'C', or 'D')
})

# Insert data into the multiple_choice_questions table
insert_data("multiple_choice_questions", {
    "question": "What is the capital of France?",
    "choice_a": "Berlin",
    "choice_b": "Madrid",
    "choice_c": "Paris",
    "choice_d": "Rome",
    "correct_answer": "C"
})
insert_data("multiple_choice_questions", {
    "question": "Which language is primarily used for iOS development?",
    "choice_a": "Java",
    "choice_b": "Kotlin",
    "choice_c": "Swift",
    "choice_d": "C#",
    "correct_answer": "C"
})

# Retrieve and print all questions and answers
all_questions = get_all_data("multiple_choice_questions")
for q in all_questions:
    print(f"Q: {q[1]}")
    print(f"A) {q[2]}")
    print(f"B) {q[3]}")
    print(f"C) {q[4]}")
    print(f"D) {q[5]}")
    print(f"Correct Answer: {q[6]}")
    print()

# Close the connection when done
conn.close()
