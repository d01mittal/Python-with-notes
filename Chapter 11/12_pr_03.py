class employee:
    salary=5000
    increment=1000
    # def __init__(self):
    #     self.salary=salary
    #     self.increment=increment
    @property
    def totalsalary(self):
        return self.salary+self.increment
    @totalsalary.setter
    def totalsalary(self, val):
        self.increment=val-self.salary
e=employee()
print(e.totalsalary)
e.totalsalary=7000
print(e.increment)