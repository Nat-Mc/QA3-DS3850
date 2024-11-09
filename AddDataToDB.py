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

# Example usage
# Create a table for questions and answers
create_table("questions_answers", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "question": "TEXT NOT NULL",
    "answer": "TEXT NOT NULL"
})

# Insert data into questions_answers table
insert_data("questions_answers", {
    "question": "What is Python?",
    "answer": "Python is a programming language."
})
insert_data("questions_answers", {
    "question": "What is SQLite?",
    "answer": "SQLite is a lightweight database library."
})

# Retrieve and print all questions and answers
all_qa = get_all_data("questions_answers")
for qa in all_qa:
    print(f"Q: {qa[1]}")
    print(f"A: {qa[2]}")
    print()

# Close the connection when done
conn.close()
