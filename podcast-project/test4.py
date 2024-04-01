import csv
from faker import Faker


# Create a Faker instance
fake = Faker()
# Define the number of rows of fake data to generate
num_rows = 100

def create_fake_customer_csv():
    # Define the full path and filename for the CSV file
    csv_file = "podcast-project/csv/customer_fake_data.csv"  # Replace with your desired path and filename
    # Define the CSV header
    csv_header = ["Name", "Age", "Address", "Phone", "Email"]
    # Generate fake data and write it to a CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(csv_header)
        # Generate and write fake data for each row
        for i in range(num_rows):
            name = fake.name()
            age = fake.random_int(min=18, max=99, step=1)
            address = fake.address()
            phone = fake.phone_number()
            email = fake.email()
            # Write the data to the CSV file
            writer.writerow([name, age, address, phone, email])

    print(f"Customer fake data saved to {csv_file}")
