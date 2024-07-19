class complex:
    def __init__(self,num1,i):
        self.num1=num1
        self.icap=i
    def __add__(self,num2):
        super().__init__()
        return f"{self.num1 + num2.num1} + {self.icap + num2.icap}i"
    
    def __mul__(self,num2):
        super().__init__()
        return f"{(self.num1 * num2.num1)-(self.icap * num2.icap)} + {(self.num1 * num2.icap) + (self.icap * num2.num1)}i"
c=complex(3,2)
d=complex(1,7)
print(c+d)
print(c*d)