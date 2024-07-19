m1=int(input("ENTER THE MARKS OF SUBJECT 1: "))
m2=int(input("ENTER THE MARKS OF SUBJECT 2: "))
m3=int(input("ENTER THE MARKS OF SUBJECT 3: "))
tp=((m1+m2+m3)/300)*100
if(m1>=33 and m2>=33 and m3>=33):
    if(tp>=40):
        print("passed")
    else:
        print("failed")
else:
    print("failed")