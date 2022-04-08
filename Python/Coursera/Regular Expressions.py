import  re
x = 'My 2 favorite number are 19 and 24'
y = re.findall('[0-9]+',x)
print(y)
y=re.findall('[AEIOMfbNld]+',x)
print(y)

###########################################################
k ='From stephen.marge@uct.ac.za Sat Jun 5 09:14:16 2018'
y= re.findall('.\S+@\S+',k)
print(y)
y= re.findall('.\S+@\S?',k)
print(y)
atpos = k.find('@')
sppos = k.find(' ',atpos)
host=k[atpos+1:sppos]
print(host)


##############################################################
word = k.split()
email = word[1]
pieces = email.split('@')
print(pieces[1])
###############################################################
y=re.findall('@([^ ]*)',k)
print(y)
y=re.findall('^From .*@[^ ]*',k)
print(y)