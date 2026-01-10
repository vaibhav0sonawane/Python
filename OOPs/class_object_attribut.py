class Student:
    college_name="JSPM university"
    #class attribute:use to store common values and contain less space in the memory
    name="annonymous"#default name if name value not given
    def __init__(self,Fullname,marks):#it is a object attribute:use to store value of object like s1 ,s2
        self.name=Fullname
        self.mark=marks

s1=Student("vaibhav",71)
print(s1.name)
print(s1.mark)
print(Student.college_name)#class attribute print statement