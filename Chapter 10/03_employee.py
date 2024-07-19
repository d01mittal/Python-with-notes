class employee:
    company="google"
    salary=100
hari=employee()
mike=employee()
s=hari.company
t=mike.company
hari.salary=300
mike.salary=400
print(s)
print(t)
employee.company="youtube"
a=hari.company
b=mike.company
print(a)
print(b)
print(hari.salary)
print(mike.salary)