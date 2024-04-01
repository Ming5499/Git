import csv
from faker import Faker

# Create a Faker instance
fake = Faker()

# Define the number of rows of fake data to generate
num_rows = 100

# Define the CSV file name
csv_file = "fake_data.csv"

# Define the CSV header
csv_header = ["Name", "Age", "Address", "Sex", "Email", "Job"]

# Generate fake data and write it to a CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(csv_header)
    
    # Generate and write fake data for each row
    for _ in range(num_rows):
        name = fake.name()
        age = fake.random_int(min=18, max=99, step=1)
        address = fake.address()
        sex = fake.random_element(elements=("Male", "Female"))
        email = fake.email()
        job = fake.job()
        
        # Write the data to the CSV file
        writer.writerow([name, age, address, sex, email, job])

print(f"Fake data saved to {csv_file}")
