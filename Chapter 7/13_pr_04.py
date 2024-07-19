num=int(input("ENTER THE NUMBER: "))
a=0
if num==1:
    print("IT IS NOT A PRIME NUMBER")
elif num==0:
    print("IT IS NEITHER PRIME NOR COMPOSITE")
for i in range(2,num):
    n=num%i
    if(n==0):
        a=1
        break
if num!=1 and num!=0:
  if a==0:
    print("IT IS A PRIME NUMBER")
  else:
    print("IT IS NOT A PRIME NUMBER")