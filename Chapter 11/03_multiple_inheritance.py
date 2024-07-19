class employee:
    company="google"
    @staticmethod
    def symbol():
        print("the symbol is GOOGLE")

class clerk:
    company="axis bank"
    @staticmethod
    def cash():
        print("the total cash is in trillions")

class program(employee,clerk):
    company="tata"
    @staticmethod
    def salt():
        print("salt is very pure")

hello=program()
print(hello.company)
hello.symbol()
hello.cash()
hello.salt()