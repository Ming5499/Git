from random import randrange


n=int(input('Nhap so phan tu')) 
lst=[0]*n
for i in range(n):
    lst[i]=randrange(1,5)
print('List la:')
print(lst,end='\t')

k=int(input())
while lst.count(k)>0:
    lst.remove(k)
print()
print(lst)

def CheckDoiXung(lst):
    for i in range(len(lst)):
        if lst[i]!=lst[len(lst)-i-1]:
            return False
        return True

kt=CheckDoiXung(lst)
if kt==True:
    print('Ham doi xung')
else:
    print('ham khong doi xung')
        
    
    
"""dem=lst.count(k)
print(k,'xuat hien',dem,'lan')

def timSoNguyenTo(n):
    dem=0
    for i in range(1,n+1):
        if n%i==0:
            dem+=1
    return d==2
demnt=0
tongnt=0
for i in lst:
    if timSoNguyenTo(i):
        demnt+=1
        tongnt+=i
print(tongnt)"""

lst2=sorted(lst)
