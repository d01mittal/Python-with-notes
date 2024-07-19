# def div(num):
#     if(num%5==0):
#         return True
#     else:
#         return False
div=lambda num:num%5==0
l=[5,6,7,8,9,10,15,16]
print(list(filter(div,l)))