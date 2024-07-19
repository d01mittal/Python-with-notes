with open('this.txt') as f:
    c=f.read()
with open('copy.txt','w') as f:
    f.write(c)