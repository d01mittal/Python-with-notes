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
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
        return vector(newlist)
    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum+=self.vec[i]*vec2.vec[i]
        return sum
v1=vector([1, 5, 9])
v2=vector([5, 9, 8])
print("First vector is: ",v1)
print("Second vector is: ",v2)
print("Additon of both vectors is: ",v1+v2)
print("Dot product of both vectors is: ",v1*v2)