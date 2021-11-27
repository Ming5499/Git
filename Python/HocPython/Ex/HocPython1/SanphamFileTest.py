from SanphamFile import *
def LuuFile(path,data):
    file=open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()
masp=input('Nhap ma sp:')
tensp=input('Nhap ten sp:')
dongia=float(input('Nhap gia:'))
line=masp+';'+tensp+';'+str(dongia)
LuuFile('database.txt',line)
dssp=DocFile('database.txt')
print(dssp)