d={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"item"
}
print("the options are",d.keys())
a=input("enter a hindi word\n")
# print("the meaning of this word is\t",d[a])
print("the meaning of this word is\t",d.get(a))