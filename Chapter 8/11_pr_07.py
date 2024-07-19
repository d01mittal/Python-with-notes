def remove(string,word):
    new=string.replace(word,"")
    return new.strip()
s="     HI I AM GOOD     "
a=remove(s,"GOOD")
print(a)