from code123 import emailProcess,printMess


def main():
    emails=['abc@example.com', 'bcam@example','bmc@yahoo.com']
    for email in emails:
        username_email,domain_email = emailProcess(email)
        printMess(username_email,domain_email)
    
    
if __name__ == '__main__':
    main() 
    