while True:
    print("Nhap 1 so")
    n=int(input())
    dem = 0
    for i in range(1,n+1):
        if n%1 ==0:
            dem+=1
        if(dem==2):
            print(n,'la so nguyen to')
        else:
            print(n,'khong phai la so nguyen to')
        print
        
        