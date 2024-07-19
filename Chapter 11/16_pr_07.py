class vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1= ""
        index=0
        for i in self.vec:
            str1+=f"{i}a{index} + "
            index+=1
        return str1[:-2]
    def __add__(self,vec2):
        if len(self.vec)!=len(vec2.vec):
            return f"The lengths of two vectors are not same so addition can't perform"
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
        return vector(newlist)
    def __mul__(self,vec2):
        if len(self.vec)!=len(vec2.vec):
            return f"The lengths of two vectors are not same so multiplication can't perform"
        sum=0
        for i in range(len(self.vec)):
            sum+=self.vec[i]*vec2.vec[i]
        return sum
    def __len__(self):
        return len(self.vec)
v1=vector([1, 5, 9, 6])
v2=vector([5, 9, 8])
print("First vector is: ",v1)
print("Second vector is: ",v2)
print("Additon of both vectors is: ",v1+v2)
print("Dot product of both vectors is: ",v1*v2)
print(len(v1))
print(len(v2))