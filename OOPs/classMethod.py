#a method is bound to the class and recieves 
# the class as an implicites  first arrgument


#syntax:class student:
#  @class method
# def college(cls,name) :: here cls is class name is attribute of class
#        pass

#eg

class students:
    name:"anonymous"
    
    @classmethod
    def std_name(cls,name):
        cls.name=name

    def student(self,name):
        self.name=name

p1=students()
p1.std_name("Vaibhav sonawane")
print(students.name)
print(p1.name)


#tyoes of methods
"""1.static method :does not change any instince of class or object
2.class method(cls):we can change instince of a class using it
3.instance/init method(self):can change value of a constructor or a object"""