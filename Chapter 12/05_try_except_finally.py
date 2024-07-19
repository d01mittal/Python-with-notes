try:
    a=int(input("Enter a number: "))
    c=1/a
except Exception as e:
    print(f"Exception is: {e}")
    exit()
finally:
    print("We are done")   # this will print every time, even the exccept contains 'exit()'
print("We are done fully") # this will not print if exception occurs