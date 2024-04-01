from faker import Faker
import csv

# Create a Faker instance
fake = Faker()

# Define the number of records you want to generate in each batch
batch_size = 10000
num_batches = 20  # 100,000 records per batch * 50 batches = 5,000,000 records

# Define the fields you want in your CSV
fields = ['name', 'age', 'address', 'sex', 'email', 'job']

# Generate and save data in batches
for batch_num in range(num_batches):
    fake_data_list = []
    for _ in range(batch_size):
        fake_data = {
            'name': fake.name(),
            'age': fake.random_int(min=18, max=65, step=1),
            'address': fake.address(),
            'sex': fake.random_element(elements=('Male', 'Female')),
            'email': fake.email(),
            'job': fake.job()
        }
        fake_data_list.append(fake_data)

    # Define the CSV file name for each batch
    csv_file = f"fake_data_batch_{batch_num + 1}.csv"

    # Write the fake data to the CSV file for each batch
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        
        # Write the header
        writer.writeheader()
        
        # Write the data rows
        for fake_data in fake_data_list:
            writer.writerow(fake_data)

    print(f"Batch {batch_num + 1} saved to {csv_file}")

print("All batches generated and saved.")
