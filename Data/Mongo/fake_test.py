import random
from faker import Faker

fake = Faker()

def generate_fake_data():
    user_id = fake.uuid4()
    driver_id = fake.uuid4() if random.choice([True, False]) else None

    ride_1 = {
        "_id": "1",
        "user_id": user_id,
        "driver_id": driver_id,
        "start_location": fake.city(),
        "end_location": fake.city(),
        "status": random.choice(["completed", "pending"])
    }

    ride_2 = {
        "_id": "2",
        "user_id": user_id,
        "driver_id": driver_id,
        "start_location": fake.city(),
        "end_location": fake.city(),
        "status": random.choice(["completed", "pending"])
    }

    user_data = {
        "_id": user_id,
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(),
        "rides": [ride_1, ride_2]
    }

    return user_data

# Generate and display fake data
fake_data = generate_fake_data()
print(fake_data)
