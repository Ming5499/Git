import string
import random

LETTERS = string.ascii_letters
NUMBER = string.digits
PUNCTUATION = string.punctuation

print(LETTERS)

def password_generator(length=8):
    printable=f'{LETTERS}{NUMBER}{PUNCTUATION}'
    
    printable=list(printable)
    random.shuffle(printable)
    
    random_password= random.choices(printable,k=length )
    random_password = ''.join(random_password)
    return random_password

def main():
    password = password_generator()
    print(password)

if __name__ == '__main__':
    main()