def square(num):
    n=0
    if num<0:
        return False
    else:
        while n*n<=num:
            if n*n==num:
                return True
            n+=1
    return False
print(square(16))
