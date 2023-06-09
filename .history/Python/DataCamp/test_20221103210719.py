for i in range(10):
    print (i+1)

count = 0
for i in "Datacampa1a":
    if i == 'a':
        count = count +1
        print(count)

sequence = [1,2,8,100,200,'datacamp','tutorial']
for i in range(len(sequence)):
    print (sequence[i])

for i in range(len(sequence)):
    element = sequence[i]
    if type(element) == int:
        sequence[i] = element + 4
print(sequence)

for i in sequence:

    if type(i) == int:
        i = i + 4
print(sequence)

for i in range(11):
    for j in range(i):
        print (i, end=' ')
    print()

# Take user input
number = 2

# Condition of the while loop
while number < 5 :
    # Find the mod of 2
    if number%2 == 0:
        print("The number "+str(number)+" is even")
    else:
        print("The number "+str(number)+" is odd")

    # Increment `number` by 1
    number = number+1

#OOP
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age +=1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)
ozzy.doginfo()
skippy.doginfo()
filou.doginfo()

ozzy = Dog("Ozzy", 2)
print(ozzy.age)


#List
numbers = range(10)
# Initialize `new_list`
new_list = []

# Add values to `new_list`
for n in numbers:
    if n%2==0:
        new_list.append(n**2)

# Print `new_list`
print(new_list)

# Initialize the `kilometer` list
kilometer = [39.2, 36.5, 37.3, 37.8]

# Construct `feet` with `map()`
feet = map(lambda x: float(3280.8399)*x, kilometer)

# Print `feet` as a list
print(list(feet))

# Map the values of `feet` to integers
feet = list(map(int, feet))

# Filter `feet` to only include uneven distances
uneven = filter(lambda x: x%2, feet)

# Check the type of `uneven`
type(uneven)

# Print `uneven` as a list
print(list(uneven))