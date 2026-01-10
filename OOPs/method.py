class Student:
    def __init__(self,Fullname,marks):#method 1
        self.name=Fullname
        self.mark=marks

    def marks(self):
        return self.mark

s1=Student("vaibhav",71)#method 2
print(s1.name)
print(s1.mark)

s2=Student("Aniket",81)
print(s2.name)
print(s2.marks()) 
