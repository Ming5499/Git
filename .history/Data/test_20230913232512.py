from faker import Faker
import csv

# Create a Faker instance
fake = Faker()

# Define the number of records you want to generate
num_records = 10

# Define the fields you want in your CSV
fields = ['name', 'age', 'address', 'sex', 'email', 'job']

# Create a list to store the fake data dictionaries
fake_data_list = []

for _ in range(num_records):
    fake_data = {
        'name': fake.name(),
        'age': fake.random_int(min=18, max=65, step=1),
        'address': fake.address(),
        'sex': fake.random_element(elements=('Male', 'Female')),
        'email': fake.email(),
        'job': fake.job()
    }
    fake_data_list.append(fake_data)  # Append the generated fake data to the list

# Define the CSV file name
csv_file = "fake_data.csv"

# Write the fake data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    
    # Write the header
    writer.writeheader()
    
    # Write the data rows
    for fake_data in fake_data_list:
        writer.writerow(fake_data)

print(f"Fake data saved to {csv_file}")
