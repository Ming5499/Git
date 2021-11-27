
from random import randrange


n=int(input('Moi ban nhap phan tu'))
lst=[0]*n
for i in range(n):
    lst[i] = randrange(-50,50)
print(lst)
print('x'*30)
print("Duyet theo Collection")
for i in lst:
    print(i,end='  ')
print('Duyet theo Index')
for i in range(len(lst)):
    print ('vi tri i:' , i ,'phan tu' ,lst[i])
print('Duyet nguoc :')
for i in range(len(lst)-1,-1,-1):
   print ('vi tri i:' , i ,'phan tu' ,lst[i]) 