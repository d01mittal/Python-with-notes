temp=float(input("ENTER THE TEMPERATURE IN CELCIUS: "))
def conv(temp):
    f=temp*(9/5)+32
    return f
fa=conv(temp)
print("TEMPERATURE IN FAHRENHEIT",fa)