def total(num):
    try:
        return int(num)+1
    except:
        raise ValueError("The value which is entered should be integer type")
a=total('dfg45')
print(a)
