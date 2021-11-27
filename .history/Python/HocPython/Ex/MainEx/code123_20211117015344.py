def emailProcess(email):
    username_email = email[0:email.find('@')]
    domain_email = email[email.find('@')+1:]
    print(f"User name is: {username_email}")
    print(f"Domain name is: {domain_email}")
    return [domain_email, username_email]

def printMess(username_email,domain_email):
    print()
    
def main():
    email = input('Please enter your email: ').strip()
    print(f"Hello {email}")
    emailProcess(email)
    
if __name__ == '__main__':
    main()    