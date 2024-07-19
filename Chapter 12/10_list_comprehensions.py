a=[1, 3, 5, 6, 8, 68, 123, 126]
j=[1, 7, 12, 11, 22]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)
b=[i for i in j if i>8]
print(b)
c=[i for i in a if i>8]
print(c)