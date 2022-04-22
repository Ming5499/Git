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