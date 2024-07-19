class employee:
    salary=5600
    salarybonus=500
    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
    @totalsalary.setter
    def totalsalary(self,val):
            self.salarybonus= val - self.salary
e=employee()
print(e.totalsalary)
e.totalsalary=6200
print(e.totalsalary)
print(e.salary)
print(e.salarybonus)