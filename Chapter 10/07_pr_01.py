class programmer:
    company="google"
    def __init__(self,name,work):
        self.name=name
        self.work=work
    def getinfo(self):
        print(f"the name of the employee of company {self.company} is {self.name} and work in {self.work}")
hello=programmer("DM","Google")
hello.getinfo()
bye=programmer("SK","YOUTUBE")
bye.getinfo()