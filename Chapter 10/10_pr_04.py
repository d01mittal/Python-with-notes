class calculator:
    def __init__(self,num):
        self.number=num
    @staticmethod
    def greet():
        print("hello")
    def square(self):
        print(f"the square of {self.number} is {self.number**2}")
    def squareroot(self):
        print(f"the squareroot of {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"the cube of {self.number} is {self.number**3}")

n=int(input("enter a number: "))
he=calculator(n)
he.greet()
he.square()
he.squareroot()
he.cube()