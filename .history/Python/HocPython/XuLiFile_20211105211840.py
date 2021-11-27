def LuuFile(path):
    file=open(path,'w',encoding='utf8')
    file.writelines('SV1;NguyenVanA;1998')
    file.writelines('SV1;NguyenVanA;1998')
    file.writelines('SV1;NguyenVanA;1998')
    file.close()
LuuFile("csdl.txt")