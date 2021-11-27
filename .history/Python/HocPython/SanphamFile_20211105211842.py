def LuuFile(path,data):
    file=open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()
def DocFile(path):
    arrProduct=[]
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data = line.strip()
        arr=data.split(';')
        arrProduct.append(arr)
    file.close()
    return arrProduct
def SortSp(dssp)
    for i in range(len(dssp)):
        for j in range(len(dssp)):
            a=dssp[i]
            b=dssp[j]
            if a[2]>b[2]:
                dssp[i]=b
                dssp[j]=a
 