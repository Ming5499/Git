filename = 'abc.txt'
file = open(filename,mode = 'r') # 'r' to read
text= file.read()
file.close()
print(text)

-------------------------------------------------------
#2
with open('abc', 'r') as file:
    print(file.read())