
def doixung(s):
    flag=True
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            flag=False
            break
    return True
def main():
    s=input('Nhap chuoi')
    if doixung(s)==True:
        print('Chuoi doi xung')
    else:
        print('Chuoi khong doi xung')
    
while True:
    main()
    k=input(print('Tiep tuc khong'))
    if k=='k':
        break 
print('Tam biet')    

    
    
    