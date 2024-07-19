try:
    a=int(input("enter a number: "))
    c=1/a
    print(c)
except ValueError as e:
    print("Make sure you are entering a valid value")
except ZeroDivisionError as e:
    print("Dividing by zero is not allowed")