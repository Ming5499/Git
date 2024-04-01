from faker import Faker
import csv

# Create a Faker instance
fake = Faker()

# Specify a directory path where you want to save the file
file_path = 'C:/Users/Admin/Desktop/VSCode/Git/fake_data.csv'


# Define the number of records you want to generate
num_records = 10

# Define the fields you want in your CSV
fields = ['name', 'age', 'address', 'sex', 'email', 'job']

# Generate fake data and save it to a CSV file
with open(file_path, 'w', newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
    csvwriter.writeheader()

    for _ in range(num_records):
        fake_data = {
            'name': fake.name(),
            'age': fake.random_int(min=18, max=65, step=1),
            'address': fake.address(),
            'sex': fake.random_element(elements=('Male', 'Female')),
            'email': fake.email(),
            'job': fake.job()
        }
        csvwriter.writerow(fake_data)

print(f'{num_records} fake records have been saved to fake_data.csv')
