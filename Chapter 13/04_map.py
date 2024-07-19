# def square(num):
#     return num*num
square=lambda num:num*num
l=[1,8,7]
# l2=[i*i for i in l ]
# print(l2)
print(list(map(square,l)))