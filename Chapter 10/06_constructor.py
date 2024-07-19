class Greet:
    def __init__(self,name):
        self.name=name
        print("employee is created!",name)
    @staticmethod
    def greet():
        print("good morning sir")
    @staticmethod
    def time():
        print("the time is 9am in the morning")
hello=Greet("dm")
hello.greet()
hello.time()