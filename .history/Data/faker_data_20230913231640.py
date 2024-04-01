from faker import Faker
fake = Faker(locale='cn')
print (fake.email())
print(fake.country())
print(fake.name())
print(fake.text())
print(fake.latitude(), fake.longitude())
print(fake.url())
