from SanphamFile import *

masp=input('Nhap ma sp:')
tensp=input('Nhap ten sp:')
dongia=float(input('Nhap gia:'))
line=masp+';'+tensp+';'+str(dongia)
LuuFile('database.txt',line)