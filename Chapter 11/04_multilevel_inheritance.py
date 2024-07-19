class person:
    country="india"
    salary="Rs. 1500000"
    @staticmethod
    def takebreadth():
        print("i am a person and i am breathing in this harsh world")

class employee(person):
    company="tata"
    def getsalary(self):
        print(f"the salary of the employee is {self.salary}")

class programmer(employee):
    company="google"
    def getsalary(self):
        print(f"no salary to the programmers but i want this salary {self.salary}")

p=person()
e=employee()
pr=programmer()
print(p.country)
print(p.salary)
p.takebreadth()
print(e.company)
e.getsalary()
print(pr.company)
pr.getsalary()