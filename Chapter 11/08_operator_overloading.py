class employee:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        return self.num + num2.num
    def __mul__(self,num2):
        return self.num * num2.num
e=employee(4)
f=employee(6)
print(e+f)
print(e*f)