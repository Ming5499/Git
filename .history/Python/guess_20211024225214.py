from random import randrange
result = randrange(1,101)
win=False
guess=0 
print(result)
while guess<7:
        guess+=1
        x=input('Nhap so tu 1 den 100: ')
        print('So lan doan:', guess)
        if x==result:
            print('Dung roi')
            win==True
            break
        if result>x:
            print('Lon hon')
        elif result<x: 
            print('Nho hon') 
if win==False:
    print('game over')
