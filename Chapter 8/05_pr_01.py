num1=int(input("ENTER NUMBER 1: "))
num2=int(input("ENTER NUMBER 2: "))
num3=int(input("ENTER NUMBER 3: "))
def greatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
g=greatest(num1,num2,num3)
print("THE GREATEST AMONG THESE NUMBERS IS: ",g)