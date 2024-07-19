a1=int(input("enter number 1: "))
a2=int(input("enter number 2: "))
a3=int(input("enter number 3: "))
a4=int(input("enter number 4: "))
if(a1>a4):
    f1=a1
else:
    f1=a4
if(a2>a3):
    f2=a2
else:
    f2=a3
if(f1>f2):
    print(f1," is the gratest")
else:
    print(f2," is the gratest")