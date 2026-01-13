#defination:whr=en one class is 
# derive the properties and method of another class


"""Single  inheritance
class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stop...")
     
class tata(car):
    def __init__(self,name):
        self.name=name

car1=tata("tiago")
print(car1.start())"""


"""-------------------------############_--------------------------------"""


#multi-level inheritance

"""class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stop...")
     
class tata(car):
    def __init__(self,name):
        self.name=name

class Color(tata):
    def __init__(self, color):
        self.color=color
        print("color of car is :",car)
       
c1=Color("Brown")
print(c1.color)"""

"""-------------------------############_--------------------------------"""


#multiple inheritance
"""class A:
    varA="Welcome to class A"

class B:
    varB="Welcome to class B"

class C(A,B):
    varC="Welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)"""

"""-------------------------############_--------------------------------"""

#Super method
class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stop...")
     
class tata(car):
    def __init__(self,name):
        self.name = name

class Color(tata):
    def __init__(self, color):
        super().start()
        self.color=color
        
       
c1=Color("Brown")
print(c1.color)