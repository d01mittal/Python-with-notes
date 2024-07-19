n=int(input("ENTER A NUMBER: "))
def sum(num):
    if num==1:
        return 1
    return num+sum(num-1)
a=sum(n)
print(f"THE SUM OF FIRST {n} NATURAL NUMBERS IS: {a}")