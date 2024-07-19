try:
    a=int(input("Enter a number: "))
    c=1/a
except Exception as e:
    print(f"Exception is: {e}")
else:
    print("There is not any exception, code is successful")