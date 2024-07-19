# class employee:
#     company="DM"
#     salary=100
#     def changesalary(self,sl):
#         self.__class__.salary=sl
# e=employee()
# print(e.salary)
# e.changesalary(500)
# print(e.salary)
# print(employee.salary)

class employee:
    company="DM"
    salary=100
    @classmethod
    def changesalary(cls,sl):
        cls.salary=sl
e=employee()
print(e.salary)
e.changesalary(500)
print(e.salary)
print(employee.salary)