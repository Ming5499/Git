def ToiUuChuoi(s):
    s2=s
    s2=s2.strip()
    arr=s2.split(' ')
    for i in arr:
        
        if len(i.split())!=0:
            s2=s2 + i + " "
    return s2.strip()
s='Tran    DUy Thanh '
print(s,len(s))
s=ToiUuChuoi(s)
print(s,len(s))