###RANGE() FUNCTION
for seq in range(10):
    print(seq)

for seq in range(5,10):
    print(seq)

for seq in range(50,1000,100):
    print(seq)

list1 = [2,4,6,8,10,12,14,16,18,20]
count = 0
for i in range(len(list1)):
    count = count + list1[i]
    print(count)
print('sum of the list:', count)

#PRINT
def value(items):
    for item in items:
        print(item, end=' ')

####DEF
def hello():
    name = str(input("Enter your name: "))
    if name:
        print("Hello " + str(name))
    else:
        print("Hello World")
    return


hello()
# Define `plus()` function to accept a variable number of arguments
def plus(*args):
  return sum(args)

# Calculate the sum
plus(1,4,5)

# Define `plus()` function to accept a variable number of arguments
def plus(*args):
  total = 0
  for i in args:
    total += i
  return total

# Calculate the sum
plus(20,30,40,50)

##lambda
double = lambda x: x*2

double(5)