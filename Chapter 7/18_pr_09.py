n=int(input("ENTER A NUMBER: "))
for i in range(1,n+1):
    if i==(n//2)+1:
        print("*" * (n-i),end="")
        print(" ",end="")
        print("*" * (n-i))
        continue
    print("*"*n)