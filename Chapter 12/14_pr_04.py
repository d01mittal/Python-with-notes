a=int(input("Enter an integer: "))
b=int(input("Enter an integer: "))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Infinite")