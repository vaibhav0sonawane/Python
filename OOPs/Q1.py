#create class take marks and name 3 sub and method to print average
class Student:
      def __init__(self,name,marks):
            self.name=name
            self.marks=marks
      @staticmethod #USED WHEN THERE IS NO NEED FOR SELF  PARAMETER(IT works at class lewvel)
      def marks_avg():
        marks=(s1.marks+s2.marks+s3.marks)/3
        print("avg of the total marks is:")
        return marks

s1=Student("vaibhav",81)
print(s1.marks)
s2=Student("varad",67)
print(s2.marks)
s3=Student("shubham",89)
print(s3.marks)
print(Student.marks_avg())