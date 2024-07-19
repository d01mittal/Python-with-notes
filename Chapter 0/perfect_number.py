def per(num):
    n=1
    if num<=0:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                n+=i
        if n==num:
            return True
num=int(input("Enter a number: "))
a=per(num)
if a is True:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")