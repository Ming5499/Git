from faker import Faker
import csv

# Create a Faker instance
fake = Faker()

# Define the number of records you want to generate
num_records = 10

# Define the fields you want in your CSV
fields = ['name', 'age', 'address', 'sex', 'email', 'job']


for _ in range(num_records):
    fake_data = {
            'name': fake.name(),
            'age': fake.random_int(min=18, max=65, step=1),
            'address': fake.address(),
            'sex': fake.random_element(elements=('Male', 'Female')),
            'email': fake.email(),
            'job': fake.job()
        }
    print(num_records) 

