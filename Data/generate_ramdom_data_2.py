from faker import Faker
import sqlite3

fake = Faker()

conn = sqlite3.connect('random_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS random_data (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
    )
''')

for _ in range(100):
    name = fake.name()
    age = fake.random_int(min=18, max=65)
    email = fake.email()

    cursor.execute("INSERT INTO random_data (name, age, email) VALUES (?, ?, ?)",
                   (name, age, email))

conn.commit()
