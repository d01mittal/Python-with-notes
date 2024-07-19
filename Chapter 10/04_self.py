class employee:
    company="google"
    def getsalary(self):
        print(f"salary of this employee in company {self.company} is 100k")
me=employee()
me.getsalary()    # employee.getsalary(me)