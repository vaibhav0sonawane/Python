class Student:
    #default constructor:contain only self
    def __init__(self,Fullname,marks):
        pass

    #parametric constructor:contain more values then self 
    def __init__(self,Fullname,marks):#here me is s1 object
        self.name=Fullname
        self.mark=marks

s1=Student("vaibhav",71)
print(s1.name)
print(s1.mark)

s2=Student("Aniket",81)
print(s2.name)
print(s2.mark) 