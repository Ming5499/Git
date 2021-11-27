s=float(input("Nhap gia tri"))
print("Ban nhap: ",s)
print(type(s))
def StrtoBool(s):
    return s.lower in ("true","yes")
x=input("Moi ban nhap True/False")
x=StrtoBool(x)
print(x)