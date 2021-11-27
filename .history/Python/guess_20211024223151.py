import random

result = random.randint(1,100)
    guess=0 
    while guess<7:
        guess+=1
        x=int(input('Nhap so tu 1 den 100: ')) 
        print('So lan doan:', guess)
        if x=reuslt:
            print('Dung roi')
            break
        elif x>result:
            print('Lon hon')
        elif x<result:
            print('Nho hon')           
print('game over')
