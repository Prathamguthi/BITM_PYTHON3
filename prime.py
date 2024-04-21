n=int(input("enter the no:"))
flag=False
if n==1:
    print("is not a prime no")
else:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
    if flag:
        print(n,"is not prime")
    else:
        print(n,"is prime")