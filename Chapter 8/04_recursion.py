n=int(input("ENTER A NUMBER: "))
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
f=fact(n)
print(f"THE FACTORIAL OF {n} is {f}")
    