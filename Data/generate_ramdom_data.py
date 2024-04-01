import sqlite3
import random

# Connect to the SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('random_data.db')
cursor = conn.cursor()

# Create a table (change the schema to match your requirements)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS random_data (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
    )
''')

# Generate and insert random data into the table
for _ in range(100):  # Adjust the number of rows you want to insert
    name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
    age = random.randint(18, 65)
    email = f'{name}@example.com'

    cursor.execute("INSERT INTO random_data (name, age, email) VALUES (?, ?, ?)",
                   (name, age, email))

# Commit the changes to the database
conn.commit()
