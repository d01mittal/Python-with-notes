marks=int(input("enter the marks of the student"))
if(marks>90 and marks<=100):
    print("the grade of the student is EX")
elif(marks>80 and marks<=90):
    print("the grade of the student is A")
elif(marks>70 and marks<=80):
    print("the grade of the student is B")
elif(marks>60 and marks<=70):
    print("the grade of the student is C")
elif(marks>=50 and marks<=60):
    print("the grade of the student is D")
else:
    print("the grade of the student is F")