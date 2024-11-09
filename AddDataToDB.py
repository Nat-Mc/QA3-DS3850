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
create_table("world_history", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "question": "TEXT NOT NULL",
    "choice_a": "TEXT NOT NULL",
    "choice_b": "TEXT NOT NULL",
    "choice_c": "TEXT NOT NULL",
    "choice_d": "TEXT NOT NULL",
    "correct_answer": "TEXT NOT NULL"  # stores the correct choice (e.g., 'A', 'B', 'C', or 'D')
})


insert_data("world_history", {
    "question": "What is the capital of France?",
    "choice_a": "Berlin",
    "choice_b": "Madrid",
    "choice_c": "Paris",
    "choice_d": "Rome",
    "correct_answer": "C"
})
insert_data("world_history", {
    "question": "Which language is primarily used for iOS development?",
    "choice_a": "Java",
    "choice_b": "Kotlin",
    "choice_c": "Swift",
    "choice_d": "C#",
    "correct_answer": "C"
})

# Retrieve and print all questions and answers
all_questions = get_all_data("world_history")
for q in all_questions:
    print(f"Q: {q[1]}")
    print(f"A) {q[2]}")
    print(f"B) {q[3]}")
    print(f"C) {q[4]}")
    print(f"D) {q[5]}")
    print(f"Correct Answer: {q[6]}")
    print()

# List of multiple-choice questions on famous historical events
questions_data = [
    {
        "question": "In which year did World War II end?",
        "choice_a": "1943",
        "choice_b": "1944",
        "choice_c": "1945",
        "choice_d": "1946",
        "correct_answer": "C"
    },
    {
        "question": "Who was the first man to step on the moon?",
        "choice_a": "Buzz Aldrin",
        "choice_b": "Neil Armstrong",
        "choice_c": "Yuri Gagarin",
        "choice_d": "Michael Collins",
        "correct_answer": "B"
    },
    {
        "question": "What year did the Berlin Wall fall?",
        "choice_a": "1987",
        "choice_b": "1988",
        "choice_c": "1989",
        "choice_d": "1990",
        "correct_answer": "C"
    },
    {
        "question": "Who was the first President of the United States?",
        "choice_a": "Thomas Jefferson",
        "choice_b": "Abraham Lincoln",
        "choice_c": "George Washington",
        "choice_d": "John Adams",
        "correct_answer": "C"
    },
    {
        "question": "In which country did the Industrial Revolution begin?",
        "choice_a": "France",
        "choice_b": "United Kingdom",
        "choice_c": "Germany",
        "choice_d": "United States",
        "correct_answer": "B"
    },
    {
        "question": "The Titanic sank in which year?",
        "choice_a": "1910",
        "choice_b": "1911",
        "choice_c": "1912",
        "choice_d": "1913",
        "correct_answer": "C"
    },
    {
        "question": "Which country was responsible for the invention of gunpowder?",
        "choice_a": "India",
        "choice_b": "Egypt",
        "choice_c": "China",
        "choice_d": "Greece",
        "correct_answer": "C"
    },
    {
        "question": "In what year did the American Civil War start?",
        "choice_a": "1860",
        "choice_b": "1861",
        "choice_c": "1862",
        "choice_d": "1863",
        "correct_answer": "B"
    },
    {
        "question": "What event triggered World War I?",
        "choice_a": "Invasion of Poland",
        "choice_b": "Sinking of Lusitania",
        "choice_c": "Assassination of Archduke Ferdinand",
        "choice_d": "Zimmermann Telegram",
        "correct_answer": "C"
    },
    {
        "question": "Who led India to independence from British rule?",
        "choice_a": "Jawaharlal Nehru",
        "choice_b": "Subhas Chandra Bose",
        "choice_c": "Mahatma Gandhi",
        "choice_d": "Sardar Patel",
        "correct_answer": "C"
    }
]

# Insert each question into the multiple_choice_questions table
for question in questions_data:
    insert_data("world_history", question)

# Retrieve and print all questions and answers to verify
all_questions = get_all_data("world_history")
for q in all_questions:
    print(f"Q: {q[1]}")
    print(f"A) {q[2]}")
    print(f"B) {q[3]}")
    print(f"C) {q[4]}")
    print(f"D) {q[5]}")
    print(f"Correct Answer: {q[6]}")
    print()

    # Create the intro_to_python_questions table
create_table("DS3850", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "question": "TEXT NOT NULL",
    "choice_a": "TEXT NOT NULL",
    "choice_b": "TEXT NOT NULL",
    "choice_c": "TEXT NOT NULL",
    "choice_d": "TEXT NOT NULL",
    "correct_answer": "TEXT NOT NULL"
})

# List of introductory Python questions
python_questions_data = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "choice_a": "def",
        "choice_b": "func",
        "choice_c": "define",
        "choice_d": "function",
        "correct_answer": "A"
    },
    {
        "question": "What is the output of 'print(type(5))' in Python?",
        "choice_a": "<class 'str'>",
        "choice_b": "<class 'int'>",
        "choice_c": "<class 'float'>",
        "choice_d": "<class 'bool'>",
        "correct_answer": "B"
    },
    {
        "question": "Which of the following is a correct way to start a comment in Python?",
        "choice_a": "//",
        "choice_b": "<!-- -->",
        "choice_c": "#",
        "choice_d": "/* */",
        "correct_answer": "C"
    },
    {
        "question": "What will 'print(2 ** 3)' output?",
        "choice_a": "5",
        "choice_b": "6",
        "choice_c": "8",
        "choice_d": "9",
        "correct_answer": "C"
    },
    {
        "question": "What is the correct way to create a list in Python?",
        "choice_a": "list = {1, 2, 3}",
        "choice_b": "list = (1, 2, 3)",
        "choice_c": "list = [1, 2, 3]",
        "choice_d": "list = <1, 2, 3>",
        "correct_answer": "C"
    },
    {
        "question": "What function is used to display output in Python?",
        "choice_a": "echo()",
        "choice_b": "print()",
        "choice_c": "write()",
        "choice_d": "display()",
        "correct_answer": "B"
    },
    {
        "question": "Which operator is used for floor division in Python?",
        "choice_a": "/",
        "choice_b": "//",
        "choice_c": "%",
        "choice_d": "**",
        "correct_answer": "B"
    },
    {
        "question": "What data type does the expression '3.14' have in Python?",
        "choice_a": "int",
        "choice_b": "float",
        "choice_c": "str",
        "choice_d": "bool",
        "correct_answer": "B"
    },
    {
        "question": "How do you create a variable in Python with the value 10?",
        "choice_a": "var = 10",
        "choice_b": "int var = 10",
        "choice_c": "10 = var",
        "choice_d": "let var = 10",
        "correct_answer": "A"
    },
    {
        "question": "Which function can convert a string '10' to an integer in Python?",
        "choice_a": "to_int('10')",
        "choice_b": "int('10')",
        "choice_c": "str(10)",
        "choice_d": "convert('10')",
        "correct_answer": "B"
    }
]


# Create the dbms_trivia table
create_table("DS3860", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "question": "TEXT NOT NULL",
    "choice_a": "TEXT NOT NULL",
    "choice_b": "TEXT NOT NULL",
    "choice_c": "TEXT NOT NULL",
    "choice_d": "TEXT NOT NULL",
    "correct_answer": "TEXT NOT NULL"
})

# List of multiple-choice questions related to database management systems
dbms_trivia_data = [
    {
        "question": "What is the full form of DBMS?",
        "choice_a": "Data Backup Management System",
        "choice_b": "Data Base Management System",
        "choice_c": "Database Maintenance System",
        "choice_d": "Data Management System",
        "correct_answer": "B"
    },
    {
        "question": "Which of the following is a DBMS model?",
        "choice_a": "Hierarchical Model",
        "choice_b": "Object-Oriented Model",
        "choice_c": "Network Model",
        "choice_d": "All of the above",
        "correct_answer": "D"
    },
    {
        "question": "What is a primary key in a DBMS?",
        "choice_a": "A field that uniquely identifies each record in a table",
        "choice_b": "A field that contains null values",
        "choice_c": "A field that holds large text values",
        "choice_d": "A field used for indexing",
        "correct_answer": "A"
    },
    {
        "question": "Which SQL statement is used to retrieve data from a table?",
        "choice_a": "SELECT",
        "choice_b": "INSERT",
        "choice_c": "UPDATE",
        "choice_d": "DELETE",
        "correct_answer": "A"
    },
    {
        "question": "In a relational DBMS, which is the relationship between tables?",
        "choice_a": "One-to-One",
        "choice_b": "One-to-Many",
        "choice_c": "Many-to-Many",
        "choice_d": "All of the above",
        "correct_answer": "D"
    },
    {
        "question": "Which SQL clause is used to filter records?",
        "choice_a": "ORDER BY",
        "choice_b": "HAVING",
        "choice_c": "WHERE",
        "choice_d": "SELECT",
        "correct_answer": "C"
    },
    {
        "question": "What is normalization in DBMS?",
        "choice_a": "Process of converting data into a logical format",
        "choice_b": "Process of organizing data to reduce redundancy",
        "choice_c": "Process of compressing data",
        "choice_d": "Process of indexing data",
        "correct_answer": "B"
    },
    {
        "question": "Which of the following is NOT a type of DBMS?",
        "choice_a": "Hierarchical DBMS",
        "choice_b": "Relational DBMS",
        "choice_c": "Network DBMS",
        "choice_d": "Object-oriented OS",
        "correct_answer": "D"
    },
    {
        "question": "What is the purpose of the 'JOIN' operation in SQL?",
        "choice_a": "To combine multiple tables into one",
        "choice_b": "To filter data",
        "choice_c": "To sort data",
        "choice_d": "To update data in a table",
        "correct_answer": "A"
    },
    {
        "question": "Which command is used to create a new table in SQL?",
        "choice_a": "CREATE TABLE",
        "choice_b": "MAKE TABLE",
        "choice_c": "NEW TABLE",
        "choice_d": "BUILD TABLE",
        "correct_answer": "A"
    }
]

# Create the rock_band_trivia table
create_table("rock_band_trivia", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "question": "TEXT NOT NULL",
    "choice_a": "TEXT NOT NULL",
    "choice_b": "TEXT NOT NULL",
    "choice_c": "TEXT NOT NULL",
    "choice_d": "TEXT NOT NULL",
    "correct_answer": "TEXT NOT NULL"
})

# List of multiple-choice questions related to classic rock bands
rock_band_trivia_data = [
    {
        "question": "Which band is known for the hit song 'Stairway to Heaven'?",
        "choice_a": "The Doors",
        "choice_b": "Pink Floyd",
        "choice_c": "Led Zeppelin",
        "choice_d": "Queen",
        "correct_answer": "C"
    },
    {
        "question": "Who was the lead singer of Queen?",
        "choice_a": "David Bowie",
        "choice_b": "Freddie Mercury",
        "choice_c": "Robert Plant",
        "choice_d": "Mick Jagger",
        "correct_answer": "B"
    },
    {
        "question": "Which band released the album 'Dark Side of the Moon'?",
        "choice_a": "The Beatles",
        "choice_b": "Pink Floyd",
        "choice_c": "The Rolling Stones",
        "choice_d": "The Who",
        "correct_answer": "B"
    },
    {
        "question": "Which band performed the iconic song 'Smoke on the Water'?",
        "choice_a": "The Who",
        "choice_b": "Deep Purple",
        "choice_c": "AC/DC",
        "choice_d": "Led Zeppelin",
        "correct_answer": "B"
    },
    {
        "question": "Which classic rock band is famous for the song 'Hotel California'?",
        "choice_a": "The Rolling Stones",
        "choice_b": "The Eagles",
        "choice_c": "Lynyrd Skynyrd",
        "choice_d": "Fleetwood Mac",
        "correct_answer": "B"
    },
    {
        "question": "Which rock band released 'The Wall' album in 1979?",
        "choice_a": "AC/DC",
        "choice_b": "The Rolling Stones",
        "choice_c": "The Beatles",
        "choice_d": "Pink Floyd",
        "correct_answer": "D"
    },
    {
        "question": "Who is known as the 'Godfather of Punk'?",
        "choice_a": "Johnny Rotten",
        "choice_b": "Joey Ramone",
        "choice_c": "Iggy Pop",
        "choice_d": "Jim Morrison",
        "correct_answer": "C"
    },
    {
        "question": "Which band was originally known as 'The New Yardbirds'?",
        "choice_a": "Led Zeppelin",
        "choice_b": "The Rolling Stones",
        "choice_c": "The Who",
        "choice_d": "The Kinks",
        "correct_answer": "A"
    },
    {
        "question": "Which band performed the song 'Born to Run'?",
        "choice_a": "Bruce Springsteen and the E Street Band",
        "choice_b": "The Rolling Stones",
        "choice_c": "The Clash",
        "choice_d": "U2",
        "correct_answer": "A"
    },
    {
        "question": "What was the original name of the band 'The Beatles'?",
        "choice_a": "The Quarrymen",
        "choice_b": "The Yardbirds",
        "choice_c": "The Skiffle Kings",
        "choice_d": "The Rolling Stones",
        "correct_answer": "A"
    }
]

# Insert the rock band trivia questions into the rock_band_trivia table
for question in rock_band_trivia_data:
    insert_data("rock_band_trivia", question)

# Retrieve and print all rock band trivia questions and answers to verify
all_rock_band_trivia = get_all_data("rock_band_trivia")
for q in all_rock_band_trivia:
    print(f"Q: {q[1]}")
    print(f"A) {q[2]}")
    print(f"B) {q[3]}")
    print(f"C) {q[4]}")
    print(f"D) {q[5]}")
    print(f"Correct Answer: {q[6]}")
    print()


# Create the movie_trivia table
create_table("movie_trivia", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "question": "TEXT NOT NULL",
    "choice_a": "TEXT NOT NULL",
    "choice_b": "TEXT NOT NULL",
    "choice_c": "TEXT NOT NULL",
    "choice_d": "TEXT NOT NULL",
    "correct_answer": "TEXT NOT NULL"
})

# List of multiple-choice questions related to movies
movie_trivia_data = [
    {
        "question": "Who directed the movie 'Jaws'?",
        "choice_a": "Steven Spielberg",
        "choice_b": "George Lucas",
        "choice_c": "Martin Scorsese",
        "choice_d": "Francis Ford Coppola",
        "correct_answer": "A"
    },
    {
        "question": "Which movie won the Academy Award for Best Picture in 1994?",
        "choice_a": "The Shawshank Redemption",
        "choice_b": "Forrest Gump",
        "choice_c": "Pulp Fiction",
        "choice_d": "The Lion King",
        "correct_answer": "B"
    },
    {
        "question": "Which actor played the character of 'Jack Dawson' in Titanic?",
        "choice_a": "Johnny Depp",
        "choice_b": "Brad Pitt",
        "choice_c": "Leonardo DiCaprio",
        "choice_d": "Tom Cruise",
        "correct_answer": "C"
    },
    {
        "question": "What is the name of the fictional African country in the movie 'Black Panther'?",
        "choice_a": "Wakanda",
        "choice_b": "Zamunda",
        "choice_c": "Genovia",
        "choice_d": "Elbonia",
        "correct_answer": "A"
    },
    {
        "question": "Which movie features the quote 'May the Force be with you'?",
        "choice_a": "Star Trek",
        "choice_b": "Star Wars",
        "choice_c": "The Matrix",
        "choice_d": "Avatar",
        "correct_answer": "B"
    },
    {
        "question": "Which actor starred as the titular character in the movie 'The Godfather'?",
        "choice_a": "Al Pacino",
        "choice_b": "Marlon Brando",
        "choice_c": "Robert De Niro",
        "choice_d": "Jack Nicholson",
        "correct_answer": "B"
    },
    {
        "question": "What year was the movie 'The Matrix' released?",
        "choice_a": "1997",
        "choice_b": "1998",
        "choice_c": "1999",
        "choice_d": "2000",
        "correct_answer": "C"
    },
    {
        "question": "Which movie is known for the line 'Here's looking at you, kid'?",
        "choice_a": "Gone with the Wind",
        "choice_b": "Casablanca",
        "choice_c": "Citizen Kane",
        "choice_d": "The Godfather",
        "correct_answer": "B"
    },
    {
        "question": "Who played the character of 'Forrest Gump'?",
        "choice_a": "Tom Hanks",
        "choice_b": "Brad Pitt",
        "choice_c": "Matt Damon",
        "choice_d": "Johnny Depp",
        "correct_answer": "A"
    },
    {
        "question": "What movie is the quote 'I'll be back' from?",
        "choice_a": "RoboCop",
        "choice_b": "The Terminator",
        "choice_c": "Die Hard",
        "choice_d": "Predator",
        "correct_answer": "B"
    }
]

# Insert the movie trivia questions into the movie_trivia table
for question in movie_trivia_data:
    insert_data("movie_trivia", question)

# Retrieve and print all movie trivia questions and answers to verify
all_movie_trivia = get_all_data("movie_trivia")
for q in all_movie_trivia:
    print(f"Q: {q[1]}")
    print(f"A) {q[2]}")
    print(f"B) {q[3]}")
    print(f"C) {q[4]}")
    print(f"D) {q[5]}")
    print(f"Correct Answer: {q[6]}")
    print()

# Close the connection when done
conn.close()

