a= input("enter a number: ")
try:
    a=int(a)
    if a>6:
        print("your number is greater than 6")
except Exception as e:
    print(e)
    print("i")