a=input("enter a string:")
c=0
c1=0
for i in a:
    if i.isdigit()==True:
        c+=1
print('Digits:',c)
for j in a:
    if j.isalpha()==True:
        c1+=1
print('Letters:',c1)
