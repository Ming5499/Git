import random
from faker import Faker
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Update the connection string as needed
db = client['mydb']  # Replace 'mydb' with your database name
collection = db['mycollection']  # Replace 'mycollection' with your collection name

# Create a Faker instance
fake = Faker()

# Define the number of fake records you want to generate
num_records = 100  # You can change this to the desired number of records

# Generate and insert fake data
for _ in range(num_records):
    fake_data = {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'phone_number': fake.phone_number(),
        'age': random.randint(18, 60),
    }

    collection.insert_one(fake_data)

print(f'{num_records} fake records inserted into MongoDB.')
