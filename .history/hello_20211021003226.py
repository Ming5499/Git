count=sum=0
print("Nhap 5 gia tri")
while count>5:
   val=int(input("Nhap gia tri"))

   sum=sum+val
   count=count+1
   if val<0:
      print("Nhap sai")
      break
   else:
      print("Trung binh cong:" , sum/count)

   
