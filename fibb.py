def fibb(i):
    if i==0:
        return(0)
    elif i==1:
        return(1)
    else:
        return(fibb(i-1)+fibb(i-2))
n=int(input("Enter the number"))
for i in range(0,n):
    print(fibb(i))
    