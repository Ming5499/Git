#%%
count=sum=0
print("nhap numberinput 5 gia tri")
while count<5:
   val=int(input(" vao gia tri"))

   sum=sum+val
   count=count+1
   if val<0:
      print("nhapwrong") 
      break
else:
    print("Trung binh cong:" , sum/count)

# %%
