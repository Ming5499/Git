def FN(m,n=0):
    s=0
    for i in range (1,m+n,1):
        s+=i
        return s
print(FN(5,1))