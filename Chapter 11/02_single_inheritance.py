class employee:
    company="google"
    @staticmethod
    def showdetails():
        print("this is an employee")
class programmer(employee):
    company="youtube"
    language="python"
    def getlang(self):
        print(f"the language is {self.language}")
    @staticmethod
    def showdetails():
        print("this is a programmer")
hello=programmer()
bye=employee()
bye.showdetails()
print(hello.company)
print(bye.company)
hello.getlang()
hello.showdetails()