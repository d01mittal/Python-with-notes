class person:
    country="india"
    salary="Rs. 1500000"
    @staticmethod
    def takebreadth():
        print("i am a person and i am breathing in this harsh world")

class employee(person):
    company="tata"
    def takebreadth(self):
        super().takebreadth()
        print(f"the salary of the employee is {self.salary}")

class programmer(employee):
    company="google"
    def takebreadth(self):
        super().takebreadth()
        print(f"no salary to the programmers but i want this salary {self.salary}")

p=person()
p.takebreadth()

e=employee()
e.takebreadth()

pr=programmer()
pr.takebreadth()