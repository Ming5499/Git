from random import randrange


n=int(input('Nhap so phan tu'))
lst=[0]*n
for i in range(n):
    lst[i]=randrange(-100,100)
print(lst,end='\t)